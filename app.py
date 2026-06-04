import streamlit as st
import torch
import google.generativeai as genai
from transformers import pipeline
import re
import time
import urllib.parse
import calendar
from datetime import datetime, date
from diffusers import StableDiffusionPipeline


st.set_page_config(page_title="Assistente MIO", layout="wide")


genai.configure(api_key="sua chave api aqui")


@st.cache_resource
def load_sentiment_model():
    return pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

@st.cache_resource
def load_image_model():
    model_id = "runwayml/stable-diffusion-v1-5"
    device = "cuda" if torch.cuda.is_available() else "cpu"
    pipe = StableDiffusionPipeline.from_pretrained(
        model_id,
        torch_dtype=torch.float16 if device == "cuda" else torch.float32
    )
    return pipe.to(device)

def clean_prompt(text):
    cleaned = re.sub(r'[^\w\s]', '', text)
    return cleaned[:100]

classifier = load_sentiment_model()
image_pipe = load_image_model()
gemini_model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    system_instruction="Você é a MIO, uma assistente terapêutica. Seu objetivo é ajudar o usuário a explorar seus sentimentos."
)


if "usuarios_db" not in st.session_state:
    st.session_state.usuarios_db = {"Duda": "1234"}
if "terapeutas_db" not in st.session_state:
    st.session_state.terapeutas_db = {"12345": "admin"} # CRP: Senha

if "autenticado" not in st.session_state: st.session_state.autenticado = False
if "historico_conversa" not in st.session_state: st.session_state.historico_conversa = []
if "meus_relatorios" not in st.session_state: st.session_state.meus_relatorios = []
if "historico_humor" not in st.session_state: st.session_state.historico_humor = {}
if "modo_terapeuta" not in st.session_state: st.session_state.modo_terapeuta = False
if "tela_atual" not in st.session_state: st.session_state.tela_atual = "login" # login, cadastro_user, cadastro_terapeuta
if "usuario_atual" not in st.session_state: st.session_state.usuario_atual = None



def exibir_calendario_humor():
    st.markdown("### 📅 Calendário de Humor")
    hoje = date.today()
    cal = calendar.Calendar(firstweekday=6)
    semanas = cal.monthdatescalendar(hoje.year, hoje.month)
    cols_header = st.columns(7)
    for i, nome_dia in enumerate(["Dom", "Seg", "Ter", "Qua", "Qui", "Sex", "Sáb"]):
        cols_header[i].caption(nome_dia)
    for semana in semanas:
        cols = st.columns(7)
        for i, dia in enumerate(semana):
            if dia.month == hoje.month:
                data_str = dia.strftime("%Y-%m-%d")
                humor = st.session_state.historico_humor.get(data_str, "")
                emoji = "😊" if humor == "POSITIVE" else "😔" if humor == "NEGATIVE" else ""
                with cols[i]:
                    st.write(f"**{dia.day}**")
                    if emoji: st.write(emoji)
            else:
                cols[i].write("")

@st.dialog("Relatório do Dia", width="large")
def modal_relatorio():
    st.write("### 📝 Reflexão Diária")
    with st.form("form_relatorio", clear_on_submit=True):
        data_relatorio = st.date_input("Data", value=date.today())
        titulo = st.text_input("Título do dia")
        conteudo = st.text_area("O que aconteceu hoje?", height=200)
        enviar = st.form_submit_button("Salvar Relatório", use_container_width=True)
        if enviar and conteudo:
            analise = classifier(conteudo[:512])[0]
            st.session_state.historico_humor[data_relatorio.strftime("%Y-%m-%d")] = analise['label']
            st.session_state.meus_relatorios.append({
                "usuario": st.session_state.usuario_atual,
                "data": data_relatorio,
                "titulo": titulo,
                "texto": conteudo,
                "humor": analise['label']
            })
            st.success("Relatório salvo!")
            time.sleep(1)
            st.rerun()

@st.dialog("MIO", width="large")
def modal_mio():
    tab1, tab2 = st.tabs(["Sentimento", "Conversa"])
    with tab1:
        st.subheader("Qual seu humor hoje?")
        sentiment_input = st.text_input("Como você se sente?")
        if st.button("Analisar Humor"):
            if sentiment_input:
                res = classifier(sentiment_input)[0]
                st.session_state.historico_humor[date.today().strftime("%Y-%m-%d")] = res['label']
                st.info(f"Sentimento registrado: {'😊' if res['label'] == 'POSITIVE' else '😔'}")
                st.rerun()
    with tab2:
        container_chat = st.container(height=400)
        with container_chat:
            for chat in st.session_state.historico_conversa:
                with st.chat_message("user"): st.write(chat["pergunta"])
                with st.chat_message("assistant"):
                    st.write(chat["resposta"])
                    if chat.get("imagem"): st.image(chat["imagem"], width=400)
        with st.form("chat_form", clear_on_submit=True):
            user_input = st.text_input("Diga algo:")
            if st.form_submit_button("Enviar") and user_input:
                try:
                    res_gemini = gemini_model.generate_content(user_input)
                    img = image_pipe(prompt=f"Digital art, {clean_prompt(res_gemini.text)}", num_inference_steps=20).images[0]
                    st.session_state.historico_conversa.append({"pergunta": user_input, "resposta": res_gemini.text, "imagem": img})
                    st.rerun()
                except Exception as e:
                    st.error(f"Erro: {e}")



