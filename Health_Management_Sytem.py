
# HEALTH MANAGEMENT SYSTEM

def getdate():
    import datetime
    return datetime.datetime.now()


current_time = str(getdate())


def health_system():

    print("WELCOME TO HEALTH MANAGEMENT SYSTEM!!")

    a = int(input("Enter:- \n"
                  "1 -> View Logs \n"
                  "2 -> Enter Logs \n"
                  ": "))

    if a == 2:

        b = int(input("Enter:- \n"
                      "1 for Lakshya \n"
                      "2 for Anushka \n"
                      "3 for Hanu \n"
                      ": "))

        if b == 1:                                  # LAKSHYA
            c = int(input("Enter:- \n"
                          "1 for Food Logs \n"
                          "2 for Excercise Logs  \n"
                          ": "))

            if c == 1:
                log = input("Enter food you ate: ")
                f = open("lakshya_food_log.txt", "a")
                f.write("[" + current_time + "]" + " -> " + log + "\n")
                print("Record Added Sucessfully!")
                f.close()

            elif c == 2:
                log = input("Enter excercise you did: ")
                f = open("lakshya_excercise_log.txt", "a")
                f.write("[" + current_time + "]" + " -> " + log + "\n")
                print("Record Added Sucessfully!")
                f.close()

            else:
                print("WRONG INPUT!!")

        elif b == 2:                                # ANUSHKA
            c = int(input("Enter:- \n"
                          "1 for Food Logs \n"
                          "2 for Excercise Logs  \n"
                          ": "))

            if c == 1:
                log = input("Enter food you ate: ")
                f = open("anushka_food_log.txt", "a")
                f.write("[" + current_time + "]" + " -> " + log + "\n")
                print("Record Added Sucessfully!")
                f.close()

            elif c == 2:
                log = input("Enter excercise you did: ")
                f = open("anushka_excercise_log.txt", "a")
                f.write("[" + current_time + "]" + " -> " + log + "\n")
                print("Record Added Sucessfully!")
                f.close()

            else:
                print("WRONG INPUT!!")

        elif b == 3:                                # HANU
            c = int(input("Enter:- \n"
                          "1 for Food Logs \n"
                          "2 for Excercise Logs  \n"
                          ": "))

            if c == 1:
                log = input("Enter food you ate: ")
                f = open("hanu_food_log.txt", "a")
                f.write("[" + current_time + "]" + " -> " + log + "\n")
                print("Record Added Sucessfully!")
                f.close()

            elif c == 2:
                log = input("Enter excercise you did: ")
                f = open("hanu_excercise_log.txt", "a")
                f.write("[" + current_time + "]" + " -> " + log + "\n")
                print("Record Added Sucessfully!")
                f.close()

            else:
                print("WRONG INPUT!!")

    elif a == 1:

        b = int(input("Enter:- \n"
                      "1 for Lakshya \n"
                      "2 for Anushka \n"
                      "3 for Hanu \n"
                      ": "))

        if b == 1:                              # LAKSHYA
            c = int(input("Enter:- \n"
                          "1 for Food Logs \n"
                          "2 for Excercise Logs \n"
                          ": "))

            if c == 1:
                print("Lakshya's food log are: \n")
                f = open("lakshya_food_log.txt", "r")
                log = f.read()
                print(log)
                f.close()

            elif c == 2:
                print("Lakshya's excercise logs are: \n")
                f = open("lakshya_excercise_log.txt", "r")
                log = f.read()
                print(log)
                f.close()

            else:
                print("WRONG INPUT!!")

        elif b == 2:                                  # ANUSHKA
            c = int(input("Enter:- \n"
                          "1 for Food Logs \n"
                          "2 for Excercise Logs \n"
                          ": "))

            if c == 1:
                print("Anushka's food log are: \n")
                f = open("anushka_food_log.txt", "r")
                log = f.read()
                print(log)
                f.close()

            elif c == 2:
                print("Anushka's excercise logs are: \n")
                f = open("anushka_excercise_log.txt", "r")
                log = f.read()
                print(log)
                f.close()

            else:
                print("WRONG INPUT!!")

        elif b == 3:                                  # HANU
            c = int(input("Enter:- \n"
                          "1 for Food Logs \n"
                          "2 for Excercise Logs \n"
                          ": "))

            if c == 1:
                print("Hanu's food log are: \n")
                f = open("hanu_food_log.txt", "r")
                log = f.read()
                print(log)
                f.close()

            elif c == 2:
                print("Hanu's excercise logs are: \n")
                f = open("hanu_excercise_log.txt", "r")
                log = f.read()
                print(log)
                f.close()

            else:
                print("WRONG INPUT!!")

        else:
            print("WRONG INPUT!!")

    re_run = input("Want to run again (Y/N): ")

    if re_run.capitalize() == 'Y':
        health_system()

    elif re_run.capitalize() == 'N':
        print("Have a good day!")

    else:
        print("WRONG INPUT!!")


health_system()