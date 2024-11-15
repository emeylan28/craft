import mysql.connector
from config import USER, PASSWORD, HOST, PORT


class DbConnectionError(Exception):
    pass

def _connect_to_db(db_name):
    cnx = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=db_name,
        port=PORT
    )
    return cnx

def find_all_crafts(activity_or_item):
    try:
        db_name = "crafts"
        db_connect = _connect_to_db(db_name)
        cur = db_connect.cursor()

        table_name = activity_or_item

        print(f"Connected to the database: {db_name}")

        query = f"""SELECT * FROM {table_name};"""

        cur.execute(query)
        result = cur.fetchall()

        return result

        cur.close()

    except Exception:
        raise DbConnectionError("Failed to connect to the database")

    finally:
        if db_connect:
            db_connect.close()
            print("Connection closed")
        else:
            print("No connection to close")


def find_craft_activity(craft_activity):
    try:
        db_name = "crafts"
        db_connect = _connect_to_db(db_name)
        cur = db_connect.cursor()
        db_table_name = craft_activity

        print(f"Connected to the database: {db_name}")

        query = f"""SELECT item, item_type FROM {db_table_name};"""

        cur.execute(query)
        result = cur.fetchall()

        result_string = ""
        for i in result:
            result_string = result_string + i[0] + ": " + i[1] + ", "

        result_string = result_string[:-2]

        craft_activity = craft_activity.replace("_", " ")

        craft_string = f"You will need the following for {craft_activity}: {result_string}"

        print(craft_string)
        return craft_string

        cur.close()

    except Exception:
        raise DbConnectionError("Failed to connect to the database")

    finally:
        if db_connect:
            db_connect.close()
            print("Connection closed")
        else:
            print("No connection to close")

def all_craft_items():
    try:
        db_name = "crafts"
        db_connect = _connect_to_db(db_name)
        cur = db_connect.cursor()

        print(f"Connected to the database: {db_name}")

        query = f"""SELECT * FROM craft_items;"""

        cur.execute(query)
        result = cur.fetchall()

        print(result)
        return result

        cur.close()

    except Exception:
        raise DbConnectionError("Failed to connect to the database")

    finally:
        if db_connect:
            db_connect.close()
            print("Connection closed")
        else:
            print("No connection to close")

def find_crafty_item(craft_item):
    try:
        if craft_item == "wool":
            column_names = "item_type, material, colour, weight_g, item_use"
            table_name = "wool"
        elif craft_item == "thread":
            column_names = "item,item_type, colour"
            table_name = "thread"
        elif craft_item == "paper":
            column_names = "item_size, colour, weight_gsm"
            table_name = "paper"
        elif craft_item == "card":
            column_names = "item_size, colour, weight_gsm"
            table_name = "card"
        elif craft_item == "fabric":
            column_names = "item_type, pattern, colour, item_use"
            table_name = "fabric"
        elif craft_item == "hand sewing needle":
            column_names = "item_type"
            table_name = "hand_sewing_needle"
        elif craft_item == "knitting needle":
            column_names = "item_type,size_mm, item_use"
            table_name = "knitting_needle"
        elif craft_item == "machine sewing needle":
            column_names = "item_type"
            table_name = "machine_sewing_needle"
        else:
            column_names = "item_type, colour, item_use"
            table_name = "other"

        query = f"""SELECT {column_names} FROM {table_name} WHERE item = '{craft_item}'"""

        db_name = "crafts"
        db_connect = _connect_to_db(db_name)
        cur = db_connect.cursor()

        print(f"Connected to the database: {db_name}")

        cur.execute(query)
        result = cur.fetchall()

        if "_" in craft_item:
            craft_item.replace("_", " ")
            return craft_item

        item_string = f"Here are the {column_names.replace("_", " ")} we have for {craft_item.replace("_", " ")}."
        craft_item_string = str(item_string + "\n" + "")

        for i in result:
            craft_item_string = craft_item_string + str(i) + "\n"

        print(craft_item_string)

        return craft_item_string

        cur.close()


    except Exception:
        raise DbConnectionError("Failed to connect to the database")

    finally:
        if db_connect:
            db_connect.close()
            print("Connection closed")
        else:
            print("No connection to close")

def add_new_craft(new_craft):
    try:
        db_name = 'crafts'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print(f"Connected to DB: {db_name}")

        query = f"""
            INSERT INTO craft_type 
                (craft)
            VALUES
                ("{new_craft}");
            """

        print(f"{new_craft} has been added to craft_type table.")
        cur.execute(query)
        db_connection.commit()
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")


def create_new_craft_table(new_craft):
    try:
        db_name = 'crafts'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print(f"Connected to DB: {db_name}")

        new_craft = (new_craft.lower()).replace(" ", "_")

        query1 = f"""
            CREATE TABLE {new_craft} 
                (item VARCHAR(50) NOT NULL, item_type VARCHAR(50) DEFAULT 'Your choice');
            """

        print(f"{new_craft} table has been created.")

        cur.execute(query1)
        db_connection.commit()
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")


def new_craft_table_data(craft_list):
    try:
        db_name = 'crafts'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print(f"Connected to DB: {db_name}")

        print(craft_list)

        craft = craft_list[0]
        item = craft_list[1]
        item_type = craft_list[2]

        craft = (craft.lower()).replace(" ", "_")

        query = f"""
            INSERT INTO {craft} 
                (item, item_type)
            VALUES
                ("{item}", "{item_type}");
            """

        print(f"{craft} table has been added to.")

        cur.execute(query)
        db_connection.commit()
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

