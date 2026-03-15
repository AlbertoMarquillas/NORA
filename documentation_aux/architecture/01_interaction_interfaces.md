# 2. Interaction Interfaces

## Definition

The **Interaction Interfaces** module defines the human-facing access layer of NORA.

This module contains the channels through which a person intentionally exchanges information, control signals, feedback, or interruptions with the system.

Within the architecture, an interaction interface is not a sensing mechanism and is not an internal reasoning process. It is a **human-system interaction surface**.

The module defines the practical forms through which a human accesses NORA as an embodied multimodal system.

These forms include:

* **interaction channel**  
human-facing medium through which a person communicates with, controls, observes, or interrupts NORA.

* **interaction surface**  
concrete access point where interaction occurs, such as voice, screen, touch, gesture, proximity interface, or remote client.

* **interaction event**  
normalized user-originated act expressed through an interface, such as a command, confirmation, cancellation, selection, or interruption.

* **interaction feedback**  
human-perceivable output through which NORA exposes state, responses, prompts, or execution status.

The Interaction Interfaces module groups these elements into a single architectural layer so that the rest of the system remains independent from the specific interface through which the interaction occurs.

NORA is accessed through multiple intentional human-facing channels rather than through a single input-output path. For that reason, interaction is defined as a complete architectural domain.

---

## Architectural Role

The Interaction Interfaces module defines the boundary layer between humans and the internal system.

It establishes:

* **interaction entry points**  
the channels through which users initiate or continue interaction with NORA.

* **interaction output surfaces**  
the channels through which NORA returns feedback, responses, prompts, and visible state to humans.

* **interaction control signals**  
the human-originated acts that regulate interaction flow, such as confirm, reject, cancel, stop, continue, or select.

* **interaction exposure**  
the way system state, capabilities, and ongoing activity become accessible to human users or administrators.

This module defines the interaction role of each channel, not the low-level processing of the signal used by that channel.

The architectural distinction is the following:

* spoken language as a user interaction channel belongs to Interaction Interfaces
* acoustic capture and speech processing belong to Perception
* gesture as an intentional command belongs to Interaction Interfaces
* visual detection of body pose belongs to Perception

This separation keeps human-facing interaction architecture distinct from sensing and signal interpretation logic.

## Architectural Necessity

NORA operates as an embodied intelligent system rather than as a single software application accessed through a single interface.

The system includes the following properties:

* physical embodiment
* multimodal perception
* conversational dialogue
* long-lived interaction sessions
* local and remote access
* multiple users with distinct roles

Because of these properties, interaction with NORA does not occur through a single interface. The system exposes multiple interaction surfaces adapted to different physical and operational contexts.

Within the architecture, each interaction surface has distinct characteristics, including:

* physical constraints
* latency characteristics
* security implications
* accessibility conditions
* user experience properties

The Interaction Interfaces module exists to model and organize these human-system interaction surfaces as a coherent architectural layer.

---

## Scope of the Module

The Interaction Interfaces module contains all channels whose primary role is **intentional human-system interaction**.

These channels include:

* spoken interaction channels
* auditory feedback channels
* visual feedback surfaces
* tactile interaction surfaces
* gesture-based interaction commands
* short-range identification interfaces
* remote interaction clients

These elements represent the surfaces through which humans communicate with, observe, and control the system.

The module defines the **interaction role** of these channels within the architecture.

---

## Exclusions

The Interaction Interfaces module does not include sensing, interpretation, or execution mechanisms.

The following responsibilities belong to other architectural modules:

* acoustic signal capture and speech recognition  
  Perception of the Environment

* visual sensing and computer vision analysis  
  Perception of the Environment

* semantic interpretation and intent detection  
  Planning, Interpretation and Agents

* execution of physical or digital actions  
  Action and Expression

* identity verification, authentication, and permissions  
  Identity, Access and Security

## Architectural Role Within the System

The Interaction Interfaces module forms the boundary layer between humans and the internal subsystems of NORA.

Through this layer, human-originated interaction enters the system and system feedback becomes accessible to humans.

The module connects the human environment with several internal architectural domains, including:

* Perception of the Environment
* Cognitive Core
* Dialogue and Session System
* Planning, Interpretation and Agents
* Action and Expression
* Backend and Application Services

Within the system architecture, interaction follows the general structure:

Human → Interaction Interface → Internal Processing and Decision Layers → Action and Feedback

Interaction interfaces are not responsible for reasoning, perception, or execution. Their role is to expose the entry and exit surfaces through which the system becomes accessible to human users.

The module provides:

* structured human input channels
* structured feedback channels
* separation between interaction surfaces and internal processing logic
* a unified abstraction for local and remote interaction mechanisms

Without this architectural layer, human input, internal logic, and feedback mechanisms would become tightly coupled and difficult to extend.

---

## Core Architectural Properties

The Interaction Interfaces module exhibits several structural properties within the system architecture.

### Modality Independence

Interaction channels are independent from the internal reasoning and control mechanisms of the system.

Different interaction modalities can produce equivalent normalized interaction events.

Examples of normalized interaction events include:

* confirm
* cancel
* request_help
* start_session
* stop_action
* select_target

Multiple interaction surfaces may produce the same interaction event. For example, confirmation may originate from spoken language, a touch interaction, or a remote client interface.

### Multimodal Coexistence

The architecture supports simultaneous operation of multiple interaction interfaces.

Different interaction modalities may remain active concurrently and contribute to the same interaction session.

Examples of concurrent modalities include:

* spoken interaction and visual feedback
* local user interaction and remote administrative monitoring
* gesture-based commands combined with spoken dialogue

The system architecture treats these modalities as parallel interaction channels mapped into the same internal interaction framework.

### Interruptibility

Interaction channels provide mechanisms through which users can interrupt or override ongoing system activity.

Interrupt signals may originate from multiple interaction modalities, including:

* spoken cancellation
* gesture-based stop commands
* physical buttons or tactile controls
* remote administrative commands

These interruption signals propagate through the interaction layer into the dialogue, planning, and execution subsystems.

### Feedback Visibility

Interaction interfaces expose system feedback through human-perceivable channels.

Feedback channels include:

* spoken responses
* textual responses
* graphical or visual indicators
* tactile signals
* remote monitoring interfaces

These channels expose system state and interaction progress to human users.

Observable system states include:

* listening
* waiting for input
* processing
* executing actions
* awaiting confirmation
* blocked state
* error state

### Accessibility and Redundancy

