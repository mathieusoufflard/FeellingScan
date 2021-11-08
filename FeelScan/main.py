import os
import webbrowser
import random
import ia
import RPi.GPIO as GPIO

#LED
from rpi_ws281x import *
import argparse
LED_COUNT      = 60     
LED_PIN        = 18      
LED_FREQ_HZ    = 800000  
LED_DMA        = 10      
LED_BRIGHTNESS = 255     
LED_INVERT     = False   
LED_CHANNEL    = 0     

BUTTON_PIN = 2

Angry = ["https://www.youtube.com/embed/UfcAVejslrU?rel=0&autoplay=1",
         "https://www.youtube.com/embed/-fFbeSykaJk?rel=0&autoplay=1",
         "https://www.youtube.com/watch?v=UDVtMYqUAyw?rel=0&autoplay=1",
         "https://www.youtube.com/embed/2EfLc_jP2g8?rel=0&autoplay=1",
         "https://www.youtube.com/embed/6PAeMgE1pEQ?rel=0&autoplay=1",
         "https://www.youtube.com/watch?v=d-diB65scQU?rel=0&autoplay=1"]

Sad = ["https://www.youtube.com/embed/pUZeSYsU0Uk?rel=0&autoplay=1",
       "https://www.youtube.com/embed/oN2Xs-MvxLw?rel=0&autoplay=1",
       "https://www.youtube.com/watch?v=SJsGISX8O8k?rel=0&autoplay=1",
       "https://www.youtube.com/embed/lp-EO5I60KA",
       "https://www.youtube.com/watch?v=Sfqt2KtSj-Q"]

Happy = ["https://www.youtube.com/watch?v=-bl7bEw3kgw?rel=0&autoplay=1",
         "https://www.youtube.com/embed/HgzGwKwLmgM?rel=0&autoplay=1",
         "https://www.youtube.com/watch?v=btPJPFnesV4?rel=0&autoplay=1",
         "https://www.youtube.com/watch?v=tx0b39P1XCs?rel=0&autoplay=1",
         "https://www.youtube.com/watch?v=qK5KhQG06xU?rel=0&autoplay=1"]

Tired = ["https://www.youtube.com/watch?v=nxGoVw0DTGs?rel=0&autoplay=1",
         "https://www.youtube.com/embed/C9IwBJYTwQ0?rel=0&autoplay=1",
         "https://www.youtube.com/watch?v=uSD4vsh1zDA?rel=0&autoplay=1",
         "https://www.youtube.com/watch?v=OPf0YbXqDm0?rel=0&autoplay=1",
         "https://www.youtube.com/watch?v=iSLwVaebsJg?rel=0&autoplay=1"]

def setColorLed(strip, color, wait_ms=50):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)

def setColorLoadingLed(strip, color, wait_ms=50, iterations=10):
    for j in range(iterations):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, color)
            strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)

def runnning_commands_shell():
    os.system(
        'imagesnap -d NexiGo N930AF FHD Webcam /Users/franciskouaho/PycharmProjects/pythonProject1/uploads/capture.jpg')
    return ia.main()


def main():
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    strip.begin()
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
    try
         while True:
         etat = GPIO.input(BUTTON_PIN)   
         if (etat == 0) :
            print("Appui detecte")
            setColorLoadingLed(strip, Color(127,127,127), 200, 10)
            FEELING = runnning_commands_shell()
            if(FEELING == "Happy"):
                webbrowser.open(Happy[random.randint(0, 4)])
                setColorLed(strip, Color(255,255,128), 50)
            elif(FEELING == "Sad"):
                webbrowser.open(Sad[random.randint(0, 4)])
                setColorLed(strip, Color(25,217,255), 50)
            elif(FEELING == "Angry"):
                webbrowser.open(Angry[random.randint(0, 5)])
                setColorLed(strip, Color(179,102,255), 50)
            elif(FEELING == "Tired"):
                webbrowser.open(Tired[random.randint(0, 4)])
                setColorLed(strip, Color(56,171,30), 50)
            else:
                webbrowser.open(Happy[random.randint(0, 4)])
                setColorLed(strip, Color(204,136,16), 50)
                webbrowser.close

         # Temps de repos pour eviter la surchauffe du processeur
         time.sleep(0.3)
         
    except KeyboardInterrupt:
         setColorLed(strip, Color(0,0,0), 10)
         

main()
