import pybind11
from distutils.core import setup, Extension

ext_modules = [
    Extension(
        '_DES', # имя библиотеки собранной pybind11
        ['sources/DES.cpp'], # Тестовый файлик который компилируем
        include_dirs=[pybind11.get_include()],  # не забываем добавить инклюды pybind11
        language='c++', # Указываем язык
    ),
]

setup(
    name='_DES', # имя библиотеки собранной pybind11
    description='pybind11 extension',
    ext_modules=ext_modules,
    requires=['pybind11'],  # Указываем зависимость от pybind11
    package_dir = {'': 'lib'}
)