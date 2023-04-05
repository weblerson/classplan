import tomllib


class Utils:

    @staticmethod
    def read_toml(key: str, value: str) -> str:
        with open('env.toml', 'rb') as fs:
            data = tomllib.load(fs)

            return data[key][value]
