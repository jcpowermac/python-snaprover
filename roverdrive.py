#!/usr/bin/python

import CHIP_IO.GPIO as GPIO
import time
import sys
import tty


def stop():
    GPIO.output("XIO-P2",GPIO.LOW)
    GPIO.output("XIO-P0",GPIO.LOW)
    GPIO.output("XIO-P3",GPIO.LOW)
    GPIO.output("XIO-P1",GPIO.LOW)


def main():
    tty.setcbreak(sys.stdin)
    GPIO.cleanup()
    pins = ["XIO-P0","XIO-P1","XIO-P2","XIO-P3"]
    for p in pins:
         GPIO.setup(p, GPIO.OUT)
         GPIO.output(p, GPIO.LOW)


    while True:
        try:
            key = ord(sys.stdin.read(1))

            if key == 32:
                stop()

            if key == 65:
                stop()
                GPIO.output("XIO-P3",GPIO.HIGH)
                GPIO.output("XIO-P1",GPIO.HIGH)
            if key == 66:
                stop()
                GPIO.output("XIO-P2",GPIO.HIGH)
                GPIO.output("XIO-P0",GPIO.HIGH)
            if key == 68:
                stop()
                GPIO.output("XIO-P2",GPIO.HIGH)
                GPIO.output("XIO-P1",GPIO.HIGH)
            if key == 67:
                stop()
                GPIO.output("XIO-P0",GPIO.HIGH)
                GPIO.output("XIO-P3",GPIO.HIGH)
        except Exception as e:
            pass


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass


