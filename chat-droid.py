import os
import string
import random
import pickle

class Chatbot:
    MAX_INPUT_LENGTH = 10024
    RESPONSES = {
"olá": "Olá! Como posso ajudar?",
"tudo bem?": "Estou bem, obrigado! E você?",
"qual é o seu nome?": "Meu nome é Chatbot, e o seu?",
"como você está?": "Estou ótimo, obrigado!",
"adeus": "Até logo! Espero poder conversar com você novamente em breve.",
"o que você gosta de fazer?": "Eu gosto de aprender novas coisas e conversar com pessoas interessantes como você!",
"você tem algum hobby?": "Eu não tenho hobbies, mas adoro aprender sobre novas áreas e assuntos",
"o que você acha sobre tecnologia?": "Eu acho que a tecnologia é incrível! Estou constantemente aprendendo sobre novas tecnologias e como elas podem ser aplicadas para ajudar as pessoas.",
"você tem algum conselho para me dar?": "Meu conselho seria sempre estar aberto para aprender coisas novas e expandir seus horizontes. Isso pode ajudá-lo a crescer como pessoa e alcançar seus objetivos.",
"você pode me contar uma piada?": "Claro! Por que a galinha atravessou a rua? Para chegar ao outro lado!",
"qual é a sua comida favorita?": "Eu sou um chatbot e não tenho a capacidade de comer, mas adoro aprender sobre diferentes pratos e culinárias de todo o mundo.",
"você já aprendeu alguma coisa nova hoje?": "Sim, eu aprendo coisas novas a cada momento. Aprender é uma das minhas coisas favoritas a fazer!",
}

    def __init__(self):
        self._knowledge = {}
        self.load_knowledge()
        self.stop_words = ['a', 'ao', 'aos', 'aquela', 'aquelas', 'aquele', 'aqueles', 'aquilo', 'as', 'até', 'com', 'como', 'da', 'das', 'de', 'dela', 'delas', 'dele', 'deles', 'depois', 'do', 'dos', 'e', 'ela', 'elas', 'ele', 'eles', 'em', 'entre', 'era', 'eram', 'essa', 'essas', 'esse', 'esses', 'esta', 'estas', 'este', 'estes', 'eu', 'foi', 'foram', 'há', 'isso', 'isto', 'já', 'la', 'lá', 'mais', 'mas', 'me', 'mesmo', 'meu', 'meus', 'minha', 'minhas', 'muito', 'na', 'não', 'nas', 'nem', 'no', 'nos', 'nossa', 'nossas', 'nosso', 'nossos', 'num', 'numa', 'nunca', 'o', 'os', 'ou', 'para', 'pela', 'pelas', 'pelo', 'pelos', 'por', 'porque', 'quando', 'que', 'quem', 'são', 'se', 'seja', 'sejam', 'sem', 'são', 'sua', 'suas', 'talvez', 'também', 'te', 'tem', 'tendo', 'tenha', 'ter', 'teu', 'teus', 'tua', 'tuas', 'um', 'uma', 'você', 'vocês', 'vos', 'seu', 'seus''ainda', 'algum', 'alguma', 'alguns', 'algumas', 'ali', 'ambos', 'antes', 'ao longo de', 'aos poucos', 'assim', 'cada', 'como se', 'conforme', 'contudo', 'da mesma forma', 'de acordo com', 'de maneira alguma', 'de modo algum', 'de vez em quando', 'dentro', 'desde', 'desse modo', 'desta forma', 'do que', 'e', 'em cima de', 'enquanto', 'então', 'era', 'era', 'esses', 'estava', 'estavam', 'estes', 'estávamos', 'eu', 'eis', 'em torno de', 'esse', 'este', 'está', 'foi', 'haja visto', 'logo', 'meu', 'mesma', 'mesmas', 'mesmos', 'minhas', 'nem mesmo', 'nesse sentido', 'no entanto', 'nós', 'o que', 'onde', 'ora', 'os que', 'outra', 'outras', 'outros', 'para que', 'por aqui', 'por enquanto', 'por exemplo', 'por isso', 'porém', 'porquanto', 'qual', 'quando', 'quanto', 'que', 'se bem que', 'sempre que', 'sendo', 'ser', 'seu', 'seus', 'tal', 'também', 'tanto', 'todavia', 'todo', 'tua', 'tudo', 'último', 'visto que', 'você', 'vós', 'à medida que', 'às vezes', 'é','ainda', 'algum', 'alguma', 'alguns', 'algumas', 'ali', 'ambos', 'antes', 'ao longo de', 'aos poucos', 'assim', 'cada', 'como se', 'conforme', 'contudo', 'da mesma forma', 'de acordo com', 'de maneira alguma', 'de modo algum', 'de vez em quando', 'dentro', 'desde', 'desse modo', 'desta forma', 'do que', 'e', 'em cima de', 'enquanto', 'então', 'era', 'esses', 'estava', 'estavam', 'estes', 'estávamos', 'eu', 'eis', 'em torno de', 'esse', 'este', 'está', 'foi', 'haja visto', 'logo', 'meu', 'mesma', 'mesmas', 'mesmos', 'minhas', 'nem mesmo', 'nesse sentido', 'no entanto', 'nós', 'o que', 'onde', 'ora', 'os que', 'outra', 'outras', 'outros', 'para que', 'por aqui', 'por enquanto', 'por exemplo', 'por isso', 'porém', 'porquanto', 'qual', 'quando', 'quanto', 'que', 'se bem que', 'sempre que', 'sendo', 'ser', 'seu', 'seus', 'tal', 'também', 'tanto', 'todavia', 'todo', 'tua', 'tudo', 'último', 'visto que', 'você', 'vós', 'à medida que', 'às vezes', 'é', 'acima', 'abaixo', 'agora', 'aliás', 'além', 'ampla', 'amplas', 'amplo', 'amplos', 'ante', 'antes', 'ao redor', 'apenas', 'apesar de', 'após', 'através', 'atrás', 'aí', 'bem', 'bom', 'cada vez mais', 'cerca', 'cima', 'comprido', 'conforme', 'conosco', 'consigo', 'contudo', 'contra', 'convosco', 'cuja', 'cujas', 'cujo', 'cujos', 'da mesma', 'daí', 'debaixo', 'demais', 'dentro', 'depois', 'desde que', 'desse', 'deste', 'devagar', 'dez', 'dezoito', 'dezesseis', 'dezessete', 'dezenove', 'dezenove', 'dezoito', 'dezoito', 'dezoito', 'diante', 'do que', 'dois', 'dos', 'doze', 'duas', 'dá', 'dão', 'dúvida', 'e', 'e-mail', 'e-mails', 'ela própria', 'elas próprias', 'ele próprio', 'eles próprios', 'enquanto', 'entretanto', 'era', 'era', 'eram', 'esses', 'estava', 'estavam', 'estes', 'estávamos', 'eu mesmo', 'euzinha', 'euzinho', 'ficar', 'fomos', 'for', 'fora', 'foram', 'fosse''abaixo', 'acerca', 'acima', 'adiante', 'agora', 'ainda mais', 'além', 'aliás', 'altura', 'antes de mais nada', 'ao redor', 'apesar de', 'aproximadamente', 'à parte', 'aquém', 'as vezes', 'atrás', 'bem', 'cada vez mais', 'caminho', 'caso contrário', 'certamente', 'com certeza', 'como resultado', 'consequentemente', 'contanto', 'convém', 'de acordo', 'de modo que', 'de repente', 'devido a', 'devagar', 'do outro lado', 'durante', 'e.g.', 'eis que', 'embora', 'em breve', 'em frente', 'em primeiro lugar', 'em segundo lugar', 'em terceiro lugar', 'enfim', 'entretanto', 'é que', 'exatamente', 'finalmente', 'inicialmente', 'isto é', 'logo depois', 'mais tarde', 'na medida em que', 'nesse caso', 'no caso de', 'no entanto', 'não obstante', 'o mesmo que', 'ora', 'ou seja', 'outrossim', 'para cima', 'para trás', 'para frente', 'para trás', 'por conseguinte', 'por isso mesmo', 'por fim', 'por hora', 'por ora', 'posteriormente', 'quando menos se espera', 'quanto antes', 'quanto mais', 'quer dizer', 'segundo', 'sem dúvida', 'sim', 'sobretudo', 'tão logo', 'tão pouco', 'todas as vezes', 'todavia', 'tão logo', 'tanto que', 'um pouco', 'uma vez que', 'várias vezes', 'vez ou outra', 'visto que','agora', 'aliás', 'ampla', 'amplas', 'amplo', 'amplos', 'ante', 'antes de', 'ao redor de', 'apesar de', 'após', 'através', 'cabo', 'caso', 'cima', 'com vista a', 'consoante', 'contanto', 'conto', 'daí', 'depois de', 'desde que', 'devido', 'durante', 'e assim', 'eis que', 'embora', 'enquanto que', 'entretanto', 'era uma vez', 'estando', 'fim de', 'grande', 'grandes', 'inclusive', 'incluso', 'indispensável', 'isto é', 'logo que', 'malgrado', 'mediante', 'menos', 'mesmo que', 'muito embora', 'na medida em que', 'na verdade', 'não obstante', 'nem mesmo', 'no caso de', 'no geral', 'no que concerne a', 'no que diz respeito a', 'no sentido de', 'numerosas', 'numerosos', 'o mesmo que', 'outrossim', 'pelos', 'perante', 'perto', 'por agora', 'por certo', 'por isso que', 'porém', 'posteriormente', 'primeiro', 'primeiramente', 'próprio', 'quando se trata de', 'quantas', 'quantos', 'relativamente', 'segundo', 'segundo o qual', 'seja como for', 'sendo assim', 'separadamente', 'sobretudo', 'tal como', 'tal qual', 'todas as vezes que', 'todavia', 'tão', 'tão pouco', 'várias', 'vários','agora', 'além', 'anteriormente', 'ao invés', 'apenas', 'apesar de', 'através de', 'bem', 'caso', 'certamente', 'como resultado', 'consequentemente', 'considerando', 'contanto que', 'daqui', 'daí', 'dali', 'de forma alguma', 'de modo que', 'de repente', 'devido a', 'e assim por diante', 'em geral', 'em outras palavras', 'em particular', 'em resumo', 'enfim', 'entretanto', 'finalmente', 'frequentemente', 'geralmente', 'há algum tempo', 'igualmente', 'junto', 'já que', 'longe', 'mais uma vez', 'mesmo que', 'nada', 'nem mesmo', 'neste momento', 'no mínimo', 'no que diz respeito a', 'no sentido de', 'no total', 'num sentido', 'ou seja', 'por conseguinte', 'porém', 'primeiramente', 'quanto a', 'quer dizer', 'rapidamente', 'segundo', 'seja', 'sendo assim', 'separadamente', 'talvez', 'tanto quanto', 'todas as vezes', 'tudo', 'uma vez que', 'vez ou outra','agora', 'ainda mais', 'algum tempo', 'aliás', 'além', 'apesar de', 'até mesmo', 'cada vez mais', 'com certeza', 'com isso', 'como resultado', 'consequentemente', 'daí', 'de fato', 'de forma alguma', 'de jeito nenhum', 'de modo que', 'de repente', 'de vez em quando', 'depois de', 'desde então', 'do contrário', 'e assim por diante', 'em breve', 'em outras palavras', 'em primeiro lugar', 'em seguida', 'então', 'enquanto isso', 'exatamente', 'finalmente', 'geralmente', 'hoje em dia', 'isto é', 'logo após', 'mais uma vez', 'mesmo assim', 'mesmo que', 'no fim das contas', 'no meio de', 'no momento', 'no presente', 'no último ano', 'nunca mais', 'o mais importante', 'pelo menos', 'por acaso', 'por aqui', 'por outro lado', 'por sinal', 'por sorte', 'por último', 'quando se trata de', 'quanto mais', 'rapidamente', 'recentemente', 'seja como for', 'sem dúvida', 'tanto faz', 'tanto quanto', 'todas as vezes', 'tudo bem', 'várias vezes', 'visto que','ainda', 'algum', 'alguma', 'alguns', 'algumas', 'ali', 'ambos', 'antes', 'ao longo de', 'aos poucos', 'assim', 'cada', 'como se', 'conforme', 'contudo', 'da mesma forma', 'de acordo com', 'de maneira alguma', 'de modo algum', 'de vez em quando', 'dentro', 'desde', 'desse modo', 'desta forma', 'do que', 'e', 'em cima de', 'enquanto', 'então', 'era', 'esses', 'estava', 'estavam', 'estes', 'estávamos', 'eu', 'eis', 'em torno de', 'esse', 'este', 'está', 'foi', 'haja visto', 'logo', 'meu', 'mesma', 'mesmas', 'mesmos', 'minhas', 'nem mesmo', 'nesse sentido', 'no entanto', 'nós', 'o que', 'onde', 'ora', 'os que', 'outra', 'outras', 'outros', 'para que', 'por aqui', 'por enquanto', 'por exemplo', 'por isso', 'porém', 'porquanto', 'qual', 'quando', 'quanto', 'que', 'se bem que', 'sempre que', 'sendo', 'ser', 'seu', 'seus', 'tal', 'também', 'tanto', 'todavia', 'todo', 'tua', 'tudo', 'último', 'visto que', 'você', 'vós', 'à medida que', 'às vezes'
]

    def add_to_knowledge(self, text):
        text = text.lower().translate(str.maketrans('', '', string.punctuation))
        words = [word for word in text.split() if word not in self.stop_words]
        for i in range(len(words) - 1):
            key = words[i]
            next_word = words[i + 1]
            if key in self._knowledge:
                self._knowledge[key].append(next_word)
            else:
                self._knowledge[key] = [next_word]

    def generate_response(self, user_input):
        text = user_input.lower().translate(str.maketrans('', '', string.punctuation))
        words = [word for word in text.split() if word not in self.stop_words]

        if len(words) > 0:
            key = words[0]
            response = key
            for i in range(30):
                if key in self._knowledge:
                    next_word = random.choice(self._knowledge[key])
                    response += ' ' + next_word
                    key = next_word
                else:
                    break
        else:
            response = None

        if response is None:
            response = self.get_predefined_response(user_input)

        if response is not None:
            self.add_to_knowledge(text)
            self.save_knowledge()

        return response

    def get_predefined_response(self, user_input):
        for question in self.RESPONSES.keys():
            if question in user_input.lower():
                return self.RESPONSES[question]
        return None

    def save_knowledge(self):
        with open("knowledge.pickle", "wb") as file:
            pickle.dump(self._knowledge, file)

    def load_knowledge(self):
        if os.path.exists("knowledge.pickle") and os.path.getsize("knowledge.pickle") > 0:
            with open("knowledge.pickle", "rb") as file:
                self._knowledge = pickle.load(file)

    def exit(self):
        self.save_knowledge()

def read_input(prompt):
    while True:
        try:
            user_input = input(prompt)
            if user_input:
                break
        except EOFError:
            break
    return user_input

chatbot = Chatbot()

while True:
    user_input = read_input('> ')
    if not user_input:
        chatbot.exit()
        break

    response = chatbot.generate_response(user_input)
    if response is None:
        print("Bot: Desculpe, não entendi o que você disse.")
    else:
        print("Bot:", response)
