#! /usr/bin/env python

import sys

print 'usage: ' + sys.argv[0] + ' ...talk to Isaac about this one...'

############################
#############################
                            ##
num_x_trans = 3             ##
num_y_trans = 3             ##
num_z_trans = 3             ##
                            ##
#############################
############################

lattice_constant = 1.0

import random
import sys
import numpy

a1 = numpy.array([1.0,0.0,0.0])
a2 = numpy.array([0.0,1.0,0.0])
a3 = numpy.array([0.0,0.0,1.0])

sc =      numpy.array([[0.0,0.0,0.0]])

bcc =     numpy.array([[0.0,0.0,0.0],
                       [0.5,0.5,0.5]])

fcc =     numpy.array([[0.0,0.0,0.0], 
                       [0.5,0.5,0.0],
                       [0.5,0.0,0.5],
                       [0.0,0.5,0.5]])

cI16_JY = numpy.array([[4.0E-02,  4.0E-02,  4.0E-02], 
                       [4.6E-01,  9.6E-01,  5.4E-01], 
                       [9.6E-01,  5.4E-01,  4.6E-01],  
                       [2.9E-01,  2.9E-01,  2.9E-01],  
                       [5.4E-01,  4.6E-01,  9.6E-01], 
                       [2.1E-01,  7.1E-01,  7.9E-01],  
                       [7.1E-01,  7.9E-01,  2.1E-01],  
                       [7.9E-01,  2.1E-01,  7.1E-01],  
                       [5.4E-01,  5.4E-01,  5.4E-01],  
                       [9.6E-01,  4.6E-01,  4.0E-02],  
                       [4.6E-01,  4.0E-02,  9.6E-01],  
                       [4.0E-02,  9.6E-01,  4.6E-01],  
                       [7.9E-01,  7.9E-01,  7.9E-01],  
                       [7.1E-01,  2.1E-01,  2.9E-01],  
                       [2.1E-01,  2.9E-01,  7.1E-01],  
                       [2.9E-01,  7.1E-01,  2.1E-01]])

basis_atoms = fcc 

bravis_lattice = []

for i in range(num_x_trans):
     for j in range(num_y_trans):
          for k in range(num_z_trans):
               for l in range(len(basis_atoms)):
                    bravis_lattice.append(i*a1 + j*a2 + k*a3 + basis_atoms[l])

filename = 'xred.dat'

outputFile = open(filename,'w')


for triple in bravis_lattice:
         
     xcart = lattice_constant/float(num_x_trans)*(triple[0])
     ycart = lattice_constant/float(num_y_trans)*(triple[1])
     zcart = lattice_constant/float(num_z_trans)*(triple[2])

     outputFile.write(' ' + repr(xcart) + '   ' + repr(ycart) + '   ' + repr(zcart) + '\n')
               
outputFile.close()
