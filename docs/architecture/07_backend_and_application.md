# 8. Backend and Application

## Definition

The Backend and Application module is the architectural layer that exposes NORA as an executable software system and coordinates the runtime interaction between its internal domains, external interfaces, and execution infrastructure.

This module defines the application structures through which the architecture becomes operationally accessible, internally coordinated, and externally observable.

The Backend and Application module introduces several architectural elements:

* an application boundary
* an application endpoint
* an application service
* an orchestration flow
* an event ingress path
* a realtime distribution channel
* an operational observability surface

An application boundary is the software boundary through which external clients, interfaces, or services access NORA.

An application endpoint is a structured entry point through which a request, command, or query enters the system.

An application service is a software component responsible for executing an application-level use case by coordinating multiple architectural domains.

An orchestration flow is a structured runtime interaction in which several domains participate in a coordinated operation.

An event ingress path is the standardized path through which operational events enter the behavioural core of the system.

A realtime distribution channel is a communication structure through which changing runtime state is propagated to observing clients.

An operational observability surface is the structured exposure of logs, traces, metrics, and runtime diagnostics.

Together, these elements define the Backend and Application module as the layer where architectural capabilities become operational application behaviour.

## Architectural Purpose

The purpose of the Backend and Application module is to transform the architectural capabilities of NORA into a coherent and operable software system.

NORA contains multiple architectural domains:

* perception
* dialogue and session management
* planning and specialized agents
* action and expression
* persistence and memory
* identity and access control
* frontend interaction interfaces
* hardware and external integrations

These domains represent capabilities of the system but they do not define how those capabilities are accessed or coordinated at runtime.

The Backend and Application module defines the operational structures that allow these domains to participate in system-level behaviour.

These structures include:

* application access points
* service-level use cases
* runtime orchestration flows
* event routing mechanisms
* realtime state propagation
* technical observability structures

Through these structures the architecture becomes runnable, inspectable, and externally accessible.

## Architectural Role

Within the global NORA architecture the Backend and Application module operates as the coordination layer between external interfaces and internal system behaviour.

Conceptually the architecture can be represented as:

External Interfaces / Frontend Clients / External Systems ↔ Backend and Application ↔ Internal Architectural Domains

External interaction requests enter the system through backend endpoints.

Application services translate those requests into structured operations.

Orchestration flows coordinate domain participation.

Runtime state changes are propagated through realtime channels.

Operational activity is recorded through observability structures.

Through these mechanisms the Backend and Application module acts as the operational coordination layer of the architecture.

## Structural Necessity

NORA is a distributed architectural system composed of multiple specialized domains.

These domains have different responsibilities:

* perception processes environmental input
* the cognitive core maintains behavioural state
* planners generate execution strategies
* dialogue systems maintain conversational continuity
* persistence systems store durable information
* action modules perform outputs and control operations

Direct coupling between all domains would produce a system that is difficult to maintain, inspect, or evolve.

The Backend and Application module introduces a structured coordination layer that defines how domains interact during runtime operations.

This layer defines:

* how requests enter the system
* how use cases are executed
* how domain services are invoked
* how events propagate
* how runtime state is exposed
* how operational activity is observed

Through this layer the architecture becomes operationally coherent.

## Scope of the Module

The Backend and Application module includes the software structures responsible for application orchestration, runtime coordination, and system exposure.

The module contains:

* application endpoints
* request processing structures
* realtime communication channels
* application services
* orchestration coordinators
* event ingress mechanisms
* runtime observability systems

The module does not include:

* sensor processing pipelines
* semantic interpretation logic
* internal behavioural modelling of the FSM
* physical device control implementation
* frontend rendering logic
* storage engine implementation

Those responsibilities belong to other modules in the architecture.

The Backend and Application module coordinates these domains but does not replace them.

## Core Architectural Responsibilities

The module performs several structural responsibilities inside the architecture.

### Application Exposure

The module defines the software interfaces through which the system becomes accessible.

Application exposure structures include:

* HTTP APIs
* realtime communication channels
* administrative endpoints
* configuration interfaces
* integration access points

These interfaces form the controlled access surface of the system.

### Use Case Execution

The module defines application services responsible for executing system use cases.

A use case represents a structured system operation such as:

* creating a session
* restoring a conversational project
* dispatching an event
* updating a user context
* triggering a hardware action
* executing an administrative operation

Application services coordinate the domain logic required to complete these operations.

### Domain Coordination

The module coordinates interactions between architectural domains.

A domain coordination flow may include interactions such as:

* perception results entering the dispatcher
* FSM transitions triggering state updates
* planner outputs triggering action requests
* session state updates synchronizing frontend clients

These flows are implemented through orchestration structures that preserve domain separation.

### Event Routing

The module defines the standardized pathways through which events enter the behavioural core of the system.

Event ingress mechanisms receive events originating from:

* frontend commands
* perception pipelines
* backend processes
* external integrations

These events are normalized and routed toward the event dispatcher and control architecture.

### Realtime State Distribution

The module distributes live runtime information through realtime communication channels.

Realtime state propagation may include:

* FSM state updates
* conversation progress
* action execution progress
* technical notifications
* telemetry streams
* hardware status

Realtime distribution keeps observing clients synchronized with the running system.

### Operational Observability

The module provides structured visibility into runtime system behaviour.

Observability structures include:

* logs
* traces
* metrics
* error reports
* runtime diagnostics

These mechanisms allow the system to be monitored, inspected, and debugged during operation.

## Relationship With Other Modules

The Backend and Application module interacts with most architectural domains of NORA.

### Identity, Access and Security

Backend entry points operate as protected access surfaces.

Authentication and authorization determine which identities may access which operations.

Security policies regulate execution permissions and access control.

### Interaction Interfaces and Frontend

Frontend interfaces communicate with the system through backend APIs and realtime channels.

The backend therefore acts as the operational gateway between user-facing clients and internal domain services.

### Perception

Perception pipelines produce structured outputs that may generate events or state changes.

The backend routes these outputs into application flows or the event dispatch system.

### Cognitive Core

The cognitive core maintains behavioural state.

Backend mechanisms expose behavioural state to clients and provide the operational pathways through which events reach the FSM.

### Dialogue and Session System

Sessions, conversational projects, and dialogue state are created, updated, and retrieved through backend services.

These services expose dialogue structures as operational system features.

### Planning, Interpretation and Agents

Application use cases may invoke planners and specialized agents as part of larger operational flows.

The backend coordinates these invocations while reasoning remains inside the planning architecture.

### Action and Expression

Once execution decisions are produced, the backend coordinates the propagation of these actions toward output channels and records their operational state.

### Persistence and Memory

Persistent data such as users, sessions, projects, logs, and configuration values are accessed through backend services.

Persistence modules store this information while backend services coordinate operational access.

## Internal Structure

The Backend and Application module is composed of several submodules.

### 8.1 HTTP API

Defines the request–response interface through which structured client and service requests access NORA.

### 8.2 WebSocket / Realtime

Defines the live communication channels through which runtime state updates and notifications are propagated.

### 8.3 Application Services

Defines the service layer responsible for executing application-level use cases.

### 8.4 Coordinators / Orchestrators

Defines runtime coordination components that connect architectural domains during composite operations.

### 8.5 Event Dispatcher

Defines the standardized entry point through which operational events enter the behavioural control architecture.

### 8.6 Observability

Defines the technical supervision layer responsible for logs, traces, metrics, and runtime diagnostics.

Together these submodules transform the architectural capabilities of NORA into a coherent running system.

## Architectural Importance

The Backend and Application module provides the operational structure that binds together the rest of the architecture.

Without this module the system would consist of isolated capabilities without a coordinated execution environment.

Through this module the architecture gains:

* controlled application access surfaces
* coordinated system use cases
* structured event propagation
* realtime runtime visibility
* cross-domain orchestration
* operational observability

The Backend and Application module therefore represents the layer that allows NORA to function as an integrated software platform rather than a collection of independent subsystems.

# 8.1 HTTP API

## Definition

The HTTP API is the request-response interface through which frontend clients, administrative interfaces, remote systems, and external services communicate with NORA using structured network requests.

