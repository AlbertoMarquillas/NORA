# 10. Frontend and Visualization

## Definition

The **Frontend and Visualization** module defines the visual interaction layer through which users and administrators observe, control, and interact with NORA.

While the Backend and Application layer exposes system capabilities and orchestrates internal services, the frontend represents the **human-facing operational surface** of the system.

This module is responsible for presenting information, enabling interaction, and providing operational transparency over the robot's behaviour, internal state, conversations, and system capabilities.

The frontend does not execute the cognitive logic of NORA, nor does it implement perception, planning, or action systems. Instead, it provides the visual and interactive environment that allows humans to understand and control the system in an intuitive and structured way.

---

## Architectural Purpose

The purpose of the Frontend and Visualization module is to translate the internal behaviour of NORA into a **clear, accessible, and interactive visual interface**.

NORA is a complex multimodal system composed of many subsystems:

* perception modules
* cognitive core and FSM
* dialogue and session systems
* planning and specialized agents
* action and expression channels
* persistent storage
* hardware interfaces
* external integrations

Without a dedicated visualization layer, observing and controlling these subsystems would require direct access to internal APIs, logs, or technical tools.

The frontend solves this by providing structured interfaces that allow users and administrators to:

* interact with the robot
* visualize system behaviour
* access conversation history
* manage projects
* configure preferences
* monitor hardware and runtime status
* perform administrative operations

Through this module, the internal complexity of the architecture becomes manageable for human operators.

---

## Role in the Global Architecture

Within the global architecture of NORA, the frontend acts as the **visual and interactive gateway** between humans and the system.

Conceptually, its position can be represented as:

Human User / Administrator → Frontend Interface → Backend and Application → Internal Domains

The frontend communicates with the backend through APIs and realtime channels, while the backend coordinates interactions with the rest of the architecture.

This separation ensures that user interfaces remain independent from the internal implementation details of the system.

---

## Why This Module Is Necessary

A cognitive robot system such as NORA must provide ways for humans to:

* communicate with the system
* understand what the system is doing
* inspect internal states
* configure behaviour
* recover sessions or projects
* diagnose problems

Without a frontend layer, these operations would require command-line tools or direct database access, which would not be suitable for most users.

The frontend module is therefore necessary because it provides:

* an accessible interaction surface
* operational visibility into the system
* configuration interfaces
* administrative control tools
* visualization of internal behaviour

This allows NORA to function as a practical system rather than a purely technical platform.

---

## Scope of the Module

The Frontend and Visualization module includes everything related to **visual representation and user interaction with the system**.

Its scope includes:

* graphical user interfaces
* user interaction screens
* administrative dashboards
* chat interfaces
* project visualization tools
* system monitoring views
* configuration panels
* device management interfaces

Its scope does **not** include:

* backend business logic
* cognitive reasoning
* perception pipelines
* action execution
* database management
* authentication logic implementation

Those responsibilities remain in other architectural modules.

The frontend interacts with those domains through the backend services and realtime communication channels.

---

## Core Responsibilities

The Frontend and Visualization module performs several key responsibilities.

### User Interaction

It provides the primary interface through which users communicate with NORA.

This includes:

* conversational interfaces
* command interfaces
* project management screens
* preference configuration

These interfaces allow users to engage with the system in a structured way.

### System Visualization

The frontend visualizes the internal behaviour of the system so that users and administrators can understand what is happening.

Examples include:

* FSM state visualization
* conversation progress
* system notifications
* action execution feedback
* sensor status

This transparency improves trust and usability.

### Operational Monitoring

Administrative interfaces allow technical users to inspect system health and behaviour.

Examples include:

* hardware status
* telemetry information
* event streams
* system logs
* module availability

These tools are essential for debugging and maintenance.

### Configuration and Control

The frontend provides interfaces for modifying system configuration and user preferences.

Examples include:

* language settings
* voice configuration
* connected devices
* feature activation
* interaction preferences

This allows the behaviour of NORA to adapt to different users and environments.

### Administrative Control

Administrative tools allow privileged users to manage the system.

Examples include:

* managing users
* assigning permissions
* restarting modules
* inspecting logs
* executing maintenance operations

These capabilities are essential for operating the system in real environments.

---

## Relationship With Other Modules

The Frontend and Visualization module interacts with several other architectural components.

### Relationship With Backend and Application

The frontend communicates with the system primarily through:

* HTTP APIs
* realtime channels

The backend exposes system capabilities, while the frontend provides the human interface that consumes those capabilities.

### Relationship With Identity and Security

User authentication and authorization rules defined in the Identity and Access module determine which frontend features are available to each user.

For example:

* standard users access conversation interfaces
* advanced users access additional tools
* administrators access system control panels

### Relationship With Dialogue and Sessions

The frontend presents the conversation interface and allows users to interact with sessions and conversational projects.

Session information, message history, and context summaries are visualized through the frontend interface.

### Relationship With the Cognitive Core

The frontend can visualize operational state information from the FSM, allowing users or developers to observe how the system transitions between states.

This visualization is particularly useful for debugging and system monitoring.

### Relationship With Perception and Action

The frontend may display information produced by perception modules, such as camera streams or detected objects.

Similarly, it may visualize actions executed by the robot, such as movement, speech, or device control.

---

## Design Principles

Several principles should guide the design of the frontend architecture.

### Clarity

Interfaces should make system behaviour understandable.

Users should be able to easily determine:

* what the system is doing
* what it is waiting for
* what actions are available

### Responsiveness

The interface should update dynamically as the system state changes.

Realtime communication channels help maintain synchronization between the backend and the user interface.

### Separation From Backend Logic

The frontend should focus on visualization and interaction rather than embedding system logic.

Application behaviour should remain implemented in backend services.

### Role-Based Interfaces

Different users require different levels of control.

For example:

* end users require simple interaction interfaces
* developers require debugging tools
* administrators require system management capabilities

The interface should adapt accordingly.

### Observability

The frontend should expose sufficient information to make the system observable without requiring internal debugging tools.

This improves transparency and maintainability.

---

## Internal Structure

To maintain clarity, the Frontend and Visualization module is divided into three major submodules:

* **10.1 User Interface Zone** – the primary interface used by regular users to interact with NORA.
* **10.2 Administration Zone** – advanced system control and monitoring tools.
* **10.3 System State Visualization** – live visualization of internal system state and operational information.

These submodules organize the different roles the frontend must support while keeping the architecture understandable.

---

## Typical Examples of Frontend Interactions

Representative frontend interactions in NORA may include:

* opening a conversational session
* reviewing conversation history
* restoring a conversational project
* observing FSM state transitions
* monitoring hardware status
* inspecting system logs
* modifying user preferences
* configuring connected devices
* executing administrative maintenance operations

These examples illustrate how the frontend acts as the human interface to the full architecture.

---

## Architectural Importance

The Frontend and Visualization module is essential for transforming NORA from a purely technical architecture into a usable system.

Without it, interaction would depend entirely on internal tools and APIs.

By providing structured visual interfaces, this module allows:

* intuitive interaction with the system
* real-time visibility of behaviour
* effective system administration
* monitoring and debugging
* accessible configuration and control

In practical terms, the frontend becomes the **window through which humans perceive and operate the NORA system**.

# 10.1 User Zone

## Definition

The **User Zone** is the primary frontend area through which standard users interact with NORA in a direct, accessible, and personalized way.

It represents the main user-facing interface of the platform and groups the visual tools required for day-to-day interaction with the system. Through this area, users can communicate with NORA, access their projects, review their interaction history, configure personal preferences, and manage the devices associated with their account.

Within the overall frontend architecture, the User Zone is not intended for deep technical supervision or system administration. Its purpose is to provide a **clear, practical, and user-centered interaction space** that supports normal usage of NORA.

In other words, if the Administration Zone is designed for control and maintenance, the User Zone is designed for **interaction, continuity, and personalization**.

---

## Architectural Purpose

The purpose of the User Zone is to provide a structured frontend surface where users can:

* access NORA as a personal assistant or cognitive system
* interact through chat or visual workflows
* continue ongoing sessions or projects
* inspect their own history
* configure how the system behaves for them
* manage their associated devices and personal environment

Because NORA supports persistent dialogue, user profiles, conversational projects, and multiple forms of interaction, the frontend must provide more than a single chat window.

The User Zone exists to organize those capabilities into a coherent interface adapted to regular users.

---

## Role in the Frontend Architecture

Within the **Frontend and Visualization** module, the User Zone is the **main interaction surface for non-administrative usage**.

Conceptually, it is the frontend counterpart of several internal architectural domains:

* the **Dialogue and Session System**, because it exposes conversations, sessions, and continuity
* the **Project System**, because it allows users to open and manage conversational projects
* the **User Profile**, because it allows personalization and preference configuration
* the **Backend and Application** layer, because it consumes APIs and realtime updates

This means the User Zone is not just a visual shell. It is the operational frontend space where the user experiences NORA as an interactive system.

---

## Why This Submodule Is Necessary

Without a dedicated user area, the frontend would become an unstructured mixture of:

* chat functionality
* configuration screens
* personal data
* project management
* device management
* system visualization

This would reduce clarity and make the experience harder to use.

The User Zone is necessary because it separates **normal user interaction flows** from technical or administrative flows.

It gives standard users a space focused on:

* communicating with NORA
* continuing work over time
* managing their own environment
* understanding their own interactions

This separation is especially important in NORA because the system is not only conversational, but also persistent, multimodal, and personalized.

---

## Scope of the User Zone

The User Zone includes the frontend capabilities primarily intended for regular authenticated users.

Its scope includes:

* login entry point for users
* personal dashboard
* chat and conversational interaction
* project access and continuity
* interaction history
* personal configuration
* profile access
* linked device management

Its scope does **not** include:

* advanced system administration
* protected technical logs
* permission management for all users
* hardware maintenance operations
* infrastructure supervision

Those belong to the Administration Zone.

---

## Main Components

The User Zone is composed of several major interface areas.

### Login

The login interface is the entry point through which a user authenticates and gains access to their personalized NORA environment.

Its role is to:

* identify the user
* start an authenticated session
* load the corresponding profile and permissions
* establish continuity with previous sessions and preferences

Although authentication logic belongs to the Identity, Access and Security module, the User Zone must provide the frontend surface for it.

The login experience may include:

* email or username login
* password entry
* OAuth access
* QR-assisted flows
* trusted device recognition

From the frontend perspective, login should be simple, secure, and clearly separated from later interaction screens.

---

### Dashboard

The dashboard is the main landing area after authentication.

Its purpose is to provide the user with a summarized view of their current relationship with NORA.

Typical information shown in the dashboard may include:

* active session status
* recent conversations
* current or recent projects
* pending reminders or tasks
* quick access to main actions
* system highlights relevant to the user

The dashboard acts as the **user’s operational home screen** inside NORA.

Rather than forcing the user to begin from an empty interface every time, it provides continuity, shortcuts, and context.

---

### Chat

The chat interface is the core conversational surface of the User Zone.

It allows the user to communicate directly with NORA through a textual or hybrid visual conversation interface.

This component is the frontend representation of the Dialogue and Session System.

Typical chat capabilities include:

* sending messages
* receiving responses
* continuing active sessions
* seeing conversation history within the active thread
* receiving clarifications and confirmations
* interacting with multimodal outputs when available

In architectural terms, the chat is not just message rendering. It is the **visible conversational container** for sessions, context, and interactive continuity.

---

### Projects

The projects area allows the user to access and continue persistent conversational or task-oriented projects.

Examples may include:

* learning workflows
* programming projects
* study plans
* long-running personal goals
* topic-based conversations

This interface must allow users to:

* list available projects
* open a project
* continue its associated context
* inspect project-related content
* identify current progress or status

The projects area is especially important in NORA because many user interactions are not isolated conversations but parts of larger long-term processes.

---

### History

The history area allows the user to inspect previous interactions with NORA.

This may include:

* previous conversations
* past sessions
* historical summaries
* prior project interactions
* timestamps and metadata

The purpose of the history interface is not only archival access, but also continuity.

It helps the user:

* remember previous work
* reopen earlier conversations
* locate relevant information
* understand what has already been discussed

This component is therefore closely related to session recovery and conversational persistence.

---

### Configuration

The configuration area allows the user to modify how NORA behaves for them.

Typical configurable settings may include:

* interface language
* voice settings
* notification preferences
* interaction style
* display preferences
* personalization options

This interface gives the user control over the operational experience without exposing deeper technical system internals.

Its purpose is to make NORA adaptable to individual needs while preserving architectural separation between personal settings and global administrative configuration.

---

### Profile

The profile area provides access to the user’s personal information and persistent identity-related settings.

Typical profile information may include:

* display name
* preferred language
* linked identity methods
* personalization data
* educational level or interaction preferences

The profile area serves as the frontend view of the **User Profile** submodule from the identity architecture.

