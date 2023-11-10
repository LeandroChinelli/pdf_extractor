import re
from .constants import RegexPatterns
from unidecode import unidecode

class TextCleaning:
    def __init__(self) -> None:
        self.regex = RegexPatterns()
    
    def text_cleaninig(self, text: str) -> str:
        cleaned_text = self.remove_accents(text)
        cleaned_text = self.remove_dots(cleaned_text)
        cleaned_text = self.remove_spaces(cleaned_text)
        cleaned_text = self.remove_non_alphanum(cleaned_text)
        cleaned_text = self.convert_uppercase(cleaned_text)
        cleaned_text = self.treat_total_values(cleaned_text)
        return cleaned_text
    
    @staticmethod
    def remove_accents(text: str) -> str:
        return unidecode(text)

    @staticmethod    
    def remove_dots(text: str) -> str:
        text = text.replace('.', '')
        return text

    @staticmethod
    def remove_spaces(text: str) -> str:
        text = text.replace(' ', '')
        return text
    
    def remove_non_alphanum(self, text):
        # Remove all non-alphanumeric characters except $
        text = re.sub(self.regex.NON_APLHANUM_PATTERS, 'w', text)
        return text

    @staticmethod
    def convert_uppercase(input_text):
        return input_text.upper()
    
    @staticmethod
    def treat_total_values(text: str) -> str:
        text = text.replace('VALORTOTAL', '01JAN2099VALORTOTAL')
        return text 
