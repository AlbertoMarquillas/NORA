# 8. Backend and Application

## Definition

The **Backend and Application** module is the architectural layer responsible for orchestrating use cases, exposing APIs, coordinating communication between domains, and providing the runtime services that connect NORA’s internal intelligence with external interfaces and system operations.

If the **Cognitive Core** defines how NORA behaves internally, and the **Planning, Interpretation and Agents** layer determines what NORA should do, the Backend and Application layer defines **how the system is operationally connected, coordinated, exposed, and supervised as a running software platform**.

This module acts as the application-level backbone of NORA. It does not perform perception itself, does not define the robot’s behavioural logic, and does not directly replace the execution layer. Instead, it provides the software structures that allow all those domains to work together reliably in a real system.

In practical terms, this module is where architectural decisions become executable application flows.

---

## Architectural Purpose

The purpose of the Backend and Application module is to provide a **stable operational layer** that connects the rest of the architecture into a coherent software system.

NORA is not a single isolated model or script. It is a multimodal cognitive platform composed of many interacting subsystems:

* perception pipelines
* dialogue and session management
* planning and specialized agents
* action and expression channels
* persistent storage
* user and security systems
* frontend interfaces
* hardware controllers
* external integrations

Without an application layer, these parts would remain disconnected or would depend on brittle direct coupling.

The Backend and Application module exists to:

* expose the system through controlled interfaces
* coordinate communication between subsystems
* implement application-level use cases
* standardize event flow
* provide realtime state propagation
* centralize observability and operational monitoring

This makes the whole architecture runnable, debuggable, maintainable, and extensible.

---

## Role in the Global Architecture

Within the global NORA architecture, this module acts as the **operational orchestration layer** between the cognitive system and the external world of clients, services, tools, and runtime infrastructure.

Conceptually, its role can be understood as:

**Frontend / External Systems / Internal Domains ↔ Backend and Application ↔ Core System Behaviour**

This means the Backend and Application layer is the place where:

* frontend requests are received and validated
* internal services are invoked
* system events are routed
* state changes are exposed to clients
* domain boundaries are coordinated
* technical monitoring is performed

It therefore acts as the **software nervous system** of the architecture.

---

## Why This Module Is Necessary in NORA

A system like NORA cannot rely on direct connections between all modules.

For example:

* the frontend should not directly manipulate FSM internals
* the planner should not directly manage websocket client state
* perception modules should not decide how APIs are exposed
* hardware controllers should not be responsible for user-facing session logic

Those responsibilities must be mediated through a dedicated application layer.

The Backend and Application module is necessary because NORA requires:

* a structured API surface
* realtime communication channels
* service-level orchestration
* event dispatch coordination
* runtime observability
* clear boundaries between domain logic and technical infrastructure

Without this module, the architecture would become tightly coupled, difficult to debug, and hard to evolve as the system grows.

---

## Scope of the Module

The Backend and Application module includes the software structures responsible for **application orchestration and system exposure**.

Its scope includes:

* HTTP APIs and service endpoints
* realtime communication channels
* application services implementing use cases
* coordinators and orchestration components
* standardized event dispatch entry points
* logs, traces, metrics, and technical observability

Its scope does **not** include:

* raw perception processing
* internal behavioural modelling of the FSM itself
* semantic interpretation or planning logic
* direct hardware implementation details
* long-term storage engines themselves
* frontend rendering itself

Those responsibilities belong to other modules.

This distinction is important because the Backend and Application layer should coordinate domains without absorbing their internal logic.

---

## Core Responsibilities

This module performs several major architectural responsibilities.

### API Exposure

It exposes controlled entry points through which frontend interfaces, remote clients, admin tools, and external systems can interact with NORA.

This includes endpoints for:

* authentication
* events
* sessions
* projects
* users
* administration
* hardware control
* configuration

### Realtime State Distribution

It provides live communication channels so that other system parts and frontend clients can observe what is happening in real time.

Examples include:

* current FSM state
* live notifications
* technical logs
* telemetry streams
* active conversation state
* progress of ongoing actions

### Use Case Orchestration

It implements the application-level services that transform domain capabilities into usable system behaviours.

Examples include:

* creating a session
* opening a project
* dispatching an event
* synchronizing user context
* updating hardware state
* triggering an admin action

### Domain Coordination

It coordinates communication between major architectural modules without collapsing their separation of concerns.

Examples include:

* perception to FSM
* FSM to planner
* planner to agents
* planner to action
* dialogue to sessions
* users to permissions to execution

### Event Routing

It provides a standardized operational pathway through which system events enter the behavioural core.

This avoids fragmented or inconsistent event injection across the system.

### Observability and Supervision

It centralizes technical insight into the runtime system.

This includes:

* logging
* tracing
* metrics
* technical auditability
* live debugging visibility

This responsibility is essential in a complex embodied system where many asynchronous processes may run simultaneously.

---

## Design Principles

Several principles should guide the design of this module.

### Separation of Concerns

The Backend and Application layer should orchestrate domains, not replace them.

It should coordinate perception, cognition, dialogue, planning, action, persistence, and frontend interaction while preserving the internal autonomy of each domain.

### Explicit Boundaries

Every exposed API, event route, or service should make architectural responsibility clear.

A request should enter the system through a well-defined interface and then be delegated to the correct service or coordinator.

### Use-Case Orientation

Application services should be organized around concrete system use cases rather than around arbitrary technical groupings.

This improves maintainability and aligns the implementation with system behaviour.

### Event Consistency

All important operational events should flow through clear and standardized paths.

This is especially important for FSM integration, realtime frontend synchronization, and technical observability.

### Realtime Awareness

Because NORA is interactive and embodied, the backend cannot be designed only around request-response logic.

It must also support streaming state, live notifications, ongoing action progress, and asynchronous event propagation.

### Observability by Design

Logs, traces, metrics, and technical debugging should not be added as an afterthought.

They should be part of the architecture from the beginning.

---

## Relationship With Other Modules

The Backend and Application layer interacts with almost every architectural domain.

### Relationship With Identity, Access and Security

Authentication, authorization, session validation, and permission enforcement are applied at many backend entry points.

The backend exposes protected interfaces, but trust logic remains defined by the identity and security architecture.

### Relationship With Interaction Interfaces and Frontend

Frontend interfaces and remote interaction channels communicate with the system primarily through this module.

The backend acts as the operational gateway between user-facing clients and internal domain services.

### Relationship With Perception

Perception modules may emit events, status changes, or processed results that need to be routed through application coordinators or the event dispatcher.

### Relationship With the Cognitive Core

The Backend and Application layer does not define the FSM, but it often acts as the infrastructure through which FSM events are injected, states are observed, and transitions are surfaced to other system components.

This remains consistent with the role of the Cognitive Core as the formal behavioural engine of NORA.

### Relationship With Dialogue and Session System

Sessions, projects, conversation history, and recovery flows typically rely on application services to expose, create, update, retrieve, and synchronize their runtime state.

