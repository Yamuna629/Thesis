# -*- coding: utf-8 -*-
"""
Created on Tue May 18 21:57:10 2021

@author: pvrma
"""
import numpy as np
import time
import voxelization

zmax = -0.003

particle_data = voxelization.import_sq_data('sq_pill_dem_data.csv', zmax)
"""
In the above line of code, we are importing the multisphere particles and converting it
into sphere data using the multisphere configuration obtained previously.
"""
normalized_voxel_size = 0.5
bounding_box = [-0.0125,0.0125,-0.0125,0.0125,-0.05,-0.001]
P1 = voxelization.sq_vox(particle_data, bounding_box, normalized_voxel_size, 'pill_sq')#voxelizing the sphere data.
