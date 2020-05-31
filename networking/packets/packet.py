# All original packets will have this format
# [Continue or End Flag][Packet id][Packet args]
# all continuation packets will have this structure
# [Continue or End Flag][Packet args]


class Packet:
    CONTINUE_FLAG = 'C'
    END_FLAG = 'E'

    def __init__(self):
        self.eos = True

    def bytes(self):
        pass


def from_str(stream: str):
    print(str)


def continues(stream: str) -> bool:
    if stream[0] == Packet.CONTINUE_FLAG:
        return True
    elif stream[0] != Packet.END_FLAG:
        raise ValueError()


def reconstruct(stream: str, new_bytes: str):
    stream += new_bytes[4:len(new_bytes)]
