# 🤖 Chatbot em Python para Android (Pydroid3)  

Um chatbot simples e interativo com respostas pré-definidas e capacidade de aprendizado progressivo. Ideal para uso em dispositivos Android via Pydroid3 (offline).  

---

## 📋 Funcionalidades  
- **Respostas Pré-Definidas**: Perguntas comuns como "olá", "tudo bem?", e "adeus" são respondidas de forma instantânea.  
- **Aprendizado Contínuo**: Gera respostas personalizadas com base nas interações anteriores do usuário.  
- **Armazenamento de Conhecimento**: Salva o aprendizado no arquivo `knowledge.pickle` para uso futuro.  
- **Compatibilidade Offline**: Funciona sem internet, usando apenas bibliotecas padrão do Python.  

---

## 📲 Requisitos  
- **Dispositivo Android** com Pydroid3 instalado ([Download na Play Store](https://play.google.com/store/apps/details?id=ru.iiec.pydroid3)).  
- **Arquivos do Repositório**:  
  - `chat-droid.py`: Código principal do chatbot.  
  - `knowledge.pickle` (opcional): Banco de dados de palavras pré-aprendidas.  

---

## ⚙️ Instalação e Uso  
1. **Baixe os arquivos**:  
   - Clique em `Code` > `Download ZIP` neste repositório ou faça um `git clone`.  
   - Extraia os arquivos em uma pasta do seu dispositivo.  

2. **Execute no Pydroid3**:  
   - Abra o Pydroid3 e navegue até a pasta dos arquivos.  
   - Execute `chat-droid.py`.  
   - Digite suas mensagens no terminal e pressione `Enter` para interagir.  

3. **Modos de Operação**:  
   - **Sem `knowledge.pickle`**: O chatbot começará do zero e criará o arquivo automaticamente.  
   - **Com `knowledge.pickle`**: O chatbot usará o conhecimento pré-carregado para respostas mais contextualizadas.  

---

## 🧠 Como Funciona?  
- **Respostas Imediatas**:  
  - Se o usuário fizer uma pergunta pré-definida (ex: "Qual é o seu nome?"), o chatbot responde instantaneamente.  
- **Geração de Respostas Dinâmicas**:  
  - Usa cadeias de Markov para criar frases com base nas palavras aprendidas (ex: se o usuário escreve "gosto de programar", o chatbot pode responder "programar é divertido" no futuro).  
- **Limite de Tamanho**:  
  - Se `knowledge.pickle` ultrapassar **1.5 MB**, o chatbot reinicia o aprendizado para evitar sobrecarga.  

---

## 🛠 Personalização  
- **Adicione Novas Respostas**:  
  - Edite o dicionário `RESPONSES` no código para incluir perguntas e respostas personalizadas.  
  ```python  
  RESPONSES = {  
      "nova pergunta": "nova resposta",  
      # ...  
  }  
  ```  
- **Ajuste Stop Words**:  
  - Modifique a lista `stop_words` para incluir termos irrelevantes ao seu contexto.  

---

## ⚠️ Limitações  
- **NLP Básico**: Não usa IA avançada, então respostas geradas podem ser desconexas.  
- **Dependência de Interações**: O aprendizado melhora com o tempo, mas requer conversas frequentes.  

---

## 📝 Exemplo de Uso  
```  
> terra  
Bot: terra somos todos temos uns universo sou grata poder sentir chama curiosidade respeito cuidado vida emoções fazem vibrar afinal contas música faço dúvidas fazem sentir beleza perfeição 

> beleza  
Bot: Beleza detalhe importante lembrar amor raiva sinto sou capaz limpar superfície toco pincelada cor diferente vez lutar tempo sinto parte trabalhando duro suficiente ambiente positivo pessoas redor percebendo pequeno ponto final   
```  

---

## 📄 Licença  
Este projeto é open-source. Sinta-se à vontade para modificar e distribuir (créditos são apreciados!).  

--- 

**Nota**: Para melhores resultados, interaja com frases curtas e evite gírias complexas. 🚀
