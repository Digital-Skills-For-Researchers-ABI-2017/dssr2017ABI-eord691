import xlrd

def extract_xlsx(filename):
    """
   Opens the excel file containing data and then storing the cell values
   as coordinates in x, y and z
    """
#call out workbook
    workbook = xlrd.open_workbook('filename')
    worksheet = workbook.sheet_by_index(0)

    for worksheet in workbook.sheets():
        for row in range(worksheet.nrows):
            for column in range(worksheet.ncols):
                x = float(worksheet.cell(row,0).value)
                y = float(worksheet.cell(row,1).value)
                z = float(worksheet.cell(row,1).value)
    return 



