import bpy  #importing blender info.
import os   #importing operating system information.

print("Hello World \r\n") 
x = 9

for obj in bpy.data.objects:
    print(obj.name)
    obj.location = [ x, 0, 0]
    x = x + 5    

def add_cube(position, rotation, scale):
    bpy.ops.mesh.primitive_cube_add()       #Adds cube to the blender scene.
    rtn = bpy.context.selected_objects[0]  #Extracts first object.
    rtn.name = "Ryan"                      #Name of object.
    rtn.location = position
    rtn.scale = scale            #Scale of object.
    return rtn



for env in os.environ:
    print(env)