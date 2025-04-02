import random
questions = {
    "Who was the first president of Uganda": "Sir Edward Muteesa II",
    "Who heads DOGE in the USA": "Elon Musk",
    "Who founded Facebook?": "Mark Zuckerberg",
    "Who's founded Microsoft": "Bill Gates",
    "Who is the current president of the United States(2025)": "Donald J Trump",
    "Which party does Donald J.Trump belong to?":"Republican Party"
}

def play_trivial(questions):
    questions_list = list(questions.keys())
    total_questions = 3
    score = 0

    sample_questions = random.sample(questions_list,total_questions)

    for index, question in enumerate(sample_questions):
        print(f'{index}. {question}: ')
        user_answer = input("What's your answer: ").lower().strip()
        if user_answer == questions[question].lower():
            score += 1
            print("Correct answer! Keep it up.")
        else:
            print(f'Wrong answer. The correct answer is {questions[question]}')
    
    print(f'Your score is {score}/{total_questions}')

play_trivial(questions)