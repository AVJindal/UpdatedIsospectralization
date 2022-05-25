from shape_library import *
from spectrum_alignment import *

from Conversions import *

#import os
#os.environ["CUDA_VISIBLE_DEVICES"]="1"

params = OptimizationParams()
params.evals = [20]
params.numsteps = 5000
params.plot=False

[VERT, TRIV] = load_mesh('data/oval/');
[VERT,TRIV] = resample(VERT, TRIV, 300)

# [VERT_t, TRIV_t] = load_mesh('data/mickey/')
# evals_t = calc_evals(VERT_t,TRIV_t)
# mesh = prepare_mesh(VERT,TRIV,'float32')
# run_optimization(mesh = mesh, target_evals = evals_t, out_path = 'results/mickey', params = params)

# [VERT_t, TRIV_t] = load_mesh('data/bell/')
# evals_t = calc_evals(VERT_t,TRIV_t)
# mesh = prepare_mesh(VERT,TRIV,'float32')
# run_optimization(mesh = mesh, target_evals = evals_t, out_path = 'results/bell', params = params)


# #My Apple logo - won't run because files are formatted badly
vert_triv('data/Apple/Apple Logo.obj', 'data/Apple/')
[VERT_t, TRIV_t] = load_mesh('data/Apple/')
evals_t = calc_evals(VERT_t,TRIV_t)
mesh = prepare_mesh(VERT,TRIV,'float32')
run_optimization(mesh = mesh, target_evals = evals_t, out_path = 'results/Apple', params = params)