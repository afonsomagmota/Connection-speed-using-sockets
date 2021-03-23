# Connection-speed-using-sockets
Allows to calculate the connection speed based on a test data between a server and a client. Implementing sockets and state machines data transfer can be staged and delimited.

In this example both the server and the client are ran in the IPv4 loopback address in a specific port. Applying state machines can be useful to mantain the data sent coherent. 

To calculate the speed, the client sends an example string. The server discovers the time that took that information to arrive. Then, knowing that connection speed is equal to the quocient of data with time, the server divides the data with the time that took that information to arrive.

It's a simple piece of code that can be pretty useful in a lot of situations! Don't forget to run the server first, or else the connection won't be estabilished.
