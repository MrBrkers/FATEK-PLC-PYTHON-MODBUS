
import time
from pymodbus.client.sync import ModbusSerialClient
modbus = ModbusSerialClient(method='rtu', port='COM7', baudrate=9600, parity ='N', bytesize = 8, stopbits=1,unit=1)
modbus.connect()    
if not modbus.connect() :
    print("baglidegil")
if modbus.connect() :
    #for setting a M bit (check the Modbus addresses of
    print("bagli")
    while modbus.connect():
        at = int(input("1 mi 0 mi : "))
        if at == 1 :
            result = modbus.write_coils(address = 2005,count=1,values=1,unit=1)
            print(result)
            #it sets M5 bit of FATEK FBs series PLC
    
            time.sleep(2)
        if at == 0 :
            result = modbus.write_coils(address = 2005,count=2,values=0,unit=1)
            print(result)
            
            time.sleep(2)
