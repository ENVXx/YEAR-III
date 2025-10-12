# Constructing the Routh chart
import numpy as np
import matplotlib as m
##
def main():
    print("Routh Stability Table Generator\nElias N.V 10/11/2025")
    a = input("a seperated by ','").split(",")
    N = len(a)
    if N%2 == 0:
        width = int((N/2)+1)
    else:
        width = int((N+1)/2)
    R = np.zeros((N+1,width))
    R[0,0] = 1
    R[1,0] = float(a[0])
    aind = 1
    
    for i in range(0,width-1):
        R[0,i+1] = float(a[aind])
        aind = aind+1
        if aind > len(a)-1:
            break
        else:
            R[1,i+1] = float(a[aind])
            aind = aind+1
    
    for i in range(2,N+1):
        for j in range(0,width-1):
            arr = np.array([[(R[(i-2),0]),(R[(i-2),(j+1)])],[(R[(i-1),0]),(R[(i-1),(j+1)])]])
            R[i,j] = -np.linalg.det(arr)/R[(i-1),0]
    R = np.round(R,decimals=4)
    print(R)
if __name__ == "__main__":
    main()