import json


class Block:
    def __init__(self, hash_prev_block, transactions, nonce):
        self.hash_pref_block = hash_prev_block
        self.transaction = transactions #TODO
        self.nonce = nonce
    def get_hash(self):
        data = self.get_dict()
        json_data = json.dumps(data)
        return hashing.hash(json_data) #TODO
    def get_dict(self):
        transaction_hash_list = []
        for i in self.transactions:
            transaction_hash_list.append(i.get_hash()) #TODO
        return {
            "transaction_hashes": transaction_hash_list,
            "hash_previous_block": self.hash_pref_block,
            "nonce": self.nonce
        }