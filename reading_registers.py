import time
from pymodbus.client.sync import ModbusSerialClient
modbus = ModbusSerialClient(method='rtu', port='COM7', baudrate=9600, parity ='N', bytesize = 8, stopbits=1,unit=1)
modbus.connect()    

if not modbus.connect() :
    print("baglidegil")
    
if modbus.connect() :

    print("bagli")
    read=modbus.read_holding_registers(address= 6005,count = 1,unit = 1)

    print(read.registers)
    
    time.sleep(2)
