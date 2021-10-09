print("\t\t\t\t\tSnake     Water     Gun")
your_points=0
computer_points=0
number_of_game=0
while(number_of_game<=9):
    import random
    list1=["Snake","Water","Gun"]
    game=random.choice(list1)
    num=input("Enter you choice\n")
    number_of_game=number_of_game+1
    number_of_choice_left=10-number_of_game
    if game=="Snake":
        if num=="s":
            print("Match tie\n")
            your_points=your_points+0
            computer_points=computer_points+0
            print(f"Your choice={num}\nComputer's choice={game}\nYour points {your_points}\nComputer's points {computer_points}")
        elif num=="w":
            print("You loose\n")
            your_points = your_points + 0
            computer_points = computer_points + 1
            print(f"Your choice={num}\nComputer's choice={game}\nYour points {your_points}\nComputer's points {computer_points}")
        elif num=="g":
            print("You win\n")
            your_points = your_points + 1
            computer_points = computer_points + 0
            print(f"Your choice={num}\nComputer's choice={game}\nYour points {your_points}\nComputer's points {computer_points}")
    elif game=="Water":
        if num=="s":
            print("You win\n")
            your_points=your_points+1
            computer_points=computer_points+0
            print(f"Your choice={num}\nComputer's choice={game}\nYour points {your_points}\nComputer's points {computer_points}")
        elif num=="w":
            print("Match tie\n")
            your_points = your_points + 0
            computer_points = computer_points + 0
            print(f"Your choice={num}\nComputer's choice={game}\nYour points {your_points}\nComputer's points {computer_points}")
        elif num=="g":
            print("You loose\n")
            your_points = your_points + 0
            computer_points = computer_points + 1
            print(f"Your choice={num}\nComputer's choice={game}\nYour points {your_points}\nComputer's points {computer_points}")
    elif game=="Gun":
        if num=="s":
            print("You loose\n")
            your_points=your_points+0
            computer_points=computer_points+1
            print(f"Your choice={num}\nComputer's choice={game}\nYour points {your_points}\nComputer's points {computer_points}")
        elif num=="w":
            print("You win\n")
            your_points = your_points + 1
            computer_points = computer_points + 0
            print(f"Your choice={num}\nComputer's choice={game}\nYour points {your_points}\nComputer's points {computer_points}")
        elif num=="g":
            print("Match tie\n")
            your_points = your_points + 0
            computer_points = computer_points + 0
            print(f"Your choice={num}\nComputer's choice={game}\nYour points {your_points}\nComputer's points {computer_points}")
    print(f"Number of choice left {number_of_choice_left}")