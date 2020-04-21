from time import time
from datetime import datetime
from pygame import mixer

def playmusic(song_name, stopper):
    mixer.init()
    mixer.music.load(song_name)
    mixer.music.set_volume(0.7)
    mixer.music.play()
    while True:
        user_input = input()
        if user_input == stopper:
            mixer.music.stop()
            break


def dranked(action):
    with open("log.txt", "a") as log:
        log.write(f"{action} at {datetime.now()}\n")


if __name__ == '__main__':
    water_reminder = 30*60
    eye_reminder = 40*60
    physical_reminder = 50*60
    water_strt = time()
    eye_strt = time()
    physical_strt = time()
    print("-------Welcome to our Healthcare system-------")
    print("I care for you!")
    print("Now i'll give reminder to drink water in every 30 min.\n"
          "and to relax your eye in every 40 min.\n"
          "and to get up and walk for sometime in every 50 min.\n"
          "and your all record will be saved in 'log.txt' file\n"
          "-----------Happy Coding!---------\n")
    while True:
        if time() - water_strt > water_reminder:
            print("Water drinking time. Enter 'drank' to stop the reminder")
            playmusic('water.mp3', 'drank')
            water_strt = time()
            dranked("Water Dranked!")
        if time() - eye_strt > eye_reminder:
            print("Eye relaxing time. Enter 'relaxed' to stop the reminder")
            playmusic('eye.mp3', 'relaxed')
            water_strt = time()
            dranked("Eye Relaxed!")
        if time() - physical_strt > physical_reminder:
            print("Exercise time. Enter 'done' to stop the reminder")
            playmusic('physical.mp3', 'done')
            water_strt = time()
            dranked("Exercise Done!")



