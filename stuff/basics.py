#! /usr/bin/env python3

'''
Author: 		Arturo Aguilar Lagunas
Date:			Tue Oct 19 11:14:09 AM CDT 2021
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

class Axis():
    def __init__(self, p1, p2, p3):
        self.axises = np.eye(3)
        self.p = np.array([p1, p2, p3], dtype=float).reshape(3, 1)

    def rotate(self, alpha=0.0, beta=0.0, gamma=0.0):
        self.axises = np.matmul( get_rx(alpha), self.axises)
        self.axises = np.matmul( get_ry(beta), self.axises)
        self.axises = np.matmul( get_rz(gamma), self.axises)
        return self.axises

class Link():
    CARTESIAN = 0
    CYLINDICAL = 1
    SPHERICAL = 2

    def __init__(self, v1, v2, v3, m=CARTESIAN):
        self.v = np.array([v1, v2, v3], dtype=float)

        if m == Link.CARTESIAN:
            self.v_cartesian = self.v
            # self.v_cylindrical = np.array([rho, theta, z])
            # self.v_spherical = np.array([r, theta, phi])
        elif m == Link.CYLINDRICAL:
            # self.v_cartesian = np.array([x, y, z])
            self.v_cylindrical = self.v
            # self.v_spherical = np.array([r, theta, phi])
        elif m == Link.SHPERICAL:
            # self.v_cartesian = np.array([x, y, z])
            # self.v_cylindrical = np.array([rho, theta, z])
            self.v_spherical = self.v
        else:
            raise Exception("Invalid system")

        print(self.v.shape)

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

