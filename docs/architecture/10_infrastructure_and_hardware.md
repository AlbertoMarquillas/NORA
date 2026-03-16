# 11. Infrastructure and Hardware

## Definition

The Infrastructure and Hardware module is the architectural domain that defines the physical substrate of NORA.

This module describes the material, electronic, computational, electromechanical, and low-level technical elements through which NORA exists as a real deployed system.

Within the global architecture, this module does not represent a secondary implementation detail, a later deployment note, or a purely operational appendix. It represents the architectural layer that defines the physical basis of execution, perception, communication, and action.

Other modules define how NORA interprets, remembers, reasons, plans, dialogues, visualizes, and integrates with external capabilities. The Infrastructure and Hardware module defines the physical entities through which those architectural functions become materially realizable.

In declarative architectural terms, this module defines what physical things exist in the system, what kind of physical roles they perform, how those physical elements are organized, what technical limits they impose, and how they connect the software architecture to the real world.

This module therefore defines the physical body, physical support structure, and low-level technical substrate of NORA.

### What This Module Contains

The Infrastructure and Hardware module contains the following architectural categories:

* computation devices
* embedded controllers
* sensors
* actuators
* connectivity mechanisms
* communication buses and interfaces
* network access elements
* external controllable devices
* deployment topology
* hardware constraints
* hardware operational states
* hardware maintenance structure

Each of these categories refers to a different kind of physical architectural entity.

### What a Computation Device Is

A computation device is a physical processing unit that executes software processes belonging to NORA.

A computation device provides:

* processing capacity
* executable runtime environment
* memory resources
* input and output interfaces
* local communication endpoints
* physical hosting for software modules

Within the architecture, a computation device is not defined by brand or vendor first. It is defined by role.

A computation device is the physical host of one or more software functions.

Examples of architectural roles performed by computation devices include:

* local orchestration
* inference execution
* backend service hosting
* dialogue management execution
* sensor data preprocessing
* control coordination
* state monitoring
* edge-level automation

### What an Embedded Controller Is

An embedded controller is a physical control-oriented processing unit dedicated to low-level hardware interaction.

An embedded controller is characterized by direct connection to electronic components, deterministic or near-deterministic control behaviour, stable execution of low-level logic, and proximity to sensors or actuators.

Within NORA, an embedded controller is the hardware entity responsible for direct device-level control functions such as:

* reading low-level sensor signals
* driving actuators
* executing timing-sensitive loops
* handling GPIO or bus communication
* propagating critical local control signals
* interfacing with mechanical or electrical subsystems

### What a Sensor Is

A sensor is a physical input component that transforms a measurable property of the world or of the system itself into a signal available for processing.

A sensor captures physical reality in signal form.

That physical reality may belong to:

* the surrounding environment
* a nearby user
* an external object
* the robot body or platform
* the internal operational state of hardware

A sensor therefore defines a physical observation channel.

### What an Actuator Is

An actuator is a physical output component that transforms a system command into a physical effect.

That effect may be:

* mechanical
* visual
* acoustic
* electrical
* tactile
* light-based
* switching-based

An actuator therefore defines a physical action channel.

### What a Connectivity Mechanism Is

A connectivity mechanism is a physical or protocol-level communication path through which hardware elements exchange data, status, synchronization signals, or commands.

A connectivity mechanism may exist:

* between internal components of NORA
* between distributed compute nodes
* between NORA and external devices
* between NORA and local or remote infrastructure

Connectivity mechanisms define the physical and technical pathways through which the hardware system functions as a connected whole.

### What an External Controllable Device Is

An external controllable device is a device outside the main hardware body of NORA that participates in system behaviour through monitoring, command reception, state exchange, or coordinated operation.

Such a device is not a passive background object. It is part of the operational environment of the architecture.

Examples of architectural roles played by controllable external devices include:

* appliance receiving commands
* smart environment endpoint
* external sensor platform
* domestic infrastructure element
* remotely managed physical system

### What Deployment Topology Is

Deployment topology is the physical arrangement and interconnection structure of the hardware system.

It describes:

* where physical components are located
* which components are co-located
* which components are distributed
* how components are linked
* what communication boundaries exist
* what maintenance boundaries exist
* what hardware groupings form operational units

Deployment topology is therefore the spatial and structural organization of the system.

### What a Hardware Constraint Is

A hardware constraint is a limitation imposed by the material, computational, electrical, thermal, mechanical, or communication properties of the system.

A hardware constraint is not an accidental side note. It is an architectural condition that defines what the system can sustain, how quickly it can react, what precision it can achieve, and under what conditions it remains operational.

### What a Hardware Operational State Is

A hardware operational state is the current condition of a physical component with respect to availability and function.

Examples of hardware operational state categories include:

* present
* connected
* powered
* active
* idle
* degraded
* unavailable
* failed
* disconnected
* overheated
* low-power

The architecture includes hardware operational states because higher system behaviour depends on the real condition of physical components.

---

## Architectural Purpose

The purpose of the Infrastructure and Hardware module is to define the physical execution environment of NORA as an explicit architectural domain.

NORA is a multimodal cognitive system with physical embodiment potential, environmental sensing, system actuation, distributed execution, and interaction with real devices. Because of that, the architecture includes not only abstract software structures but also the material structures that host, feed, constrain, and implement those software structures.

This module defines the physical execution environment across five major architectural domains:

* computational execution
* physical sensing
* physical actuation
* hardware communication
* deployment embodiment

Each of these domains corresponds to a different architectural requirement.

### Computational Execution

Computational execution is the existence of physical processing capacity through which NORA software runs.

This includes the hardware required for:

* application runtime
* local control
* dialogue execution
* inference execution
* coordination logic
* background services
* monitoring tasks
* distributed processing

### Physical Sensing

Physical sensing is the existence of hardware channels that convert environmental or internal conditions into machine-processable signals.

This includes sensing of:

* sound
* image and video
* touch
* motion
* proximity
* identity-related physical tokens
* environmental variables
* device-internal state

### Physical Actuation

Physical actuation is the existence of hardware channels through which NORA produces effects in the world.

This includes:

* sound output
* screen output
* light emission
* movement
* switching behaviour
* haptic signalling
* command propagation toward external devices

### Hardware Communication

Hardware communication is the existence of internal and external communication paths that make the distributed hardware system operationally coherent.

This includes:

* internal buses
* peripheral interfaces
* board-to-board communication
* local wireless links
* network interfaces
* internet paths
* protocol-based device communication

### Deployment Embodiment

Deployment embodiment is the existence of a concrete physical form through which the architecture is realized.

This includes:

* hardware distribution across nodes
* device placement
* enclosure or body integration
* wiring organization
* maintenance boundaries
* physical accessibility
* component replacement structure

Without this module, the architecture would describe what NORA does at the logical level but would not define the physical means through which that behaviour exists in reality.

This module therefore grounds the whole architecture in material execution reality.

---

## Why This Module Exists in NORA

This module exists because NORA is defined as a real embodied or embeddable system rather than as a purely abstract software assistant.

A purely abstract assistant can leave hardware implicit. NORA cannot.

In NORA, physical substrate determines architectural possibility.

The hardware architecture determines:

* what signals can be captured
* what outputs can be generated
* what timing guarantees are possible
* what processing can occur locally
* what dependencies exist on remote systems
* what actions are physically feasible
* what kinds of failure can occur
* what safety boundaries apply
* what maintenance operations are required
* what deployment forms are valid

This means hardware is not merely where the software happens to run. Hardware defines the real-world operational envelope of the system.

### Architecture-Relevant Physical Facts in NORA

In NORA, the following are architectural facts rather than incidental engineering details:

* the system listens through physical audio hardware
* the system sees through physical optical hardware
* the system detects nearby conditions through dedicated sensors
* the system acts through physical output and control hardware
* the system runs on concrete processing devices
* the system exchanges signals through concrete buses and networks
* the system coordinates with devices outside its main body
* the system depends on physical availability, power, connectivity, and timing conditions

These facts affect multiple modules across the architecture.

For that reason, Infrastructure and Hardware exists as a first-class architectural module.

---

## Scope of the Module

