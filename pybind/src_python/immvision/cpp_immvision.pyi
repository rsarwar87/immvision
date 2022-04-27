import typing
import numpy as np
from .cv_types import *

# <autogen:ColorAdjustmentsValues.piy> // Autogenerated code below! Do not edit!

class ColorAdjustmentsValues:
    "Color adjustments (esp. useful for a float matrix)"
    
    # Pre-multiply values by a Factor before displaying
    factor: float = 1.
    # Add a delta to the values before displaying
    delta: float = 0.

# </autogen:ColorAdjustmentsValues.piy> // Autogenerated code end



# <autogen:ImageNavigatorParams.piy> // Autogenerated code below! Do not edit!

class ImageNavigatorParams:
    "Set of display parameters and options for an ImageNavigator"
    

    #
    #  ImageNavigatorParams store the parameters for an ImageNavigator
    #  (as well as user selected watched pixels, selected channel, etc.)
    #  Its default constructor will give them reasonable choices, which you can adapt to your needs.
    #  Its values will be updated when the user pans or zooms the image, adds watched pixels, etc.
    #

    #
    #  Display size and title
    #
    # Size of the navigator (can be different from the image size)
    image_display_size: Size = (0, 0)
    # Title displayed in the border
    legend: str = "Image Navigator"

    #
    #  Zoom and Pan (represented by an affine transform matrix, of size 3x3)
    #
    # ZoomPanMatrix can be created using MakeZoomPanMatrix to create a view centered around a given point
    zoom_pan_matrix: Matx33d = np.eye(3)
    # If displaying several navigators, those with the same ZoomKey will zoom and pan together
    zoom_key: str = ""

    #
    #  Color adjustments
    #
    # Color adjustments for float matrixes
    color_adjustments: ColorAdjustmentsValues = ColorAdjustmentsValues()
    # If displaying several navigators, those with the same ColorAdjustmentsKey will adjust together
    color_adjustments_key: str = ""

    #
    #  Zoom and pan with the mouse
    #
    # 
    pan_with_mouse: bool = True
    # 
    zoom_with_mouse_wheel: bool = True
    # Color Order: RGB or RGBA versus BGR or BGRA (Note: by default OpenCV uses BGR and BGRA)
    is_color_order_bgr: bool = True

    #
    #  Image display options
    #
    # if SelectedChannel >= 0 then only this channel is displayed
    selected_channel: int = -1
    # show a checkerboard behind transparent portions of 4 channels RGBA images
    show_alpha_channel_checkerboard: bool = True
    # Grid displayed when the zoom is high
    show_grid: bool = True
    # Pixel values show when the zoom is high
    draw_values_on_zoomed_pixels: bool = True

    #
    #  Navigator display options
    #
    # Show matrix type and size
    show_image_info: bool = True
    # Show pixel values
    show_pixel_info: bool = True
    # Show buttons that enable to zoom in/out (the mouse wheel also zoom)
    show_zoom_buttons: bool = True
    # Show a rectangular border with the legend
    show_legend_border: bool = True
    # Open the options panel
    show_options: bool = False
    # If set to true, then the option panel will be displayed in a transient tooltip window
    show_options_in_tooltip: bool = False

    #
    #  Watched Pixels
    #
    # List of Watched Pixel coordinates
    watched_pixels: list[Point] = list[Point]()
    # Shall the watched pixels be drawn on the image
    highlight_watched_pixels: bool = True

# </autogen:ImageNavigatorParams.piy> // Autogenerated code end

