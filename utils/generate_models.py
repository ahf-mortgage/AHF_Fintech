import pandas as pd
from pyexcelerate import Workbook

def generate_models_from_excel(file_path):
    df = pd.read_excel(file_path, engine='openpyxl')

    with open('models.py', 'w') as f:
        f.write('from django.db import models\n\n')

        for column in df.columns:
            column_name = column.lower().replace(' ', '_')
            column_type = df[column].dtype

            if column_type == 'object':
                model_field = 'CharField(max_length=100)'
            elif column_type == 'int64':
                model_field = 'IntegerField()'
            elif column_type == 'float64':
                model_field = 'FloatField()'
            else:
                model_field = 'CharField(max_length=100)'  # Default to CharField if the data type is unknown

            f.write(f'class {column_name.capitalize()}(models.Model):\n')
            f.write(f'    {column_name} = models.{model_field}\n\n')

        # Add logic to capture formulas and their results
        f.write('    @classmethod\n')
        f.write('    def capture_formulas(cls):\n')
        f.write('        workbook = Workbook()\n')
        f.write('        sheet = workbook.new_sheet("Formulas")\n')
        f.write('        headers = ["Formula", "Result"]\n')
        f.write('        sheet.append(headers)\n\n')

        for index, row in df.iterrows():
            for column in df.columns:
                cell_value = row[column]
                if isinstance(cell_value, str) and cell_value.startswith('='):
                    formula = cell_value[1:]
                    result = df.at[index, column]
                    sheet_row = [formula, result]
                    f.write(f'        sheet.append({sheet_row})\n')

        f.write('\n        workbook.save_as("formulas.xlsx")\n')

generate_models_from_excel('./data.xlsx')