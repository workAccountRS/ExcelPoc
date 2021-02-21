from ExcelHandler import ExcelHandler
import Utilities
import csv
import time

# TO CALCULATE EXECUTION TIME
start_time = time.time()

InputFileName = "testFile.xlsx"

# TASK 1 READ THE EXCEL FILE:

excelHandler = ExcelHandler(fileName=InputFileName)
lastRow = excelHandler.getMaxRow(sheet='Landing DB') + 1

logID = Utilities.getBatchID()
currentTime = Utilities.getCurrentTime()

skipedRows = []
errors = []

# CREATE CSV
with open('landing_DB.csv', 'a+') as csv_file:
    pass

# ADD HEADER (CSV)
with open('landing_DB.csv') as csv_file:
    row_count = sum(1 for row in csv_file)
    if row_count == 0:
        with open('landing_DB.csv', 'a', newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter='#')
            writer.writerows([['Sheet_Source', 'Cell_Source', 'Cell_Content', 'Time_Stamp', 'Batch_ID']])

# LOOP THROUGH THE MAP
for rowNumber in range(2, excelHandler.getMaxRow(sheet='S2T Mapping') + 1):
    currentRowData = excelHandler.getRowDataFromSheet(sheet='S2T Mapping', row=rowNumber)
    sheet_source = currentRowData[0]
    cell_source = currentRowData[1]
    sheet_target = currentRowData[2]
    cell_target = currentRowData[3]

    if sheet_target == 'NA':
        skipedRows.append(rowNumber)
        continue

    source_data = excelHandler.getCellFromSheet(sheet=sheet_source, cell=cell_source)
    target_data = excelHandler.getCellFromSheet(sheet=sheet_target, cell=cell_target)

    print("============= ROW NUMBER: ", rowNumber)
    print("UNIQUE ID: ", str(logID), " DATE AND TIME =", currentTime)
    print("SOURCE DATA: ", source_data)
    print("============================")

    # TASK 2 FILL THE LANDING DB:
    # Sheet_Source | Cell_Source | Cell_Content	| Time_Stamp | Batch_ID

    with open('landing_DB.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter='#')
        writer.writerow([sheet_source, cell_source, source_data, currentTime, str(logID)])

    # WRITING ON A EXCEL FILE (Write Test)
    try:
        excelHandler.writeCell(sheet='Target', cell=str(cell_target), value=source_data)

        excelHandler.writeCell(sheet='Landing DB', cell=str('A' + str(lastRow)), value=sheet_source)
        excelHandler.writeCell(sheet='Landing DB', cell=str('B' + str(lastRow)), value=cell_source)
        excelHandler.writeCell(sheet='Landing DB', cell=str('C' + str(lastRow)), value=source_data)
        excelHandler.writeCell(sheet='Landing DB', cell=str('D' + str(lastRow)), value=currentTime)
        excelHandler.writeCell(sheet='Landing DB', cell=str('E' + str(lastRow)), value=str(logID))
    except:
        print("ERROR IN ROW#" + str(rowNumber))
        errors.append(['ROW NUMBER:' + str(rowNumber) , 'CELL SOURCE:' + cell_source ,'CELL TARGET:' + cell_target])

    # NEXT ROW TO WRITE
    lastRow += 1

# Save the spreadsheet
excelHandler.saveSpreadSheet(fileName=InputFileName)


# ========================== RESULTS

print("ERRORS IN ROWS: " , errors)
print("SKIPPED ROWS: " , skipedRows)

# TO CALCULATE EXECUTION TIME
print("--- %s seconds ---" % (time.time() - start_time))