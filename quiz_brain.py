from data import question_data


class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.true_cnt = 0
        self.question_list = question_list

    def still_has_question(self):
        if len(question_data) < self.question_number + 1:
            print(f"\nCongrats :) Your last score is {self.true_cnt}/{self.question_number}")
            return False
        return True

    def next_question(self):
        """
        Asks the next question
        :return: Answer
        """
        current_question = self.question_list[self.question_number]
        answer = input(f"Q.{self.question_number + 1}: {current_question.text} (True/False)?: ")
        if answer in [str(current_question.answer)[0],
                      str(current_question.answer),
                      str(current_question.answer)[0].lower(),
                      str(current_question.answer).lower(),
                      str(current_question.answer).upper()]:
            self.question_number += 1
            self.true_cnt += 1
            print(f"Your score is {self.true_cnt}/{self.question_number}")
            return answer
        elif answer in ['quit', 'exit', 'off']:
            print(f"\nYour last score is {self.true_cnt}/{self.question_number}\n"
                  f"Hope you enjoyed the quiz :)")
            return 'exit'
        else:
            self.question_number += 1
            print(f"Your score is {self.true_cnt}/{self.question_number}")
            return answer
