class Colors():

    COLORS = [
        "RED",
        "BLUE",
        "YELLOW",
        "GREEN",
        "WHITE"
    ]

    @staticmethod
    def getColor(color):
        for option in Colors.COLORS:
            if str(color).upper() == option:
                return option
        else:
            return None
