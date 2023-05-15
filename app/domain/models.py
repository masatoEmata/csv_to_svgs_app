class SVGRow:
    def __init__(self, row: list):
        self.row = row
        self.svg_data = self._process_svg_data()

    def _process_svg_data(self) -> str:
        return self.row[0]

    @property
    def svg_data(self) -> str:
        return self._svg_data

    @svg_data.setter
    def svg_data(self, value: str) -> None:
        self._svg_data = value
