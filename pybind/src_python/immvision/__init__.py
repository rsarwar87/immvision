_DEBUG_GL_TEXTURES = False
from . import _cpp_immvision
from .cv_types import *
__version__ = _cpp_immvision.__version__


# <autogen:init_struct> // Autogenerated code below! Do not edit!


class ColorAdjustmentsValues(_cpp_immvision.ColorAdjustmentsValues):
    """ Color adjustments (esp. useful for a float matrix)

    * factor: float = 1.
            Pre-multiply values by a Factor before displaying
    * delta: float = 0.
            Add a delta to the values before displaying

    """
    
    def __init__(
        self,
        # Pre-multiply values by a Factor before displaying
        factor: float = 1.,
        # Add a delta to the values before displaying
        delta: float = 0.,

    ):
        _cpp_immvision.ColorAdjustmentsValues.__init__(self)
        self.factor = factor
        self.delta = delta



class MouseInformation(_cpp_immvision.MouseInformation):
    """ Contains information about the mouse inside an image

    * mouse_position: Point2d = (-1., -1.)
            Mouse position in the original image/matrix
            This position is given with float coordinates, and will be (-1., -1.) if the mouse is not hovering the image
    * mouse_position_displayed: Point = (-1, -1)
            Mouse position in the displayed portion of the image (the original image can be zoomed,
            and only show a subset if it may be shown).
            This position is given with integer coordinates, and will be (-1, -1) if the mouse is not hovering the image

 Note: you can query ImGui::IsMouseDown(mouse_button) (c++) or imgui.is_mouse_down(mouse_button) (Python)

    """
    
    def __init__(
        self,
        # Mouse position in the original image/matrix
        # This position is given with float coordinates, and will be (-1., -1.) if the mouse is not hovering the image
        mouse_position: Point2d = (-1., -1.),
        # Mouse position in the displayed portion of the image (the original image can be zoomed,
        # and only show a subset if it may be shown).
        # This position is given with integer coordinates, and will be (-1, -1) if the mouse is not hovering the image
        mouse_position_displayed: Point = (-1, -1),

    ):
        _cpp_immvision.MouseInformation.__init__(self)
        self.mouse_position = mouse_position
        self.mouse_position_displayed = mouse_position_displayed



