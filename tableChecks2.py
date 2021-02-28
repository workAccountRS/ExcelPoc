from typing import Type

from ValidationRules import ValidationRules

rules = ValidationRules()


class Table2:

    def table_rules(self, input, columns, dataType='text',lookups=None):

        output = {'isnull': [],
                  'wrong type': [],
                  'wrong language': [],
                  'out of range lookup':[]}

        for item in columns:
            if item in [*lookups['CL_ID']]:
                if not rules.check_dict(input[item],item,lookups):
                    output['out of range lookup'].append(item)

            if str(item).upper().__contains__('FREQUENCY'):
                continue
            else:
                # CHECK DATA TYPE
                dataType = 'text'
                if str(item).upper() == 'TIME_PERIOD_Y':
                    dataType = 'number'
                if not rules.data_type(input[item], dataType):
                    output['isnull'].append(item)

                # CHECK IF DATA IS NULL
                if not rules.notnull(input[item]):
                    output['isnull'].append(item)

                # CHECK LANGUAGE
                if str(item).upper().__contains__('EN'):
                    if not rules.lang(input[item].lower(), 'en'):
                        output['wrong language'].append(item)

                elif str(item).upper().__contains__('AR'):
                    if not rules.lang(input[item], 'ar'):
                        output['wrong language'].append(item)

        return output
