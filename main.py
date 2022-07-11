import machine
import utime

led_onboard = machine.Pin(25, machine.Pin.OUT)
#f = open("tempLogFile.txt", "x")

while True:
        #This turns the onboard LED ON and OFF
        led_onboard.value(0)
        utime.sleep(2)
        led_onboard.value(1)
        utime.sleep(10)
        
        #This reads the onboard TEMPSENSOR built into RP2040 chip
        sensor_temp = machine.ADC(4)
        
        #This calculated the Celsius and Fahrenheit values
        CONVERSION_FACTOR = 3.3 / (65535)
        reading = sensor_temp.read_u16() * CONVERSION_FACTOR
        temperature_celsius = 27 - (reading - 0.706)/0.001721
        temperature_fahrenheit = (temperature_celsius * 9/5) + 32
        
        #Rounds the temp values
        temperature_fahrenheit = round(temperature_fahrenheit, 2)
        temperature_celsius = round(temperature_celsius, 2)
        
        #This outputs formatted values to the console 
        print("Celsius: ", temperature_celsius, " |  Fahrenheit: ", temperature_fahrenheit)
        
        #This appends the Temp reading to the TempLogFile.txt
        f = open("TempLogFile.txt", "a")
        f.write("Celsius: ")
        f.write(f"{temperature_celsius}")
        f.write("| Fahrenheit: ")
        f.write(f"{temperature_fahrenheit}")
        f.write("\n")
        f.close()
        
        
