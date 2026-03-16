# 1. Identity, Access and Security

## Definition

The **Identity, Access and Security** module defines who interacts with NORA, how identities are verified, what each entity is allowed to do, and how the system protects its internal resources.

This module establishes the trust and control layer of the system. Every interaction with NORA, whether conversational, physical, or digital, must ultimately be associated with:

* **Identity**  
logical representation of the actor responsible for an interaction with the system.

* **Permission model**  
structured set of rules that determines which actions an identity is allowed to perform.

* **Security policy**  
system rules that define how resources, operations, and data are protected.

* **Traceable action context**  
execution context that records the identity, session, and conditions under which an action occurred.

Without this module, the system cannot determine whether an action is legitimate, safe, or authorized.

NORA combines AI agents, physical hardware, multimodal perception, persistent memory, and external integrations. In this context, identity and security are foundational architectural requirements.

## Architectural Role

The Identity, Access and Security module acts as the trust boundary of the NORA system.

It ensures that:

* **Authorized resource access**  
system resources are accessed only by identities that possess the required permissions.

* **Action traceability**  
every relevant operation can be linked to the identity, session, and context that produced it.

* **Protection of sensitive operations**  
operations that affect security, configuration, data integrity, or hardware behaviour are protected through authorization controls.

* **Misuse detection and mitigation**  
abnormal or unauthorized behaviour is detectable and can trigger protective responses.

This module defines and enforces three fundamental responsibilities:

### Identity Management

Identity management defines the actors that interact with NORA.

The system defines the following actor categories:

* **Human users**  
people interacting directly with NORA through conversational, visual, or physical interfaces.

* **Administrators**  
privileged users responsible for supervising, configuring, and maintaining the system.

* **External systems**  
software services or platforms that interact with NORA through APIs or integrations.

* **Devices interacting with NORA**  
hardware components or connected devices that exchange data or commands with the system.

Identity management includes:

* **User entities**  
formal identity records representing the actors recognized by the system.

* **Identity attributes**  
structured properties associated with an identity, such as identifiers, roles, status, and linked authentication data.

* **Identity resolution**  
process through which the system determines which identity is associated with a given interaction, signal, or request.

* **Identity lifecycle**  
set of state changes and management operations affecting an identity across its existence in the system.

### Access Control

Access control determines which actions an identity is authorized to perform within NORA.

Access control mechanisms enforce permissions across the following system resources:

* **API endpoints**  
programmatic interfaces exposed by backend services that allow external or internal components to interact with NORA.

* **Hardware control**  
operations that command or configure physical components such as sensors, actuators, and connected devices.

* **Conversation data**  
conversational content generated during interactions between users and the system.

* **Persistent memory**  
stored knowledge, records, and contextual data maintained across sessions.

* **Administrative tools**  
privileged system interfaces used to supervise, configure, or maintain NORA.

* **System configuration**  
operational parameters that control system behaviour, module configuration, and infrastructure settings.

Access control policies apply uniformly across all interaction channels, including voice interfaces, graphical interfaces, physical interaction, and external APIs.

### Security Enforcement

Security enforcement provides the mechanisms that protect the system from misuse, abuse, or unintended behaviour.

Security enforcement includes:

* **Authentication mechanisms**  
processes that verify the identity of actors interacting with NORA before granting access to protected resources.

* **Authorization policies**  
rules that determine whether an authenticated identity is allowed to perform a specific action on a specific resource.

* **Protection of sensitive resources**  
safeguards that prevent unauthorized access to critical data, configuration, hardware control, and system capabilities.

* **Audit logging**  
structured recording of security-relevant events, actions, and decisions for traceability and accountability.

* **Suspicious behaviour monitoring**  
continuous observation of system activity to detect abnormal patterns or potentially malicious actions.

* **Session control**  
mechanisms that manage the lifecycle and validity of interaction sessions associated with authenticated identities.

* **Protection against automated attacks**  
safeguards that limit or block automated attempts to exploit system interfaces, authentication flows, or resources.

Because NORA operates in both digital and physical environments, security enforcement protects not only data and services but also physical actions performed through hardware components.

## Architectural Importance

In conventional software systems, identity and security primarily protect data and software services.

In NORA, identity and security also protect the system's interaction with the physical world and external infrastructures.

This includes protection of:

* **Physical actions**  
operations that control movement, actuators, and other hardware components capable of affecting the physical environment.

* **Sensor access**  
operations that activate or read sensors such as microphones, cameras, and other perception devices.

* **External integrations**  
interactions with external platforms, services, and connected systems.

* **Personal memory and conversations**  
stored conversational data and user-related knowledge maintained by the system.

* **System configuration and internal state**  
operational parameters and runtime state that determine how the system behaves.

Because these resources span both digital and physical domains, identity and security influence nearly every subsystem of the NORA architecture.

## Relationship With Other Architectural Modules

The Identity, Access and Security module provides the trust and authorization layer used by multiple subsystems of NORA.

These interactions ensure that system operations are always associated with an identity and executed under controlled permissions.

### Dialogue and Session System

conversational sessions are linked to an identity or to a controlled anonymous interaction context.

This association ensures that dialogue history, conversational actions, and contextual memory remain traceable and access-controlled.

### Backend Services

backend APIs validate incoming requests through authentication and authorization mechanisms before allowing access to system resources.

This guarantees that programmatic interactions respect the same security model as human interactions.

### Planning and Agents

actions proposed by planning modules or specialized agents are validated against authorization policies before execution.

This prevents agents from executing operations that exceed the permissions associated with the initiating identity.

### Action and Hardware Control

commands affecting hardware components are subject to authorization checks before execution.

This includes operations such as actuator control, device management, and sensor activation.

### Persistent Storage

access to stored data is governed by identity-aware authorization rules.

