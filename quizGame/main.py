from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

ques = []
for i in question_data:
    text = i['question']
    answer = i['correct_answer']
    newQuestion = Question(text, answer)
    ques.append(newQuestion)

newGame = QuizBrain(ques)

while newGame.stillHaveQuestions():
    newGame.nextQuestion()

print("You have completed the quiz!")
print(f"Your final score was {newGame.score} / {newGame.questionNumber}")





