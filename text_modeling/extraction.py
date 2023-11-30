import re
import PyPDF2
from pandas import DataFrame
import pandas as pd
from .cleaning import TextCleaning
from .regex_extraction import RegexExtraction

class ExtractionPDF:
    def __init__(self) -> None:
        self.clean = TextCleaning()
        self.extract = RegexExtraction()
        
    def extract_pdf(self, pdf_path: str) -> DataFrame:
        
        dates_list, values_list, places_list = self.extract_text_to_list(pdf_path)
        
        dates = self.organized_dates(dates_list)
        values = self.organized_values(values_list)
        places = self.organized_places(places_list)
        df_pdf = pd.DataFrame({'dates': dates
                                ,'values': values
                                ,'places': places})

        return df_pdf
    
    def organized_dates(self, dates_list: list) -> list:
        flat_dates = [item for sublist in dates_list for item in sublist]
        dates = []
        for i in flat_dates:
            dates.append(i[0])
        return dates
    
    def organized_values(self, values_list: list) -> list:
        values_0 = [item for sublist in values_list for item in sublist]
        values = [item for item in values_0 if item != 'R$0,00']
        return values
    
    def organized_places(self, places_list: list) -> list:
        flat_places = [item for sublist in places_list for item in sublist]
        places = []
        for i in flat_places:
            if len(i[2])>100:
                places.append(i[2][:100])
            else:
                places.append(i[2])
        return places
    
    def extract_text_to_list(self, pdf_path: str) -> list:
        data_dates = []
        data_values = []
        data_places = []

        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file, strict=False)
            last_page_num = len(pdf_reader.pages)
            for page in pdf_reader.pages:
                if not(
                        page['/StructParents'] == 0
                        or page['/StructParents'] == (last_page_num)
                        or page['/StructParents'] == (last_page_num - 1)
                        or page['/StructParents'] == (last_page_num - 2)
                        or page['/StructParents'] == (last_page_num - 3)
                       ):
                    text = page.extract_text()
                    text = self.clean.text_cleaninig(text)
                    dates,values, places = self.extract.regex_extraction(text)
                    data_dates.append(dates)
                    data_values.append(values)
                    data_places.append(places)
                else: 
                    continue
        return data_dates, data_values, data_places