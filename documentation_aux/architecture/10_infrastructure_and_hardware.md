# 11. Infrastructure and Hardware

## Definition

The **Infrastructure and Hardware** module defines the physical and technical foundation on which NORA exists, operates, senses, computes, communicates, and acts.

While the cognitive, dialogue, planning, backend, and frontend modules describe how NORA behaves as an intelligent system, this module describes **the real embodied substrate that makes that behaviour possible in practice**.

NORA is not conceived as a purely abstract software assistant. It is conceived as a deployed multimodal system that may live inside a robot, an edge device, a distributed hardware platform, or a hybrid physical-digital installation. Because of that, the architecture must explicitly define the hardware and infrastructure layer rather than treating it as an implementation detail.

This module includes the computational devices, sensors, actuators, communication buses, network interfaces, and external controllable devices that together form the operational body of the system.

---

## Architectural Purpose

The purpose of the Infrastructure and Hardware module is to provide a structured description of the **physical execution environment** of NORA.

A system like NORA depends on more than software logic. It requires:

* computing units that run perception, planning, memory, and orchestration workloads
* sensors that capture information from the surrounding world
* actuators that allow the system to express itself and affect the environment
* connectivity layers that link internal components and external systems
* external devices that can be monitored or controlled

Without this module, the architecture would describe intelligence in abstraction, but it would not explain how that intelligence is physically realized, distributed, constrained, or connected.

This module therefore anchors the full architecture in real deployment conditions.

---

## Why This Module Is Necessary in NORA

In many software systems, hardware is reduced to an invisible execution platform. In NORA, that is not sufficient.

NORA is intended to operate as a multimodal embodied cognitive system that may:

* listen through microphones
* see through cameras
* identify users through NFC or other physical channels
* move mechanical parts
* emit light and sound
* run on embedded or edge hardware
* communicate with local devices and cloud services
* control appliances, sensors, or domestic infrastructure

Because of this, hardware is not just a support concern. It directly influences:

* what the system can perceive
* what actions it can perform
* what latency constraints exist
* what processing can occur locally
* what reliability and safety requirements apply
* how modules are physically distributed

For NORA, infrastructure and hardware are architectural concerns, not merely deployment notes.

---

## Scope of the Module

The Infrastructure and Hardware module includes the physical and low-level technical elements required for NORA to exist and operate as a real system.

Its scope includes:

* computation devices
* embedded controllers
* physical sensors
* actuators and output hardware
* connectivity technologies and buses
* external controllable devices
* hardware distribution and deployment topology

Its scope does **not** include:

* user-facing interaction design
* high-level perception logic
* planning and reasoning logic
* dialogue continuity
* application-level APIs
* persistent data modelling

Those belong to other architectural modules.

This distinction is important because the Infrastructure and Hardware module defines **with what physical substrate the system exists**, not how the higher cognitive layers reason about that substrate.

---

## Architectural Role Within the System

Within the global architecture, the Infrastructure and Hardware module acts as the **material support layer** that enables all other modules to run.

Conceptually, its role can be summarized as:

**Physical world ↔ Sensors / Devices / Compute / Connectivity ↔ NORA software architecture**

This means the module sits at the boundary between:

* the software system
* the robot body or device platform
* the surrounding physical environment
* external connected devices and infrastructures

It provides the real channels through which perception, control, expression, and external integration become physically possible.

---

## Core Responsibilities

This module performs several architectural responsibilities.

### 1. Provide Computational Execution Capacity

It defines the hardware platforms that execute the software components of NORA.

This includes devices such as:

* embedded compute boards
* microcontrollers
* local control processors
* edge machines
* higher-performance computing nodes when required

These platforms determine what workloads can run locally and how the system is distributed.

### 2. Provide Physical Sensing

It defines the hardware components that capture information from the environment and from the robot itself.

This includes:

* microphones
* cameras
* proximity sensors
* environmental sensors
* tactile sensors
* internal status sensors

Through these devices, the higher-level Perception module receives raw data from the real world.

### 3. Provide Physical Actuation

It defines the components that allow NORA to produce observable effects.

This includes:

* speakers
* displays
* LEDs
* servos
* motors
* relays
* haptic components
* controllable external devices

Through these components, the Action and Expression module can materialize the system's decisions.

### 4. Provide Communication Paths

It defines how internal hardware components and external systems communicate.

This includes:

* local buses
* short-range wireless links
* network interfaces
* internet connectivity
* machine-to-machine communication protocols

These communication paths are essential for distributed execution, hardware coordination, and integration with remote services.

### 5. Define Embodiment Constraints

The hardware layer defines practical constraints that affect the whole architecture.

Examples include:

* processing power limits
* thermal limits
* battery or power constraints
* camera field of view
* microphone quality
* servo precision
* network availability
* sensor update rates

These constraints shape system behaviour and must be acknowledged architecturally.

### 6. Support Physical Deployment and Maintenance

The module also provides the foundation for real deployment, maintenance, replacement, and scaling decisions.

This includes practical concerns such as:

* modular hardware organization
* replaceable components
* wiring and bus topology
* device discoverability
* operational monitoring
* fault isolation

---

## Design Principles

Several principles should guide the design of this module.

### Separation Between Capability and Implementation

The architecture should distinguish between:

* **what capability is needed**
* **which specific hardware component provides it**

This allows NORA to evolve from one device or sensor to another without changing the higher-level conceptual architecture.

### Hardware Modularity

Sensors, actuators, compute boards, and external devices should be organized in a modular way so the system can evolve incrementally.

This is especially important in a project like NORA, where hardware configurations may change during prototyping and later deployment.

