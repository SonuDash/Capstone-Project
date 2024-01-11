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


## 09/01/24
There is key change in the proceedings the project has been renamed to FPGA based on board computing system for **Satellite**. 
Here is a summary of the PDF document:

- **Introduction**: The paper presents a reconfigurable architecture for an on-board processor to be used in space exploration missions¹[1]²[2]. It uses a COTS reconfigurable MPSoC and dynamic partial reconfiguration to provide adaptive performance, dependability, and power consumption. The processor is applied to a vision-based navigation system that requires different image processing algorithms depending on the mission phase³[3].
  
- **Use Case Scenario**: The paper describes a scenario where a spacecraft lander carries a rover to be deployed on an astronomical body⁴[4]. The lander uses a camera to perform absolute and relative navigation based on surface features detection and matching⁵[5]. The rover uses stereo vision to navigate on the terrain. The paper proposes to use a single FPGA device to host different accelerators for each navigation mode, using reconfiguration to switch between them.
  
- **Related Work**: The paper reviews the state-of-the-art in the use of rad-hard and COTS FPGAs and MPSoCs in space missions, as well as the techniques for exploiting dynamic and partial reconfiguration for functional adaptation and fault mitigation⁶[6].
  
- **Background Information**: The paper provides relevant information about the Zynq UltraScale+ MPSoC architecture, the RTEMS real-time operating system, and the ARTICo3 framework for reconfigurable multi-accelerator systems.
  
- **System Architecture**: The paper describes the proposed on-board processor architecture, which consists of a software subsystem running on the RPU of the Zynq UltraScale+ device, and a hardware subsystem composed of four reconfigurable slots managed by the ARTICo3 framework. The software subsystem includes mission-specific tasks, reconfiguration tasks, and fault detection, isolation, and recovery tasks. The hardware subsystem includes different accelerators for the vision-based navigation algorithms.
  
- **Hardware Subsystem Management**: The paper explains how the reconfiguration and data-handling tasks control the mode changes and the data transfers between the software and hardware subsystems. It also details how the ARTICo3 primitives are integrated in the mission-specific tasks to invoke the accelerators.
  
- **Fault Mitigation Techniques**: The paper presents the fault mitigation techniques applied to the proposed architecture, which include a reconfiguration-aware readback scrubber, a reconfiguration-aware SEM-IP, and a reconfiguration-aware watchdog. It also analyzes the performance and overhead of these techniques, as well as the worst-case fault detection and correction times.
  
- **Application Mapping**: The paper discusses how the vision-based navigation application is mapped onto the proposed platform, showing the resource occupancy, the reconfiguration time, and the execution time of each accelerator. It also compares the results with a non-reconfigurable baseline implementation.
  
- **Experimental Results**: The paper evaluates the proposed architecture and the fault mitigation techniques using a radiation test campaign with protons and heavy ions. It reports the number and type of faults observed, the fault coverage achieved, and the impact of the faults on the application output. It also compares the results with a non-reconfigurable baseline implementation.
  
- **Conclusions and Future Work**: The paper concludes that the proposed reconfigurable architecture provides a cost-efficient and flexible solution for on-board processing in space applications, enabling the reuse of a single device for multiple non-concurrent tasks and enhancing the system reliability¹[1]. It also identifies some limitations and challenges for future work, such as the need for more accurate fault injection tools, the development of more sophisticated fault mitigation techniques, and the extension of the architecture to support multi-device reconfiguration.


## 10/01/24 0th review
11:20 AM
Response:
- Overly negative
- Panelists wanted something more specific
- Decision to make the project more of payload calculation specific


## 11/01/24
Research on SolSat intensified
New repo to be commited soon.