It allows users to inspect and update the persistent information that shapes how NORA interacts with them.

---

### Devices

The devices area allows the user to inspect and manage the devices linked to their account or interaction environment.

Examples may include:

* trusted smartphones
* tablets
* NFC-linked devices
* remote access devices
* paired external interfaces

Typical capabilities may include:

* listing associated devices
* identifying active devices
* revoking a linked device
* managing trust relationships
* checking last usage or availability

This component is important because NORA is not limited to one single screen or one single point of interaction. The system may exist across multiple surfaces and trusted device relationships.

---

## Relationship With Other Modules

The User Zone interacts with several other architectural components.

### Relationship With Identity and Access

The User Zone depends on user authentication, session validation, and profile loading.

Available interface elements may vary depending on:

* whether the user is authenticated
* which role the user has
* which permissions are active

### Relationship With Dialogue and Sessions

The chat, history, and continuity mechanisms of the User Zone are direct frontend counterparts of the Dialogue and Session System.

This includes:

* active session continuity
* session recovery
* conversational history access
* project-linked dialogue

### Relationship With Persistence

Many elements of the User Zone rely on persistent data.

Examples include:

* saved conversations
* projects
* profile information
* configuration preferences
* device associations

The frontend itself does not manage persistence directly, but it visualizes persistent information retrieved through backend services.

### Relationship With Backend and Application

The User Zone consumes:

* HTTP endpoints
* realtime updates
* session APIs
* project APIs
* profile services

This makes it a direct consumer of the Backend and Application layer.

---

## Design Principles

Several principles should guide the design of the User Zone.

### User-Centered Simplicity

The interface should prioritize clarity and directness.

Users should be able to understand:

* where to talk to NORA
* where to find their projects
* where to recover previous work
* where to change preferences

### Continuity First

Because NORA supports persistent dialogue and long-term projects, the interface should not feel stateless.

It should make continuity visible through:

* recent sessions
* active projects
* historical context
* resumable interactions

### Personalization

The User Zone should reflect the user’s identity and preferences.

Examples include:

* preferred language
* selected voice
* favorite workflows
* saved devices

### Clear Separation From Admin Tools

The user interface should remain focused on personal interaction and should not overload normal users with technical controls that belong to administrators.

### Realtime Feedback

Whenever useful, the User Zone should reflect live system behaviour, such as:

* active conversation state
* task progress
* current system feedback relevant to the user

---

## Typical User Flows

Representative user flows inside the User Zone may include:

### Start Interaction Flow

1. User logs in
2. Dashboard loads
3. User opens chat
4. User starts or resumes a conversation

### Continue Project Flow

1. User opens projects area
2. Selects an existing project
3. Project context is restored
4. User continues the interaction from the associated context

### Review History Flow

1. User enters history area
2. Browses previous sessions
3. Opens a prior conversation
4. Recovers relevant context or information

### Update Preferences Flow

1. User enters configuration or profile area
2. Changes settings such as language or voice
3. Saves preferences
4. Future interactions adapt accordingly

### Manage Devices Flow

1. User enters devices area
2. Reviews associated devices
3. Revokes or confirms a device
4. Trust relationships are updated

These flows show that the User Zone is not a single page but a structured interaction environment.

---

## Inputs and Outputs

### Representative Inputs

Examples of frontend inputs in the User Zone may include:

* login request
* chat message
* project selection
* history recovery request
* preference update
* profile edit
* device management action

### Representative Outputs

Examples of frontend outputs in the User Zone may include:

* conversation view
* dashboard summaries
* project cards or lists
* historical records
* confirmation messages
* profile data views
* linked device status

These outputs allow the user to interact with NORA in a visually structured and persistent way.

---

## Architectural Importance

The **User Zone** is one of the most important frontend submodules because it is the place where most users actually experience NORA.

It concentrates the practical interaction surface of the system and turns the underlying architecture into something usable, personal, and continuous.

Without this submodule, users would lack a coherent place to:

* talk to NORA
* continue long-term work
* review past interactions
* configure their environment
* manage their personal relationship with the system

For that reason, the User Zone should be treated as the **primary human interaction surface of the frontend architecture**.

# 10.2 Administration Zone

## Definition

The **Administration Zone** is the advanced frontend area through which authorized technical users supervise, configure, maintain, and control the operational state of NORA.

