from setuptools import Extension, setup, find_namespace_packages
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

packages = find_namespace_packages(
        where='./python/',
        include=['libgarib*'],
)

if "libgarib.parsers" not in packages:
    raise Exception("Binary format parsing modules are missing from source "
                    "distribution, cannot build package. Regenerate parser"
                    "modules with 'make parsers' and then try again")

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
    packages=packages + ["libgarib.cppcore"],
    package_dir={
        "libgarib":"python/libgarib",
        "libgarib.cppcore":"c/"
    },
    package_data={
        "libgarib": ["parsers/*.rng"],
        "libgarib.cppcore": ["*"]
    },
    ext_modules=[
        Pybind11Extension(
            name="libgarib.cppcore.fla2",
            sources=["./c/fla2.c", "./c/fla2-python.cpp"],
            include_dirs=["./c"]
        ),
    ]


)
