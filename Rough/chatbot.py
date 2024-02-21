from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import re
chatbot = ChatBot('disaterbot0')
trainer = ListTrainer(chatbot)
trainer.train([
    "what is your emergency?",
    "fire accident",
    "can you share your location?",
    "yes",
    "help is on the way."
])
while True:
    try:
        bot_input = chatbot.get_response(input().strip())
        bot_input = str(bot_input)
        bot_input = bot_input.replace("No value for search_text was available on the provided input"," ")
        print(bot_input)

    except(KeyboardInterrupt, EOFError, SystemExit):
        break
