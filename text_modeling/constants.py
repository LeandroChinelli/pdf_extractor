import os

class RegexPatterns:
    DATES_PATTERNS = r'([0-3]\d(JAN|FEV|MAR|ABR|MAI|JUN|JUL|AGO|SET|OUT|NOV|DEZ)\d{4})'
    VALUES_PATTERNS = r'R\$\d{0,5},\d{2}'
    TO_EXCLUDE_PATTERS = r'COTACAODODOLARAMERICANOR\$\d{0,5},\d{2}'
    PLACES_PATTERNS = f'{DATES_PATTERNS}(.*?){VALUES_PATTERNS}'
    NON_APLHANUM_PATTERS  = r'[^a-zA-Z0-9$,]'


class FilePath:
    def __init__(self):
        self.files = self.get_all_files(f'{os.getcwd()}\\credit_card_receipt\\')

    def get_all_files(self, folder_path):
        files = []
        for root, dirs, filenames in os.walk(folder_path):
            for filename in filenames:
                file_path = os.path.join(root, filename)
                file_data = [file_path, filename]
                files.append(file_data)
        return files

    def get_files(self):
        return self.files

class Constants:
    TOTAL_VALUE = 'VALORTOTAL'
    ONLINE_PAYMENT = 'PAGAMENTOONLINE'
    REGULAR_PAYMENT = 'PAGTODEBITOAUTOMATICO'