This protection applies to user data, conversational history, stored knowledge, and project-related information.

### Frontend Interfaces

user-facing interfaces implement authentication flows and maintain secure sessions associated with system identities.

This ensures that graphical, conversational, and administrative interfaces operate under the same identity model.

## Design Principles

The design of the Identity, Access and Security module follows a set of architectural principles that guide how trust, permissions, and protection are implemented across the system.

### Separation of Concerns

identity management, authentication, authorization, and security enforcement are implemented as distinct responsibilities within the architecture.

This separation maintains system clarity, reduces coupling, and allows each component to evolve independently.

### Least Privilege

each identity is granted only the permissions required to perform its intended tasks.

This principle limits the potential impact of errors, compromised identities, or malicious actions.

### Traceability

critical operations are linked to the identity, session, and contextual conditions under which they occurred.

Traceability enables auditing, debugging, and accountability across system activity.

### Multi-Modal Security

security mechanisms operate consistently across all interaction channels supported by NORA.

This includes voice interaction, graphical interfaces, external APIs, and physical device control.

### Context-Aware Authorization

authorization decisions are evaluated using both identity information and relevant runtime context.

Authorization policies evaluate contextual factors that influence whether an action is permitted.

These contextual factors include:

* **Current FSM state**  
the current state of the system's operational state machine, which determines which actions are valid at a given moment.

* **Active session**  
the authenticated interaction session associated with the identity initiating the action.

* **Device used**  
the hardware or interface through which the request originates.

* **User presence**  
confirmation that the user associated with the identity is physically present or actively interacting with the system.

* **System safety conditions**  
operational constraints that prevent actions that could compromise system safety, stability, or hardware integrity.

## Submodules

The Identity, Access and Security module is composed of the following submodules:

* **1.1 Users**  
Defines the identity entities recognized by the system and the categories of users interacting with NORA.

* **1.2 Authentication**  
Implements the mechanisms used to verify the identity of actors interacting with the system.

* **1.3 Authorization**  
Defines and enforces the permission model that determines which actions an identity is allowed to perform.

* **1.4 User Profile**  
Stores user-specific preferences, personalization settings, and configuration associated with an identity.

* **1.5 Security**  
Implements protection mechanisms such as auditing, monitoring, and safeguards against malicious or unintended system use.

Together, these submodules establish the identity model, permission structure, and security protections that govern all interactions with NORA.

Each of these components contributes to maintaining system integrity, safety, and accountability.

# 1.1 Users

## Definition

The **Users** submodule defines the identities that interact with NORA.

A user is a logical actor within the system. Each user identity has associated credentials, roles, permissions, preferences, and persistent data.

Within the architecture, user identity acts as the anchor point connecting authentication, authorization, personalization, sessions, and system actions.

Through user identity, NORA associates interactions with a specific actor and maintains continuity across sessions and devices.

## Identity Model

The identity model separates several related concepts to maintain a clear and modular architecture:

| Concept      | Description                                                   |
|  | - |
| **Identity** | Logical representation of an actor within the system          |
| **Account**  | Authentication credentials associated with the identity       |
| **Role**     | Set of permissions assigned to the identity                   |
| **Profile**  | Personal configuration used to adapt system behaviour         |

This separation ensures that identity, authentication, authorization, and personalization remain independent architectural components.

## User Types

NORA defines user capability levels that determine the permissions and operational scope associated with a user identity.

These types represent access profiles applied to identities rather than different identity structures.

## User Capability Levels

NORA defines four user capability levels:

* Guest
* User
* Pro
* Admin

These levels determine the operational scope, protected resources, and administrative access associated with a user identity.

| Type  | Persistent Identity | Personal Data | Projects | Advanced Tools | Admin Tools | System Configuration | Technical Observability |
|-|||-|-|-|-|-|
| Guest | No                  | No            | No       | No             | No          | No                   | No                      |
| User  | Yes                 | Yes           | No      | Limited        | No          | No                   | No                      |
| Pro   | Yes                 | Yes           | Yes      | Yes            | No          | No                   | Limited / No            |
| Admin | Yes                 | Yes           | Yes      | Yes            | Yes         | Yes                  | Yes                     |

### Guest

A **Guest** is an unauthenticated actor interacting with NORA without a persistent identity.

Guest access enables interaction with the system without account creation or authentication. This mode supports operation in shared or public environments.

Guest users interact with NORA through temporary sessions and have access only to non-sensitive system capabilities.

Guest users do not have access to:

* persistent identity
* personal data
* personal profiles
* projects
* advanced tools
* administrative tools
* system configuration
* technical observability interfaces

Guest interactions are internally logged but are not associated with a persistent user identity.

### User

A **User** is a standard authenticated identity within NORA.

User identities provide persistent interaction with the system and enable storage of personal data and configuration.

Users have access to:

* personal data associated with their identity
* personal profile and preference configuration
* persistent sessions
* conversation history
* personal memory
* linked personal devices
* standard system tools and interaction capabilities

Users do not have access to:

* personal projects
* administrative tools
* system configuration
* technical observability interfaces

User identities operate within the standard permission scope defined by the system.

### Pro

A **Pro** user is an authenticated identity with extended system capabilities.

Pro users have access to the same resources as standard users together with advanced tools and increased operational limits.

Pro users have access to:

* personal data and persistent identity
* personal projects
* advanced tools and system capabilities
* extended operational limits and resources

Pro users do not have access to:

* administrative tools
* system configuration
* full technical observability capabilities

Pro users do not manage the system but have access to advanced functionality intended for experienced users.

### Admin

An **Admin** is an authenticated identity with administrative privileges over the NORA system.

Administrators supervise, configure, and maintain system operation.

Admin users have access to:

* user and identity management
* system logs and audit records
* hardware and subsystem monitoring
* system configuration
* administrative tools
* technical observability interfaces
* maintenance and operational control actions

