def function(x):
    return (x+3)**2

def derivative(x):
    return 2*(x+3)

x=2
learning_rate=0.1
iteration=1000
tolerance=1e-6

for i in range (iteration):
    gradient= derivative(x)
    new_x=x-learning_rate*gradient
    
    if abs( new_x-x) < tolerance:
        print("Converged at iteration:",i+1)
        break

    x=new_x
    

print("Local Minima:",x)
#print("Minimum value of the function y is:",function(x))




    