#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import xlrd
import json

# ctype : 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error



def checkType(cell):
    if cell.ctype == 2:
        return str(int(cell.value))
    else:
        return str(cell.value)


def parseExcel():
    filepath = '/Users/wuqiyan/Documents/PayRel/paramsConfig.xlsx'
    data = xlrd.open_workbook(filepath)
    table = data.sheets()[0]
    nrows = table.nrows
    ncols = table.ncols
    jstr = {}
    sdksort = []
    for i in range(nrows):

        if i == 0:
            continue
        if i == 1:
            continue
        print i
        ss = {}
        for j in range(ncols):

            value = table.cell(i, j).value

            if i == 2 and j == 0:
                jstr['game_name'] = str(value)
                continue

            if i == 3 and j == 0:
                jstr['sdkRule'] = str(int(value))
                continue


            # if i > 4 & i < 10:
            #
            #     temp = checkType(table.cell(i, j))
            #     if j == 0:
            #         ss['sdk'] = temp
            #     elif j == 1:
            #         ss['appId'] = temp
            #     elif j == 2:
            #         ss['uid'] = temp
            #     elif j == 3:
            #         ss['sec'] = temp
            #     continue


            # temp = ''
            # if table.cell(i, j).ctype == 2:
            #     temp += str(int(value))
            # else:
            #     temp += value
            # ru += temp
            # ru += ','
        # print ru
        sdksort.append(ss)
    jstr['sdkSort'] = sdksort
    print jstr



if __name__ == "__main__":
    parseExcel()




