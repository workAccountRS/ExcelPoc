import cx_Oracle
import config




connection = None

try:

            connection = cx_Oracle.connect('{0}/{1}@{2}:{3}/{4}'.format(config.username,
                                                                        config.password,
                                                                        config.dsn,
                                                                        config.port,
                                                                        config.SERVICE_NAME))

            cx_Oracle.connect

            print(connection.version)

            db = cx_Oracle.connect('{0}/{1}@{2}:{3}/{4}'.format(config.username,
                                                            config.password,
                                                            config.dsn,
                                                            config.port,
                                                            config.SERVICE_NAME))

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

            print('-------------------landing_db------------------------')

            sql = """SELECT * FROM landing_db"""
            cursor = connection.cursor()
            cursor.execute(sql)
            for each in cursor.description:
                print(each[0:2])


            print('-------------------landing_db------------------------')

            print('---------------------relational_db---------------------')

            sql = """SELECT * FROM relational_db"""

            cursor = connection.cursor()
            cursor.execute(sql)
            c = 0
            for each in cursor.description:
                print(each[0:2])

            print('---------------------relational_db---------------------')

            print('---------------------s2t_mapping---------------------')

            sql = """SELECT * FROM s2t_mapping """

            cursor = connection.cursor()
            cursor.execute(sql)
            c = 0
            for each in cursor.description:
                print(each[0:2])

            print('---------------------s2t_mapping---------------------')


            print('---------------------ref_dictionary ---------------------')

            sql = """SELECT * FROM ref_dictionary """

            cursor = connection.cursor()
            cursor.execute(sql)
            c = 0
            for each in cursor.description:
                print(each[0:2])

            print('---------------------ref_dictionary---------------------')



except cx_Oracle.Error as error:
            print('ERROR', error)
finally:
            # release the connection
            if connection:
                connection.close()