### Distribution Awareness

NORA may run across multiple physical devices rather than a single board.

For example:

* a Raspberry Pi may run local orchestration
* one or more microcontrollers may handle low-level IO or servo control
* a remote machine may provide heavier inference or backend services

The architecture should therefore describe hardware as a distributed system when appropriate.

### Real-Time Suitability

Some hardware interactions have tighter timing constraints than others.

For example:

* wakeword detection requires low latency
* servo control requires stable timing
* emergency stop signals require immediate propagation
* video processing may require sustained throughput

The infrastructure must support these timing realities.

### Safety and Reliability

Because NORA may interact physically with people, devices, and the environment, the hardware layer must support safe operation.

This includes:

* fail-safe states
* controlled power behaviour
* protected actuators
* reliable communication with critical modules
* graceful degradation when hardware fails

### Replaceability and Evolvability

The architecture should remain robust even if specific hardware models change over time.

This means the conceptual model should not be overly tied to one exact board, sensor, or actuator unless that specificity is intentionally required.

---

## Relationship With Other Architectural Modules

The Infrastructure and Hardware module interacts with many other parts of the system.

### Relationship With Perception

Perception depends on hardware sensors to acquire raw signals from the world.

The Infrastructure and Hardware module defines the physical sensing devices, while the Perception module defines how their signals are processed and interpreted.

### Relationship With Action and Expression

Action and Expression depends on hardware output devices and actuators to produce real-world effects.

The hardware module defines the speakers, displays, LEDs, motors, and other devices, while the Action and Expression module defines how they are used behaviourally.

### Relationship With the Cognitive Core

The Cognitive Core depends on infrastructure status to regulate behaviour.

For example, if a camera fails, a motor overheats, or a battery becomes low, the Cognitive Core may alter state or inhibit actions.

### Relationship With Backend and Application

The backend may expose hardware status, diagnostics, and control interfaces, but the physical substrate itself belongs to this module.

### Relationship With Frontend and Visualization

Frontend tools may display infrastructure state, telemetry, and diagnostics, but they do not define the hardware itself.

### Relationship With Integrations and External Services

Some external integrations depend on the available communication infrastructure and controllable device ecosystem defined here.

---

## Internal Structure

To maintain clarity, the Infrastructure and Hardware module is divided into several submodules.

### 11.1 Computation

Defines the hardware platforms responsible for running NORA's software workloads.

### 11.2 Sensors

Defines the hardware input devices that capture information from the environment or from the robot itself.

### 11.3 Actuators

Defines the hardware output and movement components through which NORA expresses behaviour or affects the environment.

### 11.4 Connectivity

Defines the communication technologies, buses, and links that connect internal components and external systems.

### 11.5 Controllable External Devices

Defines the external appliances, smart devices, and connected systems that NORA can observe, coordinate, or control.

Together, these submodules provide a complete architectural description of the physical and technical substrate of NORA.

---

## Representative Questions This Module Answers

This module helps answer practical architectural questions such as:

* On what devices does NORA actually run?
* Which components perform heavy processing and which perform low-level control?
* What sensors are available to perceive the world?
* What actuators are available to express behaviour?
* How do internal modules communicate physically?
* Which external devices can be controlled from NORA?
* What deployment and hardware constraints shape the system?

These are not secondary implementation details. They are part of the architectural identity of an embodied system.

---

## Architectural Importance

The Infrastructure and Hardware module is what allows NORA to exist as a **real deployed embodied platform rather than only as a conceptual intelligence stack**.

Without this module, the architecture could still describe:

* interaction
* perception
* cognition
* dialogue
* planning
* action
* persistence
* frontend behaviour

But it would still be missing the physical substrate that makes all of that possible.

By explicitly modelling infrastructure and hardware as a dedicated architectural domain, NORA gains:

* embodiment clarity
* deployment realism
* physical-system traceability
* support for modular hardware evolution
* a clearer bridge between software architecture and robotic implementation

For that reason, the Infrastructure and Hardware module is a foundational part of the complete system architecture.

# 11.1 Computation

## Definition

The **Computation** submodule defines the set of hardware processing units responsible for executing the software components of the NORA system.

These devices provide the computational capacity required to run perception pipelines, cognitive processes, dialogue systems, planning mechanisms, backend services, and hardware control layers.

Within the Infrastructure and Hardware module, the Computation submodule represents the **physical processing backbone of the system**.

If the Sensors submodule defines how information enters the system, and the Actuators submodule defines how the system affects the physical world, the Computation submodule defines **where the software intelligence of NORA actually runs**.

---

## Architectural Purpose

The purpose of the Computation submodule is to describe the physical computing devices that host and execute the software architecture of NORA.

An embodied cognitive system requires several different classes of computing devices because the tasks involved have very different characteristics:

* high‑level reasoning and dialogue
* real‑time sensor processing
* hardware control
* networking and communication
* safety and fallback control

Different devices may specialize in different layers of the architecture.

For example:

* a small microcontroller may handle direct hardware control
* an embedded computer may process cameras and sensors
* a more powerful computer may run large language models or planning systems

By explicitly defining these devices, the architecture clarifies **how software modules are physically distributed across hardware resources**.

---

## Role in the Global Architecture

Within the overall system architecture, computation devices act as the **execution environment of the software system**.

Conceptually the relationship can be summarized as:

**Software modules → executed on → computation hardware**

These devices run the components belonging to multiple layers of the architecture, including:

* Perception modules
* Cognitive Core logic
* Dialogue and session management
* Planning and agents
* Backend services and APIs
* Hardware control interfaces

