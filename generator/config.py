import os
import yaml


class Config:
    config_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..'))
    config_filename = 'config.yml'
    configurations = None

    def __init__(self):
        Config.load_configurations()
        for k, v in self.configurations.items():
            try:
                setattr(self, k, v)
            except Exception as e:
                raise e
    
    @classmethod 
    def load_configurations(cls):
        filepath = os.path.join(cls.config_path, cls.config_filename)
        with open (filepath, 'r') as file:
            try:
                cls.configurations = yaml.safe_load(file)
            except Exception as e:
                raise e
        
    @property
    def configs(self):
        return vars(self)

    def __repr__(self):
        return '{}'.format(self.configs)
