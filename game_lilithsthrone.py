from ..basic_game import BasicGame


class LilithsThrone(BasicGame):

    Name = "Lilith's Throne Support Plugin"
    Author = "Werradith_Toximble"
    Version = "1.0"

    GameName = "Lilith's Throne"
    GameShortName = "lilithsthrone"
    GameBinary = "LilithsThrone.jar"
    GameDataPath = "res\mods"
    GameDocumentsDirectory = "%GAME_PATH%\data"
    GameSavesDirectory = "%GAME_DOCUMENTS%\saves"
    GameSaveExtension = "xml"

    def iniFiles(self):
        return ["properties.xml"]
