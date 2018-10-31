import pygame
from pygame.mixer import Sound
from gpiozero import MotionSensor
from time import sleep
import random

pygame.init()
pygame.mixer.init()

#get the sound files from directory(.ogg files only)
sounds = [
        pygame.mixer.Sound("/home/pi/Music/drone.ogg"), #files are stored in the /Music directory
        pygame.mixer.Sound("/home/pi/Music/reversed_vocals.ogg"),
        pygame.mixer.Sound("/home/pi/Music/ghost_sounds.ogg"),
        pygame.mixer.Sound("/home/pi/Music/monster_growl.ogg")
        ]

# uses GPIO pin 4 for sensor input 
pir = MotionSensor(4)
while True:
    if pir.motion_detected:
        print("Motion Detected!")
        playSound = random.choice(sounds)
        playSound.play()
        # Let's the sound play fully before continuing
        sleep(10)
        playSound.stop()
    else:
        print ("No Motion!")
