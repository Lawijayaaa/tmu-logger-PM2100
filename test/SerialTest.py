#!/usr/bin/env python3
from pymodbus.client import ModbusSerialClient
import time

#init modbus device
client = ModbusSerialClient(method='rtu', port='/dev/ttyACM0', baudrate=9600)
loop = False

def testBatch():
    getElect1 = client.read_holding_registers(2999, 8, slave = 2)
    getElect2 = client.read_holding_registers(3019, 14, slave = 2)
    getElect3 = client.read_holding_registers(3053, 24, slave = 2)
    getElect4 = client.read_holding_registers(3077, 18, slave = 2)
    getElect5 = client.read_holding_registers(3213, 20, slave = 2)
    getElect6 = client.read_holding_registers(21299, 24, slave = 2)
    
    print(getElect1)
    print(getElect2)
    print(getElect3)
    print(getElect4)
    print(getElect5)
    print(getElect6)
    
    print("~~~")

#Loop
if loop:
    while True:
        testBatch()
        time.sleep(2)
else:   
    testBatch()
