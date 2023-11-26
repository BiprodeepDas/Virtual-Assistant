import json
from difflib import get_close_matches


def load_knowledge(filepath: str) -> dict:
    with open(filepath, 'r') as file:
        data: dict = json.load(file)
    return data


def save_knowledge(filepath: str, data: dict):
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=2)


def best_match(user_ques: str, questions: list[str]) -> str | None:
    matches: list = get_close_matches(user_ques, questions, n=1, cutoff=0.7)
    return matches[0] if matches else None


def get_answer(question: str, knowledge: dict) -> str | None:
    for q in knowledge["questions"]:
        if q["questions"] == question:
            return q["answer"]


def chat_bot():
    knowledge: dict = load_knowledge('knowledge.json')

    while True:
        ip: str = input('You : ')

        if ip.lower() == 'quit':
            break

        bestmatch: str | None = best_match(ip, [q["questions"] for q in knowledge["questions"]])

        if bestmatch:
            answer: str = get_answer(bestmatch, knowledge)
            print(f'Bot : {answer}')
        else:
            print('Bot : I don\'t know the answer.Can you teach me ?')
            new_ans: str = input('Type the answer of "s" to skip ! : ')

            if new_ans.lower() != 's':
                knowledge["questions"].append({"questions": ip, "answer": new_ans})
                save_knowledge('knowledge.json', knowledge)
                print("Thank you, i learned a new response !")


if __name__ == '__main__':
    chat_bot()
