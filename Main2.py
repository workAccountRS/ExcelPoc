from ExcelHandler import ExcelHandler
import Utilities
import csv
import time

# TO CALCULATE EXECUTION TIME
start_time = time.time()

InputFileName = "testFile.xlsx"

# TASK 1 READ THE EXCEL FILE:

excelHandler = ExcelHandler(fileName=InputFileName)

logID = Utilities.getBatchID()
currentTime = Utilities.getCurrentTime()

skipedRows = []
errors = []


# LOOP THROUGH THE MAP
for rowNumber in range(4, excelHandler.getMaxRow(sheet='Rational DB Mapping') + 1):
    currentRowData = excelHandler.getRowDataFromSheet(sheet='Rational DB Mapping', row=rowNumber)
    print(currentRowData)



# Save the spreadsheet
excelHandler.saveSpreadSheet(fileName=InputFileName)


# ========================== RESULTS

print("ERRORS IN ROWS: " , errors)
print("SKIPPED ROWS: " , skipedRows)

# TO CALCULATE EXECUTION TIME
print("--- %s seconds ---" % (time.time() - start_time))