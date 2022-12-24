# jupytee - magics for using GPT-like models inside Jupyter

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/fperez/jupytee/HEAD?labpath=examples%2Fjupytee-demo.ipynb)

A small, experimental playground with Jupyter magics to use OpenAI's GPT-3 models inside Jupyter environments.

This isn't even alpha software - it's just a quick and dirty prototype.  But it works, if you have the python `openai` package installed and the environment variable `OPENAI_API_KEY` defined with your personal API key as [per the docs](https://beta.openai.com/account/api-keys).

Yes, the name is a silly play on the pronunciation of GPT and Jupyter.

## Installation

`pip install jupytee`


## Usage

To load the extension, use

`%load_ext jupytee`

The package provides a few core magics, `%chat`, `%pic` and `%code` (along with some extra helpers), that wrap your interactions around the [OpenAI Python API](https://beta.openai.com/docs/api-reference/introduction). They target the main entry points of the API: text completion, image generation and code completion, respectively. 

You can see them in action in the notebook contained in the `examples` directory (which you can run immediately by clicking on the Binder button above).

Briefly, these are some examples of how you can use them. A simple question (note the extra space before `?`, needed b/c IPython's help will otherwise trigger by accident):

```
%chat What is 100F in Celsius ?
```

You can control the sampling temperature with `-T`:

```
%chat -T 1 --raw Write an uplifting short poem
```

Markdown (with math) work:

```
%%chat
Produce the LaTeX form of Maxwell's equations.
```

For `pic`, you can control image size and the number of images returned:

```
%pic -s m -n 2 an astronaut knitting
```

When generating code, you can iteratively refine the answer by referring to the `CODE` special word (in all CAPS):

`%code A function to add two numbers.`

and then:

`%code Update CODE to have a docstring explaining its use.`


## License

BSD 3-Clause.
