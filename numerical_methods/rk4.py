import math
from grapher import plottingfunction

def main():
    starting_time = float(input("Enter starting time: "))
    end_time = float(input("Enter end time: "))
    step_size = float(input("Enter step size: "))
    initial_condition = float(input("Enter the initial value: "))
    
    y_values, time_values = rk_4(f, starting_time, end_time, step_size, initial_condition)
    plottingfunction(time_values, y_values,'rk-4','time','y' , 'rk4')
    
    for t, y in zip(time_values, y_values):
        print(f"t = {t:.4f}, y = {y:.4f}")

def rk_4(f, to, tf, h, yo):
    t = to
    y = yo
    time_values = [t]
    y_values = [yo]

    while t <= tf:
        k1 = h * f(t, y)
        k2 = h * f(t + h/2, y + k1/2)
        k3 = h * f(t + h/2, y + k2/2)
        k4 = h * f(t + h, y + k3)
        y = y + 1/6 * (k1 + 2*k2 + 2*k3 + k4)
        t = t + h
        y_values.append(y)
        time_values.append(t)

    return y_values, time_values

def f(t, y):
    return math.cos(t)

if __name__ == "__main__":
    main()