The Infrastructure and Hardware module defines the physical and low-level technical substrate required for NORA to exist as a deployed operational system.

Its scope includes the following architectural domains.

### In Scope

* physical computation hardware
* embedded control hardware
* onboard or local processing units
* distributed processing nodes
* hardware accelerators when present
* physical sensors
* internal status sensing hardware
* physical actuators
* device-level output hardware
* mechanical motion components
* switching and relay components
* wired communication buses
* short-range communication links
* network interfaces
* device-to-device communication interfaces
* internet access pathways as hardware/network substrate
* controllable external appliances and smart devices
* physical deployment structure
* hardware grouping and distribution
* hardware constraints
* hardware replacement and maintenance boundaries
* hardware fault isolation structure

### Out of Scope

The following elements do not belong to this module because they belong to other architectural domains:

* user interaction design
* dialogue modelling
* semantic interpretation
* signal interpretation logic
* planning logic
* cognitive-state logic
* application service logic
* API surface definition
* persistence logic
* frontend rendering logic
* external cloud-service capability definitions

### Meaning of This Boundary

This module defines with what physical substrate the system exists.

It does not define:

* how signals are semantically interpreted
* how responses are linguistically formulated
* how plans are selected
* how memories are stored logically
* how interfaces are visually designed
* how application use cases are orchestrated at the software level

This boundary is essential because it preserves architectural clarity between physical support structure and higher-level system behaviour.

---

## Architectural Role Within the Global System

Within the global NORA architecture, the Infrastructure and Hardware module acts as the material support layer.

It is the architectural layer that stands between the software-defined system and the physical world.

This role can be expressed as:

Physical world ↔ physical sensing, compute, communication, and actuation substrate ↔ NORA software architecture

This module performs several structural roles in that position.

### 1. Physical Hosting Role

The module provides the physical machines and controllers on which software modules execute.

This includes hosting of:

* perception-related software
* dialogue-related software
* backend services
* memory services
* orchestration logic
* local control logic
* monitoring logic
* action coordination logic

The physical hosting role answers the question: on what actual hardware do system processes run?

### 2. Physical Input Role

The module provides the hardware entry points through which signals become available to the software system.

These entry points are the raw physical origins of perception and status awareness.

The physical input role answers the question: through what physical channels does the system obtain real-world and internal-state information?

### 3. Physical Output Role

The module provides the hardware channels through which software decisions become material effects.

These effects may be expressive, mechanical, electrical, or environmental.

The physical output role answers the question: through what physical channels does the system produce observable consequences?

### 4. Physical Interconnection Role

The module provides the communication pathways through which the hardware system functions as a connected whole.

This includes both internal hardware communication and communication with external infrastructure.

The physical interconnection role answers the question: how are the physical parts of the system linked together?

### 5. Constraint Propagation Role

The module defines the physical limits that constrain higher-level behaviour.

Those limits propagate upward into perception, cognition, planning, action, dialogue timing, and system availability.

The constraint propagation role answers the question: what material limits shape the behaviour of the architecture?

### 6. Deployment Realization Role

The module defines how the architecture becomes deployable as a real installed or assembled system.

This includes physical arrangement, component grouping, maintenance structure, and node distribution.

The deployment realization role answers the question: what real physical platform realizes the architecture?

---

## Core Responsibilities

The Infrastructure and Hardware module performs a set of explicit architectural responsibilities.

### 1. Definition of Computational Execution Capacity

This module defines the physical devices that execute NORA software.

A computational execution device is any hardware unit that hosts software processes belonging to the architecture.

This responsibility includes definition of:

* compute boards
* embedded computers
* microcontrollers
* local processing nodes
* dedicated control processors
* remote supporting processors when they are part of the deployment architecture
* optional acceleration units

This responsibility also defines:

* which workloads execute on which devices
* which devices perform higher-level processing
* which devices perform low-level control
* which devices provide local autonomy
* which devices provide support functions such as monitoring or diagnostics

This responsibility establishes the physical execution map of the system.

### 2. Definition of Physical Sensing Capacity

This module defines the physical devices that acquire signals from the world and from the system itself.

A sensing capacity is the set of hardware observation channels available to the architecture.

This responsibility includes definition of sensing categories such as:

* acoustic sensing
* visual sensing
* proximity sensing
* environmental sensing
* tactile sensing
* motion-related sensing
* identification-related sensing
* internal diagnostic sensing

This responsibility defines:

* what can be sensed physically
* through which device category it is sensed
* from what physical location or subsystem it is sensed
* with what kind of update, range, or channel constraints it is sensed

This responsibility establishes the raw physical observability of the platform.

### 3. Definition of Physical Actuation Capacity

This module defines the physical devices that generate effects in the world.

An actuation capacity is the set of hardware action channels available to the system.

This responsibility includes definition of actuation categories such as:

* audio output
* visual display output
* light signalling
* mechanical movement
* relay or switch control
* haptic output
* external-device command propagation

This responsibility defines:

* what kind of effects the system can generate
* through which physical device classes those effects are produced
* what movement or signal limits exist
* what local control interfaces connect to those output paths

This responsibility establishes the physical expressivity and control reach of the platform.

### 4. Definition of Communication Structure

This module defines the internal and external communication pathways of the hardware system.

A communication structure is the set of physical and protocol-level links that connect compute units, peripherals, sensors, actuators, and external devices.

This responsibility includes definition of:

* internal buses
* serial interfaces
* wired peripheral links
* wireless local links
* Ethernet or equivalent network interfaces
* internet connectivity endpoints
* local machine-to-machine communication channels
* hardware-to-backend communication paths when applicable

This responsibility defines:

* which physical components are linked
* through which communication medium they are linked
* which boundaries separate local and remote communication
* which communication dependencies exist for normal operation
* which critical signals require reliable propagation paths

This responsibility establishes the physical communication graph of the deployment.

### 5. Definition of Embodiment Constraints

This module defines the physical constraints that shape the rest of the architecture.

An embodiment constraint is a system limitation arising from hardware reality.

This responsibility includes definition of constraints such as:

* processing power limits
* memory limits
* storage constraints when hardware-bound
* battery or power limits
* thermal limits
* sensor range limits
* sensor precision limits
* sensor refresh-rate limits
* field-of-view limits
* audio capture quality limits
* actuation range limits
* actuation precision limits
* communication latency limits
* connectivity availability limits
* bandwidth limits
* mechanical wear constraints

This responsibility ensures that all higher-level modules are grounded in actual material limits.

### 6. Definition of Deployment and Maintenance Structure

This module defines the hardware organization through which NORA can be assembled, deployed, maintained, monitored, repaired, and evolved.

A deployment and maintenance structure is the physical organization of components into a serviceable platform.

This responsibility includes definition of:

* hardware modular grouping
* node boundaries
* replaceable component boundaries
* physical access points
* wiring organization
* bus topology
* maintenance access structure
* discoverability of connected devices
* monitoring access points
* fault-isolation boundaries

This responsibility establishes how the platform continues to operate as a maintained real-world system.

---

## Architectural Properties of the Module

The Infrastructure and Hardware module has a number of structural properties that characterize its place in the architecture.

### Materiality

This module describes physical entities rather than purely logical abstractions.

Its entities occupy space, consume power, generate heat, expose interfaces, transmit signals, and degrade or fail under physical conditions.

### Embodiment

This module defines the body-level substrate of NORA.

Embodiment here means that the system is not only an information-processing architecture but also a physically situated platform with sensing surfaces, output channels, and concrete deployment form.

### Distribution

This module represents the system as potentially distributed across multiple hardware nodes.

A distributed hardware node is a physically distinct unit that hosts a subset of system functionality and communicates with other units through defined links.

This allows the architecture to describe systems that are:

* single-device
* multi-board
* edge-plus-controller
* hybrid local-remote
* robot-plus-infrastructure

### Constraint Propagation

The physical limitations defined in this module propagate into the rest of the architecture.

For example:

* a camera limitation affects perception
* a compute limitation affects inference and planning latency
* a network limitation affects backend coordination
* an actuator precision limit affects action quality
* a power constraint affects system availability

This makes physical limitation an architecture-wide influence.

