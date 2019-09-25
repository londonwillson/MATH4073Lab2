
import numpy as np

def classicalGS(A,k,n):
    Q = A
    QT = np.transpose(Q)
    R = np.zeros([k, k])
    for j in range(1,n):
        for i in range(1, j-1):
            R[i,j] = np.dot(QT[i],A[j])
            print(R[i,j])
            Q[j] = Q[j] - R[i,j]*Q[i]
        print(Q[j])
        R[j,j] = np.sqrt(np.dot(QT[j],Q[j]))
        Q[j] = np.multiply((1/R[j,j]), Q[j])
    return Q, R
def modifiedGS(A,k):
    Q = A
    QT = np.transpose(Q)
    R = np.zeroes[k, k]
    for j in range(1,n):
        for i in range(1, j-1):
            r[i,j] = QT[i] * Q[j]
            Q[j] = Q[j] - r[i,j]*Q[i]
        r[j,j] = sqrt(QT[j]*Q[j])
        Q[j] = 1/r[j,j] * Q[j]
    return Q, R
def BackwardsSubstitution(C, n):
    x = [0.0]
    count = n - 1
    for i in reversed(range(0, (n-1))):
        sum = 0
        y=0
        for j in reversed(range(count,n)):
            #print("j= " +str(j))
            #print("y " + str(y))
            sum = sum + C[i,j]*x[y]
            y += 1
        count -= 1
        calc = ((C[i,(n-1)]-sum)/C[i,i])
        x.append(calc)
    return x
def main():
    A = np.matrix([[1, 0, 1], [1,1,0], [0,1,1]])
    k = np.shape(A)[1]
    n = np.shape(A)[0]
    print(k)
    Q, R = classicalGS(A,k,n)
    print("Q: " + str(Q))
    print("R: " + str(R))
main()
