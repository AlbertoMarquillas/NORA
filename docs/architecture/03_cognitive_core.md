# 4. Cognitive Core

## Definition

The Cognitive Core is the architectural subsystem responsible for maintaining the internal operational state of NORA and regulating system behaviour across events, interactions, and subsystem activity.

The Cognitive Core acts as the internal control layer of the architecture. It maintains the live operational state of the system, stores the dynamic operational context required for system behaviour, records short‑term internal memory, and regulates behavioural transitions.

While Interaction Interfaces define how users communicate with NORA and the Perception System defines how the system acquires information from the environment, the Cognitive Core defines how the system internally represents its current situation and how behaviour evolves across events.

Through this subsystem, NORA maintains operational continuity, coordinates internal subsystems, and preserves behavioural coherence across multimodal inputs, asynchronous events, and ongoing interactions.

The Cognitive Core provides the internal behavioural foundation that allows NORA to operate as a unified system rather than as a collection of independent modules.

## Core Concepts

The Cognitive Core architecture is defined through several explicit internal concepts.

* operational state
  structured representation describing what the system is currently doing and which behaviours are active

* system event
  normalized internal signal representing something that occurred in the system or environment

* state transition
  change from one operational state to another triggered by a system event

* operational context
  collection of contextual variables required for correct system operation

* behavioural constraint
  condition that regulates which behaviours are allowed under the current operational situation

* control memory
  short‑term internal memory used to maintain continuity across event sequences

* behavioural modulation state
  internal condition that influences how the system reacts to events and how responses are expressed

These concepts define the internal control model used by the Cognitive Core.

## Architectural Purpose

The purpose of the Cognitive Core is to provide an explicit internal model of system operation.

NORA operates as a multimodal embodied cognitive system capable of perceiving its environment, interacting with users, maintaining persistent sessions, executing actions, reacting to asynchronous events, and coordinating multiple subsystems simultaneously.

System behaviour therefore depends not only on the most recent input but also on contextual factors such as the active user, the interaction origin, the operational state of the system, subsystem availability, recent system events, and behavioural constraints.

The Cognitive Core centralizes these elements into a coherent operational model that provides a stable behavioural foundation for the rest of the architecture.

## Architectural Role

Within the overall architecture, the Cognitive Core sits between incoming system events and higher‑level reasoning or execution layers.

Conceptually the information flow can be represented as:

Interfaces / Perception / External Events → Cognitive Core → Dialogue / Planning / Action

In this role, the Cognitive Core does not perform sensing or direct actuation. Instead, it interprets incoming events, manages the operational state of the system, maintains contextual information, and determines the behavioural conditions under which other modules operate.

The Cognitive Core therefore acts as the behavioural coordination layer of the architecture.

## Responsibilities

The Cognitive Core performs several architectural responsibilities.

### Operational State Management

The module maintains the current operational state of the system.

Operational state describes the behavioural condition of NORA and the currently active system activity.

Examples of operational states include:

* idle
* listening
* interpreting input
* planning response
* waiting for confirmation
* executing action
* generating output
* recovering from error

The operational state defines which behaviours are active and which transitions are possible.

### Event Interpretation

Incoming system events are interpreted relative to the current operational state and operational context.

Examples of system events include:

* perception events
* interaction events
* internal system events
* subsystem state changes

Event interpretation determines how the system reacts to events under the current operational situation.

### Context Maintenance

The Cognitive Core maintains the dynamic operational context required for coherent behaviour.

Operational context may include:

* active user identity
* interaction origin
* active interaction session
* current interaction modality
* latest system event
* latest interpreted intent
* subsystem availability

This shared context allows multiple subsystems to operate coherently within the same operational situation.

### Behaviour Regulation

The module regulates behaviour through behavioural constraints and operational conditions.

Examples of behavioural constraints include:

* confirmation requirements
* interruption prioritization
* restricted action execution
* subsystem availability conditions
* safety conditions