### Relationship With Planning, Interpretation and Agents

The backend may invoke planners and agents as part of application use cases, but it should not absorb their reasoning role.

Instead, it coordinates their participation in larger flows.

### Relationship With Action and Expression

Once decisions are ready for execution, the backend may coordinate delivery toward action channels, frontend updates, and logging systems.

### Relationship With Persistence

The backend often mediates access to persistent data such as users, sessions, projects, events, logs, and configuration.

However, storage concerns remain conceptually separate from application orchestration.

---

## Internal Structure

To maintain architectural clarity, the Backend and Application module is divided into the following submodules:

### 8.1 API HTTP

Defines the request-response interface through which frontend clients and external services interact with NORA.

### 8.2 WebSocket / Realtime

Defines the live communication channels used for state streaming, notifications, logs, telemetry, and real-time interaction updates.

### 8.3 Application Services

Defines the use-case-oriented service layer that coordinates system behaviour at the application level.

### 8.4 Coordinators / Orchestrators

Defines the modules that connect major architectural domains while preserving separation of responsibilities.

### 8.5 Event Dispatcher

Defines the standardized event entry point into the operational core, especially the FSM.

### 8.6 Observability

Defines the technical visibility layer for logs, traces, metrics, and runtime supervision.

Together, these components turn NORA from a set of architectural domains into a coherent running platform.

---

## Typical Examples of What This Module Handles

Representative backend and application responsibilities may include:

* receiving a frontend command to open a session
* validating an authenticated request
* pushing a live FSM state update to the web interface
* routing a perception event to the dispatcher
* calling a project service to restore a conversational project
* triggering an admin maintenance action
* exposing conversation history through an API endpoint
* streaming live telemetry to an admin dashboard
* recording technical traces for a failing action flow

These examples show that this module is not only an integration convenience layer, but a fundamental architectural pillar for the operational life of the system.

---

## Architectural Importance

The Backend and Application module is what allows NORA to exist as a **coordinated software system rather than as a loose collection of modules**.

Without it, the architecture would still describe many important capabilities, but it would lack:

* controlled access paths
* structured application services
* live coordination between domains
* consistent event injection
* technical observability
* practical runtime organization

By introducing this module as a dedicated architectural layer, NORA gains the operational structure required for real deployment, maintainability, monitoring, and long-term growth.

In that sense, the Backend and Application module is the layer that operationally binds together the rest of the architecture.

# 8.1 HTTP API

## Definition

The **HTTP API** is the application interface through which frontend clients, administrative tools, remote systems, and external services communicate with NORA using structured request-response interactions.

Within the Backend and Application module, the HTTP API provides the **formal access surface** of the system. It exposes controlled endpoints that allow other components to query system state, trigger use cases, manage resources, and interact with NORA in a standardized way.

If the Cognitive Core defines how NORA behaves internally, and the Application Services implement operational use cases, the HTTP API defines **how those capabilities are exposed to the outside in a secure, structured, and maintainable way**.

This submodule therefore acts as the main synchronous communication gateway of the platform.

---

## Architectural Purpose

The purpose of the HTTP API is to provide a **stable, explicit, and interoperable contract** between NORA and any client or service that needs to interact with it through standard web protocols.

NORA includes many possible clients and integration points:

* the web frontend
* local admin interfaces
* remote dashboards
* mobile or tablet interfaces in future extensions
* internal services exposed over the network
* external systems and automations
* integration middleware

All these actors need a structured way to communicate with the system without directly depending on internal code or runtime implementation details.

The HTTP API exists to provide that structure.

It allows NORA to expose:

* authenticated access points
* system resources
* application use cases
* operational commands
* state queries
* management endpoints

Through this, the system becomes externally usable while preserving internal modularity.

---

## Role in the Global Architecture

Within the global NORA architecture, the HTTP API acts as the **request-response boundary layer** between external consumers and internal application logic.

Conceptually, the role of this submodule can be represented as:

**Client / External System → HTTP API → Application Service / Coordinator / Dispatcher → Internal Domains**

This means the HTTP API is responsible for receiving structured requests, validating them, delegating them to the correct application-level components, and returning structured responses.

It does **not** contain the full business logic of the system. Instead, it should remain a thin and explicit interface layer that translates external requests into internal service operations.

---

## Why the HTTP API Is Necessary in NORA

NORA is a complex system that must be observed, configured, controlled, and extended from outside its internal runtime.

For example:

* the frontend needs to retrieve session data
* an admin panel needs to inspect hardware state
* a remote client may need to trigger an event
* an external integration may need to create a task or push a command
* the system may need machine-readable access to users, projects, logs, or configuration

Without a formal API, these interactions would depend on ad hoc internal connections, direct database access, or tightly coupled custom interfaces.

That would make the architecture fragile, insecure, and difficult to evolve.

The HTTP API is necessary because it provides:

* explicit system contracts
* controlled entry points
* transport-level interoperability
* modular access to application capabilities
* a clear separation between clients and domain internals

---

## Scope of the Submodule

The HTTP API submodule includes everything related to the **definition, exposure, and handling of synchronous request-response endpoints**.

Its scope includes:

* route definitions
* endpoint structure
* request validation
* response schemas
* authentication enforcement at API boundaries
* authorization checks at exposed operations
* delegation to application services
* error response normalization
* transport-level API conventions

Its scope does **not** include:

* realtime streaming state propagation
* internal behavioural logic of the FSM
* long-running event queues themselves
* direct implementation of domain reasoning
* frontend rendering
* low-level database models

Those concerns belong to other submodules or modules.

---

## Main Responsibilities

The HTTP API submodule performs several key architectural responsibilities.

### Endpoint Exposure

It exposes structured endpoints that represent the externally accessible functionality of the system.

These endpoints should correspond to meaningful resources or use cases such as:

* authentication
* session retrieval
* project management
* user management
* hardware status
* admin operations
* configuration access

### Request Validation

Incoming requests must be validated before entering the application layer.

This includes validation of:

* payload structure
* required fields
* parameter formats
* query constraints
* route parameters
* authentication credentials

This protects the system from malformed or inconsistent inputs.

### Delegation to Application Services

The API should not absorb internal business logic.

Instead, after validation and access control checks, it delegates work to:

* application services
* coordinators
* event dispatchers
* domain-specific handlers

This preserves clean architectural boundaries.

### Structured Responses

The HTTP API must return consistent and machine-readable responses.

Responses may include:

* requested data
* status information
* operation results
* validation errors
* authorization failures
* execution summaries

Consistency here is critical for frontend reliability and external integration.

### Access Control Enforcement

Many endpoints are protected and must enforce:

* authentication
* authorization
* role restrictions
* resource access rules

Although trust and permission logic belong to the Identity, Access and Security module, the HTTP API is one of the main places where those rules are operationally enforced.

### Error Normalization

The API should provide predictable error responses.

