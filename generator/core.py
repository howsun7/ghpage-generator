import os
from jinja2 import Template

class Generator:
    output_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..'))
    templates_path = os.path.abspath(
        os.path.join(os.path.dirname( __file__ ), '..', 'templates'))
    output_filename = 'index.html'

    def __init__(self, config):
        self.config = config
        self.input_path = os.path.join(
            self.templates_path, config.template_filename)
        self.template_string = None

    def generate(self):
        self.get_template_string()

        template = Template(self.template_string)
        content = template.render(**self.config.configs)
        
        output_path = os.path.join(self.output_path, self.output_filename)

        with open(output_path, 'w') as file:
            try: 
                file.write(content)
            except Exception as e:
                raise e

    def get_template_string(self):
        with open(self.input_path, 'r') as file:
            try:
                self.template_string = file.read()
            except Exception as e:
                raise e
        
    



    # def read_file(self):
    #     filepath = 
    #     with