Within the Backend and Application module, the HTTP API defines the formal synchronous access surface of the system.

This submodule introduces the architectural elements through which external software interaction becomes explicit, controlled, and interoperable.

The HTTP API introduces the following architectural elements:

* an API boundary
* an endpoint
* a route
* a request model
* a response model
* a transport contract
* an authentication boundary
* an authorization boundary
* an error model
* an API resource surface
* an API use-case surface

An API boundary is the formal software boundary through which external clients access application capabilities.

An endpoint is a specific externally accessible operation exposed through the API.

A route is the transport-level address through which an endpoint is reached.

A request model is the structured representation of the input accepted by an endpoint.

A response model is the structured representation of the output returned by an endpoint.

A transport contract is the explicit definition of how a client communicates with the system through requests and responses.

An authentication boundary is the point at which the identity of the caller is resolved and validated.

An authorization boundary is the point at which the system determines whether the caller is allowed to perform the requested operation.

An error model is the structured representation of failure conditions exposed by the API.

An API resource surface is the part of the API that exposes system entities such as users, sessions, projects, configuration objects, or system state representations.

An API use-case surface is the part of the API that exposes explicit operations such as login, dispatch event, restart module, recover session, or execute maintenance action.

Together, these elements define the HTTP API as the architectural submodule that exposes NORA through a formal synchronous software contract.

## Architectural Purpose

The purpose of the HTTP API is to provide the explicit network contract through which NORA is accessed, queried, controlled, and integrated by external software actors.

NORA contains many possible software consumers:

* the web frontend
* administrative interfaces
* remote control dashboards
* companion device interfaces
* integration middleware
* automation systems
* external services
* internal networked components

These actors interact with NORA as clients of the system.

The HTTP API defines the software structures through which that interaction occurs.

The submodule provides:

* structured access points
* stable request formats
* stable response formats
* explicit operation boundaries
* machine-readable system contracts
* interoperable network exposure
* controlled access to application capabilities

Through these structures, NORA becomes operable as a network-accessible software platform while preserving the separation between external clients and internal domain implementation.

## Architectural Role

Within the global architecture, the HTTP API acts as the request-response boundary layer between external consumers and internal application coordination.

Its architectural position can be represented as:

Client / External Service / Admin Interface → HTTP API → Application Service / Coordinator / Dispatcher → Internal Domains

This means the HTTP API performs the following structural role:

* it receives external requests
* it resolves the target endpoint
* it validates the request structure
* it resolves caller identity when required
* it enforces access restrictions
* it delegates the requested operation to the corresponding application component
* it formats the resulting output into a structured response

The HTTP API therefore acts as the formal synchronous gateway of NORA.

It is not the location of the full internal logic of the platform.

It is the interface layer through which internal application capabilities are exposed as stable software operations.

## Structural Necessity

NORA is a cognitive and operational system that must be accessed from outside its internal runtime.

External software actors need to:

* retrieve system state
* create and manage sessions
* access projects
* authenticate identities
* inspect configuration
* inspect hardware state
* trigger operational commands
* invoke administrative actions
* integrate external workflows

Without a formal API layer, these interactions would depend on direct internal coupling, custom non-standard interfaces, or uncontrolled access to internal resources.

That would remove architectural boundaries between clients and system internals.

The HTTP API exists because NORA requires:

* a formal request-response contract
* explicit operation entry points
* controlled transport-level access
* machine-readable integration surfaces
* stable client-facing interfaces
* clear separation between external consumers and internal application logic

The HTTP API is therefore a structural necessity of the backend architecture.

## Scope of the Submodule

The HTTP API submodule contains the software structures responsible for exposing, validating, securing, and handling synchronous request-response operations.

Its scope includes:

* route definitions
* endpoint definitions
* request parsing
* request validation
* request normalization
* response construction
* response normalization
* authentication checks at the API boundary
* authorization enforcement at exposed operations
* delegation to application services
* delegation to coordinators
* delegation to event dispatch entry points
* transport-level conventions
* API error representation
* versioned or grouped endpoint organization

The submodule does not include:

* realtime bidirectional streaming channels
* internal behavioural logic of the FSM
* semantic interpretation logic
* planning logic
* direct hardware control implementation
* persistence engine implementation
* frontend rendering logic
* low-level infrastructure provisioning

These responsibilities belong to other submodules or modules.

The HTTP API exposes and coordinates access to those domains without replacing their internal logic.

## Core Architectural Responsibilities

The HTTP API performs several structural responsibilities inside the Backend and Application module.

### 1. Endpoint Exposure

The HTTP API exposes a structured set of externally accessible operations.

An exposed endpoint is a defined access point through which a client performs a read, write, action, or inspection operation over the system.

Endpoint exposure includes:

* resource retrieval endpoints
* resource update endpoints
* resource creation endpoints
* controlled action endpoints
* inspection endpoints
* administrative endpoints
* integration endpoints
* health or status endpoints

This endpoint surface defines how NORA is externally usable.

### 2. Request Interpretation and Validation

The HTTP API receives transport-level requests and transforms them into validated application inputs.

Request handling includes:

* route matching
* method interpretation
* parameter extraction
* body parsing
* schema validation
* file or payload handling
* header inspection
* query parsing
* required-field verification
* type validation
* structural normalization

This responsibility defines what a valid API request is and prevents malformed inputs from entering deeper application layers.

### 3. Access Boundary Enforcement

The HTTP API is one of the primary trust boundaries of the architecture.

At this boundary, the system resolves whether the caller is known, authenticated, and authorized to perform the requested operation.

This includes:

* caller identification
* credential validation
* token validation
* session-bound identity resolution
* permission checks
* role checks
* protected endpoint restriction
* sensitive operation gating

The trust model is defined elsewhere in the architecture, but the HTTP API is one of the principal points where that model becomes operational.

### 4. Delegation to Application Components

The HTTP API does not own the full internal logic of the use cases it exposes.

Instead, it delegates the requested operation to the corresponding backend component.

Delegation targets include:

* application services
* orchestration coordinators
* event dispatcher entry points
* domain-specific execution handlers

This delegation preserves the separation between interface exposure and application execution.

### 5. Structured Response Construction

The HTTP API returns structured responses that represent the result of the requested operation.

A response structure may contain:

* entity data
* collection data
* operation result objects
* acknowledgement objects
* state snapshots
* validation failures
* permission failures
* domain-level failure information
* dependency failure information

This responsibility defines how clients observe the result of an interaction with NORA.

### 6. Error Normalization

The HTTP API exposes a predictable error surface.

An API error surface is the structured set of failure representations exposed to clients.

This includes normalized representation of:

* invalid request structure
* authentication failure
* authorization failure
* missing resource
* invalid operation state
* conflict conditions
* dependency unavailability
* internal failure

This normalized error structure makes client integration, debugging, and frontend behaviour consistent.

### 7. Transport-Level Contract Preservation

The HTTP API preserves consistency of the request-response contract across all endpoint groups.

This includes consistency in:

* naming conventions
* route organization
* status semantics
* response envelope patterns
* pagination patterns
* filtering conventions
* authentication expectations
* error representation
* versioning conventions

This responsibility gives the API a coherent architectural identity.

## Internal Conceptual Structure

The HTTP API is not only a list of routes.

It is a structured architectural surface composed of several conceptual layers.

### API Boundary Layer

The API boundary layer is the external software frontier of NORA.

It defines where client interaction begins.

### Routing Layer

The routing layer maps transport paths and HTTP methods to endpoint handlers.

It defines how incoming requests are directed to specific operations.

### Validation Layer

The validation layer defines which request forms are structurally valid and which are rejected.

It formalizes accepted inputs.

### Access Control Layer

The access control layer resolves identity context and enforces permissions over API operations.

It formalizes who may use which endpoint.

### Delegation Layer

The delegation layer connects endpoint handlers to application services, coordinators, or dispatch mechanisms.

It formalizes how exposed operations are executed internally.

### Response Layer

The response layer defines how successful and unsuccessful outcomes are represented to clients.

It formalizes external output representation.