### Operational Dependency

All deployed software modules depend on physical infrastructure.

This means that every runtime function in NORA is operationally dependent on the existence, availability, and condition of hardware entities defined in this module.

### Maintainability

The module includes structure for replacement, diagnosis, and ongoing operation.

A real system is not only assembled once. It exists through sustained operation, partial failure, repair, and evolution.

Maintainability is therefore an architectural property rather than an afterthought.

---

## Design Principles

This module follows a set of declarative architectural principles.

### Separation Between Capability and Hardware Instance

The architecture distinguishes between:

* a required capability
* the hardware instance that realizes that capability

A capability is an architectural function such as local orchestration, visual sensing, audio output, or relay control.

A hardware instance is the concrete physical component that provides that capability.

This distinction matters because the architecture remains stable even if a board, sensor, or actuator is replaced by another component with the same role.

### Hardware Modularity

The hardware architecture is organized into identifiable component groups.

A modular hardware group is a bounded physical subsystem with a recognizable role, connection structure, and maintenance boundary.

Examples of modular grouping include:

* compute subsystem
* sensor subsystem
* actuation subsystem
* communication subsystem
* external-device control subsystem

This principle makes the platform structurally evolvable and maintainable.

### Distribution Awareness

The architecture explicitly represents hardware as distributable across multiple physical units.

Different hardware nodes may specialize in:

* local orchestration
* low-level IO
* movement control
* sensor acquisition
* heavy inference
* backend exposure

This principle means physical distribution belongs to architecture, not only to deployment notes.

### Timing Realism

Different hardware-dependent operations belong to different timing classes.

A timing class is the temporal behaviour associated with a physical operation.

Examples include:

* immediate stop propagation
* stable control-loop timing
* low-latency interaction detection
* sustained audiovisual streaming
* asynchronous network coordination

The architecture therefore includes timing reality as part of the hardware model.

### Safety Grounding

The presence of physical sensing and actuation means the system interacts with real environments and devices.

Because of that, the hardware layer includes safety-relevant structure.

This includes:

* safe inactive states
* constrained actuation paths
* protected electrical or motion channels
* failure containment boundaries
* degradation-aware operational limits
* reliable propagation of critical control signals

### Evolvability of Hardware Realization

The architecture is defined at the level of physical role and structural relation, not only at the level of vendor-specific hardware naming.

This allows the platform to evolve while preserving conceptual continuity.

A sensor replacement changes the hardware instance.
A board upgrade changes the hardware instance.
A bus substitution changes the implementation path.

The architecture changes only if the structural capability model changes.

---

## Relationship With Other Architectural Modules

The Infrastructure and Hardware module interacts structurally with many other modules of NORA.

### Relationship With Perception

The Infrastructure and Hardware module defines the physical sources of raw signals.

The Perception module defines the processing and interpretation of those signals.

This relationship can be expressed as:

* hardware defines the sensing source
* perception defines the signal interpretation pipeline

A microphone belongs here.
Speech recognition logic belongs to Perception and adjacent cognitive modules.

A camera belongs here.
Image interpretation belongs to Perception.

### Relationship With Action and Expression

The Infrastructure and Hardware module defines the physical output and motion channels.

The Action and Expression module defines how the system uses those channels behaviourally.

This relationship can be expressed as:

* hardware defines the output mechanism
* action defines the behavioural execution through that mechanism

A speaker belongs here.
Speech generation strategy belongs to Action and Expression.

A servo belongs here.
Motion behaviour belongs to Action and Expression.

### Relationship With the Cognitive Core

The Infrastructure and Hardware module defines component condition, availability, and physical constraints.

The Cognitive Core incorporates those realities into state regulation, mode selection, inhibition, prioritization, and behavioural adjustment.

This relationship can be expressed as:

* hardware defines physical operational reality
* the cognitive core uses that reality in behavioural regulation

### Relationship With Backend and Application

The Infrastructure and Hardware module defines the actual physical substrate being supervised, coordinated, or exposed.

The Backend and Application module defines software interfaces and application-level coordination over that substrate.

This relationship can be expressed as:

* hardware defines what physical entities exist
* backend defines how those entities are monitored, accessed, or coordinated through software services

### Relationship With Frontend and Visualization

The Infrastructure and Hardware module defines the physical entities and statuses that may be represented visually.

The Frontend and Visualization module defines how those entities become visible, navigable, and interpretable through interfaces.

This relationship can be expressed as:

* hardware defines what exists physically
* frontend defines how that physical reality is represented to users or administrators

### Relationship With Integrations and External Services

The Infrastructure and Hardware module defines the local communication substrate and external-device base through which integrations interact with the physical world.

The Integrations and External Services module defines the external service-level capabilities that connect to or operate over those channels.

This relationship can be expressed as:

* hardware defines the local physical communication and device-control substrate
* integrations define the external service and protocol ecosystem layered over it

---

## Internal Structure

The Infrastructure and Hardware module is divided into five submodules. Each submodule defines a distinct class of physical architectural entities.

### 11.1 Computation

The Computation submodule defines the physical processing units that execute NORA software.

It defines:

* where software modules run
* how computation is distributed
* which nodes perform local control
* which nodes perform orchestration
* which nodes perform heavier processing
* which nodes provide support services

### 11.2 Sensors

The Sensors submodule defines the physical input devices that capture signals from the environment, from nearby users, and from the internal platform.

It defines:

* what categories of physical observation exist
* what sensor types belong to the system
* what internal-state measurements are available
* what sensing channels feed the higher architecture

### 11.3 Actuators

The Actuators submodule defines the physical output and movement-producing devices through which NORA creates effects in the world.

It defines:

* what hardware output channels exist
* what movement mechanisms exist
* what signalling hardware exists
* what control outputs can be physically emitted

### 11.4 Connectivity

The Connectivity submodule defines the communication technologies, buses, interfaces, and links that connect internal components and external systems.

It defines:

* what physical communication paths exist
* what network interfaces exist
* what peripheral buses exist
* what local and remote communication boundaries exist

### 11.5 Controllable External Devices

The Controllable External Devices submodule defines the external appliances, infrastructures, and smart devices that participate in the operational environment of NORA through monitoring, coordination, or control.

It defines:

* what external device classes form part of the controllable ecosystem
* what kinds of physical systems can receive commands
* what kinds of external device states may be observed

Together, these submodules form the complete architectural description of the physical and technical substrate of NORA.

---

## Representative Architectural Questions Answered by This Module

The Infrastructure and Hardware module defines the architectural answers to questions such as:

* what physical devices execute the system?
* what hardware units perform low-level control?
* what hardware units perform higher-level computation?
* what signals can the system capture from the environment?
* what signals can the system capture from its own internal state?
* what physical effects can the system generate?
* what kinds of movement, display, sound, lighting, or switching are physically available?
* how are hardware elements connected to each other?
* what communication dependencies exist between local and remote components?
* what external devices are part of the controllable operational environment?
* what physical constraints shape system behaviour?
* how is the deployed platform distributed, maintained, monitored, and repaired?

These are architectural questions because they define the real material structure of the system rather than incidental implementation detail.

---

## Architectural Importance

The Infrastructure and Hardware module is the architectural domain that allows NORA to exist as a real embodied platform.

Without this module, the architecture could still describe:

* interaction
* perception
* cognition
* dialogue
* planning
* memory
* backend behaviour
* frontend behaviour
* integrations

But it would still lack the physical substrate that hosts those functions, feeds them with signals, constrains them through material limits, and materializes them as real effects.

Through the explicit existence of this module, the architecture gains:

* explicit embodiment
* explicit physical execution structure
* explicit computation hosting
* explicit physical sensing structure
* explicit actuation structure
* explicit communication infrastructure
* explicit deployment topology
* explicit material constraints
* explicit maintenance structure
* explicit physical-system traceability

For that reason, the Infrastructure and Hardware module is a foundational architectural domain of NORA.

# 11.1 Computation

## Definition

The Computation submodule defines the physical processing devices that execute the software architecture of NORA.

A computation device is a physical hardware unit capable of executing software instructions belonging to the system. These devices provide processing capacity, memory resources, runtime environments, and communication interfaces required for the execution of system behaviour.

