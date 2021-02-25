import cx_Oracle
import config

# TEST 1
# TEST 2

class DB:
    connection = None
    cx_Oracle.init_oracle_client(
        lib_dir=r"C:\Users\Hanoof.Alqadeh\Downloads\instantclient-basic-windows.x64-18.5.0.0.0dbru\instantclient_18_5")
    def __init__(self):
        print('DB...')
        try:

            self.connection = cx_Oracle.connect('{0}/{1}@{2}:{3}/{4}'.format(config.username,
                                                                             config.password,
                                                                             config.dsn,
                                                                             config.port,
                                                                             config.SERVICE_NAME))

            cx_Oracle.connect

            print('V::', self.connection.version)


        except cx_Oracle.Error as error:
            print('ERROR', error)
            # release the connection
            if self.connection:
                self.connection.close()

    def printDescription(self):
        print('-------------------landing_db------------------------')

        sql = """SELECT * FROM landing_db"""
        cursor = self.connection.cursor()
        cursor.execute(sql)
        for each in cursor.description:
            print(each[0:2])
        for each in cursor.execute(sql):
            print(each)

            print('-------------------landing_db------------------------')

        print('---------------------relational_db---------------------')

        sql = """SELECT * FROM relational_db"""

        cursor = self.connection.cursor()
        cursor.execute(sql)
        c = 0
        for each in cursor.description:
            print(each[0:2])

            print('---------------------relational_db---------------------')

    def getRowByNumber(self, rowNumber='1'):
        sql = """with cte as (select relational_db.*, ROW_NUMBER() OVER (ORDER BY batch_id) R from relational_db) select * from cte where R =2""".format(rowNumber)
        print(':::::', sql)
        cursor = self.connection.cursor()
        for each in cursor.execute(sql):
            print(each)
            return each

    def insertIntoLandingDB(self, sheetSource='', cellSource='', cellContent='', TimeStamp='', BatchID=''):
        sql = """INSERT INTO LANDING_DB (Sheet_Source,Cell_Source,Cell_Content,Time_Stamp,Batch_ID)
        values ('{0}','{1}','{2}','{3}','{4}', '{5}')""".format(sheetSource, cellSource, cellContent, TimeStamp,
                                                                BatchID)
        print(':::::', sql)
        cursor = self.connection.cursor()
        cursor.execute(sql)
        self.connection.commit()


    def insertIntoRelationalDB(self, PUBLICATION_NAME_AR,
                    PUBLICATION_NAME_EN,
                    PUBLICATION_DATE_AR,
                    PUBLICATION_DATE_EN,
                    TABLE_ID,
                    REP_NAME_AR,
                    REP_NAME_EN,
                    TEM_ID,
                    AGE_GROUP_AR,
                    AGE_GROUP_EN,
                    SEX_AR,
                    SEX_EN,
                    OBS_VALUE,
                    TIME_PERIOD_Y,
                    TIME_PERIOD_M,
                    NOTE1_AR,
                    NOTE1_EN,
                    NOTE2_AR,
                    NOTE2_EN,
                    NOTE3_AR,
                    NOTE3_EN,
                    SOURCE_AR,
                    SOURCE_EN,
                    TIME_STAMP, Batch_ID ):
        sql = """insert into RELATIONAL_DB ( PUBLICATION_NAME_AR, PUBLICATION_NAME_EN, PUBLICATION_DATE_AR, 
        PUBLICATION_DATE_EN, TABLE_ID, REP_NAME_AR, REP_NAME_EN, TEM_ID, CL_AGE_GROUP_AR_V1, CL_AGE_GROUP_EN_V1, CL_SEX_AR_V1, CL_SEX_EN_V2, 
        OBS_VALUE, TIME_PERIOD_Y, TIME_PERIOD_M, NOTE1_AR, NOTE1_EN, NOTE2_AR, NOTE2_EN, NOTE3_AR, NOTE3_EN, 
        SOURCE_AR, SOURCE_EN, TIME_STAMP, BATCH_ID) values (
        '{0}' ,
         '{1}' , 
         '{2}' ,
          '{3}' ,
           '{4}' ,
            '{5}' , 
            '{6}' , 
        '{7}' , '{8}' , '{9}' , '{10}' , '{11}', '{12}' , '{13}' ,
         '{14}' , '{15}' , '{16}' , '{17}' , '{18}' , 
        '{19}' , '{20}' , '{21}' , '{22}' , '{23}' , '{24}')""".format(
            PUBLICATION_NAME_AR,
            PUBLICATION_NAME_EN,
            PUBLICATION_DATE_AR,
            PUBLICATION_DATE_EN,
            TABLE_ID,
            REP_NAME_AR,
            REP_NAME_EN,
            TEM_ID,
            AGE_GROUP_AR,
            AGE_GROUP_EN,
            SEX_AR,
            SEX_EN,
            OBS_VALUE,
            TIME_PERIOD_Y,
            TIME_PERIOD_M,
            NOTE1_AR,
            NOTE1_EN,
            NOTE2_AR,
            NOTE2_EN,
            NOTE3_AR,
            NOTE3_EN,
            SOURCE_AR,
            SOURCE_EN,
            TIME_STAMP, Batch_ID)
        print(':::::', sql)
        cursor = self.connection.cursor()
        cursor.execute(sql)
        self.connection.commit()

    def insertIntos2t_mapping(self, SHEET_SOURCE,
                               CELL_SOURCE,
                               SHEET_TARGET,
                               CELL_TARGET,
                               CELL_TYPE,
                               DESC_AR,
                               DATA_TYPE,
                               IS_MANDARORY,
                               REF_DICTIONARY ):
         sql = """INSERT INTO S2T_MAPPING (SHEET_SOURCE,CELL_SOURCE,SHEET_TARGET,CELL_TARGET,CELL_TYPE,DESC_AR,DATA_TYPE,IS_MANDARORY ,REF_DICTIONARY)
                values ('{0}','{1}','{2}','{3}','{4}', '{5}', '{6}', '{7}','{8}')""".format(SHEET_SOURCE, CELL_SOURCE, SHEET_TARGET, CELL_TARGET,
                                                                        CELL_TYPE,DESC_AR,DATA_TYPE,IS_MANDARORY,REF_DICTIONARY)
         print(':::::', sql)
         cursor = self.connection.cursor()
         cursor.execute(sql)

         self.connection.commit()

    def insertIntoref_dictionary(self, DESCRIPTION,ID,CL_ID):
         sql = """INSERT INTO REF_DICTIONARY (DESCRIPTION,ID,CL_ID)
                values ('{0}','{1}','{2}')""".format(DESCRIPTION, ID, CL_ID)

         print(':::::', sql)
         cursor = self.connection.cursor()
         cursor.execute(sql)
         self.connection.commit()



    def print2(self):
        db = cx_Oracle.connect('{0}/{1}@{2}:{3}/{4}'.format(config.username,
                                                            config.password,
                                                            config.dsn,
                                                            config.port,
                                                            config.SERVICE_NAME))
        cursor = db.cursor()
        SQL = "SELECT * FROM s2t_mapping"
        cursor.execute(SQL)
        for record in cursor:
            print('s2t_mapping', record)

        # cursor = db.cursor()
        # SQL = "SELECT * FROM relational_db"
        # cursor.execute(SQL)
        # for record in cursor:
        #     print('relational_db', record)
        #
        # SQL = "SELECT * FROM landing_db"
        # cursor.execute(SQL)
        # for record in cursor:
        #     print('landing_db', record)



    def closeConnection(self):
        # release the connection
        if self.connection:
            self.connection.close()

    #
    # connection_prod = cx_Oracle.connect('{0}/{1}@{2}:{3}/{4}'.format(config.username,
    #                                                                 config.password,
    #                                                                 config.dsn,
    #                                                                 config.port,
    #                                                                 config.SERVICE_NAME))
    #
    # cursor_prod = connection_prod.cursor()
    #
    # # set array size for source cursor to some reasonable value
    # # increasing this value reduces round-trips but increases memory usage
    # cursor_prod.arraysize = 500
    #
    # connection_dev = cx_Oracle.connect('{0}/{1}@{2}:{3}/{4}'.format(config.username,
    #                                                                 config.password,
    #                                                                 config.dsn,
    #                                                                 config.port,
    #                                                                 config.SERVICE_NAME))
    # cursor_dev = connection_dev.cursor()
    #
    # cursor_prod.execute("select * from Rational_DB_Mapping")
    # bind_names = ",".join(":" + str(i + 1) \
    #         for i in range(len(cursor_prod.description)))
    # sql_load = "insert into Rational_DB_Mapping values (" + bind_names + ")"
    # while True:
    #     rows = cursor_prod.fetchmany()
    #     if not rows:
    #         break
    #     cursor_dev.executemany(sql_load, rows)

