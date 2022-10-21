class QuizBrain:

    def __init__(self, questionList):
        self.questionNumber = 0
        self.questionList = questionList
        self.score = 0

    def nextQuestion(self):
        currentQuestion = self.questionList[self.questionNumber]
        self.questionNumber += 1
        userChoice = input(f"Q.{self.questionNumber}: {currentQuestion.question} (True/False)\n")
        self.correctAnswer(userChoice, currentQuestion.answer)


    def stillHaveQuestions(self):
        return self.questionNumber < len(self.questionList)


    def correctAnswer(self, userAns, corrAns):
        if corrAns == 'True':
            corAlt = 't'
        else:
            corAlt = 'f'
        if userAns.lower() == corrAns.lower() or userAns.lower() == corAlt:
            print("You got it right!")
            self.score += 1
        else:
            print("You got it wrong.")
        print(f"The correct answer is {corrAns}")
        print(f"Your score is {self.score}/{self.questionNumber}")
        print("\n")




