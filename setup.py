import setuptools

with open("README2.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='TubeDownloader',
    version='0.2.0',
    author='victordpc',
    author_email='victordpc@gmail.com',
    packages=['TubeDownloader'],
    license='LGPL v3',
    url='https://github.com/victordpc/TubeDownloader',
    description='Download audio track of youtube video',
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=["youtube", "download", "audio"],
    classifiers=['Development Status :: 4 - Beta',
                'Programming Language :: Python :: 3.8',
                'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
                'Topic :: Multimedia :: Sound/Audio'],
    install_requires=['pytube3'],
    include_package_data=True,
)
    # python_requires=">=3.6",
