from core.database import general as gen
from res.values import strings as _str
import pandas as pd


class ContractsService:

    @classmethod
    def load_table(cls):
        database, mes = gen.connect()

        if mes == _str.DB_CON_OK_MESSAGE:
            with database as cursor:
                cursor.execute("""
                            SELECT id,
                                   name,
                                   time,
                                   recovery_time,
                                   type,
                                   amount,
                                   max_amount,
                                   donate_cost_for_one,
                                   sell_cost_for_one,
                                   img_source,
                                   needs_lvl,
                                   get_exp,
                                   random_rewards,
                                   needs_contracts
                            FROM Contracts
                            WHERE version_app <= (
                                                  SELECT version_app
                                                  FROM Systems
                                                  LIMIT 1
                                                )
                            """)
                data = [list(row) for row in cursor.fetchall()]
                columns = [column[0] for column in cursor.description]

            return pd.DataFrame(data, columns=columns), mes
        return None, mes

