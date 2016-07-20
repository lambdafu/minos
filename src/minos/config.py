import six
import os
import toml
from attrdict import AttrDict

DEFAULT_INPUT = '''
[neo4j]
address = "bold://localhost"
'''

DEFAULT = toml.loads(DEFAULT_INPUT)


class Config(AttrDict):
    def __init__(self, *args, **kwargs):
        super(Config, self).__init__(*args, **kwargs)

    @classmethod
    def fromstring(cls, data):
        cfg = cls()
        cfg.update(DEFAULT)

        config = toml.loads(data)
        cfg.update(config)

        return cfg

    @classmethod
    def parse(cls, fh):
        data = fh.readlines()
        return cls.fromstring("\n".join(data))

    def dumps(self):
        return toml.dumps(self)