The Computation submodule therefore connects the logical architecture of NORA with the real physical machines capable of executing it.

---

## Scope of the Submodule

The Computation submodule includes the hardware units responsible for processing and executing software.

Its scope includes:

* embedded computers
* microcontrollers
* dedicated compute modules
* local servers or mini PCs
* optional hardware accelerators

Its scope does **not** include:

* sensor hardware
* actuator hardware
* networking infrastructure
* external cloud services

Those belong to other submodules such as Sensors, Actuators, Connectivity, or External Integrations.

---

## Core Responsibilities

### Execution of Software Modules

All software modules in the architecture must ultimately run on a physical processing device.

Computation hardware is responsible for executing:

* perception pipelines
* speech processing
* visual processing
* dialogue management
* planning and reasoning
* backend APIs
* device drivers

---

### Distribution of System Workloads

A complex embodied system often distributes computation across several devices to improve performance, modularity, and safety.

Examples include:

* delegating motor control to a microcontroller
* running perception pipelines on an embedded computer
* executing high‑level reasoning on a more powerful processor

This distributed architecture improves scalability and fault isolation.

---

### Real‑Time Hardware Control

Some tasks require strict timing constraints, particularly those related to sensors, actuators, and physical control loops.

Microcontrollers and dedicated hardware controllers may therefore handle:

* servo control
* motor control
* sensor sampling
* safety monitoring

These tasks may operate independently of the high‑level cognitive software to ensure stable physical behaviour.

---

### High‑Level Cognitive Processing

Higher‑level computational devices may handle tasks that require more processing power, such as:

* natural language processing
* planning
* perception pipelines
* machine learning inference
* multimodal integration

These devices typically run operating systems capable of supporting complex software stacks.

---

## Main Computation Devices

The architecture identifies several major categories of computing devices.

### Raspberry Pi

A **Raspberry Pi** is a compact embedded computer capable of running a full operating system such as Linux.

In the NORA architecture, a Raspberry Pi can act as the main onboard computing unit responsible for executing many of the software modules of the system.

Possible responsibilities include:

* running backend services
* executing perception pipelines
* managing dialogue systems
* interfacing with sensors and actuators
* networking with external services

The Raspberry Pi offers a good balance between computational power, energy consumption, and hardware integration capabilities.

---

### Arduino

An **Arduino** is a microcontroller platform designed for direct hardware interaction and deterministic control.

Unlike embedded computers, Arduinos typically do not run a general‑purpose operating system.

Instead they execute firmware programs responsible for interacting with hardware components such as:

* servos
* motors
* LEDs
* sensors
* relays

In the NORA architecture, an Arduino may act as a **low‑level hardware controller** that receives commands from higher‑level software running on devices such as the Raspberry Pi.

This separation improves reliability and simplifies hardware interfacing.

---

### Microcontrollers

Microcontrollers are compact processing units specialized for embedded control tasks.

They are often used in situations where:

* strict timing constraints exist
* power consumption must remain low
* simple control loops are required

In the context of NORA, microcontrollers may support tasks such as:

* sensor polling
* actuator control
* safety monitoring
* communication with higher‑level processors

While Arduino boards are one example of microcontroller platforms, other specialized microcontrollers may also be used depending on hardware requirements.

---

### Mini PC

A **Mini PC** is a compact but relatively powerful computing device capable of running full desktop‑class operating systems.

In the NORA architecture, a Mini PC may be used when more computational power is required than what embedded boards typically provide.

Possible use cases include:

* running large language models locally
* executing heavy perception pipelines
* performing real‑time video processing
* hosting multiple backend services simultaneously

A Mini PC may act as the primary compute node in more advanced versions of the robot.

---

### Future External GPU

A **GPU (Graphics Processing Unit)** provides highly parallel computational capabilities useful for machine learning, computer vision, and large‑scale numerical processing.

In future versions of the system, an external GPU may be connected to support workloads such as:

* deep learning inference
* real‑time vision processing
* large language model execution
* multimodal data processing

The architecture treats the GPU as a **future hardware accelerator** that can significantly increase the system's computational capacity.

---

### Edge Device

An **Edge Device** refers to any computing unit located close to the physical robot that performs computation locally rather than relying entirely on cloud services.

Edge devices reduce latency, improve privacy, and increase reliability in environments where network connectivity may be unstable.

In the NORA architecture, edge computing may involve devices such as:

* onboard embedded computers
* nearby local servers
* dedicated AI inference devices

Edge processing allows NORA to continue functioning even when internet connectivity is unavailable.

---

## Relationship With Other Modules

### Relationship With Sensors

Sensors provide raw physical signals that are captured by hardware devices.

Computation hardware is responsible for processing those signals through perception pipelines and other software modules.

---

### Relationship With Actuators

Computation hardware generates the control signals that ultimately drive actuators.

For example, high‑level commands may be translated into low‑level motor instructions executed by microcontrollers.

---

### Relationship With the Cognitive Core

The Cognitive Core is a logical software construct.

Its algorithms and state machines must ultimately execute on computation hardware.

---

### Relationship With Backend and Application

Backend services, APIs, and orchestration components also run on computation hardware, typically on embedded computers or mini PCs.

---

## Design Principles

### Layered Processing

The architecture should distribute computation across layers of increasing complexity, from low‑level control to high‑level reasoning.

---

### Hardware Specialization

Different devices should specialize in tasks that match their capabilities.

For example:

* microcontrollers for deterministic control
* embedded computers for perception and system coordination
* GPUs for heavy machine learning workloads

---