These constraints determine which behaviours are permitted under the current operational situation.

### Continuity Across Events

The Cognitive Core maintains short‑term operational continuity across sequences of events.

This continuity allows the system to maintain coherent behaviour during ongoing interactions, multi‑step actions, interruptions, and asynchronous system activity.

### Behavioural Modulation

The Cognitive Core maintains an internal behavioural modulation state that influences how the system reacts to events and expresses responses.

Behavioural modulation may influence elements such as:

* response style
* dialogue tone
* visual feedback
* motion or expression behaviour

### Traceability

Centralizing operational state and behavioural transitions provides traceability of system behaviour.

Traceability allows system activity to be inspected, debugged, audited, and analyzed across event sequences.

## Scope

The Cognitive Core includes mechanisms responsible for modelling and regulating the internal operational behaviour of NORA.

Its scope includes:

* operational state modelling
* event‑driven state transitions
* operational context management
* behavioural constraints
* short‑term control memory

The Cognitive Core does not include the following responsibilities:

* raw sensory processing
* user interface rendering
* long‑term conversational memory
* domain‑specific reasoning
* action execution
* low‑level actuator control

These responsibilities belong to other architectural modules.

## Internal Structure

The Cognitive Core is divided into several internal submodules.

### 4.1 Finite State Machine

The Finite State Machine models the operational states of the system and defines the possible transitions between those states.

### 4.2 Operational Context

The Operational Context stores the live contextual information required for system operation.

### 4.3 Emotional State

The Emotional State represents the internal behavioural modulation state that influences how the system reacts to events and expresses responses.

### 4.4 Internal Cognitive Memory

Internal Cognitive Memory provides short‑term memory used for maintaining operational continuity across event sequences.

Together these components define the internal behavioural control layer that allows NORA to maintain coherent operation across perception events, interaction events, planning decisions, and system actions.

# 4.1 Finite State Machine

## Definition

The Finite State Machine is the mechanism used by the Cognitive Core to model and regulate the operational behaviour of NORA.

A finite state machine represents system behaviour as a set of explicit operational states connected by transitions. Transitions occur when system events are evaluated relative to the current state and valid transition conditions are satisfied.

At any moment, the system is associated with one operational state. Incoming events are interpreted relative to that state and may produce a transition to a different state.

The Finite State Machine provides the formal structure through which behavioural evolution of the system is defined and controlled.

Within the architecture, the FSM centralizes behavioural transitions so that perception modules, interaction mechanisms, planning components, and action subsystems operate within a coherent operational framework.

## Core Concepts

The FSM architecture is defined through several fundamental concepts.

* operational state
  structured representation describing the current behavioural condition of the system

* system event
  normalized signal representing something that occurred in the system or environment

* state transition
  change from one operational state to another triggered by a system event

* transition guard
  condition that must be satisfied for a transition to occur

* transition action
  operation triggered as a consequence of a state transition

* event queue
  ordered structure that stores incoming system events awaiting evaluation

* event dispatcher
  architectural component responsible for injecting events into the FSM

These concepts define the operational model used by the FSM.

## Architectural Role

Within the Cognitive Core, the FSM acts as the behavioural control mechanism that governs how system behaviour evolves across events.

Perception systems, interaction interfaces, backend services, and internal modules produce events. These events are propagated to the FSM, where they are interpreted relative to the current operational state.

The FSM determines whether a valid transition exists and updates the system state accordingly.

The FSM therefore defines the behavioural progression of the system across time.

Conceptually the behavioural flow can be represented as:

Event Sources → Event Dispatcher → FSM → State Transition → Triggered Actions

The FSM does not perform perception, reasoning, or execution directly. It regulates the behavioural structure within which those operations occur.

## Operational States

An operational state represents the current behavioural condition of the system.

Each state defines:

* which events are meaningful
* which transitions are valid
* which system behaviours are active
* which operations are restricted

