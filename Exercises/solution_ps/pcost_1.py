import os
import sys
import re
import csv

import decimal

def portfolio_cost(file_path) -> float:
    
    total_cost = 0
    
    with open(file_path,'r') as f:

        for i in f:

            # print(i)
            try:
                breaking_characters = str(i).split(" ")
                quantity = int(breaking_characters[1])
                price = float(breaking_characters[2].partition('\n')[0])
                
                total_cost = total_cost + quantity*price
            except ValueError as e:
                print(f"Couldn't parse:{i} \n Reason: {e}")  
    
        return total_cost

# if __name__ == "__main__":
#     print(portfolio_cost('Data/portfolio3.dat'))