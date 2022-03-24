
from gpiozero import Button, LED, PWMLED
from time import sleep
from lobe import ImageModel
import pygame
import pygame.camera

button = Button(11)
yellow_led = LED(16) #glass
blue_led = LED(24) #cardboard
green_led = LED(18) #metal
red_led = LED(1) #plastic
white_led = LED(14) #paper
red2_led = PWMLED(26) #Status light and retake photo


pygame.camera.init()


model = ImageModel.load('/home/pi/model')

def take_photo():
    
    red2_led.blink(0.1,0.1)
    sleep(2)
    print("Pressed")
    red2_led.on()
    
    camlist = pygame.camera.list_cameras()
    cam = pygame.camera.Camera(camlist[0], (640, 480))
    cam.start()
    sleep(3) 
    image = cam.get_image()
    pygame.image.save(image, "/home/pi/images/image.jpg")
    cam.stop()
    red2_led.off()
    sleep(1)


def led_select(label):
    print(label)
    if label == "glass":
        yellow_led.on()
        sleep(5)
    if label == "cardboard":
        blue_led.on()
        sleep(5)
    if label == "metal":
        green_led.on()
        sleep(5)
    if label == "plastic":
        red_led.on()
        sleep(5)
    if label == "paper":
        white_led.on()
        sleep(5)
    if label == "not trash!":
        red2_led.on()
        sleep(5)
    else:
        yellow_led.off()
        blue_led.off()
        green_led.off()
        red_led.off()
        white_led.off()
        red2_led.off()


while True:
    if button.is_pressed:
        take_photo()
        result = model.predict_from_file('/home/pi/images/image.jpg')
        led_select(result.prediction)
    else:
        red2_led.pulse(2,1)
    sleep(1)