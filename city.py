# -*- coding: utf-8 -*-
import random
import math

class City:
    
    def __init__(self,
                 name: str = "Default",
                 longitude: int = random.random() * 200,
                 latitude: int = random.random() * 200):
        self.name = name
        self.longitude = longitude 
        self.latitude = latitude
    
    def get_name(self):
        return self.name
        
    def get_longitude(self):
        return self.longitude
    
    def get_latitude(self):
        return self.latitude
    
    def distance_to(self, city: 'City'):
        first = math.sin(self.get_longitude()) * math.sin(city.get_longitude())
        second = math.cos(self.get_longitude()) * math.cos(city.get_longitude())
        third = math.cos(city.get_latitude() - self.get_latitude())
        return 6400*math.acos(first + second*third) 
    
    def __str__(self):
        return f'{self.get_name()}->'
    