The architecture supports multiple interaction paths for similar user intentions.

Equivalent interaction actions may be expressed through different interaction modalities.

Examples include:

* spoken commands or tactile interaction
* visual interface feedback or spoken responses
* gesture-based commands or verbal commands
* local interaction or remote interaction

This redundancy increases accessibility and operational resilience.

### Channel-Aware Security Context

Interaction interfaces carry contextual information related to the interaction channel.

This context is propagated to downstream security and authorization mechanisms.

Interaction context may include:

* interaction modality
* physical proximity
* device identity
* interface trust level
* user identity signals

Security and authorization decisions are performed by the Identity, Access and Security module, but interaction interfaces provide the contextual information required for those decisions.

## Main Responsibilities

The Interaction Interfaces module defines the architectural mechanisms through which humans access, control, and observe NORA.

Its responsibilities include the following functions.

### Interaction Entry Points

The module defines the interaction channels through which human-originated interaction enters the system.

Interaction entry points include:

* spoken interaction channels
* tactile interaction surfaces
* gesture-based command channels
* proximity identification interfaces
* local graphical interfaces
* remote client interfaces

These entry points represent the human-facing surfaces through which interaction sessions, commands, and control signals originate.

### Interaction Output Surfaces

The module defines the surfaces through which the system exposes feedback and information to humans.

Interaction output surfaces include:

* spoken responses
* graphical displays
* visual state indicators
* interactive menus
* notifications and alerts
* remote monitoring dashboards

These surfaces expose system responses, operational state, and interaction progress.

### Control Signals

The module defines the normalized control intentions through which humans regulate interaction flow.

Control signals include:

* confirm
* deny
* cancel
* repeat
* continue
* stop
* select

These signals may originate from different interaction modalities but converge to a shared internal interaction event.

### Human-Usable Operational Access

The module defines the human-facing surfaces through which users and administrators observe and influence system operation.

Operational interaction capabilities include:

* inspection of system state
* access to operational logs
* triggering of manual commands
* selection of operating modes
* observation of active sessions or hardware status

These capabilities expose operational visibility and manual control through interaction surfaces.

### Channel Normalization

The module provides a mapping layer between heterogeneous interaction channels and normalized internal interaction events.

Different interaction modalities can produce equivalent normalized events.

This normalization maintains architectural modularity and prevents internal logic from depending on specific interaction modalities.

---

## Relationship With Other Modules

The Interaction Interfaces module interacts with several other architectural domains.

### Relationship With Perception of the Environment

Perception processes and interprets raw sensory signals.

Interaction Interfaces define the human interaction role of those channels.

Within the architecture:

* acoustic capture and speech recognition belong to Perception of the Environment
* spoken interaction commands belong to Interaction Interfaces
* gesture detection belongs to Perception of the Environment
* gesture-based commands belong to Interaction Interfaces

### Relationship With Identity, Access and Security

Interaction interfaces expose the channels through which identification or authentication procedures may begin.

Identity verification, authentication logic, and permission evaluation belong to the Identity, Access and Security module.

Interaction interfaces provide the human-facing surfaces through which these mechanisms are accessed.

### Relationship With the Cognitive Core

The Cognitive Core defines operational reasoning and behavioural decisions.

Interaction interfaces expose the human-facing mechanisms through which users initiate, influence, or interrupt those behaviours.

### Relationship With Dialogue and Session System

The Dialogue and Session System maintains conversational continuity and interaction state.

Interaction interfaces provide the channels through which dialogue exchanges occur.

### Relationship With Planning, Interpretation and Agents

Planning and agent selection determine the operational actions of the system.

Interaction interfaces expose the mechanisms through which plans request clarification, confirmation, additional input, or user feedback.

### Relationship With Action and Expression

The Action and Expression module executes physical or digital actions.

Interaction interfaces represent the subset of those actions that appear as human-facing outputs or interaction surfaces.

## Internal Organization of the Module

The Interaction Interfaces module is composed of several submodules.  
Each submodule represents a distinct human-facing interaction channel.

### 2.1 Voice Interface
Human interaction through spoken language.  
This interface supports conversational dialogue and spoken command interaction.

### 2.2 Local Screen Interface
Graphical interaction surface integrated into the physical system.  
This interface exposes visual feedback, menus, and interactive controls.

### 2.3 Web Frontend Interface
Browser-based interaction interface accessible from remote devices.  
This interface provides operational access for users and administrators.

### 2.4 Touch and Physical Interaction
Direct physical interaction through tactile surfaces, buttons, or contact with the system body.

### 2.5 NFC / RFID Interface
Short-range proximity interface used for identification, activation, and profile association.

### 2.6 Gesture Interface
Human interaction through recognized body movements or hand gestures.

### 2.7 Remote Interfaces
External-device interaction channels including mobile clients, administrative terminals, and programmatic remote access interfaces.

Each of these submodules represents a specific interaction modality through which humans or human-operated systems interact with NORA.

---

## Common Interaction Patterns

Although interaction channels differ in modality, they share a set of common interaction patterns.  
These patterns represent recurring structures of human-system interaction.

### Interaction Initiation

Interaction begins through an interaction entry point.  
This pattern represents the start of a user-system interaction exchange.

Interaction initiation may occur through any supported interaction channel.

### Query or Command

A user expresses a request for information or asks the system to perform an action.

This pattern represents intentional input directed toward the system's cognitive and planning subsystems.

### Confirmation or Rejection

A user accepts or rejects a proposed action, interpretation, or system decision.

Confirmation and rejection signals regulate decision execution and plan continuation.

### Interruption

A user stops or overrides an ongoing system activity.

Interruption signals propagate through the interaction layer toward dialogue, planning, and execution subsystems.

### Follow-Up Interaction

A user continues an interaction across multiple exchanges.

This pattern represents interaction continuity within the dialogue and session system.

Follow-up interaction allows refinement of requests, continuation of tasks, and persistence of interaction context across turns.

## Interaction Inputs

The Interaction Interfaces module receives human-originated interaction inputs through the available interaction channels.

These inputs represent intentional human actions directed toward the system.

Interaction inputs include the following categories.

### Spoken Inputs

Inputs expressed through spoken language.

Examples of spoken inputs include:

* wake phrase activation
* free-form spoken request
* spoken confirmation
* spoken rejection or cancellation
* dictated text input

### Tactile Inputs

Inputs expressed through direct physical contact with interaction surfaces.

Tactile inputs include:

