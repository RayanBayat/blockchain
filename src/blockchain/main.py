import hashlib
import logging
import time

LOGGER = logging.getLogger()
logging.basicConfig(level=logging.INFO)


class Block:
    def __init__(self, sender: str, receiver: str, amount: int, prev_hash: str = "0") -> None:
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.timestamp = time.time()
        self.prev_hash = prev_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        return hashlib.sha256(
            (f"{self.sender}{self.receiver}{self.amount}{self.timestamp}{self.prev_hash}").encode()
        ).hexdigest()


class Blockchain:
    def __init__(self) -> None:
        self.transactions = [Block("0", "0", 0)]

    def add_block(self, sender, receiver, amount) -> None:
        self.transactions.append(Block(sender, receiver, amount, self.transactions[-1].hash))
        LOGGER.info(f"Block added: {self.transactions[-1].hash}, {sender} -> {receiver}, Amount: {amount}")

    def is_valid(self) -> bool:
        for i in range(len(self.transactions) - 1, 0, -1):
            if (
                self.transactions[i].prev_hash != self.transactions[i - 1].hash
                or self.transactions[i].hash != self.transactions[i].calculate_hash()
            ):
                return False
        return True