Operational states provide the behavioural frame in which system events are interpreted.

Examples of operational states include:

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

These states represent high-level behavioural conditions of the system.

## System Events

A system event represents a normalized description of something that occurred in the system or environment.

Events originate from multiple architectural domains.

Event sources include:

* perception subsystems
* interaction interfaces
* internal system modules
* backend services
* external integrations

Examples of system events include:

* wake word detected
* speech recognized
* gesture detected
* interaction command received
* planner result available
* action completed
* timeout reached
* error detected
* external trigger received

Events do not directly produce behaviour. Behaviour emerges from the evaluation of events relative to the current operational state.

## State Transitions

A state transition represents a change from one operational state to another.

Transitions occur when a system event is evaluated in the context of the current state and a valid transition rule exists.

A transition definition includes:

* origin state
* triggering event
* transition guard
* destination state
* transition actions

Example transition description:

Origin State: INACTIVE
Event: WAKE_WORD_DETECTED
Guard: microphone available
Destination State: LISTENING

Transitions define the behavioural evolution of the system.

## Transition Guards

Transition guards represent contextual conditions required for a transition to occur.

Guards reference information from operational context, subsystem status, or safety conditions.

Examples of guard conditions include:

* user authenticated
* subsystem available
* safety condition satisfied
* planner result valid

If the guard condition is not satisfied, the transition is not executed.

## Transition Actions

State transitions may trigger operations referred to as transition actions.

Transition actions represent operations executed when a transition occurs.

Examples of transition actions include:

* updating operational context
* activating perception pipelines
* invoking planning modules
* triggering dialogue generation
* notifying user interfaces
* recording system activity

These actions coordinate behaviour across multiple architectural modules.

## Event Queue

Incoming system events are stored in an event queue before evaluation.

The event queue defines the order in which events are processed by the FSM.

Sequential processing of queued events ensures deterministic behaviour even when events originate concurrently from multiple sources.

Event queues may incorporate prioritization mechanisms so that certain event types are processed earlier than others.

Examples of prioritized events include:

* safety alerts
* interruption commands
* emergency conditions

## Event Dispatcher

The event dispatcher is responsible for injecting events into the FSM.

The dispatcher acts as the standardized entry point through which operational events enter the behavioural control layer.

Events originating from perception pipelines, interaction interfaces, backend services, or internal modules are forwarded to the dispatcher.

The dispatcher places events into the event queue where they await evaluation by the FSM.

## FSM Behaviour Cycle

During system operation, behavioural processing follows a recurring cycle.

1. An event is generated by a subsystem or external source.
2. The event is forwarded to the event dispatcher.
3. The dispatcher places the event into the FSM event queue.
4. The FSM retrieves the next event from the queue.
5. The event is evaluated relative to the current operational state.
6. If a valid transition rule exists and guard conditions are satisfied, the FSM performs the transition.
7. Transition actions are executed.
8. The new operational state becomes active.

This behavioural cycle continues throughout system operation.

## State Categories

Operational states may be grouped into behavioural categories.

Lifecycle states

* OFF
* INITIALIZING
* SHUTTING_DOWN

Idle states

* INACTIVE
* OBSERVING

Interaction states

* LISTENING
* INTERPRETING
* SPEAKING

Decision states

* PLANNING
* WAITING_FOR_CONFIRMATION

Execution states

* EXECUTING_ACTION

Recovery states

* ERROR
* RECOVERING
* SUSPENDED

These categories help organize the behavioural state graph of the system.

## Transition History

The FSM maintains a transition history describing behavioural changes of the system.

Transition history records may include:

* timestamp
* origin state
* triggering event
* destination state
* evaluated guards
* executed actions

Transition history enables system observability, debugging, behavioural analysis, and auditability.

## Relationship With Other Modules

Perception System

Perception subsystems generate perception events that may trigger FSM transitions.

Interaction Interfaces

Human interaction events propagate through the dispatcher to the FSM.