* touch events
* button presses
* touchscreen selections
* emergency stop activation

### Proximity Identification Inputs

Inputs generated through short-range identification technologies.

These include:

* NFC tag scans
* RFID credential scans

### Gesture Inputs

Inputs expressed through recognized body movement or hand gesture.

Gesture inputs include:

* greeting gestures
* stop gestures
* pointing gestures
* confirmation gestures

### Remote Interaction Inputs

Inputs originating from remote interaction clients.

These include:

* browser-based commands
* administrative terminal requests
* external user-facing API interaction requests

Interaction inputs represent interface-level events.  
The extraction and interpretation of raw signals associated with these inputs belong to other architectural modules such as Perception of the Environment.

## Interaction Outputs

The Interaction Interfaces module exposes human-perceivable outputs through the available interaction surfaces.

These outputs represent the visible or audible manifestation of internal system responses, system state, or interaction feedback.

Interaction outputs include the following categories.

### Spoken Outputs

Auditory responses generated through spoken language.

These outputs include:

* spoken replies
* spoken clarification requests
* spoken confirmations
* spoken error messages

### Visual Outputs

Graphical or visual information presented through screens or display surfaces.

Visual outputs include:

* textual updates on local display
* images or video previews
* graphical status indicators
* confirmation prompts
* rendered menus
* dashboard state updates

### Notification Outputs

Short-form alerts or attention signals directed toward the user.

These include:

* notification banners
* browser alerts
* status notifications
* interaction prompts

### Interaction State Indicators

Visual or auditory indicators representing the current interaction state of the system.

These indicators include:

* interaction mode indicator
* active listening indicator
* processing indicator
* cancellation acknowledgement

## Structural Properties of Interaction

The Interaction Interfaces module introduces several structural properties related to the coexistence and coordination of multiple interaction channels.

### Cross-Modality Consistency

All interaction interfaces represent access paths to the same underlying system.

Regardless of the modality used, interaction channels map to a shared internal interaction framework. Commands, confirmations, interruptions, and dialogue exchanges maintain consistent semantics across modalities.

### Multi-Channel Concurrency

Interaction events may originate simultaneously from multiple interaction channels.

The architecture supports concurrent interaction events originating from different sources, including:

* local human interaction
* remote administrative interaction
* programmatic external interaction clients

Concurrent interaction events are propagated through the interaction layer toward downstream subsystems, where arbitration, prioritization, or synchronization mechanisms may be applied.

### Channel-Specific Latency Characteristics

Different interaction channels exhibit different response and latency characteristics.

Examples include:

* conversational voice interaction with rapid turn-taking
* graphical interfaces with periodic refresh cycles
* interruption channels requiring immediate propagation

These latency characteristics influence the timing behaviour of dialogue, planning, and execution subsystems.

### Intent Ambiguity Across Modalities

Interaction modalities produce input signals with different levels of intentional clarity.

Certain modalities produce highly explicit inputs, while others produce signals that require additional interpretation.

The interaction layer preserves channel context so that downstream subsystems can apply appropriate interpretation thresholds, confirmation policies, or safety checks.

### Local and Remote Interaction Context

Interaction events may originate from local human presence or from remote interaction clients.

The architecture preserves the origin context of interaction events so that downstream subsystems can apply operational policies related to physical presence, authority level, or safety constraints.

---

## Architectural Implications

The structural properties of interaction interfaces influence several architectural mechanisms within the system.

The architecture includes mechanisms for:

* channel-specific interface adapters
* normalization of heterogeneous interaction events
* modality-aware feedback generation
* shared interruption and cancellation semantics
* coordination between local and remote interaction channels
* interaction routing based on user presence or interaction origin
* propagation of channel-related trust or safety metadata

These mechanisms integrate with other architectural layers including backend services, event dispatch systems, dialogue management, planning subsystems, and hardware control logic.

# 2.1 Voice Interface

## Definition

The Voice Interface represents the spoken language interaction channel through which humans communicate with the NORA system.

Through this interface, users generate interaction events using speech. These events may include requests, commands, confirmations, interruptions, and conversational dialogue exchanges.

Within the system architecture, spoken interaction is treated as an interaction modality rather than as a sensory process.

The acquisition and interpretation of acoustic signals — including microphone capture, wake phrase detection, voice activity detection, and speech recognition — belong to the Perception of the Environment module.

The Voice Interface therefore defines the human interaction role of spoken language as a communication medium between humans and the system.

---

## Architectural Role

Within the system architecture, the Voice Interface functions as the primary conversational interaction channel.

Through this interface, spoken interaction events enter the interaction layer and propagate toward dialogue management, planning subsystems, and execution mechanisms.

The interface supports several categories of interaction:

* spoken interaction initiation
* spoken information requests
* spoken command input
* conversational dialogue exchanges
* spoken confirmations and rejections
* spoken interruption signals
* clarification requests expressed through speech
* dictated textual input

These spoken interaction events are normalized within the interaction layer and mapped to internal interaction events shared across other interaction modalities.

---

## Interaction Model

Spoken interaction follows a conversational interaction cycle composed of several stages.

1. A user produces spoken input directed at the system.
2. The perception subsystem captures and interprets the acoustic signal.
3. The recognized speech content is converted into a normalized interaction event.
4. The interaction event is propagated to dialogue management and planning subsystems.
5. The system determines the appropriate response or action.
6. The response is delivered to the user through spoken output.

This cycle defines the conversational interaction structure associated with the Voice Interface.

---

## Core Responsibilities

The Voice Interface defines the spoken interaction mechanisms through which users communicate with the system.

### Conversational Interaction

Spoken language supports conversational dialogue exchanges between humans and the system.

These exchanges may involve information requests, explanations, topic discussion, and dialogue continuation across multiple turns.

### Command Interaction

Spoken language may express commands directed toward the system.

Command interaction produces normalized internal interaction events corresponding to requested actions or tasks.

### Confirmation and Rejection

Spoken input may represent confirmation or rejection signals regulating plan continuation or execution approval.

### Interruption and Cancellation

Spoken interaction supports interruption signals capable of stopping or modifying ongoing system behaviour.

### Dictation

Spoken input may represent textual content intended for transcription.

### Guided Dialogue Interaction

Spoken interaction may support structured dialogue flows used in tutoring, training, or guided conversational activities.

---

## Interaction Surfaces

Voice interaction occurs through acoustic communication between the user and the system.

Interaction surfaces include:

