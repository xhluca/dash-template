{%- if cookiecutter.format == 'bootstrap' -%}
    {%- include 'cookiecutter_templates/app_bootstrap.py' -%}
{%- elif cookiecutter.format == 'regular' -%}
    {%- include 'cookiecutter_templates/app_regular.py' -%}
{%- endif -%}