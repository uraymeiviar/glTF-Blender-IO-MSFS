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

from ..msfs_material_function import MSFS_Material, MSFS_ShaderNodes


class MSFS_Environment_Occluder(MSFS_Material):
    def __init__(self, material, buildTree=False):
        super().__init__(material, buildTree)

    def customShaderTree(self):
        self.principledBSDF = self.getNode(MSFS_ShaderNodes.principledBSDF.value)
        self.principledBSDF.inputs[21].default_value = 0