* spoken language directed at the system
* wake phrases or spoken address signals
* conversational dialogue turns

These acoustic signals are captured by the perception subsystem and converted into normalized interaction events.

---

## Interaction Events

The Voice Interface produces several categories of spoken interaction events.

These include:

* interaction initiation events
* information request events
* command events
* confirmation signals
* rejection signals
* interruption signals
* clarification requests
* correction signals
* dictated text events
* conversational dialogue turns

These events are integrated with events originating from other interaction modalities.

---

## Interaction Outputs

The Voice Interface exposes spoken outputs produced by the system.

These outputs represent audible manifestations of internal responses, system state communication, or dialogue continuation.

Spoken outputs include:

* responses to information requests
* confirmations of system actions
* clarification prompts
* spoken instructions
* narrative information delivery
* reading of textual content
* dialogue prompts

---

## Relationship With Other Modules

### Perception of the Environment

The perception subsystem processes raw acoustic signals captured by microphones and converts them into recognized speech.

### Dialogue and Session System

Spoken interaction events participate in dialogue exchanges managed by the dialogue subsystem.

### Planning, Interpretation and Agents

Spoken interaction events propagate to planning subsystems and specialized agents responsible for determining system behaviour.

### Action and Expression

Spoken outputs are produced through speech synthesis mechanisms defined in the Action and Expression module.

---

## Structural Properties of Spoken Interaction

### Conversational Interaction Structure

Voice interaction follows a turn-based conversational structure in which human input and system responses alternate across dialogue turns.

### Low-Latency Interaction

Spoken interaction requires short response latency to maintain natural conversational flow.

### Interruptible Interaction

Spoken interaction supports interruption signals capable of modifying or stopping ongoing system behaviour.

### Dialogue-Based Error Recovery

Misinterpretation or incomplete input may produce clarification interactions handled through the dialogue system.

### Multilingual Interaction Context

Voice interaction may occur in multiple languages, and the interaction layer preserves language context for downstream subsystems.

---

# 2.2 Local Screen Interface

## Definition

The Local Screen Interface represents the visual interaction surface integrated into the physical NORA system.

Through this interface, the system exposes graphical feedback, structured information, and visual interaction elements to users located near the robot.

Within the architecture, the local screen constitutes a human-facing visual surface embedded in the robot. It presents system responses, interaction state, and operational information through graphical output.

The Local Screen Interface therefore defines the visual interaction role of the on-device display within the interaction layer.

---

## Architectural Role

Within the system architecture, the Local Screen Interface functions as the primary visual interaction surface integrated into the device.

Through this interface, the system exposes visual representations of internal state, interaction progress, and system behaviour.

The interface supports several categories of interaction:

* visual feedback related to interaction state
* presentation of structured information
* graphical representation of system responses
* graphical interaction elements when touch interaction is available
* visual expression of system behaviour

Visual outputs presented on the screen originate from downstream reasoning, dialogue, or execution subsystems.

---

## Interaction Model

The Local Screen Interface participates in multimodal interaction flows.

Visual outputs displayed on the screen may accompany interaction events originating from other modalities, including spoken interaction, gesture interaction, touch interaction, or remote commands.

Typical interaction flow may include:

1. An interaction event occurs through another modality.
2. Internal subsystems determine the corresponding system response.
3. Visual output representing the response or system state is generated.
4. The visual output is rendered on the local screen.

The screen may also function as a direct interaction surface when graphical interaction elements are enabled.

---

## Core Responsibilities

The Local Screen Interface defines several categories of visual interaction capabilities.

### Visual Interaction Feedback

The screen exposes visual indicators representing the interaction state of the system.

These indicators communicate internal activity and interaction progress.

### Structured Information Display

The screen presents structured information that benefits from visual representation.

These outputs include textual information, images, graphical representations, and contextual displays.

### Graphical Interaction Controls

When touch interaction is enabled, the screen exposes graphical user interface elements capable of generating interaction events.

These elements include menus, buttons, selectable options, and configuration panels.

### Expressive Visual Output

The screen may present visual elements representing expressive system behaviour or personality.

### Contextual Interaction Information

The screen may display contextual information related to ongoing system activity or interaction sessions.

---

## Interaction Surfaces

Visual interaction occurs through the integrated display surface of the robot.

Interaction surfaces include:

* graphical display panels
* visual notification areas
* graphical interface elements
* animated visual regions

These surfaces render visual outputs generated by system subsystems.

---

## Interaction Events

When touch capability is available, the Local Screen Interface may generate interaction events originating from graphical interface elements.

Examples include:

* menu selection events
* button activation events
* option selection events
* configuration change events

These events are propagated to backend subsystems responsible for processing user interaction.

---

## Interaction Outputs

The Local Screen Interface exposes visual outputs representing system responses, system state, and interaction context.

These outputs include:

* textual information displays
* image rendering
* video rendering
* camera feed visualization
* graphical menus and interface elements
* notification displays
* animated visual elements
* system status panels
* project or task information displays
* machine-readable codes such as QR codes
* navigation or route visualizations

These outputs contribute to multimodal interaction by complementing spoken interaction and other interaction modalities.

---

## Relationship With Other Modules

### Interaction Interfaces

The Local Screen Interface represents the visual interaction surface embedded in the physical system within the Interaction Interfaces module.

### Dialogue and Session System

The screen may display contextual information associated with ongoing dialogue exchanges or interaction sessions.

### Action and Expression

Visual outputs rendered on the screen originate from the Action and Expression module responsible for generating graphical system responses.

### Frontend and Visualization

Graphical components, rendering logic, and interface definitions may be shared with frontend systems defined in the Frontend and Visualization module.

---

## Structural Properties of Visual Interaction

### Readability Across Interaction Distance

Visual information presented on the screen is designed for interpretation at typical interaction distances between users and the robot.

### Multimodal Interaction Support

Visual outputs complement other interaction modalities, especially spoken interaction.

### Synchronization With Spoken Interaction

Visual outputs remain coordinated with spoken responses generated through the Voice Interface.

### Safe Interaction Controls

Graphical interaction controls are structured to reduce accidental activation and maintain predictable system behaviour.

### Expressive Visual Behaviour

The screen may present visual elements representing expressive system behaviour.

---

# 2.3 Web Frontend Interface

## Definition

The Web Frontend Interface represents the browser-based remote interaction surface through which users and administrators access the NORA system from external devices.

Through this interface, the system exposes remote conversational access, operational information, system state, and administrative capabilities through graphical user interfaces accessible via standard web browsers.

