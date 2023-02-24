# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 11:08:16 2023

@author: HAGAN NANA KWEKU GYANYI 6937921
GiTHUB Account: 2002NANA-HAGAN"""

# list of available cars and their prices 
cars ={ 
"Toyota Camry": 50000,
"Lamborghini aventador": 450000,
"SUV":90000,
"Ford Explorer":70000,
"BMW X7 2023 model": 200000,
"VW Golf 7": 80000,
"Hyundai Elantra": 60000,
"Toyota RAV 4": 70000,
"Kia Rio": 55000,
"honda civic":40000,
"hyundai accent":35000,
"Kia picanto":32000,
"ford focus":44000,
"kia soul": 30000,
"suzuki celerio": 49000,
"dodge charger": 60000,
"chevrolet bolt": 70000,
"bugatti veyron":800000,
"aston martin one-77": 750000,
}
# get user input for car name
car_name = int("Enter a car_name:)"
# check if car name is in the list of available cars
if car_name in cars
 print ("yes")
 #if car name is present, get its price
 car_price = cars[car_name]
 print( f "The price of {car_name} is ${car_price}.” )
else:
 # if car name is not present, inform the user
 print(f "Sorry, {car_name} is not available.” )