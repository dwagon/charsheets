""" Character sheet renderer"""

import argparse
import importlib.util
import sys

from jinja2 import FileSystemLoader, Environment

from charsheets.character import Character


#############################################################################
def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog="CharSheets")
    parser.add_argument("charfile", type=argparse.FileType("r"))
    parser.add_argument("--template", default="char_sheet.jinja")
    args = parser.parse_args()
    return args


#############################################################################
def import_sheet(file_handle, module_name="charsheet"):
    spec = importlib.util.spec_from_file_location(module_name, file_handle.name)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


#############################################################################
def render(charsheet: Character, template_file: str) -> str:
    # LateX uses lots of {{ }} - so change delimiter
    env = Environment(
        loader=FileSystemLoader("templates"),
        block_start_string="[%",
        block_end_string="%]",
        variable_start_string="[[",
        variable_end_string="]]",
    )
    template = env.get_template(template_file)
    tex = template.render(X=charsheet)
    return tex


#############################################################################
def compile(input_str: str):
    """Compile into PDF"""


#############################################################################
def main():
    args = parse_args()
    character_module = import_sheet(args.charfile)
    charsheet = Character(character_module)
    tex_output = render(charsheet, args.template)
    compile(tex_output)
    print(tex_output)


#############################################################################
if __name__ == "__main__":
    main()
