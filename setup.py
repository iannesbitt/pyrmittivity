import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyrmittivity",
    version="0.1.0",
    author="Ian Nesbitt",
    author_email="ian.nesbitt@gmail.com",
    license='GPLv3',
    description="Solve for variables in Maxwell's Equations describing permittivity",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/iannesbitt/pyrmittivity/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Physics",
        "Intended Audience :: Science/Research",
        "Natural Language :: English",
        "Development Status :: 4 - Beta",
    ],
)