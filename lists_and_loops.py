from vpython import *

# Make a list of cubes that are at the corners of an imaginary 3D cube in space.
# Animate your cubes so that they slowly change colors, 
# but they aren't all the same color at the same time.
cubes = []

large_cube_s = 50
small_cube_s = 10
for i in range(2):
    cubes.append(box(pos=vec(0,(-1)**i*large_cube_s/2,0)))
    cubes.append(box(pos=vec(large_cube_s,(-1)**i*large_cube_s/2,0)))
    cubes.append(box(pos=vec(0,(-1)**i*large_cube_s/2,large_cube_s)))
    cubes.append(box(pos=vec(large_cube_s,(-1)**i*large_cube_s/2,large_cube_s)))

for cube in cubes:
    cube.length = small_cube_s
    cube.width = small_cube_s
    cube.height = small_cube_s


frames = 0
rate(10)

def get_color(r,g,b):
    r = r%255
    g = g%255
    b = b%255

    return vec(r/255,g/255,b/255)

color_change_rate = 1/100
while True:
    for i in range(len(cubes)):
        cubes[i].color = get_color(i**i*color_change_rate,frames*color_change_rate,i*frames*color_change_rate)
    frames += 1

