""""
"""
    #Écrivez un programme qui imprime les n premiers termes de la suite de Fibonacci.
"""
import numpy as np
import  matplotlib.pyplot as plt
if __name__ =="__main__":
    tabFibonacci=[]
    fn =0
    Fn1=0
    Fn2 =1
    nbre = int(input("Entrez une borne superieur : "))
    for i in range(0,nbre):
        fn = Fn1 +Fn2
        Fn1 = Fn2
        Fn2 = fn
        tabFibonacci.append(fn)

    #resultat
    print(tabFibonacci)

#tracer de la courbe
    a = np.array(tabFibonacci)
    b = np.array([1,2,3,4,5,6,7,8,8])

    plt.plot(a,b)
    plt.ylabel(b)
    plt.xlabel(a)
    plt.show() 
"""

"""
Plot 3D.

source : PythonProgramming.net
"""
import matplotlib.pyplot as plt
from matplotlib import style
from mpl_toolkits.mplot3d import axes3d

style.use('ggplot')

fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')

x, y, z = axes3d.get_test_data()

ax1.plot_wireframe(x, y, z, rstride=3, cstride=3)

ax1.set_xlabel('x axis')
ax1.set_ylabel('y axis')
ax1.set_zlabel('z axis')

plt.show()
