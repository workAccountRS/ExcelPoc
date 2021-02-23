from ExcelHandler import ExcelHandler
import Utilities
import csv
import time

# TO CALCULATE EXECUTION TIME
start_time = time.time()

InputFileName = "testFile.xlsx"

# TASK 1 READ THE EXCEL FILE:

excelHandler = ExcelHandler(fileName=InputFileName, dataOnlyFlag=True)

logID = Utilities.getBatchID()
currentTime = Utilities.getCurrentTime()

skipedRows = []
errors = []

#
# # LOOP THROUGH THE MAP
# for rowNumber in range(4, excelHandler.getMaxRow(sheet='Rational DB Mapping') + 1):
#     currentRowData = excelHandler.getRowDataFromSheet(sheet='Rational DB Mapping', row=rowNumber)


currentRowData = excelHandler.getRowDataFromSheet(sheet='Relational DB', row=2)
print(currentRowData)

currentRowData = excelHandler.getRowDataFromSheet(sheet='Relational DB', row=6)

Publication_Name_Ar = currentRowData[0]
Publication_Name_En = currentRowData[1]
Publication_Date_Ar = currentRowData[2]
Publication_Date_En = currentRowData[3]
Table_ID = currentRowData[4]
Rep_Name_Ar = currentRowData[5]
REP_NAME_EN = currentRowData[6]
TEM_ID  = currentRowData[7]
Age_Group_Ar = currentRowData[8]
Age_Group_En = currentRowData[9]
Sex_Ar = currentRowData[10]
Sex_En = currentRowData[11]
Obs_Value = currentRowData[12]
Time_Period_Y = currentRowData[13]
Time_Period_M = currentRowData[14]
Note1_Ar = currentRowData[15]
Note1_En = currentRowData[16]
Note2_Ar = currentRowData[17]
Note2_En = currentRowData[18]
Note3_Ar = currentRowData[19]
Note3_En = currentRowData[20]
Source_Ar = currentRowData[21]
Source_En = currentRowData[22]
Time_Stamp = currentRowData[23]
Batch_ID = currentRowData[24]




# Save the spreadsheet
excelHandler.saveSpreadSheet(fileName=InputFileName)


# ========================== RESULTS

print("ERRORS IN ROWS: " , errors)
print("SKIPPED ROWS: " , skipedRows)

# TO CALCULATE EXECUTION TIME
print("--- Took %s seconds to process ---" % (time.time() - start_time))