def tela_cadastro_terapeuta():
    empty_l, center_col, empty_r = st.columns([1, 1.5, 1])
    with center_col:
        st.markdown("<h2 style='text-align: center;'>CADASTRO DE TERAPEUTA</h2>", unsafe_allow_html=True)
        with st.form("form_reg_terapeuta"):
            novo_crp = st.text_input("Registro Profissional (CRP/CRM)")
            nova_senha = st.text_input("Defina uma Senha", type="password")
            confirmar = st.text_input("Confirme a Senha", type="password")
            if st.form_submit_button("Finalizar Cadastro", use_container_width=True):
                if novo_crp in st.session_state.terapeutas_db:
                    st.error("Este registro já está cadastrado.")
                elif nova_senha != confirmar:
                    st.error("As senhas não conferem.")
                elif novo_crp and nova_senha:
                    st.session_state.terapeutas_db[novo_crp] = nova_senha
                    st.success("Terapeuta cadastrado com sucesso!")
                    time.sleep(1)
                    st.session_state.tela_atual = "login"
                    st.rerun()
        if st.button("Voltar"):
            st.session_state.tela_atual = "login"
            st.rerun()

def login_terapeuta():
    st.markdown("## 🩺 Acesso Profissional")
    with st.form("form_terapeuta"):
        registro = st.text_input("CRP/CRM")
        senha_t = st.text_input("Senha", type="password")
        if st.form_submit_button("Entrar", use_container_width=True):
            if registro in st.session_state.terapeutas_db and st.session_state.terapeutas_db[registro] == senha_t:
                st.session_state.autenticado = True
                st.session_state.modo_terapeuta = True
                st.session_state.usuario_atual = f"Terapeuta ({registro})"
                st.rerun()
            else:
                st.error("Credenciais inválidas.")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Voltar"):
            st.session_state.modo_terapeuta = False
            st.rerun()
    with col2:
        if st.button("Criar Conta de Terapeuta"):
            st.session_state.tela_atual = "cadastro_terapeuta"
            st.rerun()

def tela_cadastro_user():
    empty_l, center_col, empty_r = st.columns([1, 1.5, 1])
    with center_col:
        st.markdown("<h2 style='text-align: center;'>NOVO CADASTRO</h2>", unsafe_allow_html=True)
        with st.form("form_registro"):
            novo_usuario = st.text_input("Escolha um Usuário")
            nova_senha = st.text_input("Escolha uma Senha", type="password")
            confirmar = st.text_input("Confirme a Senha", type="password")
            if st.form_submit_button("Cadastrar", use_container_width=True):
                if novo_usuario in st.session_state.usuarios_db:
                    st.error("Usuário já existe.")
                elif nova_senha != confirmar:
                    st.error("As senhas não coincidem.")
                elif novo_usuario and nova_senha:
                    st.session_state.usuarios_db[novo_usuario] = nova_senha
                    st.success("Cadastro realizado!")
                    time.sleep(1)
                    st.session_state.tela_atual = "login"
                    st.rerun()
        if st.button("Voltar para Login"):
            st.session_state.tela_atual = "login"
            st.rerun()

def login_screen():
    empty_l, center_col, empty_r = st.columns([1, 1.5, 1])
    with center_col:
        st.markdown("<h2 style='text-align: center;'>BEM VINDO</h2>", unsafe_allow_html=True)
        with st.form("login_form"):
            usuario = st.text_input("Usuário")
            senha = st.text_input("Senha", type="password")
            if st.form_submit_button("Entrar", use_container_width=True):
                if usuario in st.session_state.usuarios_db and st.session_state.usuarios_db[usuario] == senha:
                    st.session_state.autenticado = True
                    st.session_state.usuario_atual = usuario
                    st.rerun()
                else:
                    st.error("Dados incorretos.")
        
        st.divider()
        if st.button("Criar Minha Conta ", use_container_width=True):
            st.session_state.tela_atual = "cadastro_user"
            st.rerun()
        if st.button("Sou Terapeuta 🩺", use_container_width=True):
            st.session_state.modo_terapeuta = True
            st.rerun()



if not st.session_state.autenticado:
    if st.session_state.tela_atual == "cadastro_terapeuta":
        tela_cadastro_terapeuta()
    elif st.session_state.modo_terapeuta:
        login_terapeuta()
    elif st.session_state.tela_atual == "cadastro_user":
        tela_cadastro_user()
    else:
        login_screen()
else:
    # --- ÁREA LOGADA ---
    if st.session_state.modo_terapeuta:
        st.title("👨‍⚕️ Painel do Terapeuta")
        st.write(f"Bem-vindo, {st.session_state.usuario_atual}")
        if st.session_state.meus_relatorios:
            for r in st.session_state.meus_relatorios:
                with st.expander(f"{r['data']} - Paciente: {r.get('usuario', 'Desconhecido')}"):
                    st.write(f"**Título:** {r['titulo']}")
                    st.write(r['texto'])
                    st.caption(f"Humor: {r['humor']}")
        else:
            st.info("Nenhum relatório disponível.")
    else:
        st.title("Sistema Operacional MIO")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Iniciar Conversa Terapêutica", use_container_width=True): modal_mio()
        with col2:
            if st.button("Escrever Relatório do Dia", use_container_width=True): modal_relatorio()

    # SIDEBAR
    with st.sidebar:
        st.write(f"Sessão: {st.session_state.usuario_atual}")
        if st.button("Sair"):
            st.session_state.autenticado = False
            st.session_state.modo_terapeuta = False
            st.session_state.tela_atual = "login"
            st.rerun()
        st.divider()
        exibir_calendario_humor()
        st.divider()
        st.link_button("Falar com Terapeuta", f"https://wa.me/5567984746659?text=Ajuda")
