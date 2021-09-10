from collections import namedtuple
import sqlite3
import numbers

# ---------------------Create database and table ----------------------------------
def create_table():
    """ create product database connection to the SQLite database
        have product table and transfer table 
    :return: Connection object or None 
    """

    try:
        connect = sqlite3.connect('productDB.db')
        cur = connect.cursor()
        sql = "create TABLE if not EXISTS product (product_id INTEGER PRIMARY KEY,"\
            "product_name text UNIQUE, stockA int, stockB int, product_price real);"
        
        cur.execute(sql)
        connect.commit()

        sql = "create table if not exists transfer "\
            "(transfer_id text PRIMARY key not null, product_id INTEGER, product_quantity int, type_stock INTEGER NOT NULL);"

        cur.execute(sql)
        connect.commit()
    except connect.Error as err:
        print(f'error is {err}')
        return False
    
    finally:
        cur.close()
        connect.close()


#---------------- Product data when click save ------------------------

def insert_product_table(pname: str, stockA: numbers.Real, stockB: numbers.Real, price: numbers.Number) -> bool:
    """ 
    Insert data to product table
    :param: product_name, stockA, stockB
    :return: True or False 
    """
    try:
        connect = sqlite3.connect('productDB.db')
        cur = connect.cursor()

        # get data from database
        datas_pid = cur.execute("select count(*) from product;").fetchone()
        pid = datas_pid[0]

        if not pid:
            pid = 1
        else:
            pid += 1

        # Insert data to database
        sql = "INSERT INTO product (product_id, product_name, stockA, stockB, product_price) "\
            "VALUES (?, ?, ?, ?, ?)"
        cur.execute(sql, (pid, pname, stockA, stockB, price))
        connect.commit()

    except connect.Error as err:
        print('insert_product_table')
        print(f'error is {err}')
        return False
    else:
        return True
    finally:
        cur.close()
        connect.close()


def select_product_name(productname: str) -> bool:
    """ 
    Check data in database with product name
    :param: prodcutname
    :return: True or False
    """

    try:
        connect = sqlite3.connect('productDB.db')
        cur = connect.cursor()

        sql = "SELECT * FROM product WHERE product_name = ?;"
        cur.execute(sql, (productname, ))
        connect.commit()
        result = False
        for _ in cur.fetchall():
            result = True
        return result
    
    except connect.Error as err:
        print('select_product_name')
        print(f'error is {err}')
        return False
    
    finally:
        cur.close()
        connect.close()
        

def select_product_id():
    """
    Search product ID in database
    """

    try:
        connect = sqlite3.connect('productDB.db')
        cur = connect.cursor()

        sql = "SELECT product_id FROM product order by product_id;"
        data = cur.execute(sql)
        connect.commit()
        result = False
        for row in data:
            result = row[0]
        return result

    except connect.Error as err:
        print('select_product_id')
        print(f'error is {err}')
    finally:
        cur.close()
        cur.close()


def select_product_table():
    try:
        connect = sqlite3.connect('productDB.db')
        cur = connect.cursor()

        sql = "select * from product;"
        cur.execute(sql)
        connect.commit()

    except connect.Error as err:
        print('select_product_table')
        print(f'error is {err}')
        return False

    else:
        return cur.fetchall()
    finally:
        cur.close()
        connect.close()


def update_product_table(pid: int, pname: str, stockA: numbers.Real, stockB: numbers.Real):
    try:
        connect = sqlite3.connect("productDB.db")
        cur = connect.cursor()
        sql = "UPDATE product SET product_name=?, stockA=?, stockB=? WHERE product_id = ?;"
        cur.execute(sql, (pname, stockA, stockB, pid))
        connect.commit()
        return True
    
    except connect.Error as err:
        print('update_product_table')
        print(f'error is {err}')
        return False

    finally:
        cur.close()
        connect.close()

#---------------------- Transfer Table ---------------------------------

def select_transfer_id():
    try:
        connect = sqlite3.connect('productDB.db')
        cur = connect.cursor()
        sql = "select * from transfer ;"
        data = cur.execute(sql)
        connect.commit()

        result = False
        for row in data:
            result = row[0]
        return result

    except connect.Error as err:
        print('select_tansfer_id')
        print(f'error is {err}')

    finally:
        cur.close()
        connect.close()


def insert_transfer_table(tid, pid, pqty, type_stock):
    try:
        connect = sqlite3.connect('productDB.db')
        cur = connect.cursor()
        sql = "INSERT INTO transfer (transfer_id, product_id, product_quantity, type_stock) values(?, ?, ?, ?);"
        cur.execute(sql, (tid, pid, pqty, type_stock))
        connect.commit()

    except connect.Error as err:
        print('insert_transfer_table')
        print(f'error is {err}')
    finally:
        cur.close()
        connect.close()


def select_transfer_table(status: int):
    try:
        connect = sqlite3.connect('productDB.db')
        cur = connect.cursor()
        sql = "select tf.transfer_id, pd.product_name, tf.product_quantity from product as pd join transfer as tf using(product_id) where type_stock = ?;"
        data = cur.execute(sql, (status,)).fetchall()
        connect.commit()


        Result = namedtuple('Result', 'code name quantity')

        return map(Result._make, data), Result

    except connect.Error as err:
        print(err)
        


if __name__ == '__main__':
    create_table()