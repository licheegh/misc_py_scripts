import serial
import time
import datetime

class DataError(Exception):
    def __init__(self,data):
        self.data = data

def SendData(SerObj, Cmd, Number):
    """docstring for SendData"""
    time.sleep(0.05)
    SerObj.write(Cmd)
    t1=time.time()
    data = ser.read(1)
    t2=time.time()
    data = data + ser.read(Number-1)
    #print tinfo,
    tinfo = (t2-t1)*1000
    if len(data) != Number:
        return ["No Receive",tinfo,data]
    else:
        string = ' '.join(hex(ord(x))[2:] for x in data)
        return [string,tinfo,data]

def SendNKE(SerObj):
    """docstring for fname"""
    data = SendData(SerObj,SND_NKE,1)
    if data[2] != "\xE5":
        raise DataError(data[2])
        return data
    else:
        return data

ser = serial.Serial(port='COM9', baudrate=2400, timeout=0.5, parity=serial.PARITY_EVEN)
fdata = open("data.txt",'a')
print "Port Name:" + ser.name
#x = ser.read()          # read one byte
#s = ser.read(10)        # read up to ten bytes (timeout)
#line = ser.readline()   # read a '\n' terminated line
SND_NKE = "\x10\x40\xFD\x3D\x16" #1 byte return
REQ_UD2 = "\x10\x7B\xFD\x78\x16" #34 byte return

counter=0
tsum= 8.0 * 10
while True:
    print str(counter) + ": ",

    data = str(datetime.datetime.now())
    fdata.write(data + "\n")

    data = SendData(ser,SND_NKE,1)
    print "'"+data[0]+"'",
    data = data[0] + "\n"
    fdata.write(data)

    data = SendData(ser,REQ_UD2,33)
    tsum = tsum - tsum / 10
    tsum = data[1] + tsum
    tinfo="t:{:.3f}ms".format(tsum/10)
    print "'"+data[0]+"'" + tinfo,
    pinfo = data[0] + '\n'
    fdata.write(pinfo)
    
    fdata.write(tinfo + "\n")
    fdata.flush()
    counter = counter + 1
    print

    #time.sleep(20.0)

fdata.close()
ser.close()