Unlike the Local Screen Interface, which is embedded in the physical system, the Web Frontend Interface operates as an external interaction surface accessible through network-connected devices.

Within the Interaction Interfaces module, the Web Frontend Interface defines the primary browser-based visual and operational interaction channel available outside the robot body.

---

## Architectural Role

Within the system architecture, the Web Frontend Interface functions as the primary browser-based remote interaction channel.

Through this interface, users and administrators interact with the system without requiring physical proximity to the robot.

The interface supports several categories of interaction:

* remote conversational interaction
* visualization of system state
* monitoring of sessions and operational activity
* administrative and configuration interaction
* observability and diagnostics access

The Web Frontend Interface complements the local interaction surfaces embedded in the robot and extends system access to external computing devices.

---

## Interaction Model

Interaction through the Web Frontend Interface follows a client–server interaction structure.

1. A user accesses the web client through a browser-based interface.
2. Authentication and authorization mechanisms validate access through the Identity, Access and Security module.
3. The web client exchanges requests, commands, or queries with backend services.
4. Backend services process the interaction event and propagate it toward internal subsystems.
5. Responses, state updates, or event streams are returned to the client interface.

This interaction model supports both request–response communication and realtime event propagation.

---

## Core Responsibilities

The Web Frontend Interface supports several categories of browser-based remote interaction.

### Remote Conversational Interaction

The interface exposes browser-based communication surfaces through which users exchange messages, requests, and dialogue turns with the system.

### System Monitoring

The interface exposes visual representations of system state, session status, operational context, and hardware-related information.

### Administrative Interaction

The interface exposes management and configuration surfaces through which authorized users interact with administrative system functions.

### Observability Access

The interface exposes operational information associated with logs, telemetry, metrics, and event traces generated by backend subsystems.

### Remote Command Execution

The interface produces remote interaction events capable of triggering system behaviour, configuration changes, or operational actions.

---

## Interaction Surfaces

The Web Frontend Interface exposes several categories of browser-based interaction surfaces.

These include:

* system dashboard surfaces
* conversational chat surfaces
* project and task management surfaces
* administration panels
* monitoring and diagnostics views
* configuration views

Each of these surfaces presents graphical interaction elements through which users observe the system or generate remote interaction events.

---

## Interaction Events

The Web Frontend Interface produces several categories of browser-originated interaction events.

These include:

* authentication requests
* conversational interaction events
* command requests
* configuration change events
* project management events
* administrative commands
* system inspection requests
* hardware-related control requests

These events are transmitted to backend services responsible for processing remote interaction and coordinating subsystem behaviour.

---

## Interaction Outputs

The Web Frontend Interface exposes graphical outputs representing system responses, system state, and operational information.

These outputs include:

* system responses to user interaction
* session and conversation information
* project or task status
* hardware telemetry and operational state
* alerts and notifications
* logs, metrics, and diagnostics views
* confirmation prompts and configuration feedback

These outputs allow users and administrators to observe and influence the system through a remote graphical interaction surface.

---

## Relationship With Other Modules

### Identity, Access and Security

Authentication and authorization procedures governing browser-based access are defined by the Identity, Access and Security module.

### Backend and Application Services

The Web Frontend Interface communicates with backend services responsible for processing interaction events, managing system state, and orchestrating subsystem behaviour.

### Cognitive Core

Interaction events originating from the web client propagate toward the cognitive core, where they influence reasoning, decision processes, and system behaviour.

### Dialogue and Session System

Conversational interaction through the web client integrates with dialogue management and session tracking mechanisms.

### Action and Expression

System behaviour triggered through browser-based interaction may result in physical or digital actions executed by downstream subsystems.

### Observability

The interface exposes logs, metrics, and state information generated by observability-related backend mechanisms.

---

## Structural Properties of Browser-Based Remote Interaction

### Network Dependency

Interaction requires network connectivity between the browser-based client and backend services.

### Distributed Access

Multiple users or client devices may access the interface from different locations.

### Remote Operational Visibility

The interface exposes operational state and system behaviour without requiring physical presence near the robot.

### Realtime Update Capability

The interaction model supports propagation of live state changes, event streams, and telemetry updates.

### Authorization-Scoped Access

Administrative and operational capabilities exposed through the interface are constrained by authentication and authorization mechanisms.

---

# 2.4 Touch / Physical Interaction

## Definition

Touch / Physical Interaction refers to direct contact-based interaction between humans and the NORA system through tactile sensors, physical buttons, touch-sensitive surfaces, or body-contact detection mechanisms.

This interaction modality relies on physical proximity and intentional contact with the robot body or control elements. Through physical contact, users generate interaction events that the system interprets as commands, confirmations, interruptions, or social signals.

Within the Interaction Interfaces module, Touch / Physical Interaction represents the primary tactile interaction surface available to users physically present near the system.

---

## Architectural Role

Within the system architecture, Touch / Physical Interaction functions as a direct local control interface.

Through this interface, users located near the robot generate interaction events through physical contact with the device.

The interface supports several categories of interaction:

* initiation of interaction
* confirmation or cancellation of actions
* triggering of predefined system behaviours
* interruption of ongoing operations
* tactile social interaction with the embodied system

Due to the deterministic nature of contact events, this interface provides a reliable and immediate interaction mechanism for both routine control and safety-critical intervention.

---

## Interaction Model

Touch-based interaction follows a stimulus–event–response interaction structure.

1. A user performs physical contact with a tactile surface or control element.
2. Sensors detect the contact event.
3. The perception subsystem captures the signal produced by the tactile hardware.
4. The event is transformed into a normalized interaction event.
5. The event is propagated to the cognitive core and related subsystems.

Because tactile interaction produces discrete hardware-level signals, interaction events originating from this interface are typically unambiguous and rapidly processed.

---

## Core Responsibilities

The Touch / Physical Interaction interface supports several categories of tactile interaction.

### Direct Control

Users generate direct control commands through physical contact with control elements.

These commands may initiate interaction, confirm actions, cancel operations, or trigger predefined system behaviours.

### Social Contact Interaction

Tactile interaction may also represent social signals between humans and the embodied system.

Physical contact events occurring on designated surfaces of the robot body may influence expressive behaviour or interaction state.

### Safety Overrides

Physical interaction mechanisms provide immediate safety intervention capabilities.

These mechanisms include dedicated controls capable of interrupting system behaviour or halting ongoing physical operations.