Administrative actions are always:

* authenticated
* authorized
* logged for auditing

## Role-Based Design

Although Guest, User, Pro, and Admin are described as user capability levels, the authorization model of NORA is based on **Role-Based Access Control (RBAC)**.

In this model:

* each identity is associated with one or more roles
* roles define sets of permissions
* permissions determine which actions the identity can perform

Conceptual structure:

```
User
 ├── roles
 │   ├── user
 │   ├── pro
 │   └── admin
 ├── permissions
 └── profile
```


This design separates identity from permission management and enables the authorization system to evolve without modifying the underlying identity structure.

## Device Associations

Device associations link physical or personal devices to a user identity.

Associated devices represent trusted interaction endpoints through which a user can access NORA.

Supported device types include:

* smartphones
* tablets
* laptops
* NFC tags
* wearable devices

Device associations enable the following capabilities:

* **Trusted device authentication**  
authentication mechanisms that recognize previously registered devices linked to a user identity.

* **Automatic identity recognition**  
identification of a user based on signals originating from a registered device.

* **Cross-device session continuity**  
ability to maintain or recover interaction sessions across multiple devices associated with the same identity.

* **Secure device pairing with NORA**  
controlled process that registers a device as belonging to a specific user identity.

## Identity Lifecycle

The Users submodule manages the lifecycle of identities within NORA.

Identity lifecycle events include:

* identity creation
* identity verification
* role assignment
* profile initialization
* device association
* profile updates
* identity deactivation
* identity deletion

Lifecycle management ensures that identities remain consistent, secure, and auditable throughout their existence in the system.

## Inputs

The Users submodule receives identity-related inputs from authentication systems, perception modules, interfaces, and administrative operations.

These inputs include:

* identity registration
* login requests
* anonymous interaction events
* NFC tag detection
* facial recognition identification
* device linking requests
* profile updates
* identity deactivation requests
* identity deletion requests

## Outputs

The Users submodule produces identity-related outputs used by other parts of the system.

These outputs include:

* resolved `identity_id`
* loaded user profile
* assigned roles
* computed permission set
* active user change event
* identity creation event
* identity resolution result

## Interaction With Other Modules

The Users submodule interacts with several other architectural components of NORA.

**Authentication**  
validates credentials and associates authentication results with a user identity.

**Authorization**  
evaluates the permissions assigned to the identity and determines which actions are allowed.

**User Profile**  
stores personal configuration, preferences, and personalization data associated with the identity.

**Sessions and Dialogue**  
associates conversational sessions and interaction context with a specific user identity.

**Persistent Storage**  
stores identity records, roles, device associations, and related metadata.

**Frontend Interfaces**  
provide user interfaces through which identities access and manage their account and profile information.

## Architectural Importance

The Users submodule forms the foundation of identity within NORA.

Every action performed within the system is traceable to a user identity or to a controlled anonymous interaction.

By centralizing identity management, the system ensures:

* consistent permission enforcement
* traceability of actions
* identity-based personalization of user interactions
* reliable system security

# 1.2 Authentication

## Definition

The **Authentication** submodule verifies the identity of actors interacting with NORA.

Authentication answers the question:

> Who is interacting with the system?

Authentication verifies that an actor claiming a specific identity is validated through one or more authentication mechanisms before access to protected resources or actions is granted.

Authentication is distinct from **authorization**, which determines which actions an authenticated identity is allowed to perform.

| Concept            | Purpose                |
|  | - |
| **Authentication** | Verifies identity      |
| **Authorization**  | Determines permissions |

Authentication mechanisms in NORA support multiple interaction modalities, including voice interaction, graphical interfaces, physical proximity mechanisms, and remote digital access.

## Authentication Model

NORA implements a **multi-method authentication model**, in which identity verification can be performed through several independent mechanisms.

Authentication relies on the following mechanism categories:

* **Credential-based authentication**  
verification of identity through knowledge-based credentials such as passwords or secret phrases.

* **Token-based authentication**  
verification using temporary or persistent authentication tokens issued after successful identity validation.

* **Biometric authentication**  
verification of identity using biometric characteristics such as voice patterns or facial recognition.

* **Device-based authentication**  
verification of identity based on trusted devices previously associated with a user identity.

* **Proximity-based authentication**  
verification triggered by physical presence signals such as NFC tags, Bluetooth devices, or similar proximity mechanisms.

These mechanisms can be combined to implement **multi-factor authentication (MFA)**, where identity verification requires multiple independent authentication factors.

## Credential-Based Authentication

Credential-based authentication verifies identity using knowledge-based credentials associated with a user identity.

### Email / Username Login

authentication mechanism in which a user provides a unique identifier together with a secret credential.

The identifier corresponds to an account attribute such as:

* email address
* username

This mechanism is used for authentication through graphical interfaces, administrative interfaces, and remote access systems.

### Password Authentication

authentication mechanism based on a secret known only to the user and the system.

Passwords are not stored in plaintext. The system stores:

* salted cryptographic hashes
* password-related metadata

Password authentication includes the following security protections:

* strong password hashing algorithms
* password complexity enforcement
* rate limiting for authentication attempts

## Token-Based Authentication

Token-based authentication verifies identity through authentication tokens issued after successful credential validation.

### Access Tokens

authentication tokens representing an authenticated identity during a session.

Access tokens are used to:

* authorize API requests
* maintain authenticated sessions
* avoid repeated credential submission

Access tokens contain identity and session information such as:

* identity identifier
* session identifier
* expiration timestamp

### Refresh Tokens

long-lived authentication tokens used to generate new access tokens without requiring the user to authenticate again.

Refresh tokens enable secure session continuity while keeping access tokens short-lived.

## OAuth Authentication

