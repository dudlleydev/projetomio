# 🧠 MIO - Assistente Terapêutico Virtual

O **MIO (Meu Interlocutor Online)** é uma plataforma de apoio terapêutico desenvolvida com Inteligência Artificial para auxiliar usuários no acompanhamento emocional, registro de sentimentos e reflexões diárias.

A aplicação utiliza modelos de IA para análise de sentimentos, geração de respostas terapêuticas e criação de imagens contextuais, proporcionando uma experiência interativa e personalizada.

---

# ✨ Funcionalidades

## 👤 Área do Usuário

### 💬 Conversa Terapêutica

* Chat interativo com a assistente MIO.
* Respostas geradas pelo Google Gemini.
* Histórico completo das conversas.
* Geração automática de imagens relacionadas ao contexto da conversa.

### 😊 Análise de Humor

* Registro diário de emoções.
* Classificação automática de sentimentos.
* Identificação de humor positivo ou negativo.

### 📝 Relatórios Diários

* Escrita de reflexões pessoais.
* Análise automática do conteúdo.
* Associação do humor ao dia correspondente.

### 📅 Calendário Emocional

* Visualização mensal do humor.
* Emojis indicam o estado emocional registrado:

  * 😊 Positivo
  * 😔 Negativo

---

## 👨‍⚕️ Área do Terapeuta

### Painel Profissional

* Login exclusivo para terapeutas.
* Visualização dos relatórios dos pacientes.
* Acompanhamento do histórico emocional.

---

# 🛠️ Tecnologias Utilizadas

| Tecnologia              | Função                    |
| ----------------------- | ------------------------- |
| Streamlit               | Interface Web             |
| Google Gemini 2.5 Flash | Conversação Inteligente   |
| DistilBERT              | Análise de Sentimentos    |
| Stable Diffusion v1.5   | Geração de Imagens        |
| PyTorch                 | Processamento dos modelos |
| Transformers            | Pipeline NLP              |
| Diffusers               | Geração de imagens        |

---

# 📦 Instalação

## Pré-requisitos

* Python 3.9 ou superior
* Git
* CUDA (opcional para uso de GPU)

---

## Instalar Dependências

```bash
pip install streamlit
pip install torch
pip install google-generativeai
pip install transformers
pip install diffusers
```

Ou:

```bash
pip install streamlit torch google-generativeai transformers diffusers
```

---

# 🔑 Configuração da API Gemini

No código localize:

```python
genai.configure(api_key="SUA_CHAVE_AQUI")
```

Substitua pela sua chave obtida no Google AI Studio.

---

# ▶️ Executando o Projeto

```bash
streamlit run app.py
```

Após executar, o sistema abrirá automaticamente no navegador.

---

# 🔐 Sistema de Autenticação

## Usuário

| Usuário | Senha |
| ------- | ----- |
| Duda    | 1234  |

## Terapeuta

| Registro | Senha |
| -------- | ----- |
| 12345    | admin |

⚠️ Essas credenciais são armazenadas apenas durante a execução da aplicação.

---

# 📂 Estrutura do Projeto

```text
MIO/
│
├── app.py
├── README.md
└── requirements.txt
```

---

# 🧠 Arquitetura da Aplicação

## Análise de Sentimentos

Modelo utilizado:

```text
distilbert-base-uncased-finetuned-sst-2-english
```

Responsável por classificar textos como:

* POSITIVE
* NEGATIVE

---

## Conversação Inteligente

Modelo utilizado:

```text
Gemini 2.5 Flash
```

A MIO atua como assistente terapêutica e incentiva o usuário a refletir sobre emoções e experiências.

---

## Geração de Imagens

Modelo utilizado:

```text
runwayml/stable-diffusion-v1-5
```

As imagens são geradas automaticamente a partir do contexto da resposta produzida pelo Gemini.

---

# ⚠️ Limitações

* Dados armazenados apenas em memória.
* Não utiliza banco de dados.
* Senhas armazenadas em texto simples.
* Chave da API configurada diretamente no código.
* Histórico é perdido ao reiniciar a aplicação.
* Geração de imagens pode ser lenta sem GPU.

---

# 🚀 Melhorias Futuras

* Banco de dados SQLite ou PostgreSQL
* Hash de senhas com bcrypt
* Variáveis de ambiente para credenciais
* Cache para imagens geradas
* Integração OAuth
* Dashboard analítico para terapeutas
* Histórico persistente
* Deploy com Docker
* Hospedagem em nuvem

---

# 📞 Contato com Profissional

O sistema possui integração direta com WhatsApp para facilitar o contato entre usuários e profissionais de saúde mental.

---

# 📄 Licença

Projeto desenvolvido para fins acadêmicos e educacionais.

Licenças dos modelos utilizados:

| Modelo           | Licença                 |
| ---------------- | ----------------------- |
| Stable Diffusion | CreativeML Open RAIL-M  |
| DistilBERT       | Apache 2.0              |
| Google Gemini    | Termos de Uso Google AI |

---

# 👩‍💻 Desenvolvido por

Projeto acadêmico focado em:

* Inteligência Artificial
* Machine Learning
* Processamento de Linguagem Natural (NLP)
* Análise de Sentimentos
* Desenvolvimento Web com Streamlit
* Tecnologia aplicada à Saúde Mental
# 🧠 MIO - Assistente Terapêutico Virtual