Errors should be distinguishable and structured, for example:

* invalid request
* unauthorized
* forbidden
* not found
* conflict
* internal error
* unavailable dependency

This makes integrations easier to build and debug.

---

## API Design Principles

Several principles should guide the design of the HTTP API.

### Explicit Contracts

Every endpoint should define clearly:

* its purpose
* accepted input
* expected output
* possible errors
* required permissions

The API must be understandable without knowing the internal implementation.

### Thin Controller Principle

Endpoint handlers should remain lightweight.

They should mainly perform:

* parsing
* validation
* access checks
* delegation
* response formatting

Core business logic should live in application services or domain layers.

### Resource and Use-Case Balance

Some endpoints naturally expose resources such as users, sessions, or projects.

Others represent explicit actions such as dispatching an event, restarting a module, or triggering a maintenance operation.

The API design should balance REST-like resource clarity with action-oriented use cases when appropriate.

### Consistency Across Domains

Naming conventions, response patterns, authentication rules, and error formats should remain consistent across all endpoint groups.

### Security by Default

Sensitive endpoints should never assume trust by default.

Authentication, authorization, auditability, and validation must be applied systematically.

### Evolvability

The API should be designed so new endpoints, versions, and domains can be added without breaking the conceptual structure.

---

## Typical Endpoint Domains

Based on the current architecture, the HTTP API may be organized into several major endpoint domains.

### Auth

Endpoints related to identity verification and session access.

Typical responsibilities may include:

* login
* logout
* token refresh
* current authenticated user retrieval
* trusted device registration

### Events

Endpoints used to inject or inspect system events.

Typical responsibilities may include:

* posting a structured event
* retrieving recent events
* testing event flows
* forwarding integration-generated events

### FSM

Endpoints that expose operational state machine information.

Typical responsibilities may include:

* retrieving current state
* retrieving transition history
* inspecting allowed transitions
* triggering controlled administrative transitions when permitted

### Sessions

Endpoints for managing conversational or interaction sessions.

Typical responsibilities may include:

* create session
* retrieve active session
* list previous sessions
* close or suspend session
* recover stored session

### Projects

Endpoints related to conversational projects or long-running objectives.

Typical responsibilities may include:

* create project
* list projects
* open project
* update project context
* archive or complete project

### Users

Endpoints related to user entities and associated profile information.

Typical responsibilities may include:

* retrieve users
* retrieve current profile
* update preferences
* manage linked devices
* inspect roles and permissions where allowed

### Admin

Endpoints for high-privilege system administration.

Typical responsibilities may include:

* manage users
* inspect protected logs
* restart modules
* trigger maintenance operations
* change global configuration

### Hardware

Endpoints that expose or control hardware-related information.

Typical responsibilities may include:

* camera status
* microphone status
* servo availability
* battery state
* device diagnostics
* manual hardware commands under policy

### Configuration

Endpoints that expose or modify application configuration.

Typical responsibilities may include:

* retrieve configuration values
* update runtime settings
* inspect feature flags
* manage environment-dependent behaviour

These domains help structure the API and keep responsibilities understandable.

---

## Request and Response Model

The HTTP API should define a clear model for how information enters and leaves the system.

### Requests

Requests may include:

* route parameters
* query parameters
* JSON bodies
* uploaded files
* authentication headers
* idempotency or tracing metadata

Each request should be validated and transformed into a form that application services can consume safely.

### Responses

Responses should be structured and predictable.

Typical response categories include:

* entity data
* operation result objects
* paginated collections
* acknowledgement responses
* validation error objects
* permission error objects

A well-designed response model improves both frontend development and integration reliability.

---

## Authentication and Authorization at the API Boundary

The HTTP API is one of the most sensitive trust boundaries in the whole system.

For that reason, endpoint access should be governed by the identity and authorization model already defined elsewhere in the architecture.

At the API layer, this typically means:

* identifying the caller
* validating credentials or tokens
* resolving the active user or client identity
* checking permissions for the requested operation
* rejecting unauthorized or forbidden actions
* propagating identity context to downstream services

Administrative, hardware, and sensitive configuration endpoints should apply stricter policies than public or user-level endpoints.

---

## Relationship With Application Services

The HTTP API should remain tightly connected to the Application Services layer but clearly separated from it.

The API receives requests.

The Application Services perform use-case logic.

For example:

* the API endpoint receives a request to open a session
* the Session Service resolves the real application operation
* the API returns the structured result

This separation ensures that the same service logic can potentially be reused by:

* HTTP endpoints
* WebSocket message handlers
* admin tools
* internal coordinators
* scheduled tasks

---

## Relationship With Realtime Channels

The HTTP API and WebSocket / Realtime submodule serve different communication roles.

### HTTP API

Best suited for:

* explicit requests
* resource retrieval
* updates initiated by the client
* administrative operations
* synchronous control flows

### WebSocket / Realtime

Best suited for:

* live state updates
* notifications
* streaming logs
* telemetry
* conversation progress events

The two should complement each other rather than compete.

---

## Error Handling Strategy

A mature API architecture should define a predictable error model.

Typical classes of errors include:

### Validation Errors

The request is malformed or incomplete.

### Authentication Errors

The caller could not be authenticated.

### Authorization Errors

The caller is authenticated but does not have permission.

### Domain Errors

The request is structurally valid, but the requested action cannot be completed because of domain-level conditions.

Examples:

* session not found
* project already archived
* hardware unavailable
* invalid FSM state for requested operation

### Infrastructure Errors

A dependency or runtime service failed.

Examples:

* database unavailable
* external provider timeout
* internal service failure

These categories should be represented consistently in API responses.

---

## Typical Examples

Representative HTTP API interactions in NORA may include:

* `POST /auth/login` to authenticate a user
* `GET /fsm/state` to retrieve the current operational state
* `GET /sessions/active` to retrieve the active session
* `POST /events` to inject a structured event
* `GET /projects` to list available conversational projects
* `PATCH /users/me/profile` to update user preferences
* `GET /hardware/status` to inspect hardware health
* `POST /admin/modules/restart` to trigger a protected maintenance action

These are examples of the kind of contract this submodule provides, not a fixed final route design.

---

## Internal Architectural Implications

Even at the documentation level, defining the HTTP API submodule implies several implementation-facing architectural choices.

The system will likely require:

* route modules grouped by domain
* request and response schemas
* authentication middleware
* authorization guards
* service injection patterns
* standardized error handlers
* audit logging hooks for sensitive endpoints
* API versioning or compatibility strategy

These implications help keep the future implementation aligned with the architectural model.

---

## Architectural Importance

The HTTP API is one of the most visible and strategically important submodules in the Backend and Application layer.

It is the formal gateway through which NORA becomes:

* accessible from the frontend
* controllable from external systems
* inspectable by admin tools
* integrable with broader software ecosystems

Without a clear HTTP API, NORA would lack a stable software surface for controlled interaction and operational integration.

