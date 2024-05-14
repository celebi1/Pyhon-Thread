Multithreading Example in Python
Introduction
This Python script demonstrates the use of multithreading to run multiple tasks concurrently. It utilizes the threading module to create and manage threads.

Code Overview
Imports: The script starts with importing necessary modules: threading for multithreading and time for time-related operations.

Global Variables:

done: A flag variable indicating whether the program is done (not currently used in the code).
Worker Function (worker(text)):

This function defines the task performed by each thread.
It takes a text argument and continuously increments a counter every second.
It prints the provided text along with the current value of the counter.
Thread Creation and Starting:

Two threads, t1 and t2, are created using the threading.Thread class.
t1 is set as a daemon thread (will exit when the main program exits), while t2 is not.
Each thread is assigned the worker function with different text arguments.
Both threads are started with the start() method.
Thread Joining:

The main program waits for both threads to finish using the join() method.
This ensures that the program waits for all threads to complete before proceeding.
Program Termination:

After threads finish execution, the program prompts the user to press Enter to quit.
Upon receiving input, the program sets the done flag to True (though not utilized further).
Conclusion
This example illustrates how to utilize multithreading in Python to execute multiple tasks concurrently,
improving program efficiency by leveraging the capabilities of modern processors.
