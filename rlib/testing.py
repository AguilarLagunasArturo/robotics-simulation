#! /usr/bin/env python3

'''
    Author:       Arturo Aguilar Lagunas
    Date:         Sat Nov 20 11:24:47 PM CST 2021
    Description:  Testing DH stuff
'''

import numpy as np
# import scipy

def get_ghm(a=0, alpha=0, d=0, theta=0, dh_args=None):

    if dh_args is not None:
        a, alpha, d, theta = dh_args

    return np.array([
        [np.cos(theta), -np.sin(theta), 0, a],
        [np.sin(theta)*np.cos(alpha), np.cos(theta)*np.cos(alpha), -np.sin(alpha), -np.sin(alpha)*d],
        [np.sin(theta)*np.sin(alpha), np.cos(theta)*np.sin(alpha), np.cos(alpha), np.cos(alpha)*d],
        [0, 0, 0, 1]
    ], dtype=float)

if __name__ == '__main__':
    dh = [
        [0, 0, 0, 0], # 1
        [9, 0, 0, 0], # 2
        [9, 0, 0, 0], # 3
        [0, 0, 8, 0]  # e
    ]

    hm = [ get_ghm(dh_args=dh_i) for dh_i in dh ]
    # [print(ti) for ti in hm ]
    print()
    # t = np.matmul( hm[3], np.matmul( hm[2], np.matmul( hm[1], hm[0] ) ) )
    t = np.matmul( hm[0], np.matmul(hm[1], hm[2]) )
    print(t)