### Alternative Interaction Channel

Touch interaction provides an alternative interaction channel when voice, gesture, or remote interfaces are unavailable or unsuitable.

---

## Interaction Surfaces

The Touch / Physical Interaction interface may expose several categories of tactile interaction surfaces.

These include:

* physical hardware buttons
* capacitive touch sensors
* pressure-sensitive surfaces
* touchscreen surfaces
* body-mounted contact sensors
* emergency stop controls

Each tactile surface generates hardware-level signals that are interpreted by the perception subsystem as interaction events.

---

## Interaction Events

The Touch / Physical Interaction interface produces several categories of interaction events.

Examples include:

* button press events
* touchscreen interaction events
* body-contact detection events
* tactile gesture events
* emergency stop activation events

These events are propagated to backend subsystems responsible for interpreting interaction commands and determining appropriate system responses.

---

## Interaction Outputs

Touch-based interaction events may trigger several categories of system responses.

These responses may include:

* initiation of interaction sessions
* confirmation or cancellation of actions
* interruption of system behaviour
* execution of predefined commands
* activation of safety mechanisms

Feedback related to tactile interaction may be expressed through other system output channels such as speech synthesis, visual indicators, screen messages, or robotic motion.

---

## Relationship With Other Modules

### Perception

The perception subsystem processes raw signals generated by tactile sensors and converts them into normalized interaction events.

### Cognitive Core

Interaction events generated through tactile input propagate toward the cognitive core, where they influence system state, reasoning processes, and behaviour planning.

### Action and Expression

System responses triggered by tactile interaction may be expressed through speech output, movement, visual indicators, or other expressive behaviours.

### Identity, Access and Security

Certain tactile controls may be subject to authorization policies depending on system configuration and safety requirements.

---

## Structural Properties of Physical Interaction

The Touch / Physical Interaction interface exhibits several structural properties associated with embodied systems.

### Physical Proximity Requirement

Interaction requires the presence of a user physically near the robot.

### Deterministic Event Generation

Tactile hardware generates discrete interaction signals that produce well-defined interaction events.

### Immediate Response Capability

Physical interaction enables rapid user control of the system due to direct hardware signal generation.

### Safety-Critical Control Path

Certain tactile interaction surfaces provide direct mechanisms for interrupting or halting system behaviour.

---

# 2.5 NFC / RFID Interface

## Definition

NFC / RFID Interaction refers to proximity-based interaction between users and the NORA system through Near Field Communication (NFC) or Radio Frequency Identification (RFID) tags, cards, badges, or wearable devices.

Through short-range wireless identification, users generate interaction events by bringing a compatible device close to an NFC or RFID reader integrated into the robot.

Unlike voice, screen, or touch interfaces, this interaction modality does not require speech, visual interfaces, or manual input. Interaction occurs through proximity detection and tag identification.

Within the Interaction Interfaces module, NFC / RFID Interaction represents the primary proximity-based identification interface available to users physically present near the system.

---

## Architectural Role

Within the system architecture, the NFC / RFID interface functions as a proximity-based identification and activation mechanism.

Through this interface, the system can associate detected tags with identities, profiles, permissions, or predefined actions.

The interface supports several categories of interaction:

* user identification
* loading of user context or profile
* activation of interaction sessions
* switching of operational modes
* triggering of predefined system behaviours

Because NFC / RFID interaction requires physical proximity, it provides a fast and low-friction mechanism for identifying users and activating system functionality.

---

## Interaction Model

NFC / RFID interaction follows a proximity detection interaction structure.

1. A user presents a tag, card, badge, or compatible device near the NFC / RFID reader.
2. The reader detects the device and retrieves its identifier.
3. The perception subsystem captures the identifier provided by the reader hardware.
4. The identifier is converted into a normalized interaction event.
5. The system resolves the identifier to an associated identity, permission level, or predefined command.

Once resolved, the corresponding system behaviour or context transition is triggered.

Because tag detection is hardware-driven, these events typically occur rapidly and require minimal user effort.

---

## Core Responsibilities

The NFC / RFID interface supports several categories of proximity-based interaction.

### User Identification

Detected tags may be associated with registered user identities.

When a tag is detected, the system may retrieve the identity associated with the identifier and load user-specific interaction context.

### Profile Context Loading

Tag detection may trigger the loading of user preferences or interaction parameters associated with the detected identity.

These parameters may influence language settings, permissions, or personalized behaviour.

### System Activation

Tag detection may activate the system or initiate interaction sessions.

Activation mechanisms allow users to begin interaction without requiring voice commands or manual interface navigation.

### Access Control

Certain tags may correspond to authorization credentials.

Detection of these credentials may grant or restrict access to administrative capabilities or restricted operational modes.

### Triggered Behaviour

Specific identifiers may be mapped to predefined system commands or actions.

Detection of these identifiers triggers execution of the associated behaviour.

---

## Interaction Surfaces

The NFC / RFID interface exposes proximity-based interaction surfaces associated with hardware readers integrated into the robot.

Typical mechanisms include:

* NFC cards
* RFID badges
* NFC stickers
* wearable NFC devices
* smartphone NFC interaction

Readers may be integrated into designated areas of the robot body where proximity-based interaction occurs.

---

## Interaction Events

The NFC / RFID interface produces several categories of interaction events.

Examples include:

* known tag detected
* unknown tag detected
* authorized credential detected
* restricted credential detected
* tag removal or absence event

These events are propagated to backend subsystems responsible for resolving identifiers and determining the appropriate system response.

---

## Interaction Outputs

Detection of NFC / RFID events may trigger several categories of system responses.

These responses may include:

* loading of a user profile
* activation of a session
* switching of operational context
* authorization approval or denial
* execution of predefined commands

Feedback related to tag detection may be communicated through other system output channels such as speech synthesis, visual indicators, screen messages, or LED signals.

---

## Relationship With Other Modules

### Identity, Access and Security

Identifiers detected through NFC / RFID readers may be mapped to user identities or authorization credentials managed by the identity and access subsystem.

### Perception

The perception subsystem processes signals generated by NFC or RFID reader hardware and converts them into normalized interaction events.

### Cognitive Core

Resolved identifiers influence system behaviour, operational context, and decision processes.

### Dialogue and Sessions

Tag detection may initiate or resume conversational sessions associated with identified users.

### Action and Expression

The system may respond to tag detection events through speech output, visual indicators, or other expressive behaviours.

---

## Structural Properties of Proximity Interaction

