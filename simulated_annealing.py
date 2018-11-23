# -*- coding: utf-8 -*-
from city import City
from traverser import Traverser
import math
from travel import Travel
import random
import pandas as pd

from matplotlib import pyplot as plt

def acceptanceProbability(energy,  new_energy, temperature):
    if new_energy < energy:
        return 1.0
    return math.exp((energy -  new_energy) / temperature)
    
def main():
    
    # Read csv file 
    data = pd.read_csv("cities.csv")
    
    # Delete faulty row and cast row to int
    new_data = data[data.Население != '96[3]']
    new_data['Население'] = new_data['Население'].astype(int)
    new_data['Город'] = new_data['Город'].astype(str)
    
  
    Sorted = new_data.sort_values(['Население'], ascending=False)
    final_data = Sorted.head(30)
    final_data.ix[506, 'Город'] = 'Москва'
    final_data.ix[782, 'Город'] = 'Санкт-Петербург'
    
    
    final_data.Город.dtype
    
    for i in range(0, 30):
        Traverser.add_city(City(final_data['Город'].values[i],
                                final_data['Долгота'].values[i],
                                final_data['Широта'].values[i]))

    # initial temperature
    temp = 10000
    
    # cooling rate
    cooling_rate = 0.997
    
    current_solution = Travel()
    current_solution.generate_individual()
    
    # Initial figure
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111)
    longitude = [x.get_longitude() for x in current_solution.get_tour()]
    latitude = [x.get_latitude() for x in current_solution.get_tour()]
    names = [x.get_name() for x in current_solution.get_tour()]
    plt.plot(longitude, latitude, color='orange')
    for xy in zip(longitude, latitude):                                       # <--
        ax.annotate('%s' % names[longitude.index(xy[0])], xy=xy, textcoords='data') # <--

    plt.show()
    
    print("Initial solution distance: " + str(current_solution.get_distance()))
    
    # Set as current best
    best = Travel(current_solution.get_tour())

    while (temp > 1):
        new_solution = Travel(current_solution.get_tour())
        
        # get random position in tour
        tour_pos1 = int(new_solution.tour_size() * random.random())
        tour_pos2 = int(new_solution.tour_size() * random.random())
        # get cities at selected positions in the tour
        city_swap1 = new_solution.get_city(tour_pos1)
        city_swap2 = new_solution.get_city(tour_pos2)
        
        # swap them
        new_solution.set_city(tour_pos2, city_swap1)
        new_solution.set_city(tour_pos1, city_swap2)
        
        # get energy of solutions
        current_energy = current_solution.get_distance()
        neighbour_energy = new_solution.get_distance()
        
        # decide if we should accept the neighbour
        if (acceptanceProbability(current_energy, neighbour_energy, temp) > random.random()):
            current_solution = Travel(new_solution.get_tour())
            
        # keep track of the best solution found
        if (current_solution.get_distance() < best.get_distance()):
            best = Travel(current_solution.get_tour())
        
        # cool system
        temp *= cooling_rate
        
    print("Final solution distance: " + str(best.get_distance()))
    print("Tour: " + str(best))
    
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111)
    longitude = [x.get_longitude() for x in best.get_tour()]
    latitude = [x.get_latitude() for x in best.get_tour()]
    names = [x.get_name() for x in best.get_tour()]
    plt.plot(longitude, latitude, color='red')
    for xy in zip(longitude, latitude):                                       # <--
        ax.annotate('%s' % names[longitude.index(xy[0])], xy=xy, textcoords='data') # <--

    plt.show()
        
if __name__ == "__main__":
    main()