# 2. Interaction Interfaces

## Definition

The **Interaction Interfaces** module defines every human-facing channel through which a person can intentionally communicate with, control, observe, or interrupt NORA.

This module describes the **surfaces of interaction** between the user and the system. It answers a fundamental architectural question:

**How does a human access NORA in practice?**

NORA is not designed as a purely software-based assistant hidden behind a single chat box or API. It is conceived as a multimodal embodied system that can exist in a physical environment, interact through speech, screen, touch, gesture, and proximity technologies, and also be accessed remotely from external devices. Because of this, interaction cannot be modeled as a single input-output channel. It must be treated as a full architectural domain.

The Interaction Interfaces module groups all those channels into one coherent layer so that the rest of the architecture can remain independent from the particular interface being used at any given moment.

---

## Architectural Purpose

The purpose of this module is to provide a structured abstraction for all intentional user interaction channels.

This means that the module is responsible for defining:

* how users initiate interaction with NORA
* how users receive feedback from NORA
* how commands, confirmations, interruptions, and selections are expressed
* how local and remote interaction channels coexist
* how the system exposes its state and capabilities to humans

At the architectural level, this module does **not** define how raw signals are processed internally. Instead, it defines the **interaction role** of each channel.

For example:

* a spoken sentence belongs here as a user interaction mechanism
* the acoustic processing of that sentence belongs to perception
* a gesture used to say “stop” belongs here as an interface command
* the computer vision model detecting the hand pose belongs to perception

This distinction is essential to avoid mixing user experience design with signal processing and sensing logic.

---

## Why This Module Is Necessary in NORA

In a conventional application, the interface may be reduced to a web or mobile UI. In NORA, that is not sufficient.

NORA is intended to operate as a persistent intelligent system with:

* physical embodiment
* multimodal perception
* conversational dialogue
* long-lived sessions
* local and remote control
* possible access by multiple users with different roles

Because of that, the system must support multiple ways of interacting depending on the situation.

Examples:

* a person may speak to NORA naturally from across the room
* a user may touch the robot to interrupt or confirm an action
* an administrator may monitor NORA remotely through a web dashboard
* a user may identify themselves using NFC
* a gesture may serve as a silent command in situations where speaking is inconvenient

All of these are interfaces, but they are not equivalent. Each one has different constraints, affordances, security implications, latency expectations, and UX consequences. This module exists to model that diversity cleanly.

---

## Scope of the Module

The Interaction Interfaces module includes all channels whose main purpose is **intentional human-system interaction**.

Typical examples include:

* speaking to NORA
* listening to spoken responses
* seeing visual feedback on the robot’s local screen
* interacting through a browser-based frontend
* touching buttons or tactile surfaces
* using NFC or RFID tags for quick identification or activation
* issuing commands through gestures
* accessing NORA from remote devices or external terminals

This module does **not** include:

* raw audio capture as a sensing process
* camera analysis as visual perception
* intent inference as a semantic processing task
* hardware execution as an action layer concern
* authentication and permissions as identity and security concerns

Those belong to other architectural modules.

---

## Architectural Role Within the System

The Interaction Interfaces module acts as the **boundary layer between humans and the rest of NORA**.

It sits between the user and several internal subsystems, especially:

* perception
* the core cognitive system
* the dialogue and session layer
* planning and agent selection
* action and expression
* backend application services

Conceptually, the flow is similar to this:

**Human ↔ Interaction Interface ↔ Internal Processing / Decision Layers ↔ Action / Feedback**

This means that interaction interfaces are not the intelligence of the system themselves. They are the **entry and exit points** through which intelligence becomes usable.

Without this layer:

* the system would have no structured way to receive intentional human input
* outputs would not be organized according to user-facing channels
* local and remote interaction would become mixed with internal logic
* modality-specific behaviours would be hard to manage and extend

---

## Core Design Principles

Several design principles should guide the implementation of this module.

### Modality Independence

The rest of the system should not depend on whether the user interacted through voice, touch, gesture, or web interface unless that distinction is explicitly relevant.

This allows NORA to map multiple interfaces to shared internal events such as:

* confirm
* cancel
* request_help
* start_session
* stop_action
* select_target

A confirmation spoken aloud and a confirmation produced by touching a screen should be able to converge to a common interaction event when appropriate.

### Multimodal Coexistence

NORA should support several interaction interfaces at the same time.

For example:

* voice may be active while the local screen displays live feedback
* a remote admin may monitor the system while a local user interacts physically
* gesture and voice may complement each other during a conversation

The architecture must therefore support simultaneous or overlapping modalities without ambiguity.

### Interruptibility

Human-facing systems must always provide clear ways to interrupt, stop, cancel, or override ongoing interaction.

This is especially important in NORA because the system may:

* speak continuously
* execute actions in the physical world
* access hardware
* run long multi-step plans

Interfaces must support interruption through multiple modalities such as:

* verbal cancellation
* stop gesture
* button press
* remote admin command

### Feedback Visibility

Every interface should provide sufficient feedback so the user understands what NORA is doing.

Feedback may be:

* spoken
* textual
* visual
* tactile
* remote

This principle is critical for trust and usability. A user should be able to tell whether NORA is:

* listening
* waiting
* thinking
* acting
* blocked
* requesting confirmation
* encountering an error

### Accessibility and Redundancy

Different users and contexts require different interaction channels.

For that reason, important interaction flows should not depend on a single modality only. When possible, NORA should support equivalent interaction paths such as:

* voice or touch
* local screen or spoken response
* gesture or verbal command
* remote control or local control

This improves accessibility, resilience, and practical usability.

### Channel-Aware Security

Although identity and permission logic belong elsewhere, each interaction channel may imply different security and trust constraints.

For example:

