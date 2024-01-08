# Capstone-Project
This is a repo for my final year project as a final year student of Electronics and Computer Engineering in VIT Chennai.

Papers refering to:
- FPGA Based flying satellite
- FPGA-based operational concept and payload data processing for the Flying Laptop satellite
- RFlySim: Automatic test platform for UAV autopilot systems with FPGA-based hardware-in-the-loop simulations

## 08/01/24
### Important points from FPGA based On-Board Computer System for the “Flying Laptop” Micro-Satellite:
Here is a summary of the key points from the paper:

- The paper presents the architecture of an on-board computer system (OBCS) for the "Flying Laptop" microsatellite developed at the University of Stuttgart. 

- The OBCS exploits the capabilities of Xilinx Virtex-II Pro FPGAs to realize a highly integrated system on a single circuit board.

- The OBCS unifies all satellite computing functions including attitude control, telemetry/command handling, and payload data processing onto one redundant system. This provides simplicity and high fault tolerance.  

- The OBCS consists of 4 identical computer nodes in a master/monitor configuration for redundancy. The nodes are based on the Xilinx Virtex-II Pro FPGA and communicate with a separate command decoder and voter unit (CDV).

- The nodes directly execute control algorithms in hardware using the Handel-C language. This allows parallel execution without an operating system. Handel-C provides the determinism and timing control needed.

- Each node computes checksums that are compared to detect faults. Faulty nodes can be reset and restarted while the system continues operation. Permanently failing nodes can be isolated.

- A configuration controller implemented in a separate FPGA handles reliable startup and reconfiguration of the Virtex-II Pro FPGA on power-up or reset. Multiple configuration versions are stored.

- The OBCS approach demonstrates innovative concepts and solutions for implementing dependable high-performance computing systems for spacecraft using COTS components.


### Important Points from FPGA-based operational concept and payload data processing for the Flying Laptop satellite
Here is a summary of the key points from the paper:

- The paper presents the operational concept and on-board payload data processing design for the "Flying Laptop" microsatellite developed at the University of Stuttgart.

- The operational concept is flexible to support various technology demonstrations and earth observation experiments. It uses parallel state machines for the subsystems implemented in FPGAs.

- The onboard computer exploits FPGAs to realize high performance parallel processing. Algorithms run directly in hardware without an OS.

- Massive onboard data storage is not feasible. Thus data reduction through compression and processing is necessary. 

- Implemented processing algorithms include radiometric/geometric correction, image screening, classification, compression etc. running in pipelines.

- Processing enables applications like real-time image transmission and onboard decision making on which data to store/downlink.

- Autonomy can be added in stages - higher level commanding, intelligent processing, and satellite self decision making. But ground processing is still easier and more flexible.

- Overall, the onboard system maximally leverages the parallel processing capabilities of FPGAs to realize a high-performance, reconfigurable computing system matched to the needs of the microsatellite.


### Important Points from RFlySim
Here is a summary of the key points from the aerospace science paper:

- They present an automatic test platform called RFlySim for UAV autopilot systems. It uses hardware-in-the-loop (HIL) simulation with an FPGA to provide high fidelity and realism.

- A unified modeling framework is proposed that is compatible with different types of UAVs. This allows for sharing fault modes, safety design experience, and certification frameworks.

- Modular, model-based design (MBD) methods are used along with automatic code generation. This improves software credibility, standardization, and certification.

- The hardware includes an FPGA-based real-time simulator, the autopilot system under test, and a GPU-powered host computer running realistic 3D simulation.

- Experimental results verified the simulation accuracy. Successful applications demonstrated uses for rapid prototyping, algorithm comparisons, autonomous flight testing, and automatic fault injection testing.

- Main advantages are extensibility to new vehicle types, comprehensive fault testing capabilities, easier verification through modularity, and a path towards certification standards for UAVs.

In summary, they have developed an innovative real-time HIL simulation platform to improve UAV development, testing, and safety certification. The fidelity, automation, and compatibility offered are advances over current practice.
