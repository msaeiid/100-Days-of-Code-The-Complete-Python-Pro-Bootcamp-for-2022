# PascalCase for class name
# snake_case for everything else
from data import question_data as data
from question_model import Question
from quiz_brain import QuizBrain

# Second challenge question bank
question_bank = [Question(question['question'], question['correct_answer']) for question in data]
question_brain = QuizBrain(question_bank)
while question_brain.still_has_questions():
    question_brain.next_question()
print("You've completed the quiz")
print(f"Yor final score was: {question_brain.score}/{len(question_bank)}")