With it, the system gains:

* structured access
* interoperability
* modular client integration
* secure operational boundaries
* a maintainable contract between internals and externals

For that reason, the HTTP API should be treated as a first-class architectural interface of the whole platform.

# 8.2 WebSocket / Realtime

## Definition

The **WebSocket / Realtime** submodule provides the communication infrastructure that allows NORA to stream live information, events, and state updates to connected clients without requiring repeated request-response cycles.

Unlike the HTTP API, which is based on synchronous request-response interactions, the realtime layer enables **persistent bidirectional communication channels** between the system and external clients such as the web frontend, monitoring tools, or administrative interfaces.

Through these channels, NORA can continuously broadcast operational information, notify clients about events as they occur, and synchronize the state of the system with remote interfaces in real time.

This capability is essential for interactive systems where many events occur asynchronously and where users need to observe system behaviour live.

---

## Architectural Purpose

The purpose of the WebSocket / Realtime subsystem is to support **continuous, low-latency communication between the backend and connected clients**.

NORA is an embodied, event-driven system where state changes frequently:

* the FSM transitions between states
* sensors produce new information
* actions are executed
* conversations progress
* hardware status changes
* events are emitted

Polling the HTTP API for these changes would be inefficient and would introduce unnecessary latency.

The realtime subsystem solves this by allowing the backend to **push updates to clients immediately when they occur**.

This design enables responsive interfaces and accurate operational monitoring.

---

## Role in the Global Architecture

Within the overall architecture, the WebSocket / Realtime layer acts as the **live communication channel** between the system runtime and external observers or controllers.

Conceptually, the communication flow may be represented as:

**Internal Event / State Change → Realtime Channel → Connected Client**

Clients connected to this channel may include:

* the web frontend
* the administrative dashboard
* monitoring systems
* developer debugging tools
* remote interfaces

These clients subscribe to realtime streams and receive updates whenever relevant changes occur.

---

## Why Realtime Communication Is Necessary in NORA

A system like NORA performs many operations that evolve over time rather than completing instantly.

Examples include:

* conversation exchanges
* FSM state transitions
* long-running actions
* sensor updates
* perception events
* hardware status monitoring
* media playback

Users and administrators often need to **observe these changes as they happen**.

For example:

* the frontend may display the current FSM state
* a developer may watch event flows during debugging
* the interface may show conversation progress live
* the admin panel may display system logs in real time

Without realtime communication, these interfaces would require frequent polling, which increases server load and reduces responsiveness.

The realtime subsystem therefore provides an efficient solution for streaming dynamic information.

---

## Scope of the Submodule

The WebSocket / Realtime submodule includes the infrastructure responsible for **persistent bidirectional communication and live event streaming**.

Its scope includes:

* WebSocket connection handling
* client session tracking
* event broadcasting
* state update streaming
* message routing to connected clients
* subscription management
* realtime authentication enforcement

Its scope does **not** include:

* the definition of domain events themselves
* internal behavioural logic of the FSM
* application service implementation
* storage of events or logs

Instead, the subsystem focuses on **transporting realtime information between the backend and external clients**.

---

## Core Responsibilities

The realtime subsystem performs several important operational responsibilities.

### Connection Management

The system must manage persistent connections with multiple clients simultaneously.

This includes:

* establishing WebSocket connections
* authenticating the connection
* tracking active connections
* managing connection lifecycles
* handling disconnections

Because NORA may have multiple dashboards or interfaces connected at the same time, the system must support concurrent clients reliably.

### State Broadcasting

One of the most common realtime tasks is broadcasting system state updates.

Examples include:

* FSM state transitions
* active session updates
* current emotional state
* hardware status

Whenever these states change, the backend can broadcast updates so connected interfaces remain synchronized.

### Event Streaming

Realtime channels allow the system to stream events as they occur.

Examples include:

* perception events
* planner decisions
* action executions
* warnings or alerts

This makes it possible to observe system activity live without waiting for logs or manual queries.

### Notification Delivery

The realtime subsystem can deliver immediate notifications to clients.

Examples include:

* interaction alerts
* task completion messages
* administrative warnings
* system notifications

These notifications allow interfaces to respond instantly to important changes.

### Action Progress Updates

Some operations may take time to complete.

For example:

* media playback
* navigation tasks
* document scanning
* long-running agent operations

Realtime messages allow the system to send progress updates so clients can visualize ongoing activity.

---

## Typical Realtime Channels

The realtime subsystem may organize communication through several logical channels.

### FSM State Channel

Streams updates whenever the system state machine transitions between states.

Typical data may include:

* current state
* previous state
* triggering event
* timestamp

This channel allows interfaces to visualize system behaviour live.

### Notification Channel

Streams user-facing or system-facing notifications.

Examples include:

* reminders
* alerts
* completion messages

### Log Stream

Streams technical logs in real time.

This is particularly useful for:

* debugging
* monitoring
* observing event flows

### Telemetry Channel

Streams operational metrics and hardware status.

Examples include:

* CPU load
* memory usage
* sensor data
* network status

### Conversation Channel

Streams conversation updates between the user and NORA.

Examples include:

* user message received
* system response generated
* dialogue state updates

This allows chat interfaces to update instantly.

### Action Progress Channel

Streams updates about ongoing tasks or actions.

Examples include:

* media playback progress
* camera capture status
* scanning progress
* long-running agent tasks

---

## Realtime Message Structure

Messages transmitted through realtime channels should follow a consistent structure.

Typical message components may include:

* message type
* event identifier
* timestamp
* payload data
* metadata

A standardized message structure simplifies frontend integration and debugging.

---

## Authentication and Security

Realtime channels must respect the same trust model defined in the Identity and Security architecture.

Typical requirements include:

* validating authentication tokens during connection
* verifying permissions for channel subscriptions
* isolating user-specific streams
* protecting administrative channels

Unauthorized clients should not receive restricted system information.

---

## Relationship With the HTTP API

The HTTP API and the WebSocket / Realtime subsystem serve complementary purposes.

### HTTP API

Used for:

* retrieving resources
* performing explicit operations
* submitting commands

### Realtime Channels

Used for:

* observing system behaviour
* receiving asynchronous events
* synchronizing live interfaces

In many cases a client will use both simultaneously.

Example:

1. The frontend uses the HTTP API to request session data.
2. The frontend subscribes to a realtime channel to receive live conversation updates.

---

## Relationship With the Event System

The realtime subsystem often consumes events produced by other parts of the system.

For example:

* the FSM dispatcher may emit transition events
* perception modules may emit detection events
* application services may emit notifications

The realtime subsystem can subscribe to these internal signals and forward them to connected clients.

This makes the system transparent and observable.

---

## Typical Examples

Examples of realtime interactions in NORA include:

* the frontend receiving a live FSM state change
* an admin dashboard streaming system logs
* the chat interface receiving a new assistant message
* the monitoring panel displaying hardware telemetry
* a debugging interface observing event flows

