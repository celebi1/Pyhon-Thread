import threading
import time

done = False  # A flag variable to indicate if the program is done


def worker(text):
    counter = 0  # Initialize a counter variable
    while True:
        time.sleep(1)  # Sleep for 1 second
        counter += 1  # Increment the counter by 1
        print(f"{text}:{counter}")  # Print the text and the current counter value


# Create a daemon thread t1 that runs the worker function with the argument "ABC"
t1 = threading.Thread(target=worker, daemon=True, args=("ABC",))

# Create a non-daemon thread t2 that runs the worker function with the argument "XYZ"
t2 = threading.Thread(target=worker, daemon=False, args=("XYZ",))

# Start both threads
t1.start()
t2.start()

# Wait for both threads to finish
t1.join()
t2.join()

# Wait for user input to quit
input("Press enter to quit")
done = True  # Update the flag variable to indicate the program is done
