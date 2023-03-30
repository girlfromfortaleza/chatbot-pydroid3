# chatbot-pydroid3

//Dois arquivos//

Os arquivos "chat-droid.py" e "knowledge.pickle" são arquivos que fazem parte de um sistema de chatbot. O "chat-droid.py" é o arquivo principal do programa, que contém o código que realiza a interação do usuário com o chatbot no terminal. Já o arquivo "knowledge.pickle" contém o conhecimento prévio que o chatbot possui para responder às perguntas dos usuários.

Caso você baixe apenas o arquivo "chat-droid.py" e execute o programa, o código irá criar um novo arquivo "knowledge.pickle" do zero na mesma pasta do codigo, e o chatbot não terá nenhum conhecimento prévio para responder às perguntas dos usuários.

Por outro lado, se você baixar também esse  arquivo "knowledge.pickle" que está neste repositório, significa que o chatbot já possui conhecimento prévio limitado e é capaz de fornecer respostas mais precisas e personalizadas aos usuários. Neste caso, ao baixar os dois arquivos e executar o programa, ele utilizará o arquivo de conhecimento prévio para responder qualquer coisa que tenha haver com a entrada de resposta do usuário. Lembrando que se o arquivo "knowledge.pickle" ultrapassar 1,5 MB, automaticamente começará tudo do zero o aprendizado.

//Resumo do código//

Este código é uma implementação de um chatbot que responde a perguntas e conversa com usuários. Ele possui uma série de respostas pré-definidas para perguntas comuns, como "olá", "tudo bem?" e "adeus", bem como algumas respostas mais elaboradas sobre tecnologia, aprendizado e hobbies.

A classe Chatbot tem um atributo _knowledge que é um dicionário usado para armazenar informações adicionais que o chatbot pode aprender durante uma conversa. As informações são salvas usando a biblioteca pickle, que permite serializar objetos Python.

Além disso, a classe possui um atributo stop_words, que é uma lista de palavras comuns em português que o chatbot ignora ao analisar a entrada do usuário. Isso permite que o chatbot se concentre nas palavras mais importantes na entrada e forneça respostas mais precisas.

A classe Chatbot também tem dois métodos: load_knowledge e save_knowledge. O primeiro é usado para carregar informações previamente aprendidas a partir do dicionário _knowledge, enquanto o segundo é usado para salvar informações aprendidas durante a conversa de volta ao dicionário.

No geral, este código fornece uma base sólida para a construção de um chatbot em Python e pode ser facilmente adaptado para outras línguas e conjuntos de respostas.

O diferencial desse código é a sua capacidade de aprendizado e personalização, permitindo que o Chatbot possa ser adaptado às necessidades do usuário e aprimorar suas respostas com o tempo. Este código é compatível com Pydroid 3, que é um IDE para Python em dispositivos Android. O código não usa nenhuma biblioteca que não esteja incluída na instalação padrão do Python, então ele deve funcionar sem problemas no Pydroid 3 no modo offline.
