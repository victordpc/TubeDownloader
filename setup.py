import setuptools

with open("README2.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='TubeDownloader',
    version='0.1.3',
    author='victordpc',
    author_email='victordpc@gmail.com',
    packages=setuptools.find_packages(),
    license='LGPL v3',
    url='https://github.com/victordpc/TubeDownloader',
    description='Download audio track of youtube video',
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=["youtube", "download", "audio"],
    classifiers=['Programming Language :: Python',
                 'Programming Language :: Python :: 3.8'],
    include_package_data=True,
    zip_safe=True,
    python_requires=">=3.6",
)
