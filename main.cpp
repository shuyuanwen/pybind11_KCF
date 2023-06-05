#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "kcf/kcftracker.hpp"
#include <iostream>
#include <vector>
#include <opencv2/opencv.hpp>
#include <pybind11/numpy.h>
#include <pybind11/stl.h>
#include "mat_warper.h"
#include "ndarray_converter.h"

namespace py = pybind11;
using namespace cv;
using namespace std;

PYBIND11_MODULE(kcf_demo, m) {

    NDArrayConverter::init_numpy();

    m.doc() = "Simple Kcf tracker demo";

    py::class_<KCFTracker>(m, "KCFTracker")
        .def(py::init<bool, bool,bool, bool>())
        .def_readwrite("interp_factor", &KCFTracker::interp_factor)
        .def_readwrite("template_size", &KCFTracker::template_size)
        .def_readwrite("sigma", &KCFTracker::sigma)
        .def_readwrite("lambda", &KCFTracker::lambda)
        .def_readwrite("output_sigma_factor", &KCFTracker::output_sigma_factor)
        .def_readwrite("scale_step", &KCFTracker::scale_step)
        .def_readwrite("scale_weight", &KCFTracker::scale_weight)
        .def_readwrite("padding", &KCFTracker::padding)
        .def_readwrite("cell_size", &KCFTracker::cell_size)
        .def_readwrite("cell_sizeQ", &KCFTracker::cell_sizeQ)
        .def("trackerInit", &KCFTracker::trackerInit, py::arg("rect"), py::arg("img"))
        .def("trackerUpdate", &KCFTracker::trackerUpdate, py::arg("img"));
}