# 4. Cognitive Core

## Definition

The Cognitive Core is the central logical and operational subsystem of NORA. It is responsible for transforming perception outputs, interaction events, internal conditions, and contextual information into coherent system behaviour.

If Interaction Interfaces define how humans communicate with NORA, and Perception defines how the system senses the world, the Cognitive Core defines how the system internally understands its current situation and how it should behave in response.

This module acts as the internal control center of the architecture. It organizes the system’s active state, operational context, internal behavioural condition, and short‑term control memory. Through this module, NORA maintains continuity across events, regulates behaviour, decides whether transitions should occur, and preserves internal coherence across multimodal and asynchronous interactions.

The Cognitive Core therefore allows NORA to behave as a unified system rather than as a set of independent modules.

## Architectural Purpose

The purpose of the Cognitive Core is to provide a stable and explicit internal model of system operation.

NORA is a multimodal embodied cognitive system capable of perceiving its environment, interacting with users, maintaining persistent sessions, executing actions, reacting to asynchronous events, and coordinating multiple subsystems simultaneously.

Because of this complexity, behaviour cannot depend only on the most recent input. It must also depend on contextual factors such as the current operational state, the active user, the interaction mode, recent transitions, internal restrictions, and subsystem availability.

The Cognitive Core centralizes this logic so that all other modules operate on top of a consistent behavioural foundation.

## Architectural Role

Within the overall architecture, the Cognitive Core sits between incoming system events and higher‑level decision or execution layers.

Conceptually the information flow can be described as:

Interfaces / Perception / External Events → Cognitive Core → Dialogue / Planning / Action

In this role, the Cognitive Core does not perform sensing or direct actuation. Instead, it provides the internal behavioural layer that interprets events, manages operational state, and determines the conditions under which other modules operate.

## Responsibilities

The Cognitive Core performs several key responsibilities.

### Operational State Management

The module maintains the current operational state of NORA. This state describes what the system is currently doing and what behaviours are possible at that moment.

Examples of operational modes include being idle, listening to the user, interpreting input, planning a response, waiting for confirmation, executing an action, speaking, or recovering from an error.

### Event Interpretation

Incoming events from perception, interfaces, or backend services do not automatically determine behaviour. The Cognitive Core interprets those events relative to the current state and context.

For example, a spoken command may start a new interaction when the system is idle, but it may be interpreted as follow‑up input when an interaction is already active.

### Context Maintenance

The Cognitive Core stores the dynamic context required for coherent operation. This context includes information such as the active user, the source of activation, the current interaction mode, the latest event, the latest interpreted intent, and subsystem availability.

This shared context allows different parts of the system to coordinate behaviour consistently.

### Behaviour Regulation

The module regulates behaviour through conditions and constraints. It may block actions, require confirmation, prioritize interruptions, or suspend certain behaviours depending on the operational situation.

### Continuity Across Events

The Cognitive Core maintains short‑term continuity so that the system remembers what has recently occurred. This allows NORA to continue interactions smoothly, recover from interruptions, and maintain internal consistency across event sequences.

### Internal Behavioural State

The module can maintain an internal behavioural or emotional state that modulates how the system reacts to events. This internal condition influences decision‑making and later expression through voice, visual feedback, or motion.

### Traceability

By centralizing operational state and transitions, the Cognitive Core makes system behaviour easier to inspect, debug, and audit.

## Scope

The Cognitive Core includes mechanisms responsible for modelling and regulating NORA’s internal operational behaviour.

Its scope includes:

* operational state modelling
* event‑driven transitions
* dynamic operational context
* behavioural modulation
* short‑term control memory

Its scope does not include:

* raw sensory processing
* user interface rendering
* long‑term conversational memory
* domain‑specific reasoning or planning
* low‑level actuator control

These responsibilities belong to other modules in the architecture.

## Internal Structure

To maintain clarity and separation of concerns, the Cognitive Core is divided into several submodules:

4.1 FSM
The finite state machine that models the operational behaviour of the system.

4.2 Operational Context
The live contextual information required for system operation.

4.3 Emotional State
The internal behavioural state that modulates reactions and expression.

4.4 Internal Cognitive Memory
Short‑term internal memory used for maintaining operational continuity.