Within the Infrastructure and Hardware module, the Computation submodule defines the physical execution layer of the architecture.

If sensors define how physical signals enter the system and actuators define how the system produces effects in the physical world, the Computation submodule defines the physical machines that host the software processes responsible for perception, cognition, dialogue, planning, coordination, and control.

In architectural terms, the Computation submodule answers the question:

Where does the software of NORA actually run?

The answer is defined through a set of computation devices that together form the processing substrate of the system.

---

## Core Architectural Concepts

To define this submodule declaratively, several core concepts are introduced.

### Computation Device

A computation device is a physical processing unit that executes software instructions belonging to the architecture.

A computation device provides:

• a processor capable of executing instructions
• memory resources for program execution
• runtime environment for software processes
• communication interfaces to other system components
• input and output channels to hardware devices

A computation device hosts one or more software modules belonging to the architecture.

Examples of hosted modules include perception pipelines, cognitive processes, dialogue managers, planning systems, backend services, and hardware control interfaces.

### Processing Node

A processing node is a computation device considered as a participant in the distributed execution of the system.

A node may host multiple software modules and may communicate with other nodes through defined communication interfaces.

In distributed deployments, NORA may consist of multiple processing nodes connected through network or bus communication mechanisms.

### Embedded Computer

An embedded computer is a compact computing platform capable of running a general-purpose operating system and executing complex software stacks.

Embedded computers typically perform mid‑level and high‑level processing tasks such as perception pipelines, orchestration logic, dialogue systems, and backend services.

### Microcontroller

A microcontroller is a compact processing unit designed for embedded control tasks with tight timing constraints and direct hardware interaction.

Microcontrollers typically execute firmware programs responsible for deterministic control of sensors, actuators, and low‑level hardware interfaces.

### Hardware Accelerator

A hardware accelerator is a specialized processing device designed to perform specific categories of computation more efficiently than general‑purpose processors.

Examples include GPUs and AI inference accelerators used for machine learning workloads, vision processing, or large‑scale numerical operations.

### Edge Processing

Edge processing refers to computation performed close to the physical environment where the system operates.

Edge computation reduces latency, increases reliability during network disruption, and enables local autonomy of the system.

---

## Architectural Purpose

The purpose of the Computation submodule is to define the hardware devices that execute the software architecture of NORA.

An embodied cognitive system performs many different classes of computation. These computations differ significantly in timing requirements, processing complexity, reliability requirements, and energy consumption.

Because of these differences, the architecture includes multiple classes of computation devices.

Different devices may specialize in different forms of processing, including:

• low‑level hardware control
• real‑time sensor acquisition
• perception processing
• dialogue management
• planning and reasoning
• machine learning inference
• system coordination
• network communication
• backend service execution

By defining computation devices explicitly, the architecture clarifies how software modules are distributed across the available processing resources.

---

## Role Within the Global Architecture

Within the full NORA architecture, computation devices form the execution substrate of the system.

Software modules belonging to many architectural domains run on these devices.

Examples include modules belonging to:

• Perception
• Cognitive Core
• Dialogue and Session System
• Planning, Interpretation and Agents
• Backend and Application
• Hardware control layers

This relationship can be expressed as:

Software modules → executed on → computation devices

The Computation submodule therefore connects the logical architecture of NORA with the physical machines capable of executing it.

---

## Scope of the Submodule

The Computation submodule includes hardware units responsible for executing software processes belonging to the architecture.

### In Scope

The submodule includes:

• embedded computers
• microcontrollers
• compact compute modules
• mini PCs
• onboard processing boards
• dedicated inference devices
• hardware accelerators when present
• distributed processing nodes participating in system execution

### Out of Scope

The submodule does not include:

• sensors
• actuators
• communication buses
• networking infrastructure
• cloud services

These elements belong to other submodules such as Sensors, Actuators, Connectivity, and Integrations.

---

## Core Responsibilities

### Execution of Software Modules

All software modules belonging to the architecture ultimately execute on computation hardware.

These modules include components responsible for:

• perception pipelines
• signal preprocessing
• speech processing
• visual processing
• dialogue management
• planning and reasoning
• agent coordination
• backend services
• API handling
• system monitoring
• hardware control interfaces

The Computation submodule therefore provides the runtime execution environment for the entire software architecture.

### Distribution of System Workloads

A complex embodied system distributes computation across several hardware devices.

Workload distribution may include patterns such as:

• delegating low‑level control tasks to microcontrollers
• executing perception pipelines on embedded computers
• performing high‑level reasoning on more powerful processors
• offloading specialized workloads to hardware accelerators

This distribution allows the architecture to achieve better performance, modularity, and fault isolation.

### Real‑Time Hardware Control

Certain hardware interactions require stable and predictable timing.

Examples include:

• servo control
• motor control
• sensor polling
• safety monitoring

These tasks may run on microcontrollers or dedicated embedded processors that execute deterministic control loops.

### High‑Level Cognitive Processing

High‑level computational devices execute tasks that require larger computational resources.

Examples include:

• natural language processing
• planning algorithms
• multimodal perception pipelines
• machine learning inference
• state management

These tasks typically run on devices capable of supporting full operating systems and complex runtime environments.

---

## Categories of Computation Devices

The architecture identifies several categories of computation devices.

### Raspberry Pi

A Raspberry Pi is a compact embedded computer capable of running a full operating system such as Linux.

Within the architecture, a Raspberry Pi may function as a central embedded compute node.

Possible responsibilities include:

• executing perception pipelines
• running backend services
• coordinating dialogue systems
• interfacing with sensors and actuators
• managing local network communication

The Raspberry Pi provides a balance between computational power, energy efficiency, and hardware interfacing capability.

### Arduino

An Arduino is a microcontroller platform designed for direct hardware interaction.

Unlike embedded computers, Arduino devices typically execute firmware programs rather than full operating systems.

Within the architecture, Arduino devices may perform low‑level control tasks such as:

• servo control
• motor control
• LED control
• relay switching
• sensor sampling

These devices may receive commands from higher‑level computation devices such as embedded computers.

### Microcontrollers

Microcontrollers are embedded processing units specialized for deterministic control tasks.

They are typically used in situations where:

• precise timing is required
• power consumption must remain low
• direct hardware access is necessary

In the NORA architecture, microcontrollers may support tasks such as sensor polling, actuator control, safety monitoring, and communication with higher‑level processors.

### Mini PC

A mini PC is a compact computing device capable of running full desktop‑class operating systems.

Within the architecture, a mini PC may provide higher computational capacity than smaller embedded devices.

Possible use cases include:

• running large language models locally
• performing intensive perception processing
• hosting multiple backend services
• executing complex planning systems

A mini PC may act as the primary compute node in more advanced deployments of the system.

### External GPU

A GPU is a specialized processor optimized for highly parallel computation.

Within the architecture, a GPU may act as a hardware accelerator for tasks such as:

• deep learning inference
• computer vision pipelines
• multimodal data processing

An external GPU may significantly increase the computational capacity of the system.

### Edge Devices

Edge devices are computing units located close to the operational environment of the system.

Edge computation reduces latency and allows the system to operate independently of remote cloud services.

Examples of edge devices include onboard embedded computers, local servers, and dedicated inference hardware.

---

## Relationship With Other Modules

### Relationship With Sensors

Sensors capture physical signals from the environment or from the system itself.

Computation devices execute software responsible for processing those signals.

### Relationship With Actuators

Computation devices generate control commands that drive actuators.

Higher‑level commands may be translated into low‑level control signals executed by microcontrollers.

### Relationship With the Cognitive Core

The Cognitive Core represents logical reasoning and system state management.

Its algorithms and processes execute on computation hardware.

### Relationship With Backend and Application

Backend services and APIs execute on computation devices that host server processes and communication services.

---

## Design Principles

### Layered Processing

The architecture distributes computation across layers ranging from low‑level hardware control to high‑level reasoning.

### Hardware Specialization

Different computation devices specialize in tasks that match their capabilities.

Examples include:

• microcontrollers for deterministic hardware control
• embedded computers for perception and system coordination
• GPUs for heavy machine learning workloads

### Fault Isolation

Separating low‑level hardware control from high‑level reasoning reduces the risk that software failures affect physical safety.

### Scalability

The architecture allows additional computation devices to be integrated without redesigning the entire system.

---

## Architectural Importance

The Computation submodule defines the physical infrastructure that executes the software architecture of NORA.

All perception, cognition, dialogue, planning, and control processes ultimately depend on the existence of computation hardware capable of executing them.

For this reason, the Computation submodule forms a foundational element of the Infrastructure and Hardware module and enables the transformation of NORA from a conceptual architecture into a real operational system.

# 11.2 Sensors

## Definition

The Sensors submodule defines the physical input devices through which NORA receives measurable signals from the external environment, from nearby users, and from its own internal physical condition.

A sensor is a hardware component that converts a physical phenomenon into a measurable signal that can be processed by the system.

Sensors represent the physical observation surface of NORA.

Within the Infrastructure and Hardware module, sensors are the components that create the raw informational interface between the physical world and the digital system.

If computation devices define where software processes execute and actuators define how the system produces effects in the world, sensors define how physical signals become available to the architecture.

In architectural terms, the Sensors submodule answers the question:

What physical signals can NORA observe and measure?

---

## Core Architectural Concepts

### Sensor

A sensor is a hardware device that detects a measurable physical property and converts it into an electrical or digital signal.

A sensor therefore performs three operations:

• detection of a physical phenomenon
• transformation of that phenomenon into an electrical signal
• delivery of that signal to a computation device

Sensors provide the raw signals that later become perceptual information after interpretation by higher-level modules.

### Sensing Channel

A sensing channel is the pathway through which a specific type of physical signal enters the system.

Examples of sensing channels include:

• acoustic channel
• visual channel
• proximity channel
• tactile channel
• environmental channel
• identity channel
• internal-state monitoring channel

Each sensing channel corresponds to a different class of observable physical signals.

### Sensing Modality

A sensing modality is the type of physical phenomenon that a sensor measures.

Examples of sensing modalities include:

• sound
• light
• electromagnetic fields
• pressure or contact
• distance
• temperature
• humidity
• electrical state
• motion

Each modality corresponds to a different way the system can perceive the world.

### Environmental Sensing

Environmental sensing refers to the measurement of conditions in the surrounding physical environment.

Examples include temperature, humidity, ambient light, and proximity detection.

These sensors provide contextual information about the operating conditions of the system.

### Interaction Sensing

Interaction sensing refers to sensors that detect actions performed by users interacting with the system.

Examples include microphones for speech input, cameras for gesture detection, and tactile sensors for touch interaction.

### Internal State Sensing

Internal state sensing refers to sensors that monitor the physical condition of the system itself.

Examples include battery monitoring, temperature sensors inside the enclosure, or future motion sensors.

These sensors allow the system to monitor its own operational status.

---

## Architectural Purpose

The purpose of the Sensors submodule is to define the complete physical sensing surface of NORA.

An embodied cognitive system interacts with its environment through sensing and actuation. Sensing enables the system to detect events, conditions, and interactions occurring in the physical world.

The Sensors submodule documents:

• which sensors exist
• which physical phenomena they measure
• which sensing channels they support
• which roles they perform in the architecture

Without sensors, NORA would have no direct access to the surrounding environment or to its own physical state.

The existence of sensors therefore determines which aspects of reality the system can observe and react to.

---

## Role Within the Global Architecture

Within the full architecture, sensors represent the origin of observable data.

Information flow can be described as:

Physical world / system body
→ Sensors
→ Perception module
→ Cognitive processing

Sensors capture raw signals.

Perception interprets those signals and transforms them into structured information.

Cognitive modules then reason about that information.

Sensor outputs may also contribute to:

• system safety monitoring
• backend telemetry
• system observability
• operational diagnostics

Because sensors determine what information is available to the system, the design of this submodule directly influences the behavioural capabilities of NORA.

---

## Scope of the Submodule

The Sensors submodule includes all hardware devices that capture measurable input signals.

### In Scope

• microphones
• cameras
• proximity sensors
• tactile sensors
• environmental sensors
• power-state monitoring sensors
• identity-detection hardware such as NFC
• motion sensing hardware

### Out of Scope

The submodule does not include:

• interpretation of signals
• classification or recognition algorithms
• behavioural decision logic
• actuator control

These functions belong to other modules such as Perception, Planning, and Action.

---

## Core Responsibilities

### Signal Acquisition

The primary responsibility of sensors is to capture measurable physical signals.

Examples of measurable phenomena include:

• acoustic waves
• visible light
• electromagnetic near-field communication
• physical pressure
• object distance
• temperature
• humidity
• electrical voltage

Sensors convert these phenomena into signals that computation devices can process.

### Environmental Awareness

Environmental sensors measure conditions present in the surrounding environment.

Examples include:

• temperature sensors
• humidity sensors
• ambient light sensors
• proximity sensors

These measurements provide contextual information that may influence system behaviour.

### Human Interaction Detection

Some sensors directly support human interaction with the system.

Examples include:

• microphones capturing speech
• cameras observing gestures or faces
• NFC readers detecting identity tokens
• tactile sensors detecting touch

These sensors enable natural multimodal interaction between humans and the system.

### Internal State Monitoring

Certain sensors measure internal physical conditions of the system.

Examples include:

• battery state sensors
• thermal sensors
• motion sensors
• hardware diagnostics sensors

These measurements support stability, maintenance monitoring, and safe operation.

---

## Sensor Types

### Microphones

Microphones capture acoustic signals from the surrounding environment.

These signals form the acoustic sensing channel of the system.

Typical uses include:

• wake-word detection
• speech recognition
• acoustic environment monitoring
• speaker identification

### Cameras

Cameras capture visual information in the form of images or video streams.

These signals form the visual sensing channel of the system.

Visual data may support:

• person detection
• face detection
• gesture recognition
• scene analysis
• optical character recognition
• QR code scanning

### NFC Sensors

NFC sensors detect nearby NFC-enabled tags or cards through near-field electromagnetic communication.

These sensors support identity recognition and device pairing.

Typical uses include:

• user identification
• quick authentication
• profile activation
• access control

### Temperature Sensors

Temperature sensors measure thermal conditions either in the surrounding environment or inside the device enclosure.

Temperature measurements support:

• environmental awareness
• hardware protection
• thermal monitoring

### Humidity Sensors

Humidity sensors measure the moisture level in the surrounding air.

These measurements support environmental monitoring and climate awareness.

### Light Sensors

Light sensors measure ambient illumination levels.

Ambient light information may be used for:

• adaptive display brightness
• camera exposure adjustment
• day or night detection

### Proximity Sensors

Proximity sensors detect nearby objects or users without physical contact.

Technologies may include infrared detection, ultrasonic distance measurement, or time-of-flight sensing.

These sensors support:

• presence detection
• user approach detection
• collision avoidance

### Tactile Sensors

Tactile sensors detect direct physical interaction with the system.

Examples include capacitive touch sensors, pressure sensors, or contact switches.

These sensors allow physical interaction with the system for actions such as activation, confirmation, or interruption.

### Battery Sensors

Battery monitoring sensors measure the energy state of the device.

Typical measurements include:

• battery level
• voltage
• charging status
• discharge rate

Battery sensing enables energy management and safe operation.

### Future IMU

An inertial measurement unit measures motion-related properties such as acceleration and angular velocity.

An IMU may support:

• motion monitoring
• stability awareness
• orientation estimation

### Future Encoders

Encoders measure mechanical rotation or position.

Encoders support closed-loop motion control and precise actuator positioning.

---

## Relationship With Other Modules

### Relationship With Perception

Sensors produce raw signals.

The Perception module processes those signals and interprets them.

### Relationship With Interaction Interfaces

Some sensors provide the input channels used by interaction interfaces, such as voice input or visual gesture input.

### Relationship With the Cognitive Core

Sensor outputs may influence system state transitions, contextual updates, and behavioural decision processes.

### Relationship With Observability

Sensor measurements and sensor health information may be exposed through monitoring and telemetry systems.

