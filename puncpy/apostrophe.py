from puncpy.model import ApostropheItem
from puncpy.model import ApostropheItemCollection


class Apostrophe:

    # Rules
    d1 = {
        "Apostrophe_Rule_1": ("NNN", "POS")
    }

    def execute(self, text: str) -> ApostropheItemCollection:
        # Validate text is single sentence and  sentence contains an apostrophe
        # - return empty ApostropheItemCollection

        # Tokenize

        # Tag

        # Interpret - match tagged text to rules

        # Build response

        return [ApostropheItem("It's", "Apostrophe_Rule_1")]
