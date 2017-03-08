import random
def read_data(questions_file, answers_file):
    with open(questions_file, 'r') as questions:
        with open(answers_file, 'r') as answers:
            return zip(questions.readlines(), answers.readlines())

def start_read_data():
    q_a = read_data('questions.txt', 'answers.txt')
    correct = []
    incorrect = []
    while len(q_a) != 0 or len(incorrect) != 0:
        current_choice = None
        if len(q_a) != 0:
            current_choice = random.choice(q_a)
        else:
            current_choice = random.choice(incorrect)
        print(current_choice[0])
        raw_input("Show answer? Press enter...")
        print(current_choice[1])
        response = raw_input("Did you get it correct? (y/n)")
        q_a.remove(current_choice)
        if response == "y":
            correct.append(current_choice)
        else:
            incorrect.append(current_choice)


if __name__ == '__main__':
    try:
        start_read_data()
    except KeyboardInterrupt:
        print("Finished! You got a decent score idek.")
