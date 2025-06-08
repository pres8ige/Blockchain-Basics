# PoW: Miner with highest random power wins

# PoS: Staker with highest random stake wins

# DPoS: Count votes for delegates → randomly select from highest voted ones if tied

# Explains each selection logic inline


import random

# Mock Validators
miners = {
    "MinerA": random.randint(1, 100),
    "MinerB": random.randint(1, 100),
    "MinerC": random.randint(1, 100)
}

stakers = {
    "StakerA": random.randint(1, 1000),
    "StakerB": random.randint(1, 1000),
    "StakerC": random.randint(1, 1000)
}

voters = {
    "Voter1": "DelegateA",
    "Voter2": "DelegateB",
    "Voter3": "DelegateA"
}

# Proof of Work (PoW)
pow_winner = max(miners, key=miners.get)
print(f"\n[PoW] Validator selected: {pow_winner}")
print(f"Explanation: Miner with highest power ({miners[pow_winner]}) wins\n")

# Proof of Stake (PoS)
pos_winner = max(stakers, key=stakers.get)
print(f"[PoS] Validator selected: {pos_winner}")
print(f"Explanation: Staker with highest stake ({stakers[pos_winner]}) wins\n")

# Delegated Proof of Stake (DPoS)
vote_counts = {}
for voter, delegate in voters.items():
    vote_counts[delegate] = vote_counts.get(delegate, 0) + 1

max_votes = max(vote_counts.values())
top_delegates = [d for d, v in vote_counts.items() if v == max_votes]
dpos_winner = random.choice(top_delegates)

print(f"[DPoS] Validator selected: {dpos_winner}")
print(f"Explanation: Delegate with most votes ({max_votes}) is selected randomly from top candidates if tied\n")

# Show all mock data for clarity
print("===== Mock Data Used =====")
print("Miners (PoW power):", miners)
print("Stakers (PoS stake):", stakers)
print("Voters (DPoS votes):", voters)
print("==========================\n")
