
import time
from pygame import mixer


import datetime
log_time = str(datetime.datetime.now())
# print(a)

current_time = time.strftime('%H:%M:%S')
start_time = '09:00:00'
end_time = '17:00:00'

total_glass_of_water = 18
glass_of_water_drank = 0
water_after = int((8*60*60)/18)
# water_after = 5
eyes_after = 30*60 - water_after
# eyes_after = 8
exercise_after = 45*60 - (water_after + eyes_after)
ask_ques = ""
work_done = ''
no_work_done = ''


def drink_water():

    file = 'water.mp3'
    time.sleep(water_after)
    global glass_of_water_drank

    while glass_of_water_drank != total_glass_of_water:

        global ask_ques
        global no_work_done
        print("\nTime to drink Water!")
        # time.sleep(2)
        ask_ques = "Did you drank water?: "
        no_work_done = "Please drink water!"
        # print(time.time())
        play_music(file)

        if work_done.lower() == 'yes':

            glass_of_water_drank += 1

            with open("logs.txt", "a") as f:
                f.write(f"Drank water at {log_time} \n")

            break


def rest_eye():

    file = 'eyes.mp3'

    time.sleep(eyes_after)
    global ask_ques
    global no_work_done
    print("\nTime to give break to your eyes!")
    ask_ques = "Did you gave break to your eyes?: "
    no_work_done = "Please give rest to your eyes!"
    # print(time.time())
    play_music(file)

    if work_done.lower() == 'yes':

        with open("logs.txt", "a") as f:
            f.write(f"Gave rest to eyes at {log_time} \n")


def exercise():

    file = 'excercise.mp3'

    time.sleep(exercise_after)
    global ask_ques
    global no_work_done
    print("\nTime to exercise!")
    ask_ques = "Did you exercised?: "
    no_work_done = "Please Exercise!"
    # print(time.time())
    play_music(file)

    if work_done.lower() == 'yes':

        with open("logs.txt", "a") as f:
            f.write(f"Exercised at {log_time} \n")


def play_music(file):

    # pygame.init()
    mixer.init()
    mixer.music.load(file)
    mixer.music.set_volume(9)
    mixer.music.play(-1)

    while mixer.music.get_busy():
        global work_done
        global no_work_done
        work_done = input(f"{ask_ques}")

        if work_done.lower() == 'yes':
            stop_music()

        elif work_done.lower() == 'no':
            print(f"{no_work_done}")

        else:
            play_music(file)


def stop_music():

    # time.sleep(5)
    mixer.music.stop()


if start_time < current_time < end_time:

    if __name__ == '__main__':

        while True:
            print(f"\nStarted at: {time.strftime('%H:%M:%S')}")

            drink_water()
            rest_eye()
            exercise()

else:
    print("\nNot office hours!")
    input("\nPress Enter to exit")

