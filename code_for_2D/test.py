from shape_library import *
from spectrum_alignment import *

from Conversions import *

# import os
# os.environ["CUDA_VISIBLE_DEVICES"]="1"

params = OptimizationParams()
params.evals = [20]
params.numsteps = 8000
params.plot=False


[VERT, TRIV] = load_mesh('data/oval/'); # Oval Setup (Bell, Mickey)

# # Square setup (stepfunc)
# vert_triv('data/Square/Square.obj', 'data/Square/')
# [VERT, TRIV] = load_ply('data/Square/Round Square.ply');

# [VERT, TRIV] = load_ply('data/Star/SmoothStar3.ply'); # Star setup

# Circle Setup (Apple)
# vert_triv('data/Circle/Circle.obj', 'data/Circle/')
# [VERT, TRIV] = load_mesh('data/Circle/');
# [VERT, TRIV] = load_ply('data/Circle/Circle2.ply');

#Donut - does not work at all - it is not simply connected but it should still work because they do similar examples in the paper
# [VERT, TRIV] = load_ply('data/Donut/Donut.ply');

# #load
[VERT,TRIV] = resample(VERT, TRIV, 300)
mesh = prepare_mesh(VERT,TRIV,'float32')

# #Mickey
# [VERT_t, TRIV_t] = load_mesh('data/mickey/')
# evals_t = calc_evals(VERT_t,TRIV_t)
# run_optimization(mesh = mesh, target_evals = evals_t, out_path = 'results/mickey', params = params)

# #Bell
# [VERT_t, TRIV_t] = load_mesh('data/bell/')
# evals_t = calc_evals(VERT_t,TRIV_t)
# run_optimization(mesh = mesh, target_evals = evals_t, out_path = 'results/bell', params = params)

# #My Apple logo - won't run because files are formatted badly
# vert_triv('data/Apple/Apple Logo.obj', 'data/Apple/')
# [VERT_t, TRIV_t] = load_mesh('data/Apple/')
# [VERT_t,TRIV_t] = resample(VERT_t, TRIV_t, 300)
# evals_t = calc_evals(VERT_t,TRIV_t)
# run_optimization(mesh = mesh, target_evals = evals_t, out_path = 'results/Apple', params = params)

# # Step function-looking one (2D pneuflex?)
# vert_triv('data/Stepfunc/Stepfunc.obj', 'data/Stepfunc/')
# [VERT_t, TRIV_t] = load_mesh('data/Stepfunc/')

# [VERT_t, TRIV_t] = load_ply('data/Stepfunc/stepfunc2.ply')
# [VERT_t,TRIV_t] = resample(VERT_t, TRIV_t, 300)
# evals_t = calc_evals(VERT_t,TRIV_t)
# run_optimization(mesh = mesh, target_evals = evals_t, out_path = 'results/Stepfunc', params = params)

# # Flower (mine)
# vert_triv('data/Flower/Flower.obj', 'data/Flower/')
#
# [VERT_t, TRIV_t] = load_ply('data/Flower/Flower.ply')
# #[VERT_t,TRIV_t] = resample(VERT_t, TRIV_t, 300)
# evals_t = calc_evals(VERT_t,TRIV_t)
# run_optimization(mesh = mesh, target_evals = evals_t, out_path = 'results/Flower', params = params)

# #Trillium
# [VERT_t, TRIV_t] = load_ply('data/Trillium/Trillium4.ply')
# #[VERT_t,TRIV_t] = resample(VERT_t, TRIV_t, 300)
# evals_t = calc_evals(VERT_t,TRIV_t)
# run_optimization(mesh = mesh, target_evals = evals_t, out_path = 'results/Trillium', params = params)


# Heart (mine) - actually works!
# [VERT_t, TRIV_t] = load_ply('data/Heart/heart.ply')
# #[VERT_t,TRIV_t] = resample(VERT_t, TRIV_t, 300)
# evals_t = calc_evals(VERT_t,TRIV_t)
# run_optimization(mesh = mesh, target_evals = evals_t, out_path = 'results/Heart', params = params)

# ## Star
# [VERT_t, TRIV_t] = load_ply('data/Star/Star2.ply')
# # [VERT_t,TRIV_t] = resample(VERT_t, TRIV_t, 300)
# evals_t = calc_evals(VERT_t,TRIV_t)
# run_optimization(mesh = mesh, target_evals = evals_t, out_path = 'results/Star', params = params)

##Stubby star
# [VERT_t, TRIV_t] = load_ply('data/Star/SmoothStar.ply')
# # [VERT_t,TRIV_t] = resample(VERT_t, TRIV_t, 300)
# evals_t = calc_evals(VERT_t,TRIV_t)
# run_optimization(mesh = mesh, target_evals = evals_t, out_path = 'results/SmoothStar', params = params)

## Plane
# [VERT_t, TRIV_t] = load_ply('data/Plane/Plane.ply')
# # [VERT_t,TRIV_t] = resample(VERT_t, TRIV_t, 300)
# evals_t = calc_evals(VERT_t,TRIV_t)
# run_optimization(mesh = mesh, target_evals = evals_t, out_path = 'results/Plane', params = params)

# # Square
# [VERT_t, TRIV_t] = load_ply('data/Square/Round Square.ply');
# evals_t = calc_evals(VERT_t,TRIV_t)
#
# run_optimization(mesh = mesh, target_evals = evals_t, out_path = 'results/Square', params = params)

# # Circle
# [VERT_t, TRIV_t] = load_ply('data/Circle/Circle2.ply');
# # [VERT_t,TRIV_T] = resample(VERT_t, TRIV_t, 300)
# evals_t = calc_evals(VERT_t,TRIV_t)
# run_optimization(mesh = mesh, target_evals = evals_t, out_path = 'results/Circle', params = params)

#Square donut - Does not work at all :( (read above about donut initial mesh)
# [VERT_t, TRIV_t] = load_ply('data/Donut/SquareDonut.ply');
# # [VERT_t,TRIV_T] = resample(VERT_t, TRIV_t, 300)
# evals_t = calc_evals(VERT_t,TRIV_t)
# run_optimization(mesh = mesh, target_evals = evals_t, out_path = 'results/Square Donut', params = params)

# evals_t= rectangle_evals(1,0.5)
# run_optimization(mesh = mesh, target_evals = evals_t, out_path = 'results/n1to500', params = params)

[VERT_t, TRIV_t] = load_ply('data/Simple shapes/Rect(0.15x0.3).ply');
evals_t = calc_evals(VERT_t,TRIV_t)
# evals_t = RATriangle(0.5)
# run_optimization(mesh = mesh, target_evals = evals_t, out_path = 'results/RAT(0.5)', params = params)

# [VERT_t, TRIV_t] = load_ply('data/Strings/string(150mm).ply');
# evals_t = calc_evals(VERT_t,TRIV_t)
# evals_t = string_evals(150)
# run_optimization(mesh = mesh, target_evals = evals_t, out_path = 'results/String(150mm)', params = params)

## collecting Eigenvalues
# eval = calc_evals(VERT,TRIV)
# eval= RATriangle(0.5)
np.savetxt('Frequencies/rect(0.15x0.3)(HZ).txt', hertz(evals_t))
