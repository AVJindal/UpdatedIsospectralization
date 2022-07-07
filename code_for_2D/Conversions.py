from shape_library import *
from spectrum_alignment import *
import numpy as np

a = 343  # [m/s]


def vert_triv(object, path):
    shape = open(object, 'r')
    vertices = open("%smesh.vert" % path, 'w')
    faces = open('%smesh.triv' % path, 'w')

    for line in shape:
        if line[:2] == "v ":
            index1 = line.find(" ") + 1
            # index2 = line.find(" ", index1 + 1)
            # index3 = line.find(" ", index2 + 1)

            vertices.write(str(line[index1:]))

        elif line[0] == "f":
            string = line.replace("//", " ")

            i = string.find(" ") + 1
            face = []
            for item in range(string.count(" ")):
                if string.find(" ", i) == -1:
                    face.append(string[i:-1])
                    break
                face.append(string[i:string.find(" ", i)])
                i = string.find(" ", i) + 1

            # Very ugly but it does what I want... The file still maybe formatted badly however(?)
            face = str(np.array(list(set(face))))
            face = face.replace("'", "")
            face = face.replace("[", "")
            face = face.replace("]", "")

            faces.write(face + "\n")

    shape.close()
    vertices.close()
    faces.close()
    return
    # not sure if I need these lines, we'll see I guess
    # np.savetxt("%s/mesh.vert" %path, vertices)
    # np.savetxt("%s/mesh.triv" %path, faces)

def hertz(values):
    new= []
    for i in range(len(values)):
        new.append(values[i]/(2*np.pi))
    return np.array(new)


def string_evals(L):
    evals= []
    for n in range(1,30):
        evals.append((a * n * np.pi) / L)
    evals.sort()
    print(evals)
    return np.array(evals)

def rectangle_evals(L, H):
    evals = []
    for n in range(1, 10):
        for k in range(1, 10):
            evals.append(a * np.pi * ((k / H)**2 + (n / L) ** 2) ** (1 / 2))
    evals.sort()
    return np.array(evals)

def RATriangle(b):
    evals = []
    for n in range(1, 6):
        for m in range(1, 6):
            # evals.append((np.pi/a)**2*((m+n)**2)+n**2)
            evals.append(a * ((np.pi / b )  * ((m + n) ** 2 + n ** 2) * ( 1 / 2)))
    evals.sort()
    print(len(evals))
    return np.array(evals)