Together, these layers define the internal architectural composition of the HTTP API.

## API Surface Types

The HTTP API exposes two major kinds of software surface.

### Resource Surface

A resource surface exposes system entities as accessible objects.

Examples of exposed resources include:

* users
* sessions
* projects
* configuration objects
* hardware state summaries
* event records
* diagnostic summaries

A resource-oriented endpoint allows clients to retrieve, create, update, or inspect structured system entities.

### Use-Case Surface

A use-case surface exposes explicit system operations.

Examples of exposed operations include:

* login
* logout
* recover session
* dispatch event
* restart module
* trigger maintenance action
* acknowledge notification
* execute protected hardware command

A use-case-oriented endpoint exposes an action rather than a passive entity.

The HTTP API contains both surface types.

## API Domain Organization

To preserve clarity, the HTTP API may be organized into endpoint domains.

An endpoint domain is a coherent group of routes that expose one area of the architecture.

Typical endpoint domains include the following.

### Auth

The Auth domain exposes identity-related access operations.

It may include:

* login operations
* logout operations
* token refresh operations
* current identity retrieval
* device trust registration
* authentication status inspection

### Events

The Events domain exposes event-related operations.

It may include:

* event submission
* event inspection
* recent event retrieval
* integration event forwarding
* event flow testing endpoints

### FSM

The FSM domain exposes behavioural-state inspection and controlled state operations.

It may include:

* current state retrieval
* transition history retrieval
* allowed transition inspection
* protected administrative transition operations

### Sessions

The Sessions domain exposes session lifecycle operations.

It may include:

* session creation
* active session retrieval
* session listing
* session suspension
* session closure
* session recovery

### Projects

The Projects domain exposes long-running objective and project operations.

It may include:

* project creation
* project retrieval
* project listing
* project opening
* project update
* project archival
* project completion

### Users

The Users domain exposes user-related entities and profile operations.

It may include:

* user retrieval
* current profile retrieval
* profile update
* preference update
* device association inspection
* role and permission inspection where authorized

### Admin

The Admin domain exposes privileged system control operations.

It may include:

* privileged user management
* protected log inspection
* module restart operations
* maintenance actions
* protected runtime inspection
* global configuration actions

### Hardware

The Hardware domain exposes hardware state and controlled hardware operations.

It may include:

* hardware state retrieval
* sensor availability inspection
* actuator availability inspection
* battery or power state inspection
* diagnostic retrieval
* policy-controlled manual commands

### Configuration

The Configuration domain exposes configuration inspection and configuration modification operations.

It may include:

* runtime configuration retrieval
* setting updates
* feature flag inspection
* environment-dependent behaviour inspection

These endpoint domains structure the API into understandable architectural regions.

## Request Model

A request is the structured inbound representation of an external operation.

The HTTP API request model may include:

* route parameters
* query parameters
* request body objects
* file uploads
* content type declarations
* authentication headers
* correlation identifiers
* tracing metadata
* idempotency metadata

Each request is transformed from a transport-level representation into a validated application input.

The request model therefore defines how information enters the backend.

## Response Model

A response is the structured outbound representation of the system result.

The HTTP API response model may include:

* single-entity objects
* collection objects
* paginated result sets
* operation acknowledgements
* state snapshots
* execution summaries
* validation error objects
* permission error objects
* domain failure objects
* infrastructure failure objects

The response model defines how the backend exposes the outcome of an operation to the client.

## Authentication and Authorization at the API Boundary

The HTTP API is one of the principal security-relevant surfaces of NORA.

At this boundary, the system resolves the caller identity context and determines operation eligibility.

This boundary includes:

* credential-bearing requests
* token-bearing requests
* session-bound requests
* privileged requests
* user-scoped requests
* public requests when defined

The API boundary therefore carries:

* caller identity context
* role context
* permission context
* request traceability context
* protected-operation context

This makes the HTTP API one of the primary locations where identity and security architecture become runtime behaviour.

## Relationship With Application Services

The HTTP API and the Application Services submodule are directly connected but structurally distinct.

The HTTP API defines the external contract.

Application Services define the execution logic of application-level use cases.

The relationship between both submodules can be expressed as follows:

* the HTTP API receives the request
* the HTTP API validates the input and resolves access context
* the HTTP API delegates the operation
* the Application Service performs the use-case logic
* the HTTP API formats and returns the result

This separation means that the same application service can participate in multiple access surfaces such as:

* HTTP endpoints
* WebSocket message handlers
* administrative interfaces
* internal orchestration flows
* scheduled operations

## Relationship With Realtime Channels

The HTTP API and the WebSocket / Realtime submodule expose different communication forms.

The HTTP API exposes discrete request-response interactions.

The WebSocket / Realtime submodule exposes live state propagation and streaming interactions.

The HTTP API is the appropriate surface for:

* explicit retrieval operations
* explicit update operations
* controlled command submission
* protected administrative actions
* synchronous inspection operations

The WebSocket / Realtime submodule is the appropriate surface for:

* live state updates
* notifications
* streaming telemetry
* live logs
* progress propagation
* ongoing runtime observation

Together, both submodules define the full communication surface of the backend.

## Error Model

The HTTP API defines a structured error model.

An error model is the formal classification and representation of failure conditions exposed through the API.

The error model includes several major classes.

### Validation Errors

Validation errors represent structurally invalid requests.

Examples include:

* missing required fields
* invalid parameter types
* malformed payloads
* schema violations

### Authentication Errors

Authentication errors represent failure to establish caller identity.

Examples include:

* invalid credentials
* expired tokens
* missing authentication information

### Authorization Errors

Authorization errors represent denied access after identity resolution.

Examples include:

* insufficient permissions
* forbidden administrative operation
* disallowed resource access

### Domain Errors

Domain errors represent requests that are structurally valid but impossible under current domain conditions.

Examples include:

* session not found
* project already archived
* invalid FSM state for requested action
* hardware unavailable for requested operation

### Infrastructure Errors

Infrastructure errors represent failure of supporting system dependencies.

Examples include:

* database unavailable
* dependency timeout
* downstream service failure
* internal backend failure

These classes define the external failure language of the HTTP API.

## Internal Architectural Implications

Defining the HTTP API as an architectural submodule implies a set of implementation-facing structures.

These structures include:

* route modules grouped by domain
* endpoint handlers
* request schemas
* response schemas
* authentication middleware
* authorization guards
* request context resolution
* service injection mechanisms
* standardized exception handlers
* audit logging hooks for sensitive operations
* versioning structures
* compatibility management structures

These implications are not separate from the architecture.

They are implementation consequences of the architectural definition of the submodule.

## Typical Examples

Representative HTTP API interactions in NORA include:

* an authentication request entering through an auth endpoint
* a session retrieval request entering through a sessions endpoint
* a project listing request entering through a projects endpoint
* a structured event submission entering through an events endpoint
* a state inspection request entering through an FSM endpoint
* a profile update request entering through a users endpoint
* a hardware inspection request entering through a hardware endpoint
* a protected maintenance request entering through an admin endpoint

These examples illustrate the kind of synchronous application contract exposed by the submodule.

## Architectural Importance

The HTTP API is one of the most visible and structurally important submodules of the Backend and Application module.

It is the formal synchronous gateway through which NORA becomes accessible as a software platform.

Through the HTTP API, the architecture gains:

* explicit external contracts
* controlled access boundaries
* interoperable software exposure
* structured client interaction
* reusable application access paths
* security-relevant operational boundaries
* maintainable separation between clients and internal logic

Without this submodule, NORA lacks a stable request-response surface for external interaction.

With this submodule, NORA becomes accessible, integrable, controllable, and inspectable through a formal application interface.

# 8.2 WebSocket / Realtime

## Definition

The WebSocket / Realtime submodule is the communication layer that enables persistent bidirectional channels between the backend runtime of NORA and connected external clients.

This submodule defines the architectural structures through which live system information, runtime events, and state changes are transmitted to external observers without relying on repeated request‑response interactions.

The WebSocket / Realtime submodule introduces the following architectural elements:

