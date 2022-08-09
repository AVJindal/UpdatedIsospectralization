import matplotlib.pyplot as plt
import numpy as np
from shape_library import *
from spectrum_alignment import *

params = OptimizationParams()
params.numsteps = 8000

def get_data(algorithm = "AdagradOptimizer", rate = 0.99 ):
    [VERT, TRIV] = load_mesh('data/oval/')
    [VERT, TRIV] = resample(VERT, TRIV, 300)
    mesh = prepare_mesh(VERT, TRIV, 'float32')

    [VERT_t, TRIV_t] = load_ply('data/Heart/heart.ply')
    evals_t = calc_evals(VERT_t, TRIV_t)
    data = run_optimization(mesh=mesh, target_evals=evals_t, out_path='results/Heart', params=params, algorithm= algorithm, rate=rate)
    return data

def iterations_error():
    data= get_data()
    plt.title("Oval to Heart: Error Vs Iterations")
    plt.xlabel("Iterations")
    plt.ylabel("Error") # Change name?
    plt.plot(data[:,0], data[:,1], 'b-')
    # plt.plot(np.array(np.arange(len(data[:,1])), data[:,1], 'b-'))
    print(range(len(data[:,1])))
    plt.grid()
    plt.show()
    plt.savefig("Graphs/HeartError.png")

def algorithms():
    als= {"AdamOptimizer": [0.005], "AdadeltaOptimizer": [0.005, 0.5, 0.99] , "AdagradOptimizer": [0.005, 0.5, 0.99]}
    algs= {}
    for algorithm in als:
        for learn in als.get(algorithm):
            err_trials = []
            iter_trials = []
            for i in range(10):
                dat= get_data(algorithm, rate= learn)
                err_trials.append(dat[-1,1])
                iter_trials.append(dat[-1, 1])
            err= np.average(err_trials)
            iterr= np.average(iter_trials)
            algs.update({"%s (%d)"%algorithm %learn: [err, iterr]})
    fig= plt.figure()
    ax= fig.add_axes([0,0,1,1])
    for entry in algs:
        ax.bar(entry, algs.get(entry[0]), color= 'b', width= 0.25)
        ax.bar(entry, algs.get(entry[1]), color= 'b', width= 0.25)
    plt.show()
    plt.savefig("Graphs/Algorithms.png")

algorithms()





