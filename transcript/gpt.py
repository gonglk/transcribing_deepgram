import os
import openai
from dotenv import load_dotenv
#session_token = os.getenv("session_token")
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')
#print(session_token)
import time
def generate_text(transcript):
    response = openai.Completion.create(
            engine="text-davinci-002",
            prompt="Answer the following questions {}:".format(transcript),
            temperature=0.9,
            max_tokens=4000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.2
        
        )
    return response['choices'][0]['text'].replace("\n\n","").strip()

#transcript ="How are you today? What is machine learning? Where is Canberra?"
#print(generate_text(transcript))

import nltk


def is_question(sentence):
    question_words = ["what", "when", "where", "who", "whom", "whose", "why", "how"]
    is_question_word = False
    for word in question_words:
        if word in sentence.lower():
            is_question_word = True
            break
    return is_question_word and sentence.endswith("?")

def find_questions(paragraph):
    sentences = nltk.sent_tokenize(paragraph)
    questions = []
    for sentence in sentences:
        if is_question(sentence):
            questions.append(sentence)
    return questions

#paragraph = "What is your name? This is not a question. How are you today? What is machine learning?"
#print(find_questions(paragraph))
def GPT_answers(transcript):
    
    questions = find_questions(transcript)
    answer_list = []
    if len(questions)>0:
        for question in questions:
            answer = generate_text(question)
            answer_list.append({question:answer})
    return answer_list
#transcript = "What is your name? This is not a question. How are you today? What is machine learning?" 

#start = time.time()
#print(GPT_answers(transcript))
#end = time.time()
#print(end-start)

