#! /usr/bin/env python3

'''
Author:         Arturo Aguilar Lagunas
Date:           Tue Oct 19 11:14:09 AM CDT 2021
Description:    Basic operations for manipuling links
'''

import numpy as np

def get_rx(theta=0):
    return np.array([
        [1, 0, 0],
        [0, np.cos(theta), -np.sin(theta)],
        [0, np.sin(theta), np.cos(theta)]
    ], dtype=float)

def get_ry(theta=0):
    return np.array([
        [np.cos(theta), 0, np.sin(theta)],
        [0, 1, 0],
        [-np.sin(theta), 0, np.cos(theta)]
    ], dtype=float)

def get_rz(theta=0):
    return np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta), np.cos(theta), 0],
        [0, 0, 1]
    ], dtype=float)

def rotate(element, alpha=0.0, beta=0.0, gamma=0.0):
    element = np.matmul( get_rx(alpha), element )
    element = np.matmul( get_ry(beta), element )
    element = np.matmul( get_rz(gamma), element )
    return element

def rotate_t(element, alpha=0.0, beta=0.0, gamma=0.0):
    element = np.matmul( np.transpose(get_rx(alpha)), element )
    element = np.matmul( np.transpose(get_ry(beta)), element )
    element = np.matmul( np.transpose(get_rz(gamma)), element )
    return element

class Axis:
    def __init__(self, pos=[0, 0, 0]):
        self.axises = np.eye(3)                             # Cannonical representation of the unit vectors
        self.pos = np.array(pos, dtype=float).reshape(3, 1) # Position in space (Axis)

    # Rotate the axises
    def rotate(self, alpha=0.0, beta=0.0, gamma=0.0):
        self.axises = rotate(self.axises, alpha, beta, gamma)
        return self.axises

# TODO: INHERIT FROM AXIS CLASS
class Link:
    ''' NOTES:
        - INITIAL POSITION, MAGNITUDE/LEGHT/SIZE IN +Z DIRECTION
        - TODO: POSITION IN SPACE FROM LINK IS DIFERENT FROM THE ONE IN AXIS
    '''
    count = 0
    def __init__(self, pos=[0, 0, 0], dir=[0, 0, 0], lenght=1.0):
        Link.count += 1                                          # New link created
        self.axis = Axis(pos)                                    # Axis definition
        self.id = 'link-{}'.format(Link.count)                   # Link id
        self.pos = np.array(pos, dtype=float).reshape(3, 1)      # Position in space (Link)
        self.lenght = np.array([0, 0, lenght], dtype=float).reshape(3, 1)
        #self.lenght = rotate(                                    # Lenght vector definition
        #    np.array([0, 0, lenght], dtype=float).reshape(3, 1), # Lenght in Z axis
        #    dir[0], dir[1], dir[2])                              # Rotation in X, Y, Z

        print('created: {}'.format(self.id))

    def rotate(self, alpha=0.0, beta=0.0, gamma=0.0):
        self.axis.rotate(alpha, beta, gamma)
        print(self.lenght)
        self.lenght = rotate(self.lenght, alpha, beta, gamma)
        print(self.lenght)

    # TODO: Code system equivalencies
    def __calculate_cartesian(self):
        # x, y, z
        pass

    def __calculate_cylindrical(self):
        # rho, theta, z
        pass

    def __calculate_spherical(self):
        # r, theta, phi
        pass
