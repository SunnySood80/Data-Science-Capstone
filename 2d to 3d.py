import bpy
import os
import random
import math

def setup_scene():
    # Set up the scene
    scene = bpy.context.scene

    # Clear existing objects.
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()

    # Set render engine to Cycles for better quality (can also use Eevee)
    scene.render.engine = 'CYCLES'
    scene.cycles.device = 'GPU' # If you have a GPU, otherwise use 'CPU'

    return scene

def create_lighting():
    # Add a new light
    bpy.ops.object.light_add(type='SUN', radius=1, location=(0, 0, 5))
    light = bpy.context.object

    # Set the light's parameters
    light.data.energy = 3

def create_camera():
    # Add a new camera
    bpy.ops.object.camera_add(location=(0, -3, 2), rotation=(math.radians(75), 0, math.radians(180)))
    camera = bpy.context.object

    # Set the camera's parameters
    camera.data.lens = 35  # Focal length

    return camera

def create_leaf(image_path, image_displace_strength=0.2, noise_displace_strength=0.3, bend_angle_x=25.0, bend_angle_y=25.0, bend_angle_z=25.0):
    # Add a plane
    bpy.ops.mesh.primitive_plane_add(size=2, enter_editmode=False, align='WORLD', location=(0, 0, 0))
    plane = bpy.context.active_object

    # Ensure it's the active object
    bpy.context.view_layer.objects.active = plane
    plane.select_set(True)

    # Subdivide the plane
    bpy.ops.object.editmode_toggle()
    bpy.ops.mesh.subdivide(number_cuts=27)
    bpy.ops.object.editmode_toggle()

    # Add Displacement Modifier for image texture
    disp_mod = plane.modifiers.new(name="Image Displace", type='DISPLACE')
    tex = bpy.data.textures.new(name="Image Texture", type='IMAGE')
    tex.image = bpy.data.images.load(image_path)
    disp_mod.texture = tex
    disp_mod.strength = image_displace_strength

    # Add Displacement Modifier for noise
    noise_disp_mod = plane.modifiers.new(name="Noise Displace", type='DISPLACE')
    noise_tex = bpy.data.textures.new(name="Noise Texture", type='CLOUDS')
    noise_disp_mod.texture = noise_tex
    noise_disp_mod.strength = noise_displace_strength

    # Set shading to smooth
    bpy.ops.object.shade_smooth()

    # Add a Simple Deform (Bend) Modifier for each axis
    bend_mod_x = plane.modifiers.new(name="Bend X", type='SIMPLE_DEFORM')
    bend_mod_x.deform_method = 'BEND'
    bend_mod_x.deform_axis = 'X'
    bend_mod_x.factor = math.radians(bend_angle_x)

    bend_mod_y = plane.modifiers.new(name="Bend Y", type='SIMPLE_DEFORM')
    bend_mod_y.deform_method = 'BEND'
    bend_mod_y.deform_axis = 'Y'
    bend_mod_y.factor = math.radians(bend_angle_y)

    bend_mod_z = plane.modifiers.new(name="Bend Z", type='SIMPLE_DEFORM')
    bend_mod_z.deform_method = 'BEND'
    bend_mod_z.deform_axis = 'Z'
    bend_mod_z.factor = math.radians(bend_angle_z)

    # Create a material and assign
    mat = bpy.data.materials.new(name="Leaf Material")
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes["Principled BSDF"]
    tex_image = mat.node_tree.nodes.new('ShaderNodeTexImage')
    tex_image.image = bpy.data.images.load(image_path)
    mat.node_tree.links.new(bsdf.inputs['Base Color'], tex_image.outputs['Color'])

    plane.data.materials.append(mat)

    # Adjust material settings for transparency
    mat.blend_method = 'BLEND'

    # Add Subdivision Surface Modifier for smoother geometry
    subdiv_mod = plane.modifiers.new(name="Subdivision Surface", type='SUBSURF')
    subdiv_mod.levels = 2
    subdiv_mod.render_levels = 2

    return plane

def render_scene(scene, camera, output_path):
    # Set the output path for the render
    scene.render.filepath = output_path
    scene.render.image_settings.file_format = 'PNG'  # Set output format to .png

    # Set the active camera
    scene.camera = camera

    # Render Scene
    bpy.ops.render.render(write_still=True)

if __name__ == "__main__":
    # Define paths
    image_path = r"C:\path\to\your\image.jpg"  # replace with your image path
    render_output_path = r"C:\path\to\your\output\render.png"  # replace with your desired output path

    # Verify paths
    if not os.path.exists(image_path):
        print(f"No image found at {image_path}")
    else:
        # Setup scene
        current_scene = setup_scene()

        # Create lights
        create_lighting()

        # Create camera
        cam = create_camera()

        # Displacement strengths and bend angles for X, Y, and Z axes
        image_displace_strength = random.uniform(0.1, 0.3)
        noise_displace_strength = random.uniform(0.1, 0.5)
        bend_angle_x = random.uniform(-30, 30)
        bend_angle_y = random.uniform(-30, 30)
        bend_angle_z = random.uniform(-30, 30)

        # Create the leaf with modifiers
        created_plane = create_leaf(image_path, image_displace_strength, noise_displace_strength, bend_angle_x, bend_angle_y, bend_angle_z)

        # Render the scene
        render_scene(current_scene, cam, render_output_path)

        print(f"Render complete! Image saved at {render_output_path}")
