import pymysql
import datetime as dt

MYSQL_CONFIG = {
                'host': 'localhost',
                'user': 'Timerxan',
                'port': 3306,
                'password': '123456',
                'db_name': 'sakila',
                'table_name': 'files_test_5'
                }

DB_CONFIG = (
             ('file_new_name', 'varchar(100)'),
             ('load_and_save_date', 'datetime'),
             ('loaded_from_computer_name', 'varchar(100)'),
             ('file_initial_absolute_path', 'varchar(256)'),
             ('file_initial_creation_date', 'datetime'),
             ('file_size', 'int')
            )


def insert_data_to_mysql_database(file_new_name: str, file_info: str, mysql_config: dict, db_config: list = DB_CONFIG):
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

                current_date = dt.datetime.now().strftime('"%Y-%m-%d %H:%M:%S"')

                insert_data= f'INSERT INTO '\
                             f'{mysql_config["table_name"]}({", ".join(f"{column[0]}" for column in db_config)}) '\
                             f'VALUES ("{file_new_name}" ,"{current_date}", ' \
                             f'"{file_info[1]}", "{file_info[2]}")'
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


# insert_data_to_mysql_database(('file_10', 'fileinfo_1', 'file_attr_23423342'), MYSQL_CONFIG)
