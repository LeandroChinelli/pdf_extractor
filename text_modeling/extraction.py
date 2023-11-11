import re
import PyPDF2
import pandas as pd
from .cleaning import TextCleaning
from .regex_extraction import RegexExtraction

class ExtractionPDF:
    def __init__(self) -> None:
        self.clean = TextCleaning()
        self.extract = RegexExtraction()
        
    def extract_pdf(self, pdf_path: str) -> list:
        data_dates = []
        data_values = []
        data_places = []
        data_list = []

        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file, strict=False)

            for page in pdf_reader.pages:
                text = page.extract_text()
                text = self.clean.text_cleaninig(text)
                dates,values, places = self.extract.regex_extraction(text)
                data_list_i = [dates, values, places]    
                data_list.append(data_list_i)
                data_dates.append(dates)
                data_values.append(values)
                data_places.append(places)
                
        return data_dates, data_values, data_places