### Fault Isolation

Separating critical hardware control from high‑level reasoning reduces the risk that software failures affect basic physical safety.

---

### Scalability

The architecture should allow the addition of more powerful computing devices without requiring a complete redesign of the system.

---

## Architectural Importance

The Computation submodule defines the physical infrastructure on which the entire software architecture of NORA operates.

Without computation hardware, none of the higher‑level modules — perception, cognition, dialogue, planning, or action — could exist in practice.

For this reason, the Computation submodule forms the **foundation that transforms NORA from a conceptual software architecture into a real embodied system capable of operating in the physical world**.

# 11.2 Sensors

## Definition

The **Sensors** submodule defines the set of hardware input devices that allow NORA to perceive physical signals from its environment, from nearby users, and from its own internal physical state.

Within the Infrastructure and Hardware module, sensors represent the **physical entry points through which real‑world information becomes available to the software system**.

Sensors transform measurable physical phenomena such as sound, light, motion, temperature, or electrical state into digital signals that can later be processed by higher layers of the architecture.

If the Perception module defines how signals are interpreted and transformed into meaning, the Sensors submodule defines **which hardware components produce those signals in the first place**.

For example:

• a microphone captures sound
• a camera captures images
• a proximity sensor detects nearby objects
• a tactile sensor detects physical contact

The interpretation of these signals belongs to the Perception layer, while the acquisition of the raw signals belongs to this submodule.

---

## Architectural Purpose

The purpose of the Sensors submodule is to define the **complete hardware sensing surface of NORA**.

A multimodal embodied system requires multiple sensing modalities in order to interact with humans and operate safely in the physical world. These sensing capabilities allow the system to:

• hear human speech
• observe people and objects
• detect physical interaction
• sense environmental conditions
• monitor its own physical state

Without sensors, NORA would have no access to the surrounding environment and would be unable to react to real‑world events.

This submodule therefore documents:

• which physical sensing devices exist
• what type of signals they measure
• what operational role each sensor plays
• how sensing capabilities support perception, interaction, safety, and system monitoring

---

## Role in the Global Architecture

Within the global architecture, sensors act as the **origin of observable data**.

Conceptually the information flow can be described as:

Physical world / robot body
→ Sensors
→ Perception
→ Cognitive processing

Sensors therefore form the bridge between the physical environment and the digital system.

The data produced by sensors can be used by several architectural layers, including:

• Perception modules
• Cognitive Core context updates
• Safety mechanisms
• Hardware monitoring
• Backend telemetry
• System observability

Because sensing capabilities determine what the system can detect or react to, the design of this submodule has a direct impact on the behavioural capabilities of the robot.

---

## Scope of the Submodule

The Sensors submodule includes hardware devices that capture input signals.

Its scope includes:

• audio sensors
• visual sensors
• proximity sensors
• tactile sensors
• environmental sensors
• power‑state sensors
• future inertial and positional sensing hardware

It does **not** include:

• interpretation of signals
• classification of detected events
• planning or decision making
• actuator control

Those responsibilities belong to other modules such as Perception, Planning, and Action.

---

## Core Responsibilities

### Signal Acquisition

The primary responsibility of sensors is to acquire measurable physical signals.

These signals may include:

• acoustic waves
• visible light
• electromagnetic near‑field communication
• physical pressure
• distance to nearby objects
• temperature
• humidity
• electrical state

Sensors convert these phenomena into digital measurements usable by software modules.

---

### Environmental Awareness

Environmental sensors provide contextual information about the physical surroundings.

Examples include:

• temperature sensors
• humidity sensors
• ambient light sensors
• proximity sensors

These measurements help the system adapt its behaviour according to environmental conditions.

---

### Human Interaction Detection

Some sensors directly support human interaction with the robot.

Examples include:

• microphones for speech interaction
• cameras for visual interaction
• NFC readers for identity recognition
• tactile sensors for touch‑based interaction

These sensors enable natural multimodal interaction between humans and the system.

---

### Internal State Monitoring

Some sensors measure internal physical conditions of the robot itself.

Examples include:

• battery state sensors
• future IMU sensors
• future encoder sensors

These measurements support system stability, maintenance monitoring, and safe operation.

---

## Sensor Types

### Microphones

Microphones capture acoustic signals from the surrounding environment.

They provide the raw audio stream used for:

• wakeword detection
• speech recognition
• acoustic scene analysis
• future speaker identification

Microphones are essential because voice interaction is one of the primary communication channels of the system.

Design considerations may include:

• microphone arrays
• far‑field audio capture
• noise suppression
• echo cancellation

---

### Cameras

Cameras capture visual information from the environment.

Image or video streams obtained from cameras can be used for:

• person detection
• face detection
• facial recognition
• gesture detection
• OCR
• scene analysis
• QR code scanning

Cameras enable visual awareness and support both perception and interaction capabilities.

---

### NFC

NFC (Near Field Communication) sensors allow the system to detect nearby NFC‑enabled tags or cards.

This capability supports use cases such as:

• user identification
• quick login
• profile activation
• device pairing
• access control

NFC provides a simple physical mechanism for identity recognition without requiring voice or visual authentication.

---

### Temperature Sensors

Temperature sensors measure thermal conditions either in the environment or within the robot's enclosure.

These measurements may be used for:

• environmental awareness
• hardware protection
• thermal management
• maintenance alerts

---

### Humidity Sensors

Humidity sensors measure the moisture level of the surrounding air.

Humidity information can contribute to:

• environmental monitoring
• indoor comfort analysis
• climate‑related automation

---

### Light Sensors

