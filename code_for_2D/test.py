from shape_library import *
from spectrum_alignment import *

from Conversions import *

#import os
#os.environ["CUDA_VISIBLE_DEVICES"]="1"

params = OptimizationParams()
params.evals = [20]
params.numsteps = 5000
params.plot=False

# # Oval Setup (Bell, Mickey)
[VERT, TRIV] = load_mesh('data/oval/');
[VERT,TRIV] = resample(VERT, TRIV, 300)

# # Square setup (stepfunc)
# vert_triv('data/Square/Square.obj', 'data/Square/')
# [VERT, TRIV] = load_mesh('data/Square/');
# [VERT,TRIV] = resample(VERT, TRIV, 300)

# # Circle Setup (Apple)
# vert_triv('data/Circle/Circle.obj', 'data/Circle/')
# [VERT, TRIV] = load_mesh('data/Circle/');
# [VERT,TRIV] = resample(VERT, TRIV, 300)

# #Mickey
# [VERT_t, TRIV_t] = load_mesh('data/mickey/')
# evals_t = calc_evals(VERT_t,TRIV_t)
# mesh = prepare_mesh(VERT,TRIV,'float32')
# run_optimization(mesh = mesh, target_evals = evals_t, out_path = 'results/mickey', params = params)

# #Bell
# [VERT_t, TRIV_t] = load_mesh('data/bell/')
# evals_t = calc_evals(VERT_t,TRIV_t)
# mesh = prepare_mesh(VERT,TRIV,'float32')
# run_optimization(mesh = mesh, target_evals = evals_t, out_path = 'results/bell', params = params)

# #My Apple logo - won't run because files are formatted badly
# vert_triv('data/Apple/Apple Logo.obj', 'data/Apple/')
# [VERT_t, TRIV_t] = load_mesh('data/Apple/')
# [VERT_t,TRIV_t] = resample(VERT_t, TRIV_t, 300)
# evals_t = calc_evals(VERT_t,TRIV_t)
# mesh = prepare_mesh(VERT,TRIV,'float32')
# run_optimization(mesh = mesh, target_evals = evals_t, out_path = 'results/Apple', params = params)

# # Step function-looking one (2D pneuflex?)
vert_triv('data/Stepfunc/Stepfunc.obj', 'data/Stepfunc/')
[VERT_t, TRIV_t] = load_mesh('data/Stepfunc/')
#[VERT_t,TRIV_t] = resample(VERT_t, TRIV_t, 300)
evals_t = calc_evals(VERT_t,TRIV_t)
mesh = prepare_mesh(VERT,TRIV,'float32')
run_optimization(mesh = mesh, target_evals = evals_t, out_path = 'results/Stepfunc', params = params)

# # Flower (mine)
# vert_triv('data/Flower/Flower.obj', 'data/Flower/')
# [VERT_t, TRIV_t] = load_mesh('data/Flower/')
# [VERT_t,TRIV_t] = resample(VERT_t, TRIV_t, 300)
# evals_t = calc_evals(VERT_t,TRIV_t)
# mesh = prepare_mesh(VERT,TRIV,'float32')
# run_optimization(mesh = mesh, target_evals = evals_t, out_path = 'results/Flower', params = params)
