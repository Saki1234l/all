import sqlite3
import random

class Sqlite:

    def __init__(self, db_file: str) -> None:
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        self.cursor.executescript("""CREATE TABLE IF NOT EXISTS "users" (
            user_id INTEGER NOT NULL,
            username TEXT,
            referrer INTEGER NOT NULL,
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_number TEXT
            );""")

        self.cursor = self.conn.cursor()
        self.cursor.executescript("""CREATE TABLE IF NOT EXISTS "admins" (
            user_id INTEGER NOT NULL,
            username TEXT,
            referrer_admin INTEGER,
            balance INTEGER
            );""")

        self.cursor = self.conn.cursor()
        self.cursor.executescript("""CREATE TABLE IF NOT EXISTS "managers" (
            user_id INTEGER NOT NULL,
            username TEXT,
            manager_id INTEGER,
            passport_photo TEXT,
            manager_first_name TEXT,
            manager_last_name TEXT,
            referrer_admin INTEGER
            );""")

        self.cursor.executescript("""CREATE TABLE IF NOT EXISTS "deliverymans" (
            user_id INTEGER NOT NULL,
            balance   INTEGER NOT NULL DEFAULT 0,
            passport_photo TEXT,
            deliveryman_first_name TEXT,
            deliveryman_last_name TEXT,
            referrer_admin INTEGER,
            deliveryman_id INTEGER,
            username TEXT,
            user_number TEXT
            );""")

        self.cursor = self.conn.cursor()
        self.cursor.executescript("""CREATE TABLE IF NOT EXISTS "order_history" (
            order_id INTEGER,
            user_id INTEGER,
            cost INTEGER,
            delivery INTEGER,
            deliveryman_id INTEGER,
            id INTEGER,
            order_address TEXT,
            buy_date INTEGER,
            product_id INTEGER,
            status INTEGER
            );""")
        self.conn.commit()

        self.cursor = self.conn.cursor()
        self.cursor.executescript("""CREATE TABLE IF NOT EXISTS "buy_history" (
            order_id INTEGER,
            cheque_id INTEGER,
            amount INTEGER,
            delivery INTEGER,
            kaspi_number INTEGER,
            profit INTEGER
            );""")

        self.cursor = self.conn.cursor()
        self.cursor.executescript("""CREATE TABLE IF NOT EXISTS "products" (
            id INTEGER,
            price INTEGER,
            product_photos TEXT,
            in_stock INTEGER
            );""")
        self.conn.commit()

        self.cursor = self.conn.cursor()
        self.cursor.executescript("""CREATE TABLE IF NOT EXISTS "kaspi_numbers" (
            kaspi_number INTEGER
            );""")
        self.conn.commit()

    def user_in_bd(self, user_id, username, ref_id=None) -> None:
        check = self.cursor.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
        if check.fetchone() is None:
            if ref_id != None:
                self.cursor.execute('INSERT INTO "users" (user_id, username, referrer) VALUES (?, ?, ?)', (user_id, username, ref_id,))
                self.conn.commit()
            else:
                self.cursor.execute('INSERT INTO "users" (user_id, username) VALUES (?, ?)', (user_id, username,))
                self.conn.commit()
        else:
            pass

    def deliveryman_in_bd(self, user_id, username, referrer_admin, passport_photo, deliveryman_first_name, deliveryman_last_name, user_number):
        check_id = self.cursor.execute("SELECT * FROM deliverymans WHERE user_id=?", (user_id,))
        if check_id.fetchone() is None:
            while True:
                deliveryman_id = random.randint(10000, 99999)
                check_deliveryman_id = self.cursor.execute("SELECT * FROM deliverymans WHERE deliveryman_id=?", (deliveryman_id,))
                if check_deliveryman_id.fetchone() is None:
                    self.cursor.execute('INSERT INTO "deliverymans" (user_id, username, referrer_admin, passport_photo, deliveryman_first_name, deliveryman_last_name, user_number, deliveryman_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?)', (user_id, username, referrer_admin, passport_photo, deliveryman_first_name, deliveryman_last_name, user_number, deliveryman_id))
                    self.conn.commit()
                    break
                else:
                    pass
        else:
            pass

    def manager_in_bd(self, user_id, username, referrer_admin, passport_photo, manager_first_name, manager_last_name, user_number) -> None:
        check_id = self.cursor.execute("SELECT * FROM managers WHERE user_id=?", (user_id,))
        if check_id.fetchone() is None:
            while True:
                manager_id = random.randint(10000, 99999)
                check_manager_id = self.cursor.execute("SELECT * FROM managers WHERE manager_id=?", (manager_id,))
                if check_manager_id.fetchone() is None:
                    self.cursor.execute('INSERT INTO "managers" (user_id, username, referrer_admin, passport_photo, manager_first_name, manager_last_name, user_number) VALUES (?, ?, ?, ?, ?, ?, ?)', (user_id, username, referrer_admin, passport_photo, manager_first_name, manager_last_name, user_number))
                    self.conn.commit()
                    break
                else:
                    pass
        else:
            pass

    def user_in_bd(self, user_id, username, referrer_admin):
        check_id = self.cursor.execute("SELECT * FROM admins WHERE user_id=?", (user_id,))
        if check_id.fetchone() is None:
            self.cursor.execute('INSERT INTO "admins" (user_id, username, referrer_admin) VALUES (?, ?, ?)', (user_id, username, referrer_admin))
            self.conn.commit()
        else:
            pass

    def get_all_id(self) -> sqlite3.Cursor:
        users_id = self.cursor.execute("SELECT user_id FROM users")
        return users_id

    def get_all_information_user(self, user_id) -> tuple:
        id_ = self.cursor.execute("SELECT id FROM users WHERE user_id=?", (user_id, )).fetchone()[0]
        user_number = self.cursor.execute("SELECT user_number FROM users WHERE user_id=?", (user_id, )).fetchone()[0]
        return referrer, id_, user_number

    def get_all_information_deliveryman(self, user_id) -> tuple:
        referrer_admin = self.cursor.execute("SELECT referrer_admin FROM deliverymans WHERE user_id=?", (user_id, )).fetchone()[0]
        passport_photo = self.cursor.execute("SELECT passport_photo FROM deliverymans WHERE user_id=?", (user_id, )).fetchone()[0]
        deliveryman_first_name = self.cursor.execute("SELECT deliveryman_first_name FROM deliverymans WHERE user_id=?", (user_id, )).fetchone()[0]
        deliveryman_last_name = self.cursor.execute("SELECT deliveryman_last_name FROM deliverymans WHERE user_id=?", (user_id, )).fetchone()[0]
        user_number = self.cursor.execute("SELECT user_number FROM deliverymans WHERE user_id=?", (user_id, )).fetchone()[0]
        balance = self.cursor.execute("SELECT balance FROM deliverymans WHERE user_id=?", (user_id, )).fetchone()[0]
        deliveryman_id = self.cursor.execute("SELECT deliveryman_id FROM deliverymans WHERE user_id=?", (user_id, )).fetchone()[0]
        return referrer_admin, passport_photo, deliveryman_first_name, deliveryman_last_name, user_number, balance, deliveryman_id

    def get_all_information_manager(self, user_id) -> tuple:
        referrer_admin = self.cursor.execute("SELECT referrer_admin FROM managers WHERE user_id=?", (user_id, )).fetchone()[0]
        passport_photo = self.cursor.execute("SELECT passport_photo FROM managers WHERE user_id=?", (user_id, )).fetchone()[0]
        manager_first_name = self.cursor.execute("SELECT manager_first_name FROM managers WHERE user_id=?", (user_id, )).fetchone()[0]
        manager_last_name = self.cursor.execute("SELECT manager_last_name FROM managers WHERE user_id=?", (user_id, )).fetchone()[0]
        user_number = self.cursor.execute("SELECT user_number FROM managers WHERE user_id=?", (user_id, )).fetchone()[0]
        manager_id = self.cursor.execute("SELECT manager_id FROM managers WHERE user_id=?", (user_id, )).fetchone()[0]
        return referrer_admin, passport_photo, manager_first_name, manager_last_name, user_number, manager_id

    def get_all_information_admin(self, user_id) -> tuple:
        username = self.cursor.execute("SELECT username FROM admins WHERE user_id=?", (user_id, )).fetchone()[0]
        referrer_admin = self.cursor.execute("SELECT referrer_admin FROM admins WHERE user_id=?", (user_id, )).fetchone()[0]
        user_number = self.cursor.execute("SELECT user_number FROM users WHERE user_id=?", (user_id, )).fetchone()[0]
        balance = self.cursor.execute("SELECT balance FROM users WHERE user_id=?", (user_id, )).fetchone()[0]
        return referrer, referrer_admin, user_number, balance

    def add_balance(self, name, amount, id_):
        with self.conn:
            self.cursor.execute(f'UPDATE users SET {name} = {name} + ? WHERE user_id = ?', (amount, id_,))
            self.conn.commit()

    def set_summ(self, amount, id_):
        with self.conn:
            self.cursor.execute('UPDATE users SET summ = ? WHERE user_id = ?', (amount, id_,))
            self.conn.commit()

    def minus_balance(self, name, amount, id_):
        with self.conn:
            self.cursor.execute(f'UPDATE users SET {name} = {name} - ? WHERE user_id = ?', (amount, id_,))
            self.conn.commit()

    def edit_bd(self,bd, id_):
        with self.conn:
            self.cursor.execute('UPDATE users SET bd = ? WHERE user_id = ?', (bd, id_,))
            self.conn.commit()

    def get_bd(self, id_):
        with self.conn:
            billid = self.cursor.execute('SELECT bd FROM users WHERE user_id = ?', (id_,)).fetchone()[0]
            return billid

    def edit_numb(self,numb, id_):
        with self.conn:
            self.cursor.execute('UPDATE users SET numb = ? WHERE user_id = ?', (numb, id_,))
            self.conn.commit()
    
    def get_ref(self, id_):
        with self.conn:
            res = self.cursor.execute('SELECT referrer FROM users WHERE user_id = ?', (id_,)).fetchone()[0]
            return res

    def payment1(self, userid, messageid, cash_, coment_, id_):
        with self.conn:
            self.cursor.execute('INSERT INTO "payments" (user_id, message_id, cash, coment, id) VALUES (?, ?, ?, ?, ?)', (userid, messageid, cash_, coment_, id_,))
            self.conn.commit()

    def payment2(self, userid, messageid):
        with self.conn:
            answer = self.cursor.execute("SELECT * FROM users WHERE (user_id, message_id) VALUES (?, ?), (userid, messageid,)").fetchone()[0]
            return answer