## Convert .mesh to .obj

Usage: `python mesh-to-obj.py infile.mesh outfile.obj`

## Convert .obj to .mesh

Usage: `python obj-to-mesh.py infile.obj outfile.mesh`

## Remarks

You will notice a rectangular grid when opening a .obj file that you converted from a Ortho4XP mesh. This is the (usually ZL19) grid from Ortho4XP which is used to align the images tiles. Make sure you only change the elevation of vertices belongig to this grid but not their coordinates to prevent distorted textures.

## Known Issues

Both conversions are currently dropping the Normals. If you have issues when opening the .obj file in Blender, select all Vertices in Edit Mode and press `ctrl+n` to recalculate the normals. If necessary, you can then also flip the normals by selecting `Mesh > Normals > Flip` in the menu.

## Reference

- Mesh Format: [University of Bordeaux](https://www.math.u-bordeaux.fr/~dobrzyns/logiciels/RT-422/node59.html)
- OBJ Format: [Wikipedia](https://en.wikipedia.org/wiki/Wavefront_.obj_file)
