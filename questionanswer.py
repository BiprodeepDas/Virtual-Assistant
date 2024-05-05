import google.generativeai as palm
import chatbot
from chatbot import load_knowledge

palm.configure(api_key='AIzaSyDjFZqQ2pjAYZbAaXvSChLQoZSoWAgNjj0')
def replyques(quest):
    completion = palm.generate_text(
        model='models/text-bison-001',
        prompt=f"{quest}\n"
               "Give line by line explanation and use calculator if it is required",
        temperature=1.0,
        # The maximum length of the response
        max_output_tokens=2000,)

    print(f"Assistant : {completion.result}")


# ques='''
# name some
#
#
# '''
# replyques(ques)
