import datetime
import time

def parse(data):
    # print("got mec10 data: " + data)
    int_value = int("0x"+data,16)

    #get solid temp
    tempValue =  (0xff0000000000000000000000 & int_value) >> 88
    tempValue += (0x001f00000000000000000000 & int_value) >> 72

    #recovery value range
    fTempValue = float(tempValue)/100.0
    # print("temp: " + str(fTempValue))

    #get vwc
    rawVWC  = (0x00E000000000000000000000 & int_value) >> 85
    rawVWC += (0x0000FF000000000000000000 & int_value) >> 69
    rawVWC += (0x000000070000000000000000 & int_value) >> 53
    # print("raw VWC" + str(rawVWC))
    fVWC = float(rawVWC)/100.0
    # print("vwc: " + str(fVWC))

    #get ec
    rawEC  = (0x000000F80000000000000000 & int_value) >> 67
    rawEC += (0x00000000FF00000000000000 & int_value) >> 51
    rawEC += (0x000000000003000000000000 & int_value) >> 35
    # print("raw EC: " + str(rawEC))

    #get salinity
    rawSal  = (0x0000000000FC000000000000 & int_value) >> 50
    rawSal += (0x000000000000FF0000000000 & int_value) >> 34
    rawSal += (0x000000000000000100000000 & int_value) >> 18
    # print("sal : " + str(rawSal))

    #gettds
    rawTDS  = (0x00000000000000FE00000000 & int_value) >> 33
    rawTDS += (0x0000000000000000FF000000 & int_value) >> 17
    # print("tds: " + str(rawTDS))

    #get epsilon
    rawEps  = (0x000000000000000000FF0000 & int_value) >> 16
    rawEps += (0x000000000000000000001F00 & int_value)
    # print("rawEPS: " + str(rawEps))
    fEps = float(rawEps)/100.0

#    param = {'field1':fTempValue,'field2':fVWC,'field3':rawEC,'field4':rawSal,'field5':rawTDS,'field6':fEps}
#    print(param)
    return [fTempValue, fVWC, rawEC, rawSal, rawTDS, fEps]
