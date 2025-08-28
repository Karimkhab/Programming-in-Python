class Question:
    def __init__(self, question, answer_list, correct_answer):
        self.question = question
        self.answer_list = answer_list
        self.correct_answer = correct_answer

    def print_question(self):
        print(f'Question: {self.question}')
        for i, answer in enumerate(self.answer_list):
            print(f'\t{i}: {answer}')


class Quiz:
    def __init__(self):
        self.score = 0
        self.questions = []
        pass

    def add_question(self, question, answer_list, correct_answer):
        question = Question(question, answer_list, correct_answer)
        self.questions.append(question)

    def take_quiz(self):
        for question in self.questions:
            question.print_question()
            answer = int(input('Enter your answer: '))
            if answer == question.correct_answer:
                self.score += 1

    def grade_quiz(self):
        print(f'Grade of quiz: {self.score / len(self.questions) * 100}%')

quiz = Quiz()
quiz.add_question("What is the best city in the world?", ["A. NYC", "B. Innopolis", "C. Berlin",
"D. Madrid"], 1)
quiz.add_question("Which planet is known as the Red Planet?", ["A. Mars", "B. Venus", "C.Jupiter", "D. Saturn"], 0)
quiz.add_question("Who painted the Mona Lisa?", ["A. Leonardo da Vinci", "B. Innopolis art club", "C. Pablo Picasso", "D. Michelangelo"], 0)
quiz.take_quiz()
quiz.grade_quiz()