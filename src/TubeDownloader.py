import errno
from operator import attrgetter
import os
from pytube import YouTube
import re
import tkinter as tk
from tkinter import filedialog
from tkinter import PhotoImage
from tkinter import Tk
from tkinter import ttk
from tkinter import constants as cs
from tkinter import messagebox
import unicodedata
import urllib.request


class TubeDownloader():
    '''
    Application to store locally web videos.
    '''

    def __init__(self, root):
        '''
        Constructor
        '''
        self.root = root

        self.root.title('TubeDownloader')
        self.root.iconphoto(True, PhotoImage(file=r'src/img/icon.png'))
        self.root.resizable(0, 0)

        self._create_window(self.root)

    def _create_window(self, root):
        '''
        Create the interfaces object
        '''
        # Buttons
        btn1 = ttk.Button(root, text='\nDescargar\n', command=self._download)
        btn1.grid(row=0, column=3, columnspan=2, rowspan=4, padx=5, pady=15)

        # File selector
        ttk.Label(root, text='Fichero rutas:', justify=cs.RIGHT).grid(
            row=0, column=0, sticky=cs.E, padx=5, pady=5)
        btn2 = ttk.Button(root, text='...', command=self._select_file)
        btn2.grid(row=0, column=2)
        self.tb_fichero = ttk.Entry(root, justify=cs.LEFT, width=50)
        self.tb_fichero.grid(row=0, column=1, padx=5, pady=5)

        # Url selector
        ttk.Label(root, text='URL vídeo:', justify=cs.RIGHT).grid(
            row=1, column=0, sticky=cs.E, padx=5, pady=5)
        self.tb_url = ttk.Entry(root, justify=cs.LEFT, width=50)
        self.tb_url.grid(row=1, column=1, padx=5, pady=5)

        # Target folder
        ttk.Label(root, text='Carpeta destino:', justify=cs.RIGHT).grid(
            row=3, column=0, sticky=cs.E, padx=5, pady=5)
        btn3 = ttk.Button(root, text='...', command=self._select_folder)
        btn3.grid(row=3, column=2)
        self.tb_folder = ttk.Entry(root, justify=cs.LEFT, width=50)
        self.tb_folder.grid(row=3, column=1, padx=5, pady=5)
        self.tb_folder.insert(0, 'C:\\Musica')

        self.progress = ttk.Progressbar(root, orient=cs.HORIZONTAL,
                                        length=600, mode='determinate')
        self.progress.grid(row=4, column=0, columnspan=4, padx=5, pady=5)

        self.controls = [btn1, btn2, btn3,
                         self.tb_fichero, self.tb_folder, self.tb_url]

    def _download(self):
        try:
            self.enable(False)

            fichero = self.tb_fichero.get()
            url = self.tb_url.get()
            target = self.tb_folder.get()

            if target == '':
                messagebox.showinfo(
                    message="Debe seleccionar una carpeta de destino ", title="Information")
            elif os.path.exists(target) == False:
                self.create_folder(target)

            if fichero == ''and url == '':
                messagebox.showinfo(
                    message="Debe seleccionar un fichero para descargar o introducir una dirección Url", title="Information")
            else:
                if fichero != '':
                    if os.path.exists(fichero):
                        self.download_csv(fichero, target)
                    else:
                        messagebox.showinfo(
                            message="Debe seleccionar un fichero válido", title="Information")

                if url != '' and self.checkUrl(url):
                    self.download_url(url, target)
        finally:
            self.enable(True)

    def _select_file(self):
        file_path = filedialog.askopenfilename(
            initialdir='/', title="Select photo",
            filetypes=(("csv files", "*.csv"), ("all files", "*.*")))

        if file_path != '':
            self.tb_fichero.delete(0, cs.END)
            self.tb_fichero.insert(0, file_path)

    def _select_folder(self):
        file_path = filedialog.askdirectory(
            initialdir='/', title="Select target ")

        if file_path != '':
            self.tb_fichero.delete(0, cs.END)
            self.tb_fichero.insert(0, file_path)

    def _on_closing(self):
        self.root.destroy()

    def download_csv(self, csv, target):
        list_url = list()
        with open(csv, 'r') as the_file:
            for line in the_file:
                list_url.append(line)

        total = len(list_url)
        step = 100/total
        acum = 0
        for element in list_url:
            self.download_url(element, target)
            acum += step
            self._update_progress(int(acum))

    def download_url(self, url, target):
        if self.checkUrl(url):
            yt = YouTube(url)
            lstst = yt.streams.filter(only_audio=True).fmt_streams
            best = max(lstst, key=attrgetter('bitrate'))
            best.download(target, filename=self.valid_filename(
                best.default_filename))

    def valid_filename(self, value, allow_unicode=False):
        '''
        Convert to ASCII if 'allow_unicode' is False. Convert spaces to hyphens.
        Remove characters that aren't alphanumerics, underscores, or hyphens.
        Convert to lowercase. Also strip leading and trailing whitespace.
        '''
        value = str(value)
        value = unicodedata.normalize('NFKD', value).encode(
            'ascii', 'ignore').decode('ascii')
        value = re.sub(r'[^\w\s-]', '', value).strip().lower()
        return re.sub(r'[-\s]+', '-', value)

    def checkUrl(self, url):
        c = urllib.request.urlopen(url)
        if c.status == 200:
            result = True
        return result

    def create_folder(self, path: str):
        '''
        Create folder.

        Create folder recived, if obtains a relative path, try to create 
        it in the current directory if not exists, if the folder already
        exists do nothing.

        Parameters
            path,   path of the objetive folder
        '''

        try:
            os.makedirs(path)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise

    def _update_progress(self, step):
        self.progress['value'] = step
        self.root.update()

    def enable(self, option):
        for element in self.controls:
            if option:
                element.config(state='normal')
            else:
                element.config(state="disabled")


if __name__ == "__main__":
    root = Tk()
    TubeDownloader(root)
    root.mainloop()
