class QuizBrain:
    def __init__(self, list_of_questions):
        self.question_number = 0
        self.score = 0
        self.question_list = list_of_questions


    def more_questions(self):
        # for self.question_number in self.question_list:
            if self.question_number < len(self.question_list):
                return True
            else:
                False
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}:{current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, right_answer):
        if user_answer.lower() == right_answer.lower():
            self.score += 1
            print("Your answer is right")
        else:
            print("The answer is incorrect")
        print(f"your score is {self.score}/{self.question_number}")