class ImageParams(_cpp_immvision.ImageParams):
    """ Set of display parameters and options for an Image


 ImageParams store the parameters for a displayed image
 (as well as user selected watched pixels, selected channel, etc.)
 Its default constructor will give them reasonable choices, which you can adapt to your needs.
 Its values will be updated when the user pans or zooms the image, adds watched pixels, etc.

 Refresh Images Textures
    * refresh_image: bool = False
            Refresh Image: images textures are cached. Set to True if your image matrix/buffer has changed
            (for example, for live video images)

 Display size and title
    * image_display_size: Size = (0, 0)
            Size of the displayed image (can be different from the matrix size)
            If you specify only the width or height (e.g (300, 0), then the other dimension
            will be calculated automatically, respecting the original image w/h ratio.
    * legend: str = "Image"
            Title displayed in the border

 Zoom and Pan (represented by an affine transform matrix, of size 3x3)
    * zoom_pan_matrix: Matx33d = np.eye(3)
            ZoomPanMatrix can be created using MakeZoomPanMatrix to create a view centered around a given point
    * zoom_key: str = ""
            If displaying several images, those with the same ZoomKey will zoom and pan together

 Color adjustments
    * color_adjustments: ColorAdjustmentsValues = ColorAdjustmentsValues()
            Color adjustments for float matrixes
    * color_adjustments_key: str = ""
            If displaying several images, those with the same ColorAdjustmentsKey will adjust together

 Zoom and pan with the mouse
    * pan_with_mouse: bool = True
    * zoom_with_mouse_wheel: bool = True
    * is_color_order_bgr: bool = True
            Color Order: RGB or RGBA versus BGR or BGRA (Note: by default OpenCV uses BGR and BGRA)

 Image display options
    * selected_channel: int = -1
            if SelectedChannel >= 0 then only this channel is displayed
    * show_alpha_channel_checkerboard: bool = True
            show a checkerboard behind transparent portions of 4 channels RGBA images
    * show_grid: bool = True
            Grid displayed when the zoom is high
    * draw_values_on_zoomed_pixels: bool = True
            Pixel values show when the zoom is high

 Image display options
    * show_image_info: bool = True
            Show matrix type and size
    * show_pixel_info: bool = True
            Show pixel values
    * show_zoom_buttons: bool = True
            Show buttons that enable to zoom in/out (the mouse wheel also zoom)
    * show_legend_border: bool = True
            Show a rectangular border with the legend
    * show_options_panel: bool = False
            Open the options panel
    * show_options_in_tooltip: bool = False
            If set to True, then the option panel will be displayed in a transient tooltip window
    * show_options_button: bool = True
            If set to False, then the Options button will not be displayed

 Watched Pixels
    * watched_pixels: list[Point] = list[Point]()
            List of Watched Pixel coordinates
    * highlight_watched_pixels: bool = True
            Shall the watched pixels be drawn on the image
    * mouse_info: MouseInformation = MouseInformation()
            Mouse position information. These values are filled after displaying an image

    """
    
    def __init__(
        self,
        # Refresh Image: images textures are cached. Set to true if your image matrix/buffer has changed
        # (for example, for live video images)
        refresh_image: bool = False,
        # Size of the displayed image (can be different from the matrix size)
        # If you specify only the width or height (e.g (300, 0), then the other dimension
        # will be calculated automatically, respecting the original image w/h ratio.
        image_display_size: Size = (0, 0),
        # Title displayed in the border
        legend: str = "Image",
        # ZoomPanMatrix can be created using MakeZoomPanMatrix to create a view centered around a given point
        zoom_pan_matrix: Matx33d = np.eye(3),
        # If displaying several images, those with the same ZoomKey will zoom and pan together
        zoom_key: str = "",
        # Color adjustments for float matrixes
        color_adjustments: ColorAdjustmentsValues = ColorAdjustmentsValues(),
        # If displaying several images, those with the same ColorAdjustmentsKey will adjust together
        color_adjustments_key: str = "",
        # 
        pan_with_mouse: bool = True,
        # 
        zoom_with_mouse_wheel: bool = True,
        # Color Order: RGB or RGBA versus BGR or BGRA (Note: by default OpenCV uses BGR and BGRA)
        is_color_order_bgr: bool = True,
        # if SelectedChannel >= 0 then only this channel is displayed
        selected_channel: int = -1,
        # show a checkerboard behind transparent portions of 4 channels RGBA images
        show_alpha_channel_checkerboard: bool = True,
        # Grid displayed when the zoom is high
        show_grid: bool = True,
        # Pixel values show when the zoom is high
        draw_values_on_zoomed_pixels: bool = True,
        # Show matrix type and size
        show_image_info: bool = True,
        # Show pixel values
        show_pixel_info: bool = True,
        # Show buttons that enable to zoom in/out (the mouse wheel also zoom)
        show_zoom_buttons: bool = True,
        # Show a rectangular border with the legend
        show_legend_border: bool = True,
        # Open the options panel
        show_options_panel: bool = False,
        # If set to true, then the option panel will be displayed in a transient tooltip window
        show_options_in_tooltip: bool = False,
        # If set to false, then the Options button will not be displayed
        show_options_button: bool = True,
        # List of Watched Pixel coordinates
        watched_pixels: list[Point] = list[Point](),
        # Shall the watched pixels be drawn on the image
        highlight_watched_pixels: bool = True,
        # Mouse position information. These values are filled after displaying an image
        mouse_info: MouseInformation = MouseInformation(),

    ):
        _cpp_immvision.ImageParams.__init__(self)
        self.refresh_image = refresh_image
        self.image_display_size = image_display_size
        self.legend = legend
        self.zoom_pan_matrix = zoom_pan_matrix
        self.zoom_key = zoom_key
        self.color_adjustments = color_adjustments
        self.color_adjustments_key = color_adjustments_key
        self.pan_with_mouse = pan_with_mouse
        self.zoom_with_mouse_wheel = zoom_with_mouse_wheel
        self.is_color_order_bgr = is_color_order_bgr
        self.selected_channel = selected_channel
        self.show_alpha_channel_checkerboard = show_alpha_channel_checkerboard
        self.show_grid = show_grid
        self.draw_values_on_zoomed_pixels = draw_values_on_zoomed_pixels
        self.show_image_info = show_image_info
        self.show_pixel_info = show_pixel_info
        self.show_zoom_buttons = show_zoom_buttons
        self.show_legend_border = show_legend_border
        self.show_options_panel = show_options_panel
        self.show_options_in_tooltip = show_options_in_tooltip
        self.show_options_button = show_options_button
        self.watched_pixels = watched_pixels
        self.highlight_watched_pixels = highlight_watched_pixels
        self.mouse_info = mouse_info



