
class Helper_app:
    @staticmethod
    def isValidNumber(value):
        try:
            return int(value)
        except ValueError:
            return False
    