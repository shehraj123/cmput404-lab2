## Question 1

TCP socket is specified by 
```
socket.SOCK_STREAM
```
argument when socket is created.

## Question 2

The difference between client socket and server socket is in the way we use the sockets.
In client sockets, we dont bind to address & port instead connect to the HOST and PORT.
Server sockets listen and accept any requests received on the host address.

## Question 3

In order to instruct OS to let us reuse the same bind port, we pass in the second parameter(arg2) of 
```
socket.setsockopt(arg1, arg2, arg3) 
```
as
```
socket.SO_REUSEADDR
```

## Question 4

We get the ip address and the port of the client trying to connect to the server.

## Question 5

We are not making any HTTP request in the case of echo_server. Only thing returned by server is the message for echo.
In case of request made to www.google.com, the HTML for the google homepage is returned.

## Question 6

Link:

[Github](https://github.com/shehraj123/cmput404-lab2)

