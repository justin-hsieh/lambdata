
import setuptools

REQUIRED = [
  "pandas",
  "numpy"
]
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lambdatahsieh",
    version="0.1.1",
    author="jhsieh",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/justin-hsieh/lambdatahsieh",
    packages=setuptools.find_packages(),
    install_requires=REQUIRED,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
