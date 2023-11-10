class RegexPatterns:
    DATES_PATTERNS = r'\d{2}[A-Z]{3}\d{4}'
    VALUES_PATTERNS = r'R\$\d{0,4},\d{2}'
    PLACES_PATTERNS = f'{DATES_PATTERNS}(.*?){VALUES_PATTERNS}'
    NON_APLHANUM_PATTERS  = r'[^a-zA-Z0-9$,]'