import random

def generate_math_question(a,b):
    num1 = random.randint(a, b)
    num2 = random.randint(a, b)
    operator = random.choice(['+','-','*','/'])
    a = f"{num1} {operator} {num2}"

    return a

print(generate_math_question(1,10))

def check_answer(task, answer):
    try:
        result = float(answer)
        return result == eval(task)
    except ValueError:
        return False

def math_quiz(number_of_questions):
    print("Добро пожаловать в математический тест!")
    correct_answers = 0

    for i in range(number_of_questions):
        question = generate_math_question(1, 5)
        user_answer = input(f'{question} = ')
        if check_answer(question, user_answer):
            correct_answers += 1

    print("Тест завершен.")
    print(f"Вы правильно решили {correct_answers} из {number_of_questions} вопросов.")

    if correct_answers >= number_of_questions * 0.8:
        print("Отлично! Вы получаете оценку A.")
    elif correct_answers >= number_of_questions * 0.6:
        print("Хорошо! Вы получаете оценку B.")
    else:
        print("Попробуйте еще раз. Вы получаете оценку C.")


math_quiz(7)
