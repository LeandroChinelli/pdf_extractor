import re
import PyPDF2
import pandas as pd

def extract_pdf(pdf_path):
    data_dates = []
    data_values = []
    data_places = []
    
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file,strict=False)

        for page in pdf_reader.pages:
            text = page.extract_text()
            
            dates = regex_dates(text)
            data_dates.append(dates)
            
            values = regex_values(text)
            data_values.append(values)

            places = regex_places(text)
            data_places.append(places)

    return data_dates, data_values, data_places

def regex_dates(text):
    pattern = re.compile(r'\d{2}\s[a-z]{3}\s\d{4}')
    matches = pattern.findall(text)
    return matches

def regex_values(text):
    pattern = re.compile(r'R\$\s\d{0,4},\d{2}')
    matches = pattern.findall(text)
    return matches

def regex_places(text):
    pattern = re.compile(r'\d{2}\s[a-z]{3}\s\d{4}(\S{9})')
    pattern_end = r'R\$\s\d{0,4},\d{2}'
    matches = pattern.findall(text)
    return matches


if __name__=='__main__':
    pdf_path = '/home/leandrochinelli/repos/faturanovembro.pdf'
    dates,values,places = extract_pdf(pdf_path)

    flat_dates = [item for sublist in dates for item in sublist]
    flat_values = [item for sublist in values for item in sublist]
    flat_places = [item for sublist in places for item in sublist]
    
    print(len(flat_dates))
    print(len(flat_values ))
    print(len(flat_places))

    df_pdf = pd.DataFrame({'dates':flat_dates, 'places':flat_places, 'values':flat_values})

    print(df_pdf)