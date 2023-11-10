import re
from .constants import RegexPatterns

class RegexExtraction:
    def __init__(self) -> None:
        self.regex = RegexPatterns()
        
    def regex_extraction(self, text: str) -> list:
        dates = self.regex_dates(text)
        values = self.regex_values(text)
        places = self.regex_places(text)
        return dates, values, places

    def regex_dates(self, text:str) -> list:
        pattern = re.compile(self.regex.DATES_PATTERNS)
        matches = pattern.findall(text)
        return matches

    def regex_values(self, text:str) -> list:
        pattern = re.compile(self.regex.VALUES_PATTERNS)
        matches = pattern.findall(text)
        return matches

    def regex_places(self, text:str) -> list:
        matches = re.findall(self.regex.PLACES_PATTERNS, text)
        return matches