While the **User Zone** is focused on normal interaction, continuity, and personalization, the Administration Zone is focused on **system governance, technical visibility, operational control, and maintenance**.

This submodule provides privileged interfaces intended for users such as administrators, developers, operators, or maintainers who need access to deeper system capabilities than those available in the standard user-facing area.

Within the frontend architecture, the Administration Zone acts as the **visual control surface for advanced system management**.

---

## Architectural Purpose

The purpose of the Administration Zone is to expose the tools required to operate NORA as a real deployed system rather than only as a conversational product.

A complex embodied cognitive system such as NORA requires more than a normal user interface. It also requires administrative tools for:

* supervising runtime behaviour
* inspecting internal state
* managing users and permissions
* observing hardware and telemetry
* troubleshooting failures
* triggering technical actions
* maintaining configuration consistency

Without a dedicated administration area, those responsibilities would fall back to raw APIs, ad hoc scripts, or direct access to backend services, which would reduce operational clarity and increase risk.

The Administration Zone exists to centralize these technical capabilities into a structured and secure frontend environment.

---

## Role in the Frontend Architecture

Within the **Frontend and Visualization** module, the Administration Zone is the **privileged operational interface**.

Conceptually, it is the frontend counterpart of several internal architectural domains, especially:

* **Identity, Access and Security**, because it includes user and permission management
* **Backend and Application**, because it exposes technical control and orchestration surfaces
* **Cognitive Core**, because it may visualize FSM state and operational flow
* **Perception, Hardware, and Action systems**, because it may expose technical monitoring and manual controls
* **Persistence and Observability**, because it may show logs, metrics, events, and telemetry

This makes the Administration Zone a cross-cutting frontend area that reflects the internal structure of the full system.

---

## Why This Submodule Is Necessary

NORA is not only a user-facing assistant. It is also a running platform composed of:

* backend services
* perception modules
* state machines
* sessions and projects
* hardware devices
* realtime channels
* persistence systems
* security policies

Operating such a system requires dedicated administrative interfaces.

The Administration Zone is necessary because it separates:

* normal user interaction
* technical supervision and control

This separation is essential for several reasons:

* it protects sensitive capabilities from regular users
* it reduces interface clutter in the normal user area
* it enables safe technical workflows
* it improves system maintainability
* it supports debugging, monitoring, and intervention

In architectural terms, the Administration Zone ensures that advanced operational control exists as a first-class frontend capability rather than as an afterthought.

---

## Scope of the Administration Zone

The Administration Zone includes the frontend capabilities intended for privileged operational management.

Its scope includes:

* user administration
* permission and role supervision
* access to system logs
* hardware state monitoring
* telemetry visualization
* live event observation
* manual tools and technical actions
* restart and recovery controls
* global configuration management

Its scope does **not** include:

* the implementation of backend logic itself
* raw infrastructure management outside the system boundary
* domain reasoning performed by planners or agents
* direct hardware firmware implementation

Those concerns belong to other architectural layers.

The Administration Zone provides the frontend access surface for them.

---

## Main Components

The Administration Zone is composed of several major interface areas.

### Users

The users area provides interfaces for inspecting and managing user accounts known by NORA.

Typical capabilities may include:

* listing users
* inspecting account status
* viewing associated roles
* reviewing linked devices
* activating or deactivating accounts
* inspecting account-related metadata

This area is especially important for systems where multiple users interact with NORA across time, devices, and trust levels.

From the frontend perspective, the users panel is the main administrative entry point for identity supervision.

---

### Permissions

The permissions area allows administrators to inspect and manage access control policies associated with users, roles, or system capabilities.

Typical capabilities may include:

* viewing role assignments
* inspecting effective permissions
* adjusting permission sets
* reviewing access levels for protected domains
* checking which users can access sensitive tools or hardware

Because NORA includes both digital and physical actions, permission management is particularly important.

Permissions may affect access to:

* administrative endpoints
* hardware controls
* persistent memory
* external integrations
* system configuration

This area is the frontend expression of the authorization architecture.

---

### Logs

The logs area provides structured access to technical records generated by the system.

Typical log categories may include:

* backend logs
* action execution logs
* error logs
* audit logs
* security logs
* session-related technical logs

The purpose of this area is to make the system inspectable during debugging, maintenance, and incident analysis.

Rather than requiring direct terminal access, administrators can use the frontend to inspect operational traces in a controlled way.

---

### Hardware Status

