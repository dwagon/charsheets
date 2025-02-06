""" Character sheet renderer"""

import argparse
import importlib.util
from typing import Type

from jinja2 import FileSystemLoader, Environment

from charsheets.character import Character


#############################################################################
def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog="CharSheets")
    parser.add_argument("charfile", type=argparse.FileType("r"))
    parser.add_argument("--template", default="char_sheet.jinja")
    return parser.parse_args()


#############################################################################
def import_character(file_handle, module_name="charsheet") -> Type[Character]:
    spec = importlib.util.spec_from_file_location(module_name, file_handle.name)
    if spec is None:
        raise ImportError(f"Couldn't load {module_name}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return getattr(module, "character")


#############################################################################
def render(character: Character, template_file: str) -> str:
    # LateX uses lots of {{ }} - so change delimiter
    env = Environment(
        loader=FileSystemLoader("templates"),
        block_start_string="[%",
        block_end_string="%]",
        variable_start_string="[[",
        variable_end_string="]]",
        comment_start_string="[#",
        comment_end_string="#]",
    )
    template = env.get_template(template_file)
    return template.render(X=character)


#############################################################################
def main():
    args = parse_args()
    character = import_character(args.charfile)
    tex_output = render(character, args.template)
    print(tex_output)


#############################################################################
if __name__ == "__main__":
    main()