* a realtime communication channel
* a persistent client connection
* a connection session
* a subscription context
* a realtime message
* a broadcast stream
* a state propagation channel
* an event forwarding channel
* a realtime notification channel

A realtime communication channel is a persistent network pathway that allows the backend and the client to exchange messages continuously during an open connection.

A persistent client connection is an active transport link maintained between a client and the backend runtime.

A connection session is the runtime structure that represents one active client connection and its associated context.

A subscription context is the set of realtime streams or topics to which a connected client is currently subscribed.

A realtime message is the structured unit of information transmitted through the channel.

A broadcast stream is a realtime message flow delivered to multiple connected clients simultaneously.

A state propagation channel is a stream used to transmit updates about system state changes.

An event forwarding channel is a stream used to propagate events produced by internal system components.

A realtime notification channel is a stream used to deliver user-facing or system-facing alerts.

Together, these elements define the realtime communication architecture of NORA.

## Architectural Purpose

The purpose of the WebSocket / Realtime submodule is to expose the dynamic behaviour of the system to connected clients while the system is running.

Many operations in NORA evolve continuously rather than completing instantly.

These operations include:

* behavioural state transitions
* dialogue progression
* perception events
* action execution
* sensor updates
* system notifications
* hardware telemetry

The realtime subsystem allows the backend runtime to propagate these changes immediately to observing clients.

This design eliminates the need for repeated polling of HTTP endpoints and provides a continuous flow of operational information.

Through this mechanism, NORA exposes its evolving runtime behaviour as a live observable stream.

## Architectural Role

Within the global architecture, the WebSocket / Realtime submodule acts as the live communication bridge between the runtime system and connected external observers.

Its position in the architecture can be represented as:

Internal Event or State Change → Realtime Dispatcher → WebSocket Channel → Connected Client

The realtime subsystem therefore performs the following architectural function:

* it receives internal state changes or events
* it converts those signals into structured realtime messages
* it distributes those messages to subscribed clients

This makes the runtime behaviour of the system externally observable.

## Structural Necessity

NORA is an interactive system in which many processes evolve continuously.

Examples of evolving system behaviour include:

* FSM state transitions
* dialogue turn progression
* perception detection results
* ongoing actions
* hardware state monitoring
* telemetry updates

External interfaces frequently need to observe these behaviours in real time.

Examples include:

* user interfaces displaying system state
* administrative dashboards monitoring operation
* debugging tools observing event flows
* monitoring tools collecting telemetry

Without realtime communication, these interfaces would need to repeatedly query the HTTP API for updates.

This would increase system load and introduce latency between the occurrence of an event and its observation.

The realtime subsystem eliminates this inefficiency by allowing the backend to push updates immediately.

## Scope of the Submodule

The WebSocket / Realtime submodule contains the infrastructure responsible for persistent communication channels and live message propagation.

The submodule includes:

* connection establishment
* connection session tracking
* connection lifecycle management
* subscription tracking
* realtime message dispatch
* broadcast distribution
* channel-based routing
* connection authentication
* permission enforcement for streams

The submodule does not include:

* the definition of domain events
* behavioural state machine logic
* application service implementation
* persistent event storage
* frontend rendering logic

These responsibilities belong to other modules.

The realtime subsystem focuses exclusively on the transport and distribution of runtime information.

## Core Architectural Responsibilities

The WebSocket / Realtime subsystem performs several core responsibilities within the backend architecture.

### Connection Management

The subsystem manages persistent communication connections between clients and the backend runtime.

Connection management includes:

* accepting connection requests
* establishing persistent channels
* associating connections with identities
* tracking active connections
* maintaining connection state
* detecting disconnections
* cleaning up terminated connections

Each connected client corresponds to a connection session maintained by the system.

### Subscription Management

Connected clients may subscribe to specific streams of realtime information.

Subscription management includes:

* registering client subscriptions
* updating subscription sets
* filtering messages according to subscription context
* isolating user-specific streams

Subscriptions allow clients to receive only the streams that are relevant to their interface or function.

### Event Streaming

The realtime subsystem forwards internal events to connected clients.

Event streaming includes events such as:

* FSM transitions
* perception detections
* planner decisions
* action execution events
* system alerts

These events are converted into structured realtime messages and delivered through the corresponding channels.

### State Synchronization

The subsystem propagates updates whenever relevant system state changes occur.

Examples of propagated state include:

* behavioural state
* active session status
* dialogue state
* hardware state
* configuration changes

State synchronization ensures that remote interfaces remain consistent with the backend runtime.

### Notification Delivery

The realtime subsystem delivers notifications immediately when specific conditions occur.

Notifications may include:

* system alerts
* task completion signals
* administrative warnings
* interaction reminders

Notification streams allow interfaces to react immediately to important events.

### Action Progress Streaming

Certain operations in NORA may progress over time.

Examples include:

* long-running agent tasks
* media playback
* scanning operations
* hardware procedures

The realtime subsystem can stream progress updates that represent the current stage of such operations.

## Realtime Channel Types

The realtime architecture may define several logical channels.

### FSM State Channel

This channel streams behavioural state transitions.

Typical transmitted data includes:

* current state
* previous state
* triggering event
* transition timestamp

### Notification Channel

This channel streams system notifications and alerts.

Typical transmitted data includes:

* notification type
* notification message
* severity level
* timestamp

### Log Stream

This channel streams technical logs generated by the system runtime.

It is primarily used by administrative or debugging interfaces.

### Telemetry Channel

This channel streams system telemetry information.

Examples include:

* CPU load
* memory usage
* sensor readings
* hardware status

### Conversation Channel

This channel streams dialogue updates during user interaction.

Typical transmitted data includes:

* user messages
* system responses
* conversation state updates

### Action Progress Channel

This channel streams updates about ongoing operations.

Examples include:

* task progress
* action completion states
* intermediate execution stages

## Realtime Message Model

Realtime messages follow a structured representation.

A typical message structure includes:

* message type
* event identifier
* timestamp
* payload data
* metadata

This structure ensures that realtime clients can interpret incoming messages consistently.

## Authentication and Security

The realtime subsystem operates within the same identity and security model as the rest of the backend.

Security mechanisms include:

* validating authentication tokens during connection establishment
* resolving the identity context of the connection
* enforcing permission checks for protected streams
* isolating user-specific streams
* protecting administrative channels

These mechanisms ensure that sensitive information is not exposed to unauthorized clients.

## Relationship With the HTTP API

The HTTP API and the WebSocket / Realtime submodule represent complementary communication interfaces.

The HTTP API exposes synchronous request-response operations.

The WebSocket subsystem exposes asynchronous state propagation.

Typical interaction patterns include:

* a client retrieving initial state through the HTTP API
* the same client subscribing to realtime channels for ongoing updates

Together these mechanisms define the full communication surface of the backend.

## Relationship With the Event System

The realtime subsystem frequently consumes events produced by other parts of the architecture.

Examples of event sources include:

* the event dispatcher
* the behavioural state machine
* perception pipelines
* application services
* hardware controllers

These events are transformed into realtime messages and distributed to subscribed clients.

This integration allows the internal behaviour of the system to become externally observable.

## Implementation Implications

The architectural definition of this submodule implies several implementation components.

These components include:

* a WebSocket server
* a connection manager
* message broadcasting utilities
* subscription registries
* message serialization mechanisms
* integration with event dispatch
* integration with logging systems

These components collectively implement the realtime transport layer.

## Typical Examples

Representative realtime interactions in NORA include:

* a frontend interface receiving a state transition update
* an administrative dashboard streaming runtime logs
* a monitoring interface receiving telemetry updates
* a chat interface receiving a new assistant message
* a debugging interface observing event flows

These interactions demonstrate how realtime channels expose live system behaviour.

## Architectural Importance

The WebSocket / Realtime subsystem allows NORA to expose its runtime behaviour as a continuous observable stream.

Without this subsystem, external interfaces would rely on repeated polling and would observe system state with delay.

With realtime channels, NORA provides:

* live state synchronization
* immediate event visibility
* responsive user interfaces
* operational monitoring
* live debugging capabilities

For these reasons, the WebSocket / Realtime subsystem forms a fundamental communication component of the Backend and Application architecture.

