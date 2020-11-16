# Klasa do wczytywania pliku

class FileLoader:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.directory = "" # TODO: set default directory