---

## Architectural Importance

The Sensors submodule provides the physical observation capabilities of NORA.

Through sensors, the system obtains information about:

• humans interacting with it
• objects and conditions in the environment
• internal operational state

These signals provide the foundation upon which perception, cognition, and interaction are built.

Without sensors, the system would have no direct connection with the physical world.

# 11.3 Actuators

## Definition

The Actuators submodule defines the physical output devices through which NORA produces effects in the physical world.

An actuator is a hardware component that converts a system command into a physical effect that can be perceived by humans, detected by sensors, or applied to devices and infrastructure.

Within the Infrastructure and Hardware module, actuators represent the physical execution mechanisms of the system.

If sensors provide the physical signals that enter the system and computation devices execute the software processes of the architecture, actuators provide the hardware channels through which system decisions become observable actions.

In architectural terms, actuators answer the question:

What physical effects can NORA produce?

These effects may include sound, visual output, movement, electrical switching, tactile feedback, or control signals sent to external devices.

---

## Core Architectural Concepts

### Actuator

An actuator is a hardware device that converts a digital control signal into a physical effect.

This conversion typically involves electrical signals driving mechanical, acoustic, optical, or electronic systems.

An actuator therefore performs three fundamental functions:

• reception of a control signal from computation hardware
• transformation of that signal into a physical action
• generation of a perceivable or measurable effect

### Actuation Channel

An actuation channel is the pathway through which a specific category of system output reaches the physical world.

Examples of actuation channels include:

• acoustic channel
• visual signalling channel
• display channel
• mechanical motion channel
• electrical switching channel
• tactile feedback channel
• external device control channel

Each actuation channel corresponds to a different class of system behaviour.

### Actuation Modality

An actuation modality refers to the type of physical effect produced by an actuator.

Examples include:

• sound generation
• light emission
• image display
• mechanical movement
• vibration
• electrical switching

These modalities define how the system expresses actions physically.

### Expressive Actuation

Expressive actuation refers to outputs that communicate information or states to humans.

Examples include speech output, display messages, visual indicators, and sound notifications.

These outputs allow the system to express responses, feedback, and internal states.

### Mechanical Actuation

Mechanical actuation refers to actuators that produce physical movement or mechanical interaction.

Examples include servo motors and drive motors.

Mechanical actuation allows the system to move components of its body or perform physical gestures.

### Switching Actuation

Switching actuation refers to actuators that control electrical circuits or activate external devices.

Examples include relays and smart device control interfaces.

These actuators allow the system to influence electrical systems in its environment.

### Haptic Actuation

Haptic actuation refers to tactile output mechanisms such as vibration motors.

These outputs produce physical sensations that can be felt by users interacting with the system.

---

## Architectural Purpose

The purpose of the Actuators submodule is to define the hardware components that allow NORA to perform actions in the physical world.

An embodied cognitive system must not only observe and reason about its environment but must also express responses and perform actions that produce physical consequences.

Actuators provide the mechanisms that make this possible.

Through actuators the system can:

• communicate with humans
• express internal system states
• perform physical movements
• activate devices and infrastructure
• generate feedback signals

Without actuators, the system could sense and compute but would be unable to produce visible, audible, or physical responses.

---

## Role Within the Global Architecture

Within the overall architecture, actuators represent the final stage of behaviour execution.

Information flow related to actions can be summarized as:

System decision
→ Action and Expression module
→ control signals
→ actuators
→ physical effect

In this chain, the Action and Expression module determines what action should occur, while the Actuators submodule defines the hardware devices that produce the physical outcome.

Actuators therefore transform digital control instructions into real-world signals and motion.

---

## Scope of the Submodule

The Actuators submodule includes hardware devices that generate physical output signals or movement.

### In Scope

• speakers
• display screens
• LED indicators
• servo motors
• electric motors
• vibration motors
• relays
• smart device control interfaces

### Out of Scope

The submodule does not include:

• behavioural decision logic
• dialogue generation
• planning algorithms
• signal interpretation

These responsibilities belong to other modules such as Cognitive Core, Planning and Agents, and Action and Expression.

---

## Core Responsibilities

### Physical Action Execution

The primary responsibility of actuators is to convert system commands into physical effects.

Examples of actuator-generated effects include:

• sound output
• visual information display
• light signalling
• mechanical motion
• electrical switching

These effects allow system behaviour to become observable and interactive.

### Human Communication

Many actuators serve as communication channels between the system and humans.

Examples include:

• speakers for spoken responses
• displays for graphical output
• LEDs for state indicators

These outputs form the expressive interface of the system.

### Mechanical Interaction

Mechanical actuators enable movement of the robot body or components.

These actuators allow the system to perform gestures, orientation changes, or other physical behaviours.

### Environmental Control

Certain actuators enable the system to control devices and infrastructure in its environment.

Examples include switching electrical circuits or sending commands to smart devices.

---

## Actuator Types

### Speakers

Speakers generate acoustic output from electrical audio signals.

They provide the acoustic actuation channel of the system.

Typical uses include:

• synthesized speech
• notification sounds
• multimedia playback

### Display Screen

A display screen generates visual output in the form of text, graphics, or video.

Displays provide the visual information interface between the system and users.

Typical uses include:

• textual responses
• graphical interfaces
• visual feedback
• system state indicators

### LEDs

LED indicators produce light signals that represent system states.

Typical uses include:

• activity indication
• listening state
• processing state
• alert signalling

### Servo Motors

Servo motors produce controlled rotational movement.

They allow precise positioning of mechanical components such as a robot head or camera mount.

### Electric Motors

Electric motors generate rotational or translational mechanical motion.

These motors may drive movement of mechanical assemblies or rotating structures.

### Haptic Vibration Motors

Vibration motors produce tactile feedback signals.

These signals can provide silent alerts or interaction feedback.

### Relays

Relays control electrical circuits by switching them on or off in response to digital control signals.

Relays allow the system to control electrical devices such as lighting or appliances.

### Smart Device Interfaces

Smart device control interfaces allow the system to send commands to connected appliances or automation systems.

Examples include smart lights, connected plugs, thermostats, or automated devices.

---

## Relationship With Other Modules

### Relationship With Action and Expression

The Action and Expression module defines behavioural actions.

The Actuators submodule defines the hardware devices that execute those actions.

### Relationship With Sensors

Sensor measurements may influence actuator behaviour.

For example, proximity sensors may restrict movement or light sensors may adjust display brightness.

### Relationship With Computation

Computation devices generate the control signals that drive actuators.

These signals may be transmitted directly or through embedded controllers.

### Relationship With Backend Systems

Actuator commands and states may be monitored or controlled through backend services and administrative interfaces.

---

## Design Principles

### Reliability

Actuators must operate predictably because they produce physical effects.

### Safety

Movement and switching actuators must include safeguards to prevent unsafe behaviour.

### Clear Action Mapping

Each actuator corresponds to defined actions within the Action and Expression module.

### Expandability

The architecture allows additional actuator types to be integrated without structural redesign.

---

## Architectural Importance

The Actuators submodule defines how NORA manifests behaviour in the physical world.

Through actuators the system can:

• speak
• display information
• signal internal states
• perform movement
• control external devices

Actuators complete the loop between sensing, cognition, decision making, and physical action.

Without actuators, the system would remain purely observational and incapable of producing real-world effects.

# 11.4 Connectivity

## Definition

The Connectivity submodule defines the communication mechanisms that allow NORA to exchange data with internal hardware components, external devices, and networked services.

Within the Infrastructure and Hardware module, connectivity represents the physical and protocol-level communication layer that links the system to its environment and to its distributed hardware elements.

If sensors provide physical signals entering the system and actuators produce physical effects in the environment, connectivity defines how information travels between components of the system and between NORA and external systems.

Connectivity therefore answers the architectural question:

How does information move between devices and subsystems?

Through connectivity mechanisms the system can:

• communicate with sensors and actuators
• exchange data between computation units
• interact with external devices
• connect to networks and the internet
• receive commands from remote services

Without connectivity, NORA would operate as an isolated device unable to integrate with networks, external services, or distributed hardware components.

