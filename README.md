# Gerador de Planos de Aula com IA

## Descrição
Esta aplicação web facilita a criação de planos de aula para professores. Utiliza **Streamlit** para a interface e **LangChain** com um modelo gratuito da **Hugging Face** (`mistralai/Mistral-7B-Instruct-v0.1`) para gerar planos de aula personalizados.

## Funcionalidades
- Selecionar a **série** (1ª a 5ª).
- Escolher a **matéria** (Geografia, Matemática, Inglês, Português, Ciência).
- Escolher o **bimestre** (1º a 4º).
- Gerar um **plano de aula estruturado** com:
  - Objetivo
  - Conteúdo Programático
  - Atividades
  - 10 perguntas abertas com respostas

## Tecnologias Utilizadas
- **Python**
- **Streamlit** (para interface web)
- **LangChain** (para integração com IA)
- **Hugging Face Inference API** (modelo `mistralai/Mistral-7B-Instruct-v0.1`)

## Como Executar
1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-repo/plano-aula.git
   cd plano-aula
   ```
2. Crie um ambiente virtual e instale as dependências:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   pip install -r requirements.txt
   ```
3. Configure sua API Key da Hugging Face:
   ```bash
   export HUGGINGFACEHUB_API_TOKEN="sua_chave_aqui"  # Linux/macOS
   set HUGGINGFACEHUB_API_TOKEN="sua_chave_aqui"  # Windows
   ```
4. Execute a aplicação:
   ```bash
   streamlit run app.py
   ```

## Como Funciona
1. O usuário escolhe a série, matéria e bimestre.
2. Ao clicar no botão **Gerar Plano de Aula**, a aplicação envia um prompt ao modelo da Hugging Face.
3. O modelo gera um plano de aula estruturado, incluindo perguntas abertas.
4. O plano gerado é exibido na tela.

## Exemplo de Uso
**Entrada:**
- Série: 2ª Série
- Matéria: Matemática
- Bimestre: 1º Bimestre

**Saída:**
```
Objetivo: Introduzir os conceitos básicos de adição e subtração.
Conteúdo Programático:
- Números naturais
- Operações básicas (adição e subtração)
Atividades:
- Jogos interativos com somas e subtrações
- Exercícios práticos com desafios matemáticos

Perguntas:
1. O que significa somar dois números?
   Resposta: Somar é juntar quantidades para obter um total.
...
```

## Considerações Finais
Este projeto pode ser expandido para incluir novos modelos e funcionalidades, como exportação dos planos para PDF ou armazenamento dos históricos de geração. 🚀

