# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 10:47:38 2020

@author: Grant
"""

import math

def p(x, mu, sigma):
    return (1 / (2 * math.pi * sigma**2)**(1/2)) * math.exp(-(x - mu)**2 / (2 * sigma**2))

class_q = [[1, 100]]

p_mu = 0.2
p_sigma = 0.3

q1_chosen = 0.3
q2_set = 0.3

difference = 1
convergence_criteria = 0.01

x = [0.1, 0.8, 0.5, 0.9]

m_max = 0
s_set = 0.3

convergence = False

maximum = 0
maximum1 = 0

while convergence == False:
    q1_chosen_previous = q1_chosen
    #q2_chosen_previous = q2_chosen
    
    m_max_previous = m_max
    #s_max_previous = s_max
    
    maximum = 0
    for m in range(1, 200):
        #for s in range(1, 100):
        m = m / 100
        #s = s / 100
            
        temp = 0
        for y in x:
            temp = temp + p(y, q1_chosen, q2_set) * p(y, p_mu, p_sigma) * p(y, m, s_set)
        #print(temp)
            
        if temp > maximum:
            m_max = m
            #s_max = s
            maximum = temp
    
    maximum1 = 0
    for a in range(class_q[0][0], class_q[0][1]):
        #for b in range(class_q[1][0], class_q[1][1]):
        a_new = a / 100
        #b_new = b / 100
            
        temp1 = 0
        for y in x:
            temp1 = temp1 + p(y, a_new, q2_set) * p(y, p_mu, p_sigma) * p(y, m_max, s_set)
            
        if temp1 > maximum1:
            q1_chosen = a_new
            #q2_chosen = b_new
            maximum1 = temp1
    
    convergence = True
    
    if abs(q1_chosen - q1_chosen_previous) > convergence_criteria:
        convergece = False
    
    #if abs(q2_chosen - q2_chosen_previous) > convergence_criteria:
    #    convergece = False
        
    if abs(m_max - m_max_previous) > convergence_criteria:
        convergece = False
    
    #if abs(s_max - s_max_previous) > convergence_criteria:
    #    convergece = False

print([m_max, s_set, q1_chosen, q2_set])