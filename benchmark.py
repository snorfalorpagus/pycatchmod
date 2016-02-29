from pycatchmod import SubCatchment
import numpy as np
import time

def f():
    n = 10
    area = 100.0
    subcatchment = SubCatchment(100.0, np.zeros(n), np.zeros(n), np.zeros(n), np.zeros(n),
                                direct_percolation=0.2, potential_drying_constant=100, gradient_drying_curve=0.3,
                                linear_storage_constant=0.5, nonlinear_storage_constant=10.0)

    rainfall = np.arange(n, dtype=np.float64)
    pet = np.arange(n, dtype=np.float64)[::-1]
    percolation = np.empty_like(rainfall)
    outflow = np.empty_like(rainfall)

    for n in range(0, 365*100):
        subcatchment.step(rainfall, pet, percolation, outflow)

def run(f, count):
    t0 = time.clock()
    for n in range(0, count):
        f()
    tn = time.clock()
    return (tn-t0) / count

if __name__ == '__main__':
    print(run(f, 5))
