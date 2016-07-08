#!/usr/bin/env python

import os, sys
import random
import numpy

def read_xyz(input_filename):

    inputFile = open(input_filename, 'r')

    natoms = int(inputFile.readline())
    inputFile.readline() # skip comment line

    atom_names = []
    atom_coords = numpy.zeros((natoms,3),dtype=float)

    for i in range(natoms):
        line = inputFile.readline()
        atom_names.append(line.split()[0])
        atom_coords[i][0] = float(line.split()[1])
        atom_coords[i][1] = float(line.split()[2])
        atom_coords[i][2] = float(line.split()[3])

    return atom_names, atom_coords

def main():
    """
    This code adds thermal noise to a set of atoms
    """
    # A clean way to ask for user input
    try:
        # Attempt to retrieve required input from user
        prog = sys.argv[0]
        input_file = sys.argv[1]
        lamda = float(sys.argv[2])
    except IndexError:
        # Tell the user what they need to give
        print '\nusage: '+prog+' input_file lamda (amount of thermal noise)\n'
        # Exit the program cleanly
        sys.exit(0)

    num_x_trans = 1             
    num_y_trans = 1             
    num_z_trans = 1             
                                
    number_of_snapshots = 1000  
                                
    lattice_constant = 1.0

    a1 = numpy.array([1.0,0.0,0.0])
    a2 = numpy.array([0.0,1.0,0.0])
    a3 = numpy.array([0.0,0.0,1.0])

    atom_names, basis_atoms = read_xyz(input_file) 

    number_of_particles = num_x_trans*num_y_trans*num_z_trans*len(basis_atoms)
    rs = (lattice_constant)*(3/(4*number_of_particles*numpy.pi))**(1.0/3.0)
    print rs

    sigma_x = lamda  
    sigma_y = lamda 
    sigma_z = lamda 

    bravis_lattice = []
    name_list = []

    for i in range(num_x_trans):
         for j in range(num_y_trans):
              for k in range(num_z_trans):
                   for l in range(len(basis_atoms)):
                        name_list.append(atom_names[l])
                        bravis_lattice.append(i*a1 + j*a2 + k*a3 + basis_atoms[l])

    filename = 'TRAJEC.' + '%.4f' % lamda + '.xyz'


    outputFile = open(filename,'w')


    for time_step in range(number_of_snapshots):

        outputFile.write(repr(len(bravis_lattice)) + '\n')
        outputFile.write(repr(time_step + 1) + '\n')

        id = 0

        for triple in bravis_lattice:
         
            xcart = lattice_constant/float(num_x_trans)*triple[0] + random.gauss(0.0, sigma_x)
            ycart = lattice_constant/float(num_y_trans)*triple[1] + random.gauss(0.0, sigma_y)
            zcart = lattice_constant/float(num_z_trans)*triple[2] + random.gauss(0.0, sigma_z)

            name = name_list[id]
            
            outputFile.write(name + ' ' + repr(xcart) + '   ' + repr(ycart) + '   ' + repr(zcart) + '\n')
            id += 1   
    outputFile.close()



# This executes main() only if executed from shell
if __name__ == '__main__':
    main()
