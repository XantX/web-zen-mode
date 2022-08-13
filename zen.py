# import shutil
# shutil.copy("test", "C:/Windows/System32/drivers/etc")
# Leer configuracion
import datetime
import os
from common.timeConfig import timeConfig


def limpiar():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")


fTime = open('config', 'r')

times = fTime.readlines()

configTime = timeConfig()

configTime.setTimes(times)


limpiar()
print("Termina en:", str(configTime.finalHour) + ":" + str(configTime.finalMin))
while True:
    tiempo = datetime.datetime.now()
    print("Tiempo actual:", str(tiempo.hour) + ":" + str(tiempo.minute) + ":" + str(tiempo.second), end="\r")
    if tiempo.hour == configTime.initHour and tiempo.minute == configTime.initMin:
        print("Times Init")
    if tiempo.hour == configTime.finalHour and tiempo.minute == configTime.finalMin:
        print("Time Finish")
        break
