from core.database import general as gen
from res.values import strings as _str
import pandas as pd


class BuildService:

    @classmethod
    def load_table(cls):
        database, mes = gen.connect()

        if mes == _str.DB_CON_OK_MESSAGE:
            with database as cursor:
                cursor.execute("""
                            SELECT id,
                                   name,
                                   time_building,
                                   amount_turn,
                                   cost_skip_build, 
                                   price,
                                   type,
                                   needs_lvl,
                                   get_exp,
                                   max_amount,
                                   contracts
                            FROM Build
                            WHERE version_app <= (
                                                  SELECT version_app
                                                  FROM Systems
                                                  LIMIT 1
                                                )
                            """)
                data = [list(row) for row in cursor.fetchall()]
                columns = [column[0] for column in cursor.description]

            return pd.DataFrame(data,columns=columns), mes
        return None, mes

  #  @classmethod
  #  def 