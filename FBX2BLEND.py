import bpy
bpy.data.filepath
file_path = bpy.data.filepath
file_name = bpy.path.display_name_from_filepath(file_path)
file_fbx = ".fbx"
file_blend = ".blend"
# Import FBX
bpy.ops.import_scene.fbx( filepath = file_name+file_fbx)
# Export blend file
bpy.ops.wm.save_mainfile( filepath = file_name+file_blend)
# Close Blender
bpy.ops.wm.quit_blender()