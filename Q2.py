
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
    split_amount = round(bill / num_people, 2)

    for friend in friends:
        friends[friend] = split_amount

    print(friends)