These interactions allow interfaces to remain synchronized with the system without repeated polling.

---

## Implementation Implications

Defining this architectural component implies several implementation requirements.

The system may require:

* WebSocket server infrastructure
* connection manager components
* event broadcasting utilities
* subscription management
* message serialization logic
* integration with the logging and telemetry systems

These components should remain modular and aligned with the broader application architecture.

---

## Architectural Importance

The WebSocket / Realtime subsystem is essential for providing a responsive and transparent user experience.

Without realtime communication, many interfaces would rely on inefficient polling mechanisms and would not reflect system state accurately.

By introducing persistent communication channels, NORA gains the ability to:

* synchronize interfaces instantly
* stream system activity
* support live monitoring and debugging
* provide responsive interactive experiences

This capability is particularly important for embodied systems where behaviour evolves continuously and must be observable by users and administrators.

For these reasons, the realtime subsystem forms a fundamental part of the Backend and Applic

# 8.3 Application Services

## Definition

The **Application Services** submodule defines the layer responsible for implementing the concrete use cases of the NORA system. These services coordinate domain modules, execute application-level operations, and translate external requests or internal triggers into coherent system actions.

Within the Backend and Application architecture, Application Services act as the **operational bridge between external interfaces and the internal domain logic of the system**.

While the HTTP API exposes endpoints and the WebSocket layer distributes realtime events, Application Services perform the actual orchestration of tasks required to satisfy a request or system event.

They therefore represent the **use-case execution layer** of the platform.

---

## Architectural Purpose

The purpose of Application Services is to transform the capabilities of the system's internal domains into **structured operational behaviours**.

NORA contains many specialized architectural modules:

* identity and access management
* perception pipelines
* the cognitive core and FSM
* dialogue and session management
* planning and specialized agents
* action and expression systems
* persistence and memory

Each of these domains encapsulates specific responsibilities and internal logic.

Application Services exist to **coordinate these domains when a concrete system operation must be executed**.

For example:

* opening a conversational session
* restoring a project
* dispatching an event to the FSM
* retrieving conversation history
* synchronizing hardware state
* executing an administrative operation

These tasks require interaction between multiple modules. Application Services manage those interactions without collapsing domain boundaries.

---

## Role in the Global Architecture

Within the architecture, Application Services operate between the system interfaces and the domain modules.

Conceptually the flow can be represented as:

Client / Event / Trigger → HTTP API or Realtime Layer → Application Service → Domain Modules

This means Application Services receive validated input from interface layers and coordinate the necessary operations across the internal architecture.

They do not implement the full internal logic of domains such as perception or planning. Instead, they orchestrate those capabilities to achieve system-level outcomes.

---

## Why Application Services Are Necessary in NORA

Without a dedicated application service layer, system interfaces would have to interact directly with many internal modules.

For example, an API endpoint attempting to open a session might need to:

* validate the user
* retrieve profile information
* check permissions
* initialize a session
* update the FSM
* notify the dialogue system
* record the event in persistence

Embedding all that logic directly in API controllers would quickly create large, unmaintainable components.

Application Services solve this by providing **centralized orchestration points for use cases**.

This approach offers several benefits:

* clearer separation between transport logic and application logic
* reusable use-case implementations
* simpler interfaces
* improved testing and maintainability

---

## Scope of the Submodule

The Application Services layer includes all components responsible for executing system-level operations.

Its scope includes:

* coordinating domain modules
* executing application use cases
* interacting with persistence layers
* invoking planners or agents when required
* publishing events
* updating system state

Its scope does **not** include:

* transport protocols (handled by API or realtime layers)
* domain-specific reasoning (handled by domain modules)
* UI rendering
* hardware drivers

Application Services remain focused on **orchestration and execution of system behaviours**.

---

## Core Responsibilities

The Application Services layer performs several key responsibilities.

### Use-Case Execution

Each service represents a specific operational capability of the system.

Examples include:

* creating a user session
* loading a conversational project
* dispatching an event
* retrieving historical data
* updating user preferences

These services translate high-level requests into sequences of domain operations.

### Domain Coordination

Application Services coordinate the interaction of several domain modules during a use case.

For example:

* retrieving user information from persistence
* updating the FSM context
* triggering an action
* recording the result

The service ensures these operations occur in the correct order and context.

### Transaction Management

Some operations involve multiple data modifications.

Application Services ensure these operations remain consistent by coordinating transactions with the persistence layer.

This guarantees that partial operations do not leave the system in an inconsistent state.

### Event Publication

When a service completes an operation, it may publish events for other parts of the system.

Examples include:

* session created
* project opened
* hardware state updated
* action executed

These events may be forwarded to the event dispatcher, realtime channels, or logging systems.

### Validation of Operational Context

Although request validation occurs at the API layer, services often perform **domain-level validation**.

Examples include:

* verifying that a session is active
* confirming that a project exists
* ensuring that a device is available

This validation ensures system behaviour remains consistent with domain rules.

---

## Typical Application Services

Based on the architecture of NORA, several services may be defined.

### Event Service

Responsible for managing system events and interacting with the event dispatcher.

Typical responsibilities include:

* injecting events
* retrieving recent events
* forwarding perception events
* coordinating event flows

### Session Service

Responsible for managing interaction sessions.

Typical responsibilities include:

* creating sessions
* retrieving active sessions
* suspending sessions
* closing sessions
* restoring previous sessions

### Project Service

Responsible for managing conversational projects.

Typical responsibilities include:

* creating projects
* opening projects
* retrieving project context
* updating project information
* archiving completed projects

### Dialogue Service

Responsible for managing conversational interactions.

Typical responsibilities include:

* storing dialogue turns
* retrieving conversation history
* coordinating dialogue context
* forwarding messages to planning or agents

### User Service

Responsible for managing user entities and profiles.

Typical responsibilities include:

* retrieving user data
* updating user preferences
* linking devices
* resolving permissions

### Device Service

Responsible for interacting with hardware state through application-level operations.

Typical responsibilities include:

* retrieving device status
* updating hardware configuration
* coordinating hardware commands

### Admin Service

Responsible for high-level administrative operations.

Typical responsibilities include:

* inspecting system status
* restarting modules
* triggering maintenance tasks
* managing protected configuration

---

## Service Design Principles

Several architectural principles should guide the design of Application Services.

### Single Responsibility per Use Case

Each service method should correspond to a specific system operation.

This prevents services from becoming large monolithic components.

### Domain Independence

Application Services should coordinate domains without absorbing their internal logic.

This preserves modularity and keeps domain knowledge localized.

### Idempotent Operations When Possible

Many operations should be designed so they can be safely repeated without producing unintended side effects.

This improves robustness when dealing with retries or network issues.

### Explicit Side Effects

Services should clearly define what changes they produce in system state.

This improves traceability and debugging.

---

## Relationship With Other Backend Components

Application Services are tightly integrated with several other backend elements.