Dialogue and Session System

Dialogue behaviour is activated when the FSM enters interaction-related states.

Planning, Interpretation and Agents

Planning modules may be invoked when the FSM enters decision-related states.

Action and Expression

Physical or digital actions are triggered when the FSM enters execution-related states.

## Role Within the Cognitive Core

Within the Cognitive Core, the FSM provides the formal behavioural structure of the system.

Other Cognitive Core components such as operational context, emotional state, and internal cognitive memory supply contextual information used during event evaluation and transition decisions.

Together these components define the behavioural control layer that allows the system to maintain coherent operation across perception events, interaction sequences, planning activities, and action execution.

# 4.2 Operational Context

## Definition

The Operational Context is the subsystem of the Cognitive Core that maintains the dynamic representation of the current runtime situation of NORA.

While the Finite State Machine defines the structural behavioural state of the system, the Operational Context stores the live information required to interpret events and evaluate behavioural conditions.

The Operational Context therefore represents the situational variables that describe the current operating conditions of the system.

These variables include information about active users, interaction state, subsystem availability, active actions, recent events, and safety conditions.

The Operational Context allows the system to interpret the same event differently depending on the surrounding runtime situation.

## Core Concepts

The Operational Context architecture is defined through several fundamental concepts.

* contextual variable
  runtime variable describing a situational property of the system

* context state
  structured collection of contextual variables representing the current system situation

* context update
  modification of contextual variables triggered by events or subsystem activity

* context access
  read or write operation performed on contextual variables by architectural modules

* context source
  subsystem responsible for producing or updating contextual variables

These concepts define the structure through which situational information is represented within the Cognitive Core.

## Architectural Role

Within the Cognitive Core, the Operational Context provides the situational information required for behavioural evaluation.

The Finite State Machine evaluates system events relative to the current operational state and the current operational context.

Operational context therefore acts as the runtime information layer used during transition evaluation and behavioural regulation.

Conceptually the relationship can be described as:

Event → FSM Evaluation → State Transition

FSM Evaluation depends on:

* current operational state
* operational context variables

The Operational Context therefore supplies the situational data required for context-aware behavioural control.

## Context Characteristics

Operational Context exhibits several structural characteristics within the architecture.

Dynamic

Context variables change continuously during runtime as events occur and subsystem conditions evolve.

Short-lived

Most contextual variables represent transient runtime conditions rather than long-term stored information.

Shared

Multiple architectural components may read contextual variables when evaluating behaviour.

Behaviourally relevant

Each contextual variable represents information that influences behavioural decisions or transition evaluation.

Non-persistent

Operational Context exists primarily in runtime memory and is typically reset when the system restarts.

## Context Categories

The Operational Context contains several categories of contextual information.

### User Context

User Context describes information about the currently relevant user.

Examples of contextual variables include:

* active_user_id
* authenticated_user
* user_presence_detected
* user_profile_loaded

User Context supports identity-aware interaction behaviour.

### Interaction Context

Interaction Context describes the current interaction flow between the system and external actors.

Examples of contextual variables include:

* interaction_active
* interaction_mode
* interaction_source
* conversation_active
* session_id

Interaction Context supports interpretation of interaction events within ongoing interaction sessions.

### Activation Context

Activation Context describes the mechanism that triggered the current interaction or system activation.

Examples include:

* wake_word
* gesture
* physical_button
* nfc_tag
* remote_command

Activation Context provides information about the origin of system activation.

### System Context

System Context describes the operational status of hardware and software subsystems.

Examples of contextual variables include:

* microphone_available
* camera_available
* network_available
* sensors_operational
* hardware_error_state

System Context allows the system to adapt behaviour according to subsystem availability.

### Action Context

Action Context describes the execution status of system actions.

Examples of contextual variables include:

* action_in_progress
* current_action_type
* action_source
* awaiting_confirmation

Action Context prevents conflicting operations and supports interruption handling.

### Event Context