OAuth authentication verifies user identity through external identity providers.

authentication mechanism in which an external platform validates the user identity and returns an authorization token to NORA.

Supported external identity providers include:

* Google
* GitHub
* Apple
* Microsoft

OAuth authentication also supports delegated authorization, allowing NORA to access external services on behalf of the authenticated identity.

Delegated authorization includes access to external resources such as:

* calendars
* email services
* cloud platforms

In this model, OAuth provides both identity verification and delegated access to external services.

## Biometric Authentication

Biometric authentication verifies identity using physical or behavioural characteristics of the user.

In NORA, biometric authentication is integrated with the perception system, since the robot interacts with users through sensors such as cameras and microphones.

Biometric authentication mechanisms include:

* **Facial recognition**  
identity verification based on facial features captured through the vision system.

* **Voice biometrics**  
identity verification using acoustic characteristics of a user's voice.

* **Fingerprint authentication**  
identity verification using fingerprint sensors available on the robot or on trusted external devices.

* **Behavioural voice patterns**  
identity verification based on speech patterns and behavioural vocal characteristics.

### Facial Recognition

Facial recognition uses the robot's camera system to identify or authenticate a user based on facial features.

This mechanism enables NORA to:

* recognize returning users
* automatically activate associated user profiles
* personalize interactions immediately

Facial recognition operates in two modes:

* **identification** — estimating which identity corresponds to the detected face
* **authentication** — confirming a claimed identity with sufficient confidence

### Voice Biometrics

Voice biometrics identifies users through acoustic characteristics of their voice.

Voice authentication relies on mechanisms such as:

* voiceprint matching
* acoustic feature analysis
* speech pattern recognition

This mechanism supports voice-first interactions in which credential-based authentication is impractical.

### Fingerprint Authentication

Fingerprint authentication verifies identity through fingerprint sensors available either on the robot hardware or on associated trusted devices.

This mechanism provides a strong authentication factor for sensitive operations.

### Biometric Security Considerations

Biometric authentication requires careful handling of sensitive data.

Biometric security protections include:

* secure processing of biometric signals
* avoidance of raw biometric data storage
* fallback authentication mechanisms
* tolerance management for recognition uncertainty

## Proximity Authentication

Proximity authentication verifies identity based on the physical presence of a user or device near the robot.

Proximity authentication mechanisms include:

* **NFC / RFID authentication**  
authentication mechanism in which a user presents a physical tag or device detected by the robot through short-range communication technologies.

* **Bluetooth proximity authentication**  
authentication mechanism in which a previously associated device is detected through Bluetooth signals indicating the presence of the user near the robot.

* **WiFi proximity authentication**  
authentication mechanism in which a trusted device is detected through the local wireless network, allowing the system to infer the presence of the associated identity.

* **QR code authentication**  
authentication mechanism in which a user scans a QR code generated by the robot to complete identity verification on a trusted external device.

### NFC / RFID Authentication

NFC and RFID authentication allow users to authenticate by presenting a physical tag or device near the robot.

Supported proximity identifiers include:

* NFC cards
* NFC stickers
* wearable tags
* smartphones operating in NFC emulation mode

NFC and RFID authentication operate as **possession-based authentication factors** and may require additional verification for sensitive operations.

### Bluetooth / WiFi Proximity Detection

Bluetooth and WiFi proximity detection allow NORA to recognize trusted devices associated with a user identity.

This mechanism relies on previously registered devices such as:

* smartphones
* tablets
* laptops
* wearable devices

When a trusted device is detected within proximity of the robot, the system can:

* infer the presence of the associated identity
* assist identity resolution
* trigger authentication workflows

### QR Code Authentication

QR code authentication links the robot session with a trusted external device.

Authentication flow:

1. NORA generates a QR code
2. the user scans the QR code using a trusted device
3. authentication is performed on the external device
4. the verified identity is associated with the robot session

## Trusted Devices

Trusted devices are devices associated with a user identity and recognized by the system during authentication.

#definition: devices previously registered and linked to a user identity that can participate in authentication workflows.

Trusted devices include:

* smartphones
* tablets
* laptops
* wearable devices

Trusted devices enable the system to:

* reduce authentication friction
* maintain authenticated sessions
* recognize returning users
* support possession-based authentication factors

Device trust remains revocable and auditable to maintain system security.



## Multi-Factor Authentication

Multi-factor authentication (MFA) requires multiple independent authentication factors to verify a user identity.

Authentication factors belong to the following categories:

| Factor Type | Description |
|-|-|
| **Knowledge** | authentication based on information known by the user |
| **Possession** | authentication based on a device or object owned by the user |
| **Inherence** | authentication based on biometric characteristics of the user |

Examples of factor combinations include:

* password + trusted device
* NFC tag + voice biometrics
* facial recognition + PIN

Multi-factor authentication increases security by requiring independent proof of identity across different factor categories.

## Inputs

The Authentication submodule receives authentication signals and credentials used to verify a user identity.

Authentication inputs include:

* username or email identifier
* password credential
* access token
* refresh token
* OAuth authentication callback
* NFC tag detection
* QR code authentication request
* facial recognition signal
* voice biometric signal
* fingerprint authentication signal
* trusted device signature
* PIN credential

## Outputs

The Authentication submodule produces authentication results and identity verification events used by other system components.

Authentication outputs include:

* authentication success
* authentication failure
* identity resolution result
* access token issuance
* token refresh event
* authentication challenge request
* suspicious authentication attempt detection
* session initialization

## Interaction With Other Modules

The Authentication module interacts closely with several other architectural components of NORA.

**Users**  
#definition: provides identity records and identity attributes used during authentication processes.

**Authorization**  
#definition: determines which actions an authenticated identity is allowed to perform.

**Sessions and Dialogue**  
#definition: associates authenticated identities with active interaction sessions.

