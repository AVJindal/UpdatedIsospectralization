import matplotlib.pyplot as plt
import numpy as np
from shape_library import *
from spectrum_alignment import *
import csv

params = OptimizationParams()
params.numsteps = 8000

def get_data(outpath, algorithm="AdagradOptimizer", rate= 0.99 ):
    [VERT, TRIV] = load_mesh('data/oval/')
    [VERT, TRIV] = resample(VERT, TRIV, 300)
    mesh = prepare_mesh(VERT, TRIV, 'float32')

    [VERT_t, TRIV_t] = load_ply('data/Heart/heart.ply')
    evals_t = calc_evals(VERT_t, TRIV_t)
    data = run_optimization(mesh=mesh, target_evals=evals_t, out_path=outpath, params=params, algorithm= algorithm, learningrate=rate)
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
    all_err = []
    all_iter = []
    all_als = []
    # for algorithm in als:
    #     for learn in als.get(algorithm):
    #         print('%s (%f)'%(algorithm, learn))
    #         err_trials = []
    #         iter_trials = []
    #         # for i in range(3):
    #         if 1==1:
    #             dat= get_data(outpath= 'results/Heart/heart(%s %f)' %(algorithm, learn), algorithm=algorithm, rate= learn)
    #             err_trials.append(dat[-1,1])
    #             iter_trials.append(dat[-1, 0])
    #         err= np.average(err_trials)
    #         iterr= np.average(iter_trials)
    #         all_err.append(err)
    #         all_iter.append(iterr)
    #         all_als.append("%s (%f)" %(algorithm, round(learn, 2)))
    #         algs.update({"%s (%f)" %(algorithm, round(learn, 2)): [err, iterr]})
    ###test
    # all_err = [1,2]
    # all_iter = [3,4]
    # all_als = ['wow', 'oup']
    w = csv.writer(open("Graphs/1trial.csv", "w"))
    for key, val in algs.items():
        w.writerow([key, val[0], val[1]])

    barWidth = 0.25
    fig, ax = plt.subplots(figsize=(12, 8))
    ax2=ax.twinx()
    br1 = np.arange(len(all_err))
    br2 = [x + barWidth for x in br1]

    ax.bar(br1, all_err, color='r', width=barWidth, edgecolor='grey', label='Final Error')
    ax2.bar(br2, all_iter, color='b', width=barWidth, edgecolor='grey', label='Total Iterations')

    # Adding Xticks
    ax.set_xlabel('Algorithm and Learning Rate', fontweight='bold', fontsize=15)
    ax.set_ylabel('Error', fontweight='bold', fontsize=15)
    ax2.set_ylabel('Iterations', fontweight='bold', fontsize=15)
    plt.xticks(br1 + barWidth/2, all_als)
    plt.title('Optimization Algorithm Evaluation')

    plt.legend()
    plt.show()

algorithms()





