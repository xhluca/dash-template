{%- if cookiecutter.format == 'bootstrap' -%}
    {%- include 'templates/app_bootstrap.py' -%}
{%- elif cookiecutter.format == 'regular' -%}
    {%- include 'templates/app_regular.py' -%}
{%- endif -%}