**Security**  
#definition: monitors authentication attempts and detects suspicious or abnormal authentication behaviour.

**Frontend Interfaces**  
#definition: provide authentication interfaces such as login flows, token handling, and authentication responses.



## Architectural Importance

Authentication acts as the **gateway to system trust**.

Without reliable authentication mechanisms, the system cannot safely:

* associate actions with identities
* protect sensitive resources
* personalize interactions
* enforce authorization policies

Because NORA operates in both digital and physical environments, authentication supports multiple interaction modalities including interfaces, sensors, trusted devices, and remote client applications.

# 1.3 Authorization

## Definition

The **Authorization** submodule determines what actions an authenticated identity is allowed to perform within NORA.

While authentication verifies identity, authorization evaluates whether that identity has sufficient permission to execute a specific action on a specific resource within the current system context.

Authorization therefore answers the question:

> Is this entity allowed to perform this action right now?

Authorization decisions may depend on several factors including:

* the user's roles and permissions
* the requested action
* the target resource
* the current system state
* contextual safety constraints

In NORA, authorization must operate across both digital and physical capabilities, since the system can access data, control hardware, interact with external services, and perform actions in the physical environment.



## Authorization Model

NORA implements a **policy-based access control model** built on top of **role-based permissions**.

Authorization decisions are evaluated through three layers:

1. **Identity**  
   the authenticated identity requesting the action.

2. **Roles and Permissions**  
   the roles assigned to the identity and the permissions associated with those roles.

3. **Contextual Constraints**  
   contextual conditions such as system state, active session, safety rules, and operational environment.

This layered model allows authorization to remain flexible while maintaining strong security guarantees and supporting real-time system conditions.

## Role-Based Access Control (RBAC)

The core authorization mechanism in NORA is **Role-Based Access Control (RBAC)**.

In this model:

* identities are assigned one or more roles
* roles define a set of permissions
* permissions grant access to specific actions or resources

Conceptual structure:

```
User
 ├── roles
 │   ├── user
 │   ├── pro
 │   └── admin
 └── permissions
```


Roles group permissions into predefined capability sets and simplify access management across the system.

The RBAC model used in NORA defines the following roles:

* guest
* user
* pro
* admin

## Permission Model

Permissions define the specific operations an identity is allowed to perform within the system.

Permissions are assigned to roles and determine which actions can be executed on specific resources.

Permissions correspond to the following categories of operations:

* data read operations
* data modification operations
* system command execution
* hardware control operations
* system configuration access

Permissions are represented as structured permission identifiers.

Permission identifier structure:

```
resource.operation
```

Permission identifiers follow a hierarchical naming convention that allows fine-grained control over system capabilities across modules.

## Resource-Based Authorization

Authorization decisions in NORA are evaluated against specific system resources.

Resources represent entities within the system on which actions can be performed.

Resource categories include:

* user accounts
* conversation sessions
* projects
* stored memories
* hardware components
* external integrations
* system configuration

Authorization checks evaluate the following elements:

```
identity + action + resource
```

Authorization therefore verifies whether the requesting identity has the required permission to perform the requested action on the specified resource.

## Context-Aware Authorization

NORA implements **context-aware authorization**.

Authorization decisions depend not only on identity and permissions but also on the current system context.

Contextual constraints include:

* current FSM state
* active user session
* physical user presence
* safety constraints
* system operational mode
* device used for authentication

Context-aware authorization ensures that actions remain consistent with system safety, operational constraints, and real-time conditions.

## Hardware Authorization

NORA controls physical hardware components within the system.

Hardware resources include:

* actuators
* cameras
* microphones
* LEDs
* motors
* connected devices

Because hardware actions affect the physical environment, authorization includes hardware-level restrictions.

Hardware authorization ensures that only identities with the appropriate permissions can access or control hardware resources.

Protected hardware operations include:

* camera capture
* audio recording
* actuator control
* motor movement
* IoT device control

Hardware permissions follow the structured permission identifier model:

```
resource.operation
```

Example hardware permission identifiers:

```
camera.capture
audio.record
servo.control
iot.control
```




## Integration Authorization

NORA interacts with external services through system integrations.

External integration resources include:

* smart home platforms
* messaging systems
* web services
* multimedia platforms

Authorization ensures that only identities with the appropriate permissions can trigger integration actions.

Integration operations include:

* sending messages or notifications
* controlling smart home devices
* accessing external APIs
* retrieving external data sources

Integration authorization combines:

* internal permission checks
* external service authorization mechanisms

## Administrative Authorization

Administrative operations require elevated authorization controls.

Administrative operations include:

* system configuration modification
* user and role management
* system log access
* service management
* maintenance operations

Administrative permissions follow the structured permission identifier model:

```
admin.access
admin.users.manage
admin.system.configure
admin.logs.view
```


Administrative operations are always:

* authenticated
* authorized
* logged for auditing

## Authorization Decision Process

When an action request is received, the authorization system evaluates a sequence of checks.

Authorization evaluation process:

1. verify authenticated identity
2. resolve roles associated with the identity
3. resolve permissions granted by those roles
4. evaluate whether the requested action is permitted
5. evaluate contextual constraints
6. return an authorization decision

Authorization decisions return one of the following results:

* allowed
* denied
* additional authentication required
* action blocked due to system state

## Inputs

The Authorization module receives the information required to evaluate access decisions.

Authorization inputs include:

* authenticated identity
* assigned roles
* permission set
* requested action
* target resource
* current FSM state
* active session information
* system operational mode
* device origin

## Outputs

The Authorization module produces authorization decisions and related system events.

Authorization outputs include:

* authorization granted
* authorization denied
* insufficient permissions
* additional authentication required
* action blocked by safety policy
* authorization decision event

## Interaction With Other Modules