Light sensors measure ambient illumination levels.

These measurements can be used to:

• adjust display brightness
• adapt camera settings
• detect day or night conditions
• improve visual interaction behaviour

---

### Proximity Sensors

Proximity sensors detect nearby objects or users without requiring direct physical contact.

Typical technologies include:

• infrared proximity detection
• ultrasonic distance sensing
• time‑of‑flight sensing

These sensors can support:

• presence detection
• collision avoidance
• user approach detection
• safety monitoring

---

### Tactile Sensors

Tactile sensors detect direct physical interaction with the robot.

They may include:

• capacitive touch sensors
• pressure sensors
• contact switches

These sensors allow users to interact physically with the robot for actions such as:

• activation
• confirmation
• interruption
• emotional interaction

---

### Battery Sensors

Battery sensing hardware measures the energy state of the robot.

Typical measurements include:

• battery level
• voltage
• charging state
• discharge rate

These measurements influence system behaviour such as:

• energy management
• safe shutdown
• low‑power operation

---

### Future IMU

An **Inertial Measurement Unit (IMU)** would provide motion‑related measurements such as:

• acceleration
• angular velocity
• orientation estimation

If integrated in future versions, the IMU could support:

• movement monitoring
• stability control
• physical orientation awareness

---

### Future Encoder

Encoders provide precise measurements of mechanical position or rotation.

They are commonly used for:

• motor rotation tracking
• joint position feedback
• closed‑loop motion control

Encoders become relevant when the robot includes more advanced mechanical actuation.

---

## Relationship With Other Modules

### Relationship With Perception

Sensors generate the raw signals processed by the Perception module.

Sensors capture signals.
Perception interprets them.

---

### Relationship With Interaction Interfaces

Some sensors directly support interaction channels.

Examples include microphones for voice interaction or cameras for gesture detection.

---

### Relationship With the Cognitive Core

Sensor outputs may influence operational context, system state transitions, and behaviour decisions.

---

### Relationship With Observability

Sensor data and sensor health may be exposed through backend telemetry and monitoring systems.

---

## Architectural Importance

The Sensors submodule is fundamental to transforming NORA from a purely software‑based system into a physical embodied agent.

Through sensors, NORA gains access to information about:

• humans
• objects
• environmental conditions
• its own physical state

These sensing capabilities form the foundation upon which perception, cognition, and interaction are built.

Without sensors, the system would have no direct connection with the physical world.

# 11.3 Actuators

## Definition

The **Actuators** submodule defines the set of hardware output devices that allow NORA to affect the physical world or produce perceivable signals for humans.

Within the Infrastructure and Hardware module, actuators represent the **physical mechanisms through which the system executes actions**.

If Sensors provide input from the physical world and Computation provides the processing capability, actuators provide the **mechanical, visual, acoustic, or electrical outputs that materialize system decisions into real-world effects**.

Examples of actuator outputs include:

• speaking through speakers
• displaying information on a screen
• emitting visual signals using LEDs
• moving mechanical components
• activating external electrical devices

In architectural terms, actuators are the final step in the chain:

Perception → Cognition → Planning → Action → **Actuators**

---

## Architectural Purpose

The purpose of the Actuators submodule is to define the hardware components that allow NORA to execute actions in the physical environment.

An embodied system must not only perceive and reason; it must also be able to **express, signal, and physically act**.

Actuators provide the mechanisms that make this possible.

Through actuators the system can:

• communicate with humans
• express internal states
• manipulate objects or its own body
• control external devices
• produce feedback signals

Without actuators, NORA would be capable of sensing and reasoning but unable to perform any visible or audible actions.

---

## Role in the Global Architecture

In the global architecture, actuators represent the **physical execution layer** of system behaviour.

They receive commands generated by higher-level modules such as:

• the Action and Expression module
• the Cognitive Core
• planning and control systems
• safety mechanisms

These commands are translated into physical outputs through the actuator hardware.

Conceptually the flow can be summarized as:

System decision
→ Action layer
→ hardware control signals
→ **Actuators**
→ physical effect

This means actuators transform digital control instructions into **real-world motion, sound, light, or electrical switching**.

---

## Scope of the Submodule

The Actuators submodule includes hardware devices responsible for producing output signals or physical movement.

Its scope includes:

• audio output devices
• visual output devices
• motion mechanisms
• electrical switching devices
• haptic feedback devices
• interfaces that control external physical devices

It does **not** include:

• the decision logic that determines which actions to perform
• dialogue management
• planning systems
• perception pipelines

Those responsibilities belong to other modules such as the Cognitive Core, Planning and Agents, and Action and Expression.

---

## Core Responsibilities

### Physical Action Execution

Actuators translate system commands into physical actions.

These actions may involve:

• generating sound
• producing visual output
• moving mechanical components
• switching electrical circuits
• triggering external devices

The actuator hardware ensures that system decisions can produce measurable changes in the real world.

---

### Human Communication

Some actuators support direct communication with humans.

Examples include:

• speakers for voice output
• displays for visual information
• LEDs for expressive signalling

These outputs form the primary channels through which the system expresses responses and feedback.

---

### Robotic Movement

Mechanical actuators enable the robot to move parts of its structure.

These may include:

• servos
• motors

Such actuators allow the system to perform gestures, orientation changes, and physical expressions.

---

### Environmental Control

Certain actuators allow the system to control devices or infrastructure in its environment.

Examples include:

• relays
• smart device control
• home automation interfaces

These mechanisms allow the robot to affect systems beyond its own body.

---

## Actuator Types

### Speakers

Speakers provide the primary acoustic output channel of the system.

