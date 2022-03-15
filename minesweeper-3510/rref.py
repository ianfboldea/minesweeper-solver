import numpy as np

def rref(A):
    row, col = A.shape
    # Base case
    if row == 0 or col == 0:
        return A
    for i in range(len(A)):
        if A[i,0] != 0:
            break
        else:
            B = rref(A[:,1:])
            return np.hstack([A[:,:1], B])
        if i > 0:
            temp = A[i].copy()
            A[i] = A[0]
            A[0] = temp
    A[0] = A[0] / A[0,0]
    A[1:] -= A[0] * A[1:,0:1]
    B = rref(A[1:,1:])
    return np.vstack([A[:1], np.hstack([A[1:,:1], B]) ])

# A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype="float")
# print(rref(A))