* a public touchscreen may require stricter restrictions than a trusted admin terminal
* a gesture-based command may be acceptable for simple actions but insufficient for sensitive actions
* NFC-based identification may unlock a profile but still require additional confirmation for dangerous commands

Therefore, interfaces must be designed so they can pass enough context to downstream security and authorization layers.

---

## Main Responsibilities

The Interaction Interfaces module is responsible for several architectural functions.

### 1. Interaction Entry Points

It defines how a user begins interacting with NORA.

Examples include:

* saying the wake phrase and then speaking
* tapping a screen element
* touching the robot
* scanning an NFC tag
* opening the web frontend
* sending a remote command

### 2. Interaction Output Surfaces

It defines how NORA presents information back to the user.

Examples include:

* spoken responses
* screen messages
* visual states
* menus
* notifications
* dashboards

### 3. Control Signals

It defines how humans express low-level interaction control intentions such as:

* confirm
* deny
* cancel
* repeat
* continue
* stop
* select

These control signals may appear through several modalities.

### 4. Human-Usable Operational Access

It defines how users and administrators can inspect and influence the system from user-facing surfaces.

Examples include:

* viewing current robot state
* accessing logs through the frontend
* triggering manual actions
* switching mode
* observing active conversation or hardware state

### 5. Channel Normalization

It provides a conceptual bridge between many heterogeneous interfaces and a smaller set of normalized internal interaction events.

This normalization is key for keeping the architecture modular.

---

## Relationship With Other Modules

The Interaction Interfaces module has strong relationships with several other architectural domains.

### Relationship With Perception

Perception detects and analyzes raw signals.

Interaction Interfaces define the human meaning of those channels.

Examples:

* microphone audio processing belongs to perception
* speaking with NORA belongs to interaction interfaces
* camera-based gesture recognition belongs to perception
* using a recognized gesture as a command belongs to interaction interfaces

### Relationship With Identity, Access and Security

Interaction channels are often the path through which authentication or access control begins, but the actual trust logic belongs to the identity and security layer.

Examples:

* the web frontend exposes a login page, but login validation belongs to authentication
* NFC acts as an interaction channel for identification, but access control belongs to authorization

### Relationship With the Core Cognitive System

The core decides how NORA should behave operationally.

Interaction interfaces provide the human-visible and human-usable means to start, shape, or interrupt that behaviour.

### Relationship With Dialogue and Sessions

Dialogue and sessions manage conversational continuity.

Interaction interfaces provide the user-facing channels through which that dialogue is actually experienced.

### Relationship With Planning and Agents

Planning decides what NORA should do.

Interaction interfaces define how a plan may request clarification, confirmation, data input, or user feedback.

### Relationship With Action and Expression

Action and expression define what NORA does toward the world.

Interaction interfaces define the subset of those actions that are experienced as direct human interaction surfaces.

For example, the local screen and spoken output are both interaction interfaces, but they are powered by downstream output and action subsystems.

---

## Internal Organization of the Module

This architectural module is divided into several submodules, each representing a distinct interaction channel.

* **2.1 Voice as an Interface**
  Spoken conversational and command-based interaction.

* **2.2 Local Screen**
  Physical display embedded in the robot.

* **2.3 Web Frontend**
  Browser-based remote interface for users and administrators.

* **2.4 Touch / Physical Interaction**
  Direct contact-based interaction through touch surfaces, buttons, or body interaction.

* **2.5 NFC / RFID**
  Proximity-based interface for identification, activation, and profile switching.

* **2.6 Gestures as an Interface**
  Non-verbal human commands expressed through body movement.

* **2.7 Remote Interfaces**
  External-device access channels such as mobile apps, tablets, admin terminals, and remote APIs.

Each of these submodules represents a different way for humans or human-operated systems to interact with NORA.

---

## Common Interaction Patterns Across Interfaces

Although the channels differ, many interaction patterns are shared across them.

### Initiation

A user starts interaction.

Examples:

* speaking to NORA
* opening a dashboard
* scanning an NFC tag
* touching the robot

### Query or Command

A user asks for information or requests an action.

Examples:

* asking a question
* requesting a task
* selecting an option on screen
* making a gesture command

### Confirmation or Rejection

A user approves or rejects a proposed action.

Examples:

* saying “yes” or “no”
* pressing confirm on screen
* performing a confirmation gesture

### Interruption

A user stops an ongoing behaviour.

Examples:

* saying “cancel”
* pressing an emergency button
* performing a stop gesture
* sending a remote override command

### Follow-Up Interaction

A user continues the exchange across turns.

Examples:

* continuing a conversation
* refining a search
* modifying a command
* reopening a persistent session remotely

These patterns help define common semantics across different modalities.

---

## Representative Inputs

The Interaction Interfaces module may receive many kinds of human-originated inputs, depending on the active channel.

Representative examples include:

* spoken wake phrase
* spoken free-form request
* spoken confirmation
* spoken cancellation
* dictated text
* touch event
* button press
* touchscreen selection
* emergency stop press
* NFC tag scan
* RFID credential scan
* greeting gesture
* stop gesture
* pointing gesture
* silent confirmation gesture
* remote browser command
* admin terminal request
* external user-facing API request

These are interface-level inputs. Their lower-level signal extraction may occur in other modules.

---

## Representative Outputs

The Interaction Interfaces module may expose or trigger many forms of human-facing output.

Representative examples include:

* spoken reply
* spoken clarification request
* local text update
* image shown on screen
* live camera preview
* notification banner
* menu rendered on local UI
* dashboard state update
* visual confirmation prompt
* remote status update
* browser alert
* interaction mode indicator
* active listening indicator
* cancellation acknowledgment

These outputs are the user-visible manifestation of deeper internal processes.

---

## Architectural Challenges

This module introduces several design challenges that should be considered early.

### Consistency Across Modalities

Different interfaces should feel like access paths to the same system, not unrelated subsystems.

