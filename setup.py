import setuptools

with open("README2.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='TubeDownloader',
    version='0.1.1',
    author='victordpc',
    author_email='victordpc@gmail.com',
    license='LGPL v3',
    description='Download audio track of youtube video',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/victordpc/TubeDownloader',
    keywords='download youtube audio',
    packages=setuptools.find_packages(),
    classifiers=['Programming Language :: Python',
                 'Programming Language :: Python :: 3.8'],
)
