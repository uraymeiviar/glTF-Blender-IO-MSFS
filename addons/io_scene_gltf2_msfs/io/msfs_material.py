# glTF-Blender-IO-MSFS
# Copyright (C) 2021-2022 The glTF-Blender-IO-MSFS authors

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
import bpy

from ..com import msfs_material_props as MSFSMaterialExtensions

from io_scene_gltf2.blender.imp.gltf2_blender_image import BlenderImage
from io_scene_gltf2.blender.exp.gltf2_blender_gather_texture_info import (
    gather_texture_info,
    gather_material_normal_texture_info_class,
    gather_material_occlusion_texture_info_class,
)


class MSFSMaterial:
    bl_options = {"UNDO"}

    def __new__(cls, *args, **kwargs):
        raise RuntimeError("%s should not be instantiated" % cls)

    @staticmethod
    def create_image(index, import_settings):
        pytexture = import_settings.data.textures[index]
        BlenderImage.create(import_settings, pytexture.source)
        pyimg = import_settings.data.images[pytexture.source]

        # Find image created
        if pyimg.name in bpy.data.images:
            return bpy.data.images[pyimg.name]
        elif os.path.basename(pyimg.uri) in bpy.data.images:
            return bpy.data.images[pyimg.uri]
        elif "Image_%d" % index in bpy.data.images:
            return bpy.data.images["Image_%d" % index]

    @staticmethod
    def export_image(
        blender_material, blender_image, type, export_settings, normal_scale=None
    ):
        nodes = blender_material.node_tree.nodes
        links = blender_material.node_tree.links

        # Create a fake texture node temporarily (unfortunately this is the only solid way of doing this)
        texture_node = nodes.new("ShaderNodeTexImage")
        texture_node.image = blender_image

        # Create shader to plug texture into
        shader_node = nodes.new("ShaderNodeBsdfPrincipled")

        # Gather texture info
        if type == "DEFAULT":
            link = links.new(shader_node.inputs["Base Color"], texture_node.outputs[0])

            texture_info = gather_texture_info(
                shader_node.inputs["Base Color"],
                (shader_node.inputs["Base Color"],),
                export_settings,
            )
        elif type == "NORMAL":
            normal_node = nodes.new("ShaderNodeNormalMap")
            if normal_scale:
                normal_node.inputs["Strength"].default_value = normal_scale
            link = links.new(normal_node.inputs["Color"], texture_node.outputs[0])
            normal_blend_link = links.new(
                shader_node.inputs["Normal"], normal_node.outputs[0]
            )

            texture_info = gather_material_normal_texture_info_class(
                shader_node.inputs["Normal"],
                (shader_node.inputs["Normal"],),
                export_settings,
            )

            links.remove(normal_blend_link)
        elif type == "OCCLUSION":
            # TODO: handle this - may not be needed
            texture_info = gather_material_occlusion_texture_info_class(
                shader_node.inputs[0], (shader_node.inputs[0],), export_settings
            )

        # Delete temp nodes
        links.remove(link)
        nodes.remove(shader_node)
        nodes.remove(texture_node)
        if type == "NORMAL":
            nodes.remove(normal_node)

        return texture_info.to_dict()

    @staticmethod
    def create(gltf2_material, blender_material, import_settings):
        extensions = [
            MSFSMaterialExtensions.AsoboMaterialCommon,
            MSFSMaterialExtensions.AsoboMaterialGeometryDecal,
            MSFSMaterialExtensions.AsoboMaterialGhostEffect,
            MSFSMaterialExtensions.AsoboMaterialDrawOrder,
            MSFSMaterialExtensions.AsoboDayNightCycle,
            MSFSMaterialExtensions.AsoboDisableMotionBlur,
            MSFSMaterialExtensions.AsoboPearlescent,
            MSFSMaterialExtensions.AsoboAlphaModeDither,
            MSFSMaterialExtensions.AsoboMaterialInvisible,
            MSFSMaterialExtensions.AsoboMaterialEnvironmentOccluder,
            MSFSMaterialExtensions.AsoboMaterialUVOptions,
            MSFSMaterialExtensions.AsoboMaterialShadowOptions,
            MSFSMaterialExtensions.AsoboMaterialResponsiveAAOptions,
            MSFSMaterialExtensions.AsoboMaterialDetail,
            MSFSMaterialExtensions.AsoboMaterialFakeTerrain,
            MSFSMaterialExtensions.AsoboMaterialFresnelFade,
            MSFSMaterialExtensions.AsoboSSS,
            MSFSMaterialExtensions.AsoboAnisotropic,
            MSFSMaterialExtensions.AsoboWindshield,
            MSFSMaterialExtensions.AsoboClearCoat,
            MSFSMaterialExtensions.AsoboParallaxWindow,
            MSFSMaterialExtensions.AsoboGlass,
            MSFSMaterialExtensions.AsoboTags,
            MSFSMaterialExtensions.AsoboMaterialCode,
        ]

        for extension in extensions:
            extension.from_dict(blender_material, gltf2_material, import_settings)

    @staticmethod
    def export(gltf2_material, blender_material, export_settings):
        extensions = [
            MSFSMaterialExtensions.AsoboMaterialCommon,
            MSFSMaterialExtensions.AsoboMaterialGeometryDecal,
            MSFSMaterialExtensions.AsoboMaterialGhostEffect,
            MSFSMaterialExtensions.AsoboMaterialDrawOrder,
            MSFSMaterialExtensions.AsoboDayNightCycle,
            MSFSMaterialExtensions.AsoboDisableMotionBlur,
            MSFSMaterialExtensions.AsoboPearlescent,
            MSFSMaterialExtensions.AsoboAlphaModeDither,
            MSFSMaterialExtensions.AsoboMaterialInvisible,
            MSFSMaterialExtensions.AsoboMaterialEnvironmentOccluder,
            MSFSMaterialExtensions.AsoboMaterialUVOptions,
            MSFSMaterialExtensions.AsoboMaterialShadowOptions,
            MSFSMaterialExtensions.AsoboMaterialResponsiveAAOptions,
            MSFSMaterialExtensions.AsoboMaterialDetail,
            MSFSMaterialExtensions.AsoboMaterialFakeTerrain,
            MSFSMaterialExtensions.AsoboMaterialFresnelFade,
            MSFSMaterialExtensions.AsoboSSS,
            MSFSMaterialExtensions.AsoboAnisotropic,
            MSFSMaterialExtensions.AsoboWindshield,
            MSFSMaterialExtensions.AsoboClearCoat,
            MSFSMaterialExtensions.AsoboParallaxWindow,
            MSFSMaterialExtensions.AsoboGlass,
            MSFSMaterialExtensions.AsoboTags,
            MSFSMaterialExtensions.AsoboMaterialCode,
        ]

        for extension in extensions:
            extension.to_extension(blender_material, gltf2_material, export_settings)
