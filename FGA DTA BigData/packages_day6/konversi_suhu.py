def celsius_fahrenheit(celsius):
    ''' fungsi konversi suhu celcius ke fahrenheit '''
    hasil = (celsius * 9/5) + 32 
    return hasil

def celsius_kelvin(celsius):
    ''' fungsi konversi suhu celcius ke kelvin '''
    hasil = celsius + 273.15 
    return hasil

def fahrenheit_celsius(fahrenheit):
    ''' fungsi konversi suhu fahrenheit ke celsius'''
    hasil = (fahrenheit - 32) * 5/9
    return hasil

def fahrenheit_kelvin(fahrenheit):
    ''' fungsi konversi suhu fahrenheit ke kelvin '''
    celsius = fahrenheit_celsius(fahrenheit)
    hasil = celsius_kelvin(celsius) 
    return hasil

def kelvin_celsius(kelvin):
    ''' fungsi konversi suhu kelvin ke celcius '''
    hasil = kelvin - 273.15 
    return hasil

def kelvin_fahrenheit(kelvin):
    ''' fungsi konversi suhu kelvin ke fahrenheit '''
    celsius = kelvin_celsius(kelvin)
    hasil = celsius_fahrenheit(celsius) 
    return hasil