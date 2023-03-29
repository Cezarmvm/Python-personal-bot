import telebot

#from functions import Advogado

chave_api = "--------------------------"

bot = telebot.TeleBot(chave_api)

@bot.message_handler(func=["advogado"])
def advogado(msgm):
    Advogado()


def verificar(msgm):
    return True

@bot.message_handler(func=verificar)
def responder(msgm):
    texto = """
👋 Olá!
Eu sou o seu **oráculo** e vou te ajudar a organizar o seu dia a qualquer hora e de qualquer lugar!
Selecione uma das opções:
/Advogado
/Compras
/Filosofia
/Filmes
/Gastro
/Psicologa
/Psiquiatra
/Senha
/Task
/Trabalho
    """
    bot.reply_to(msgm, texto)

def main():
    bot.polling()

if __name__ == "__main__":
    main()