### Conflict Resolution

The system may receive overlapping commands from multiple channels at the same time.

Examples:

* a local user speaks while an admin remotely sends a command
* a gesture says stop while the touchscreen still shows a pending confirmation

The architecture must define precedence, arbitration, or synchronization rules.

### Latency Expectations

Users expect different response times depending on the channel.

Examples:

* voice interaction requires fast turn-taking
* dashboards may tolerate slightly slower refresh cycles
* emergency interruption must be immediate

### Safety and Intentionality

Some channels are inherently more ambiguous than others.

For example, gestures or touch events may be harder to interpret than explicit typed or spoken input. The architecture should allow different confidence thresholds and confirmation policies depending on the interaction channel.

### Local vs Remote Priority

NORA may need policies defining whether local human interaction has priority over remote commands, especially for embodied actions.

---

## Design Implications for Implementation

Even though this section is architectural rather than implementation-specific, it implies several practical design choices.

The system will likely need:

* channel-specific adapters or handlers
* a normalized interaction event schema
* modality-aware feedback policies
* interrupt and cancel semantics shared across channels
* synchronization between local and remote interfaces
* user-presence-aware interaction routing
* per-channel trust or safety metadata

These ideas can later be reflected in backend services, event models, FSM transitions, frontend states, and hardware control rules.

---

## Summary

The **Interaction Interfaces** module defines the complete set of human-facing channels through which NORA can be used.

It includes spoken interaction, local visual interfaces, web-based control surfaces, physical touch, proximity-based identification, gesture commands, and remote access paths.

Its architectural value is that it separates **how humans interact with NORA** from:

* how signals are sensed
* how meanings are inferred
* how decisions are made
* how actions are executed internally

By modeling interaction interfaces as a dedicated module, the architecture becomes clearer, more extensible, more multimodal, and better aligned with the real nature of NORA as an embodied cognitive system.

# 2.1 Voice as an Interface

## Definition

**Voice as an Interface** refers to the use of spoken language as a primary human interaction channel with NORA. Through voice, users can communicate intentions, ask questions, issue commands, confirm actions, interrupt ongoing processes, and maintain natural conversations with the system.

Unlike traditional graphical interfaces that rely on screens, keyboards, or touch inputs, voice interaction allows users to interact with NORA in a **natural, hands-free, and context-aware manner**. This makes voice one of the most important interaction modalities for an embodied cognitive system.

In the architecture of NORA, voice is treated as an **interaction interface**, not as a raw sensory signal. The acoustic processing required to detect and interpret speech (microphone capture, speech recognition, wakeword detection, etc.) belongs to the **Perception module**. The present module focuses instead on the **role of voice as a communication medium between humans and the system**.

---

## Architectural Role

The Voice Interface serves as the **primary conversational gateway** between users and NORA. It allows the system to function as a spoken assistant capable of natural dialogue and interactive collaboration.

Through this interface, users can:

* initiate interaction with the system
* request information
* instruct NORA to perform actions
* engage in multi-turn conversations
* confirm or reject system proposals
* interrupt ongoing activities
* request clarifications
* dictate text
* practice language learning or tutoring activities

For NORA, spoken interaction also allows **situational awareness** in environments where visual or touch interfaces are impractical.

---

## Interaction Model

Voice interaction in NORA generally follows a conversational cycle composed of several stages:

1. **Activation**

   The user initiates interaction, typically by addressing the system using a wake phrase or direct speech input.

2. **Listening Phase**

   NORA captures spoken input from the user while indicating that it is actively listening.

3. **Interpretation Phase**

   The spoken input is processed by downstream modules (perception, semantic interpretation, and planning).

4. **Response Generation**

   The system prepares a response or decides on a course of action.

5. **Spoken Output**

   NORA delivers feedback, answers, or requests clarification through synthesized speech.

6. **Continuation or Termination**

   The conversation may continue through follow-up turns or terminate if the interaction concludes.

This interaction loop enables **natural conversational exchanges** between humans and the system.

---

## Core Responsibilities

The Voice Interface module is responsible for enabling several forms of spoken interaction.

### Conversational Interaction

Users can speak freely with NORA in a natural conversational manner.

Examples:

* asking general questions
* discussing topics
* requesting explanations
* engaging in tutoring or learning sessions

### Command-Based Interaction

Voice can be used to issue direct commands.

Examples:

* "Turn on the lights"
* "Show me the camera"
* "Start a new project"
* "Take a picture"

### Confirmation and Rejection

Voice allows users to confirm or reject actions proposed by the system.

Examples:

* "Yes"
* "No"
* "Correct"
* "That's wrong"

### Interruption and Cancellation

Users must be able to interrupt the system quickly through speech.

Examples:

* "Stop"
* "Cancel"
* "Wait"
* "That's enough"

### Dictation

The system can capture spoken content intended to be transcribed.

Examples:

* writing messages
* drafting documents
* capturing notes

### Guided Learning and Practice

Voice interaction allows NORA to act as a conversational tutor.

Examples:

* language learning practice
* pronunciation training
* interview simulation
* educational dialogue

---

## Possible Capabilities

Typical capabilities supported through voice interaction include:

* speaking with NORA
* receiving spoken responses
* issuing commands
* confirming or rejecting actions
* interrupting system behaviour
* dictating text
* practicing languages
* conversational tutoring
* roleplay or scenario simulation

These capabilities make voice the **most natural interface for long-form interaction**.

---

## Example User Inputs

The Voice Interface may receive various forms of spoken input.

Examples include:

* wake phrase ("NORA")
* natural questions
* task requests
* confirmations
* rejections
* cancellations
* corrections
* clarifications
* dictated text
* conversational statements

Examples:

* "NORA, what's the weather today?"
* "Turn on the living room lights"
* "Yes"
* "No"
* "Stop"
* "Repeat that"
* "Explain it again"

