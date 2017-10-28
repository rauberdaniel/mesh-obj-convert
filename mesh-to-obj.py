#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def main(argv):
    if len(argv) < 2:
        print("Please specify two arguments")
        print("python mesh-to-obj.py infile.mesh outfile.obj")
        sys.exit()

    print("Reading %s" % argv[0])

    try:
        with open(argv[0], 'r') as in_file:
            filedata = in_file.readlines()

            number_of_vertices = int(filedata[4]);
            print("%i Vertices" % number_of_vertices)

            number_of_normals = int(filedata[4+number_of_vertices+3])
            #print("%i Normals" % number_of_normals)

            number_of_triangles = int(filedata[4+number_of_vertices+3+number_of_normals+3])
            print("%i Triangles" % number_of_triangles)

            out_data = "";
            out_data += "o Scenery\n"

            print("Converting Vertices...")
            for x in range(5,number_of_vertices+5):
                line = filedata[x]
                coords = line.split(' ')
                coords.pop()
                coords = [float(coord) for coord in coords]
                out_data += "v %f %f %f\n" % (coords[0], coords[1], coords[2])

            out_data += "s off\n"

            print("Converting Triangles...")
            for x in range(number_of_vertices+number_of_normals+11,number_of_vertices+number_of_normals+11+number_of_triangles):
                line = filedata[x]
                indexes = line.split(' ')
                indexes.pop()
                indexes = [int(index) for index in indexes]
                out_data += "f %i %i %i\n" % (indexes[0], indexes[1], indexes[2])


            print("Writing obj file %s" % argv[1])
            with open(argv[1], 'w') as out_file:
                out_file.write(out_data)
    except FileNotFoundError as err:
        print("Input File %s not found" % argv[0])


if __name__ == "__main__":
    main(sys.argv[1:])
