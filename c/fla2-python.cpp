#include <pybind11/pybind11.h>

#include "fla2.h"

namespace py = pybind11;

py::bytes compress_wrapper(py::bytes src) {
    py::buffer_info info(py::buffer(src).request());
    const uint8_t *src_data = reinterpret_cast<const uint8_t *>(info.ptr);
    size_t src_len = static_cast<size_t>(info.size);

    uint8_t *dst;
    size_t dst_len;
    compress(src_data, src_len, &dst, &dst_len);
    return std::string((const char *)dst, dst_len);
}

PYBIND11_MODULE(fla2, m) {
    m.def("compress", &compress_wrapper, "Compress data into FLA2 format");
}