They allow NORA to produce:

• synthesized speech
• sound notifications
• music playback
• audio feedback signals

Speakers therefore support both conversational interaction and multimedia output.

Design considerations may include:

• sound quality
• output volume
• echo management relative to microphones

---

### Screen

A display screen provides visual output for the user.

The screen may be used to show:

• text
• graphical interfaces
• images
• video
• visual feedback
• system states

The display often acts as the main visual interface between the robot and its users.

---

### LEDs

LEDs provide simple but effective visual signals.

They can represent system states such as:

• active listening
• processing
• idle state
• alerts
• emotional expression

LEDs are often used for quick visual feedback because they are energy-efficient and easy to control.

---

### Servos

Servo motors allow controlled rotational movement of mechanical components.

They may be used to move elements such as:

• the robot head
• eyes or cameras
• arms or small limbs

Servos allow precise positioning and are commonly used in small robotic systems.

---

### Motors

Motors provide rotational or translational movement.

They may support actions such as:

• body movement
• mechanical actuation
• rotating platforms

Motors may be combined with gear systems or mechanical structures depending on the robot design.

---

### Future Haptic Vibration

A future haptic actuator may provide vibration-based feedback.

Possible uses include:

• tactile notifications
• silent alerts
• physical feedback for interaction

Haptic feedback can improve accessibility and add an additional communication channel between the system and users.

---

### Relays

Relays allow the system to switch electrical circuits on or off.

They can be used to control:

• lights
• power outlets
• appliances

Relays act as a bridge between digital control signals and electrical power systems.

---

### Home Automation Actuators

Actuators may also include interfaces to smart devices in the environment.

These may control systems such as:

• smart lights
• connected plugs
• thermostats
• automated appliances

These actuators allow the robot to participate in home automation ecosystems.

---

## Relationship With Other Modules

### Relationship With the Action and Expression Module

The Action and Expression module defines **what actions should occur**.

The Actuators submodule defines **the hardware mechanisms that execute those actions**.

---

### Relationship With Sensors

Sensors provide environmental information that may influence actuator behaviour.

For example, proximity sensors may limit movement or brightness sensors may adjust display output.

---

### Relationship With Computation

Computation hardware generates the control signals that drive actuators.

These signals may be sent directly or through microcontrollers.

---

### Relationship With Backend and Control Systems

Actuator states and commands may also be monitored, logged, or controlled through backend services and administrative interfaces.

---

## Design Principles

### Reliability

Actuators must operate predictably because they directly affect the physical environment.

---

### Safety

Movement-related actuators must include safeguards to prevent unsafe behaviour.

---

### Clear Mapping to Actions

Each actuator should correspond to well-defined actions in the Action and Expression layer.

---

### Expandability

The architecture should allow new actuator types to be integrated without requiring structural redesign.

---

## Architectural Importance

The Actuators submodule defines the mechanisms through which NORA manifests behaviour in the physical world.

Through actuators, the system can:

• speak
• display information
• signal states
• move mechanical components
• control external devices

Without actuators, the system would remain purely observational and unable to express decisions or perform actions.

For this reason, actuators form a critical component of the Infrastructure and Hardware layer and complete the interaction loop between perception, cognition, and the physical enviro

# 11.4 Connectivity

## Definition

The **Connectivity** submodule defines the communication mechanisms that allow NORA to exchange data with other devices, hardware components, and external services.

Within the Infrastructure and Hardware module, connectivity represents the **communication layer that links the system with the outside world and with its internal hardware subsystems**.

If Sensors provide input signals and Actuators produce physical output, connectivity defines **how information travels between components of the system and between NORA and external systems**.

Connectivity mechanisms allow the system to:

• communicate with external services
• interact with other devices
• exchange data between hardware modules
• control peripherals
• receive remote commands

Without connectivity, NORA would operate as an isolated device unable to integrate with networks, services, or distributed hardware components.

---

## Architectural Purpose

The purpose of the Connectivity submodule is to define the physical and protocol-level communication channels that enable interaction between NORA and other systems.

An embodied intelligent system typically requires multiple communication layers because different types of interactions have different requirements.

Examples include:

• wireless communication with networks
• wired communication with peripherals
• communication buses for embedded electronics
• internet connectivity for external services

This submodule documents the communication technologies used by the system and clarifies how data can flow between system components.

---

## Role in the Global Architecture

Within the global architecture, connectivity forms the **transport layer that enables communication between modules running on different devices or hardware interfaces**.

Conceptually, connectivity enables interactions such as:

System module → communication channel → external device or service

Connectivity mechanisms support interactions between:

• internal hardware components
• onboard computation units
• external devices
• remote servers
• smart home systems

Because many features of NORA rely on external services or distributed hardware, reliable connectivity is essential for system functionality.

---

## Scope of the Submodule

The Connectivity submodule includes communication technologies that allow devices and software components to exchange information.

Its scope includes:

• wireless communication technologies
• wired network connections
• embedded hardware communication buses
• device interfaces

It does **not** include:

• application protocols
• cloud service integrations
• logical APIs
• software message routing

Those responsibilities belong to higher-level modules such as Backend and Application or External Integrations.

---

## Core Responsibilities

### Device Communication

Connectivity mechanisms enable communication between computation units and hardware peripherals such as sensors or actuators.

Examples include serial buses and device interfaces.

---

### Network Communication

Network interfaces allow the system to connect to local networks or the internet.

These connections enable communication with:

• remote APIs
• cloud services
• mobile devices
• administrative interfaces

---

### Distributed System Integration

