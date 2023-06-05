from setuptools import Extension
from setuptools import setup


__version__ = '0.0.1'

ext_module = Extension(
    name='kcf_demo',
    sources=
    [
        r'main.cpp',
        r'mat_warper.cpp',
        r'ndarray_converter.cpp',
        r'./kcf/fhog.cpp',
        r'./kcf/kcftracker.cpp'
    ],
    include_dirs=
    [
        r'D:/APP/miniconda3/envs/aar/include',
        r'D:/APP/miniconda3/Lib/site-packages/numpy/core/include',
        r'D:/APP/OpenCV4.5.5/opencv/build/include',
        r'E:/pybind11-master/include'
    ],
    library_dirs=
    [
        r'D:/APP/miniconda3/Lib/site-packages/numpy/core/lib',
        r'D:/APP/OpenCV4.5.5/opencv/build/x64/vc15/lib'
    ],
    libraries=
    [
        'opencv_world455',
        'npymath'
    ],
    language='c++'
)

setup(
    name='kcf_demo',
    version=__version__,
    author_email='xxxx@qq.com',
    description='A simaple demo',
    ext_modules=[ext_module],
    install_requires=['numpy']
)

