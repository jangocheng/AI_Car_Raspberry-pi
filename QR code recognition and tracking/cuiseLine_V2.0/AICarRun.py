#coding: utf-8
# AI car motor drive
# zdl 2018-07-11

import RPi.GPIO as GPIO
import time
import threading
#电机引脚定义
AIN1 = 6
AIN2 = 13
BIN1 = 26
BIN2 = 19
#设置速度
RunSpeed = 60
TurnSpeed = 60
#设置GPIO口为BCM编码方式
GPIO.setmode(GPIO.BCM)
#忽略警告信息
GPIO.setwarnings(False)

#电机引脚初始化操作
def motor_init():
    GPIO.setmode(GPIO.BCM)
    global pwm_ENA1
    global pwm_ENA2
    global pwm_ENB1
    global pwm_ENB2
    #初始化GPIO引脚
    GPIO.setup(AIN1,GPIO.OUT,initial=GPIO.HIGH)
    GPIO.setup(AIN2,GPIO.OUT,initial=GPIO.HIGH)
    GPIO.setup(BIN1,GPIO.OUT,initial=GPIO.HIGH)
    GPIO.setup(BIN2,GPIO.OUT,initial=GPIO.HIGH)
    #初始化PWM频率
    pwm_ENA1 = GPIO.PWM(AIN1,2000)
    pwm_ENA2 = GPIO.PWM(AIN2,2000)
    pwm_ENB1 = GPIO.PWM(BIN1,2000)
    pwm_ENB2 = GPIO.PWM(BIN2,2000)
    pwm_ENA1.start(0)
    pwm_ENA2.start(0)
    pwm_ENB1.start(0)
    pwm_ENB2.start(0)

#car Forward
def run(delaytime):
    pwm_ENA1.ChangeDutyCycle(RunSpeed)
    pwm_ENA2.ChangeDutyCycle(0)
    pwm_ENB1.ChangeDutyCycle(RunSpeed+3)
    pwm_ENB2.ChangeDutyCycle(0)
    time.sleep(delaytime)
    
#car Reverse
def back(delaytime):
    pwm_ENA1.ChangeDutyCycle(0)
    pwm_ENA2.ChangeDutyCycle(RunSpeed)
    pwm_ENB1.ChangeDutyCycle(0)
    pwm_ENB2.ChangeDutyCycle(RunSpeed+3)
    time.sleep(delaytime)

#car right
def right(delaytime):
    pwm_ENA1.ChangeDutyCycle(TurnSpeed)
    pwm_ENA2.ChangeDutyCycle(0)
    pwm_ENB1.ChangeDutyCycle(0)
    pwm_ENB2.ChangeDutyCycle(TurnSpeed)
    time.sleep(delaytime)

#car left
def left(delaytime):
    pwm_ENA1.ChangeDutyCycle(0)
    pwm_ENA2.ChangeDutyCycle(TurnSpeed)
    pwm_ENB1.ChangeDutyCycle(TurnSpeed)
    pwm_ENB2.ChangeDutyCycle(0)
    time.sleep(delaytime)

#car stop
def brake(delaytime):
    pwm_ENA1.ChangeDutyCycle(100)
    pwm_ENA2.ChangeDutyCycle(100)
    pwm_ENB1.ChangeDutyCycle(100)
    pwm_ENB2.ChangeDutyCycle(100)
    time.sleep(delaytime)

def r_forward(Rduty, Lduty):
    # add span func
    if Rduty < 0:
        Rduty = -Rduty
        pwm_ENA1.ChangeDutyCycle(0)
        pwm_ENA2.ChangeDutyCycle(Rduty)
        pwm_ENB1.ChangeDutyCycle(Lduty)
        pwm_ENB2.ChangeDutyCycle(0)
    elif Lduty < 0:
        Lduty = -Lduty
        pwm_ENA1.ChangeDutyCycle(Rduty)
        pwm_ENA2.ChangeDutyCycle(0)
        pwm_ENB1.ChangeDutyCycle(0)
        pwm_ENB2.ChangeDutyCycle(Lduty)
    else:
        pwm_ENA1.ChangeDutyCycle(0)
        pwm_ENA2.ChangeDutyCycle(Rduty)
        pwm_ENB1.ChangeDutyCycle(0)
        pwm_ENB2.ChangeDutyCycle(Lduty)
def l_forward(Rduty, Lduty):
    pwm_ENA1.ChangeDutyCycle(Rduty)
    pwm_ENA2.ChangeDutyCycle(0)
    pwm_ENB1.ChangeDutyCycle(Lduty)
    pwm_ENB2.ChangeDutyCycle(0)
