import bpy  #importing blender info

print("Hello World") 

x = 9

for obj in bpy.data.objects:
    print(obj.name)
    obj.location = [ x, 0, 0]
    x = x + 5    

def add cube (position, rotation, scale):
    bpy.ops.mesh.primitive_cube_add()       #Adds cube to the blender scene.
    cube = bpy.context.selected_objects[0]  #Extracts first object.
    cube.name = "Ryan"                      #Name of object.
    cube.scale = [10, 10, 0.1]              #Scale of object.

