import numpy


def eigenvalue_inv(Matrix,x_init,ToL):
    err = ToL+1
    for i in range(1,len(Matrix)):
        U = np.matrix(np.zeros((1,len(Matrix))))
        U = x_init/euclidean_dist(Matrix,x_init)
        Matrix_inv = Matrix.I
        x = Matrix_inv*U
        lam=U.T*x
    while err>ToL:
        for i in range (1,len(Matrix)):
            U1 = np.matrix(np.zeros((1,len(Matrix))))
            U1 = x/euclidean_dist(Matrix,x)
            Matrix_inv = Matrix.I
            x1= Matrix_inv*U1
            lam = 1/(U1.T*x)
        err = abs(euclidean_dist(Matrix,x1)-euclidean_dist(Matrix,x))
        x = x1
    return x,lam


def euclidean_dist(Matrix,x_init):
    val = 0
    for i in range(0,len(Matrix)):
        val += x_init[i,0]**2
    return np.sqrt(float(val))

def eigenvalue(Matrix,x_init,ToL):
    err = ToL+1
    for i in range (1,len(Matrix)):
        U = np.matrix(np.zeros((1,len(Matrix))))
        U = x_init/euclidean_dist(Matrix,x_init)
        x= Matrix*U
        lam = U.T*x
    while err > ToL:
        for i in range (1,len(Matrix)):
            U1 = np.matrix(np.zeros((1,len(Matrix))))
            U1 = x/euclidean_dist(Matrix,x)
            x1= Matrix*U1
            lam = U1.T*x
        err = abs(euclidean_dist(Matrix,x1)-euclidean_dist(Matrix,x))
        x = x1
    return x,lam
