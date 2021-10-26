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

def rotate_left(mov_ax, alpha=0.0, beta=0.0, gamma=0.0, ref_ax=np.eye(3)):
    mov_ax = np.matmul( np.matmul(get_rx(alpha), ref_ax), mov_ax )
    mov_ax = np.matmul( np.matmul(get_ry(beta), ref_ax), mov_ax )
    mov_ax = np.matmul( np.matmul(get_rz(gamma), ref_ax), mov_ax )
    return mov_ax

def rotate_right(mov_ax, alpha=0.0, beta=0.0, gamma=0.0, ref_ax=np.eye(3)):
    mov_ax = np.matmul( np.matmul( ref_ax, get_rx(alpha) ), mov_ax )
    mov_ax = np.matmul( np.matmul( ref_ax, get_ry(beta) ), mov_ax )
    mov_ax = np.matmul( np.matmul( ref_ax, get_rz(gamma) ), mov_ax )
    return mov_ax

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
    ''' NOTES:
        - INITIAL POSITION, MAGNITUDE/LEGHT/SIZE IN +Z DIRECTION
        - TODO: POSITION IN SPACE FROM LINK IS DIFERENT FROM THE ONE IN AXIS
    '''
    count = 0
    def __init__(self, pos=[0, 0, 0], dir=[0, 0, 0], mag=1.0):
        self.axis = Axis(pos)                                   # Axis definition
        self.__fixed_axises = self.axis.axises                  # Fixed axises
        self.id = Link.count                                    # Link id
        self.pos = np.array(pos, dtype=float).reshape(3, 1)     # Position in space (Link)
        self.mag = mag                                          # Link's lenght
        self.__o_vec = np.array(                                # Lenght in Z axis
            [0, 0, self.mag],
            dtype=float).reshape(3, 1)

        # Align lenght vector in Z with rotated reference axis
        self.__o_vec = np.matmul(                               # Lenght in X, Y, Z
            rotate_t(self.axis.axises, dir[0], dir[1], dir[2]), # Generate reference axises
            np.array([0, 0, mag], dtype=float).reshape(3, 1) )  # Lenght in Z axis
        self.vec = self.__o_vec

        Link.count += 1                                         # New link created
        print('link-id: {}'.format(self.id))

    def rotate(self, alpha=0.0, beta=0.0, gamma=0.0):
        self.axis.rotate(alpha, beta, gamma)
        self.vec = np.matmul( np.transpose( self.axis.axises ), self.__o_vec )

    # TODO: UPDATE AXIS & VECTOR POSITION X, Y, Z
    '''def update(self, new_rotation, new_pos):
        print('updating {}'.format(self.id))

        # NOTES:
        #     - AQUI ME QUEDÉ
        #     - ROTAR EJES INDEPENDIENTEMENTE CON (ALPHA, BETA, GAMMA) ALOMEJOR
        #       ES NECESARIO UTILIZAR MATRIZ TRASPUESTA
        #     - ROTAR VECTOR CON LA NUEVA MATRIZ DE ROTACION

        self.axis.axises = np.matmul( new_rotation, self.__fixed_axises )
        print(self.axis.axises)
        self.vec = np.matmul( np.transpose( new_rotation ), self.__o_vec )
        self.pos = new_pos
        self.axis.pos = new_pos'''

    def update(self, alpha, beta, gamma, new_pos, new_ax):
        print('updating {}'.format(self.id))
        # self.axis.axises = np.matmul( new_rotation, self.__fixed_axises )
        print(self.axis.axises)
        self.axis.axises = rotate_left( self.axis.axises, alpha, beta, gamma, self.__fixed_axises )
        print(self.axis.axises)
        self.vec = np.matmul( np.transpose( self.axis.axises ), self.__o_vec )
        self.pos = new_pos
        self.axis.pos = new_pos

class Mecha:
    # TODO: CARTESIAN -> CYLINDRICAL TO ROTATE AXIS & LINK_VECTOR
    def __init__(self, articulation_points):
        self.links = []
        for i, pos in enumerate(articulation_points):
            # TODO: OBTAIN ANGLE AND MAG
            self.links.append( Link(pos=pos, dir=[0.0, 0.0, 0.0], mag=1.0) )
            if i > 0:
                self.links[i].pos = self.links[i].pos + self.links[i-1].pos
                self.links[i].axis.pos = self.links[i].axis.pos + self.links[i-1].axis.pos
                self.links[i].reference_link = self.links[i-1].id

    def rotate(self, element, alpha=0.0, beta=0.0, gamma=0.0):
        self.links[element].rotate(alpha, beta, gamma)
        if not ( element + 1 == len(self.links) ):
            for i, link in enumerate( self.links[element+1:] ):
                prev_link = self.links[i + element]
                # old
                # self.links[i + element + 1].update( prev_link.axis.axises, prev_link.pos + prev_link.vec )

                # new
                self.links[i + element + 1].update(
                    alpha, beta, gamma,
                    prev_link.pos + prev_link.vec,
                    prev_link.axis.axises )

                # print( self.links[i + element + 1].axis.axises )
