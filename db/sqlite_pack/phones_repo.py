from db.sqlite_pack._base_db_connector import BaseDbConnection


class PhonesRepo:

    def __init__(self, db_params):
        self._db = BaseDbConnection(db_params)
        self._table_name = "PHONES"

    def get_all(self):
        res = self._db.cursor.execute(f"SELECT * FROM {self._table_name}")
        return res.fetchall()

    def get_max_phone_id(self):
        max_phone_id = self._db.cursor.execute("SELECT MAX(ID) FROM PHONES;").fetchone()[0]
        return max_phone_id

    def get_all_brands(self):
        try:
            query = f"SELECT DISTINCT BRAND FROM {self._table_name}"
            result = self._db.cursor.execute(query)
            brands = [row[0] for row in result.fetchall()]
            updated_brands = list(set(brands))
            return updated_brands
        except Exception as error:
            print(f"Can`t find brands: {error}")

    def get_all_id(self):
        try:
            query = f"SELECT DISTINCT ID FROM {self._table_name}"
            result = self._db.cursor.execute(query)
            ids = [row[0] for row in result.fetchall()]
            return ids
        except Exception as error:
            print(f"Can`t find id: {error}")

    def get_phone_by_brand(self, brand: str):
        try:
            brands = self.get_all_brands()
            if brand in brands:
                res = self._db.cursor.execute(f"SELECT * FROM {self._table_name} WHERE BRAND='{brand}'")
                brand_phones = res.fetchall()
                return brand_phones
            else:
                raise ValueError()

        except Exception as error:
            print(f"Brand {brand} is not correct: {error}")

    def get_one_by_id(self, phone_id=None):
        phone_id = self.get_max_phone_id() if phone_id is None else phone_id
        res = self._db.cursor.execute(f"SELECT * FROM {self._table_name} WHERE id={phone_id}")
        phone_data = res.fetchone()
        return phone_data

    def insert_one(self, model: str, brand: str, processor: str, year: int, price: float):
        query_insert = f'''
            INSERT INTO {self._table_name} (MODEL, BRAND, PROCESSOR, YEAR, PRICE)
            VALUES (?, ?, ?, ?, ?);
        '''
        values = (model, brand, processor, year, price)
        self._db.cursor.execute(query_insert, values)
        self._db.conn.commit()

    def update_full_phone(self, model: str, brand: str, processor: str, year: int, price: float, phone_id=None):
        query_update = f'''
                    UPDATE {self._table_name}
                    SET MODEL = ?, BRAND = ?, PROCESSOR = ?, YEAR = ?, PRICE = ?
                    WHERE ID = ?;
                '''
        phone_id = self.get_max_phone_id() if phone_id is None else phone_id

        values = (model, brand, processor, year, price, phone_id)
        self._db.cursor.execute(query_update, values)  # Пишу таким чином, адже це як "захист" даних
        self._db.conn.commit()

    def partial_phone_update(self, phone_id=None, model=None, brand=None, processor=None, year=None, price=None):
        fields_to_update = []
        if model is not None:
            fields_to_update.append(f"MODEL = '{model}'")
        elif brand is not None:
            fields_to_update.append(f"BRAND = '{brand}'")
        elif processor is not None:
            fields_to_update.append(f"PROCESSOR = '{processor}'")
        elif year is not None:
            fields_to_update.append(f"YEAR = {year}")
        elif price is not None:
            fields_to_update.append(f"PRICE = {price}")

        query_update = f'''
                    UPDATE {self._table_name}
                    SET {', '.join(fields_to_update)}
                    WHERE ID = ?;
                '''
        phone_id = self.get_max_phone_id() if phone_id is None else phone_id

        values = (phone_id,)
        self._db.cursor.execute(query_update, values)
        self._db.conn.commit()

    def delete_phone_by_id(self, phone_id=None):
        phone_id = self.get_max_phone_id() if phone_id is None else phone_id
        try:
            id_list = self.get_all_id()

            if not isinstance(phone_id, int):
                raise ValueError("Invalid phone_id. Must be an integer.")

            if phone_id in id_list:
                query_delete = f"DELETE FROM {self._table_name} WHERE ID = ?"
                self._db.cursor.execute(query_delete, (phone_id,))
                self._db.conn.commit()
                print(f"Phone with ID {phone_id} deleted successfully.")

        except ValueError as e:
            print(e)
        except Exception as error:
            print(f"Error deleting phone with ID {phone_id}: {error}")

    def __del__(self):
        self._db.cursor.close()
        self._db.conn.close()
