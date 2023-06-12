
import random
num_people = int(input("Enter the number of friends joining (including you):\n"))

if num_people <= 0:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    friends = {}
    for _ in range(num_people):
        name = input()
        friends[name] = 0

    bill = float(input("Enter the total bill value:\n"))

    use_lucky_feature = input("Do you want to use the 'Who is lucky?' feature? Write Yes/No:\n")

    if use_lucky_feature.lower() == "yes":
        lucky_person = random.choice(list(friends.keys()))
        print(f"{lucky_person} is the lucky one!")
    else:
        print("No one is going to be lucky")