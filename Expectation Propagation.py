# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 13:54:34 2020

@author: Grant
"""

import math
import random

def p(x, mu, sigma):
    return (1 / (2 * math.pi * sigma**2)**(1/2)) * math.exp(-(x - mu)**2 / (2 * sigma**2))

phi = [[2, 1, 0.1, 0.1],
       [1, 2, 0.1, 0.1],
       [3, 2, 0.1, 0.1],
       [2, 3, 0.1, 0.1],
       [4, 3, 0.1, 0.1],
       [3, 4, 0.1, 0.1],
       [1, 4, 0.1, 0.1],
       [4, 1, 0.1, 0.1]]

x = [[0.1, 0.8],
     [0.1, 0.8],
     [0.2, 0.5],
     [0.2, 0.5]]

current_x = [0.1, 0.1, 0.5, 0.5]

selection = [[1, 2],
             [2, 3],
             [3, 4],
             [1, 4]]

minimum_set = [100, 100, 100, 100]

converge = False
convergence_criteria = 0.1

u = 0
while converge == False:
    select = random.choice(selection)
    
    s_1 = select[0]
    s_2 = select[1]
    
    #minimum = minimum_set[selection.index(select)]
    
    for a in range(1, 10):
        a = a / 10
        for b in range(1, 10):
            b = b / 10
            for c in range(1, 10):
                c = c / 10
                for d in range(1, 10):
                    d = d / 10
                    
                    #Z = 0
                    x_1 = x[s_1 - 1]
                    x_2 = x[s_2 - 1]
                    
                    #print(x_1)
                    #print(x_2)
                    
                    terms_1 = []
                    for i in phi:
                        if i[1] == s_1:
                            terms_1.append(i)
                    terms_2 = []
                    for i in phi:
                        if i[1] == s_2:
                            terms_2.append(i)
                    
                    #print(terms_1)
                    #print(terms_2)
                    
                    Z_1 = 1
                    for t in terms_1:
                        temp = 0
                        for y in x_1:
                            #print("HERE")
                            if t[0] in select:
                                temp = temp + p(y, a, b)
                            else:
                                temp = temp + p(y, t[2], t[3])
                            #print(temp)
                        if temp != 0:
                            Z_1 = Z_1 * temp
                    #print(Z_1)
                    
                    Z_2 = 1
                    for t in terms_2:
                        temp = 0
                        for y in x_2:
                            if t[0] in select:
                                temp = temp + p(y, c, d)
                            else:
                                temp = temp + p(y, t[2], t[3])
                        if temp != 0:
                            Z_2 = Z_2 * temp
                    #print(Z_2)
                    
                    Z = Z_1 * Z_2
                    
                    
                    
                    central_term = p(current_x[s_1 - 1], a, b) * p(current_x[s_2 - 1], c, d)
                    
                    
                    
                    p_total_1 = 1
                    for t in terms_1:
                        temp = 0
                        for y in x_1:
                            if t[0] in select:
                                temp = temp + p(y, a, b)
                            else:
                                temp = temp + p(y, t[2], t[3])
                        if temp != 0:
                            p_total_1 = p_total_1 * temp
                    p_numerator_1 = 1
                    for t in terms_1:
                        if t[0] in select:
                            p_numerator_1 = p_numerator_1 * p(current_x[s_1 - 1], a, b)
                        else:
                            p_numerator_1 = p_numerator_1 * p(current_x[s_1 - 1], t[2], t[3])
                    #print(p_total_1)
                    #print(p_numerator_1)
                    p_1 = p_numerator_1 / p_total_1
                    
                    
                    p_total_2 = 1
                    for t in terms_2:
                        temp = 0
                        for y in x_2:
                            if t[0] in select:
                                temp = temp + p(y, c, d)
                            else:
                                temp = temp + p(y, t[2], t[3])
                        if temp != 0:
                            p_total_2 = p_total_2 * temp
                    p_numerator_2 = 1
                    for t in terms_2:
                        if t[0] in select:
                            p_numerator_2 = p_numerator_2 * p(current_x[s_2 - 1], c, d)
                        else:
                            p_numerator_2 = p_numerator_2 * p(current_x[s_2 - 1], t[2], t[3])
                    #print(p_total_2)
                    #print(p_numerator_2)
                    p_2 = p_numerator_2 / p_total_2
                    
                    p_dash = p_1 * p_2
                    
                    if math.log(Z) - central_term * p_dash < minimum_set[selection.index(select)]:
                        for i in phi:
                            if i[0] == s_1 and i[1] == s_2:
                                i[2] = a
                                i[3] = b
                        
                        for j in phi:
                            if j[0] == s_2 and j[1] == s_1:
                                j[2] = c
                                j[3] = d
                        
                        minimum_set[selection.index(select)] = math.log(Z) - central_term * p_dash
                    
                    #print()
    
    u = u + 1
    
    if u > 20:
        converge = True

print(phi)
    