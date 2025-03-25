import os
from dotenv import load_dotenv
from langchain.llms import HuggingFaceHub
import re
import streamlit as st
# Carregar variáveis de ambiente
load_dotenv()
HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")

# Função para gerar o plano de aula e perguntas
def gerar_conteudo_aula(serie, materia, bimestre):
    """Gera um plano de aula e perguntas/respostas com base nos parâmetros."""
    prompt = f"""
    Gere um plano de aula em português para {materia}, {serie}, {bimestre}.
    Estruture: Objetivo, Conteúdo, Atividades.
    Após, gere 10 perguntas abertas com respostas sobre o tema.
    """
    llm = HuggingFaceHub(repo_id="mistralai/Mistral-7B-Instruct-v0.1", 
                         huggingfacehub_api_token=HUGGINGFACEHUB_API_TOKEN,
                         model_kwargs={"temperature": 0.7})
    return llm.invoke(prompt)

# Função para formatar perguntas e respostas
def formatar_perguntas_respostas(conteudo):
    """Separa e formata perguntas e respostas do conteúdo gerado."""
    partes = re.split(r"(Pergunta: |Resposta: )", conteudo)
    plano_aula = partes[0].strip()
    perguntas_respostas = []
    pergunta = None
    for parte in partes[1:]:
        if "Pergunta:" in parte:
            pergunta = partes[partes.index(parte) + 1].strip()
        elif "Resposta:" in parte and pergunta:
            resposta = partes[partes.index(parte) + 1].strip()
            perguntas_respostas.append({"pergunta": pergunta, "resposta": resposta})
            pergunta = None
    return plano_aula, perguntas_respostas

# Interface Streamlit
st.title("Gerador de Plano de Aula e Perguntas")

series = ["1ª Série", "2ª Série", "3ª Série", "4ª Série", "5ª Série"]
materias = ["Geografia", "Matemática", "Inglês", "Português", "Ciência"]
bimestres = ["1º Bimestre", "2º Bimestre", "3º Bimestre", "4º Bimestre"]

serie = st.selectbox("Selecione a Série", series)
materia = st.selectbox("Selecione a Matéria", materias)
bimestre = st.selectbox("Selecione o Bimestre", bimestres)

if st.button("Gerar Conteúdo da Aula"):
    if not HUGGINGFACEHUB_API_TOKEN:
        st.error("Configure sua chave Hugging Face no arquivo .env.")
    else:
        with st.spinner("Gerando..."):
            conteudo = gerar_conteudo_aula(serie, materia, bimestre)
            plano_aula, perguntas_respostas = formatar_perguntas_respostas(conteudo)
            st.subheader("Plano de Aula:")
            st.write(plano_aula)
            