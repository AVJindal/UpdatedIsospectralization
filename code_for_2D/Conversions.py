from shape_library import *
from spectrum_alignment import *
import numpy as np


def vert_triv(object, path):
    shape= open(object, 'r')
    vertices = open("%smesh.vert" %path, 'w')
    faces = open('%smesh.triv' %path, 'w')

    for line in shape:
        if line[:2] == "v ":
            index1 = line.find(" ") + 1
            index2 = line.find(" ", index1 + 1)
            index3 = line.find(" ", index2 + 1)

            vertex = (float(line[index1:index2]), float(line[index2:index3]), float(line[index3:-1]))
            vertex = (round(vertex[0], 2), round(vertex[1], 2), round(vertex[2], 2))
            vertices.write(str(vertex) + "\n")

        elif line[0] == "f":
            string = line.replace("//", "/")

            i = string.find(" ") + 1
            face = []
            for item in range(string.count(" ")):
                if string.find(" ", i) == -1:
                    face.append(string[i:-1])
                    break
                face.append(string[i:string.find(" ", i)])
                i = string.find(" ", i) + 1

            faces.write(str(tuple(face)) + "\n")

    shape.close()
    vertices.close()
    faces.close()
    return
    #not sure if I need these lines, we'll see I guess
    # np.savetxt("%s/mesh.vert" %path, vertices)
    # np.savetxt("%s/mesh.triv" %path, faces)
