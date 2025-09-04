from initial_conditions import *
import numpy as np
import tkinter as tk
#from random import randint
#import matplotlib.pyplot as plt

WIDTH = DAYS //2
HEIGHT = 400

X_INTERVAL = WIDTH / DAYS
Y_SCALE = .90

# Create the main window
window = tk.Tk()
window.title("PSIR Simulation V1")

# Create a canvas widget
canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

S = np.zeros(DAYS)
I = np.zeros(DAYS)
R = np.zeros(DAYS)

S[0], I[0], R[0] = S0, I0, R0
S_points, I_points, R_points = [], [], []

for t in range(1, DAYS):
    S[t] = S[t-1] - (BETA * S[t-1] * I[t-1]) / N
    I[t] = I[t-1] + (BETA * S[t-1] * I[t-1]) / N - GAMMA * I[t-1]
    R[t] = R[t-1] + GAMMA * I[t-1]
    

    if N < N0:
        N += 10
        S[t] += 10

    # if R[t] > 3:
    #     R[t] -= 1
    #     N -= 1


    # num = randint(0, 10)
    # if num >= 5 and R[t] > 0 and S[t]+1 < N:
    #     R[t] -= 1
    #     S[t] += 1


# Function to draw a point
def draw_point(x, y, c):
    # Draw a small circle (oval) to represent the point
    r = 2  # radius of the point
    canvas.create_oval(x - r, y - r, x + r, y + r, fill=c)

def draw_line(p1, p2, c):
    canvas.create_line(p1[0], p1[1], p2[0], p2[1], fill=c)


for i in range(DAYS):
    x = i*X_INTERVAL

    s_percent = S[i] / N
    s_y = HEIGHT - s_percent * HEIGHT

    S_points.append([x, s_y*Y_SCALE+0.05*HEIGHT])
    # draw_point(s_x, s_y, "blue")

    i_percent = I[i] / N
    i_y = HEIGHT - i_percent * HEIGHT

    I_points.append([x, i_y*Y_SCALE+0.05*HEIGHT])
    # draw_point(i_x, i_y , "red")

    r_percent = R[i] / N
    r_y = HEIGHT - r_percent * HEIGHT

    R_points.append([x, r_y*Y_SCALE+0.05*HEIGHT])
    # draw_point(r_y , r_y , "green")

for i in range(1, DAYS):
    draw_line(S_points[i-1], S_points[i], "blue")
    draw_line(I_points[i-1], I_points[i], "red")
    draw_line(R_points[i-1], R_points[i], "green")

# Start the Tkinter main loop
window.mainloop()

# Plotting the results
# plt.figure(figsize=(10, 6))
# plt.plot(S, label='Susceptible', color='blue')
# plt.plot(I, label='Infected', color='red')
# plt.plot(R, label='Recovered', color='green')
# plt.title('SIR Model')
# plt.xlabel('Days')
# plt.ylabel('Population')
# plt.legend()
# plt.grid()
# plt.show()