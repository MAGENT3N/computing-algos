import numpy as np 
import matplotlib.pyplot as plt
# for printing numbers upto a precision level of 4 in float system
np.set_printoptions(suppress=True, precision=4)
def main():
    x_start = float(input("Enter x_start: "))
    x_end   = float(input("Enter x_end: "))
    y_start = float(input("Enter y_start: "))
    y_end   = float(input("Enter y_end: "))
    num_samples = int(input("Enter the no of samples: "))
    integral_value,x_rand,y_rand,z_average = monte_carlo(x_start, x_end, y_start, y_end, num_samples, function)
    print(round(integral_value , 3))
    plot_monte_carlo(x_rand,y_rand,z_average)
    
   
"""
   Function for carrying out monte carlo integration
   Parameters:Start and end values of the coordinate axis(area under 
   which we want to calulate the integral), number of samples , and
   our function whose integral is to be calculated
   Return value: Returns the value of the integral within the specified
   bounds,array containing the random drawn values of x,y and average
   z-value,ie,average value of function computed at those random values
   .These returns are for plotting the graph
"""
def monte_carlo(x_start , x_end , y_start , y_end ,no_of_samples,function):
    #Generating random x and y values within the bounds
    x_random = np.random.uniform(x_start,x_end,no_of_samples)
    y_random = np.random.uniform(y_start,y_end,no_of_samples)
    #Averaging the function values computed at those random points
    z_values = function(x_random,y_random)
    average_height = np.mean(z_values)
    # Calculating the area using the start and end values,ie,the bounds
    #... of integration
    area = abs(x_start - x_end) * abs(y_start - y_end)
    integral = average_height * area
    return integral,x_random,y_random,z_values
"""
   Function for plotting the scatter plot in 3-d of our random samples
   and the average values of our function evaluated at those random points
"""
def plot_monte_carlo(x_random, y_random, z_values):
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')

    # Scatter plot: 
    # c=z_values colors the dots based on their height!
    # cmap='viridis' is a nice color gradient
    img = ax.scatter(x_random, y_random, z_values, c=z_values, cmap='viridis', s=2)
    
    # Add a color bar to show the scale
    fig.colorbar(img, ax=ax, label='Z Value (Function Result)')

    ax.set_xlabel('X Random Samples')
    ax.set_ylabel('Y Random Samples')
    ax.set_zlabel('Z Function Height')
    ax.set_title('Monte Carlo Random Samples in 3D')

    plt.show()
    
    
"""
   Function whose integral is to be calculated
"""
   
def function(x,y):
    return np.sin(x) + np.cos(y)


if __name__=="__main__":
    main()