Together these components define the internal control layer that allows NORA to behave coherently across multimodal interaction, perception events, and system actions.

# 4.1 Finite State Machine (FSM)

## Definition

The **Finite State Machine (FSM)** is the formal mechanism used by the Cognitive Core to model and control the operational behaviour of NORA.

A finite state machine represents the system as a set of **explicit states** and **transitions** triggered by **events** under specific **conditions**. At any given moment, the system exists in exactly one operational state. Incoming events are evaluated relative to that state, and if a valid transition exists, the system moves to a new state.

Within NORA, the FSM is the primary structure that ensures the robot behaves in a coherent, deterministic, and traceable way across multimodal interactions, asynchronous events, and internal system conditions.

Without an FSM, behaviour would emerge from distributed conditionals across perception modules, dialogue systems, planners, and action components. This would quickly lead to inconsistent behaviour, race conditions, and difficult debugging. The FSM centralizes behavioural control and provides a single authoritative model of system operation.

---

## Purpose of the FSM in NORA

The FSM serves several architectural purposes:

1. **Operational coherence** – ensuring the system behaves consistently even when many modules generate events simultaneously.
2. **Explicit behavioural modelling** – representing system behaviour as a well-defined state graph.
3. **Controlled transitions** – preventing invalid operations in inappropriate states.
4. **Event prioritization** – determining how incoming events should be handled.
5. **Traceability** – enabling logging and inspection of behavioural transitions.
6. **Recoverability** – providing structured paths for error handling and recovery.

Through the FSM, NORA can safely coordinate perception, dialogue, planning, and action without unpredictable interactions between subsystems.

---

## Fundamental Concepts

### States

A **state** represents the current operational condition of the system. It defines what the system is doing and which behaviours are allowed.

Examples of possible states include:

* OFF
* INITIALIZING
* INACTIVE
* OBSERVING
* LISTENING
* INTERPRETING
* PLANNING
* WAITING_FOR_CONFIRMATION
* EXECUTING_ACTION
* SPEAKING
* FINALIZING_INTERACTION
* SUSPENDED
* ERROR
* RECOVERING

Each state determines:

* which events are meaningful
* which transitions are valid
* which modules may operate
* which actions are blocked

States therefore provide the behavioural frame in which events are interpreted.

---

### Events

An **event** represents something that happened in the system or environment.

Events may originate from multiple sources:

**Perception events**

* wake word detected
* speech recognized
* gesture detected
* person detected

**Interface events**

* touchscreen input
* button press
* web command

**System events**

* action completed
* planner result available
* timeout
* error detected

**External events**

* webhook received
* IoT update
* scheduled trigger

Events do not directly trigger behaviour. Instead, they are evaluated by the FSM relative to the current state.

---

### Transitions

A **transition** defines how the system moves from one state to another when a valid event occurs.

A transition typically includes:

* origin state
* triggering event
* optional conditions (guards)
* destination state
* side effects or actions

Example:

```
State: INACTIVE
Event: EVT_WAKEWORD
Condition: microphone operational
Transition → LISTENING
```

Transitions are the primary mechanism through which the system evolves during operation.

---

### Guards (Conditions)

A **guard** is a condition that must be satisfied for a transition to occur.

Guards allow the FSM to incorporate context when deciding whether a transition is valid.

Examples:

* user authenticated
* microphone available
* system not in error state
* planner result valid
* safety conditions satisfied

If the guard condition is not satisfied, the transition is rejected.

---

### Actions

Transitions may trigger **actions**. These actions are not necessarily physical outputs; they may include internal operations such as:

* updating context
* starting speech recognition
* invoking the planner
* triggering dialogue generation
* notifying the frontend
* logging transitions

Actions allow the FSM to coordinate behaviour across modules.

---

### Event Queue

Incoming events are typically placed into an **event queue**. The FSM processes events sequentially, ensuring that behaviour remains deterministic even when events arrive concurrently.

This queue may include priority rules so that certain events (for example stop commands or safety alerts) are processed before less critical events.

---

### Dispatcher

The **dispatcher** is the component responsible for feeding events into the FSM.