The NFC / RFID interface exhibits several structural properties related to proximity-based interaction.

### Proximity Requirement

Interaction occurs only when a compatible tag is placed within the detection range of the reader.

### Deterministic Identifier Detection

Hardware readers generate discrete identifier signals corresponding to detected tags.

### Rapid Interaction Trigger

Tag detection enables immediate activation of system behaviour or context transitions.

### Identity-Linked Interaction

Interaction events generated through NFC / RFID interfaces are commonly associated with user identity or authorization credentials.

---

# 2.6 Gestures as an Interface

## Definition

Gestures as an Interface refers to interaction between humans and the NORA system through intentional human body movements such as hand gestures, arm movements, posture signals, or other visible physical cues.

Through this modality, users generate interaction events by performing recognizable movements that are interpreted by the system as commands, confirmations, interruptions, or attention signals.

Unlike voice interaction, gesture interaction allows users to communicate with the system silently and without physical contact, enabling distance-based interaction within the robot's visual perception range.

Within the Interaction Interfaces module, the Gesture Interface represents the primary non-verbal visual interaction surface available to users within the observable environment of the system.

---

## Architectural Role

Within the system architecture, the Gesture Interface functions as a visual non-verbal interaction channel.

Through this interface, the system interprets recognized body movements as interaction events that influence system behaviour.

The interface supports several categories of interaction:

* attention signals directed at the system
* non-verbal command input
* confirmation or rejection gestures
* interruption of ongoing system behaviour
* non-verbal interaction in shared environments

Gesture interaction complements other interaction interfaces such as voice, touch, and screen-based interaction, providing an alternative communication mechanism when speech or direct contact is not suitable.

---

## Interaction Model

Gesture-based interaction follows a perception–event–response interaction structure.

1. A user performs a gesture within the observable environment of the robot.
2. The vision perception subsystem detects and classifies the gesture.
3. The classified gesture is converted into a normalized interaction event.
4. The interaction event is propagated to the cognitive core and related subsystems.
5. The system determines the corresponding response or behaviour.

Because gesture interaction depends on visual detection and classification, interaction events are generated only after successful perception and gesture recognition.

---

## Core Responsibilities

The Gesture Interface supports several categories of non-verbal interaction.

### Attention Signalling

Users may perform gestures intended to attract the system's attention.

These signals indicate the presence of a user attempting to initiate interaction.

### Command Input

Certain gestures correspond to predefined command events interpreted by the system.

These commands influence system behaviour or trigger specific actions.

### Confirmation Gestures

Gestures may represent confirmation signals used to approve proposed actions or system requests.

### Cancellation and Interruption

Specific gestures may signal cancellation or interruption of ongoing system behaviour.

### Non-Verbal Interaction

Gesture interaction allows communication with the system without spoken language or physical contact.

This interaction modality is useful in environments where speech is impractical or undesirable.

---

## Interaction Surfaces

Gesture interaction occurs within the visual observation space of the robot.

Interaction surfaces include:

* hand gestures
* arm movements
* posture-based signals
* directional pointing gestures
* body movement signals

These visual signals are captured by the perception subsystem and interpreted as interaction events.

---

## Interaction Events

The Gesture Interface produces several categories of interaction events.

Examples include:

* greeting gesture detected
* stop gesture detected
* pointing gesture detected
* confirmation gesture detected
* cancellation gesture detected

These events are generated after gesture recognition by the perception subsystem and propagated to backend subsystems responsible for behavioural interpretation.

---

## Interaction Outputs

Gesture interaction events may trigger several categories of system responses.

These responses may include:

* acknowledgement of user presence
* interruption of current behaviour
* confirmation of commands
* attention focusing toward the user
* execution of gesture-triggered commands

Feedback related to gesture interaction may be expressed through speech synthesis, robot movement, visual indicators, or screen-based feedback.

---

## Relationship With Other Modules

### Perception – Vision

The perception subsystem performs gesture detection, pose estimation, and gesture classification.

Recognized gestures are converted into normalized interaction events that are consumed by the Gesture Interface.

### Cognitive Core

Interaction events generated through gestures influence system state, reasoning processes, and behavioural planning.

### Action and Expression

The system may respond to gesture interaction through movement, speech output, visual indicators, or other expressive behaviours.

### Dialogue and Session System

Gesture interaction may initiate or influence conversational sessions between users and the system.

---

## Structural Properties of Gesture Interaction

The Gesture Interface exhibits several structural properties associated with visual non-verbal interaction.

### Visual Field Dependency

Gestures must occur within the observable visual field of the robot's perception sensors.

### Perception-Dependent Event Generation

Interaction events are generated only after gesture recognition by the perception subsystem.

### Distance-Based Interaction

Gesture interaction allows users to communicate with the system without direct contact or speech.

### Non-Verbal Communication Channel

Gestures provide a communication channel independent of spoken language.

---

# 2.7 Remote Interfaces

## Definition

Remote Interfaces refer to interaction channels that allow users or external systems to communicate with, observe, or control the NORA system from devices that are not physically integrated into the robot.

Through network-connected devices, interaction events may be generated and transmitted to the system without requiring physical proximity to the robot.

Unlike local interfaces such as the Local Screen or Touch Interaction surfaces, remote interfaces operate through network communication and distributed client devices.

Within the Interaction Interfaces module, Remote Interfaces represent external interaction entry points through which the system may be accessed from outside the robot's physical environment.

---

## Architectural Role

Within the system architecture, Remote Interfaces function as network-based interaction channels that extend the reach of the system beyond its embodied hardware.

Through these interfaces, users or external systems may interact with the robot from remote locations.

The interface supports several categories of interaction:

* remote user communication with the system
* remote observation of system state
* remote command execution
* reception of system notifications
* integration with external digital services

Remote Interfaces allow the system to operate as part of a distributed computing environment rather than as an isolated robotic device.

---

## Interaction Model

Remote interaction follows a network-mediated interaction structure.

1. A remote device or external system generates a request, command, or query.
2. The request is transmitted through a network communication channel.
3. Backend services receive and process the incoming interaction event.
4. The system generates internal events or behavioural commands.
5. Responses or state updates are transmitted back to the remote interface.

Communication may occur through multiple interaction patterns including request–response communication and event-driven messaging.

---

## Core Responsibilities

The Remote Interfaces module supports several categories of distributed interaction.

### Remote User Interaction

Users may interact with the system from external devices that are not physically connected to the robot.

