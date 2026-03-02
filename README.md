# JoyIT_RC522

A python library to read/write RFID tags via the MFRC522 RFID module.

This code was edited for the use with Raspberry Pi 5 by Joy-IT. Therefore the 'RPi.GPIO' library was exchanged with 'gpiozero'.The source code was published in relation to a [blog post](https://pimylifeup.com/raspberry-pi-rfid-rc522/) and you can find out more about how to hook up your MFRC reader to a Raspberry Pi there.


### Prerequirements:

SPI has to be enabled, otherwise a error message will be shown ("FileNotFoundError: [Errno 2] No such file or directory"). 

To enable SPI you can do the following:
```console
1. sudo raspi-config
2. Interface Options -> SPI -> Enable
```

## Installation

This library is for the use with virtual environments for the Raspberry Pi 5 and older models.

```console
mkdir your_project
cd your_project
python -m venv --system-site-packages env
source env/bin/activate

pip3 install spidev
pip3 install JoyIT_RC522
```

## Example
In this library are two example codes. One is for reading from a tag and the other is for writing on a tag. You can execute them like the following.

```console
git clone https://github.com/joy-it/MFRC522-python
python3 MFRC522-python/examples/write.py
python3 MFRC522-python/examples/read.py
```
