from openpyxl import load_workbook

class ExcelWriter:
    def __init__(self, file_path):
        self.file_path = file_path
        self.wb = load_workbook(file_path)
        self.sheet = self.wb["Template"]
        self.start_row = 6

    def write_sku(self, sku, index):
        row = self.start_row + index
        self.sheet.cell(row=row, column=1).value = sku
        self.wb.save(self.file_path)
