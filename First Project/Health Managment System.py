import datetime

def gettime():
    return datetime.datetime.now()

def client_addexe(client):
    if client == "1":
        add_retr = input("What do you want to Add: ")
        with open("Herry_exe.txt", "a") as herry:
            herry.write(add_retr)
            print("Added Successfully")
    if client == "2":
        add_retr = input("What do you want to Add: ")
        with open("Rohan_exc.txt", "a") as rohan:
            rohan.write(add_retr)
            print("Added Successfully")
    if client == "3":
        add_retr = input("What do you want to Add: ")
        with open("Hammad_exc.txt", "a") as hammad:
            hammad.write(add_retr)
            print("Added Successfully")

def client_retrexe(client):
    if client == "1":
            with open("Herry_exe.txt") as herry:
                show = herry.read()
                print(show)
    print("All the Items Shown Above")
    if client == "2":
            with open("Rohan_exc.txt") as rohan:
                show = rohan.read()
                print(show)
    print("All the Items Shown Above")
    if client == "3":
            with open("Hammad_exc.txt") as hammad:
                show = hammad.read()
                print(show)
    print("All the Items Shown Above")

def client_adddiet(client):
    if client == "1":
        add_retr = str(input("What do you want to Add: "))
        with open("Herry_diet.txt", "a") as herry:
            herry.write(add_retr)
            print("Added Successfully")
    if client == "2":
        add_retr = str(input("What do you want to Add: "))
        with open("Rohan_diet.txt", "a") as rohan:
            rohan.write(add_retr)
            print("Added Successfully")
    if client == "3":
        add_retr = str(input("What do you want to Add: "))
        with open("Hammad_diet.txt", "a") as hammad:
            hammad.write(add_retr)
            print("Added Successfully")


def client_retrdiet(client):
    if client == "1":
            with open("Herry_diet.txt") as herry:
                show = herry.read()
                print(show)
    print("All the Items Shown Above")
    if client == "1":
            with open("Rohan_diet.txt") as rohan:
                show = rohan.read()
                print(show)
    print("All the Items Shown Above")
    if client == "1":
            with open("Hammad_exc.txt") as hammad:
                show = hammad.read()
                print(show)
    print("All the Items Shown Above")


if __name__ == '__main__':
    client = input("Enter 1 for Herry, 2 for Rohan, 3 for Hammad: ")
    if client == "1":
            choice = input("Enter 1 for Add and 2 for Retrieve: ")
            if choice == "1":
                choice = input("Enter 1 for Exercise and 2 for Diet: ")
                if choice == "1":
                    client_addexe(client)
                if choice == "2":
                    client_adddiet(client)
            if choice == "2":
                choice = input("Enter 1 for Exercise and 2 for Diet: ")
                if choice == "1":
                    client_retrexe(client)
                if choice == "2":
                    client_retrdiet(client)

    if client == "2":
            choice = input("Enter 1 for Add and 2 for Retrieve: ")
            if choice == "1":
                choice = input("Enter 1 for Exercise and 2 for Diet: ")
                if choice == "1":
                    client_addexe(client)
                if choice == "2":
                    client_adddiet(client)
            if choice == "2":
                choice = input("Enter 1 for Exercise and 2 for Diet: ")
                if choice == "1":
                    client_retrexe(client)
                if choice == "2":
                    client_retrdiet(client)
    if client == "3":
            choice = input("Enter 1 for Add and 2 for Retrieve: ")
            if choice == "1":
                choice = input("Enter 1 for Exercise and 2 for Diet: ")
                if choice == "1":
                    client_addexe(client)
                if choice == "2":
                    client_adddiet(client)
            if choice == "2":
                choice = input("Enter 1 for Exercise and 2 for Diet: ")
                if choice == "1":
                    client_retrexe(client)
                if choice == "2":
                    client_retrdiet(client)









