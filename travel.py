# -*- coding: utf-8 -*-
from traverser import Traverser
import random
from city import City

class Travel:
    
    tour = []
    distance = 0
    
    def __init__(self, tour = [None]*30):
        self.tour = tour.copy()
        
    def get_tour(self):
        return self.tour
    
    def generate_individual(self):
        for i in range(0, Traverser.number_of_cities()):
            self.set_city(i, Traverser.get_city(i))
        random.shuffle(self.tour)
   
    def get_city(self, tour_pos):
        return self.tour[tour_pos]
    
    def set_city(self, tour_pos, city: City):
        self.tour[tour_pos] = city
        self.distance = 0
        
    def get_distance(self):
        if self.distance == 0:
            tour_dist = 0
            for i in range(0, self.tour_size()):
                from_city = self.get_city(i)
                dest_city = City ()
                
                if i+1 < self.tour_size():
                    dest_city = self.get_city(i+1)
                else:
                    dest_city = self.get_city(0)
                tour_dist += from_city.distance_to(dest_city)
            self.distance = tour_dist
        return self.distance
            
            
    def tour_size(self):
        return len(self.tour)
    
    def __str__(self):
        gene_string = "|"
        for i in range(0, self.tour_size()):
            gene_string += str(self.get_city(i)) 
        return gene_string + str(self.get_city(0)) + "|"
    