---

## Core Architectural Concepts

### Communication Interface

A communication interface is a physical or logical hardware interface that allows two devices to exchange data.

Examples include USB ports, network interfaces, and serial communication buses.

Communication interfaces define how devices are physically connected.

### Communication Protocol

A communication protocol defines the rules governing how information is transmitted and interpreted between communicating devices.

Protocols define aspects such as:

• data format
• message timing
• synchronization
• error detection

Examples include MQTT, I2C, SPI, and serial communication protocols.

### Network Interface

A network interface is a hardware component that allows the system to connect to local or wide-area networks.

Examples include WiFi adapters and Ethernet controllers.

Network interfaces enable the system to participate in distributed computing environments.

### Hardware Bus

A hardware bus is a communication pathway that allows multiple hardware devices to communicate with a processor or controller.

Examples include I2C and SPI buses used in embedded electronics.

Hardware buses allow sensors and peripheral modules to share communication lines.

### Device Interface

A device interface is a connection point used to attach peripheral hardware to a computing device.

Examples include USB ports and serial interfaces.

Device interfaces provide standardized mechanisms for integrating external hardware.

### Communication Topology

Communication topology describes how devices are interconnected within the system.

Examples include point-to-point communication, bus architectures, and network-based communication structures.

Topology influences reliability, scalability, and system performance.

---

## Architectural Purpose

The purpose of the Connectivity submodule is to define the hardware communication technologies that enable NORA to interact with devices, networks, and distributed computing nodes.

An embodied intelligent system typically requires multiple communication layers because different types of interactions have different technical requirements.

Examples include:

• wireless communication for network connectivity
• wired communication for stable device integration
• embedded buses for internal electronics
• messaging protocols for distributed system coordination

By defining these communication technologies explicitly, the architecture clarifies how information flows between physical devices and software modules.

---

## Role in the Global Architecture

Within the global architecture, connectivity forms the transport layer that enables communication between system components that are not located within the same hardware device.

Conceptually, the communication flow can be represented as:

System module
→ communication interface
→ communication protocol
→ remote device or service

Connectivity enables interactions between:

• internal hardware peripherals
• onboard computation units
• external devices
• remote servers
• smart home environments

Because many capabilities of NORA rely on distributed hardware and networked services, connectivity is a critical enabling infrastructure.

---

## Scope of the Submodule

The Connectivity submodule includes hardware interfaces and low-level communication technologies that allow devices and software components to exchange information.

### In Scope

• wireless communication technologies
• wired network connections
• embedded hardware communication buses
• peripheral device interfaces

### Out of Scope

The submodule does not include:

• application-layer protocols
• logical APIs
• cloud service integrations
• high-level service orchestration

These responsibilities belong to higher-level architectural modules such as Backend and Application or Integrations and External Services.

---

## Core Responsibilities

### Device Communication

Connectivity mechanisms enable communication between computation devices and hardware peripherals such as sensors and actuators.

Examples include serial interfaces and embedded communication buses.

### Network Communication

Network interfaces allow the system to connect to local networks and the internet.

These connections enable communication with:

• remote APIs
• cloud services
• mobile devices
• administrative systems

### Distributed System Integration

Connectivity enables communication between multiple computing nodes in the system architecture.

Examples include communication between:

• a Raspberry Pi and an Arduino
• the robot and a nearby server
• the robot and remote backend services

### Peripheral Integration

Connectivity interfaces allow the system to attach and operate external hardware components.

These may include cameras, microphones, storage devices, and communication adapters.

---

## Connectivity Technologies

### WiFi

WiFi provides wireless network connectivity using local area network infrastructure.

Through WiFi the system can connect to local networks and access internet services.

Typical uses include communication with backend services, device management interfaces, and external APIs.

### Bluetooth

Bluetooth provides short-range wireless communication between nearby devices.

Typical uses include communication with mobile devices, wearable technology, and peripheral accessories.

Bluetooth is often used for proximity-based device interactions.

### Ethernet

Ethernet provides a wired network connection between the system and local network infrastructure.

Compared to wireless connections, Ethernet typically provides higher stability, predictable latency, and consistent bandwidth.

Ethernet is commonly used in development environments or installations where stable connectivity is required.

### Internet Connectivity

Internet connectivity allows the system to communicate with remote services located outside the local network.

Examples include language model services, weather APIs, search engines, and monitoring platforms.

Internet connectivity significantly expands the capabilities of the system beyond local processing.

### MQTT

MQTT is a lightweight messaging protocol designed for communication in distributed systems and IoT environments.

MQTT follows a publish-subscribe communication model that allows devices to exchange messages through a broker.

It is commonly used for device messaging, event distribution, and home automation communication.

### Serial Communication

Serial communication provides a direct communication channel between two hardware devices using sequential data transmission.

Serial interfaces are frequently used for communication between embedded computers and microcontrollers.

### USB

USB provides a standardized interface for connecting peripheral devices to computing hardware.

USB connections support both data transfer and electrical power delivery.

Typical USB peripherals include cameras, microphones, storage devices, and communication adapters.

### I2C

I2C is a communication bus designed for low-speed communication between integrated circuits within embedded systems.

I2C allows multiple devices to share the same communication bus using addressing mechanisms.

Typical I2C devices include environmental sensors and small peripheral modules.

### SPI

SPI is a synchronous communication protocol used for high-speed data exchange between processors and peripheral hardware.

SPI is commonly used for devices requiring higher data transfer rates than those supported by I2C.

Examples include display modules, memory devices, and high-performance sensors.

### GPIO

GPIO pins allow direct digital interaction with external hardware components.

Through GPIO the system can read input signals or trigger simple output signals used to control devices or detect events.

GPIO interfaces are frequently used for low-level hardware interaction and prototyping.

---

## Relationship With Other Modules

### Relationship With Computation

Computation devices rely on connectivity interfaces to communicate with hardware peripherals and networks.

### Relationship With Sensors

Many sensors connect to computation devices through communication interfaces such as I2C, SPI, USB, or GPIO.

### Relationship With Actuators

Actuators may also receive control signals through connectivity interfaces, particularly when controlled by microcontrollers or relay modules.

### Relationship With Integrations and External Services

Connectivity provides the physical communication layer required for interactions with external software systems and services.

---

## Design Principles

### Reliability

Connectivity mechanisms should prioritize stable and predictable communication behaviour.

### Modularity

Communication interfaces should allow new devices and peripherals to be integrated without requiring architectural redesign.

### Security

Network communication channels must incorporate appropriate security protections to prevent unauthorized access.

### Scalability

The connectivity architecture should support the future addition of new devices, sensors, and distributed computing components.

---

## Architectural Importance

Connectivity enables NORA to operate as part of a larger technological ecosystem.

Through connectivity the system can:

• communicate with external services
• exchange data with distributed hardware components
• integrate with smart environments
• interact with networked devices

Without connectivity, the system would be limited to isolated local operation and unable to leverage networked intelligence or device ecosystems.

For this reason, connectivity forms a critical enabling layer of the Infrastructure and Hardware architecture.

# 11.5 External Controllable Devices

## Definition

The External Controllable Devices submodule defines the physical devices and appliances located outside the robot that NORA can interact with, monitor, or control.

Within the Infrastructure and Hardware module, this submodule represents the external physical systems that can be influenced by the robot through connectivity interfaces, integrations, or automation platforms.

If sensors define how information enters the system and actuators define how the robot produces physical outputs within its own hardware, external controllable devices define the equipment in the surrounding environment that NORA can coordinate or operate.

These devices may exist in environments such as homes, offices, laboratories, or educational spaces where the system is deployed.

Examples include:

• lighting systems
• coffee machines
• climate control systems
• smart plugs
• televisions
• door locks
• robot vacuums

In architectural terms, these devices extend the physical influence of the system beyond the robot's internal hardware.

---

## Core Architectural Concepts

### External Device

An external device is any physical appliance or infrastructure component located outside the robot that can receive commands from the system.

External devices typically expose control interfaces through network protocols, smart-home ecosystems, or device-specific APIs.

### Device Control Channel

A device control channel is the communication pathway used to send commands from the system to the device.

