class HashTable:
    def __init__(self, size=2069):
        self.table = [[] for i in range(size)]
        self.size = size

    def find_pair_in_bucket(self, bucket, key):
        for pair in bucket:
            if pair[0] == key:
                return pair
        return False

    def add_hashed_value(self, key, value=0):
        index = self.get_hash_value(key)
        bucket = self.table[index]
        pair = self.find_pair_in_bucket(bucket, key)
        if pair is False:
            bucket.append([key, value])
        elif pair[1] != value:
            pair[1] = value

    def get_value(self, key):
        index = self.get_hash_value(key)
        bucket = self.table[index]
        pair = self.find_pair_in_bucket(bucket, key)
        if pair is not False:
            return pair[1]
        return key + ' not in table'

    def delete_key(self, key):
        index = self.get_hash_value(key)
        bucket = self.table[index]
        pair = self.find_pair_in_bucket(bucket, key)
        if pair is not False:
            bucket.remove(pair)

    def get_hash_value(self, string):
        string = str(string)
        index = 1
        hash_num = 0
        temp = 0
        for ind_char in string:
            temp += (ord(ind_char) * index)
            index += 1
        hash_num += temp % self.size
        return hash_num
