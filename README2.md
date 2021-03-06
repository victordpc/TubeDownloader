# TubeDownloader
[![Build Status](https://travis-ci.org/victordpc/TubeDownloader.svg?branch=master)](https://travis-ci.org/victordpc/TubeDownloader)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![PyPI version](https://badge.fury.io/py/TubeDownloader.svg)](https://badge.fury.io/py/TubeDownloader)

TubeDownloader is a Python application to download audio tracks of youtube video.

## Install
* ### Clone the repo
```bash
$ cd TubeDownloader
$ pip install -r requeriments.txt
```

* ### Pip
```python
pip install TubeDownloader
```

* ### Executables
[Download Windows](https://github.com/victordpc/TubeDownloader/releases/download/v0.2.0/TubeDownloader.exe)

## Run
```bash
$ python script.py
```

```python
from TubeDownloader import TubeDownloader as tb
app =tb.TubeDownloader()
```

## Use
* **Input** field `Fichero rutas` expects a file path with one URL per row:
```
https://www.youtube.com/watch?v=hqbS7O9qIXE
https://www.youtube.com/watch?v=nowQC7YFBtw
https://www.youtube.com/watch?v=z9Uz1icjwrM
https://www.youtube.com/watch?v=XKcGB3HXrIg
```
* **Input** field `URL video` expects a single URL video.
* **Output** field `Carpeta destino` expects a folder path to store the audio.

To let the magic ride, must fill at least one of the input fields, select a output folder an click the `Descargar` button.

