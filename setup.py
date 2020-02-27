import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="restutil-tjdaley",  # Replace with your own username
    version="0.0.3",
    author="Thomas J. Daley",
    author_email="tdaley@daleyfound.org",
    description="API for accessing my restutil service",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tjdaley/restutil_api",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Intended Audience :: Legal Industry",
        "Natural Language :: English",
    ],
    python_requires='>=3.6',
)
