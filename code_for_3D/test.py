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
# [VERT, TRIV] = load_ply('data/Egg/EggShell.ply')    #Egg
# [VERT, TRIV] = load_ply('data/Cylinder/Cylinder2.ply')    #Cylinder - doesn't work ! interessante
# [VERT, TRIV] = load_ply('data/Cone/Cone(70)2.ply')    #Cone (70)
mesh = prepare_mesh(VERT,TRIV,'float32')

## collecting Eigenvalues
# eval = calc_evals(VERT,TRIV)
#np.savetxt('Expected values/Round Cube EVals.txt', eval)


## Cube with extrusion
# [VERT_t, TRIV_t] = load_mesh('data/round_cuber_out_1000/')
# evals_t = calc_evals(VERT_t,TRIV_t)
# run_optimization(mesh = mesh, target_evals = evals_t, out_path = 'results/test_cube_out_disp', params = params)

##Bunny
# [VERT_t, TRIV_t] = load_ply('data/Bunny/bunny.ply')
# evals_t = calc_evals(VERT_t,TRIV_t)
# run_optimization(mesh = mesh, target_evals = evals_t, out_path = 'results/Bunny', params = params)

## Cone
# [VERT_t, TRIV_t] = load_ply('data/Cone/Cone(50)3.ply')
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
# [VERT_t, TRIV_t] = load_ply('data/Small Sphere/Small Sphere.ply')
# evals_t = calc_evals(VERT_t,TRIV_t)
# run_optimization(mesh = mesh, target_evals = evals_t, out_path = 'results/SmallSphere', params = params)

## Egg
# vert_triv('data/Egg/Egg.obj', 'data/Egg/')
# [VERT_t, TRIV_t] = load_mesh('data/Egg/')
# [VERT_t, TRIV_t] = load_ply('data/Egg/Eggshell.ply')
# evals_t = calc_evals(VERT_t,TRIV_t)
# run_optimization(mesh = mesh, target_evals = evals_t, out_path = 'results/Egg', params = params)

## Cylinder
# [VERT_t, TRIV_t] = load_ply('data/Cylinder/Cylinder2.ply')
# evals_t = calc_evals(VERT_t,TRIV_t)


[VERT_t, TRIV_t] = load_ply('data/Prisms/prism(1x1x0.15).ply')
evals_t = calc_evals(VERT_t,TRIV_t)
run_optimization(mesh = mesh, target_evals = evals_t, out_path = 'results/Cylinder', params = params)

## My prism eigenvalues
# evals_t= prism_evals(1,0.5,0.15)
# run_optimization(mesh = mesh, target_evals = evals_t, out_path = 'results/2x3x10frcube', params = params)
# [VERT_t, TRIV_t] = load_ply('data/Prisms/prism(1x1x0.15).ply')
# evals_t = calc_evals(VERT_t,TRIV_t)
# np.savetxt('Frequencies/prism(1x0.5x0.15)(HZ).txt', hertz(evals_t))