---

## Example System Outputs

NORA may produce several types of spoken responses through the voice interface.

Examples include:

* answering questions
* confirming actions
* requesting clarification
* providing instructions
* narrating information
* reading text aloud
* guiding learning exercises

Examples:

* "The temperature today is 18 degrees."
* "Do you want me to turn on the lights?"
* "I didn't understand that. Could you repeat it?"
* "Let's practice English pronunciation."

---

## Feedback and Interaction Signals

To support smooth conversation, the system should provide clear feedback signals during voice interaction.

Examples:

* listening indicators
* thinking or processing indicators
* speech playback indicators
* interruption acknowledgement
* timeout warnings

These signals may be expressed through **speech, screen indicators, LEDs, or other visual cues**.

---

## Relationship With Other Modules

### Perception

Perception processes raw audio signals captured by the microphone.

It handles tasks such as:

* audio capture
* wakeword detection
* voice activity detection
* speech-to-text

The Voice Interface then uses the resulting interpreted speech as **human interaction input**.

### Dialogue and Sessions

Spoken interactions are typically integrated into longer conversational sessions managed by the dialogue system.

### Planning and Agents

Spoken requests are interpreted and converted into intentions that the planning system and specialized agents execute.

### Action and Expression

Spoken output is produced through text-to-speech engines defined in the Action and Expression module.

---

## Design Considerations

### Naturalness

The voice interface should prioritize conversational naturalness and fluid turn-taking.

### Responsiveness

Speech interaction requires low latency to maintain the illusion of natural dialogue.

### Interruptibility

Users must always be able to interrupt the system verbally.

### Error Recovery

The system must handle misunderstandings gracefully by asking clarifying questions.

### Multilingual Support

NORA may support multiple languages and switch dynamically depending on the user context.

---

## Summary

The **Voice as an Interface** module enables natural spoken interaction between users and NORA.

It allows users to communicate with the system through conversation, commands, confirmations, and dictation, while receiving spoken feedback and guidance in return.

Although the technical processing of speech belongs to perception and other modules, voice remains the **most direct and human-centered interface** through which users interact with NORA.

# 2.2 Local Screen

## Definition

**Local Screen** refers to the physical display integrated into the NORA robot and used to provide visual feedback, contextual information, and interactive elements to users present near the system.

While voice interaction allows natural spoken communication, the local screen complements this interaction by providing **visual support, structured information, and interactive controls**. It serves as the main visual surface through which NORA can display its state, responses, and interface elements in the physical environment.

The Local Screen therefore acts as a **visual interaction surface directly embedded in the robot**, enabling users to both observe and interact with NORA without requiring external devices.

---

## Architectural Role

Within the architecture of NORA, the Local Screen functions as the **primary on-device visual interface**.

Its purpose is to:

* present information generated by the system
* support spoken interactions with visual context
* expose system status and feedback
* allow optional direct user interaction through graphical elements
* reinforce NORA’s expressive behaviour

Because NORA is designed as an embodied system, the screen becomes an important part of the user experience. It allows the robot to communicate not only through sound but also through visual cues and structured information.

This interface is especially useful in situations where:

* spoken output is insufficient or ambiguous
* detailed information must be presented
* visual confirmation is helpful
* the user prefers non-verbal interaction

---

## Interaction Model

The Local Screen typically participates in interactions in combination with other modalities, especially voice.

A typical interaction pattern may look like this:

1. The user asks a question through voice.
2. NORA processes the request.
3. The spoken response is delivered.
4. Supporting information is shown on the screen.

For example:

User: "Show me the route to the university."

NORA may:

* describe the route verbally
* display the map and directions on the screen

The screen may also be used independently when users interact through touch or when administrators monitor the system locally.

---

## Core Responsibilities

The Local Screen module supports several key visual interaction capabilities.

### Visual Feedback

The screen communicates system feedback visually so users can understand what NORA is doing.

Examples include:

* listening indicators
* processing indicators
* confirmation prompts
* warnings or errors

### Information Display

The screen allows NORA to present structured information that is difficult to communicate verbally.

Examples include:

* text explanations
* images
* charts
* navigation maps
* camera previews

### Interaction UI

When touch interaction is enabled, the screen may provide graphical interface elements.

Examples include:

* menus
* buttons
* selectable options
* configuration panels

### Emotional and Expressive Output

The screen can also display visual representations of NORA’s emotional state or personality.

Examples include:

* facial expressions
* animated avatars
* emotional indicators

### Contextual Interaction Support

The screen may reinforce ongoing tasks by showing context.

Examples include:

* current conversation topic
* selected project
* system status

---

## Possible Capabilities

Typical visual capabilities of the Local Screen include:

* displaying text
* displaying images
* displaying video
* showing camera feed
* presenting menus
* showing notifications
* rendering animations
* displaying system status
* presenting project information
* displaying QR codes
* showing navigation routes

These capabilities help NORA provide **rich multimodal interaction**.

---

## Example Outputs

The Local Screen may display different types of content depending on the interaction context.

Examples include:

* welcome messages
* active listening indicators
* transcribed speech
* task results
* navigation instructions
* camera preview
* alerts and warnings
* system diagnostics

Example visual responses:

* "Listening…"
* "Processing request…"
* "Do you want to start a new project?"
* map visualization
* QR code for sharing information

---

## Feedback and System State Indicators

Visual indicators on the screen may represent internal system states.

Examples include:

* listening
* speaking
* thinking
* waiting for confirmation
* executing an action
* encountering an error

Displaying these states improves transparency and user trust.

---

## Relationship With Other Modules

### Interaction Interfaces

The Local Screen is one of several interaction interfaces available in the system.

### Dialogue and Sessions

The screen may show contextual information related to ongoing conversations or active sessions.

### Action and Expression

Visual outputs displayed on the screen are typically generated by the action and expression subsystem.

