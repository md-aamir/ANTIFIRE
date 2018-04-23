##                                            SYNTAX ERROR
from mcp3208 import MCP3208 
import time
import sqlite3


adc = MCP3208()


averageValue    =  10                   # Change It As Per Need
temp_Variance   =  15.02317             # To Get Correct Temperature Value
smoke_pin       =  0                    # Smoke Pin To Channel 0 Of MCP3208
temp_pin        =  2                    # Temperature Pin To Channel 1 Of MCP3208
smoke_value     =  0                    # Initial Value As 0 For smoke_value
temp_value      =  0                    # Initial Value As 0 For temp_value
round_value     =  2
degree_sign     =  u'\N{DEGREE SIGN}'   # Degree Sign ( ° )

def setup(times=1):
	while True:
		smoke_value=0
		temp_value=0
		
		for i in range(times):
			smoke_value      =      smoke_value + adcread(smoke_pin)
			temp_valueTEMP   =      adcread(temp_pin)
			temp_value       =      temp_value  +   (((temp_valueTEMP/1024)*500)-temp_Variance)
		
		smoke_value  =   smoke_value/times
		temp_value   =   temp_value/times
		
		print("Temperature :- ",temp_value,degree_sign,"C","		","Smoke :- ",smoke_value,"ppm")
		time.sleep(10)


def adcread(i):
	temp = adc.read(i)/4
	return temp


def temp(times=1):
	
	temp_value=0
	
	for i in range(times):
		temp_valueTEMP   =      adcread(temp_pin)
		temp_value       =      temp_value  +   (((temp_valueTEMP/1024)*500)-temp_Variance)
	
	temp_value   =   temp_value/times
	
	return temp_value


def smoke(times=1):
	
	smoke_value=0
	
	for i in range(times):
		smoke_value      =      smoke_value + adcread(smoke_pin)
	
	smoke_value  =   smoke_value/times
	
	return smoke_value


def adcread(i):
	temp = adc.read(i)/4
	return temp


def save():
	conn=sqlite3.connect('sensorsData.db')
	
	curs=conn.cursor()
	
	
	smoke_value=round(smoke(),round_value)
	temp_value=round(temp(),round_value)
	
	curs.execute("INSERT INTO DHT_data values(datetime('now'), (?), (?))", (temp_value, smoke_value))
	conn.commit()
	
	print ("\nEntire database contents:\n")
	for row in curs.execute("SELECT * FROM DHT_data"):
		print (row)
	
	
	conn.close()

if __name__=='__main__':
	while True:
            save()
            time.sleep(2)