"""Example main for reference"""

import LuxDataCollection as ldc
import random as rand

#Create random test numbers

acc = rand.randint(0,100)
num_o_p = rand.randint(0,1000)

if __name__ == "__main__":
    #Set the com port, check available com ports with control panel or ArduinoIDE
    Apin = ldc.set_com("COM8")
    print("Board Communicated with")
    #Collect lux value
    lux = ldc.collect_lux(Apin)
    print("Lux calculated: ", lux)

    #Input data into csv passing in params
    ldc.csv_data(lux, acc, num_o_p)
    print("CSV data collected ")

    """Note: We ideally want the com port and lux collection to be the first thing the program does 
    and the csv data collection the last thing, if you want to set a path, add a path parameter into csv_data"""
