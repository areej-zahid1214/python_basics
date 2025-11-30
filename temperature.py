class Temperature:
    def _init__(self, celsius):
        self.celsius = celsius
    def convert(self):
        fahrenheit = (self.celsius * 9/5) + 32
        kelvin = self.celsius + 273.15
        print("Celsius:", self.celsius)
        print("Fahrenheit:", fahrenheit)
        print("Kelvin:", kelvin)
celsius = float(input("Enter temperature in Celsius: "))
temp = Temperature(celsius)
temp.convert()