import random

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from an empty queue")
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from an empty queue")
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def select_and_announce_winner(self):
        """
        Randomly selects a winner from the queue.
        Dequeues all items up to and including the winner.
        Returns the name of the winning customer.
        """
        if self.is_empty():
            raise IndexError("cannot select a winner from an empty queue")
        
        winner_index = random.randrange(len(self.items))
        
        winner = None
        for _ in range(winner_index + 1):
            winner = self.dequeue()
        
        print(f"Winner: {winner}")
        return winner

if __name__ == "__main__":
    queue = Queue()
    for number in range(1, 11):
        queue.enqueue(f"Customer #{number}")

    print("=== Customer Raffle (Queue) ===")
    print(f"Entries in order: {queue.items}")
    print(f"Front of line:    {queue.peek()}")
    winner = queue.select_and_announce_winner()
    print(f"Removed up to and including {winner}")
    print(f"Still waiting:    {queue.items}")
