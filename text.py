
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306, ssd1325, ssd1331, sh1106
import time

serial = i2c(port=1, address=0x3C)
device = ssd1306(serial, rotate=0)

i = 0
while 1:
	with canvas(device) as draw:
		draw.rectangle(device.bounding_box, outline="white", fill="black")
		draw.text((i*1,40), "Hi there!", fill="white")
		#time.sleep(1)
		i = (i+1) % 100


