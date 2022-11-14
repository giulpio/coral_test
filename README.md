
# Sedia_2 hardware test

sedia_2 software to test the main board.

To manage all the components on the board, the following libraries have been created
```
 led.py
 gyro.py
 mic.py
 i2c.py
 buttons.py
```

## Requirements
- coral devboard mini
- sedia_2 main board
- 2*usb_c cable
- preferred Linux PC
- ttl -> USB cable converter (recommended, not necessary)

## Coral Setup

visit [coral setup webpage](https://coral.ai/docs/dev-board-mini/get-started/)
## Installation

Open ssh interface on your PC and connect with coral

Clone the project

```bash
  git clone https://link-to-project
```

Go to the project directory

```bash
  cd coral_test
```

Install dependencies

```bash
  /bin/bash setup.sh
```
Reboot system

```bash
  reboot
```

## Authors

Developed for FINH by Materea

- [@GiulioMilani](https://github.com/GiulioAtMaterea)

