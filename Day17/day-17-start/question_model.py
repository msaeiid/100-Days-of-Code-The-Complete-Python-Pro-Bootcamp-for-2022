# First Challenge Question model
class Question:
    def __init__(self, text, answer: bool):
        self.text = text
        self.answer = answer

    def __str__(self):
        return self.text
