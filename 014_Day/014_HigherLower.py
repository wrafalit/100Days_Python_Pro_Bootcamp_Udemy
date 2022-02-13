import random
from HigerLower.game_data import data

def compare(q1,q2):
    print("Compare A: " + q1['name'] + " a " + q1['description'] + ", from " + q1['country'] +"." )
    print(q1['follower_count'] , " VS " ,q2['follower_count'])
    print("Compare B: " + q2['name'] + " a " + q2['description'] + ", from " + q2['country'] + ".")

def check(q1,q2):
    answer = input("Who has more followers? Type 'A' or 'B': ")
    global score
    more_f = ''
    if answer == "A" or answer == "a":
        answer = 'q1'
    elif answer == "B" or answer == "b":
        answer = 'q2'
    if (q1['follower_count'] > q2['follower_count']):
        more_f = 'q1'
    elif (q1['follower_count'] < q2['follower_count']):
        more_f = 'q2'
    if answer == more_f:
        score += 1
        return False
    else:
        return True





score = 0

# print(questions[0])
# print(questions[0]['name'])
question1 = random.choice(data)
question2 = random.choice(data)
game_off = False
while not game_off:
    if score > 0:
        print("You're right!. Current score: ", score)
    compare(question1,question2)
    game_off = check(question1,question2)
    print("\n" * 10)
    question1 = question2
    question2 = random.choice(data)
else:
    print("Sorry, that's wrong. Final score: ", score)