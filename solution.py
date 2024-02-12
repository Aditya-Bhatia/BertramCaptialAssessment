import random

class Coworker:
    def __init__(self, name, drink_cost):
        self.name = name
        self.drink_cost = drink_cost

    def __str__(self):
        return self.name

def select_coworker_to_pay(coworkers):
    # Calculate total drink cost
    total_cost = sum(coworker.drink_cost for coworker in coworkers)
    # Pick a random number between 0 and total drink cost
    random_cost = random.uniform(0, total_cost)
    cumulative_cost = 0
    # Loop over all the drink costs and find out when the looped costs are greater than the random number
    for coworker in coworkers:
        cumulative_cost += coworker.drink_cost
        # The coworker whose drink makes the cost go over the random amount is the one who has to pay
        if cumulative_cost >= random_cost:
            return coworker

if __name__ == "__main__":
    # Define coworkers and their favorite drinks with respective costs
    names = input("Enter the names of the remaining 5 coworkers separated by a space: ").split(" ")
    drink_cost = input("Enter the cost of all 7 coworker's drinks separated by a space: ").split(" ")
    coworkers = [
        Coworker("Bob", float(drink_cost[0])),
        Coworker("Jeremy", float(drink_cost[1])),
        Coworker(names[0], float(drink_cost[2])),
        Coworker(names[1], float(drink_cost[3])),
        Coworker(names[2], float(drink_cost[4])),
        Coworker(names[3], float(drink_cost[5])),
        Coworker(names[4], float(drink_cost[6])),
    ]

    # Select coworker to pay for coffee
    selected_coworker = select_coworker_to_pay(coworkers)
    print(f"It's {selected_coworker}'s turn to pay for coffee today!")