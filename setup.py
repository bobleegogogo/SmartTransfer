from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="smart_transfer",
    version="0.1.0",

    description="Smart Transfer: Cross-regional building damage mapping",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="zoulevi",

    python_requires=">=3.10",

    packages=find_packages(),

    install_requires=[
        "torch",
        "torchvision",
        "numpy",
        "scipy",
        "pandas",
        "scikit-learn",
        "tqdm",
        "matplotlib",
        "Pillow",
        "geopandas",
        "pyproj",
        "shapely",
        "rasterio",
        "segmentation-models-pytorch",    
    ],

    include_package_data=True,
)