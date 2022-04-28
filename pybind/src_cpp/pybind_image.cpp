#include "immvision/image.h"
#include "immvision/internal/misc/immvision_to_string.h"
#include "cvnp/cvnp.h"
#include "transfer_imgui_context.h"

#include <pybind11/pybind11.h>
#include <opencv2/core.hpp>


namespace py = pybind11;


void Image(const cv::Mat& image)
{
    transfer_imgui_context();
    cv::Size cv_size(500, 500);
    ImmVision::Image(image, cv_size);
}



void pydef_image(pybind11::module& m)
{
    m.def("Image", Image);

    using namespace ImmVision;


    auto pyClassImageParams = py::class_<ImageParams>(m, "ImageParams")
        .def(py::init<>())

        // <autogen:ImageParams.attributes> // Autogenerated code below! Do not edit!

        .def_readwrite("image_display_size", &ImageParams::ImageDisplaySize, "Size of the navigator (can be different from the image size)")
        .def_readwrite("legend", &ImageParams::Legend, "Title displayed in the border")
        .def_readwrite("zoom_pan_matrix", &ImageParams::ZoomPanMatrix, "ZoomPanMatrix can be created using MakeZoomPanMatrix to create a view centered around a given point")
        .def_readwrite("zoom_key", &ImageParams::ZoomKey, "If displaying several navigators, those with the same ZoomKey will zoom and pan together")
        .def_readwrite("color_adjustments", &ImageParams::ColorAdjustments, "Color adjustments for float matrixes")
        .def_readwrite("color_adjustments_key", &ImageParams::ColorAdjustmentsKey, "If displaying several navigators, those with the same ColorAdjustmentsKey will adjust together")
        .def_readwrite("pan_with_mouse", &ImageParams::PanWithMouse, "")
        .def_readwrite("zoom_with_mouse_wheel", &ImageParams::ZoomWithMouseWheel, "")
        .def_readwrite("is_color_order_bgr", &ImageParams::IsColorOrderBGR, "Color Order: RGB or RGBA versus BGR or BGRA (Note: by default OpenCV uses BGR and BGRA)")
        .def_readwrite("selected_channel", &ImageParams::SelectedChannel, "if SelectedChannel >= 0 then only this channel is displayed")
        .def_readwrite("show_alpha_channel_checkerboard", &ImageParams::ShowAlphaChannelCheckerboard, "show a checkerboard behind transparent portions of 4 channels RGBA images")
        .def_readwrite("show_grid", &ImageParams::ShowGrid, "Grid displayed when the zoom is high")
        .def_readwrite("draw_values_on_zoomed_pixels", &ImageParams::DrawValuesOnZoomedPixels, "Pixel values show when the zoom is high")
        .def_readwrite("show_image_info", &ImageParams::ShowImageInfo, "Show matrix type and size")
        .def_readwrite("show_pixel_info", &ImageParams::ShowPixelInfo, "Show pixel values")
        .def_readwrite("show_zoom_buttons", &ImageParams::ShowZoomButtons, "Show buttons that enable to zoom in/out (the mouse wheel also zoom)")
        .def_readwrite("show_legend_border", &ImageParams::ShowLegendBorder, "Show a rectangular border with the legend")
        .def_readwrite("show_options", &ImageParams::ShowOptions, "Open the options panel")
        .def_readwrite("show_options_in_tooltip", &ImageParams::ShowOptionsInTooltip, "If set to true, then the option panel will be displayed in a transient tooltip window")
        .def_readwrite("watched_pixels", &ImageParams::WatchedPixels, "List of Watched Pixel coordinates")
        .def_readwrite("highlight_watched_pixels", &ImageParams::HighlightWatchedPixels, "Shall the watched pixels be drawn on the image")
        
        //</autogen:ImageParams.attributes> // End of autogenerated code.
        .def("__repr__", [](const ImageParams& v){ return ToString(v); });


    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    auto c = py::class_<ColorAdjustmentsValues>(m, "ColorAdjustmentsValues")
        .def(py::init<>())
        // <autogen:ColorAdjustmentsValues.attributes> // Autogenerated code below! Do not edit!

        .def_readwrite("factor", &ColorAdjustmentsValues::Factor, "Pre-multiply values by a Factor before displaying")
        .def_readwrite("delta", &ColorAdjustmentsValues::Delta, "Add a delta to the values before displaying")
        
        //</autogen:ColorAdjustmentsValues.attributes> // End of autogenerated code.
        .def("__repr__", [](const ColorAdjustmentsValues& v){ return ToString(v); });
}




