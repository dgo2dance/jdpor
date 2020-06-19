#  基于redis的存储


import hashlib
import six

class BaseFilter(object):


    def __init__(self,
                 hash_func_name="md5",
                 redis_host='localhost',
                 redis_port=6379,
                 redis_db=0,
                 redis_key='boss',

                 ):
        self.redis_host = redis_host
        self.redis_port = redis_port
        self.redis_db = redis_db
        self.redis_key = redis_key


        self.hash_func = getattr(hashlib, hash_func_name)   #md5压缩
        self.storage = self._get_storage()

    def _get_storage(self):

        pass

    def _safe_data(self, data):
        if six.PY3:
            if isinstance(data, bytes):
                return data
            elif isinstance(data, str):
                return data.encode()
            else:
                raise Exception('请提供一个字符串')
        else:
            if isinstance(data, str):
                return data
            elif isinstance(data, unicode):
                return data.encode()
            else:
                raise Exception('请提供一个字符串')

    def _get_hash_value(self, data):

        hash_obj = self.hash_func()
        hash_obj.update(self._safe_data(data))
        hash_value = hash_obj.hexdigest()
        # print('MD5: ',hash_value)
        return hash_value

    def save(self, data):

        hash_value = self._get_hash_value(data)
        return self._save(hash_value)

    def _save(self, hash_value):

        pass

    def is_exists(self, data):

        hash_value = self._get_hash_value(data)
        return self._is_exists(hash_value)

    def _is_exists(self, hash_value):

        pass
