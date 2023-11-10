from text_modeling import ExtractionPDF

pdf_path = '/home/leandrochinelli/repos/faturanovembro.pdf'
extractor = ExtractionPDF()
dates, values, places = extractor.extract_pdf(pdf_path)

flat_dates = [item for sublist in dates for item in sublist]
flat_values = [item for sublist in values for item in sublist]
flat_places = [item for sublist in places for item in sublist]

print(len(flat_dates))
print((flat_values ))
print(len(flat_places))