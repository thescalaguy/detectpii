import re


class Regex:

    def __init__(self, obj, regex):
        self.obj = obj
        self.regex = regex

    def __call__(self, *args):
        def regex_method(text=None):
            return [
                x.strip() if isinstance(x, str) else "".join(x)
                for x in self.regex.findall(text or self.obj.text)
            ]

        return regex_method


class CommonRegex(object):

    def __init__(self, regexes: dict[str, re.Pattern], text: str = ""):
        self.text = text

        for k, v in list(regexes.items()):
            setattr(self, k, Regex(self, v)(self))

        if text:
            for key in list(regexes.keys()):
                method = getattr(self, key)
                setattr(self, key, method())
