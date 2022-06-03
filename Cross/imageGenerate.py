if __name__ == '__main__' :
    import matplotlib.pyplot as plt
    import numpy as np
    from decimal import *
    data = np.loadtxt("data.txt")
    meanspeedr = np.around(data[1, :], 2)
    x = np.around(1 / data[0, :], 2)

    plt.plot(x, meanspeedr)
    plt.xlabel("Arrive Rate")
    plt.ylabel("Stop Rate")
    plt.show()
