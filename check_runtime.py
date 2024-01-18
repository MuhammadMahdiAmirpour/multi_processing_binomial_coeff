from bicoeff import get_bicoeff

import matplotlib.pyplot as plt
import timeit

if __name__ == "__main__":
    nks = [(4, 3), (5, 3), (6, 3), (7, 4), (8, 4), (9, 4), (10, 4)]
    time_list = []
    for nk in nks:
        t = timeit.Timer(lambda: get_bicoeff(nk[0], nk[1]))
        time_list.append(t.timeit(5)/5)
    plt.plot(list(range(len(nks))), time_list, "d-")
    plt.show()