It acts as the standardized entry point for operational events coming from perception, interfaces, backend services, and internal modules.

By centralizing event injection, the dispatcher ensures that all behavioural changes pass through the same control mechanism.

---

## FSM Behaviour Flow

A simplified processing cycle typically follows this sequence:

1. An event is generated by perception, interface, backend, or internal module.
2. The event is sent to the event dispatcher.
3. The dispatcher places the event into the FSM event queue.
4. The FSM evaluates the event relative to the current state.
5. If a valid transition exists and guard conditions are satisfied, the FSM moves to the destination state.
6. Associated actions are triggered.
7. The transition is recorded in the transition history.

This cycle repeats continuously during system operation.

---

## FSM State Categories

Although the exact states may evolve, they can be grouped conceptually into several categories.

### System Lifecycle States

These states describe the lifecycle of the robot.

Examples:

* OFF
* INITIALIZING
* SHUTTING_DOWN

### Idle and Monitoring States

States where the system is active but not currently engaged in interaction.

Examples:

* INACTIVE
* OBSERVING

### Interaction States

States involved in interacting with a user.

Examples:

* LISTENING
* INTERPRETING
* SPEAKING

### Decision States

States involved in reasoning and planning.

Examples:

* PLANNING
* WAITING_FOR_CONFIRMATION

### Execution States

States where actions are being carried out.

Examples:

* EXECUTING_ACTION

### Recovery and Safety States

States entered when errors or safety conditions occur.

Examples:

* ERROR
* RECOVERING
* SUSPENDED

These categories help structure the overall behavioural graph.

---

## Transition History

Every transition executed by the FSM should be recorded in a **transition history log**.

This log may include:

* timestamp
* previous state
* triggering event
* new state
* guard conditions evaluated
* actions triggered

Maintaining this history enables debugging, system observability, and behavioural analysis.

---

## Relationship with Other Modules

### With Perception

Perception modules generate events such as wake words, gestures, or visual detections. These events are passed to the FSM via the dispatcher.

### With Dialogue and Sessions

Dialogue modules may be triggered when the FSM enters states such as INTERPRETING or SPEAKING.

### With Planning and Agents

The planner may be invoked when the FSM transitions into planning-related states.

### With Action and Expression

Physical or digital outputs are usually triggered when the FSM enters execution or speaking states.

---

## Design Principles

The FSM implementation should follow several key principles:

* **Determinism:** identical states and events should lead to identical transitions.
* **Clarity:** state definitions and transitions must be understandable.
* **Traceability:** all transitions should be logged.
* **Safety:** dangerous transitions must be prevented through guards.
* **Extensibility:** new states and transitions should be easy to add.

---

## Role Within the Cognitive Core

Within the Cognitive Core, the FSM acts as the **formal behavioural engine** of the system.

Other submodules such as operational context, emotional state, and internal cognitive memory provide supporting information that influences transitions and behaviour. The FSM uses this information when evaluating events and guard conditions.

Together, these components allow NORA to maintain a stable and coherent behavioural flow across perception events, user interactions, planning operations, and system actions.

# 4.2 Operational Context

## Definition

The **Operational Context** is the dynamic information layer of the Cognitive Core that represents the current situation of the system at runtime.

While the Finite State Machine (FSM) defines the structural behaviour of the system through states and transitions, the Operational Context provides the **live information required to interpret events correctly and make context-aware decisions**.

In other words:

* The FSM answers the question **"what state is the system in?"**
* The Operational Context answers **"what is happening around that state right now?"**

This module stores the transient, continuously updated information that describes the active environment, the current user, the source of activation, subsystem availability, and other situational factors that influence system behaviour.

The Operational Context is therefore a critical element of the Cognitive Core because it allows NORA to interpret the same event differently depending on the surrounding conditions.

---

## Architectural Purpose

The purpose of the Operational Context is to provide a **shared, real-time representation of the system's current operating conditions**.

NORA receives events from multiple sources:

* perception systems
* interaction interfaces
* backend services
* external integrations
* hardware sensors
* action modules

These events cannot be interpreted in isolation. Their meaning depends on contextual factors such as:

* whether a user is currently present
* which user is active
* whether an interaction session is ongoing
* which subsystem triggered the latest event
* whether the system is currently executing an action
* whether certain actions are temporarily inhibited
* whether hardware modules are available

The Operational Context consolidates these variables into a unified structure that can be accessed by the FSM and other components of the Cognitive Core.

This allows behaviour to remain consistent and context-sensitive even when events arrive asynchronously.

---

## Role Within the Cognitive Core

Within the Cognitive Core, the Operational Context acts as the **live situational memory of the system**.

The FSM relies on this context when evaluating guard conditions and determining whether transitions are valid.

For example, a transition triggered by a speech recognition event may depend on contextual information such as:

* whether a user is currently identified
* whether a listening interaction is active
* whether the system is already executing an action
* whether the microphone subsystem is functioning correctly

Without access to this contextual information, the FSM would not be able to make informed decisions.

The Operational Context therefore provides the data required for the FSM to interpret events in a meaningful way.

---

## Characteristics of Operational Context

Operational Context differs from other forms of memory in the architecture.

### 1. Dynamic

The context is continuously updated as events occur and system conditions change.

### 2. Short-Lived

Most contextual variables represent transient runtime conditions rather than long-term stored knowledge.

### 3. Shared Across Modules

Multiple components of the Cognitive Core may read or update contextual information.

### 4. Behaviourally Relevant

Every variable in the context should exist because it influences system behaviour or decision-making.

### 5. Non-Persistent by Default

Operational Context typically exists in memory and is reset when the system restarts, although certain elements may be reconstructed from persistent data if needed.

---

## Types of Contextual Information

The Operational Context may include several categories of information.

### User Context

Information about the currently relevant user.

Possible fields:

* active_user_id
* authenticated_user
* user_presence_detected
* user_profile_loaded

This information allows the system to adapt behaviour depending on who is interacting with it.

---

### Interaction Context

Information about the current interaction flow.

Possible fields:

* interaction_active
* interaction_mode
* interaction_source
* conversation_active
* session_id

This helps determine whether incoming inputs belong to an ongoing interaction or should start a new one.

---

### Activation Context

Information describing what triggered the current interaction.

Examples:

* wakeword
* gesture
* button
* NFC tag
* remote command

Knowing the activation source helps the system choose appropriate response strategies.

---

### System Context

Information about system-level conditions.

Possible fields:

* microphone_available
* camera_available
* network_available
* sensors_operational
* hardware_errors

This allows the system to avoid behaviours that depend on unavailable components.

---

### Action Context

Information about currently running or pending actions.

Possible fields:

* action_in_progress
* current_action_type
* action_source
* awaiting_confirmation

This prevents conflicting actions and supports interruption logic.

---

### Event Context

Information about the most recent events processed by the system.

Possible fields:

* last_event
* last_event_timestamp
* last_event_source

This allows the system to maintain behavioural continuity between events.

---

### Safety Context

Information related to safety and system protection.

Possible fields:

* emergency_stop
* safety_lock
* restricted_actions

This context ensures that potentially unsafe behaviours are prevented.

---

## Updating the Operational Context

The context is updated continuously as the system processes events.

Typical update triggers include:

* perception detections
* interface inputs
* authentication results
* hardware status updates
* action execution results
* planner outputs

Each update modifies specific contextual variables while leaving unrelated variables unchanged.

Maintaining consistent update rules is important to avoid conflicting or outdated contextual information.

---

## Access Patterns

Different components may interact with the Operational Context in different ways.

### Read Access

The FSM frequently reads contextual variables when evaluating transition guards.

Other modules may read context to adjust behaviour, such as dialogue generation adapting to the current interaction mode.

### Write Access

Certain modules may update contextual variables when events occur.

Examples include:

* perception modules updating presence information
* authentication modules updating active user identity
* action modules updating execution status

To maintain consistency, updates should follow well-defined rules and preferably pass through controlled interfaces.

---

## Relationship With Other Modules

### FSM

The FSM reads context variables to evaluate guard conditions and determine valid transitions.

### Dialogue and Sessions

Dialogue modules may rely on context variables such as active session or interaction mode.

### Planning and Agents

Planning modules may use context information such as current user or pending actions.

### Action and Expression

