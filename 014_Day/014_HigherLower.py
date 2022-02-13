import random
from HigerLower.game_data import data
from HigerLower.art import vs

def compare(q1,q2):
    print("Compare A: " + q1['name'] + " a " + q1['description'] + ", from " + q1['country'] +"." )
    print(vs)
    print("Against B: " + q2['name'] + " a " + q2['description'] + ", from " + q2['country'] + ".")

def check(q1,q2):
    answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    global score
    global questions
    more_f = ''
    if answer == "a":
        answer = 'q1'
    elif answer == "b":
        answer = 'q2'
    if (q1['follower_count'] > q2['follower_count']):
        more_f = 'q1'
        del questions[1]
    elif (q1['follower_count'] < q2['follower_count']):
        more_f = 'q2'
        del questions[0]
    if answer == more_f:
        score += 1
        return False
    else:
        return True





score = 0

# print(questions[0])
# print(questions[0]['name'])
questions = random.choices(data, k=2)
game_off = False
while not game_off:

    if score > 0:
        print("You're right!. Current score: ", score)
    compare(questions[0],questions[1])
    game_off = check(questions[0],questions[1])
    print("\n" * 10)
    questions.append(random.choice(data))
    while questions[0] == questions[1]:
        questions[1] = questions.append(random.choice(data))
else:
    print("Sorry, that's wrong. Final score: ", score)