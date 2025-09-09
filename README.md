# Computer Networks Programming Lab

This repository contains implementations of fundamental networking protocols and concepts as part of a Computer Networks Programming course. The project demonstrates practical understanding of network communication protocols through hands-on Python implementations.

## Project Structure

### 📁 **packets/** - Network Protocol Simulation Framework

Contains a custom simulation framework for implementing and testing network protocols:

- **`Node.py`** - Abstract network node implementation with FSM (Finite State Machine) capabilities
- **`Simulator.py`** - Simulation engine that manages node interactions and timing
- **`demo1.py`** - TCP-like reliable transfer protocol implementation with pipelining

**Key Features:**

- Packet abstraction with source, destination, and message payload
- Bidirectional communication links between nodes
- Timer functionality for timeout handling
- State machine framework for protocol implementation

### 📁 **UDP/** - User Datagram Protocol Implementation

Demonstrates connectionless communication with packet loss simulation:

- **`client.py`** - UDP client that sends ping packets and measures RTT (Round Trip Time)
- **`server.py`** - UDP server with configurable packet loss simulation

**Learning Objectives:**

- Understanding connectionless communication
- RTT measurement and statistics
- Packet loss handling
- UDP socket programming

### 📁 **TCP/** - Transmission Control Protocol Implementation

Shows reliable, connection-oriented communication:

- **`TCPclient.py`** - TCP client that establishes connection and sends data
- **`TCPserver.py`** - TCP server that accepts connections and responds

**Learning Objectives:**

- Connection establishment and teardown
- Reliable data transfer
- Socket programming with TCP
- Client-server architecture

### 📁 **HTTP/** - Hypertext Transfer Protocol Implementation

Demonstrates application-layer protocol over TCP:

- **`httpClient.py`** - HTTP client that sends GET requests to web servers
- **`httpServer.py`** - Simple HTTP server that responds with HTML content

**Learning Objectives:**

- HTTP protocol structure and headers
- Request-response cycle
- Content-Type and Content-Length headers
- Web communication fundamentals

## Key Concepts Demonstrated

### 1. **Protocol Stack Implementation**

- Physical layer simulation through packet abstraction
- Transport layer protocols (UDP, TCP)
- Application layer protocols (HTTP)

### 2. **Reliability Mechanisms**

- Stop-and-wait protocol
- Pipelining for improved throughput
- Acknowledgment handling
- Timeout and retransmission

### 3. **Network Programming**

- Socket programming in Python
- Client-server architecture
- Error handling and timeout management
- Data encoding/decoding

### 4. **Performance Analysis**

- RTT measurement and statistics
- Packet loss simulation
- Throughput analysis
- Network simulation techniques

## Usage Instructions

### Running the Simulations

1. **Packet Simulation (demo1.py):**

   ```bash
   cd packets/
   python demo1.py
   ```

2. **UDP Ping Test:**

   ```bash
   # Terminal 1 - Start server
   cd UDP/
   python server.py

   # Terminal 2 - Run client
   python client.py
   ```

3. **TCP Communication:**

   ```bash
   # Terminal 1 - Start server
   cd TCP/
   python TCPserver.py

   # Terminal 2 - Run client
   python TCPclient.py
   ```

4. **HTTP Server:**

   ```bash
   # Terminal 1 - Start server
   cd HTTP/
   python httpServer.py

   # Terminal 2 - Run client
   python httpClient.py
   ```

## Educational Value

This project provides hands-on experience with:

- **Network Protocol Design** - Understanding how protocols work at different layers
- **Socket Programming** - Practical implementation of network communication
- **Simulation Techniques** - Building models to test network behavior
- **Performance Analysis** - Measuring and analyzing network performance
- **Error Handling** - Dealing with packet loss, timeouts, and connection issues

## Technical Implementation Notes

- **Language:** Python 3.x
- **Key Libraries:** `socket`, `threading`, `random`, `time`
- **Architecture:** Modular design with separate concerns for different protocol layers
- **Testing:** Includes packet loss simulation and timeout handling for realistic testing

This repository serves as a comprehensive learning resource for understanding computer networks through practical implementation and experimentation.
