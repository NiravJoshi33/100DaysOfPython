from data import question_data
from question_model import Question

question_bank = []
for q in question_data:
    question_text = q["text"]
    print(question_text)
    question_answer = q["answer"]
    print(question_answer)
    new_q = Question(question_text, question_answer)
    