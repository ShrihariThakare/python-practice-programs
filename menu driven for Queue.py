queue = []
max_size = int(input("Enter size of Queue: "))

while True:
    print("\n--- QUEUE OPERATIONS ---")
    print("1. Enqueue (Insert)")
    print("2. Dequeue (Delete)")
    print("3. Display Queue")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        if len(queue) == max_size:
            print("Queue Overflow! Cannot insert.")
        else:
            element = input("Enter element to insert: ")
            queue.append(element)
            print(f"{element} inserted into queue.")

    elif choice == 2:
        if len(queue) == 0:
            print("Queue Underflow! Queue is empty.")
        else:
            removed = queue.pop(0)
            print(f"{removed} removed from queue.")

    elif choice == 3:
        if len(queue) == 0:
            print("Queue is empty.")
        else:
            print("Queue elements:", queue)

    elif choice == 4:
        print("Exiting program.")
        break

    else:
        print("Invalid choice! Try again.")

