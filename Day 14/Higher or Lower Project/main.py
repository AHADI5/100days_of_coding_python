from random import random

import game_data
import art
import random


def random_data(data):
    """
    randomly choose thing a
    randomly choose thing b

    :return: object for comparison
    """

    thing_a = random.choice(data)
    thing_b = random.choice(data)
    #     insuring that thing a and thing b are different

    while thing_a == thing_b:
        thing_b = random.choice(data)

    return thing_a, thing_b


def compare_print(a, b):

    print("Compare : ")
    print(f"{a['name']} {a['description']}, from {a['country']} ")
    print(art.vs)
    print(f"{b['name']} , {b['description']} ")

def compare_logic(obj1 , obj2) :

    highest_followers  = 0
    highest_followers_obj = obj1
    for obj in (obj1 , obj2) :
        if obj['follower_count'] > highest_followers  :
            highest_followers = obj['follower_count']
            highest_followers_obj = obj

    return  highest_followers_obj

print(art.logo)
# generated
rand_a , rand_b  = random_data(data = game_data.data)
user_obj  = {}
compare_print(rand_a ,rand_b)
user_choice = input("Who has more followers , type A or B").upper()
score  = 0
replay  = False

if user_choice == "A" :
    user_obj  = rand_a
else :
    user_obj = rand_b

if user_obj  == compare_logic(rand_a , rand_b ) :
    print(f"You win the game {user_obj}")
    replay = True
    score +=  1
else  :
    print("You failed")
    replay = False

while replay :
    rand_a, rand_b = random_data(data=game_data.data)

    prev_user_obj = user_obj
    compare_print(prev_user_obj, rand_b)

    user_choice = input("Who has more followers , type A or B").upper()
    if user_choice == "A":
        user_obj = prev_user_obj
    else:
        user_obj = rand_b

    if user_obj == compare_logic(prev_user_obj, rand_b):
        print(f"You win the game {user_obj}")
        replay = True
        score += 1
    else:
        print("You failed")
        replay = False
print(f"Score : {score}" )








