# -*- coding: utf-8 -*-
"""
@author: Paullaliberte
Monte Carlo Valuation of Euro call options - Numpy
Includes Graphical Representation
"""

import math
import numpy as np
from time import time
import matplotlib.pyplot as plt

np.random.seed(20000)
t_0 = time()

#Baseline parameters
S0 = 100.0
K = 105.0
T = 1.0
r = 0.05
sigma = 0.2
M = 50
dt = T/M
I = 250000

#Simulate
S = np.zeros((M + 1, I))
S[0] = S0

for t in range(1, M + 1):
    z = np.random.standard_normal(I)    #Normal Distribution, mean = 0, stdiv = 1
    S[t] = S[t - 1] * np.exp((r - 0.5 * sigma ** 2) * dt + sigma * math.sqrt(dt) * z)
    
    #exp is short for exponential function, not exponent.
    #np.exp can take an array i.e. x = [1, 2, 3]...
    #np.exp(x) = array([  2.71828183,   7.3890561 ,  20.08553692])
    
    
#Calculating M.C. estimator
C0 = math.exp(-r * T) * np.sum(np.maximum(S[-1] - K, 0)) / I

#Output Results
tnp1 = time() - t_0
print("Euro Option Valuation: %7.3f" % C0)
print("Duration in Seconds: %7.3f" % tnp1)

##################
######Graphs######
##################


#First 10 simulated paths
plt.plot(S[:, :10])
plt.grid(True)
plt.xlabel("time step")
plt.ylabel("index level")
plt.show()

#Freq. of simulated index level at period end
plt.hist(S[-1], bins=50)
plt.grid(True)
plt.xlabel("index level")
plt.ylabel("frequency")
plt.show()

#Maturity Inner Values
plt.hist(np.maximum(S[-1] - K, 0), bins=50)
plt.grid(True)
plt.xlabel("option inner value")
plt.ylabel("frequency")
plt.ylim(0, 50000)
plt.show()