Connectivity allows different computing nodes within the system to exchange information.

Examples include communication between:

• a Raspberry Pi and an Arduino
• a robot and a local server
• a robot and a remote backend

---

### Peripheral Integration

Connectivity interfaces enable the integration of external devices such as cameras, microphones, or storage units.

These connections provide the physical link required for hardware integration.

---

## Connectivity Technologies

### WiFi

WiFi provides wireless local network connectivity.

Through WiFi, NORA can connect to:

• local networks
• internet services
• other devices on the same network

WiFi is typically the primary connectivity method for network communication.

---

### Bluetooth

Bluetooth provides short-range wireless communication between devices.

Possible uses include:

• communication with mobile devices
• connection to wearable devices
• connection to nearby peripherals

Bluetooth is particularly useful for low-power or proximity-based communication.

---

### Ethernet

Ethernet provides a wired network connection.

Compared with wireless connections, Ethernet typically offers:

• lower latency
• higher stability
• greater bandwidth reliability

Ethernet may be used in development environments or installations where stable wired connectivity is available.

---

### Internet

Internet connectivity allows NORA to communicate with remote servers and cloud-based services.

Examples include:

• language model APIs
• weather services
• search engines
• remote monitoring systems

Internet access significantly expands the functional capabilities of the system.

---

### MQTT

MQTT is a lightweight messaging protocol designed for communication between devices in distributed systems and IoT environments.

It is commonly used for:

• device-to-device messaging
• home automation communication
• event distribution

MQTT is well suited for embedded systems due to its low bandwidth requirements and publish-subscribe communication model.

---

### Serial

Serial communication provides a direct communication channel between two hardware devices.

Serial connections are commonly used for communication between:

• microcontrollers
• embedded computers
• sensors
• actuator controllers

Serial interfaces are widely used in robotics and embedded systems.

---

### USB

USB (Universal Serial Bus) provides a flexible hardware interface for connecting peripherals.

Devices connected via USB may include:

• cameras
• microphones
• storage devices
• communication adapters

USB provides both power and data communication in a single interface.

---

### I2C

I2C (Inter-Integrated Circuit) is a communication bus commonly used in embedded electronics.

It allows multiple devices to communicate using a shared bus architecture.

Typical I2C devices include:

• sensors
• small controllers
• peripheral modules

I2C is widely used for low-speed communication between components on the same circuit board.

---

### SPI

SPI (Serial Peripheral Interface) is a synchronous communication protocol used for high-speed communication between microcontrollers and peripheral devices.

SPI is often used for devices requiring faster data exchange than I2C.

Examples include:

• display modules
• memory devices
• high-speed sensors

---

### GPIO

GPIO (General Purpose Input/Output) pins allow direct digital interaction with hardware components.

Through GPIO, the system can:

• read digital input signals
• control simple devices
• trigger hardware events

GPIO is frequently used for low-level hardware interaction and prototyping.

---

## Relationship With Other Modules

### Relationship With Computation

Connectivity interfaces are used by computation devices to communicate with hardware peripherals and networks.

---

### Relationship With Sensors

Many sensors connect to the system through connectivity interfaces such as I2C, SPI, USB, or GPIO.

---

### Relationship With Actuators

Actuators may also be controlled through connectivity interfaces, particularly when microcontrollers or relay modules are involved.

---

### Relationship With External Integrations

Connectivity provides the underlying communication mechanisms required to interact with external services and systems.

---

## Design Principles

### Reliability

Connectivity mechanisms should prioritize stability and predictable behaviour.

---

### Modularity

Communication interfaces should allow new hardware devices to be integrated without major architectural changes.

---

### Security

Network connectivity must incorporate appropriate security mechanisms to prevent unauthorized access.

---

### Scalability

The connectivity architecture should support future expansion of devices, sensors, and services.

---

## Architectural Importance

Connectivity enables NORA to function as part of a larger ecosystem of devices, services, and networks.

Through connectivity, the system can:

• communicate with external services
• control remote devices
• integrate with smart environments
• exchange information across distributed components

Without connectivity, NORA would be limited to isolated local operation and would not be able to leverage networked intelligence or device ecosystems.

For this reason, connectivity forms a key enabling layer in the Infrastructure and Hardware module.

# 11.5 External Controllable Devices

## Definition

The **External Controllable Devices** submodule defines the physical devices and appliances outside the robot itself that NORA can interact with, monitor, or control.

Within the Infrastructure and Hardware module, this submodule represents the **external physical systems that can be influenced by NORA through integrations, communication interfaces, or home automation protocols**.

If Sensors describe how NORA receives information and Actuators describe how it produces physical outputs within its own body, External Controllable Devices describe **the equipment in the surrounding environment that NORA can operate or coordinate**.

These devices may belong to smart homes, offices, laboratories, or other environments where the robot operates.

Examples include:

• turning lights on or off
• activating a coffee machine
• controlling climate systems
• operating smart plugs
• interacting with connected appliances

In architectural terms, these devices extend the physical reach of the system beyond the robot's own hardware.

---

## Architectural Purpose

The purpose of this submodule is to define the **set of external devices that the system can control or interact with in the physical environment**.

An embodied assistant often acts as a mediator between users and surrounding devices. Instead of requiring direct manual interaction with each device, the user can request actions through NORA, which then coordinates the required operations.

This capability allows the system to function as a central interface for environments such as:

• smart homes
• offices
• educational environments
• laboratories
• automation-enabled rooms

By integrating with external devices, NORA expands its ability to perform useful tasks that go beyond its internal capabilities.

---

## Role in the Global Architecture

