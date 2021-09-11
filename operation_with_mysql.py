import pymysql
import datetime as dt
import database_config as db_c


def insert_data_to_mysql_database(file_new_name: str, file_info: str, mysql_config: dict,
                                  db_config: list = db_c.DB_CONFIG):
    try:
        connection = pymysql.connect(
                                    host=mysql_config['host'],
                                    port=mysql_config['port'],
                                    user=mysql_config['user'],
                                    password=mysql_config['password'],
                                    database=mysql_config['db_name'],
                                    cursorclass=pymysql.cursors.DictCursor
                                    )
        try:
            with connection.cursor() as cursor:

                # create_table = f'CREATE TABLE {mysql_config["table_name"]}(id int AUTO_INCREMENT, '\
                #                f'{", ".join(f"{column[0]} {column[1]}" for column in db_config)}, '\
                #                'PRIMARY KEY (id));'
                # print(create_table)
                # cursor.execute(create_table)
                # print('Table created')

                current_date = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                cursor.execute('SET sql_mode = NO_BACKSLASH_ESCAPES')

                insert_data= f'INSERT INTO '\
                             f'{mysql_config["table_name"]}({", ".join(f"{column[0]}" for column in db_config)}) '\
                             f'VALUES ("{file_new_name}" ,"{current_date}", ' \
                             f'"{file_info[0]}", "{file_info[1]}", "{file_info[2]}", {file_info[3]})'
                print(insert_data)
                cursor.execute(insert_data)
                connection.commit()

        except Exception as ex:
            print('*****')
            print(ex)
        finally:
            connection.close()

    except Exception as ex:
        print('Connection to MySQL database failed.')
        print(ex)

