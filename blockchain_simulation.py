import hashlib
import time

class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        value_to_hash = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(value_to_hash.encode()).hexdigest()

blockchain = []

genesis_block = Block(0, "Genesis Block", "0")
blockchain.append(genesis_block)

block1 = Block(1, "Block 1 Data", genesis_block.hash)
blockchain.append(block1)

block2 = Block(2, "Block 2 Data", block1.hash)
blockchain.append(block2)

def display_chain():
    for block in blockchain:
        print("=" * 60)
        print(f" Block {block.index}")
        print("-" * 60)
        print(f" Data          : {block.data}")
        print(f" Timestamp     : {block.timestamp}")
        print(f" Previous Hash : {block.previous_hash}")
        print(f" Hash          : {block.hash}")
        print("=" * 60)
        print("        |")
        print("        V")

display_chain()

blockchain[1].data = "Hacked Block 1 Data"
blockchain[1].hash = blockchain[1].calculate_hash()

print("\n" + "#" * 70)
print(" AFTER TAMPERING BLOCK 1")
print("#" * 70 + "\n")

display_chain()

if blockchain[2].previous_hash != blockchain[1].hash:
    print("!" * 60)
    print(" ALERT : BLOCKCHAIN IS INVALID DUE TO TAMPERING")
    print("!" * 60)
else:
    print("-" * 60)
    print(" BLOCKCHAIN IS VALID")
    print("-" * 60)
