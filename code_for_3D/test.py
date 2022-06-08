from shape_library import *
from spectrum_alignment import *

from Conversions import *

#import os
#os.environ["CUDA_VISIBLE_DEVICES"]="1"

params = OptimizationParams()
params.min_eval_loss = 0.0001
params.evals = [20]
params.numsteps = 10000


[VERT, TRIV] = load_mesh('data/round_cuber_1000/'); #Rounded Cube
# [VERT, TRIV] = load_ply('data/Sphere/Sphere.ply')    #Sphere
mesh = prepare_mesh(VERT,TRIV,'float32')

## Cube with extrusion
# [VERT_t, TRIV_t] = load_mesh('data/round_cuber_out_1000/')
# evals_t = calc_evals(VERT_t,TRIV_t)
# run_optimization(mesh = mesh, target_evals = evals_t, out_path = 'results/test_cube_out_disp', params = params)

##Bunny
# [VERT_t, TRIV_t] = load_ply('data/Bunny/bunny.ply')
# evals_t = calc_evals(VERT_t,TRIV_t)
# run_optimization(mesh = mesh, target_evals = evals_t, out_path = 'results/Bunny', params = params)

## Cone - doesn't work at all
# [VERT_t, TRIV_t] = load_ply('data/Cone/Cone.ply')
# evals_t = calc_evals(VERT_t,TRIV_t)
# run_optimization(mesh = mesh, target_evals = evals_t, out_path = 'results/Cone', params = params)

## Torus
# [VERT_t, TRIV_t] = load_ply('data/Torus/Torus.ply')
# evals_t = calc_evals(VERT_t,TRIV_t)
# run_optimization(mesh = mesh, target_evals = evals_t, out_path = 'results/Torus', params = params)

## Dragon
# [VERT_t, TRIV_t] = load_ply('data/Dragon/dragon (4).ply')
# evals_t = calc_evals(VERT_t,TRIV_t)
# run_optimization(mesh = mesh, target_evals = evals_t, out_path = 'results/Dragon', params = params)

##Small Sphere
[VERT_t, TRIV_t] = load_ply('data/Small Sphere/Small Sphere.ply')
evals_t = calc_evals(VERT_t,TRIV_t)
run_optimization(mesh = mesh, target_evals = evals_t, out_path = 'results/SmallSphere', params = params)

## Egg
# vert_triv('data/Egg/Egg.obj', 'data/Egg/')
# [VERT_t, TRIV_t] = load_mesh('data/Egg/')
# [VERT_t, TRIV_t] = load_ply('data/Egg/Eggshell.ply')
# evals_t = calc_evals(VERT_t,TRIV_t)
# run_optimization(mesh = mesh, target_evals = evals_t, out_path = 'results/Egg', params = params)

