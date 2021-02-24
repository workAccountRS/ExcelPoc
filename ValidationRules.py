import datetime


# This will return true false booleans based on check

class ValidationRules:

    def check_notnull(self):
        return self is not None

    def check_type(self, data_type="text", date_format=None):
        if data_type == "text":
            return isinstance(self, str)

        elif data_type == "number":
            number_types = (int, float, complex)
            return isinstance(self, number_types)

        elif data_type == "date":
            try:
                datetime.datetime.strptime(self, date_format)
                return True
            except ValueError:
                return False

    # check logic
    def check_lang(self, lang=None):
        if lang == 'ar':
            alphabet = ['ا', 'ب', 'ي', 'و', 'ه', 'ن', 'م', 'ل', 'ك', 'ق', 'ف', 'غ', 'ع', 'ظ', 'ط', 'ض', 'ص', 'ش', 'س',
                        'ز', 'ر', 'ذ', 'د', 'خ', 'ح', 'ج', 'ث', 'ت']
        elif lang == 'en':
            alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                        't', 'u', 'v', 'w', 's', 'y', 'z']

        for i in self:
            if isinstance(i, str):
                if i in alphabet:
                    return True
                else:
                    return False

    def freq(self, prev=None, freq=None):
        if prev is None:
            return True

        else:
            return abs(prev - self) == freq

    def check_special_type(self):
        pass

    def check_dict(self):
        pass
