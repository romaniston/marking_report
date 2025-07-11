from flask import Flask, render_template
from openpyxl import load_workbook

import funcs

app = Flask(__name__)

# Загружаем Excel-файл
wb = load_workbook('tables\test_table.xlsx', data_only=True)
ws = wb.active

@app.route('/')
def index():

    result = []

    for merged_range in ws.merged_cells.ranges:
        if merged_range.min_col == 16:
            total_output = ws.cell(row=merged_range.min_row, column=16).value

            master_name = ws.cell(row=merged_range.min_row, column=5).value

            result.append({
                'name': master_name,
                'output': total_output
            })

    return render_template('index.html', masters=result)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=4995, debug=True)

    funcs.iter_masters_names(ws)