Event Context describes information related to recently processed system events.

Examples include:

* last_event
* last_event_timestamp
* last_event_source

Event Context supports behavioural continuity across event sequences.

### Safety Context

Safety Context describes system conditions related to safety restrictions and protection mechanisms.

Examples include:

* emergency_stop
* safety_lock
* restricted_actions

Safety Context ensures that system behaviour respects safety constraints.

## Context Updates

Context updates occur when events are processed or subsystem conditions change.

Examples of context update sources include:

* perception pipelines
* interaction interfaces
* authentication mechanisms
* hardware monitoring systems
* action execution modules
* planning results

Each update modifies specific contextual variables associated with the relevant subsystem.

## Context Access

Architectural modules interact with the Operational Context through read and write operations.

Read access

Subsystems read contextual variables to evaluate behavioural conditions and adapt behaviour.

Write access

Subsystems update contextual variables when relevant events occur or subsystem conditions change.

Controlled update mechanisms maintain consistency of contextual information across modules.

## Relationship With Other Modules

Finite State Machine

The FSM reads contextual variables when evaluating transition guards and behavioural conditions.

Perception System

Perception modules update contextual variables related to presence detection, gesture recognition, and environmental conditions.

Interaction Interfaces

Interaction modules update contextual variables describing interaction origin and interaction activity.

Dialogue and Session System

Dialogue modules use contextual variables describing interaction sessions and conversation state.

Planning, Interpretation and Agents

Planning modules read contextual variables related to user identity, current actions, and system state.

Action and Expression

Action modules update contextual variables describing execution progress and completion.

Identity, Access and Security

Authentication mechanisms update contextual variables describing active user identity and authorization state.

## Design Principles

Operational Context follows several architectural principles.

Relevance

Context variables represent information that directly influences behavioural decisions.

Consistency

Context variables represent the current system situation and remain synchronized with subsystem state.

Controlled modification

Updates to contextual variables occur through defined subsystem interfaces.

Observability

Context variables are inspectable for debugging, monitoring, and system observability.

Minimal coupling

Subsystems depend only on the contextual variables required for their operation.

## Relationship With Other Memory Systems

Operational Context represents the runtime situational layer of the Cognitive Core.

It is distinct from other memory subsystems.

Operational Context

runtime situational variables

Internal Cognitive Memory

short-term internal behavioural memory

Dialogue Memory

conversation history and dialogue state

Persistent Memory

long-term stored knowledge and user data

Each of these subsystems serves a different architectural role.

## Role Within the Cognitive Core

Within the Cognitive Core, the Operational Context provides the situational information layer used by behavioural control mechanisms.

The Finite State Machine evaluates events relative to both the current operational state and the current operational context.

Together, the FSM and Operational Context define the runtime behavioural condition of the system.

This combination allows the system to interpret events in a context-aware manner and maintain coherent behaviour across perception events, interaction sequences, planning activities, and action execution.

# 4.3 Emotional State

## Definition

The Emotional State is the subsystem of the Cognitive Core that represents the internal behavioural modulation condition of NORA.

While the Finite State Machine defines the structural operational state of the system and the Operational Context represents situational runtime variables, the Emotional State represents the internal modulation layer that influences how the system reacts to events and expresses behaviour.

The Emotional State is an internal operational abstraction. It does not represent psychological emotions. Instead, it represents behavioural modulation variables that influence response style, attention level, event prioritization, and interaction posture.

Through this subsystem, the system maintains a behavioural condition that modulates decision evaluation and behavioural expression during runtime.

## Core Concepts

The Emotional State architecture is defined through several fundamental concepts.

* emotional state
  internal behavioural condition that modulates system reactions and expressive behaviour

* emotional transition
  change from one emotional state to another triggered by system events or behavioural outcomes

* behavioural modulation
  influence of emotional state on behavioural parameters

* emotional trigger
  event or condition that produces a change in emotional state