# 8.3 Application Services

## Definition

The Application Services submodule defines the layer responsible for executing the operational use cases of NORA.

Application Services translate external requests and internal triggers into coordinated system operations involving multiple architectural domains.

Within the Backend and Application architecture, this submodule introduces the structures that transform domain capabilities into concrete system behaviour.

The Application Services submodule introduces the following architectural elements:

* an application service
* a use-case operation
* a service method
* a service orchestration flow
* a domain interaction sequence
* a service execution context
* a transactional execution boundary
* a domain coordination operation
* a service side effect
* a service result object

An application service is a backend component responsible for executing one category of system use cases.

A use-case operation is a specific system action implemented by a service.

A service method is the concrete function that executes a use case.

A service orchestration flow is the ordered sequence of domain interactions required to complete a use case.

A domain interaction sequence is the set of calls performed by a service toward domain modules.

A service execution context is the runtime context in which a service executes, including identity context, request metadata, and system state.

A transactional execution boundary is the scope in which multiple operations must succeed or fail as a consistent unit.

A domain coordination operation is a service-level action that invokes multiple modules while preserving domain separation.

A service side effect is a change in system state caused by the execution of a service.

A service result object is the structured outcome returned after the completion of a service operation.

Together, these elements define the Application Services layer as the architectural component responsible for orchestrating system behaviour.

## Architectural Purpose

The purpose of the Application Services submodule is to execute system-level operations by coordinating multiple architectural domains.

NORA contains many internal domains that encapsulate specialized logic.

These domains include:

* identity and access control
* perception pipelines
* behavioural state management
* dialogue and session management
* planning and agent reasoning
* action and expression execution
* persistence and memory

Each domain defines its own internal logic and responsibilities.

Application Services coordinate these domains when a complete system operation must be performed.

Examples of such operations include:

* opening a conversational session
* restoring a previously active project
* dispatching an event into the behavioural control system
* retrieving dialogue history
* synchronizing hardware state
* executing an administrative action

These operations require collaboration between several modules.

Application Services define the orchestration structure that performs this collaboration.

## Architectural Role

Within the overall architecture, Application Services act as the execution layer for system use cases.

The conceptual flow of execution may be represented as:

External Request or Internal Trigger → Interface Layer → Application Service → Domain Modules

Interface layers include:

* HTTP API
* WebSocket message handlers
* scheduled backend jobs
* administrative tools

Application Services receive validated input from these layers and execute the corresponding system operation.

The services then coordinate interactions with domain modules and produce the final outcome.

Application Services therefore define the operational execution layer of the backend architecture.

## Structural Necessity

A complex architecture such as NORA contains many domain modules that must interact during runtime operations.

Examples of operations requiring multiple domains include:

* session creation
* project restoration
* event dispatch
* hardware command execution
* configuration updates
* administrative maintenance

Without an application service layer, interface components would need to directly interact with multiple domains.

This would produce tightly coupled interfaces containing orchestration logic.

The Application Services layer centralizes orchestration responsibilities and provides clear execution boundaries for system operations.

This design produces several structural benefits:

* separation between transport layers and execution logic
* reusable implementation of use cases
* simplified interface layers
* clearer execution flows

The Application Services submodule therefore acts as the orchestration backbone of the backend.

## Scope of the Submodule

The Application Services layer contains all components responsible for executing application-level operations.

Its scope includes:

* service classes representing system capabilities
* service methods implementing use cases
* orchestration logic connecting domain modules
* transactional coordination with persistence layers
* domain-level validation
* event publication following operations
* result construction and return

The submodule does not include:

* transport-layer request handling
* realtime message streaming
* internal reasoning logic of domain modules
* direct sensor processing
* hardware driver implementation
* frontend rendering

These concerns belong to other modules in the architecture.

The Application Services layer coordinates these domains but does not replace their internal responsibilities.

## Core Architectural Responsibilities

The Application Services layer performs several structural responsibilities.

### Use-Case Execution

Each service implements a specific category of system operations.

A service operation translates a high-level request into a sequence of domain interactions.

Typical operations include:

* session creation
* project retrieval
* event dispatch
* preference update
* hardware synchronization

Each operation produces a clearly defined result object representing the outcome of the use case.

### Domain Coordination

Application Services coordinate interactions between domain modules.

This coordination includes:

* retrieving data from persistence
* updating behavioural state
* invoking planning components
* triggering action systems
* recording system events

The service orchestrates these interactions in a deterministic sequence.

### Transactional Consistency

Some operations involve multiple data modifications.

Application Services define execution boundaries in which related modifications must succeed together.

Examples include:

* creating a session and recording its creation event
* updating user preferences and persisting audit information

Transactional boundaries ensure that incomplete operations do not produce inconsistent system state.

### Event Publication

When operations complete, services may emit system events.

Examples of service-generated events include:

* session created
* project opened
* device state updated
* action executed

These events may be consumed by:

* the event dispatcher
* realtime broadcasting systems
* logging subsystems

### Operational Validation

Services perform domain-level validation before executing operations.

This validation verifies that requested operations are valid within the current system context.

Examples include:

* confirming that a session exists
* verifying that a project is not archived
* ensuring that a hardware device is available

This validation protects system consistency.

## Service Categories

Several categories of application services may exist in the NORA architecture.

### Event Service

The Event Service manages interactions with the system event dispatcher.

Responsibilities include:

* event injection
* event retrieval
* event forwarding
* event inspection

### Session Service

The Session Service manages the lifecycle of interaction sessions.

Responsibilities include:

* session creation
* active session retrieval
* session suspension
* session termination
* session restoration

### Project Service

The Project Service manages conversational projects.

Responsibilities include:

* project creation
* project retrieval
* project activation
* project updates
* project archival

### Dialogue Service

The Dialogue Service coordinates conversational interactions.

Responsibilities include:

* storing dialogue turns
* retrieving conversation history
* maintaining dialogue context
* forwarding dialogue inputs to planning modules

### User Service

The User Service manages user-related operations.

Responsibilities include:

* retrieving user information
* updating user preferences
* resolving permission information
* managing associated devices

### Device Service

The Device Service coordinates hardware-related operations.

Responsibilities include:

* retrieving device status
* coordinating hardware commands
* synchronizing hardware state

### Admin Service

The Admin Service manages administrative operations.

Responsibilities include:

* system inspection
* module restart operations
* maintenance operations
* configuration updates

## Service Design Structure

Application Services follow a structured internal design.

### Service Layer

The service layer contains service classes representing system capabilities.

### Use-Case Methods

Each service class exposes methods representing individual system operations.

### Domain Interaction Layer

Service methods invoke domain modules to retrieve or update system state.

### Result Construction Layer

Service methods construct result objects representing the outcome of the operation.

## Relationship With Other Backend Components

Application Services interact with several backend elements.

### HTTP API

The HTTP API forwards validated requests to Application Services.

### Realtime Subsystem

Services may publish events or updates that are broadcast through realtime channels.

### Event Dispatcher

Some service operations inject events into the system via the event dispatcher.

### Persistence Layer

Services frequently retrieve or store information using persistence repositories.

## Example Execution Flow

Consider the example of opening a conversational session.

1. A client request arrives through the HTTP API.
2. The API validates authentication and request structure.
3. The Session Service is invoked.
4. The service creates a session record through the persistence layer.
5. The behavioural state machine receives an event indicating session creation.
6. A realtime update is emitted.
7. The service returns a session result object.

This example demonstrates how Application Services coordinate multiple components during a system operation.

## Implementation Implications

The architectural definition of Application Services implies several implementation structures.

These include:

* service classes grouped by domain
* dependency injection mechanisms
* repository access layers
* transactional execution support
* event publishing utilities
* structured result objects

These structures support modular, testable service implementations.

## Architectural Importance

The Application Services layer is the operational execution layer of the backend architecture.

This submodule ensures that system operations remain clearly structured and independent from transport interfaces.

Through Application Services, the architecture gains:

* centralized orchestration of system operations
* reusable use-case implementations
* separation between interfaces and domain logic
* consistent execution boundaries

