from setuptools import Extension, setup
from pybind11.setup_helpers import Pybind11Extension

def get_version_and_cmdclass(pkg_path):
    """Load version.py module without importing the whole package.

    Template code from miniver
    """
    import os
    from importlib.util import module_from_spec, spec_from_file_location

    spec = spec_from_file_location("version", os.path.join(pkg_path, "_version.py"))
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.__version__, module.get_cmdclass(pkg_path)


version, cmdclass = get_version_and_cmdclass(r"python/libgarib")


setup(
    name="libgarib",
    version=version,
    cmdclass=cmdclass,
    install_requires = [
        "capstone",
        "construct",
        "jmespath",
        "kaitaistruct",
        "lxml",
        "numpy",
        "pillow",
        "pygltflib",
        "unicorn",
        "pyyaml",
    ],
    package_data={
        "libgarib": ["parsers/*.rng"]
    },
    ext_modules=[
        Pybind11Extension(
            name="cppcore.fla2",
            sources=["./c/fla2.c", "./c/fla2-python.cpp"],
            include_dirs=["./c"]
        ),
    ]


)
