'''
Fixed Point Iteration Method:
The fixed point iteration method works by rewriting the polynomial whose root we want, f(x)=0, as
x=g(x). Then we pick a guess point, x0 and plug it into g(x). We then get x1 and plug that into g(x) again 
to hopefully arrive at some value that approximately makes x=g(x)...
'''
import numpy as np
import matplotlib.pyplot as plt 

f= lambda x: x**3 +2*x**2 -5*x +7
# g(x) is found by rearranging f(x)=0 into x=g(x) form
g = lambda x: np.cbrt(-2*x**2 + 5*x - 7) # cbrt is just the cube root function

# x has to equal g(x) for f(x) to be 0. Geometrically, this means the x-value
# of the point where the graph of g(x) intersects the straight line y=x is the root!

def FixedPointIter(g, x0, n):
    x=x0 # initial guess
    for i in range(n):    
        x_in= x
        x_out= g(x)
        print(f"Error after {i} iteration: {abs(x_out-x_in)}")
        x=g(x)
    root= x_out
    print(f"Approximate root:{root}")
    return root
x1, x2= 15, 0
r1, r2= FixedPointIter(g, x1, 10), FixedPointIter(g, x2, 10) 

'''
Visualization using matplotlib
'''
x= np.linspace(-30,30,100)
fig, ax= plt.subplots()
ax.plot(x,g(x), color='blue', label= 'g(x)')
ax.plot(x,f(x), color='green', label= 'f(x)')
ax.plot(x,x, color='orange', label= 'y=x')
ax.set_aspect('equal')
ax.set_ylim(bottom=-20, top=40)
ax.axhline(y=0,color= 'k')
ax.axvline(x=0, color='k')
ax.grid(True)
ax.set_xlabel('x')
ax.legend(loc='upper left')
plt.title("Fixed Point Iteration Method")
plt.vlines(x1, 0, g(x1), colors="black", linestyles= "dashed")
plt.vlines(x2, 0, g(x2), colors="red", linestyles="dashed")
plt.vlines(r1,0,g(r1), colors="black", linestyles= "dashed")
plt.vlines(r2,0,g(r2), colors="red", linestyles="dashed")
def steps(g,x0,n):
    for i in range(n):    
        plt.hlines(g(x0),x0, g(x0), colors="black", linestyles= "dashed")
        plt.vlines(g(x0),g(x0),g(g(x0)),colors="black", linestyles="dashed")
        x0= g(x0)
steps(g,x1,10)
steps(g,x2,10)
# Move the bottom axis to y=0
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))
# Ensure the ticks are on the bottom
ax.xaxis.set_ticks_position('bottom')
specific_x_ticks = [x1, x2, r1, r2]
specific_x_labels = ['x1','x2','r1','r2']
plt.xticks(specific_x_ticks, specific_x_labels)
plt.show()

'''
Even though we started from two different guesses, x1 and x2, we ended up with the same root.
You can see from the plot that the dashed line 'bounces' between the graph of g(x) and the straight
line y=x. The point where the dashed line and the graph of g(x) intersect is the root.
''' 