For these reasons, the Application Services layer forms the operational backbone of the Backend and Application module.

# 8.4 Coordinators / Orchestrators

## Definition

The Coordinators / Orchestrators submodule defines the architectural components responsible for supervising and controlling multi-step operational processes that span multiple application services and domain modules.

These components govern structured workflows that involve several subsystems executing in sequence, in parallel, or under conditional control.

Within the Backend and Application architecture, Coordinators introduce the structures that manage process-level behaviour across the system.

The Coordinators / Orchestrators submodule introduces the following architectural elements:

* a coordinator
* an orchestrator
* a workflow
* a workflow step
* a workflow state
* a workflow transition
* a process execution context
* a coordination sequence
* a branching condition
* a recovery strategy
* a workflow progress signal

A coordinator is a backend component responsible for supervising the execution of a structured operational process.

An orchestrator is a coordination component responsible for controlling the order and interaction of operations across multiple services.

A workflow is a defined sequence of operations that together implement a complex system behaviour.

A workflow step is an individual operation executed during the workflow.

A workflow state represents the current stage of a running process.

A workflow transition represents the progression from one stage of a process to another.

A process execution context is the runtime information associated with a running workflow.

A coordination sequence is the ordered set of service calls executed by the coordinator.

A branching condition is the rule that determines which path a workflow follows when multiple outcomes are possible.

A recovery strategy is the defined behaviour applied when a workflow step fails.

A workflow progress signal is a structured update emitted during the execution of a workflow.

Together, these elements define the orchestration layer of the backend.

## Architectural Purpose

The purpose of the Coordinators / Orchestrators submodule is to manage operational processes that involve multiple application services and domain modules.

Some behaviours in NORA cannot be expressed as a single service operation.

These behaviours include processes such as:

* conversational interaction cycles
* perception to interpretation to planning to action pipelines
* multi-stage hardware procedures
* system initialization
* module recovery
* long-running computational tasks

These processes require the execution of several operations in a specific order while maintaining system consistency.

Coordinators define the control structures that govern these sequences.

## Architectural Role

Within the backend architecture, coordinators operate above individual application services.

The conceptual process structure can be represented as:

Trigger Event → Coordinator → Workflow Sequence → Application Services → Domain Modules

In this structure:

* application services perform individual operations
* domain modules perform domain-specific logic
* coordinators supervise the sequence and interaction of operations

The coordinator therefore defines the execution structure of complex backend processes.

## Structural Necessity

NORA is composed of multiple subsystems that interact during runtime behaviour.

Operations frequently require coordinated execution across these subsystems.

Examples include:

* perception generating interpreted input
* planners selecting response strategies
* agents generating outputs
* dialogue modules updating conversation history
* hardware modules executing actions

A workflow containing all these steps must be controlled in a predictable and observable way.

Embedding such workflows inside a single application service would produce large and tightly coupled service components.

The Coordinators / Orchestrators layer isolates workflow supervision from individual operations.

This separation produces several structural advantages:

* clearer process structure
* improved modularity
* easier observability of workflows
* simpler service implementations

## Scope of the Submodule

The Coordinators / Orchestrators submodule contains the components responsible for managing structured workflows across the architecture.

Its scope includes:

* workflow definition
* workflow execution supervision
* coordination of multiple services
* sequencing of operations
* conditional branching
* recovery handling
* progress reporting

The submodule does not include:

* transport protocol handling
* domain-level reasoning
* low-level service operations
* sensor processing

These responsibilities remain within other modules.

The orchestrator layer focuses exclusively on process-level coordination.

## Core Architectural Responsibilities

The Coordinators / Orchestrators layer performs several responsibilities.

### Workflow Coordination

The coordinator defines the sequence of operations required for a multi-step process.

Each workflow step invokes one or more application services.

The coordinator ensures the correct order of execution.

### Process State Supervision

During execution, a workflow progresses through multiple stages.

The coordinator tracks the current workflow state and determines the next transition.

This supervision provides visibility into the lifecycle of the process.

### Conditional Branching

Workflow execution may diverge depending on results produced during execution.

Branching conditions determine the next step of the workflow.

Examples include:

* selecting an agent based on intent
* retrying perception when input quality is insufficient
* triggering fallback behaviour when planning fails

### Failure Recovery

Workflows may encounter errors or unavailable resources.

Coordinators define recovery strategies such as:

* retrying failed operations
* selecting alternative execution paths
* cancelling the workflow

### Progress Reporting

During execution, coordinators may emit progress signals that describe the current workflow state.

These signals can be consumed by:

* realtime communication channels
* logging subsystems
* monitoring tools

## Types of Coordinators

The architecture may include several coordinator components.

### Interaction Coordinator

The Interaction Coordinator manages the lifecycle of user interactions.

Responsibilities include:

* receiving interpreted input
* invoking planning components
* selecting response generation mechanisms
* triggering output actions

### Perception Pipeline Coordinator

The Perception Pipeline Coordinator supervises perception processing pipelines.

Responsibilities include:

* receiving sensor signals
* invoking perception modules
* forwarding interpreted results

### Action Execution Coordinator

The Action Execution Coordinator supervises the execution of multi-step actions.

Examples include:

* hardware control sequences
* media processing pipelines
* composite system outputs

### System Lifecycle Coordinator

The System Lifecycle Coordinator manages global system processes.

Examples include:

* system startup
* module initialization
* system shutdown
* recovery procedures

### Task Execution Coordinator

The Task Execution Coordinator supervises long-running tasks.

Examples include:

* document analysis
* media processing
* background reasoning tasks

## Relationship With Application Services

Application Services implement individual system operations.

Coordinators combine those operations into structured workflows.

The relationship may be expressed as:

Application Service → atomic operation
Coordinator → multi-step orchestration

This separation prevents service implementations from containing complex workflow logic.

## Relationship With the Cognitive Core

The Cognitive Core defines behavioural states and transitions.

Coordinators may interact with the Cognitive Core by:

* emitting events
* observing state changes
* adapting workflow execution according to system state

This ensures that orchestrated processes remain consistent with the behavioural model of the system.

## Relationship With Realtime Channels

During workflow execution, coordinators may emit progress signals and state updates.

Realtime channels distribute these signals to observing interfaces.

This mechanism allows external tools to visualize ongoing system processes.

## Example Workflow

Consider a conversational response workflow.

1. A perception module produces interpreted user input.
2. The Interaction Coordinator receives the input.
3. The planner determines the response strategy.
4. An agent generates a response.
5. The action system performs speech synthesis.
6. Dialogue history is updated.
7. A realtime update is emitted.

The coordinator supervises the entire sequence.

## Implementation Implications

The architectural definition of the orchestrator layer implies several implementation components.

These may include:

* workflow management components
* orchestration classes
* process state tracking structures
* asynchronous task supervisors
* retry management utilities

These components implement reliable coordination across system processes.

## Architectural Importance

The Coordinators / Orchestrators layer provides the structural control mechanism for complex system behaviours.

Without orchestration components, workflows would be distributed across multiple services and become difficult to maintain.

By introducing a dedicated orchestration layer, the architecture gains:

* structured workflow management
* improved modularity
* explicit process supervision
* observable system execution

This submodule therefore forms the process coordination layer of the Backend and Application architecture.

# 8.5 Event Dispatcher

## Definition

The Event Dispatcher is the subsystem responsible for receiving, routing, and distributing events across the internal components of NORA.

NORA operates as an event-driven architecture in which system behaviour is frequently triggered by signals emitted by perception systems, dialogue modules, planners, hardware interfaces, backend services, or external clients.

The Event Dispatcher introduces the routing infrastructure that allows these signals to propagate through the system without creating direct dependencies between producers and consumers.

The Event Dispatcher submodule introduces the following architectural elements:

* an event
* an event producer
* an event consumer
* an event channel
* an event routing rule
* an event subscription
* an event handler
* an event dispatch operation
* an event broadcast
* an event propagation signal

An event is a structured signal representing a system occurrence.

An event producer is any component that emits an event.

An event consumer is any component that receives and processes an event.

An event channel is the internal communication path used to propagate events.

