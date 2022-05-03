import setuptools

with open("README.md", "r", encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name="juce-rsa-python",
    version="0.0.4",
    author="xt1800i",
    author_email="xt1800i@example.com",
    description="A juce RSA algorithm implementation without compiling C++ source code",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/xianyuntang/juce-rsa-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        "Operating System :: OS Independent",
    ],
)
