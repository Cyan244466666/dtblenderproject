import os   #importing operating system information.
import bpy  #importing blender info.
import sys

for env in os.environ:
 print(env)
 
for arg in sys.argv:
 print(arg)
 
bpy.ops.object.select_all(action='DESELECT')
for obj in bpy.data.objects:
  if obj.type == 'MESH':
   obj.select_set(True)
bpy.ops.object.delete()

path = curuthers/'curuthers.obj'
bpy.ops.import_scene.obj(filepath=path)
obj = bpy.context.selected_objects[0]
