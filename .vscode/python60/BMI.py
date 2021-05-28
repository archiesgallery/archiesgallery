import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

Height=float(input("Enter your height in centimeters: "))
Weight=float(input("Enter your weight in kg: "))
Height = Height/100
BMI=Weight/(Height*Height)
print("your Body Mass Index is: ",BMI)
if(BMI>0):
    if(BMI<=16):
        print(Fore.RED+Back.BLACK+"you are severely underweight")
    elif(BMI<=18.5):
        print(Fore.YELLOW+Back.BLACK+"you are underweight")
    elif(BMI<=25):
        print(Fore.BLACK + Back.GREEN+"you are Healthy")
    elif(BMI<=30):
        print(Fore.YELLOW+Back.MAGENTA+"you are overweight!")
    else:
        print(Fore.YELLOW+Back.RED+"you are severely overweight!!!!")
        print(Fore.BLACK+Back.GREEN+"please start exercies and proper diet!!")
else:("enter valid details")    