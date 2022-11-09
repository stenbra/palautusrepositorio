from urllib import request
from project import Project
import tomlkit


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        
        parser =tomlkit.loads(content)
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(parser["tool"]["poetry"]["name"], parser["tool"]["poetry"]["description"], parser["tool"]["poetry"]["dependencies"], parser["tool"]["poetry"]["dev-dependencies"])
