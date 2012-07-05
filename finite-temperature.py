#!/usr/local/bin/python

import sys

print 'usage: ' + sys.argv[0] + ' lamda'

import random
import numpy

###########################
#############################
                            ##
num_x_trans = 4             ##
num_y_trans = 4             ##
num_z_trans = 4             ##
                            ##
number_of_snapshots = 1000  ##
                            ##

#lattice_constant = 8.1239303805060814         # bcc, 4x4x4
#lattice_constant = 7.6766331707100584         # fcc, 3x3x3
#lattice_constant = 9.6719517240988271         #  sc, 2x2x2

lattice_constant = 1.0
                            ##
#############################
############################

lamda = float(sys.argv[1])

# note that in order to compare structures, density needs to be the same. sc,bcc, fcc check out okay, so the program is probably good!
# for cI16, with 16 atom basis, you need to put a *4 in denomenator...?

lattice_constant *= 0.529177


a1 = numpy.array([1.0,0.0,0.0])
a2 = numpy.array([0.0,1.0,0.0])
a3 = numpy.array([0.0,0.0,1.0])

sc  =     numpy.array([[0.0, 0.0, 0.0]])

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

bc8 =     numpy.array([[0.0E+00,  0.0E+00,  0.0E+00],
                       [5.0E-01,  0.0E+00,  5.0E-01],
                       [0.0E+00,  5.0E-01,  5.0E-01],
                       [5.0E-01,  5.0E-01,  0.0E+00],
                       [5.0E-01,  5.0E-01,  5.0E-01],
                       [0.0E+00,  5.0E-01,  0.0E+00],
                       [5.0E-01,  0.0E+00,  0.0E+00],
                       [0.0E+00,  0.0E+00,  5.0E-01]])

diamond = numpy.array([[0.00, 0.00, 0.00],
                       [0.50, 0.50, 0.00],
                       [0.50, 0.00, 0.50],
                       [0.00, 0.50, 0.50],
                       [0.25, 0.25, 0.25],
                       [0.75, 0.75, 0.25],
                       [0.75, 0.25, 0.75],
                       [0.25, 0.75, 0.75]])

basis_atoms = cI16_JY 

number_of_particles = num_x_trans*num_y_trans*num_z_trans*len(basis_atoms)
rs = (lattice_constant)*(3/(4*number_of_particles*numpy.pi))**(1.0/3.0)
print rs

sigma_x = lamda  
sigma_y = lamda 
sigma_z = lamda 

bravis_lattice = []

for i in range(num_x_trans):
     for j in range(num_y_trans):
          for k in range(num_z_trans):
               for l in range(len(basis_atoms)):
                    bravis_lattice.append(i*a1 + j*a2 + k*a3 + basis_atoms[l])

filename = 'TRAJEC.' + '%.4f' % lamda + '.xyz'
#filename = 'TRAJEC.xyz'

outputFile = open(filename,'w')


for time_step in range(number_of_snapshots):

     outputFile.write(repr(len(bravis_lattice)) + '\n')
     outputFile.write(repr(time_step + 1) + '\n')
     
     for triple in bravis_lattice:
         
          xcart = lattice_constant/float(num_x_trans)*triple[0] + random.gauss(0.0, sigma_x)
          ycart = lattice_constant/float(num_y_trans)*triple[1] + random.gauss(0.0, sigma_y)
          zcart = lattice_constant/float(num_z_trans)*triple[2] + random.gauss(0.0, sigma_z)

          outputFile.write('H ' + repr(xcart) + '   ' + repr(ycart) + '   ' + repr(zcart) + '\n')
               
outputFile.close()