### Backend and Frontend Systems

The Local Screen may share components with the frontend architecture or reuse UI elements designed for web interfaces.

---

## Design Considerations

### Readability

Information shown on the screen should be readable from typical interaction distances.

### Minimal Cognitive Load

The screen should support spoken interaction rather than overwhelm the user with unnecessary information.

### Synchronization With Voice

Visual output should remain synchronized with spoken responses to avoid confusion.

### Interaction Safety

Touch-based controls should be designed carefully to prevent accidental activation.

### Expressiveness

Visual design should reinforce NORA’s personality and emotional expression without distracting from the main interaction.

---

## Summary

The **Local Screen** module provides the primary visual interface embedded in the NORA robot.

It complements voice interaction by displaying information, supporting user interaction, and visualizing system state. Through text, images, animations, and graphical UI elements, the Local Screen enables richer and clearer communication between users and the system.

By combining visual and spoken interaction, NORA can deliver a more intuitive and transparent user experience.

# 2.3 Web Frontend

## Definition

**Web Frontend** refers to the browser-based interface that allows users and administrators to interact with, monitor, and control NORA remotely through a standard web browser.

Unlike the Local Screen, which is physically embedded in the robot, the Web Frontend exists outside the robot and can be accessed from computers, tablets, or other network-connected devices.

The Web Frontend provides a **remote visual and operational interface** that exposes system state, conversations, projects, and administrative capabilities. It allows users to observe NORA’s behaviour, interact with the system conversationally, configure settings, and perform management tasks without being physically present near the robot.

---

## Architectural Role

Within the architecture of NORA, the Web Frontend functions as the **primary remote interaction interface**.

It allows humans to:

* access NORA from outside the physical environment
* observe the internal state of the system
* interact with conversations and projects
* monitor system behaviour
* perform configuration and administrative actions

This interface is particularly important for:

* remote usage
* development and debugging
* system administration
* monitoring long-running sessions
* inspecting system behaviour and logs

Because NORA is designed as a persistent intelligent system, the Web Frontend acts as a **control and observability surface** that complements the embodied interfaces of the robot.

---

## Interaction Model

Interaction through the Web Frontend typically follows a client–server model.

1. The user opens the NORA Web Frontend in a browser.
2. The frontend authenticates the user through the identity and access module.
3. The interface communicates with backend services through HTTP APIs and realtime channels.
4. The user interacts with NORA through visual dashboards, chat interfaces, or control panels.
5. Backend services relay commands, events, and updates to the cognitive core and other subsystems.

In addition to standard request-response communication, the Web Frontend may rely on **realtime channels** (such as WebSockets) to receive live updates about system state and events.

---

## Core Responsibilities

The Web Frontend module enables several major capabilities.

### User Interaction

Users can interact with NORA through a browser-based interface.

Examples include:

* sending chat messages
* interacting with projects
* reviewing conversation history
* issuing commands

### System Monitoring

The frontend allows users to observe the internal state of the system.

Examples include:

* current FSM state
* active sessions
* active user
* sensor status
* system health

### Administrative Control

Administrators may use the Web Frontend to perform maintenance or configuration tasks.

Examples include:

* user management
* permission configuration
* system configuration
* restarting modules

### Observability and Debugging

The interface may provide tools for inspecting internal behaviour of the system.

Examples include:

* event streams
* logs
* telemetry
* performance metrics

### Remote Control

The Web Frontend may allow remote triggering of actions or commands.

Examples include:

* starting or stopping sessions
* triggering system actions
* controlling hardware functions

---

## Typical Interface Components

The Web Frontend may include several main views or panels.

### Dashboard

The dashboard provides a summary of the system status.

Possible elements:

* current robot state
* active user
* session overview
* hardware status

### Conversation Interface

A chat-style interface allowing users to communicate with NORA.

Possible elements:

* message history
* system responses
* input field

### Project Management

Users may manage conversational projects or tasks.

Possible elements:

* project list
* project context
* project history

### Administration Panel

Administrative tools for system configuration.

Possible elements:

* user management
* role configuration
* system settings

### System Monitoring

Observability tools showing internal system behaviour.

Possible elements:

* FSM transition history
* event logs
* hardware telemetry

---

## Example Inputs

The Web Frontend may generate several types of input events.

Examples include:

* login request
* chat message
* command request
* configuration change
* project creation
* project selection
* admin command
* hardware control request

These inputs are typically transmitted to backend services through APIs.

---

## Example Outputs

The Web Frontend may display various outputs generated by the system.

Examples include:

* system responses
* session information
* project status
* hardware telemetry
* alerts and notifications
* logs and metrics

---

## Relationship With Other Modules

### Identity, Access and Security

The Web Frontend relies on authentication and authorization mechanisms defined in the identity and access module.

### Backend and Application Layer

The frontend communicates with backend services through APIs and realtime communication channels.

### Core Cognitive System

User commands and interactions received through the frontend ultimately influence the behaviour of the cognitive core and FSM.

### Dialogue and Sessions

Chat-based interaction with NORA through the frontend integrates with the dialogue and session management modules.

### Observability

The frontend visualizes logs, metrics, and state information produced by the observability subsystem.

---

## Design Considerations

### Responsiveness

The interface should remain responsive even when the system performs complex tasks.

### Real-Time Updates

The frontend should support live updates for system state, events, and conversation streams.

### Usability

The interface should present complex system information in a clear and structured manner.

### Security

Administrative capabilities must be restricted to authorized users.

### Remote Accessibility

The Web Frontend should be accessible across multiple devices and network environments.

---

## Summary

The **Web Frontend** module provides a browser-based interface for remote interaction with NORA.

It allows users and administrators to communicate with the system, monitor its behaviour, configure settings, and control operations from outside the physical robot environment.

