import toml

from .abstract_info import AbstractInfo

class GuideInfo(AbstractInfo):
    def __init__(self) -> None:
        super().__init__()

        self.package = ""
        self.backend_class = ""
        self.page_class = ""

    @property
    def package_path(self) -> str:
        return self.package.replace(".", "/")

    def _parse_toml_data(self, data):
        super()._parse_toml_data(data)

        self.package = data['component']['package']
        self.backend_class = data['class']['backend']
        self.page_class = data['class']['page']

    def parse(self, filename):
        parsed_toml = toml.load(filename)
        self._parse_toml_data(parsed_toml)
    
    def dump(self):
        super().dump()

