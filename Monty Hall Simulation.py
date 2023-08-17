import random

def monty_hall_simulation(num_trials, switch_strategy=True):
    stay_wins = 0
    switch_wins = 0
    
    for _ in range(num_trials):
        # Randomly place the prize behind one of the three doors
        prize_door = random.randint(0, 2)
        
        # Contestant initially picks a random door
        contestant_choice = random.randint(0, 2)
        
        # Monty opens a door that doesn't have the prize and that the contestant didn't pick
        remaining_doors = [door for door in range(3) if door != contestant_choice and door != prize_door]
        monty_opens = random.choice(remaining_doors)
        
        if switch_strategy:
            # Switch to the other unopened door
            final_choice = [door for door in range(3) if door != contestant_choice and door != monty_opens][0]
        else:
            final_choice = contestant_choice
        
        if final_choice == prize_door:
            if switch_strategy:
                switch_wins += 1
            else:
                stay_wins += 1
    
    return stay_wins, switch_wins

if __name__ == "__main__":
    num_trials = int(input("Enter the number of simulation trials: "))
    switch_strategy = input("Enter 'y' for switch strategy, 'n' for stay strategy: ").lower() == 'y'
    
    stay_wins, switch_wins = monty_hall_simulation(num_trials, switch_strategy)
    
    print("\nSimulation Results:")
    print(f"Stay Wins: {stay_wins} out of {num_trials}")
    print(f"Switch Wins: {switch_wins} out of {num_trials}")
    print(f"Stay Win Probability: {stay_wins / num_trials:.4f}")
    print(f"Switch Win Probability: {switch_wins / num_trials:.4f}")