def item_id_finding(craft_item):
    try:
        db_name = "crafts"
        db_connect = _connect_to_db(db_name)
        cur = db_connect.cursor()

        if craft_item == "wool":
            db_table_name = "wool"
        elif craft_item == "thread":
            db_table_name = "thread"
        elif craft_item == "card":
            db_table_name = "card"
        elif craft_item == "paper":
            db_table_name = "paper"
        elif craft_item == "hand_sewing_needle":
            db_table_name = "hand_sewing_needle"
        elif craft_item == "machine_sewing_needle":
            db_table_name = "machine_sewing_needle"
        elif craft_item == "knitting_needle":
            db_table_name = "knitting_needle"
        elif craft_item == "fabric":
            db_table_name = "fabric"
        else:
            db_table_name = "other"

        print(f"Connected to the database: {db_name}")

        query = f"""SELECT item_id FROM {db_table_name} ORDER BY item_id DESC;"""

        cur.execute(query)
        result = cur.fetchone()
        result = str(result)
        result = int(((result.replace("(", "")).replace(",", "")).replace(")", ""))

        print(result)

        return result

        cur.close()

    except Exception:
        raise DbConnectionError("Failed to connect to the database")

    finally:
        if db_connect:
            db_connect.close()
            print("Connection closed")
        else:
            print("No connection to close")

def add_to_existing_craft_item(craft_and_info):
    try:
        db_name = "crafts"
        db_connect = _connect_to_db(db_name)
        cur = db_connect.cursor()

        craft = str((craft_and_info[0]).lower())
        print(craft)
        info = str(craft_and_info[1:])
        info = (info.replace("[", "")).replace("]", "")
        print(info)

        print(f"Connected to the database: {db_name}")
        values = info.title()

        if craft == "wool":
            column_names = "item, item_type, material, colour, weight_g, item_use"
            table_name = "wool"
            item_id = item_id_finding("wool") + 1
            item = craft
        elif craft == "thread":
            column_names = "item, item_type, colour"
            table_name = "thread"
            item_id = item_id_finding("thread") + 1
            item = craft
        elif craft == "paper":
            column_names = "item, item_size, colour, weight_gsm"
            table_name = "paper"
            item_id = item_id_finding("paper") + 1
            item = craft
        elif craft == "card":
            column_names = "item, item_size, colour, weight_gsm"
            table_name = "card"
            item_id = item_id_finding("card") + 1
            item = craft
        elif craft == "fabric":
            column_names = "item, item_type, pattern, colour, item_use"
            table_name = "fabric"
            item_id = item_id_finding("fabric") + 1
            item = craft
        elif craft == "hand sewing needle":
            column_names = "item, item_type"
            table_name = "hand_sewing_needle"
            item_id = item_id_finding("hand_sewing_needle") + 1
            item = craft
        elif craft == "knitting needle":
            column_names = "item, item_type, size_mm, item_use"
            table_name = "knitting_needle"
            item_id = item_id_finding("knitting_needle") + 1
            item = craft
        elif craft == "machine sewing needle":
            column_names = "item, item_type"
            table_name = "machine_sewing_needle"
            item_id = item_id_finding("machine_sewing_needle") + 1
            item = craft
        else:
            column_names = "item, item_type, colour, item_use"
            table_name = "other"
            item_id = item_id_finding("other") + 1
            item = craft

        print(table_name, column_names, item_id, values)

        query = f"""INSERT INTO {table_name}
            (item_id, {column_names})
            VALUES
            ({item_id}, '{item.title()}', {values});"""

        print(query)

        cur.execute(query)
        db_connect.commit()

        print("New craft item inserted")

        cur.close()

    except Exception:
        raise DbConnectionError("Failed to connect to the database")

    finally:
        if db_connect:
            db_connect.close()
            print("Connection closed")
        else:
            print("No connection to close")


def add_new_craft_item(new_craft_item):
    try:
        db_name = 'crafts'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print(f"Connected to DB: {db_name}")

        if new_craft_item == "wool":
            db_table_name = "wool"
        elif new_craft_item == "thread":
            db_table_name = "thread"
        elif new_craft_item == "card":
            db_table_name = "card"
        elif new_craft_item == "paper":
            db_table_name = "paper"
        elif new_craft_item == "hand_sewing_needle":
            db_table_name = "hand_sewing_needle"
        elif new_craft_item == "machine_sewing_needle":
            db_table_name = "machine_sewing_needle"
        elif new_craft_item == "knitting_needle":
            db_table_name = "knitting_needle"
        elif new_craft_item == "fabric":
            db_table_name = "fabric"
        else:
            db_table_name = "other"


        query = f"""
            INSERT INTO craft_items 
                (item, _table_name)
            VALUES
                ("{new_craft_item}", "{db_table_name}");
            """

        print(query)

        print(f"{new_craft_item} has been added to craft_item table.")
        cur.execute(query)
        db_connection.commit()
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")



list_of_craft = ["crochet", "wool", "your choice"]
crafty_info = ["wool", "chunky", "100% wool", "Rose gold", 100, "Crochet"]

if __name__ == "__main__":
    #find_all_crafts("craft_items")
    find_craft_activity("Embroidery")
    #all_craft_items()
    # find_crafty_item("fabric")
    #add_new_craft("crochet")
    #create_new_craft_table("crochet")
    #new_craft_table_data(list_of_craft)
    #item_id_finding("wool")
    #add_to_existing_craft_item(crafty_info)
    #add_new_craft_item("Clay")

