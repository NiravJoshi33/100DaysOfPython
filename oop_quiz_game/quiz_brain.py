class Quiz:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
    
    def next_question(self):
        current_question = self.question_list[self.question_number].text
        correct_ans = self.question_list[self.question_number].answer
        self.question_number += 1
        ans = input(f"Q.[{self.question_number}]: {current_question} (True/False)?")
        self.check_answer(ans, correct_ans, self.score)     

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False
    
    def check_answer(self, ans, correct_ans, score):
        if ans.lower() == correct_ans.lower():
            print("You got it right!")
            self.score = self.score + 1
        else:
            print("That's wrong") 
        print(f"The anser was {correct_ans}.")
        print(f"You current score is {self.score}/{self.question_number}")
        print("\n")


