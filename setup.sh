#!/bin/bash

echo "installing apt"
sudo apt-get install -y libffi-dev python-dev python3-dev libportaudio2 python3-libgpiod
echo "installing python lib"
python3 -m pip install adafruit-blinka sounddevice playsound adafruit-circuitpython-mpu6050
sudo python3 -m pip install adafruit-blinka sounddevice playsound adafruit-circuitpython-mpu6050
echo "installing sudo python lib"