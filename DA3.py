class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight

# Function to get the maximum value in the knapsack
def fractionalKnapsack(w, arr):
    # Sort items by the profit/weight ratio in descending order
    arr.sort(key=lambda x: x.profit/x.weight, reverse=True)
    
    finalValue = 0.0  # Variable to store the maximum value
    for item in arr:
        # If the current item can fit entirely into the knapsack, take it
        if w >= item.weight:
            finalValue += item.profit
            w -= item.weight
        else:
            # If the item can't fit entirely, take a fraction of it
            finalValue += item.profit * (w / item.weight)
            break  # Knapsack is full, stop

    return finalValue

if __name__ == "__main__":
    # Input number of items
    n = int(input("Enter number of items:\n"))
    arr = []
    
    # Input profit and weight for each item
    for i in range(n):
        profit = int(input("Enter profit of item " + str(i + 1) + ":\n"))
        weight = int(input("Enter weight of item " + str(i + 1) + ":\n"))
        arr.append(Item(profit, weight))
    
    # Input knapsack capacity
    w = int(input("Enter capacity of knapsack:\n"))
    
    # Get the maximum value that can be carried
    print("Maximum value in knapsack: ", fractionalKnapsack(w, arr))