* emotional stability mechanism
  mechanism that prevents excessive oscillation between emotional states

These concepts define how behavioural modulation is represented within the Cognitive Core.

## Architectural Role

Within the Cognitive Core, the Emotional State operates as a behavioural modulation layer.

The FSM defines the operational activity of the system.

The Operational Context represents the situational runtime conditions.

The Emotional State influences behavioural parameters used during event evaluation, interaction management, and expressive output generation.

Conceptually the relationship can be represented as:

Operational State + Operational Context + Emotional State → Behaviour

The Emotional State therefore modifies behavioural posture without altering the structural control logic of the FSM.

## Emotional State Model

The Emotional State is represented as a discrete internal state variable.

At any moment, the system is associated with one emotional state.

Emotional states represent behavioural modulation conditions that influence interaction behaviour and system response characteristics.

Examples of emotional states include:

* neutral
* attentive
* focused
* curious
* uncertain
* alert
* waiting
* frustrated
* satisfied
* recovering

These states represent behavioural modulation conditions rather than psychological emotions.

## Behavioural Modulation

The Emotional State influences behavioural parameters used during system operation.

Examples of modulated behavioural properties include:

Response pacing

speed and timing of responses

Response verbosity

level of explanation or detail in system responses

Interaction persistence

degree to which the system continues interaction after uncertainty or failure

Event prioritization

relative priority assigned to incoming events

Attention allocation

degree of sensitivity to new events or interruptions

Expression modulation

parameters influencing voice, visual indicators, or motion patterns

These modulation effects influence system behaviour without altering structural system logic.

## Emotional Triggers

Changes in emotional state occur in response to system events or behavioural outcomes.

Examples of emotional triggers include:

* perception anomalies
* successful task completion
* repeated interpretation failures
* low-confidence recognition results
* safety alerts
* interaction success or failure

These triggers generate emotional transitions within the emotional state model.

## Emotional Stability

The Emotional State subsystem includes mechanisms that regulate emotional transitions.

Emotional stability mechanisms reduce excessive oscillation between emotional states and maintain behavioural consistency during runtime.

Examples of stability mechanisms include:

* transition cooldown intervals
* minimum state duration
* weighted transition conditions

These mechanisms maintain interpretable behavioural dynamics.

## Emotional Updates

Emotional state updates occur when emotional triggers are evaluated during system operation.

Subsystems that may contribute to emotional updates include:

* perception modules
* interaction systems
* planning results
* action execution outcomes
* safety monitoring systems

Emotional transitions update the internal emotional state variable used for behavioural modulation.

## Relationship With Other Modules

Finite State Machine

FSM transitions may produce emotional triggers associated with specific operational states such as error, recovery, or execution success.

Operational Context

Contextual variables may influence emotional triggers, such as repeated recognition failures or prolonged inactivity.

Dialogue and Session System

Dialogue behaviour may adapt to emotional state when selecting response strategies.

Action and Expression

Expression subsystems read emotional state variables when determining expressive output parameters.

Planning, Interpretation and Agents

Planning modules may consider emotional state when evaluating interaction strategies or confirmation behaviour.

## Design Principles

The Emotional State subsystem follows several architectural principles.

Interpretability

Each emotional state corresponds to a clearly defined behavioural modulation condition.

Stability

Emotional transitions occur through controlled mechanisms that prevent rapid oscillation.

Behavioural relevance

Each emotional state influences behavioural parameters or interaction strategy.

Separation from expression

Internal emotional state remains separate from external expressive behaviour.

## Relationship With Expression Systems

The Emotional State represents an internal behavioural modulation variable.

External behavioural expression is implemented by other architectural modules.

Emotional State

internal behavioural condition

Expression Systems

external manifestation through voice, visual indicators, lighting, or motion

The Cognitive Core exposes emotional state information that may be interpreted by expression systems when generating external behaviour.

## Role Within the Cognitive Core

Within the Cognitive Core, the Emotional State provides behavioural modulation information used during system operation.