The Authorization module interacts with several architectural components of NORA.

**Users**  
#definition: provides identity records, roles, and permission assignments used during authorization evaluation.

**Authentication**  
#definition: ensures that authorization checks occur only after identity verification.

**Dialogue and Sessions**  
#definition: associates actions with the active interaction session and session context.

**Planning and Agents**  
#definition: validates whether actions proposed by agents are permitted before execution.

**Action and Hardware Control**  
#definition: ensures that physical operations comply with permission policies and safety constraints.

**Security**  
#definition: monitors, logs, and audits authorization decisions.

## Architectural Importance

Authorization ensures controlled operation of the system.

Without a robust authorization layer, NORA cannot safely:

* prevent unauthorized access
* restrict sensitive operations
* protect hardware resources
* enforce safe behaviour
* maintain system integrity

By combining role-based permissions with context-aware policies, NORA enforces safe and controlled interactions across both digital and physical system capabilities.

# 1.4 User Profile

## Definition

The **User Profile** submodule stores persistent personal information and configuration associated with a user identity.

While the **Users** module defines the identity itself, and **Authentication** and **Authorization** determine how that identity accesses the system and which actions it is allowed to perform, the **User Profile** defines how NORA interacts with that identity.

The user profile allows NORA to adapt its behaviour, communication style, and system configuration according to the preferences and characteristics of each individual.

User profiles provide the foundation for personalized interaction and long-term continuity across sessions, devices, and environments.

## Role in the Architecture

The User Profile acts as the **personalization layer** connecting identity information with system behaviour.

It influences several subsystems including:

* dialogue generation
* speech synthesis configuration
* language selection
* interaction preferences
* device associations
* educational and tutoring behaviour
* system personalization

Profiles allow NORA to maintain consistent interaction characteristics for each identity across sessions, devices, and interaction channels.



## Profile Structure

A user profile contains structured attributes that describe preferences, configuration settings, and contextual information associated with the identity.

Profile attributes include:

* identity attributes
* communication preferences
* language configuration
* device associations
* personalization settings
* behavioural configuration

These attributes are stored in the system's **persistent storage layer** and are loaded when an identity becomes active.

## Core Profile Attributes

### Name

The name attribute identifies the person during interaction.

NORA uses this attribute in conversational responses, greetings, and user interface elements.



### Preferred Language

The preferred language defines the default language used by the system when communicating with the identity.

This setting influences:

* speech recognition configuration
* text responses
* voice synthesis
* interface language

The preferred language acts as the baseline configuration for communication.



### Preferred Voice

The preferred voice defines the **text-to-speech configuration** associated with the identity.

Voice configuration parameters include:

* voice model
* speech speed
* speech tone
* voice provider
* emotional expression style



### Interaction Preferences

Interaction preferences define how the identity prefers to communicate with NORA.

Interaction preference attributes include:

* response verbosity
* conversational tone
* tutorial behaviour
* language formality

These preferences influence dialogue generation and agent behaviour.



### Favorite Topics

Favorite topics represent areas of interest associated with the identity.

Topic categories include:

* programming
* science
* music
* languages
* robotics
* cooking

These attributes allow NORA to personalize examples, recommendations, and conversation topics.



### Linked Devices

Linked devices represent devices associated with the identity.

Device types include:

* smartphones
* tablets
* laptops
* NFC tags
* wearable devices

Device associations support:

* trusted device authentication
* automatic identity recognition
* cross-device session continuity
* secure pairing with the robot



### Visual Preferences

Visual preferences define how information is displayed in graphical interfaces.

Interface configuration attributes include:

* theme configuration
* font size
* interface layout
* UI customization



### Educational Level

The educational level attribute determines the complexity of explanations generated by tutoring or educational agents.

Educational levels include:

* beginner
* intermediate
* advanced
* expert



### Routines

Routines represent recurring behavioural patterns associated with the identity.

Routine information includes:

* scheduled activities
* recurring tasks
* habitual interactions

Routine awareness enables proactive assistance.



### Restrictions

Restrictions define behavioural limitations applied to the system for a specific identity.

Restriction categories include:

* parental control rules
* restricted integrations
* limited hardware control

Restrictions ensure safe and appropriate system behaviour.



## Personalization Mechanism

The User Profile enables adaptive behaviour throughout the system.

Profile-driven adaptation includes:

* language configuration selection
* voice configuration activation
* loading identity-specific projects
* conversational tone adjustment
* restoration of previous interaction context

This mechanism allows NORA to maintain **consistent long-term interaction across sessions and devices**.

## Profile Updates

User profiles evolve over time as preferences, configuration, and associated information change.

Profile updates occur through:

* direct user configuration
* frontend settings interfaces
* learned preferences derived from interaction
* device association updates
* administrative modifications

Profile updates are validated to ensure data consistency and prevent invalid configurations.



## Inputs

The User Profile module receives profile-related operations and updates.

Profile inputs include:

* profile creation requests
* profile update requests
* language preference updates
* voice configuration updates
* device association updates
* device removal requests
* learned preference updates
* routine updates



## Outputs

The User Profile module produces profile data and personalization events used by other system components.

Profile outputs include:

* loaded profile configuration
* updated preference state
* device association events
* applied personalization settings
* profile modification events

## Interaction With Other Modules

The User Profile module interacts with several architectural components of NORA.

**Users**  
#definition: provides the identity associated with the profile.

**Dialogue System**  
#definition: applies profile attributes to personalize conversational behaviour.

**Voice Output System**  
#definition: applies the preferred voice configuration defined in the profile.

**Frontend Interfaces**  
#definition: present and modify user profile information through user interfaces.

**Persistent Storage**  
#definition: stores profile attributes and configuration data.

**Planning and Agents**  
#definition: apply user preferences and behavioural configuration to adjust recommendations and system behaviour.



