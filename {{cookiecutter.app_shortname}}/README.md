# {{cookiecutter.app_name}}

## Instructions

To get started, first clone this repo:

```
git clone https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.app_shortname}}.git
cd {{cookiecutter.app_shortname}}
```
### Usual setup

Create and activate a virtual environment (make sure your `python3` is 3.6+):
```
python3 -m venv venv
source venv/bin/activate
```

Install all the requirements:

```
pip3 install -r requirements.txt
```

You can now run the app:
```
python3 app.py
```

and visit http://127.0.0.1:8050/.

### Alternative setups

#### Windows
```
python3 -m venv venv
venv\Scripts\activate.bat
pip3 install -r requirements.txt
python3 app.py
```

#### Conda
```
conda create -n {{cookiecutter.app_shortname}} python={{cookiecutter.python_version}}
conda activate {{cookiecutter.app_shortname}}
pip3 install -r requirements.txt
python3 app.py
```

#### Pipenv
```
pipenv --python {{cookiecutter.python_version}}
pipenv install -r requirements.txt
```




## Contact

Interested in building or deploying apps like this? [Reach out](https://plotly.com/contact-us/) or [get a demo](https://plotly.com/get-demo).