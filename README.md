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

## Functionality

### Packets simulation (Go-Back-N with pipelining)

- Sender maintains a sliding window with size `cwin` and two indices:
  - `base`: first unacknowledged packet index
  - `next`: next packet index to send
- Receiver sends cumulative ACKs: `cack = first missing sequence number`.
- One timer is used for the oldest unacknowledged packet; on timeout the sender retransmits that packet.
- Random loss is applied to packets and ACKs to emulate unreliable links.

### UDP Ping

- Client sends timestamped pings and measures RTT per response.
- Server randomly drops or delays replies to simulate loss/jitter.
- Client prints min/max/average RTT and loss count.

### TCP Echo/HTTP

- TCP examples demonstrate connection-oriented, reliable transfer with a simple request/response.
- HTTP server replies with fixed HTML; HTTP client performs a GET request to a public server.

## Configuration (tweakable parameters)

- `packets/demo1.py`
  - `cwin`: sliding window size (default 10)
  - `timer_intval`: retransmission timer in seconds (default 5)
  - `loss_prob`: probability of packet or ACK loss (default 0.2)
- `UDP/server.py`
  - Random loss threshold (`rand > 0.7`) and variable delay (`time.sleep(rand/10)`) control drop rate and delay
- `UDP/client.py`
  - `n`: number of pings (default 10)
  - `settimeout(2)`: client receive timeout in seconds

## Expected Output Highlights

- `packets/demo1.py`
  - Logs like: `Sender <base> <next> <timerOn>` each step
  - `receiving ack... Pckt: Receiver Sender [<cack>, 'Acknowledged', <seq>]`
  - Occasional `Lost packet` / `Lost acknowledgement` due to simulated loss
  - Completion when all packets `[0..N-1]` show up in the final list
- `UDP/client.py`
  - Prints RTT per ping and summary stats (min/max/avg, lost count)
- `TCP/` and `HTTP/`
  - Server prints received requests; client prints responses

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
