#!/bin/bash

echo "########### update apt ############################"
sudo apt update
echo "########### upgrade apt ############################"
sudo apt upgrade
echo "########### installing apt dependencies ###########"
sudo apt-get install -y libffi-dev python-dev python3-dev libportaudio2 python3-libgpiod 
echo "########### installing python lib ###########"
python3 -m pip install adafruit-blinka sounddevice playsound adafruit-circuitpython-mpu6050 
echo "########### installing sudo python lib ###########"
sudo python3 -m pip install adafruit-blinka sounddevice playsound adafruit-circuitpython-mpu6050 

