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

class Axis:
    def __init__(self, p1, p2, p3):
        self.axises = np.eye(3)
        self.pos = np.array([p1, p2, p3], dtype=float).reshape(3, 1)

    def rotate(self, alpha=0.0, beta=0.0, gamma=0.0):
        self.axises = np.matmul( get_rx(alpha), self.axises)
        self.axises = np.matmul( get_ry(beta), self.axises)
        self.axises = np.matmul( get_rz(gamma), self.axises)
        return self.axises

# TODO: INHERIT FROM AXIS CLASS
class Link():
    id = 0
    ''' NOTES:
        - INITIAL POSITION, MAGNITUDE/LEGHT/SIZE IN +Z DIRECTION
        - TODO: DIRECTION FROM LINK IS DIFERENT FROM THE ONE IN AXIS
        - TODO: POSITION IN SPACE FROM LINK IS DIFERENT FROM THE ONE IN AXIS
    '''
    def __init__(self, pos=[0, 0, 0], dir=[0, 0, 0], mag=1.0):
        Link.id += 1
        self.name = 'link-{}'.format(Link.id)
        self.axis = Axis(pos[0], pos[1], pos[2])
        # TODO: Rotate self.axis by dir
        self.mag = np.array([0, 0, mag], dtype=float).reshape(3, 1)
        print('created: {}'.format(self.name))

    def rotate(self, angle):
        pass

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
