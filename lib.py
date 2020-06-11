
class UrlShortner():
    MAP = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    BASE = 62

    @staticmethod
    def url_to_id(url: str) -> int:
        """This method converts a string to max 6 digit id
        :param url:
        :returns id:
        """
        _id = 0
        for value in url:
            value = ord(value)
            _id *= UrlShortner.BASE
            if value <= ord('9'):
                _id += value - ord('0') + 52
            elif value <= ord('Z'):
                _id += value - ord('A') + 26
            else:
                _id += value - ord('a')
        return _id

    @staticmethod
    def id_to_url(_id: int) -> str:
        """This method converts id back to string
        :param id:
        :returns short_url:
        """
        short_url = ""
        while _id:
            short_url += UrlShortner.MAP[_id % UrlShortner.BASE]
            _id //= 62

        return short_url[::-1]
