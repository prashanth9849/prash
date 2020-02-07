import os
myfolder="/home/pi/Desktop"
def onMyButtonClick():
     os.system("pcmanfm \"%s\"" % myfolder)
