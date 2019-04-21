#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 09:38:59 2018

@author: bram
"""

# useful additional packages
import matplotlib.pyplot as plt

import numpy as np
import math

# importing Qiskit
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit import Aer, IBMQ, execute

# import basic plot tools
from qiskit.tools.visualization import matplotlib_circuit_drawer as circuit_drawer
from qiskit.tools.visualization import plot_histogram, qx_color_scheme

# Creating registers
tq = QuantumRegister(2)
tc0 = ClassicalRegister(1)
tc1 = ClassicalRegister(1)
teleport = QuantumCircuit(tq, tc0,tc1)


class Coinflip:
    def __init__(self, queue):
        self.queue = queue
    
    def _atomic_flip(self, cand1, cand2, coeff):
               
        #reset circuit
        teleport.reset(tq)
        
        angle = np.pi/(2 * math.acos(coeff))
        #print(angle)
        #Prepare qubit to send
        teleport.ry(np.pi/angle,tq[0])
        teleport.cx(tq[0], tq[1])
        teleport.x(tq[1])
        teleport.measure(tq[0], tc0[0])
        teleport.measure(tq[1], tc1[0])


        #circuit_drawer(teleport,style=qx_color_scheme())
            
            
        local_backend = Aer.get_backend('qasm_simulator') # note that this circuit can not be run on an IBM Q device
        teleport_job = execute(teleport, local_backend, shots = 1)
        teleport_result = teleport_job.result()
            
        data = teleport_result.get_counts(teleport)
        
        
        for key, value in data.items():
            i = 0
    
        if key == '0 1':
            bob_value = 0
            #print(key,bob_value,cand1)
            return cand1
        else:
            bob_value = 1
            #print(key,bob_value,cand2)
            return cand2
        
    def leader(self):
        assert len (self.queue) >= 2
        winner = self.queue[0]
        
        for i in range(2,len(self.queue)+1):
            coeff = math.sqrt(1/i)
            
            winner = self._atomic_flip(winner, self.queue[i-1], coeff)
        
        return winner

