#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 23:41:57 2018

@author: jessie
"""

import numpy as np

def create_gershgorin_discs(mat):
    """Obtain centers and radii of a matrix's Gershgorin discs.
    
    Arguments:
    mat -- matrix
    
    Returns:
    diagonals -- the centers of the discs
    radii -- the corresponding radii
    """

    A = np.asarray(mat)
    diagonals = np.diag(A)
    radii = np.zeros(len(A))
    
    for row in range(len(A)):
        sum_of_non_diag = 0
        for col in range(len(A)):
            if row != col:
                sum_of_non_diag += abs(A[row, col])
        radii[row] = sum_of_non_diag
        
    return diagonals, radii
