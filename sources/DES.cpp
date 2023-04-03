#include <cstdlib>
#include <algorithm>
#include <vector>
#include "DES.hpp"
#include "SHA256.cpp"

namespace py = pybind11;

PYBIND11_MODULE(_DES, m) {

    py::class_<DES>(m, "DES")
    .def(py::init()) // Указываем конструктор. Которого у структуры нет, но он нужен python.
    .def_readwrite("m_code", &DES::m_code)
    .def_readwrite("code", &DES::code)
    .def("encode", &DES::encode)
	.def("decode", &DES::decode); // переменные структуры
	m.def("sha256",&sha256);
}
