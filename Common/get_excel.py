import  xlrd
def get_excel_userid(row):
    excel =xlrd.open_workbook(r"D:\api_auto\testdata\user_id.xlsx")  #打开文件地址   最好绝对路径
    table =excel.sheets()[0]       #表格第一页的数据
    # print(table.nrows)             #表格第一页的数据行数
    # print(table.ncols)             #表格第一页的数据列数
    #
    # print(table.row_values(0))     #表格第一行数据
    # print(table.col_values(1))     #表格第一列数据
    # print(table.cell_value(0,1))     #表格第一行第二列数据

    '''1.返回两个值就传两个变量  return int(table.cell_value(row,0),table.cell_value(row,0))
      user_id, python =get_excel_userid(row)
      2.excel 是字典 用evl转化
       
      '''
    return int(table.cell_value(row,0))



def get_excellzone(filename,sheetname):
    list = []
    workbook=xlrd.open_workbook(filename)
    table =workbook.sheet_by_name(sheetname)

    for i  in range (1,table.ncols):
        list=list.append(table.row(i))

    return list

def getData(filepath,sheetname):
    '''
    #打开excel
    workbook=xlrd.open_workbook(filepath)
    #打开excel文件中的一张表
    table=workbook.sheet_by_name(sheetname)
    #读数据
    list=table.row_values(1)
    return  list
    '''
    list=[]
    workbook = xlrd.open_workbook(filepath)
    table = workbook.sheet_by_name(sheetname)
    for i  in range(1,table.nrows):
        list.append(table.row_values(i))
    return list