### Relationship With HTTP API

The API receives requests and forwards them to Application Services.

The services perform the operation and return results that the API formats as responses.

### Relationship With Realtime Channels

When important events occur, services may publish updates that are broadcast through realtime channels.

### Relationship With the Event Dispatcher

Some services inject events into the system via the event dispatcher, particularly when interacting with the FSM.

### Relationship With Persistence

Services frequently interact with repositories or persistence modules to store or retrieve system data.

---

## Typical Execution Example

Consider the example of opening a conversational session.

1. The client sends a request to the HTTP API.
2. The API validates authentication and request format.
3. The Session Service is invoked.
4. The service creates a session record in persistence.
5. The FSM is updated with the new interaction context.
6. A realtime notification is sent to connected clients.
7. The API returns the session information.

This flow illustrates how Application Services orchestrate several architectural components.

---

## Implementation Implications

Defining this architectural layer implies several implementation structures.

Typical elements may include:

* service classes grouped by domain
* dependency injection patterns
* repository access for persistence
* event publishing utilities
* transactional operation support

These components allow the application logic to remain modular and testable.

---

## Architectural Importance

The Application Services layer is one of the most important organizational structures in the backend architecture.

It ensures that system operations remain **structured, reusable, and independent from transport mechanisms**.

By separating interface layers from domain modules, NORA gains:

* clearer system architecture
* improved maintainability
* reusable use-case implementations
* easier testing and debugging

For these reasons, Application Services represent the operational backbone that transforms NORA's capabilities into concrete system behavio

# 8.4 Coordinators / Orchestrators

## Definition

The **Coordinators / Orchestrators** submodule defines the components responsible for supervising and coordinating complex multi-step behaviours that involve several application services, agents, or domain modules.

While Application Services execute individual use cases, Coordinators manage **higher-level operational flows that span multiple services or system subsystems**.

These components are responsible for ensuring that complex operations progress in a structured, consistent, and observable way across the architecture.

They therefore represent the **process orchestration layer** of the backend.

---

## Architectural Purpose

The purpose of Coordinators / Orchestrators is to manage **complex workflows that cannot be executed as a single isolated service operation**.

In a system such as NORA, many behaviours require the interaction of multiple subsystems. Examples include:

* a full conversational interaction cycle
* perception → interpretation → planning → action
* multi-step hardware procedures
* system initialization or shutdown
* long-running agent tasks

These workflows involve multiple services and modules that must be executed in a precise order, sometimes with conditional branching or retries.

Coordinators provide the structure that governs these interactions.

---

## Role in the Global Architecture

Within the backend architecture, Coordinators operate above individual application services.

Conceptually, the flow may be represented as:

External Request / System Event → Application Service → Coordinator → Multiple Domain Modules

Or alternatively:

System Event → Coordinator → Service Sequence → Domain Modules

This means Coordinators manage **the sequence and interaction of operations**, rather than executing domain logic themselves.

They act as the **directors of complex processes**, ensuring that each component participates correctly in the workflow.

---

## Why Coordinators Are Necessary in NORA

As the system grows, many operations naturally evolve into multi-stage workflows.

For example, consider the lifecycle of a conversational interaction:

1. perception captures user input
2. interpretation extracts meaning
3. the planner decides the next action
4. an agent generates a response
5. the action module executes output
6. the dialogue history is updated

Embedding this entire workflow inside a single service would create a monolithic and fragile implementation.

Instead, Coordinators allow the system to keep services focused on specific operations while orchestrating their interaction at a higher level.

This improves:

* modularity
* maintainability
* observability of workflows
* extensibility of system behaviour

---

## Scope of the Submodule

The Coordinators / Orchestrators submodule includes components responsible for **managing structured workflows and system processes**.

Its scope includes:

* orchestrating multi-step workflows
* coordinating multiple application services
* supervising long-running processes
* handling workflow branching and control flow
* managing retries or failure recovery
* publishing workflow state updates

Its scope does **not** include:

* transport protocols
* domain-specific reasoning
* low-level service operations

Instead, the focus is on **process-level coordination across the architecture**.

---

## Core Responsibilities

The orchestrator layer performs several key responsibilities.

### Workflow Coordination

The primary responsibility of a coordinator is managing the sequence of operations required for a complex system behaviour.

For example:

* triggering perception
* forwarding interpreted data
* invoking planners
* executing actions

The coordinator ensures each step occurs in the correct order.

### State Supervision

Many workflows involve intermediate states.

The coordinator tracks the progression of the process and ensures that the system transitions correctly between stages.

### Conditional Branching

Not all workflows follow a single linear path.

Coordinators may introduce branching behaviour based on results produced by services or agents.

For example:

* retry an operation if perception fails
* choose a different agent based on intent
* trigger a fallback action

### Failure Handling

Complex operations may encounter failures.

Coordinators can implement recovery strategies such as:

* retries
* fallback operations
* graceful cancellation

### Progress Reporting

Long-running processes often need to report their progress.

The coordinator may publish updates to realtime channels or logs so interfaces can track system activity.

---

## Typical Coordinators in NORA

Several orchestration components may exist depending on the system architecture.

### Interaction Coordinator

Responsible for managing the full lifecycle of a user interaction.

Typical responsibilities include:

* receiving interpreted user input
* invoking the planner
* selecting agents
* generating responses
* triggering actions

### Perception Pipeline Coordinator

Responsible for supervising perception pipelines.

Typical responsibilities include:

* receiving sensor input
* invoking detection modules
* forwarding interpreted signals

### Action Execution Coordinator

Responsible for supervising complex physical or digital actions.

Examples include:

* camera capture workflows
* hardware sequences
* multi-step output actions

### System Lifecycle Coordinator

Responsible for managing global system procedures.

Examples include:

* system initialization
* module startup
* graceful shutdown
* recovery procedures

### Task Execution Coordinator

Responsible for supervising long-running tasks initiated by planners or agents.

Examples include:

* document analysis
* media processing
* background reasoning tasks

---

## Orchestration vs Service Logic

It is important to distinguish the responsibilities of coordinators and application services.

### Application Services

* implement individual operations
* interact with domain modules
* execute atomic use cases

### Coordinators

* combine multiple services
* manage multi-step workflows
* supervise system processes

This separation prevents services from becoming large, complex modules responsible for both logic and process control.

---

## Relationship With the FSM

The FSM in the Cognitive Core defines the allowed states and transitions of the system.

Coordinators may interact with the FSM in several ways:

* triggering events
* observing state transitions
* adapting workflows based on system state

This interaction ensures that orchestrated behaviours remain consistent with the system's operational model.

---

## Relationship With Realtime Channels

Coordinators frequently publish progress updates to realtime channels.

Examples include:

* interaction progress
* task execution updates
* workflow state changes

This allows interfaces to visualize the progress of complex operations.

---

## Example Workflow

Consider the execution of a conversational response:

