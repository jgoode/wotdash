import json


class PlayerQuery:
    status = ""
    count = 0
    nickname = ""
    account_id = 0

    def __init__(self, query):
        self.query = query
        j = json.loads(query)
        self.status = j['status']
        if self.status == 'ok':
            self.count = j['meta']['count']
            r = j['data'][0]
            self.nickname = r['nickname']
            self.account_id = r['account_id']

    def to_string(self):
        st = """
        status = %s
        count = %d
        nickname = %s
        account_id = %d
        """ % (self.status, self.count, self.nickname, self.account_id)

        return st