The hardware status area allows administrators to inspect the current state of the physical and embedded components of NORA.

Examples of monitored elements may include:

* camera availability
* microphone availability
* speaker status
* servo state
* battery level
* CPU temperature
* connectivity state
* peripheral availability

This area is important because NORA is embodied and depends on physical components whose availability directly affects behaviour.

Hardware visibility helps administrators determine whether errors come from software logic or device-level failures.

---

### Telemetry

The telemetry area visualizes continuous technical measurements about the runtime behaviour of the system.

Typical telemetry may include:

* CPU usage
* memory usage
* network activity
* sensor streams
* response times
* internal service health
* queue sizes or throughput

The purpose of telemetry is to support live monitoring, anomaly detection, and performance supervision.

This area is especially useful in long-running deployments where the system must remain observable across time.

---

### Live Events

The live events area provides realtime visibility into operational events occurring in the system.

Examples may include:

* perception events
* FSM transitions
* action triggers
* session lifecycle events
* warnings and failures
* external event injections

This area acts as a live operational window into the dynamic behaviour of NORA.

For developers and administrators, it is one of the most useful tools for understanding what the system is doing at runtime.

---

### Manual Tools

The manual tools area exposes privileged technical actions that administrators may trigger directly from the frontend.

Examples may include:

* dispatching a test event
* triggering a diagnostic action
* reloading a configuration
* opening a maintenance flow
* forcing a sync operation
* performing a controlled test of hardware or modules

This area should be carefully restricted because manual tools can alter the behaviour of the running system.

Its purpose is to support operations, debugging, and maintenance without requiring direct backend access.

---

### Restarts and Recovery

This area provides administrative controls related to restarting modules, resetting subsystems, or initiating recovery procedures.

Typical actions may include:

* restarting a service
* reinitializing a perception module
* clearing transient error states
* reloading runtime state
* triggering controlled recovery flows

Because restart-like operations can affect running sessions and ongoing actions, they must be:

* protected
* clearly presented
* audited
* constrained by policy

This area is essential for safe maintenance of a live NORA deployment.

---

### Global Configuration

The global configuration area allows administrators to inspect and modify system-wide settings.

Examples may include:

* feature flags
* environment-dependent settings
* default interaction policies
* service endpoints
* hardware behaviour settings
* operational thresholds

This area differs from the user configuration area because it affects the whole system rather than one specific user.

It should therefore be highly protected and clearly separated from personal settings.

---

## Relationship With Other Modules

The Administration Zone interacts with many other architectural domains.

### Relationship With Identity, Access and Security

The Administration Zone depends heavily on authentication and authorization.

Only privileged users should be able to access it, and different administrative capabilities may require different permission levels.

This zone also exposes frontend tools for:

* user supervision
* permission inspection
* security-relevant operations
* access governance

### Relationship With Backend and Application

Most administrative functionality is exposed through backend services and realtime channels.

Examples include:

* user APIs
* event APIs
* hardware status endpoints
* logs and telemetry services
* admin operations

The Administration Zone is therefore a major consumer of the Backend and Application layer.

### Relationship With the Cognitive Core

Administrative interfaces may visualize:

* current FSM state
* transition history
* current operational context
* blocked or restricted actions

This makes the Cognitive Core observable from the admin frontend.

### Relationship With Perception, Action, and Hardware

Because NORA is embodied, the Administration Zone may expose operational visibility into:

* sensor availability
* actuator readiness
* movement status
* camera and microphone state
* intentional action execution

This helps connect software supervision with physical system reality.

### Relationship With Persistence and Technical History

The Administration Zone may visualize persistent technical records such as:

* system logs
* audit history
* failures
* event traces
* action records

This gives administrators access to operational memory of the system.

---

## Design Principles

Several principles should guide the design of the Administration Zone.

### Security First

Administrative interfaces must be designed with strict access control.

Sensitive capabilities should never be exposed casually, and dangerous actions should require explicit protection or confirmation.

### Clarity of Risk

Potentially impactful actions such as restarts, resets, or manual triggers should clearly communicate:

* what they do
* what they affect
* whether they are reversible
* whether they may interrupt users or sessions

### Observability

The interface should make the internal behaviour of the system inspectable.

This includes:

* state visibility
* log access
* telemetry
* events
* hardware condition

### Separation From Normal User Experience

The Administration Zone should remain distinct from the User Zone.

This avoids confusing normal users with technical controls and reduces the risk of accidental misuse.