## Profile vs Memory

The architecture distinguishes between **user profiles** and **user memory**.

| Component | Purpose |
|----------|--------|
| User Profile | structured configuration and user preferences |
| User Memory | knowledge learned or stored from interactions |

Profiles define how NORA interacts with an identity, while memory represents information learned or stored about that identity.

Maintaining this separation simplifies system architecture and data management.



## Architectural Importance

The User Profile module provides the personalization layer of the system.

User profiles enable:

* adaptation of communication style
* persistent user preferences
* personalized system behaviour
* consistent interactions across sessions

This capability allows NORA to maintain individualized interaction behaviour for each identity.

# 1.5 Security

## Definition

The **Security** submodule provides the mechanisms required to protect NORA from misuse, unauthorized access, system abuse, and unsafe behaviour.

Security ensures that:

* identities cannot be easily impersonated
* sensitive resources remain protected
* system behaviour remains controlled and predictable
* critical actions remain traceable and auditable
* physical and digital capabilities cannot be abused

While **Authentication** verifies identity and **Authorization** determines what an authenticated identity is allowed to do, the **Security** submodule provides broader protection mechanisms across the system, including prevention, monitoring, detection, and response.

Because NORA operates across both digital and physical environments, security mechanisms protect not only data and services, but also hardware actions, sensor access, and connected external systems.



## Role in the Architecture

The Security submodule acts as a **protective and supervisory layer** across the architecture.

Security mechanisms apply safeguards to multiple parts of the system, including:

* backend APIs
* authentication flows
* authorization decisions
* hardware control
* persistent storage
* external integrations
* active sessions
* administrative operations

The Security submodule provides mechanisms for:

* preventing unauthorized access
* detecting abnormal behaviour
* preserving system traceability
* maintaining operational safety

## Security Objectives

The Security submodule supports several core objectives:

* protection of identities and sessions
* protection of private and sensitive data
* prevention of API and service abuse
* protection of hardware and actuator control
* traceability of critical actions
* detection of suspicious or abnormal behaviour
* support for incident response and recovery

These objectives apply to both user interactions and administrative operations.



## Rate Limiting

Rate limiting restricts the frequency of requests or operations within a defined time interval.

This mechanism prevents:

* brute-force authentication attempts
* API abuse
* repeated command flooding
* excessive system load
* resource exhaustion

Rate limiting is applied to:

* login endpoints
* API routes
* external integration calls
* resource-intensive operations
* repeated hardware commands

In NORA, rate limiting is particularly important because certain operations may consume computational resources, external API quotas, or trigger repeated physical actions.

## Access Logging

The system records logs of security-relevant access events.

Access events recorded by the system include:

* authentication attempts
* successful logins
* failed login attempts
* token refresh operations
* session creation
* session termination
* access to protected endpoints

Access logging supports:

* operational debugging
* security monitoring
* usage analysis
* incident investigation

## Audit Logging

Audit logging records high-impact or sensitive operations in a structured and traceable form.

Operations recorded by audit logging include:

* system configuration changes
* permission modifications
* user management operations
* hardware control commands
* access to private memory or personal data
* execution of administrative operations

Each audit record contains:

* acting identity
* session identifier
* timestamp
* requested action
* affected resource
* decision result
* source device or origin

Audit logging ensures accountability and traceability across the system.

## Session Monitoring

The Security submodule monitors active sessions associated with users, devices, or administrative interfaces.

Session monitoring provides mechanisms for:

* listing active sessions
* detecting unusual activity
* enforcing inactivity timeouts
* terminating sessions when required
* identifying concurrent access patterns

Tracked session data includes:

* user identity
* session identifier
* authentication method
* device used
* request origin
* creation timestamp
* last activity timestamp

Session monitoring maintains visibility over active connections and system access.



## Token Revocation

The system supports revocation of active authentication tokens before their natural expiration.

Token revocation is required when:

* a device is lost or stolen
* suspicious activity is detected
* permissions have changed
* a user logs out
* an account is disabled

Revocation ensures that previously issued credentials cannot continue to be used after trust has been removed.

## Endpoint Protection

The Security submodule protects exposed backend interfaces against invalid, malicious, or abusive requests.

Endpoint protection mechanisms include:

* authentication enforcement
* authorization validation
* input validation
* request size limits
* schema validation
* security headers
* origin restrictions
* rate limiting

Endpoint protection is critical in NORA because backend services expose access to hardware, memory, sessions, and external integrations.



## Failed Attempt Protection

Repeated failed authentication or access attempts indicate potential brute-force attacks, misconfigured clients, or abusive behaviour.

The system enforces protections such as:

* temporary account lockout
* temporary IP or device restriction
* exponential retry delay
* additional verification challenges
* security alerts

These protections reduce the risk of automated attacks against authentication and access layers.

## Traceability of Sensitive Actions

Sensitive actions remain traceable to a specific identity and execution context.

Sensitive actions include:

* activating microphones or cameras
* moving robotic components
* controlling connected devices
* accessing private user data
* modifying system configuration
* granting permissions

Traceability links each action to:

* user identity or system actor
* session identifier
* timestamp
* source device or interface
* resulting decision or system effect

Traceability supports debugging, auditing, and security analysis.



## Hardware Safety Protections

Because NORA interacts with the physical environment, the Security submodule also protects hardware actions.

Protected hardware operations include:

* moving servos or motors
* activating cameras or microphones
* controlling actuators
* sending commands to external IoT devices
* triggering electrical components

Hardware safety protections include:

* permission checks
* system state validation
* motion limits
* emergency stop mechanisms
* device availability checks
* safe-mode restrictions
* physical presence verification

These safeguards prevent accidental misuse, unsafe actions, and unauthorized physical control.

## Integration Security

NORA communicates with external services such as:

