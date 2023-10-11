import xlsxwriter
from slowniki import zestaw
from szuka_pliku import find_files
import openpyxl
import pandas as pd
from kwoty import hajs

zestaw()
wartosci = list(zestaw.zak.values())
klucze = list(zestaw.zak.keys())
hajs()
pieniądze = hajs.kwoty

e = find_files("obstawiansko.xlsx","C:")

if len(e) == 0:
    workbook = xlsxwriter.Workbook('obstawiansko.xlsx')
    worksheet = workbook.add_worksheet('Sheet1')
    bold = workbook.add_format({'bold': True})

    worksheet.write('A1', 'MECZE', bold)
    worksheet.write('B1', 'ZAKLAD', bold)
    worksheet.write('C1', 'KWOTA', bold)

    for i in range(len(klucze)):
        worksheet.write(i + 1, 1, str(wartosci[i]))
        worksheet.write(i + 1, 0, str(klucze[i]))
        worksheet.write(i + 1, 2, str(pieniądze[i]))
    print('skonczyłem')

    workbook.close()

elif len(e) == 1:
    xfile = openpyxl.load_workbook('obstawiansko.xlsx')
    sheet = xfile['Sheet1']

    pd_xl_file = pd.ExcelFile("obstawiansko.xlsx")
    df = pd_xl_file.parse("Sheet1")
    dimensions = df.shape
    k = dimensions[0]

    for a in range(len(klucze)):
        n = k + a + 2
        m = str(n)
        x = "A" + m
        y = "B" + m
        z = "C" + m
        sheet[y] = str(wartosci[a])
        sheet[x] = str(klucze[a])
        sheet[z] = str(pieniądze[a])

    xfile.save('obstawiansko.xlsx')
    print('skonczyłem')