### Realtime Awareness

Because many administrative tasks depend on current runtime state, the interface should support realtime updates whenever possible.

Examples include:

* live event streams
* current hardware state
* service health
* active failures

### Auditability

Administrative actions should be traceable.

The interface should integrate with audit logging and clearly identify sensitive operations.

---

## Typical Admin Flows

Representative flows inside the Administration Zone may include:

### User Supervision Flow

1. Administrator opens users area
2. Reviews account list
3. Inspects a specific user
4. Adjusts status or role-related information if permitted

### Hardware Diagnosis Flow

1. Administrator opens hardware status area
2. Reviews subsystem availability
3. Detects that a camera or microphone is unavailable
4. Uses telemetry or logs to investigate the issue

### Live Debugging Flow

1. Administrator opens live events panel
2. Observes realtime event flow
3. Identifies a failing sequence or repeated error
4. Consults logs and state visualization
5. Triggers a maintenance action if needed

### Recovery Flow

1. Administrator detects a module failure
2. Opens restart or recovery area
3. Reviews impact and constraints
4. Executes a protected restart or recovery action
5. Confirms restored operational state

### Global Configuration Flow

1. Administrator opens configuration area
2. Reviews current global settings
3. Updates a controlled value
4. Saves and verifies the new behaviour

These flows show that the Administration Zone is the operational workspace for maintaining the system.

---

## Inputs and Outputs

### Representative Inputs

Examples of frontend inputs in the Administration Zone may include:

* user management request
* permission inspection request
* log search query
* hardware inspection command
* telemetry filter selection
* manual event dispatch
* restart request
* configuration update

### Representative Outputs

Examples of frontend outputs in the Administration Zone may include:

* user tables
* permission matrices
* log streams
* hardware state panels
* telemetry dashboards
* live event feeds
* confirmation prompts for sensitive actions
* global configuration views

These outputs make the technical state of NORA visible and operable.

---

## Architectural Importance

The **Administration Zone** is essential because NORA is not only an interactive assistant but also a living operational system that must be supervised, debugged, secured, and maintained.

Without this submodule, advanced system control would be scattered across raw tools and backend entry points.

By providing a structured administrative frontend, NORA gains:

* safer operational control
* clearer technical observability
* maintainable system supervision
* controlled access to sensitive capabilities
* better debugging and recovery workflows

For that reason, the Administration Zone should be treated as the **primary privileged control surface of the frontend architecture**.

# 10.3 State Visualization

## Definition

The **State Visualization** module is the frontend area responsible for presenting the real-time operational state of NORA and its internal subsystems.

While the **User Zone** focuses on interaction and the **Administration Zone** focuses on governance and technical control, the State Visualization module focuses on **observability of the running system**.

This submodule provides structured visual interfaces that expose the runtime condition of the robot, allowing users, administrators, and developers to understand what the system is currently doing.

Within the frontend architecture, the State Visualization module acts as the **visual window into the internal runtime state of NORA**.

---

## Architectural Purpose

The purpose of the State Visualization module is to translate the internal operational state of NORA into **clear and interpretable visual information**.

NORA is a complex event-driven system composed of multiple interacting subsystems such as:

* perception modules
* the cognitive core and FSM
* dialogue and session systems
* planning and agent execution
* action and expression subsystems
* hardware devices
* backend services

Without a dedicated visualization layer, understanding the behaviour of the system would require accessing logs, APIs, or internal debugging tools.

The State Visualization module solves this by presenting the current runtime condition of the system through structured visual panels.

This allows operators to quickly understand:

* what the system is currently doing
* what state the robot is in
* which sensors are active
* which session is currently running
* what actions have recently been executed

---

## Role in the Frontend Architecture

Within the **Frontend and Visualization** module, the State Visualization area acts as the **observability interface of the system**.

Conceptually, it represents the frontend counterpart of several internal architectural domains, including:

* **Cognitive Core**, because it visualizes FSM state and emotional state
* **Perception**, because it reflects sensor activity and environment perception
* **Dialogue and Session System**, because it shows the active session and project
* **Action and Expression**, because it shows executed outputs and actions
* **Backend and Application**, because runtime state is delivered through backend services and realtime channels

This makes the State Visualization module a cross-cutting interface that exposes the dynamic behaviour of the entire system.

---

## Why This Submodule Is Necessary