* calendars
* email systems
* smart home platforms
* messaging services
* multimedia providers
* internet APIs

Security mechanisms ensure that these integrations operate safely.

Integration security controls include:

* permission checks before external actions
* secure credential storage
* scoped access tokens
* request validation
* logging of external actions

These controls prevent abuse of connected platforms and limit the impact of compromised integrations.



## Anomaly Detection

The Security submodule detects abnormal behaviour that indicates potential misuse, compromise, or system malfunction.

Detected anomalies include:

* repeated failed login attempts
* abnormal command frequency
* unexpected hardware usage
* unusual session patterns
* suspicious administrative access
* excessive API traffic

When an anomaly is detected, the system may respond by:

* generating an alert
* restricting actions
* requiring reauthentication
* revoking tokens
* logging the event for investigation

## Incident Response Support

The Security submodule provides controlled response mechanisms for security incidents.

Response actions include:

* revoking sessions
* disabling accounts
* blocking specific actions
* switching the system to safe mode
* notifying administrators
* preserving logs for analysis

These mechanisms contain security incidents and limit the impact of abuse or compromise.



## Inputs

Inputs handled by the Security module include:

* authentication attempts
* authorization decisions
* API requests
* token validation events
* session activity
* hardware control commands
* integration requests
* configuration changes
* repeated failed access attempts
* anomaly signals



## Outputs

Outputs generated by the Security module include:

* access denied
* session terminated
* token revoked
* account temporarily locked
* action blocked by policy
* safe mode activated
* security alert generated
* audit log entry stored
* anomaly event recorded

## Interaction With Other Modules

The Security module interacts with several architectural components.

**Users**  
#definition: associates security-relevant events with system identities.

**Authentication**  
#definition: monitors authentication flows and protects login mechanisms.

**Authorization**  
#definition: enforces secure execution of authorization decisions.

**Backend Services**  
#definition: protects APIs, endpoints, and internal service boundaries.

**Action and Hardware Control**  
#definition: applies safety restrictions to physical operations.

**Persistent Storage**  
#definition: stores security logs, audit records, and incident data.

**Administrative Interfaces**  
#definition: monitors and protects privileged operations.



## Architectural Importance

The Security submodule ensures that NORA operates in a controlled, trustworthy, and safe manner.

Without strong security controls, the system becomes exposed to:

* unauthorized access
* abuse of system capabilities
* loss of traceability
* compromise of personal data
* unsafe hardware behaviour
* misuse of external integrations

By combining prevention, monitoring, traceability, and response mechanisms, the Security submodule ensures that NORA remains secure, auditable, and operationally reliable across both digital and physical domains.



## Internal Architecture Overview

The **Identity, Access and Security** module is organized as a layered architecture responsible for identity management, authentication, authorization, personalization, and system protection.

The module is composed of five main submodules that work together to control access, protect resources, and ensure safe operation of the NORA system.

### Architectural Structure

```
Identity, Access and Security
│
├── Users
│ ├── identity model
│ ├── user types
│ │ ├── guest
│ │ ├── user
│ │ ├── pro
│ │ └── admin
│ ├── role-based identity model
│ ├── device associations
│ ├── identity lifecycle
│ ├── identity inputs
│ └── identity outputs
│
├── Authentication
│ ├── credential-based authentication
│ │ ├── username / email login
│ │ └── password verification
│ ├── token-based authentication
│ │ ├── access tokens
│ │ └── refresh tokens
│ ├── OAuth authentication
│ ├── biometric authentication
│ │ ├── facial recognition
│ │ ├── voice biometrics
│ │ └── fingerprint authentication
│ ├── proximity authentication
│ │ ├── NFC / RFID
│ │ ├── QR codes
│ │ ├── Bluetooth presence
│ │ └── Wi-Fi proximity
│ ├── trusted devices
│ ├── multi-factor authentication
│ ├── authentication inputs
│ └── authentication outputs
│
├── Authorization
│ ├── policy-based access control
│ ├── role-based permissions (RBAC)
│ ├── permission model
│ ├── resource-based authorization
│ ├── context-aware authorization
│ │ ├── system state constraints
│ │ ├── session context
│ │ ├── device origin
│ │ └── safety conditions
│ ├── hardware authorization
│ ├── integration authorization
│ ├── administrative authorization
│ ├── authorization decision process
│ ├── authorization inputs
│ └── authorization outputs
│
├── User Profile
│ ├── profile attributes
│ │ ├── name
│ │ ├── preferred language
│ │ ├── preferred voice
│ │ ├── interaction preferences
│ │ ├── favourite topics
│ │ ├── linked devices
│ │ ├── visual preferences
│ │ ├── educational level
│ │ ├── routines
│ │ └── restrictions
│ ├── personalization mechanism
│ ├── profile updates
│ ├── profile inputs
│ └── profile outputs
│
├── Security
│ ├── security objectives
│ ├── rate limiting
│ ├── endpoint protection
│ ├── failed attempt protection
│ ├── access logging
│ ├── audit logging
│ ├── session monitoring
│ ├── token revocation
│ ├── traceability of sensitive actions
│ ├── hardware safety protections
│ ├── integration security
│ ├── anomaly detection
│ ├── incident response support
│ ├── security inputs
└─└── security outputs
```

### Architectural Layers

The submodules operate in complementary layers:

| Layer | Responsibility |
|------|---------------|
| **Identity Layer** | Defines actors interacting with the system |
| **Authentication Layer** | Verifies identity claims |
| **Authorization Layer** | Determines permitted actions |
| **Personalization Layer** | Adapts system behaviour to each user |
| **Security Layer** | Protects system integrity and monitors activity |

Together, these layers establish the **trust boundary of the NORA architecture**, ensuring that every action performed by the system is identifiable, authorized, monitored, and safe.