By providing remote access and observability, the Web Frontend complements the embodied interaction interfaces of NORA and enables effective management and supervision of the system.

# 2.4 Touch / Physical Interaction

## Definition

**Touch / Physical Interaction** refers to direct contact-based interaction between humans and the NORA robot through tactile sensors, buttons, touch surfaces, or body-contact detection.

Unlike voice or visual interfaces, this interaction modality is based on **physical proximity and intentional contact with the robot's body or control elements**. It enables users to communicate with NORA through simple, immediate actions such as pressing a button, touching a sensor, or interacting with a touchscreen.

Because NORA is designed as an embodied system that exists in a physical environment, physical interaction becomes an important channel for intuitive control, safety overrides, and socially expressive interaction.

---

## Architectural Role

Within the architecture of NORA, Touch / Physical Interaction acts as a **direct local control interface**.

It allows users who are physically near the robot to:

* initiate or interrupt interaction
* confirm or cancel system behaviour
* trigger immediate actions
* interact without using voice
* communicate through simple tactile gestures

This interface is particularly important for situations where:

* voice interaction is not appropriate
* the environment is noisy
* immediate control is required
* users prefer simple physical controls

Because of its immediacy and reliability, physical interaction is also a key mechanism for **safety-critical actions**, such as emergency stops.

---

## Interaction Model

Physical interaction generally follows a **direct stimulus–response model**.

1. A user touches or presses a physical interface element.
2. Sensors detect the physical contact.
3. The event is forwarded to the system through the perception layer.
4. The event is interpreted as a user interaction command.
5. The cognitive core decides how the system should respond.

Examples:

* pressing a button to start interaction
* touching a sensor to confirm an action
* pressing an emergency button to interrupt activity

Because physical interaction produces **discrete and unambiguous events**, it can serve as a reliable control mechanism.

---

## Core Responsibilities

The Touch / Physical Interaction module supports several types of interaction.

### Control Input

Users can perform direct control actions through physical inputs.

Examples:

* pressing a start button
* confirming an action
* cancelling an operation

### Social Interaction

Touch may also be used as part of human–robot social interaction.

Examples:

* touching the robot's head
* tapping a hand sensor
* performing a friendly gesture

These interactions can influence NORA's emotional state or behavioural responses.

### Safety Overrides

Physical controls provide immediate ways to interrupt system behaviour.

Examples:

* emergency stop button
* hardware kill switch

These mechanisms ensure that humans can always regain control of the system if necessary.

### Alternative Input Channel

Physical interaction provides an alternative interface when voice or gesture interaction is unavailable or inconvenient.

---

## Possible Interaction Mechanisms

Typical physical interaction mechanisms may include:

* hardware buttons
* capacitive touch sensors
* pressure sensors
* touchscreen input
* contact sensors on the robot body
* emergency stop controls

Examples of touch points on the robot may include:

* head touch sensor
* hand touch sensor
* torso control button

---

## Example Inputs

Examples of physical interaction events include:

* button pressed
* touchscreen tap
* head touch detected
* hand touch detected
* emergency stop activated

Examples:

* pressing a "start interaction" button
* touching the robot's head to attract attention
* pressing an emergency stop during movement

---

## Example Outputs

Physical interaction may trigger system responses such as:

* starting interaction
* confirming an action
* cancelling an operation
* interrupting system behaviour
* triggering a safety shutdown

The system may also provide feedback through other channels such as:

* spoken responses
* screen messages
* LED indicators

---

## Relationship With Other Modules

### Perception

Physical sensors detect contact events and forward them to the system.

### Core Cognitive System

Touch events are interpreted as interaction commands and processed by the FSM and planning modules.

### Action and Expression

The system may respond to physical interaction through speech, movement, visual feedback, or emotional expression.

### Identity and Security

Certain physical controls may require authorization depending on system configuration.

---

## Design Considerations

### Reliability

Physical controls must operate reliably and consistently.

### Accessibility

Controls should be easy to reach and clearly identifiable.

### Safety

Emergency controls must always be available and responsive.

### Intentionality

The system should minimize accidental activation caused by unintended contact.

### Feedback

Users should receive immediate feedback after interacting physically with the robot.

---

## Summary

The **Touch / Physical Interaction** module enables direct tactile interaction between humans and the NORA robot.

Through buttons, sensors, and touch surfaces, users can control the system, interrupt behaviour, and engage in embodied interaction without relying on voice or remote interfaces.

By providing reliable and immediate input mechanisms, this module plays an important role in usability, accessibility, and operational safety.

# 2.5 NFC / RFID

## Definition

**NFC / RFID Interaction** refers to proximity-based interaction between users and the NORA system through Near Field Communication (NFC) or Radio Frequency Identification (RFID) tags, cards, or wearable devices.

This interaction modality allows users to identify themselves, activate the system, trigger predefined behaviours, or switch operational contexts simply by bringing a compatible device close to an NFC or RFID reader integrated into NORA.

Unlike voice, screen, or touch interfaces, NFC/RFID interaction does not rely on speech, visual interfaces, or explicit manual input. Instead, it operates through **short-range wireless identification**, making it a fast and frictionless interaction mechanism.

Within the architecture of NORA, NFC/RFID acts as a **proximity-based interaction channel** that bridges the domains of interaction, identity, and system context.

---

## Architectural Role

The NFC/RFID interface provides a **fast identification and activation mechanism** for users physically present near the robot.

Through this interface, NORA can:

* identify a user
* load a user profile
* activate or unlock the system
* switch operational modes
* trigger predefined actions

Because the interaction requires physical proximity, NFC/RFID provides a useful balance between convenience and contextual awareness. It allows the system to recognize users without requiring them to speak, log in, or navigate menus.

This makes NFC/RFID particularly useful in environments where:

* multiple users interact with the same robot
* quick identification is required
* interaction must remain simple and intuitive

