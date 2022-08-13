# import shutil
# shutil.copy("test", "C:/Windows/System32/drivers/etc")
# Leer configuracion
import datetime
from common.timeConfig import timeConfig

fTime = open('config', 'r')

times = fTime.readlines()

configTime = timeConfig()

configTime.setTimes(times)
print(configTime.initHour, configTime.initMin)
while True:
    tiempo = datetime.datetime.now()
    if tiempo.hour == int(configTime.initHour) and tiempo.minute == int(configTime.initMin):
        print("Times Up")
        break