An event routing rule determines how an event is delivered to its consumers.

An event subscription is the registration of a consumer to receive certain types of events.

An event handler is the component that processes an event after it has been delivered.

An event dispatch operation is the procedure by which the dispatcher forwards an event to its consumers.

An event broadcast is the delivery of a single event to multiple consumers.

An event propagation signal is the internal transmission of an event through the system.

Together, these elements define the event routing infrastructure of the backend.

## Architectural Purpose

The purpose of the Event Dispatcher is to provide a controlled and observable mechanism for propagating events across the system.

Multiple subsystems in NORA may produce events during runtime operation.

These subsystems include:

* perception pipelines
* dialogue modules
* planning components
* application services
* hardware interfaces
* administrative tools

These events may represent system signals such as:

* perception detections
* user interaction signals
* planner decisions
* hardware state changes
* FSM triggers

The Event Dispatcher provides the mechanism that propagates these signals to the relevant consumers while preserving modular boundaries between modules.

## Architectural Role

Within the backend architecture, the Event Dispatcher operates as the central routing hub for system events.

The conceptual event propagation structure can be represented as:

Event Producer → Event Dispatcher → Event Consumers

Event producers may include:

* perception modules
* the HTTP API
* hardware drivers
* application services
* coordinators

Event consumers may include:

* the FSM
* application services
* workflow coordinators
* logging systems
* realtime communication channels

The dispatcher determines which consumers receive each event and performs the routing operation.

## Structural Necessity

In architectures composed of many interacting components, direct communication paths create strong coupling between modules.

For example, a perception module detecting speech input may need to notify several other components such as:

* the dialogue system
* the planner
* the FSM
* the logging subsystem
* realtime monitoring interfaces

If each of these components were connected directly, the perception module would need knowledge of every consumer.

The Event Dispatcher removes this dependency by allowing modules to emit events without referencing the components that will consume them.

This design enables modular system expansion and simplifies component interactions.

## Scope of the Submodule

The Event Dispatcher subsystem contains the infrastructure responsible for routing and distributing events across the backend.

Its scope includes:

* receiving events emitted by producers
* validating event structure
* determining routing targets
* forwarding events to subscribed consumers
* broadcasting events to multiple modules
* forwarding selected events to realtime channels
* forwarding events to logging systems

The dispatcher does not implement domain logic associated with the event.

Domain modules remain responsible for interpreting and acting upon events.

## Core Architectural Responsibilities

The Event Dispatcher performs several responsibilities.

### Event Reception

The dispatcher receives events emitted by system components.

Event producers may include internal services, perception modules, API handlers, or hardware interfaces.

### Event Validation

Before an event is routed, the dispatcher may validate its structure.

Validation typically includes checking:

* event type
* payload structure
* metadata integrity

### Event Routing

The dispatcher determines which consumers should receive the event.

Routing decisions may depend on:

* event type
* subscription rules
* routing configuration

### Event Broadcasting

Some events must be delivered to multiple consumers simultaneously.

The dispatcher performs broadcast operations when required.

### Event Logging

Events may be forwarded to logging subsystems or monitoring tools so that system behaviour can be inspected and audited.

### Realtime Event Forwarding

Certain events may be forwarded to realtime communication channels.

This allows connected clients or monitoring interfaces to observe system activity.

## Event Structure

To maintain consistency across the architecture, events follow a standardized structure.

Typical event fields include:

* event identifier
* event type
* timestamp
* event source
* payload data
* metadata

This structure allows any consumer receiving the event to interpret its contents.

## Event Categories

Events in NORA may be grouped into several categories.

### Interaction Events

Generated during user interaction with the system.

Examples include:

* speech detected
* command recognized
* dialogue turn created

### System Events

Generated by internal system operations.

Examples include:

* FSM transition
* session started
* project activated

### Hardware Events

Generated by hardware devices or sensors.

Examples include:

* camera activation
* microphone signal detected
* battery status update

### Administrative Events

Generated by administrative operations.

Examples include:

* configuration updated
* module restarted

## Relationship With the Cognitive Core

One of the primary consumers of events is the Finite State Machine defined in the Cognitive Core.

Events emitted by perception modules, services, or external interfaces may trigger state transitions within the FSM.

The dispatcher forwards these events to the FSM controller.

This allows the behavioural model of the system to react to system signals while remaining decoupled from the components that produced the events.

## Relationship With Application Services

Application services may both produce and consume events.

A service may emit an event after completing an operation.

Other services may subscribe to these events to trigger additional behaviour.

The dispatcher coordinates this communication without creating direct dependencies between services.

## Relationship With Realtime Channels

Certain events may be visible to external observers.

The dispatcher may forward these events to the realtime subsystem so that:

* user interfaces can observe system activity
* administrators can monitor system behaviour
* debugging tools can inspect event flows

## Example Event Flow

Consider a speech interaction scenario.

1. The microphone captures speech input.
2. The perception module emits a speech_detected event.
3. The Event Dispatcher receives the event.
4. The dispatcher forwards the event to the dialogue module.
5. The dispatcher forwards the event to the FSM.
6. The dispatcher logs the event.
7. The dispatcher forwards a notification to the realtime channel.

This example illustrates how a single event can trigger multiple system reactions.

## Implementation Implications

The architectural definition of the Event Dispatcher implies several implementation structures.

These may include:

* event bus implementations
* event subscription registries
* event routing tables
* event serialization utilities
* event logging hooks

These components enable efficient event propagation across the system.

## Architectural Importance

The Event Dispatcher provides the central routing mechanism that supports the event-driven behaviour of NORA.

Without this subsystem, modules would require direct communication paths with one another, producing a complex dependency structure.

By introducing an event routing layer, the architecture gains:

* decoupled module communication
* scalable event propagation
* improved system observability
* simplified extensibility of system behaviour

For these reasons, the Event Dispatcher is a fundamental infrastructure component of the Backend and Application architecture.

# 8.6 Observability

## Definition

The Observability subsystem defines the infrastructure that exposes the internal operational state, behaviour, and health of NORA during runtime.

In a system composed of multiple interacting components such as perception pipelines, planning modules, application services, realtime communication channels, and hardware interfaces, it is necessary to make system behaviour visible and diagnosable during operation.

The Observability subsystem introduces the mechanisms that collect and expose operational telemetry across the architecture.

The Observability subsystem introduces the following architectural elements:

* a log record
* a metric signal
* a trace span
* a telemetry collector
* a telemetry exporter
* a monitoring stream
* a diagnostic event
* a health signal
* an alert condition
* a monitoring interface

A log record is a structured message describing a discrete system event.

A metric signal is a numerical measurement representing a property of system operation.

A trace span is a recorded segment of an operation that propagates across system components.

A telemetry collector is a component responsible for gathering operational signals from system modules.

A telemetry exporter forwards collected signals to monitoring systems or storage backends.

A monitoring stream is the continuous flow of telemetry data generated by system components.

A diagnostic event is a signal describing abnormal system behaviour or execution anomalies.

A health signal is a measurement representing the operational state of a module or service.

An alert condition is a defined rule that triggers notifications when abnormal system behaviour is detected.

A monitoring interface is the system surface through which operational data is visualized or inspected.

Together, these elements define the telemetry and monitoring infrastructure of the backend.

## Architectural Purpose

The purpose of the Observability subsystem is to ensure that system behaviour can be inspected, monitored, and diagnosed during runtime.

NORA performs many asynchronous operations, including:

* event dispatching
* realtime communication
* planning workflows
* perception processing
* hardware interaction

These operations occur across multiple modules and execution contexts.

Observability provides the instrumentation required to understand how these operations behave during execution.

This instrumentation enables engineers and operators to:

* monitor system health
* evaluate system performance
* detect abnormal behaviour
* trace complex operations
* diagnose system failures

## Architectural Role

Within the backend architecture, Observability operates as the cross-cutting diagnostic layer that collects telemetry from system components.

The conceptual telemetry flow may be represented as:

System Components → Telemetry Collectors → Monitoring Systems

Components that produce observability signals include:

* HTTP API interfaces
* realtime communication channels
* application services
* workflow coordinators
* the event dispatcher
* the cognitive core FSM
* perception pipelines
* hardware modules

Telemetry collectors gather these signals and forward them to monitoring systems or analysis tools.

## Structural Necessity

In a distributed and event-driven architecture, system behaviour often emerges from the interaction of multiple components.

When unexpected behaviour occurs, engineers must determine:

* which event triggered the behaviour
* which module executed the operation
* how long the operation took
* where failures occurred

Without telemetry signals describing system activity, diagnosing such behaviour becomes extremely difficult.

The Observability subsystem provides the instrumentation required to reconstruct system behaviour during execution.

## Scope of the Submodule

The Observability subsystem contains the infrastructure responsible for collecting and exposing telemetry data about system behaviour.

Its scope includes:

* structured logging infrastructure
* metrics collection systems
* distributed tracing instrumentation
* runtime diagnostics
* monitoring dashboards
* alerting mechanisms

The subsystem does not implement domain-level logic or application workflows.

It focuses exclusively on exposing operational insight into system behaviour.

## Core Observability Signals

Observability typically relies on three primary telemetry categories: logs, metrics, and traces.

### Logging

Logging records discrete events that occur during system execution.

Examples include:

* API request processing
* FSM state transitions
* event emissions
* service execution
* error messages

Structured logging allows logs to be filtered, searched, and analyzed automatically.

### Metrics

Metrics represent numerical measurements that describe system behaviour and performance.

Examples include:

* CPU utilization
* memory consumption
* request latency
* active session count
* event throughput
* hardware telemetry

Metrics are typically collected continuously and aggregated into monitoring dashboards.

### Distributed Tracing

Tracing records the propagation of operations across multiple components.

For example, a single interaction may involve:

1. an HTTP API request
2. an application service
3. a coordinator
4. the FSM
5. an action module
6. a realtime broadcast

Tracing records each step of the operation, allowing engineers to observe the full execution path.

## Sources of Observability Data

Many architectural components generate telemetry signals.

### HTTP API

The API layer may emit logs and metrics describing:

* incoming requests
* authentication outcomes
* response latency
* HTTP status codes

### Event Dispatcher

The event system may emit telemetry describing:

* event emissions
* routing operations
* event processing outcomes

### Application Services

Services may log operational activities such as:

* session creation
* project activation
* task execution

### Cognitive Core

The FSM may emit telemetry describing:

* state transitions
* triggering events
* system mode changes

### Hardware Interfaces

Hardware modules may emit telemetry describing:

* device connectivity
* sensor activity
* hardware errors

## Monitoring and Visualization

Telemetry data is typically aggregated and presented through monitoring interfaces.

Monitoring tools may display:

* system health indicators
* performance metrics
* recent system events
* error rates
* hardware status

These interfaces allow engineers and operators to inspect system behaviour in real time.

## Alerting

The observability infrastructure may define alert conditions that notify operators when abnormal behaviour occurs.

Examples of alert conditions include:

* repeated service failures
* excessive request latency
* hardware disconnection
* elevated error rates

Alerts allow operators to respond to problems before they escalate into system failures.

## Relationship With Backend Components

Observability interacts with most components of the backend architecture.

### Application Services

Services emit logs and metrics describing system operations.

### Coordinators

Coordinators may emit traces describing workflow execution.

### Event Dispatcher

The dispatcher may emit telemetry describing event propagation and routing.

### Realtime Channels

Observability signals may be streamed through realtime channels to monitoring interfaces.

## Implementation Implications

Implementing the Observability subsystem typically requires several supporting components.

These may include:

* structured logging frameworks
* metrics collectors
* tracing instrumentation
* log aggregation systems
* monitoring dashboards
* alerting systems

These components allow system behaviour to be inspected and analyzed effectively.

## Architectural Importance

Observability provides the instrumentation required to operate and maintain complex software systems.

Without telemetry infrastructure, diagnosing failures in a distributed and event-driven architecture would be extremely difficult.

By introducing a dedicated observability subsystem, NORA gains:

* transparency of internal behaviour
* improved debugging capabilities
* performance monitoring
* operational reliability

For these reasons, Observability forms a fundamental part of the Backend and Application architecture.

## Architectural Importance

The Backend and Application module provides the operational execution infrastructure that connects external system interfaces with the internal cognitive and domain modules of NORA.

While other architectural modules define perception, reasoning, planning, memory, and interaction structures, the Backend and Application module is responsible for coordinating the runtime execution of system behaviour.

Through this module the architecture gains:

* structured access to system capabilities through API interfaces
* realtime propagation of system events and state
* coordinated execution of application use cases
* orchestration of complex multi-step workflows
* decoupled communication between modules through event routing
* operational transparency through telemetry and monitoring

By separating interface transport, operational execution, workflow coordination, and event routing, the architecture ensures that system behaviour remains modular, scalable, and observable.

## Architectural Structure

```
Backend and Application
│
├── HTTP API
│ ├── API boundary definition
│ ├── endpoint routing
│ ├── request validation
│ ├── response construction
│ ├── authentication enforcement
│ ├── authorization enforcement
│ ├── error handling
│ ├── transport protocol handling
│ ├── API version management
│ ├── external client access
│ ├── service invocation gateway
│ └── synchronous request-response interface
│
├── Realtime Communication
│ ├── persistent connection management
│ ├── websocket session management
│ ├── client subscription management
│ ├── event streaming channels
│ ├── broadcast message propagation
│ ├── state update distribution
│ ├── realtime notification delivery
│ ├── message serialization
│ ├── connection health monitoring
│ ├── streaming protocol handling
│ ├── realtime event forwarding
│ └── asynchronous system communication
│
├── Application Services
│ ├── use-case execution
│ ├── service method orchestration
│ ├── domain module coordination
│ ├── transactional operation boundaries
│ ├── domain validation
│ ├── system state updates
│ ├── persistence interaction
│ ├── event emission
│ ├── service result construction
│ ├── operational context management
│ ├── reusable system operations
│ └── application logic execution
│
├── Coordinators / Orchestrators
│ ├── workflow definition
│ ├── workflow execution supervision
│ ├── multi-service coordination
│ ├── process state supervision
│ ├── execution sequencing
│ ├── conditional branching control
│ ├── failure recovery strategies
│ ├── long-running task supervision
│ ├── workflow progress reporting
│ ├── cross-module process orchestration
│ ├── system lifecycle coordination
│ └── complex behaviour supervision
│
├── Event Dispatcher
│ ├── event reception
│ ├── event validation
│ ├── event routing
│ ├── event subscription management
│ ├── event broadcast propagation
│ ├── event handler invocation
│ ├── inter-module communication routing
│ ├── event forwarding to FSM
│ ├── event forwarding to services
│ ├── realtime event forwarding
│ ├── event logging integration
│ └── event-driven communication infrastructure
│
└── Observability
  ├── structured logging infrastructure
  ├── metrics collection
  ├── distributed tracing instrumentation
  ├── telemetry aggregation
  ├── diagnostic event reporting
  ├── system health monitoring
  ├── runtime diagnostics
  ├── monitoring dashboards
  ├── alert generation
  ├── telemetry export pipelines
  ├── operational telemetry analysis
  └── system observability infrastructure
```

## Architectural Layers

The Backend and Application module is organized as an operational execution architecture that transforms external interactions and internal events into coordinated system behaviour.

| Layer                        | Responsibility                                                                                        |
| ---------------------------- | ----------------------------------------------------------------------------------------------------- |
| Interface Access Layer       | Provides synchronous and realtime access to system capabilities through HTTP and WebSocket interfaces |
| Application Execution Layer  | Executes atomic system operations through application services                                        |
| Workflow Orchestration Layer | Coordinates multi-step processes across services and domain modules                                   |
| Event Communication Layer    | Propagates events between system components through the event dispatcher                              |
| Observability Layer          | Exposes telemetry, monitoring, and diagnostics describing runtime system behaviour                    |

Together these layers establish the runtime execution backbone of NORA, allowing external interactions, internal system events, and complex workflows to be processed in a structured, observable, an