These interactions may include conversational communication, command input, or status requests.

### Remote Monitoring

Remote interfaces may expose information describing the internal state and operational behaviour of the system.

This information may include system state, active sessions, or hardware status.

### Remote Command Execution

Interaction events originating from remote devices may trigger commands executed by the system.

These commands may influence system behaviour or initiate specific operations.

### System Notifications

The system may generate outbound communication directed toward remote interfaces in order to report events or system state changes.

### External System Integration

External digital systems may interact with NORA through defined remote interfaces.

These integrations allow the robot to participate in larger digital ecosystems.

---

## Interaction Surfaces

Remote interaction may occur through several categories of external client interfaces.

These include:

* mobile applications
* tablet interfaces
* remote web clients
* administrative terminals
* wearable devices
* external service clients

Each client interface communicates with backend services responsible for processing remote interaction events.

---

## Interaction Events

The Remote Interfaces module produces several categories of interaction events.

Examples include:

* remote command events
* remote status requests
* configuration change events
* administrative commands
* external API requests

These interaction events are transmitted through network communication channels and processed by backend subsystems.

---

## Interaction Outputs

Remote Interfaces expose outputs that communicate system responses or operational information to remote devices.

These outputs may include:

* system notifications
* status updates
* responses to remote commands
* task completion events
* conversation responses

These outputs allow users and external systems to observe and interact with the robot without being physically present.

---

## Relationship With Other Modules

### Backend and Application Layer

Remote Interfaces communicate with backend services responsible for processing interaction events, managing system state, and coordinating subsystem behaviour.

### Identity, Access and Security

Authentication and authorization policies determine which remote entities may access specific system capabilities.

### Cognitive Core

Interaction events originating from remote interfaces influence system reasoning, decision-making, and behavioural planning.

### Dialogue and Session System

Remote users may initiate or participate in conversational sessions with the system.

### Action and Expression

Commands originating from remote interfaces may trigger actions executed by the robot or generate responses returned through remote communication channels.

---

## Structural Properties of Remote Interaction

The Remote Interfaces module exhibits several structural properties associated with distributed system interaction.

### Network Dependency

Interaction requires network connectivity between remote clients and backend services.

### Distributed Interaction

Multiple remote clients may interact with the system concurrently from different locations.

### Asynchronous Communication

Certain interaction flows may occur asynchronously through event-driven communication channels.

### External System Participation

Remote interfaces allow external digital systems to interact with the robot as part of a larger distributed ecosystem.

---

## Internal Architecture Overview

The **Interaction Interfaces** module defines the set of human–system interaction channels through which users communicate with the NORA system.

These interfaces represent the boundary layer between human users and the internal cognitive architecture. Through these interfaces, interaction events generated by humans enter the system and system responses are exposed through human‑perceivable channels.

The module organizes multiple complementary interaction modalities that together support multimodal interaction with the system.

---

## Architectural Structure

```
Interaction Interfaces
│
├── Voice Interface
│ ├── spoken interaction channel
│ ├── conversational dialogue interaction
│ ├── spoken command input
│ ├── confirmation and rejection signals
│ ├── interruption and cancellation signals
│ ├── dictated text input
│ ├── voice interaction events
│ ├── spoken responses
│ ├── interaction feedback signals
│ ├── multilingual interaction context
│ ├── voice interaction inputs
│ └── voice interaction outputs
│
├── Local Screen Interface
│ ├── visual interaction surface
│ ├── graphical feedback indicators
│ ├── structured information display
│ ├── graphical interface controls
│ ├── expressive visual output
│ ├── contextual interaction information
│ ├── visual interaction events
│ ├── visual interaction outputs
│ ├── system state indicators
│ ├── screen interaction inputs
│ └── screen interaction outputs
│
├── Web Frontend Interface
│ ├── browser‑based interaction surface
│ ├── remote conversational interaction
│ ├── system dashboards
│ ├── monitoring and diagnostics views
│ ├── administration panels
│ ├── project and task management views
│ ├── configuration interfaces
│ ├── browser interaction events
│ ├── web interface outputs
│ ├── remote system monitoring
│ ├── web interaction inputs
│ └── web interaction outputs
│
├── Touch / Physical Interaction
│ ├── tactile interaction mechanisms
│ ├── hardware buttons
│ ├── capacitive touch sensors
│ ├── pressure sensors
│ ├── body contact sensors
│ ├── emergency stop controls
│ ├── tactile interaction events
│ ├── safety override signals
│ ├── physical interaction inputs
│ └── physical interaction outputs
│
├── NFC / RFID Interface
│ ├── proximity interaction channel
│ ├── tag identification
│ ├── user identification through tags
│ ├── profile switching
│ ├── system activation
│ ├── access control through tags
│ ├── triggered system actions
│ ├── NFC interaction events
│ ├── proximity interaction inputs
│ └── proximity interaction outputs
│
├── Gesture Interface
│ ├── gesture‑based interaction channel
│ ├── attention request gestures
│ ├── command gestures
│ ├── confirmation gestures
│ ├── cancellation gestures
│ ├── non‑verbal interaction signals
│ ├── gesture interaction events
│ ├── gesture interaction responses
│ ├── gesture interaction inputs
│ └── gesture interaction outputs
│
└── Remote Interfaces
  ├── remote device interaction
  ├── mobile device interfaces
  ├── tablet interfaces
  ├── remote web clients
  ├── external service interfaces
  ├── remote monitoring interfaces
  ├── remote command execution
  ├── system notifications
  ├── remote interaction events
  ├── remote interaction inputs
  └── remote interaction outputs
```

---

## Architectural Layers

The Interaction Interfaces module operates through several complementary layers that structure how human interaction enters and exits the system.

| Layer                             | Responsibility                                                                 |
| --------------------------------- | ------------------------------------------------------------------------------ |
| **Interaction Channel Layer**     | Defines the modalities through which humans communicate with the system        |
| **Interaction Surface Layer**     | Provides the physical or digital surfaces where interaction occurs             |
| **Interaction Event Layer**       | Normalizes interaction inputs into structured system events                    |
| **Interaction Feedback Layer**    | Communicates system state and responses back to users                          |
| **Multimodal Coordination Layer** | Ensures consistent behaviour across multiple simultaneous interaction channels |

Together, these layers establish the **human–system interaction boundary of the NORA architecture**, ensuring that user actions can be interpreted consistently regardless of the interface used while maintaining coherent multimodal interaction across the system.