Behaviour emerges from the combination of:

* operational state defined by the FSM
* situational variables stored in Operational Context
* behavioural modulation defined by Emotional State

Together these components define the runtime behavioural condition of the system.

# 4.4 Internal Cognitive Memory

## Definition

The Internal Cognitive Memory is the short‑term operational memory subsystem of the Cognitive Core. It stores recent internal events, transitions, and control information required for behavioural continuity during system runtime.

Unlike persistent memory systems, Internal Cognitive Memory maintains only short‑lived operational history. Its purpose is to allow the system to reason about recent events, ongoing operations, and recent behavioural outcomes while processing new events.

This subsystem therefore supports the internal control logic of the Cognitive Core by providing a bounded temporal window of recent system activity.

## Core Concepts

The Internal Cognitive Memory architecture is defined through several fundamental concepts.

recent event

record of a recently processed event

transition record

record of a recently executed FSM state transition

error record

record of a recent system anomaly or operational failure

activation record

information about the most recent system activation

pending operation

operation initiated by the system that has not yet reached completion

memory window

bounded temporal or structural limit defining how much recent information is stored

These concepts define the operational information maintained by the subsystem.

## Architectural Role

Within the Cognitive Core, the Internal Cognitive Memory provides short‑term operational history used during behavioural evaluation.

The FSM defines the structural behaviour of the system.

The Operational Context represents the current situational variables.

The Emotional State modulates behavioural posture.

The Internal Cognitive Memory preserves recent system activity that influences how current events are interpreted.

Conceptually the relationship can be expressed as:

Operational State + Operational Context + Emotional State + Recent Operational History → Behaviour

The Internal Cognitive Memory therefore provides the temporal continuity required for coherent behaviour across event sequences.

## Memory Model

Internal Cognitive Memory maintains a bounded set of operational records.

The memory structure contains recent operational information required by control logic.

Typical stored structures include:

recent events

queue or buffer containing recently processed events

recent transitions

history of the most recent FSM transitions

recent errors

history of recent anomalies or operational failures

recent activation

information about the most recent activation source

pending operations

operations that are currently awaiting completion or confirmation

These structures represent recent behavioural history rather than persistent knowledge.

## Behavioural Continuity

The primary function of Internal Cognitive Memory is maintaining behavioural continuity across system events.

Examples of behavioural continuity mechanisms include:

Detection of repeated events

recognizing when identical events occur in close succession

Avoidance of redundant actions

preventing repeated execution of identical operations

Failure tracking

detecting repeated operational failures

Action completion tracking

recognizing when initiated operations complete successfully

Activation continuity

maintaining behavioural continuity after system activation

These mechanisms ensure consistent behaviour during event sequences.

## Memory Window

Internal Cognitive Memory operates within a bounded memory window.

The window defines how much recent information is retained by the system.

Possible window strategies include:

fixed number of records

only the most recent N events are stored

time‑based window

records older than a defined duration are removed

priority‑based retention

certain types of records persist longer than others

This bounded structure prevents uncontrolled memory growth while preserving recent behavioural history.

## Memory Updates

Internal Cognitive Memory is updated continuously during system operation.

Typical update triggers include:

FSM state transitions

Perception events

Action execution outcomes

System errors

Interaction activations

Completion of pending operations

Each update modifies only the relevant memory structures while preserving other records within the memory window.

## Memory Access

Different Cognitive Core subsystems access Internal Cognitive Memory when evaluating behavioural decisions.

FSM

may consult recent transitions and recent events when evaluating guard conditions

Operational Context

may reference recent activation or event history

Planning and Agents

may inspect recent failures or repeated commands

Dialogue and Sessions

may reference recent activation records or recent user actions

Memory access occurs through controlled interfaces to maintain consistency of stored information.

## Relationship With Other Modules

Finite State Machine

FSM transitions are recorded as transition records within the memory subsystem.

