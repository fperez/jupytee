"""Magics to support ChatGPT interactions in IPython/Jupyter.
"""

import os
import sys

from IPython.core.magic import (Magics, magics_class, line_magic,
                                cell_magic, line_cell_magic)

from IPython.display import display, Image, JSON, Markdown

import openai

def get_chat_completion(prompt, temperature=0.6):
    response = openai.Completion.create(
                model="text-davinci-003",
                prompt=prompt,
                max_tokens=2000,
                temperature=temperature,
            )
    return response


def get_code_completion(instruction, input="", temperature=0.1):
    try:
        response = openai.Edit.create(
                    model="code-davinci-edit-001",
                    instruction=instruction,
                    input=input,
                    temperature=temperature,
                )
    except openai.InvalidRequestError as e:
        print(f"ERROR: {e.user_message}", file=sys.stderr)
    else:
        return response


def get_image(prompt, n=1, size="256x256"):
    response = openai.Image.create(prompt=prompt,
                                   n=n, size=size)
    return response


# The class MUST call this class decorator at creation time
@magics_class
class GPTChat(Magics):
    def __init__(self, shell):
        # You must call the parent constructor
        super(GPTChat, self).__init__(shell)
        self.api_key = openai.api_key = os.getenv("OPENAI_API_KEY")
        self.last_code = ""

    @line_cell_magic
    def chat(self, line, cell=None):
        "Chat with GPTChat."
        opts, args = self.parse_options(line, 'rl:T:')
        raw = 'r' in opts
        temp = float(opts.get('T', 0.6))
        
        if cell is None:
            prompt = args
        else:
            prompt = cell
        response = get_chat_completion(prompt, temperature=temp)
        output = response.choices[0].text.strip()
        if raw:
            display(Markdown(f"*Raw output*\n---\n```\n{output}\n```\n---"))
        return Markdown(output)

    @line_cell_magic
    def code(self, line, cell=None):
        """Prompt for code generation.
        
        Options:
        -l: str. Language (default Python). Used only for formatting the output,
        you'll need to specify the language in the prompt for ChatGPT to understand.
        
        """
        opts, args = self.parse_options(line, 'l:T:')
        lang = opts.get('l', 'python')
        temp = float(opts.get('T', 0.1))
        input = ""
        if cell is None:
            instruction = args
        else:
            parts =  cell.split("##")
            if len(parts) == 1:
                instruction = cell
            elif len(parts) == 2:
                instruction, input = parts
            else:
                print("Only one ## marker is supported", file=sys.stderr)
                return
        if not(input) and "CODE" in instruction:
            input = self.last_code

        response = get_code_completion(instruction, input, temperature=temp)
        self.last_code = result = response.choices[0].text.strip()
        return Markdown(f"```{lang}\n{result}\n```")

    @line_magic
    def get_code(self, line):
        "Return the last computed code in a new cell."
        self.shell.set_next_input(self.last_code)

    @line_cell_magic
    def pic(self, line, cell=None):
        """Prompt for image generation.
        
        Options:
         -s, m, l: size (small, med, large). Only one.
         -n: int. Number of images to return.
        """
        opts, args = self.parse_options(line, 'smln:')
        size_choice = set(opts.keys()).intersection({'s', 'm', 'l'})
        if len(size_choice) > 1:
            print("Error: only one of '-s', '-m', or '-l' can be specified.",
                  file=sys.stderr)
            return
        sizes = dict(s="256x256", m="512x512", l="1024x1024")
        if size_choice:
            size = sizes[size_choice.pop()]
        else:
            size = sizes['s']

        n = int(opts.get('n', 1))

        prompt = args if cell is None else cell

        response = get_image(prompt, n, size)
        for img in response.data:
            display(Image(url=img.url))


get_ipython().register_magics(GPTChat)