from app import app
import RPi.GPIO as GPIO
import spidev
import time

spi = 0

def init_spi():
	global spi
	spi = spidev.SpiDev()
	spi.open(0,1)
	spi.max_speed_hz = 100000
	spi.mode = 0b00

	GPIO.setmode(GPIO.BCM)
	GPIO.setup(24,GPIO.OUT,initial=GPIO.HIGH)
	GPIO.setup(8,GPIO.OUT,initial=GPIO.HIGH)
	# GPIO.setup(7,GPIO.OUT,initial=GPIO.HIGH)


class ReadCRCError(Exception):
	pass

class ReadNoAck(Exception):
	pass

def CRC8(dataList,initial=0,poly=0x07):
	crc = 0x00
	for inByte in dataList:
		for i in range(8):
			temp = (crc^inByte)&0x80
			crc <<= 1
			if temp != 0:
				crc ^=poly
			inByte <<= 1
		crc &= 0xFF
	return crc

def writeCommand(dataList):
	global spi
	dataList = [len(dataList)+2]+dataList
	dataList.append(CRC8(dataList))
	# print("spi packet: ",[hex(x) for x in dataList])
	GPIO.output(8,GPIO.LOW)
	spi.xfer(dataList,100000,10,8)
	GPIO.output(8,GPIO.HIGH)

def readCommand(command):
	global spi
	dataList = [1,command,0,0]
	recList = []
	GPIO.output(8,GPIO.LOW)
	recList = spi.xfer(dataList,100000,10,8)
	if recList[2] != 0x01:
		raise ReadNoAck("Slave did not react to the read command! (No acknowledge)")
	if recList[3] < 0x03:
		raise ReadCRCError("Data length byte is too short!")
	length = recList[3]
	recList = [length]
	dataList = [0]*(length-1)
	recList = recList + spi.xfer(dataList,100000,10,8)
	GPIO.output(8,GPIO.HIGH)

	if (CRC8(recList) != 0) or (recList[1] != command):
		raise ReadCRCError("Transmission errors detected!")
	return recList[2:-1]