Execution modules may update context to indicate that an action has started or finished.

### Identity and Security

Authentication modules update user-related contextual variables.

---

## Design Principles

The Operational Context should follow several design principles.

### Simplicity

The context should contain only variables that are behaviourally relevant.

### Consistency

Context variables should always represent the true current state of the system.

### Controlled Updates

Changes to the context should occur through well-defined mechanisms rather than arbitrary writes.

### Transparency

Important contextual variables should be inspectable for debugging and observability.

### Minimal Coupling

Modules should depend only on the contextual information they truly require.

---

## Relationship With Other Memory Systems

The Operational Context must not be confused with other forms of memory within the architecture.

* **Operational Context** represents the current runtime situation.
* **Internal Cognitive Memory** stores recent internal control history.
* **Dialogue Memory** stores conversation history.
* **Persistent Memory** stores long-term knowledge and user data.

Each serves a different role and should remain architecturally distinct.

---

## Summary

The Operational Context is the live situational layer of the Cognitive Core.

It provides the real-time information required to interpret events correctly, evaluate transitions in the FSM, and coordinate behaviour across modules.

Without this module, NORA would not be able to adapt behaviour to the surrounding conditions or maintain consistent operation in complex, multimodal environments.

The Operational Context therefore acts as the **dynamic situational awareness layer** that supports the decision-making logic of the Cognitive Core.

# 4.3 Emotional State

## Definition

The **Emotional State** module represents the internal affective-operational condition of NORA. It is a component of the Cognitive Core responsible for modulating how the system behaves, reacts, prioritizes events, and expresses responses during interactions.

Unlike the Finite State Machine (FSM), which models the structural operational state of the system, and the Operational Context, which stores situational runtime information, the Emotional State represents an **internal behavioural modulation layer**. Its purpose is not to simulate human emotions in a psychological sense, but to provide a structured internal variable that influences how the system processes events and expresses behaviour.

In practical terms, the Emotional State helps determine the **tone, urgency, attention level, and behavioural posture** of the system at a given moment.

---

## Architectural Purpose

The purpose of the Emotional State module is to introduce a **behavioural modulation mechanism** that allows NORA to adapt its reactions dynamically depending on internal and external conditions.

Without such a mechanism, all responses produced by the system would be uniform and purely functional. However, embodied systems interacting with humans benefit from behavioural variation that reflects internal conditions such as focus, uncertainty, alertness, or recovery.

By maintaining an internal emotional-operational state, NORA can adjust aspects such as:

* response pacing
* verbosity of explanations
* confirmation strategies
* interaction persistence
* tolerance to interruptions
* prioritization of events
* expressive feedback through voice, screen, LEDs, or motion

This module therefore contributes to making the system more adaptive, understandable, and natural during interaction.

---

## Role Within the Cognitive Core

Within the Cognitive Core architecture, the Emotional State operates as a **behavioural modifier**.

While the FSM determines *what the system is doing* and the Operational Context describes *what is happening around it*, the Emotional State influences *how the system behaves while doing it*.

For example:

* In a **neutral state**, responses may be short and direct.
* In a **focused state**, the system may ignore low-priority interruptions.
* In an **uncertain state**, the system may request clarification before acting.
* In an **alert state**, the system may prioritize safety or anomaly detection.

The Emotional State therefore acts as a modulation layer that influences decisions without replacing the structural logic of the FSM.

---

## Nature of Emotional State

The Emotional State should be understood as an **operational abstraction**, not as a literal simulation of human emotional processes.

Its primary functions are:

* influencing behavioural style
* prioritizing or deprioritizing events
* regulating persistence during interaction
* modulating expressive outputs
* supporting human-robot interaction clarity

This abstraction allows the system to maintain consistent behaviour patterns while remaining interpretable by developers and understandable to users.

---

## Possible Emotional States

The set of emotional states may evolve as the system grows, but typical states may include:

### Neutral

Default state when the system is operating normally without any special conditions.

### Attentive

Indicates that the system has detected user presence or activation and is ready to engage.

### Focused

Represents a state where the system is concentrating on executing a task or interpreting input.

### Curious

May be used when the system detects something novel or ambiguous and needs additional information.

