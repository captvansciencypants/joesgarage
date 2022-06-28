
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib as mpl

CMAP = 'viridis'
font_size = 12
mpl.rcParams['xtick.labelsize'] = font_size
mpl.rcParams['ytick.labelsize'] = font_size

def colorbar(ax, im):
    """
    Display a good colorbar
    """
    divider = make_axes_locatable(ax)
    cax = divider.append_axes('right', size='5%', pad=0.05)
    cbar = plt.colorbar(im, cax=cax)

def show_slice(disp_map, disp_str, slice_ind, clim=None):
    """
    Plot the three orthogonal slices
    """
    fig = plt.figure()
    ax = fig.add_subplot(131)
    im = ax.imshow(disp_map[slice_ind[0],:,:], clim=clim, cmap=CMAP, origin='lower')
    colorbar(ax, im)
    ax.set_xlabel('z')
    ax.set_ylabel('x')
    # ax.set_title(f'[{slice_ind[0]},:,:]')
    ax = fig.add_subplot(132)
    im = ax.imshow(disp_map[:,slice_ind[1],:], clim=clim, cmap=CMAP, origin='lower') 
    colorbar(ax, im)
    ax.set_xlabel('z')
    ax.set_ylabel('y')
    # ax.set_title(f'[:,{slice_ind[1]},:]')
    ax = fig.add_subplot(133)
    im = ax.imshow(disp_map[:,:,slice_ind[2]], clim=clim, cmap=CMAP, origin='lower')
    colorbar(ax, im)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    # ax.set_title(f'[:,:,{slice_ind[2]}]')

    plt.suptitle(disp_str)
    plt.tight_layout()
    plt.show(block=False)
