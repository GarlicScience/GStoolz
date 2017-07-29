class Contract:

    def __init__(self, id_, name, time, recovery_time, type_, amount, max_amount,
                 donate_cost, sell_cost, img, req_lvl, exp_rew, rand_rew, req_bld, allows_to):
        self.id = id_
        self.name = name
        self.recovery_time = recovery_time
        self.time = time
        self.type = type_
        self.amount = amount
        self.max_amount = max_amount
        self.donate_cost = donate_cost
        self.sell_cost = sell_cost
        self.img = img
        self.req_lvl = req_lvl
        self.exp_rew = exp_rew
        self.rand_rew = rand_rew
        self.req_bld = req_bld
        self.allows_to = allows_to

    def __str__(self):
        return '< id:{} | {} >'.format(self.id, self.name)

    def __repr__(self):
        return str(self)


class ContractConnection:

    def __init__(self, id_, id_from, amount):
        self.id = id_
        self.amount = amount
        self.id_from = id_from

    def __str__(self):
        return '~< from:{} | {} | to:{} >~'.format(self.id_from, self.amount, self.id)

    def __repr__(self):
        return str(self)