1. A perception event is emitted.
2. The Interaction Coordinator receives the interpreted input.
3. The planner determines the appropriate response strategy.
4. An agent generates a response.
5. The Action module performs speech synthesis.
6. Dialogue history is updated.
7. A realtime update is broadcast to clients.

The coordinator supervises this entire sequence.

---

## Implementation Implications

Defining coordinators in the architecture implies several implementation structures.

Possible components may include:

* workflow managers
* orchestration classes
* asynchronous task supervisors
* process state trackers
* retry management utilities

These components enable reliable coordination across complex system behaviours.

---

## Architectural Importance

The Coordinators / Orchestrators layer is essential for maintaining clarity and control in a system composed of many interacting modules.

Without orchestration components, complex workflows would be distributed across multiple services in ways that are difficult to understand and maintain.

By introducing a dedicated orchestration layer, NORA gains:

* clearer workflow management
* improved modularity
* structured process supervision
* better observability of system behaviour

This makes the system easier to ex

# 8.5 Event Dispatcher

## Definition

The **Event Dispatcher** is the subsystem responsible for receiving, routing, and distributing events across the internal components of NORA.

NORA operates as an **event-driven architecture**, where many actions and state transitions are triggered by events produced by different modules such as perception systems, dialogue systems, planners, hardware interfaces, or external clients.

The Event Dispatcher acts as the **central event routing mechanism** that ensures these signals are delivered to the appropriate modules without creating direct dependencies between them.

This subsystem therefore enables **decoupled communication between components** throughout the architecture.

---

## Architectural Purpose

The purpose of the Event Dispatcher is to provide a structured mechanism for propagating events through the system in a controlled and observable manner.

In a complex architecture like NORA, multiple modules may produce events, including:

* perception detections
* user input signals
* planner decisions
* hardware updates
* dialogue events
* FSM triggers

Without a dispatcher, these modules would need to communicate directly with each other, producing a tightly coupled architecture that would be difficult to maintain.

The Event Dispatcher introduces an intermediary that allows modules to **emit events without knowing which components will consume them**.

This decoupling greatly improves scalability and modularity.

---

## Role in the Global Architecture

Within the backend architecture, the Event Dispatcher acts as the **central routing hub for system events**.

Conceptually, event propagation may follow this structure:

Event Source → Event Dispatcher → Event Consumers

Event sources may include:

* perception modules
* the HTTP API
* hardware drivers
* application services
* coordinators

Event consumers may include:

* the FSM
* application services
* orchestrators
* logging systems
* realtime channels

The dispatcher ensures that each event is delivered to the correct consumers.

---

## Why an Event Dispatcher Is Necessary

In systems where many components interact, direct communication paths quickly become complex and fragile.

For example, a perception module detecting speech might need to notify:

* the dialogue system
* the planner
* the FSM
* the logging subsystem
* the realtime monitoring interface

If each of these connections were implemented directly, the perception module would need to know about every consumer.

This would violate modularity and make the architecture difficult to extend.

By introducing an Event Dispatcher, modules only need to **emit events**, while the dispatcher determines where they should be routed.

This simplifies both producers and consumers.

---

## Scope of the Submodule

The Event Dispatcher subsystem includes all infrastructure required to manage event distribution within the backend.

Its scope includes:

* receiving emitted events
* validating event structure
* routing events to subscribed handlers
* managing event subscriptions
* publishing events to realtime channels
* forwarding events to logging systems

Its scope does **not** include:

* implementing event business logic
* defining domain rules
* storing persistent event histories

Instead, the dispatcher focuses purely on **event routing and propagation**.

---

## Core Responsibilities

The Event Dispatcher performs several critical functions.

### Event Reception

The dispatcher receives events generated by any part of the system.

Events may originate from:

* internal modules
* API endpoints
* perception systems
* hardware signals

Once received, the dispatcher begins the routing process.

### Event Validation

Before routing an event, the dispatcher may verify that the event structure is valid.

This includes checking:

* event type
* payload structure
* required metadata

This prevents malformed events from propagating through the system.

### Event Routing

The dispatcher determines which components should receive the event.

Routing may depend on:

* event type
* subscription rules
* system state

Multiple consumers may receive the same event.

### Event Broadcasting

Some events must be broadcast to multiple parts of the system.

For example:

* FSM triggers
* perception signals
* hardware alerts

The dispatcher ensures all registered consumers receive the event.

### Event Logging

The dispatcher may also forward events to logging systems or persistence layers so that system behaviour can be audited or analyzed.

### Event Forwarding to Realtime Channels

Certain events may also be forwarded to the realtime subsystem so that connected clients can observe system behaviour.

---

## Event Structure

To maintain consistency across the system, events should follow a standardized structure.

Typical event fields may include:

* event identifier
* event type
* timestamp
* event source
* payload data
* metadata

This structure ensures that any component receiving the event can interpret it correctly.

---

## Event Types

NORA may produce several categories of events.

### Interaction Events

Generated during user interaction with the system.

Examples include:

* speech detected
* user command recognized
* dialogue turn created

### System Events

Generated by internal system behaviour.

Examples include:

* FSM transition
* session started
* project loaded

### Hardware Events

Generated by hardware devices.

Examples include:

* camera activated
* microphone input detected
* battery status update

### Administrative Events

Generated by administrative operations.

Examples include:

* configuration updated
* module restarted

---

## Relationship With the FSM

One of the most important consumers of events in the system is the **Finite State Machine (FSM)** defined in the Cognitive Core.

Many events emitted by perception systems, services, or external interfaces may trigger state transitions in the FSM.

The dispatcher therefore acts as the bridge that forwards relevant events to the FSM controller.

This allows the FSM to react to system signals without directly coupling to event producers.

---

## Relationship With Application Services

Application services may both emit and consume events.

For example:

* a service may emit an event after completing a task
* another service may subscribe to that event to trigger additional behaviour

The dispatcher ensures that these interactions remain loosely coupled.

---

## Relationship With Realtime Channels

Some events may be visible to external observers.

The dispatcher may forward selected events to the realtime subsystem so that:

* the frontend can observe system behaviour
* administrators can monitor activity
* debugging tools can inspect event flows

---

## Example Event Flow

Consider a typical interaction scenario.

1. The microphone detects speech input.
2. The perception module emits a speech_detected event.
3. The Event Dispatcher receives the event.
4. The dispatcher forwards the event to the dialogue module.
5. The dispatcher forwards the event to the FSM.
6. The dispatcher logs the event.
7. The dispatcher publishes a notification to the realtime channel.

This sequence demonstrates how a single event may trigger multiple system responses.

---

## Implementation Implications

Defining an Event Dispatcher suggests several implementation components.

Possible structures may include:

* event bus implementations
* event handler registries
* subscription management
* event serialization utilities
* event logging hooks

These structures allow the dispatcher to manage event propagation efficiently.

---

## Architectural Importance

The Event Dispatcher is a fundamental mechanism that supports the event-driven architecture of NORA.

