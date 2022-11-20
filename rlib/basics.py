#! /usr/bin/env python3

'''
Author:         Arturo Aguilar Lagunas
Date:           Tue Oct 19 11:14:09 AM CDT 2021
Description:    Basic operations for manipuling links
'''

import numpy as np

# TODO: CODE FUNCTION TO ROTATE AGAINST AN AXIS
# TODO: CREATE MECH CLASS

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

# TODO: MAYBE INHERIT FROM AXIS CLASS
class Link:
    count = 0
    def __init__(self, dh):
        self.id = Link.count                                    # Link id
        # self.axis = Axis()
        print('link-id: {}'.format(self.id))

class Mecha:
    def __init__(self, dh_args, origin=None):
        self.origin = Axis()
        self.links = []
        for dh in dh_args:
            pass
            # Get 0_TH_N, N-1_TH_N
            # Get Axises
            # Get Pos
