import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="acore",
    version="0.0.1",
    author="dmytro.malkin",
    author_email="dmytro.malkin@seagate.com",
    description="seagate automation code project",
    long_description=long_description,
    url="https://github.com/fullmetaltac/core_zero.git",
    packages=setuptools.find_packages(),
    install_requires=[
        'hid==1.0.4',
        'hidapi==0.10.0.post1',
        'pysmb==1.2.5',
        'pyserial==3.4',
        'paramiko==2.7.2',
        'requests==2.24.0',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
