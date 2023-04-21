from pathlib import Path

from jinja2 import Template


class SVGRow:
    def __init__(self, row: list):
        self.row = row
        self.svg_template = self._load_svg_template()

    def _load_svg_template(self) -> Template:
        template_path = Path(__file__).parent.parent / "templates" / "svg_template.xml"
        with open(template_path, "r", encoding="utf-8") as f:
            return Template(f.read())

    @property
    def svg_data(self) -> str:
        return self.svg_template.render(row=self.row)