O **MIO (Meu Interlocutor Online)** é uma plataforma de apoio terapêutico desenvolvida com Inteligência Artificial para auxiliar usuários no acompanhamento emocional, registro de sentimentos e reflexões diárias.

A aplicação utiliza modelos de IA para análise de sentimentos, geração de respostas terapêuticas e criação de imagens contextuais, proporcionando uma experiência interativa e personalizada.

---

# ✨ Funcionalidades

## 👤 Área do Usuário

### 💬 Conversa Terapêutica

* Chat interativo com a assistente MIO.
* Respostas geradas pelo Google Gemini.
* Histórico completo das conversas.
* Geração automática de imagens relacionadas ao contexto da conversa.

### 😊 Análise de Humor

* Registro diário de emoções.
* Classificação automática de sentimentos.
* Identificação de humor positivo ou negativo.

### 📝 Relatórios Diários

* Escrita de reflexões pessoais.
* Análise automática do conteúdo.
* Associação do humor ao dia correspondente.

### 📅 Calendário Emocional

* Visualização mensal do humor.
* Emojis indicam o estado emocional registrado:

  * 😊 Positivo
  * 😔 Negativo

---

## 👨‍⚕️ Área do Terapeuta

### Painel Profissional

* Login exclusivo para terapeutas.
* Visualização dos relatórios dos pacientes.
* Acompanhamento do histórico emocional.

---

# 🛠️ Tecnologias Utilizadas

| Tecnologia              | Função                    |
| ----------------------- | ------------------------- |
| Streamlit               | Interface Web             |
| Google Gemini 2.5 Flash | Conversação Inteligente   |
| DistilBERT              | Análise de Sentimentos    |
| Stable Diffusion v1.5   | Geração de Imagens        |
| PyTorch                 | Processamento dos modelos |
| Transformers            | Pipeline NLP              |
| Diffusers               | Geração de imagens        |

---

# 📦 Instalação

## Pré-requisitos

* Python 3.9 ou superior
* Git
* CUDA (opcional para uso de GPU)

---

## Instalar Dependências

```bash
pip install streamlit
pip install torch
pip install google-generativeai
pip install transformers
pip install diffusers
```

Ou:

```bash
pip install streamlit torch google-generativeai transformers diffusers
```

---

# 🔑 Configuração da API Gemini

No código localize:

```python
genai.configure(api_key="SUA_CHAVE_AQUI")
```

Substitua pela sua chave obtida no Google AI Studio.

---

# ▶️ Executando o Projeto

```bash
streamlit run app.py
```

Após executar, o sistema abrirá automaticamente no navegador.

---

# 🔐 Sistema de Autenticação

## Usuário

| Usuário | Senha |
| ------- | ----- |
| Duda    | 1234  |

## Terapeuta

| Registro | Senha |
| -------- | ----- |
| 12345    | admin |

⚠️ Essas credenciais são armazenadas apenas durante a execução da aplicação.

---

# 📂 Estrutura do Projeto

```text
MIO/
│
├── app.py
├── README.md
└── requirements.txt
```

---

# 🧠 Arquitetura da Aplicação

## Análise de Sentimentos

Modelo utilizado:

```text
distilbert-base-uncased-finetuned-sst-2-english
```

Responsável por classificar textos como:

* POSITIVE
* NEGATIVE

---

## Conversação Inteligente

Modelo utilizado:

```text
Gemini 2.5 Flash
```

A MIO atua como assistente terapêutica e incentiva o usuário a refletir sobre emoções e experiências.

---

## Geração de Imagens

Modelo utilizado:

```text
runwayml/stable-diffusion-v1-5
```

As imagens são geradas automaticamente a partir do contexto da resposta produzida pelo Gemini.

---

# ⚠️ Limitações

* Dados armazenados apenas em memória.
* Não utiliza banco de dados.
* Senhas armazenadas em texto simples.
* Chave da API configurada diretamente no código.
* Histórico é perdido ao reiniciar a aplicação.
* Geração de imagens pode ser lenta sem GPU.

---

# 🚀 Melhorias Futuras

* Banco de dados SQLite ou PostgreSQL
* Hash de senhas com bcrypt
* Variáveis de ambiente para credenciais
* Cache para imagens geradas
* Integração OAuth
* Dashboard analítico para terapeutas
* Histórico persistente
* Deploy com Docker
* Hospedagem em nuvem

---

# 📞 Contato com Profissional

O sistema possui integração direta com WhatsApp para facilitar o contato entre usuários e profissionais de saúde mental.

---

# 📄 Licença

Projeto desenvolvido para fins acadêmicos e educacionais.

Licenças dos modelos utilizados:

| Modelo           | Licença                 |
| ---------------- | ----------------------- |
| Stable Diffusion | CreativeML Open RAIL-M  |
| DistilBERT       | Apache 2.0              |
| Google Gemini    | Termos de Uso Google AI |

---

# 👩‍💻 Desenvolvido por

Projeto acadêmico focado em:

* Inteligência Artificial
* Machine Learning
* Processamento de Linguagem Natural (NLP)
* Análise de Sentimentos
* Desenvolvimento Web com Streamlit
* Tecnologia aplicada à Saúde Mental
 
