# jupytee - magics for using GPT-like models inside Jupyter

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/fperez/jupytee/HEAD?labpath=examples%2Fjupytee-demo.ipynb)

A small, experimental playground with Jupyter magics to use OpenAI's GPT-3 models inside Jupyter environments.

This isn't even alpha software - it's just a quick and dirty prototype.  But it works, if you have the python `openai` package installed and the environment variable `OPENAI_API_KEY` defined with your personal API key as [per the docs](https://beta.openai.com/account/api-keys).

Yes, the name is a silly play on the pronunciation of GPT and Jupyter.

## Installation

`pip install jupytee`


## Usage

The package provides a few core magics, `%chat`, `%pic` and `%code` (along with some extra helpers), that wrap your interactions around the [OpenAI Python API](https://beta.openai.com/docs/api-reference/introduction). they target the main entry points of the API: text completion, image generation and code completion, respectively. 

You can see them in action in the notebook contained in the `examples` directory (which you can run immediately by clicking on the Binder button above).

## License

BSD 3-Clause.