Without such a component, modules would need to communicate directly with one another, resulting in a complex network of dependencies.

By introducing a centralized event routing mechanism, NORA gains:

* decoupled module communication
* scalable event propagation
* improved observability
* easier extension of system behaviour

For these reasons, the Event Dispatcher plays a critical role in enabling modular and flexible system design.

# 8.6 Observability

## Definition

The **Observability subsystem** provides the infrastructure that allows the internal behaviour, health, and runtime state of NORA to be inspected, monitored, and diagnosed during operation.

In a complex event-driven system composed of many interacting modules—such as perception pipelines, planning systems, application services, realtime channels, and hardware interfaces—it is not sufficient to rely on simple debugging or manual inspection.

Observability enables the system to expose structured operational information that allows engineers and operators to understand:

* what the system is doing
* how different modules interact
* when events occur
* why specific behaviours emerge

This information is collected continuously and can be analyzed in order to detect problems, diagnose failures, evaluate performance, and understand system behaviour.

---

## Architectural Purpose

The purpose of the Observability subsystem is to ensure that NORA remains **transparent, diagnosable, and operable in real-world conditions**.

Because NORA performs many asynchronous operations—such as event dispatching, realtime communication, planning workflows, and hardware interaction—it must be possible to observe what is happening inside the system at any moment.

Observability therefore provides the mechanisms required to:

* monitor system health
* analyze operational performance
* detect abnormal behaviour
* trace complex workflows
* diagnose failures

Without observability, diagnosing issues in such a distributed and event-driven architecture would be extremely difficult.

---

## Role in the Global Architecture

Within the global architecture of NORA, the Observability subsystem acts as the **system-wide monitoring and diagnostic layer**.

Rather than belonging to a single module, observability operates across the entire system and collects operational signals from many components.

Conceptually the architecture may be represented as:

System Components → Observability Collectors → Monitoring and Analysis Interfaces

System components that generate observability data include:

* HTTP API layer
* WebSocket / realtime layer
* application services
* coordinators and orchestrators
* the event dispatcher
* the FSM in the Cognitive Core
* perception pipelines
* hardware interfaces

Observability tools collect this information and make it accessible through logs, dashboards, or monitoring systems.

---

## Why Observability Is Necessary in NORA

NORA operates as a **distributed, asynchronous, event-driven system**. Many operations occur simultaneously and interact with one another.

Examples include:

* perception modules processing sensor input
* events being routed by the event dispatcher
* FSM state transitions
* planner decisions
* agent execution
* realtime message broadcasting

When unexpected behaviour occurs, engineers must be able to determine:

* which event triggered the behaviour
* which module executed the operation
* how long the operation took
* which component produced an error

Observability provides the infrastructure necessary to answer these questions.

---

## Scope of the Submodule

The Observability subsystem includes the infrastructure required to monitor **system behaviour and operational health**.

Its scope includes:

* system logging
* metrics collection
* distributed tracing
* runtime diagnostics
* monitoring dashboards
* alerting mechanisms

Its scope does **not** include:

* domain-level decision logic
* application workflows
* business rules
* persistence of application data unrelated to monitoring

Instead, it focuses exclusively on **exposing operational insight into system behaviour**.

---

## Core Observability Signals

Observability typically relies on three primary categories of telemetry data: **logs, metrics, and traces**.

### Logging

Logs capture discrete events that occur during system execution.

Examples include:

* API requests
* FSM state transitions
* event emissions
* application service execution
* error messages
* warnings and system alerts

Logs allow engineers to reconstruct system behaviour over time and understand what happened before a failure occurred.

Structured logging formats are typically used so that logs can be filtered, searched, and analyzed automatically.

---

### Metrics

Metrics provide quantitative measurements that describe system performance and operational health.

Examples include:

* CPU utilization
* memory usage
* request latency
* number of active sessions
* event throughput
* hardware telemetry

Metrics are useful for detecting performance degradation, capacity limitations, and abnormal operational patterns.

Metrics are typically collected continuously and visualized through monitoring dashboards.

---

### Distributed Tracing

Tracing records the lifecycle of operations as they propagate through multiple system components.

For example, a single user interaction may involve:

1. an HTTP API request
2. an application service
3. a coordinator
4. the FSM
5. an action module
6. a realtime notification

Tracing allows engineers to observe the **complete path of such operations**, making it easier to identify performance bottlenecks or failures.

---

## Sources of Observability Data

Many components within the architecture contribute information to the observability subsystem.

### HTTP API Layer

The API layer may emit logs and metrics describing:

* incoming requests
* authentication failures
* response times
* HTTP status codes

---

### Event Dispatcher

The event system may produce logs describing:

* event emissions
* routing decisions
* event processing outcomes

This allows engineers to inspect how events propagate through the architecture.

---

### Application Services

Application services may log operational activities such as:

* session creation
* project loading
* task execution
* configuration changes

---

### FSM (Cognitive Core)

The FSM may emit logs and metrics describing:

* state transitions
* triggering events
* system modes

These signals are particularly useful when analyzing system behaviour.

---

### Hardware Interfaces

Hardware modules may emit telemetry describing:

* sensor activity
* device connectivity
* hardware errors
* performance measurements

---

## Monitoring and Visualization

Observability data is typically aggregated and presented through monitoring dashboards or analysis tools.

These interfaces may display:

* system health indicators
* performance metrics
* recent events
* error rates
* hardware status

Monitoring dashboards allow administrators and developers to quickly understand the operational status of the system.

---

## Alerting

Observability systems often include alerting mechanisms that notify operators when abnormal conditions occur.

Examples of alert conditions include:

* repeated service failures
* unusually high latency
* hardware disconnection
* excessive error rates
* unexpected FSM behaviour

Alerts allow operators to respond quickly and maintain system stability.

---

## Relationship With Other Backend Components

Observability interacts with nearly every part of the backend architecture.

### Application Services

Application services generate logs and metrics describing system operations.

### Coordinators / Orchestrators

Coordinators may emit traces describing the progress of complex workflows.

### Event Dispatcher

The dispatcher may log event propagation and routing behaviour.

### Realtime Channels

Certain observability information may also be streamed to debugging interfaces via realtime channels.

---

## Implementation Implications

Implementing observability typically requires several supporting components.

Possible implementation elements include:

* structured logging frameworks
* metrics collectors
* tracing instrumentation
* log aggregation systems
* monitoring dashboards
* alerting infrastructure

These components allow system behaviour to be inspected and analyzed effectively.

---

## Architectural Importance

Observability is a **fundamental capability for operating complex software systems**.

Without structured observability mechanisms, diagnosing failures in a distributed event-driven architecture like NORA would be extremely difficult.

By incorporating a dedicated observability subsystem, NORA gains:

* transparency of internal operations
* faster debugging and diagnostics
* performance monitoring
* improved operational reliability

For these reasons, observability forms a critical part of the Backend and Application architecture.
