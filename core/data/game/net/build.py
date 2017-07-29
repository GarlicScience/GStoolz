class Build:

    def __init__(self, id_, name, req_lvl, time, turn_expansion,
                 skip_cost, price, type_, exp_rew, max_amount, contracts):
        self.id = id_
        self.name_list = name
        self.req_lvl = req_lvl
        self.time = time
        self.turn_expansion = turn_expansion
        self.skip_cost = skip_cost
        self.price = price
        self.type = type_
        self.exp_rew = exp_rew
        self.max_amount = max_amount
        self.contracts = contracts

    def __str__(self):
        return '<B id:{} | {} B>'.format(self.id, list(self.name_list.values()))

    def __repr__(self):
        return self.__str__()