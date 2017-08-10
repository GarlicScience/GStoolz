from openpyxl import Workbook
from openpyxl.utils import FORMULAE as form
from openpyxl.drawing.image import Image
from core.data.pickle_to_xl import PickleToXL as ptx
from core.data.game.net.net_pickle import NetPickle
# NetPickle.download_n_save()
import pandas as pd
ptx.make_excel()
# b = pd.DataFrame(data=[[1, 2, 3], [0, 1, 2], [-1, 0, 1]], columns=['a', 'b', 'c'])
# b = b[b['a'] != 0]
# b = b.reset_index()
# del b['index']
# print(b['a'][1])
# print(b.head())
# print(form)

# ROUND('Prices + bundles'!B5, 5)
# *
# ROUND(120, 5)
# +
#   (
#     ROUND('Prices + bundles'!Q2, 5)
#     *
#     ROUND(7, 5)
#   )
# +
#   (
#     ROUND('Base contracts'!, 5)
#     *
#     ROUND(1, 5)
#   )
# +
#   (
#     ROUND('Base contracts'!, 5)
#     *
#     ROUND(1, 5)
#   )