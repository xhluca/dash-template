import os
import shutil

template_dir = os.path.join(os.getcwd(), 'cookiecutter_templates')

shutil.rmtree(template_dir)