These channels may include:

• network communication
• smart-home automation platforms
• direct device protocols

### Device Capability

A device capability represents an action or function that the system can request from the device.

Examples include switching power, adjusting temperature, starting a program, or unlocking a door.

### Device Abstraction

Device abstraction refers to representing external devices through generalized capabilities rather than specific hardware models.

For example, a light device may expose capabilities such as on, off, brightness adjustment, or color control regardless of the manufacturer.

### Smart Environment

A smart environment is a physical space where devices are digitally connected and can be controlled through software systems.

In such environments, the robot may function as a coordination interface between users and the connected infrastructure.

---

## Architectural Purpose

The purpose of this submodule is to describe the categories of external devices that the system can interact with or control in the surrounding environment.

An embodied assistant often acts as a mediator between users and connected infrastructure.

Instead of interacting directly with each device, users can request actions through the system, which then coordinates the required operations.

This capability allows the system to function as a central interaction layer for environments such as:

• smart homes
• offices
• laboratories
• automation-enabled rooms

By integrating with external devices, the system expands its functional capabilities beyond the hardware embedded in the robot itself.

---

## Role in the Global Architecture

Within the global architecture, external controllable devices represent the outermost layer of the system's operational influence.

The control flow may be summarized as:

User request
→ interpretation and planning
→ action generation
→ connectivity interface
→ external device execution

In this structure the robot does not necessarily perform the physical action itself but may delegate execution to external infrastructure.

This allows the system to coordinate complex tasks across multiple devices in the environment.

---

## Scope of the Submodule

This submodule includes devices located outside the robot that can be controlled or queried by the system.

### In Scope

• smart appliances
• home automation devices
• environmental control systems
• connected consumer electronics
• network-enabled infrastructure

### Out of Scope

The submodule does not include:

• communication technologies
• device-specific software integrations
• decision logic for device usage

These responsibilities belong to other modules such as Connectivity, Integrations and External Services, Planning, and Action and Expression.

---

## Core Responsibilities

### Environmental Device Control

External devices allow the system to influence environmental conditions in the space where it operates.

Examples include switching lighting systems or activating appliances.

### Smart Environment Integration

Many devices belong to larger automation ecosystems.

Through integration with these ecosystems the robot can act as a unified interface for interacting with multiple devices.

### Task Delegation

Some requested actions may be executed by external devices rather than the robot itself.

For example, a request to prepare coffee may be delegated to a connected coffee machine.

---

## Device Categories

### Coffee Machine

A connected coffee machine can receive commands to start beverage preparation or configure drink options.

### Lighting Systems

Smart lighting devices allow the system to control illumination levels, switching lights on or off or adjusting brightness.

### Smart Plugs

Smart plugs allow the robot to control the electrical power supplied to connected appliances.

### Television

A connected television can receive commands such as powering on, adjusting volume, or selecting media inputs.

### Smart Speakers

Smart speakers may extend the audio output capabilities of the system into other rooms.

### Climate Control Systems

Climate systems such as thermostats or air conditioning units may receive commands to regulate environmental temperature.

### Smart Locks

Connected door locks allow the system to manage physical access control in a building.

### Smart Doorbells

Doorbell systems may provide notifications, camera feeds, or visitor alerts.

### Robot Vacuum

Robot vacuum cleaners may be activated or scheduled to perform cleaning tasks.

### External Sensors

Environmental sensors installed in the building may provide additional context about motion, doors, temperature, or safety conditions.

### Printer

A network-connected printer allows the robot to send documents or images for printing.

### Future Kitchen Automation

Future integrations may include connected cooking devices or kitchen robots capable of executing automated food preparation processes.

---

## Relationship With Other Modules

### Relationship With Connectivity

Connectivity provides the communication mechanisms required to send commands to external devices.

### Relationship With Integrations

Software integrations define how device ecosystems or manufacturer APIs are accessed.

### Relationship With Planning

Planning modules determine when device actions should be executed to satisfy user requests.

### Relationship With Action and Expression

External device control actions appear as executable actions within the Action and Expression module.

---

## Design Principles

### Device Abstraction

External devices should be represented through generalized capabilities rather than vendor-specific implementations.

### Security

Because device control may involve safety-sensitive actions such as door access or electrical switching, authentication and authorization controls are required.

### Expandability

The architecture should allow additional device categories to be integrated without structural redesign.

### Reliability

Interactions with devices should include confirmation mechanisms and error handling to ensure correct execution.

---

## Architectural Importance

The External Controllable Devices submodule extends the operational reach of the system beyond the robot itself.

Through integration with surrounding infrastructure the robot can coordinate devices and automate environmental actions.

This capability transforms the system from a standalone robot into a central control interface for connected environments.
## Architectural Importance

The Infrastructure and Hardware module provides the physical foundation on which the NORA architecture operates.

While other architectural modules define perception, reasoning, dialogue, planning, execution, and system coordination at the software level, those capabilities ultimately require a material substrate capable of sensing the environment, executing computation, communicating between components, and producing physical effects.

The Infrastructure and Hardware module defines that substrate.

Through this module the architecture gains:

* physical execution platforms for software modules
* sensing channels through which environmental signals enter the system
* actuation channels through which system behaviour produces real-world effects
* hardware communication infrastructure connecting system components
* integration with external physical devices in the surrounding environment
* explicit representation of physical constraints and operational conditions

By explicitly modeling the physical infrastructure of the system, the architecture ensures that higher-level behavioural modules remain grounded in the material realities of computation, sensing, communication, and actuation.

This separation between logical system behaviour and physical execution substrate improves architectural clarity, maintainability, and deployability of the NORA system.

---

## Architectural Structure

```
Infrastructure and Hardware
│
├── Computation
│ ├── embedded computers
│ ├── microcontrollers
│ ├── distributed processing nodes
│ ├── edge computing devices
│ ├── onboard processing boards
│ ├── local orchestration processors
│ ├── inference processing devices
│ ├── hardware accelerators
│ ├── compute workload distribution
│ ├── runtime execution hosts
│ └── system processing infrastructure
│
├── Sensors
│ ├── microphones
│ ├── cameras
│ ├── NFC sensors
│ ├── proximity sensors
│ ├── tactile sensors
│ ├── temperature sensors
│ ├── humidity sensors
│ ├── light sensors
│ ├── battery monitoring sensors
│ ├── motion sensors
│ └── environmental sensing devices
│
├── Actuators
│ ├── speakers
│ ├── display screens
│ ├── LED indicators
│ ├── servo motors
│ ├── electric motors
│ ├── vibration motors
│ ├── relays
│ ├── device switching interfaces
│ ├── mechanical motion devices
│ ├── visual signalling devices
│ └── external device control channels
│
├── Connectivity
│ ├── WiFi communication
│ ├── Bluetooth communication
│ ├── Ethernet networking
│ ├── internet connectivity
│ ├── MQTT messaging
│ ├── serial communication
│ ├── USB device interfaces
│ ├── I2C hardware buses
│ ├── SPI hardware buses
│ ├── GPIO interfaces
│ └── device communication links
│
└── External Controllable Devices
  ├── coffee machines
  ├── lighting systems
  ├── smart plugs
  ├── televisions
  ├── smart speakers
  ├── climate control systems
  ├── smart locks
  ├── smart doorbells
  ├── robot vacuum cleaners
  ├── building sensor systems
  └── connected appliances
```

---

## Architectural Layers

The Infrastructure and Hardware module can be interpreted as a layered physical architecture that enables the software system to operate in the real world.

| Layer                           | Responsibility                                                                   |
| ------------------------------- | -------------------------------------------------------------------------------- |
| Physical Sensing Layer          | Provides hardware sensors that capture environmental and internal system signals |
| Physical Execution Layer        | Provides computation devices that execute the software architecture              |
| Physical Action Layer           | Provides actuators that generate observable physical effects                     |
| Hardware Communication Layer    | Provides communication interfaces connecting hardware components and networks    |
| Environmental Integration Layer | Provides interaction with external controllable devices and smart environments   |

Together these layers form the physical embodiment of the NORA architecture, allowing the system to perceive the world, execute software processes, communicate between co