### Uncertain

Represents a state where interpretation confidence is low and clarification is required.

### Alert

Indicates that an anomaly or potential safety condition has been detected.

### Waiting

Represents a temporary waiting period for confirmation, input, or completion of an external process.

### Frustrated

May occur after repeated failed attempts to interpret input or execute an action.

### Satisfied

Represents successful completion of a task or interaction.

### Recovering

Indicates that the system is attempting to restore stable operation after an error.

---

## Behavioural Effects

The Emotional State can influence several aspects of behaviour.

### Response Style

Different emotional states may influence how verbose, explanatory, or concise responses are.

### Interaction Persistence

Some states may encourage the system to continue interaction, while others may cause it to withdraw or ask for clarification.

### Event Prioritization

Certain emotional states may increase the priority of specific events.

For example:

* an alert state may prioritize safety events
* a focused state may deprioritize non-essential inputs

### Expression Modulation

Although the Emotional State is internal, it may influence how the system expresses itself through:

* voice tone
* speech pacing
* facial or visual expressions
* LED colors
* motion patterns

---

## Updating Emotional State

The Emotional State may be updated in response to several types of stimuli:

* perception events
* interaction outcomes
* planning results
* repeated errors
* success or completion of tasks
* safety signals

Transitions between emotional states should be controlled and should avoid excessive oscillation. In practice, smoothing mechanisms or cooldown periods may be used.

---

## Relationship With Other Modules

### FSM

The FSM may trigger emotional state changes when entering specific states such as error, recovery, or execution.

### Operational Context

Contextual variables may influence emotional state updates. For example, repeated recognition failures may trigger an uncertain or frustrated state.

### Action and Expression

External expression modules may read the emotional state to determine how behaviour should be displayed.

### Dialogue and Interaction

Dialogue systems may adapt tone or strategy depending on the current emotional state.

---

## Design Principles

The Emotional State module should follow several design principles.

### Interpretability

Each emotional state should have a clear behavioural meaning.

### Stability

State transitions should avoid rapid oscillations between emotional conditions.

### Behavioural Relevance

Every emotional state should exist because it affects behaviour in a meaningful way.

### Separation From Expression

The internal emotional state should remain separate from its external representation.

---

## Relationship With Expression Systems

It is important to distinguish between **internal emotional state** and **external emotional expression**.

* Emotional State belongs to the Cognitive Core.
* Emotional Expression belongs to Action and Expression modules.

For example, an internal "alert" state may lead to:

* red LED lighting
* urgent speech tone
* warning messages

However, the Cognitive Core does not directly control those outputs; it only exposes the internal state that other modules may interpret.

---

## Summary

The Emotional State module provides a behavioural modulation layer within the Cognitive Core. It influences how the system reacts to events, prioritizes tasks, and expresses behaviour during interaction.

By maintaining an interpretable internal affective-operational condition, NORA can adapt its interaction style, improve human-robot communication, and maintain more natural behavioural dynamics during operation.

# 4.4 Internal Cognitive Memory

## Definition

The **Internal Cognitive Memory** is the short-term internal memory layer of the Cognitive Core. It stores recent operational information that allows NORA to maintain behavioural continuity across events, state transitions, and system actions.

Unlike long-term memory systems that persist information across sessions, the Internal Cognitive Memory focuses on **recent operational history and short-lived control information**. Its role is to ensure that the system can reason about what just happened, what is currently pending, and what conditions may still influence behaviour.

This memory is therefore primarily **operational rather than conversational or semantic**. It exists to support the internal control logic of the Cognitive Core rather than to store knowledge for future retrieval.

---

## Architectural Purpose

The purpose of the Internal Cognitive Memory is to provide **short-term continuity for system control**.

During operation, NORA processes events continuously. Many decisions depend not only on the current event and state but also on **recent history**. For example:

* whether a command was just issued
* whether a similar event occurred moments ago
* whether an action was recently attempted
* whether a failure occurred repeatedly
* whether the system recently recovered from an error

Without a mechanism to remember these recent events, the system could behave inconsistently or repeat unnecessary operations.

The Internal Cognitive Memory therefore allows the Cognitive Core to maintain a minimal history of relevant information that supports coherent decision-making.

