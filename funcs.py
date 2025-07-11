def iter_masters_names(ws):

    row = 2
    masters_set = set()
    master_1 = ''
    master_2 = ''
    master_3 = ''
    master_4 = ''

    while True:
        cell_value = ws.cell(row=row, column=5).value
        print(cell_value)

        if cell_value is None:
            print(masters_set)
            break

        masters_set.add(cell_value)

        # print(f"Строка {row}: {cell_value}")

        row += 1

