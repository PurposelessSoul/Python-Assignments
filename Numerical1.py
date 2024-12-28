'''
The algorithm below approximates the root of a function, f, between two given bounds a and b, using the bisection
method under some threshold error, e, provided as a parameter to the function. 
'''

def bisect(f, a, b, e=0.0001): # e is set to 0.0001% by default
	if f(a)*f(b)>0:
		print('The bounds you provided have the same sign. Its not guaranteed that there is a real root between these numbers!')
	c, E =[], [] # Initializing the list of all half-way points and the error at each iteration
	Error= lambda i: abs((c[i]-c[i-1])/c[i]*100) # Error fun_ 
	i=0
	while True: # because we need to run the loop until the error<threshold
		c.append((a+b)/2)
		if i >= 1:
			E.append(Error(i))
			if Error(i) <e:
				print(f"Approximate root: {c[i]}")
				return c[i], E
				break
		if f(a)*f(c[i])<0:
			b= c[i] 		#updating the lower bound if root is between a and c
		elif f(a)*f(c[i])>0:
			a=c[i]			#updating the upper bound if root is between c and b
		i+=1
	

'''
THE PROBLEM:
Given the equation for the deflection curve or a beam, find the point of maximum deflection
using the bisection method.
Solution: First, substitute the given values of E,I,L and w0 to obtain:
y(x)= -0.2315*10**(-13)*x**5/cm**4 + 0.1667*10**(-7)*x**3/cm**2 - 0.003*x
Then, if we assume that both x and y are in cm, we can drop the units and differentiating,
we get:
y'(x)= -0.11575*(10**(-12))*x**4 + 0.5001*(10**(-7))*x**2 - 0.003
'''		
y_prime= lambda x: -0.11575*(10**(-12))*x**4 + 0.5001*(10**(-7))*x**2 - 0.003
#Then guess two points where we get opposite sign in y_prime. Let...
a=100
b=400
try:
	root= bisect(y_prime, a, b)[0] # because the fun_ return both the root and a list of all the errors at each iteration
	print(root)
except:
	print("Error in input parameters or function definition")




