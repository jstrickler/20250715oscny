import yaml

class IRS990Config:
    def __init__(self):    
        with open('irsform990.yaml') as file_in:
            config_data = yaml.load(file_in, Loader=yaml.BaseLoader)
            self.file_repo = config_data['file-repo']

    @property
    def file_repo(self):
        return self._file_repo

    @file_repo.setter
    def file_repo(self, value):
        self._file_repo = value
    