---

## Interaction Model

The NFC/RFID interaction model is based on **proximity detection**.

1. A user presents a tag, card, or wearable device near the NFC/RFID reader.
2. The reader detects the device and retrieves its identifier.
3. The identifier is transmitted to the system.
4. The identity or action associated with the tag is resolved.
5. NORA performs the corresponding behaviour.

This interaction is typically **instantaneous** and requires minimal user effort.

Examples:

* a user taps a personal NFC card to identify themselves
* an administrator scans a tag to unlock advanced controls
* a guest card activates a temporary interaction mode

---

## Core Responsibilities

The NFC/RFID interface supports several major functions.

### User Identification

Tags may be associated with specific users.

When a tag is scanned, the system can:

* identify the user
* load user preferences
* activate a personalized interaction context

### Profile Switching

NORA may switch behavioural parameters depending on the identified user.

Examples include:

* language preferences
* voice settings
* access permissions

### System Activation

NFC tags may be used to activate or unlock the robot.

Examples:

* waking the system
* enabling interaction

### Access Control

Certain tags may grant or restrict access to system capabilities.

Examples:

* administrator access
* restricted operational modes

### Triggered Actions

Specific tags may correspond to predefined commands.

Examples:

* starting a learning session
* opening a project
* activating a specific application

---

## Possible Interaction Mechanisms

Typical NFC/RFID mechanisms include:

* NFC cards
* RFID badges
* NFC stickers
* wearable NFC devices
* smartphone NFC interactions

Possible placement of readers on NORA may include:

* torso panel
* front interface area
* base station

---

## Example Inputs

Examples of NFC/RFID interaction events include:

* known user tag detected
* unknown tag detected
* administrator tag scanned
* guest tag scanned

Example actions:

* loading a user profile
* unlocking system functions
* activating a learning mode

---

## Example Outputs

System responses may include:

* user profile loaded
* session started
* system unlocked
* access denied
* confirmation message

Feedback may be delivered through:

* voice
* screen
* LED indicators

---

## Relationship With Other Modules

### Identity, Access and Security

NFC/RFID identifiers may be mapped to user identities managed by the identity and access module.

### Core Cognitive System

The system determines how the scanned tag affects system behaviour or operational state.

### Dialogue and Sessions

Scanning a tag may start or resume a conversational session associated with a user.

### Action and Expression

The robot may respond to tag detection through speech, visual indicators, or other feedback mechanisms.

---

## Design Considerations

### Security

Tag identifiers should not grant unrestricted access without validation.

### Reliability

The reader must detect tags consistently and quickly.

### Privacy

User identity information should be handled securely.

### Simplicity

Interaction through NFC/RFID should remain simple and intuitive.

### Context Awareness

The system should consider the current operational state when responding to tag scans.

---

## Summary

The **NFC/RFID** module enables proximity-based interaction between users and the NORA robot.

Through tags, cards, or wearable devices, users can quickly identify themselves, activate system functions, switch contexts, or trigger predefined actions.

By combining convenience with contextual awareness, NFC/RFID provides a fast and intuitive way to interact with NORA in multi-user environments.

# 2.6 Gestures as an Interface

## Definition

**Gestures as an Interface** refers to the use of human body movements—such as hand gestures, arm movements, posture cues, or simple physical signals—as intentional commands directed at NORA.

In this interaction modality, the user communicates with the system through **non‑verbal physical movements** that are interpreted as interaction commands.

Unlike voice interaction, gestures allow users to communicate with NORA **silently and at a distance**, which can be useful in environments where speech is inconvenient, undesirable, or impossible.

Within the architecture of NORA, gestures are treated as an **intentional human interface modality**, distinct from the perception systems that technically detect those gestures.

---

## Distinction from Vision Perception

It is important to distinguish between two architectural roles:

**Gesture detection (Perception layer)**

* camera capture
* pose estimation
* hand tracking
* gesture classification

These belong to the **Perception → Vision module**.

**Gesture interaction (Interaction Interfaces layer)**

* interpreting a gesture as a command
* triggering interaction events
* affecting system behaviour

These belong to the **Interaction Interfaces module**.

This separation ensures that perception algorithms remain independent from interaction semantics.

---

## Architectural Role

Gestures provide an additional interaction channel that complements voice, touch, and screen interfaces.

The main advantages of gesture interaction include:

* silent communication
* distance-based control
* natural human–robot interaction
* accessibility for certain users

In the architecture of NORA, gesture interaction enables users to:

* attract the robot's attention
* interrupt actions
* confirm or reject system proposals
* request interaction without speaking

Because gestures can be perceived visually at a distance, they allow NORA to react to **human body language in shared environments**.

---

## Interaction Model

Gesture-based interaction typically follows this sequence:

1. The user performs a gesture within the robot's field of view.
2. The vision perception module detects and classifies the gesture.
3. The classified gesture is converted into an interaction event.
4. The event is processed by the cognitive core (FSM, planning, etc.).
5. NORA responds through voice, movement, screen output, or other feedback.

This process allows gestures to function as **implicit commands directed at the system**.

---

## Core Responsibilities

The Gesture Interface module supports several types of interaction.

### Attention Request

Users may use gestures to attract the robot's attention.

Examples:

* waving a hand
* raising a hand

### Command Input

Gestures may represent direct commands.

Examples:

* stop gesture
* pointing gesture
* calling gesture

### Confirmation

Gestures may be used to confirm system requests.

Examples:

* thumbs up
* nod-like hand gesture

### Cancellation

Gestures may cancel ongoing actions.

Examples:

* "stop" hand signal
* dismissive motion

### Non-verbal Interaction

Gestures allow interaction without spoken language.

This can be useful in:

* noisy environments
* silent spaces
* accessibility contexts

---

## Possible Gesture Commands

Example gesture commands that NORA may support include:

