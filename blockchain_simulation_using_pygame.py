#first install pygame by pip install pygame
#3 blocks drawn side-by-side as colored rectangles
#Green = valid
#Red = invalid (when chain breaks)
#Lines connect them like a chain

#Press Spacebar to tamper Block 1’s data — its color turns red, and chain breaks

#Message displays if blockchain is invalid

#Clean, interactive visual simulation


import hashlib
import time
import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 900, 600
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
RED = (255, 100, 100)
GREEN = (100, 255, 100)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blockchain Simulation")

font = pygame.font.SysFont('Arial', 16)
big_font = pygame.font.SysFont('Arial', 36)

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

def draw_block(x, y, block, valid=True):
    color = GREEN if valid else RED
    pygame.draw.rect(screen, color, (x, y, 250, 100))
    pygame.draw.rect(screen, BLACK, (x, y, 250, 100), 2)

    text_lines = [
        f"Block {block.index}",
        f"Data: {block.data}",
        f"Hash: {block.hash[:10]}...",
        f"Prev: {block.previous_hash[:10]}..."
    ]
    for i, line in enumerate(text_lines):
        txt_surf = font.render(line, True, BLACK)
        screen.blit(txt_surf, (x + 10, y + 5 + i * 20))

def check_validity():
    for i in range(1, len(blockchain)):
        if blockchain[i].previous_hash != blockchain[i-1].hash:
            return False
    return True

def draw_chain():
    screen.fill(WHITE)
    validity = check_validity()

    positions = [(50, 100), (325, 100), (600, 100)]
    for i, (x, y) in enumerate(positions):
        valid = True
        if i > 0 and blockchain[i].previous_hash != blockchain[i-1].hash:
            valid = False
        draw_block(x, y, blockchain[i], valid)
        if i < 2:
            pygame.draw.line(screen, BLACK, (x+250, y+50), (x+325, y+50), 3)

    if not validity:
        alert = big_font.render("BLOCKCHAIN INVALID!", True, RED)
        screen.blit(alert, (WIDTH//2 - alert.get_width()//2, 250))

    pygame.display.flip()

tamper = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not tamper:
                    blockchain[1].data = "Hacked Data"
                    blockchain[1].hash = blockchain[1].calculate_hash()
                    tamper = True

    draw_chain()
