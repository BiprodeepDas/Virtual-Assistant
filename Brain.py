import google.generativeai as palm
import chatbot
from chatbot import load_knowledge

palm.configure(api_key='AIzaSyDjFZqQ2pjAYZbAaXvSChLQoZSoWAgNjj0')


def reply(quest):
    knowledge: dict = load_knowledge('knowledge.json')
    bestmatch: str | None = chatbot.best_match(quest, [q["questions"] for q in knowledge["questions"]])
    if bestmatch:
        answer: str = chatbot.get_answer(bestmatch, knowledge)
    else:
        completion = palm.chat(messages=quest)

        answer = completion.last

        knowledge["questions"].append({"questions": quest, "answer": answer})
        chatbot.save_knowledge('knowledge.json', knowledge)
    return answer

# while True:
#     i = input("Enter : ")
#     print(reply(i))
