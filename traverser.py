# -*- coding: utf-8 -*-
from city import City

class Traverser(object):
    
    _destination_cities = []
    
    @property
    def destination_cities(self):
        return type(self)._destination_cities
    
    @destination_cities.setter
    def destination_cities(self, val):
        type(self)._destination_cities = val
    
    @classmethod
    def get_city(cls, index: int):
        return cls._destination_cities[index]
    
    @classmethod
    def add_city(cls, city: City):
        cls._destination_cities.append(city)
        
    @classmethod    
    def number_of_cities(cls):
        return len(cls._destination_cities)