# All original packets will have this format
# [Continue or End Flag][Packet id][Packet args]
# all continuation packets will have this structure
# [Continue or End Flag][Packet args]


class Packet:

    def __init__(self):
        self.eos = True

    def bytes(self):
        pass


def from_str(stream: str):
    print(str)
