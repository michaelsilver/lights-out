"""
This code performs the reduced row echelon form computation
on an m x n matrix using Z2 as the field. There is also a routine
which computes the null space given the reduced matrix.

Copyright Kelly McQuighan
March 2015
"""
import numpy as np

# function to put any matrix in RREF    
def Z2_rref(A, m, n):
    # we will step through all the rows and columns until we run out of one or the other
    r = 0 # the row index
    c = 0 # the column index
    
    # we also want to keep track of the pivots
    no_pvt = []
    pvt = []
    switch = 0
    
    R = np.zeros((m,n))
    R[:,:] = A[:,:]
    
    # continue to reduce the matrix until we run out of rows or columns
    while (c < n and r < m):
        # if the leading entry equals zero, see if some other row has a one in that column
        # if so, switch the columns
        if R[r,c] == 0:
            switch = 0
            for j in range(r+1,m):
                if R[j,c] == 1:
                    R[[r,j],:] = R[[j,r],:]
                    switch = 1
                    break
            if (switch == 0):
                no_pvt = no_pvt + [c]
        # if the leading entry in row r is not zero,
        # remove the ones from any other row r_2 having a one in column c
        # by adding this row to r_2, using Z_2 addition
        # Note: this includes back solving!
        if R[r,c] != 0:
            pvt = pvt + [c]
            for j in range(m):
                if j != r:
                    R[j,:] = np.mod(R[j,:]+R[r,:]*R[j,c]/R[r,c],2)
            r += 1
        c += 1
    if c < n:
        no_pvt = no_pvt + range(c,n)
    return [R, pvt, no_pvt]

# ##### MAIN PROGRAM #######   
# def main(): 
#     print "This program puts an mxn matrix over the field Z_2 in reduced row echelon form.\n"

#     # some test matrices
#     #A = np.matrix([[1,1], [1, 0], [0,1]])
#     #A = np.matrix([[0,1], [1,1], [1, 0]])
#     #A = np.matrix([[1,1,1], [1,0,0]]) 
#     #A = np.matrix([[0,1,1], [1,1,0], [1,1,1]])   
#     A = np.matrix([[0,0,1,1], [1,1,1,0], [1,1,0,1]])
    
#     # getting the matrix dimensions
#     m = A.shape[0]
#     n = A.shape[1]
    
#     [R, pvt, no_pvt] = Z2_rref(A, m, n)
#     print 'A=\n', A, '\n\n rref(A)=\n', R, '\n\n pivots=', pvt
#     print '\n no_pivots=', no_pvt, '\n\n nullspace='

# main()