* greeting gesture
* stop gesture
* confirm gesture
* cancel gesture
* call gesture
* pointing gesture
* silence gesture

Each gesture may correspond to a **normalized interaction event** that can be processed by the system.

---

## Example Inputs

Example gesture interaction events include:

* greeting gesture detected
* stop gesture detected
* pointing gesture detected
* confirm gesture detected

These events are generated after gesture recognition in the perception layer.

---

## Example Outputs

Possible system responses to gesture interaction include:

* acknowledging the user
* stopping an action
* confirming a command
* focusing attention on the user

Feedback may be provided through:

* spoken response
* head movement
* screen output
* LED signals

---

## Relationship With Other Modules

### Vision Perception

Gesture recognition is implemented in the vision perception subsystem.

### Core Cognitive System

Gesture commands are processed as interaction events by the FSM and planning modules.

### Action and Expression

NORA may respond to gestures with movements, speech, or visual indicators.

### Dialogue and Sessions

Gesture commands may start or influence conversational interactions.

---

## Design Considerations

### Recognition Accuracy

Gesture detection must be reliable enough to avoid accidental commands.

### Ambiguity

Some gestures may be ambiguous and require confirmation.

### Visibility

Gestures must occur within the robot's visual field.

### Cultural Variation

Gestures may have different meanings across cultures.

### Safety

Critical commands triggered by gestures may require confirmation.

---

## Summary

The **Gestures as an Interface** module enables non-verbal interaction between users and NORA through body movements interpreted as commands.

By complementing voice, touch, and visual interfaces, gesture interaction expands the ways in which humans can communicate with the system, making NORA more natural and adaptable in real-world environments.

# 2.7 Remote Interfaces

## Definition

**Remote Interfaces** refer to interaction channels that allow users or external systems to communicate with, observe, or control NORA from devices that are not physically integrated into the robot.

Unlike the Local Screen or Touch Interaction modules, which require physical proximity to the robot, remote interfaces allow interaction through **network-connected devices** such as computers, tablets, mobile phones, wearable devices, or other external systems.

This interaction modality extends NORA beyond its physical embodiment and enables the robot to operate as part of a broader digital ecosystem.

Within the architecture, Remote Interfaces represent **external entry points into the system**, enabling distributed interaction and remote supervision.

---

## Architectural Role

The Remote Interfaces module enables NORA to be accessed and controlled from outside its immediate physical environment.

Through remote interfaces, users can:

* communicate with NORA from another location
* observe the robot's current state
* trigger commands
* receive notifications
* monitor ongoing tasks

This capability is essential for several scenarios:

* remote supervision of the system
* interaction through personal devices
* integration with external services
* administration and debugging

Remote interfaces transform NORA from an isolated robotic system into a **connected intelligent platform**.

---

## Interaction Model

Remote interaction typically follows a network-based communication model.

1. A remote device or system sends a request or command.
2. The request is transmitted through a network interface.
3. Backend services receive and process the request.
4. The system generates events or commands internally.
5. Responses or state updates are sent back to the remote interface.

Depending on the use case, communication may occur through:

* HTTP APIs
* realtime channels (WebSockets)
* messaging systems

This architecture allows both **request-response interaction** and **event-driven communication**.

---

## Core Responsibilities

The Remote Interfaces module enables several types of interaction.

### Remote User Interaction

Users may interact with NORA through devices that are not physically connected to the robot.

Examples include:

* mobile phone interaction
* tablet interaction
* laptop interaction

### Remote Monitoring

External devices may observe the internal state of the system.

Examples include:

* system state
* active sessions
* hardware status

### Remote Command Execution

Remote users may trigger system actions.

Examples include:

* starting a session
* issuing commands
* controlling hardware functions

### System Notifications

NORA may send notifications or alerts to remote devices.

Examples include:

* reminders
* warnings
* system status updates

### Integration with External Systems

External services may interact with NORA through defined interfaces.

Examples include:

* smart home systems
* scheduling services
* messaging platforms

---

## Possible Remote Interfaces

Typical remote interaction devices may include:

* mobile applications
* smartwatches
* tablets
* remote web browsers
* administrative terminals
* external APIs

These interfaces may provide different levels of functionality depending on user roles and permissions.

---

## Example Inputs

Examples of remote interaction events include:

* command received from mobile device
* request received from web client
* admin instruction received
* API request from external service

Examples:

* remote command to start interaction
* request for system status
* remote configuration update

---

## Example Outputs

NORA may produce several outputs directed toward remote devices.

Examples include:

* system notifications
* task completion alerts
* conversation responses
* status updates

These outputs allow users to stay informed about system activity even when they are not physically present near the robot.

---

## Relationship With Other Modules

### Backend and Application Layer

Remote interfaces communicate with backend services through APIs and realtime communication channels.

### Identity and Access Control

Remote access must respect authentication and authorization policies defined in the identity module.

### Core Cognitive System

Commands received through remote interfaces may influence the behaviour of the cognitive core.

### Dialogue and Sessions

Remote users may initiate or participate in conversational sessions with the system.

### Action and Expression

Commands triggered remotely may result in actions performed by the robot or responses returned through remote channels.

---

## Design Considerations

### Security

Remote interfaces must enforce strong authentication and authorization controls.

### Network Reliability

The system should handle network delays or disconnections gracefully.

### Synchronization

State changes must remain synchronized across local and remote interfaces.

### Latency

Remote interaction should remain responsive enough for practical use.

### Device Diversity

Interfaces should support multiple device types and screen sizes.

---

## Summary

The **Remote Interfaces** module enables NORA to interact with users and external systems beyond its physical embodiment.

Through network-connected devices and services, remote interfaces allow users to communicate with, monitor, and control the robot from anywhere.

This capability transforms NORA into a connected intelligent system that can operate within a broader technological ecosystem.