---

## Role Within the Cognitive Core

Within the Cognitive Core architecture, the Internal Cognitive Memory complements the other submodules:

* **FSM** provides the structural behavioural model.
* **Operational Context** describes the current situation of the system.
* **Emotional State** modulates behaviour.
* **Internal Cognitive Memory** preserves recent operational history.

Together, these elements allow the system to interpret events not only based on the current state and context but also on what has happened recently.

---

## Characteristics of Internal Cognitive Memory

The Internal Cognitive Memory has several defining characteristics.

### 1. Short-Term

This memory stores only recent operational information rather than long-term knowledge.

### 2. Behaviour-Oriented

All stored information must support behavioural decisions or control logic.

### 3. Non-Persistent by Default

Most of the information stored here exists only during system runtime and may be cleared when the system restarts.

### 4. Lightweight

The memory should remain compact and efficient to avoid unnecessary complexity.

### 5. Continuity-Oriented

The primary goal is to preserve continuity across events and actions.

---

## Types of Information Stored

The Internal Cognitive Memory may contain several types of information relevant to system control.

### Recent Events

A record of the most recent events processed by the system.

Examples:

* last wake word detection
* last speech recognition result
* last gesture event

This allows the system to detect repeated events or avoid redundant actions.

---

### Recent State Transitions

Information about the latest transitions executed by the FSM.

Possible fields:

* previous_state
* current_state
* transition_timestamp

This information can help diagnose unexpected behaviour or support recovery logic.

---

### Recent Errors

A record of recent system errors or failures.

Examples:

* microphone failure
* network disconnection
* planner timeout

Tracking recent errors allows the system to detect recurring problems and adjust behaviour accordingly.

---

### Last Active User

The identity of the most recent user who interacted with the system.

This may help maintain interaction continuity when the same user resumes interaction shortly afterward.

---

### Last Activation Source

Information about how the system was most recently activated.

Possible sources include:

* wake word
* gesture
* touch interface
* NFC tag
* remote command

This helps the system interpret follow-up inputs appropriately.

---

### Pending Operations

Information about operations that were initiated but not yet completed.

Examples:

* waiting for confirmation
* waiting for planner output
* waiting for external API response

This information allows the system to resume or cancel operations correctly.

---

## Updating Internal Cognitive Memory

The Internal Cognitive Memory is updated whenever relevant operational events occur.

Typical update triggers include:

* FSM transitions
* perception detections
* action execution events
* system errors
* interaction activations

Updates should be lightweight and deterministic so that memory remains consistent with system behaviour.

---

## Relationship With Other Modules

### FSM

The FSM may store transition information in the Internal Cognitive Memory to maintain behavioural history.

### Operational Context

Operational Context represents the current situation, while Internal Cognitive Memory represents recent history leading up to that situation.

### Dialogue and Sessions

Dialogue modules may occasionally consult this memory to determine whether an interaction recently occurred.

### Persistence and Logs

Although this memory is primarily runtime-based, important events may also be recorded in persistent logs for analysis or debugging.

---

## Design Principles

The Internal Cognitive Memory should follow several design principles.

### Minimalism

Only information necessary for operational continuity should be stored.

### Consistency

Stored data should always reflect actual system history.

### Bounded Size

The memory should maintain a limited window of recent information to prevent unbounded growth.

### Determinism

Memory updates should be predictable and synchronized with system behaviour.

---

## Relationship With Other Memory Systems

The architecture contains multiple memory systems, each serving a different role.

* **Internal Cognitive Memory** stores recent operational history.
* **Operational Context** stores current runtime conditions.
* **Dialogue Memory** stores conversation history.
* **Persistent Memory** stores long-term knowledge and user data.

Maintaining clear separation between these systems prevents architectural confusion and simplifies maintenance.

---

## Summary

The Internal Cognitive Memory provides short-term operational continuity for the Cognitive Core.

By storing recent events, transitions, errors, and activation information, it allows NORA to maintain coherent behaviour across event sequences and interaction flows.

Although lightweight compared to other memory systems, it plays a critical role in ensuring that system behaviour remains consistent, traceable, and responsive to recent history.
