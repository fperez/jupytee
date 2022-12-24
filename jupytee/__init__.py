"""Magics to support GPT-3 interactions in IPython/Jupyter.
"""

from .jupytee import GPTMagics


__version__ = "0.0.4"


def load_ipython_extension(ipython):
    """
    Any module file that define a function named `load_ipython_extension`
    can be loaded via `%load_ext module.path` or be configured to be
    autoloaded by IPython at startup time.
    """
    ipython.register_magics(GPTMagics)
