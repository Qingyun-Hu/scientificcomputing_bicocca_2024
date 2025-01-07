#!/usr/bin/env python3
def randcircle(num):
    import matplotlib.pyplot as plt
    import numpy as np
    theta = np.linspace(0,2*np.pi,100)
    def draw_circle(x0, y0, R, color):
        x = R*np.cos(theta) + x0
        y = R*np.sin(theta) + y0
        plt.fill(x,y,color)

    plt.figure()
    count = 0
    for i in np.arange(num):
        x1 = np.random.rand()*2
        y1 = np.random.rand()*2
        R1 = np.random.rand()*0.5
        c1 = np.random.rand(1,3)
        draw_circle(x1,y1,R1,c1)
        count = count + 1
    print(x1,c1)

    plt.axis('equal')
    plt.xlabel("x (m)")
    plt.ylabel("y (m)")
    plt.show()
    return count

def test_randcircle():
    count = randcircle(3)
    assert count == 3

if __name__ == "__main__":
    randcircle(10)