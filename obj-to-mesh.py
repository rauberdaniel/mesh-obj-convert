#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def main(argv):
    if len(argv) < 2:
        print("Please specify two arguments")
        print("python obj-to-mesh.py infile.obj outfile.mesh")
        sys.exit()

    print("Reading %s" % argv[0])

    try:
        with open(argv[0], 'r') as in_file:
            filedata = in_file.readlines()

            out_data = "MeshVersionFormatted 1\nDimension 3\n\nVertices\n";


            # Vertices
            vertices = [l.split(' ') for l in filedata if l[0:2] == 'v ']
            vertices = [(float(x[1]), float(x[2]), float(x[3])) for x in vertices]

            print("Converting %i Vertices..." % len(vertices))
            out_data += "%i\n" % len(vertices)

            for vertice in vertices:
                out_data += "%f %f %f 0\n" % vertice


            # Fake Normals
            out_data += "\n"
            out_data += "Normals\n"
            out_data += "%i\n" % len(vertices)

            for vertice in vertices:
                out_data += "0.000000000 0.000000000\n"


            # Triangles
            out_data += "\n"
            out_data += "Triangles\n"

            triangles = [l.split(' ') for l in filedata if l[0:2] == 'f ']
            triangles = [(int(t[1].split('//')[0]), int(t[2].split('//')[0]), int(t[3].split('//')[0])) for t in triangles]

            print("Converting %i Triangles…" % len(triangles))
            out_data += "%i\n" % len(triangles)

            for triangle in triangles:
                out_data += "%i %i %i 0\n" % triangle


            with open(argv[1], 'w') as out_file:
                out_file.write(out_data)

    except FileNotFoundError as err:
        print("Input File %s not found" % argv[0])


if __name__ == "__main__":
    main(sys.argv[1:])
