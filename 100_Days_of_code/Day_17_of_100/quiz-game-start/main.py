from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_list = []

for question in question_data:
    q_text = question['text']
    q_answer = question['answer']
    actual_question = Question(q_text, q_answer)
    question_list.append(actual_question)

quiz = QuizBrain(question_list)
while quiz.more_questions():
    quiz.next_question()

# for question in question_list:
#     print(question.text)