Operational Context

Operational Context stores the current situational state, while Internal Cognitive Memory stores the recent history leading to that state.

Dialogue and Session System

Dialogue modules may reference recent interaction activity stored in memory.

Persistence and Logging

Important operational records may also be stored in persistent logs for observability and system diagnostics.

## Design Principles

The Internal Cognitive Memory subsystem follows several architectural principles.

Minimal scope

only operationally relevant information is stored

Bounded structure

memory window limits the size of stored information

Deterministic updates

memory updates follow predictable rules synchronized with system events

Operational relevance

stored information must influence behavioural decisions or system control

Consistency

records reflect actual system history and behavioural outcomes

## Relationship With Other Memory Systems

The architecture contains multiple memory layers with different responsibilities.

Internal Cognitive Memory

short‑term operational history used by the Cognitive Core

Operational Context

representation of the current situational state

Dialogue Memory

storage of conversational history

Persistent Memory

long‑term storage of knowledge, users, and system data

Maintaining separation between these memory layers preserves architectural clarity.

## Role Within the Cognitive Core

Within the Cognitive Core, the Internal Cognitive Memory provides recent operational history used during behavioural evaluation.

System behaviour emerges from the interaction between:

* structural operational state defined by the FSM
* situational variables defined by Operational Context
* behavioural modulation defined by Emotional State
* recent operational history stored in Internal Cognitive Memory

Together these components define the internal cognitive condition of the system during runtime.

## Architectural Structure

```
Cognitive Core
│
├── Finite State Machine (FSM)
│ ├── system operational states
│ ├── behavioural state graph
│ ├── event-driven transitions
│ ├── transition guards
│ ├── transition actions
│ ├── event queue processing
│ ├── event dispatcher integration
│ ├── state lifecycle control
│ ├── behavioural determinism
│ ├── transition history tracking
│ └── system behavioural coordination
│
├── Operational Context
│ ├── runtime situational awareness
│ ├── active user context
│ ├── interaction context
│ ├── activation source tracking
│ ├── subsystem availability status
│ ├── hardware operational status
│ ├── action execution context
│ ├── event origin information
│ ├── safety context
│ ├── runtime contextual variables
│ ├── context update mechanisms
│ └── shared context access
│
├── Emotional State
│ ├── behavioural modulation state
│ ├── emotional state model
│ ├── emotional state transitions
│ ├── emotional triggers
│ ├── response style modulation
│ ├── interaction persistence modulation
│ ├── event prioritization modulation
│ ├── attention allocation modulation
│ ├── behavioural posture control
│ ├── emotional stability mechanisms
│ └── emotional transition regulation
│
└── Internal Cognitive Memory
  ├── short‑term operational memory
  ├── recent event history
  ├── recent state transition records
  ├── recent activation records
  ├── recent interaction records
  ├── recent error history
  ├── pending operation tracking
  ├── action execution history
  ├── behavioural continuity support
  ├── bounded memory window
  ├── memory update mechanisms
  └── recent operational history
```

---

## Architectural Layers

The Cognitive Core module operates through several complementary layers that structure how system behaviour is evaluated, modulated, and coordinated.

| Layer                             | Responsibility                                                                                   |
| --------------------------------- | ------------------------------------------------------------------------------------------------ |
| Behavioural Control Layer         | Defines the operational behaviour of the system through the Finite State Machine                 |
| Situational Awareness Layer       | Maintains the runtime context required to interpret events and system conditions                 |
| Behavioural Modulation Layer      | Adjusts system reactions and interaction posture through the Emotional State                     |
| Short‑Term Cognitive Memory Layer | Preserves recent operational history used for behavioural continuity                             |
| Behaviour Coordination Layer      | Integrates state, context, memory, and emotional modulation to produce coherent system behaviour |

Together, these layers establish the internal cognitive control architecture of NORA, ensuring that perception, interaction, planning, and action remain behaviourally consistent across system operation.
