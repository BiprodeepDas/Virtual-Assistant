import google.generativeai as palm
import medChat
from medChat import load_knowledge

palm.configure(api_key='AIzaSyDjFZqQ2pjAYZbAaXvSChLQoZSoWAgNjj0')


def reply(quest):
    knowledge: dict = load_knowledge('meds.json')
    bestmatch: str | None = medChat.best_match(quest, [q["disease"] for q in knowledge["diseases"]])
    if bestmatch:
        answer: str = medChat.get_answer(bestmatch, knowledge)
    else:
        completion = palm.chat(messages=f"suggest me medicine for {quest}")

        answer = completion.last

        knowledge["diseases"].append({"disease": quest, "medicine": answer})
        medChat.save_knowledge('meds.json', knowledge)
    return answer


def take(ip):
    print(reply(ip))
