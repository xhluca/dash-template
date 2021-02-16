import os
import shutil

dirname = "{{ cookiecutter.repo_name }}"
template_dir = os.path.join(os.getcwd(), 'templates')

shutil.rmtree(template_dir)