# </autogen:init_struct> // Autogenerated code end


# <autogen:init_function> // Autogenerated code below! Do not edit!

def factor_image_params_display_only():
    """ Create ImageParams that display the image only, with no decoration, and no user interaction
    """
    r = _cpp_immvision.factor_image_params_display_only()
    return r


def make_zoom_pan_matrix(
    zoom_center:  Point2d,
    zoom_ratio: float,
    displayed_image_size:  Size):
    """ Create a zoom/pan matrix centered around a given point of interest
    """
    r = _cpp_immvision.make_zoom_pan_matrix(zoom_center, zoom_ratio, displayed_image_size)
    return r


def image(
    image_matrix:  np.ndarray,
    params: ImageParams):
    """ Display an image, with full user control: zoom, pan, watch pixels, etc.

     Notes:

     - the ImageParams may be modified by this function: you can extract from them
       the mouse position, watched pixels, etc. Thus, their scope should extend beyond the call to Image !
       If you cannot zoom/pan in a displayed image, extend the scope of the ImageParams!

     - This function requires that both imgui and OpenGL were initialized.
       (for example, use `imgui_runner.run`for Python,  or `HelloImGui::Run` for C++)
    """

    _cpp_immvision.transfer_imgui_context_python_to_cpp()

    r = _cpp_immvision.image(image_matrix, params)
    return r


def image_display(
    mat:  np.ndarray,
    image_display_size:  Size  = (0, 0),
    refresh_image: bool  = False,
    show_options_button: bool  = True,
    is_bgr_or_bgra: bool  = True):
    """ Only, display the image, with no decoration, and no user interaction

     Parameters:
          - mat:
              The image to display
          - imageDisplaySize:
              Size of the displayed image (can be different from the mat size)
              If you specify only the width or height (e.g (300, 0), then the other dimension
              will be calculated automatically, respecting the original image w/h ratio.
          - refreshImage: images textures are cached. Set to True if your image matrix/buffer has changed
              (for example, for live video images)
          - showOptionsButton: If True, show an option button that opens the option panel
          - isBgrOrBgra: set to True if the color order of the image is BGR or BGRA (as in OpenCV, by default)

     Returns:
          The mouse position in `mat` original image coordinates, as float values.
          (i.e. it does not matter if imageDisplaySize is different from mat.size())
          It will return (-1., -1.) if the mouse is not hovering the image.

          Note: use ImGui::IsMouseDown(mouse_button) (C++) or imgui.is_mouse_down(mouse_button) (Python)
                to query more information about the mouse.

     Note: this function requires that both imgui and OpenGL were initialized.
           (for example, use `imgui_runner.run`for Python,  or `HelloImGui::Run` for C++)

    """

    _cpp_immvision.transfer_imgui_context_python_to_cpp()

    r = _cpp_immvision.image_display(mat, image_display_size, refresh_image, show_options_button, is_bgr_or_bgra)
    return r


def clear_texture_cache():
    """ Clears the internal texture cache of immvision (this is done automatically at exit time)

     Note: this function requires that both imgui and OpenGL were initialized.
           (for example, use `imgui_runner.run`for Python,  or `HelloImGui::Run` for C++)
    """

    _cpp_immvision.transfer_imgui_context_python_to_cpp()

    r = _cpp_immvision.clear_texture_cache()
    return r


def version_info():
    """ Return immvision version info
    """
    r = _cpp_immvision.version_info()
    return r



# </autogen:init_function> // Autogenerated code end


from .figure import figure as figure, figure_display as figure_display

