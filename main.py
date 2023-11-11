import os
from argparse import ArgumentParser
from text_modeling import ExtractionPDF


def main(pdf_path: str):
    extractor = ExtractionPDF()
    dates, values, places = extractor.extract_pdf(pdf_path)

    flat_dates = [item for sublist in dates for item in sublist]
    flat_values = [item for sublist in values for item in sublist]
    flat_places = [item for sublist in places for item in sublist]

    print('flat_date: ', (flat_dates))
    print('len flat_values: ', len(flat_values))
    print('flat_places: ', (flat_places))


parser = ArgumentParser()
parser.add_argument('-f', help='Input PDF file', required=False)


if __name__ == '__main__':
    args = parser.parse_args()
    file = args.f

    if not file or not os.path.exists(file):
        print('Input file not received!')
        file = input('Input file path: ')

        if not os.path.exists(file):
            print('File not found')
            exit()

    main(file)