NORA operates as a stateful, event-driven system where behaviour continuously evolves according to perception, dialogue context, internal planning, and executed actions.

Without clear visualization of these internal dynamics, it would be difficult to understand why the robot behaves in a certain way.

The State Visualization module is necessary because it provides:

* transparency of system behaviour
* easier debugging and monitoring
* improved trust in system decisions
* better operational awareness for administrators

By exposing runtime state in an interpretable form, the module allows humans to understand the internal activity of the robot without inspecting backend infrastructure directly.

---

## Scope of the State Visualization Module

The State Visualization module includes frontend components that display the runtime condition of NORA.

Its scope includes:

* FSM state visualization
* emotional state visualization
* sensor status monitoring
* active device information
* session and project visibility
* recent system outputs and actions

Its scope does **not** include:

* decision-making logic
* backend orchestration
* perception processing
* planner reasoning
* hardware control

Those responsibilities belong to other architectural layers. The visualization module simply reflects their runtime state.

---

## Main Components

The State Visualization module is composed of several visualization panels.

### FSM State

The FSM State panel displays the **current operational state of the finite state machine** that governs NORA's behaviour.

Typical information may include:

* current state
* previous state
* event that triggered the transition
* transition timestamp

This visualization helps operators understand the current operational phase of the system.

---

### Current Emotion

The Current Emotion panel displays the **internal emotional state** generated by the Cognitive Core.

Possible states may include:

* neutral
* curiosity
* focus
* doubt
* alert
* frustration
* satisfaction

Visualizing emotional state helps explain variations in behaviour such as tone of voice, animations, or response patterns.

---

### Sensors

The Sensors panel displays the **current status of perception and environmental sensors**.

Examples of monitored elements may include:

* microphone activity
* camera availability
* gesture detection
* proximity detection
* environmental sensor reporting

This panel helps administrators understand what the robot is currently perceiving from its environment.

---

### Active Device

The Active Device panel identifies the **interface or device currently interacting with the system**.

Possible devices may include:

* local robot interface
* web frontend
* mobile interface
* NFC interaction
* external API client

This information is useful in environments where multiple interaction surfaces exist.

---

### Active Session

The Active Session panel displays the **currently running interaction session**.

Typical information may include:

* session identifier
* associated user
* session type
* session duration

This panel provides visibility into the conversational context currently active in the system.

---

### Active Project

The Active Project panel displays the **project or long-term conversational context** currently associated with the session.

Examples may include:

* language learning
* programming project
* study session
* personal workflow

This connects frontend observability with the persistent conversation architecture.

---

### Executed Outputs

The Executed Outputs panel shows the **most recent actions performed by the system**.

Examples may include:

* spoken responses
* robot movements
* multimedia playback
* domotic device control
* notifications sent

This visualization helps correlate system decisions with observable actions.

---

## Relationship With Other Modules

The State Visualization module interacts with several architectural domains.

### Relationship With the Cognitive Core

FSM state and emotional state originate from the Cognitive Core and are visualized in this module.

### Relationship With Perception

Sensor information displayed here reflects the runtime condition of perception modules.

### Relationship With Dialogue and Sessions

Session and project information originate from the Dialogue and Session system.

### Relationship With Backend and Application

Most runtime updates are delivered through backend services and realtime communication channels such as WebSockets.

---

## Design Principles

Several principles should guide the design of the State Visualization module.

### Real-Time Awareness

The interface should update dynamically as the system state evolves.

### Clarity

Each panel should represent a specific aspect of system behaviour to avoid information overload.

### Architectural Consistency

Visual elements should correspond directly to internal architectural components.

### Observability

The module should make the behaviour of the system understandable without requiring backend debugging tools.

---

## Inputs and Outputs

### Representative Inputs

Examples of data received by this module may include:

* FSM state updates
* emotional state updates
* sensor status changes
* session lifecycle events
* project activation
* executed action events

### Representative Outputs

Examples of visual outputs produced by this module include:

* state indicators
* activity panels
* runtime dashboards
* event timelines
* system status widgets

---

## Architectural Importance

The **State Visualization** module is essential for making NORA observable as a living system.

By exposing the runtime state of perception, cognition, dialogue, and action, it allows users and administrators to understand how the robot behaves in real time.

This improves:

* debugging
* monitoring
* system transparency
* trust in the system

For this reason, the State Visualization module should be considered the **observability layer of the frontend architecture**.
