from data import question_data
from question_model import Question
from quiz_brain import Quiz

question_bank = []
for q in question_data:
    question_text = q["text"]
    #print(question_text)
    question_answer = q["answer"]
    # print(question_answer)
    new_q = Question(question_text, question_answer)
    question_bank.append(new_q)
    # print(question_bank[0].answer)
    
quiz = Quiz(question_bank)
quiz.next_question()

while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz")
print(f"Your final score is {quiz.score}/{len(question_bank)}")