Within the global architecture, external controllable devices represent **the outer layer of the system's physical influence**.

The flow of control can be described as:

User request
→ Interpretation and planning
→ Action execution
→ Communication with device
→ **External device performs operation**

These devices are typically controlled through the following architectural components:

• Action and Expression module
• Backend and Application services
• Connectivity interfaces
• External service integrations

The External Controllable Devices submodule therefore describes **what types of devices can exist in the environment and be controlled by the system**, even though the specific communication mechanisms are defined elsewhere.

---

## Scope of the Submodule

This submodule includes devices located outside the robot that can be controlled, activated, or queried by NORA.

Its scope includes:

• smart appliances
• home automation devices
• environmental control systems
• connected consumer electronics
• network-enabled equipment

It does **not** include:

• the communication protocols used to control them
• the software integrations required for each device
• the decision logic determining when to operate them

Those aspects belong to modules such as Connectivity, Integrations, Planning, and Action.

---

## Core Responsibilities

### Environmental Device Control

External devices allow the system to influence the environment in which it operates.

Examples include:

• switching lights on or off
• activating appliances
• adjusting environmental conditions

This expands the robot's ability to assist users in daily tasks.

---

### Smart Environment Integration

External devices are often part of larger ecosystems such as smart homes or building automation systems.

By integrating with these ecosystems, the robot can act as a unified interface for interacting with multiple devices.

---

### Task Delegation to Devices

Certain actions requested by users may be executed not by the robot itself but by external devices.

Examples include:

• brewing coffee
• starting a robot vacuum
• adjusting heating systems

In these cases, the robot acts as a **controller or coordinator rather than the direct executor of the physical action**.

---

## Device Categories

### Coffee Machine

A connected coffee machine allows NORA to trigger beverage preparation.

Possible operations may include:

• starting brewing
• selecting drink type
• scheduling preparation

This integration is useful in domestic or office environments.

---

### Lights

Smart lighting systems can be controlled by the robot to manage illumination conditions.

Typical actions include:

• turning lights on or off
• adjusting brightness
• changing colors

Lighting control can also be used to support contextual behaviours such as notifications or environmental adaptation.

---

### Smart Plugs

Smart plugs allow the system to control the electrical power supplied to connected devices.

Through these devices, NORA can:

• power appliances on or off
• schedule energy usage
• automate device activation

Smart plugs are often used to extend automation capabilities to devices that are not inherently smart.

---

### Television

A connected television can be controlled through network or smart-home integrations.

Possible interactions include:

• turning the television on or off
• selecting media sources
• adjusting volume
• launching streaming content

This allows NORA to function as a voice-based media controller.

---

### Smart Speaker

Smart speakers may act as additional audio output devices within the environment.

Integration with such devices allows the system to:

• extend voice output to other rooms
• synchronize audio playback
• delegate speech output to external speakers

---

### Climate Control Systems

Climate systems such as air conditioning, heating, or thermostats may be integrated into the system.

Possible control operations include:

• adjusting temperature
• switching climate systems on or off
• scheduling heating or cooling cycles

These capabilities improve environmental comfort and energy efficiency.

---

### Smart Locks

Connected locks can allow the robot to manage access control in a physical space.

Possible functions include:

• locking or unlocking doors
• verifying authorized access
• responding to remote access requests

Because access control is security-sensitive, these integrations typically require strict authentication policies.

---

### Smart Doorbells

Smart doorbells may provide video or notification capabilities when someone arrives at an entrance.

Integration may allow the robot to:

• notify users of visitors
• display camera feeds
• communicate with the doorbell system

---

### Robot Vacuum

A robot vacuum cleaner can be controlled by NORA to automate cleaning tasks.

Possible operations include:

• starting or stopping cleaning
• scheduling cleaning sessions
• returning to charging stations

---

### Home Sensors

External environmental sensors may also be integrated into the system.

Examples include:

• motion detectors
• door sensors
• temperature sensors
• smoke detectors

These sensors may provide additional environmental awareness beyond the robot's onboard sensors.

---

### Printer

A connected printer allows the robot to send documents or images for printing.

Possible uses include:

• printing documents
• printing images
• printing reminders or notes

---

### Future Kitchen Robot

A future integration could include connected kitchen appliances or cooking robots.

Such systems could allow the robot to:

• start cooking programs
• coordinate recipe steps
• assist users in food preparation

This type of integration expands the assistant role into domestic task automation.

---

## Relationship With Other Modules

### Relationship With Connectivity

Connectivity mechanisms such as WiFi, Bluetooth, or MQTT are typically used to communicate with external devices.

---

### Relationship With Integrations

Software integrations define how specific device ecosystems are accessed, such as smart home platforms.

---

### Relationship With the Planning System

Planning modules determine when and how external devices should be used to accomplish user requests.

---

### Relationship With Action and Expression

External device control often appears as an action in the Action and Expression module.

---

## Design Principles

### Device Abstraction

External devices should be abstracted into generic capabilities so that the system does not depend on specific brands or models.

---

### Security

Because many external devices involve sensitive operations such as door access or electrical control, secure authentication and authorization mechanisms are essential.

---

### Expandability

The architecture should allow new device types to be added without structural redesign.

---

### Reliability

Control of external devices should include confirmation mechanisms and error handling to ensure reliable operation.

---

## Architectural Importance

The External Controllable Devices submodule extends the operational scope of NORA beyond the robot itself.

Through these integrations, the system becomes capable of interacting with the broader environment and coordinating multiple devices.

This capability allows NORA to function not only as an interactive assistant but also as a **central controller for connected environments**.
