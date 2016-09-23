from tkinter.filedialog import *
from xlrd import *
from collections import OrderedDict
import simplejson as json
from tkinter.messagebox import*




def converter():

    try:

        uploadXls = askopenfilename()
        workbook = open_workbook(uploadXls)

        sheet = workbook.sheet_by_index(0)

        fileList = []

        for row in range(1, sheet.nrows):
            file = OrderedDict()
            row_values = sheet.row_values(row)
            for i in range(0, sheet.ncols):
                file[sheet.cell_value(0,i)] = row_values[i]




            fileList.append(file)

        jsonFile = json.dumps(fileList, separators=(',',':'), indent= 4 * ' ')


        with open('data.json', 'w') as f:
            f.write(jsonFile)

        showinfo("Arquivo convertido com sucesso!", "Clique em ok para fechar o programa.")
        sys.exit(0)

    except Exception:
        showerror("Arquivo não permitido!", "Favor escolher um arquivo com extensão .xls, ou .xlsx")

























