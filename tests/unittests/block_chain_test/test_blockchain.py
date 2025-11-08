import unittest

from blockchain.main import Blockchain


class TestBlockChain(unittest.TestCase):
    def test_add_block(self) -> None:
        block_chain = Blockchain()
        block_chain.add_block("sender", "receiver", 50)
        self.assertEqual(len(block_chain.transactions), 2)

    def test_is_valid(self) -> None:
        block_chain = Blockchain()
        block_chain.add_block("sender", "receiver", 50)
        block_chain.add_block("receiver", "sender", 25)
        self.assertTrue(block_chain.is_valid())

    def test_tampering_detection(self) -> None:
        block_chain = Blockchain()
        block_chain.add_block("sender", "receiver", 50)
        block_chain.add_block("receiver", "sender", 25)
        block_chain.transactions[1].amount = 999  # Tamper with transaction
        self.assertFalse(block_chain.is_valid())

    def test_long_transaction_chain(self) -> None:
        block_chain = Blockchain()
        for _ in range(100):
            block_chain.add_block("sender", "receiver", 1)
            block_chain.add_block("receiver", "sender", 1)

        self.assertTrue(block_chain.is_valid())
