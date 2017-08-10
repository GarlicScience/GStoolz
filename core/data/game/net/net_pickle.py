from core.database.game.contracts_service import ContractsService
from core.database.game.build_service import BuildService
from core.data.game.net.contract import Contract, ContractConnection
from core.data.game.net.build import Build
import pickle
from res.values import strings as _str


class NetPickle:

    @classmethod
    def download_n_save(cls):

        contract_net_node_pool, contract_net_connect_pool, contract_frame, mes1 = cls.download_contract_pools()
        build_net_node_pool, build_frame, mes2 = cls.download_build_pool()

        if mes1 == _str.DB_CON_OK_MESSAGE and mes2 == _str.DB_CON_OK_MESSAGE:
            # Pickle saving of gotten pools

            with open(_str.DUMP_CONTRACTS_NET_NODE_PATH, 'wb') as output:
                pickle.dump(contract_net_node_pool, output, pickle.HIGHEST_PROTOCOL)

            with open(_str.DUMP_CONTRACTS_NET_CONNECT_PATH, 'wb') as output:
                pickle.dump(contract_net_connect_pool, output, pickle.HIGHEST_PROTOCOL)

            with open(_str.DUMP_BUILD_NET_NODE_PATH, 'wb') as output:
                pickle.dump(build_net_node_pool, output, pickle.HIGHEST_PROTOCOL)

            # Saving DataFrames

            with open(_str.DUMP_CONTRACTS_DATA_FRAME, 'wb') as output:
                pickle.dump(contract_frame, output, pickle.HIGHEST_PROTOCOL)

            with open(_str.DUMP_BUILDS_DATA_FRAME, 'wb') as output:
                pickle.dump(build_frame, output, pickle.HIGHEST_PROTOCOL)

        else:
            return mes1 if mes1 != _str.DB_CON_OK_MESSAGE else mes2

        return _str.NET_PICKLE_DOWNLOAD_N_SAVE_OK

    @classmethod
    def load(cls):

        try:
            with open(_str.DUMP_CONTRACTS_NET_NODE_PATH, 'rb') as file:
                contract_net_node_pool = pickle.load(file)
        except IOError as err:
            return [], [], [], str(err)

        try:
            with open(_str.DUMP_CONTRACTS_NET_CONNECT_PATH, 'rb') as file:
                contract_net_connect_pool = pickle.load(file)
        except IOError as err:
            return [], [], [], str(err)

        try:
            with open(_str.DUMP_BUILD_NET_NODE_PATH, 'rb') as file:
                build_net_node_pool = pickle.load(file)
        except IOError as err:
            return [], [], [], str(err)

        return contract_net_node_pool, contract_net_connect_pool, build_net_node_pool, _str.NET_PICKLE_LOAD_OK

    @classmethod
    def load_as_frames(cls):

        try:
            with open(_str.DUMP_CONTRACTS_DATA_FRAME, 'rb') as file:
                contract_frame = pickle.load(file)
        except IOError as err:
            return None, None, str(err)

        try:
            with open(_str.DUMP_BUILDS_DATA_FRAME, 'rb') as file:
                build_frame = pickle.load(file)
        except IOError as err:
            return None, None, str(err)

        return contract_frame, build_frame, _str.NET_PICKLE_LOAD_OK

    @classmethod
    def download_contract_pools(cls):

        contracts_frame, mes = ContractsService.load_table()
        contract_net_node_pool = []
        contract_net_connect_pool = []

        if mes == _str.DB_CON_OK_MESSAGE:
            # Filling pool of contract nodes and contract interconnections

            for row in contracts_frame.itertuples():
                contract = Contract(id_=row[1], name=row[2], time=row[3], recovery_time=row[4], type_=row[5],
                                    amount=row[6], max_amount=cls.__parse_max_amount(row[7]),
                                    donate_cost=row[8], sell_cost=row[9], img=row[10], req_lvl=row[11],
                                    exp_rew=row[12],
                                    rand_rew=eval(row[13]) if row[13] else row[13],
                                    req_bld=None, allows_to=[])
                contract_net_node_pool.append(contract)
                if row[14]:
                    for connect in cls.__parse_connections(row[1], row[14]):
                        contract_net_connect_pool.append(connect)
        return contract_net_node_pool, contract_net_connect_pool, contracts_frame, mes

    @classmethod
    def download_build_pool(cls):

        build_frame, mes = BuildService.load_table()
        build_net_node_pool = []

        if mes == _str.DB_CON_OK_MESSAGE:
            # Filling pool of building nodes and filling gaps in contract nodes

            for row in build_frame.itertuples():
                build = Build(id_=row[1], name=eval(row[2]), time=eval(row[3]), turn_expansion=eval(row[4]),
                              skip_cost=eval(row[5]), price=eval(row[6]), type_=row[7], req_lvl=eval(row[8]),
                              exp_rew=eval(row[9]), max_amount=cls.__parse_max_amount(row[10]), contracts=eval(row[11]))
                build_net_node_pool.append(build)

                # TODO: Don't forget to provide a work with < req_bld >

        return build_net_node_pool, build_frame, mes

    @classmethod
    def __parse_connections(cls, id_, row):
        row = eval(row)
        result = []
        for connection in row:
            result.append(ContractConnection(id_from=int(connection['id']),
                                             amount=int(connection['amount']),
                                             id_=int(id_)))
        return result

    @classmethod
    def __parse_max_amount(cls, row):
        if row:
            row = eval(row)
            result = dict()
            for level in row:
                result[level['plvl']] = int(level['amount'])
            return result
        else:
            return row

