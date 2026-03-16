# 7. Action and Expression

## Definition

The Action and Expression module is the architectural layer responsible for producing externally observable effects and externally effective operations in NORA.

Within the architecture, this module contains the mechanisms through which the system executes operations and expresses internal system state toward humans, devices, digital services, and the surrounding environment.

An action is an externally effective operation executed by the system.

An action is a bounded execution unit that produces an effect outside the internal cognitive processes of NORA.

An action may affect:

* a human user
* a robot hardware component
* a local interface
* an external device
* a remote software system
* a connected service
* the surrounding physical environment

Examples of actions include:

* emitting speech
* rendering information on a display
* changing LED state
* moving a mechanical component
* sending a digital message
* triggering an external service
* controlling a connected device

An expression is an externally perceivable manifestation through which NORA exposes internal state, feedback, information, or behavioural modulation.

Expressions make system activity understandable and observable to humans and external observers.

Examples of expression include:

* spoken responses
* visual indicators
* status lights
* sound effects
* posture changes
* confirmation signals
* warning signals

The Action and Expression module defines the architectural domain through which NORA produces behaviour that can be perceived outside the internal system processes.

## Architectural Role

The Action and Expression module is the output realization layer of the NORA architecture.

It represents the architectural boundary where internal processes become external effects.

The module receives structured execution intentions from upstream modules and transforms them into concrete operations performed through output channels.

Within the global architecture, the operational flow can be represented as:

Perception and Cognitive Processing → Planning and Decision → Action and Expression → Humans, Devices, Digital Systems, Environment

The module does not determine objectives, intentions, or plans.

Those elements are defined by upstream modules such as the cognitive core and planning systems.

The Action and Expression module defines how an approved operation is executed and through which channel the effect is produced.

The module therefore specifies:

* the available output channels
* the execution mechanisms associated with each channel
* the primitives used to perform output operations
* the synchronization of simultaneous outputs
* the constraints applied during execution

## Core Architectural Concepts

To define the structure of the module, several architectural concepts are introduced.

### action

An action is a discrete execution unit performed by the system toward an external target.

An action produces a concrete effect.

Actions are triggered by execution requests produced by planning systems, dialogue systems, or internal processes.

### expression

An expression is an observable manifestation of internal system activity.

Expressions communicate information, feedback, or behavioural signals to humans or external observers.

### output channel

An output channel is the architectural pathway through which an action or expression is emitted.

Examples of output channels include:

* voice
* audio playback
* display output
* LED signaling
* mechanical movement
* camera operations
* network communication
* IoT device control

### execution primitive

An execution primitive is the smallest standardized operation that can be performed by an output channel.

Examples include:

* speak text
* play sound
* render text
* display image
* set LED color
* move servo
* capture image
* send notification
* toggle device state

Execution primitives are used by planners or agents to trigger concrete actions through the Action and Expression layer.

### output target

An output target is the destination entity toward which an action or expression is directed.

Examples include:

* current user
* robot display
* robot speaker
* LED controller
* motor controller
* camera subsystem
* messaging platform
* smart device

### multimodal output

A multimodal output is a coordinated set of actions or expressions performed through multiple output channels simultaneously.

Examples include:

* speech accompanied by screen text
* spoken confirmation combined with LED signals
* navigation explanation combined with map display

### execution context

The execution context is the structured runtime information required to perform an action correctly.

Execution context may include:

* active user identity
* selected language
* active dialogue session
* system state
* permissions
* hardware availability
* target device identity

### execution constraints

Execution constraints are conditions that regulate or limit the execution of actions and expressions.

Examples include:

* speech output disabled while the system is listening
* motion disabled under unsafe hardware conditions
* device control disabled without authorization

## Scope of the Module

The Action and Expression module includes all mechanisms responsible for producing externally observable behaviour or externally effective operations.

Its scope includes:

* speech output
* audio playback
* visual output on displays
* LED signalling
* physical movement and posture
* camera-triggered operations
* control of connected devices
* digital communication with external systems

The module also includes mechanisms responsible for:

* coordinating simultaneous outputs
* executing output primitives
* enforcing runtime execution constraints

The module does not include:

* sensory acquisition
* semantic interpretation
* intent detection
* planning and task selection
* memory storage
* identity verification
* authorization policy definition
* hardware infrastructure definition

Those concerns belong to other architectural modules.

## Output Domains

Outputs generated by the module can be grouped into several domains.

### Human communication outputs

Outputs directed toward human understanding and interaction.

Examples include:

* spoken responses
* visual feedback
* confirmation signals
* alerts
* guidance cues

### Physical embodiment outputs

Outputs directed toward the robot body and visible physical behaviour.

Examples include:

* head movement
* body posture
* LED signalling
* mechanical gestures

### Digital system outputs

Outputs directed toward software systems and digital platforms.

Examples include:

* notifications
* messages
* service triggers
* API actions

### Environmental control outputs

Outputs directed toward connected devices or smart environments.

Examples include:

* lights
* smart plugs
* appliances
* home automation systems

## Separation From Planning

The architecture maintains a structural separation between planning and execution.

Planning modules determine which operations must occur.

The Action and Expression module performs the operations.

Planning defines:

* the objective
* the target
* the required operation
* the order of execution

Action and Expression defines:

* the output channel
* the execution primitive
* the output target
* the runtime execution of the effect

## Main Responsibilities

The module performs several architectural responsibilities.

### Output Realization

Transforms structured execution requests into concrete external effects.

### Channel Execution

Activates the primitives associated with each output channel.

### Multimodal Coordination

Coordinates outputs emitted through multiple channels.

### Runtime Consistency

Ensures outputs remain compatible with the current system state.

### Safe Execution

Applies constraints that protect the system, the environment, and users from unsafe behaviour.

### Behaviour Expression

Produces observable signals that communicate system responses and internal state.

## Typical Inputs

Inputs received by the module include:

* generated response text
* planner execution requests
* agent actions
* system alerts
* confirmation requests
* device control instructions
* media playback instructions
* notification requests

## Typical Outputs

Outputs produced by the module include:

* spoken responses
* sound playback
* displayed information
* LED state changes
* mechanical movement
* captured images or video
* smart device control
* digital notifications

## Relationship With Other Modules

Cognitive Core

Provides behavioural state information that influences how outputs are expressed.

Dialogue and Session System

Provides conversational content that becomes spoken or visual output.

Planning, Interpretation and Agents

Produces structured execution requests.

Identity, Access and Security

Defines authorization constraints that regulate which actions are allowed.

Backend and Application

Provides services that support digital communication or remote operations.

Infrastructure and Hardware

Provides the physical devices through which actions and expressions are emitted.

Frontend and Visualization

Displays or mirrors certain outputs for user or administrative interfaces.

## Internal Structure

The Action and Expression module contains several specialized output submodules.

* Voice Output
* Sound and Multimedia
* Screen and Visual Output
* Emotional Expression
* Movement and Physical Behaviour
* Camera Actions
* IoT and Device Control
* External Communication

Each submodule defines one output domain through which NORA produces observable behaviour.

Together these submodules form the execution layer that converts internal decisions into real-world effects.

## Architectural Importance

The Action and Expression module is the architectural layer in which internal system decisions become externally observable behaviour or externally effective operations.

Without this module the system could perceive, reason, plan, and maintain context, but it would not possess a defined mechanism for expressing responses or performing operations in the external world.

This module therefore provides the bridge between internal cognition and external interaction.

# 7.1 Voice Output

## Definition

The Voice Output subsystem is the architectural component responsible for producing spoken language from NORA toward human users.

This subsystem converts textual linguistic content into audible speech that can be perceived through the robot's audio hardware.

Voice Output defines the mechanisms through which the system performs verbal communication as part of its observable behaviour.

Within the architecture, voice output is an output channel belonging to the Action and Expression module.

The subsystem transforms structured textual responses into synthesized audio signals emitted through the robot speakers.

## Architectural Role

The Voice Output subsystem realizes verbal communication between NORA and human users.

It is the architectural layer that materializes spoken responses.

The subsystem receives structured textual content produced by upstream modules and converts that content into speech.

The operational flow of the subsystem can be represented as:

textual response → speech synthesis → audio signal → speaker output → human listener

The subsystem therefore connects linguistic content generated by internal processes with the physical audio interface of the robot.

Voice Output performs the following architectural functions:

* transforming text into speech audio
* controlling acoustic parameters of the voice
* managing playback of synthesized audio
* synchronizing speech with other output channels

## Core Architectural Concepts

### spoken response

A spoken response is a verbal message produced by NORA and delivered through synthesized speech.

Spoken responses represent the primary auditory communication mechanism of the system.

Examples include:

* answering questions
* confirming actions
* providing explanations
* giving instructions

### speech synthesis

Speech synthesis is the process through which textual content is converted into an audio waveform representing human-like speech.

Speech synthesis produces audio data that can be reproduced by the robot speakers.

### speech markup

Speech markup is structured metadata embedded in textual responses that controls pronunciation, pacing, and expressive characteristics of the synthesized speech.

Speech markup modifies how text is spoken without changing the linguistic content.

### voice profile

A voice profile defines the acoustic characteristics of the synthesized voice used by NORA.

Voice profiles determine properties such as:

* voice identity
* pitch
* speech rate
* speaking style

### language configuration

Language configuration defines the linguistic rules used during speech synthesis.

Language configuration includes:

* selected spoken language
* pronunciation rules
* compatible voice models

### audio emission

Audio emission is the physical playback of synthesized speech through the robot speakers.

Audio emission converts digital audio data into audible sound.

## Subsystem Components

### Text-to-Speech Engine

The Text-to-Speech Engine is the component that converts textual input into synthesized speech audio.

The engine receives text and produces an audio waveform representing spoken language.

The output of the engine is digital audio data that can be reproduced by the robot audio hardware.

### Speech Markup Processor

The Speech Markup Processor interprets markup instructions embedded in textual responses.

These instructions influence the expressive properties of the synthesized speech.

Speech markup may specify:

* pauses
* emphasis
* phonetic corrections
* prosody adjustments
* speech rate modifications

### Voice Configuration

Voice configuration defines the acoustic parameters associated with the active voice profile.

These parameters determine how synthesized speech sounds when produced by the system.

Configurable parameters include:

* voice identity
* pitch
* speech rate
* expressive tone

### Language Selection

Language selection determines the language used during speech synthesis.

The subsystem selects the appropriate voice model and pronunciation rules corresponding to the active language.

### Audio Playback System

The Audio Playback System is responsible for delivering synthesized speech through the robot speakers.

This component performs:

* buffering of audio data
* streaming or playback control
* volume management
* synchronization with other audio sources

## Speech Execution Pipeline

Voice Output follows a structured execution sequence.

The pipeline contains the following stages:

1. reception of textual response
2. optional speech markup processing
3. speech synthesis
4. audio playback

Each stage transforms the input representation into the next stage of the speech production process.

## Synchronization With System State

Voice Output operates in coordination with other modules of the system.

Speech execution respects runtime state conditions.

Examples of coordination rules include:

* speech output pauses when the system enters a listening state
* urgent alerts interrupt ongoing speech
* confirmations occur immediately after action completion

These coordination rules maintain consistency between speech output and overall robot behaviour.

## Personalization

Voice Output supports configuration parameters associated with individual users or interaction contexts.

Possible parameters include:

* preferred voice
* preferred language
* speaking speed
* pronunciation assistance

These parameters may be stored in user profiles and applied during speech synthesis.

## Typical Actions

Typical actions produced by this subsystem include:

* speaking answers to questions
* confirming executed commands
* explaining procedures
* reading text aloud
* spelling words
* providing pronunciation feedback

## Typical Outputs

Outputs produced by the subsystem include:

* spoken responses
* confirmations
* explanations
* pronunciation demonstrations
* alerts

## Relationship With Other Modules

Dialogue and Session System

Provides textual responses that become spoken output.

Planning, Interpretation and Agents

Determines when verbal responses are required.

Identity, Access and Security

Determines permissions for speech actions when relevant.

Infrastructure and Hardware

Provides the physical audio hardware used for speech playback.

Action and Expression Module

Defines the voice channel as part of the system's output architecture.

## Architectural Importance

Voice Output is one of the primary communication mechanisms between NORA and human users.

Spoken language allows users to receive information without requiring visual attention.

The subsystem therefore provides the auditory interface through which the system communicates verbally with humans.

# 7.2 Sound and Multimedia

## Definition

The Sound and Multimedia subsystem is the architectural component responsible for producing and managing non-conversational audio and multimedia playback generated or controlled by NORA.

This subsystem handles auditory outputs that are not part of spoken dialogue. These outputs include music playback, sound effects, alarms, notifications, and other media-based audio experiences.

Within the Action and Expression module, the Sound and Multimedia subsystem defines the mechanisms through which NORA emits non-verbal audio signals and multimedia audio content through its audio hardware.

## Architectural Role

The Sound and Multimedia subsystem realizes non-conversational auditory outputs within the NORA architecture.

It receives structured playback requests from upstream modules and produces audio signals through the robot speakers or external audio devices.

The operational flow of the subsystem can be represented as:

media request → media retrieval → playback control → audio signal → speaker output → human listener

The subsystem therefore connects media content and system sound signals with the physical audio interface of the robot.

## Core Architectural Concepts

### media playback

Media playback is the reproduction of audio content through the robot audio hardware.

Playback may involve continuous streams such as music or radio, or short audio signals such as sound effects.

### sound signal

A sound signal is a short non-verbal audio cue emitted by the system.

Sound signals communicate system states or events.

Examples include:

* notification tones
* completion sounds
* warning signals

### media source

A media source is the origin from which audio content is obtained.

Media sources may include:

* locally stored audio files
* streaming platforms
* dynamically generated audio

### playback control

Playback control defines the operations used to manage audio reproduction.

Typical playback control primitives include:

* start playback
* pause playback
* resume playback
* stop playback
* adjust volume
* skip track

### media queue

A media queue is an ordered structure that organizes playback requests.

The queue determines the sequence in which media items are reproduced.

## Subsystem Components

### Media Retrieval Component

The Media Retrieval Component obtains audio content from the selected media source.

The component may access local storage or external services.

### Playback Controller

The Playback Controller manages the state of media reproduction.

This component performs operations such as starting, pausing, resuming, and stopping playback.

### Audio Mixer

The Audio Mixer coordinates multiple audio signals produced by the system.

This component manages volume levels and prevents conflicts between simultaneous audio sources.

### Media Queue Manager

The Media Queue Manager maintains the ordered list of pending media items.

This component controls sequential playback and interruption handling.

### Audio Output Interface

The Audio Output Interface delivers audio signals to the robot speakers or connected audio devices.

## Audio Sources

Audio content handled by the subsystem may originate from several types of sources.

### Local media

Audio files stored locally on the robot.

Examples include:

* notification sounds
* alert tones
* prerecorded audio clips

### Streaming media

Audio streams provided by external services.

Examples include:

* music streaming platforms
* online radio streams

### Generated audio

Audio produced dynamically by software components.

Examples include:

* procedural sound effects
* generated signals

## Playback Execution Pipeline

Audio playback follows a structured execution sequence.

1. reception of media request
2. media source selection
3. media retrieval
4. playback control activation
5. audio emission through speakers

## Synchronization With Other Modules

The subsystem operates in coordination with other output mechanisms.

Examples of coordination conditions include:

* speech output taking priority over background media
* alerts interrupting ongoing playback
* playback resuming after interruption

These coordination rules maintain coherent system behaviour when multiple audio outputs are active.

## Typical Actions

Typical actions produced by this subsystem include:

* playing music
* streaming radio
* emitting notification sounds
* triggering alarm signals
* reproducing multimedia audio

## Typical Outputs

Outputs produced by the subsystem include:

* music playback
* radio streams
* sound effects
* alarms
* notification tones

## Relationship With Other Modules

Dialogue and Session System

Produces requests for multimedia playback triggered by user interaction.

Planning, Interpretation and Agents

Determines when media playback or audio signals must be produced.

Voice Output

Coordinates speech synthesis with other audio outputs.

Infrastructure and Hardware

Provides the audio hardware used for sound reproduction.

IoT and Device Control

May route audio signals toward external speakers or connected devices.

## Architectural Importance

The Sound and Multimedia subsystem extends the auditory capabilities of NORA beyond speech.

Through music playback, sound cues, and media streaming, the subsystem provides additional auditory channels that communicate system state, deliver entertainment content, and enrich human-robot interaction.

This subsystem therefore complements spoken dialogue by providing non-verbal audio feedback and multimedia audio experiences.

# 7.3 Screen / Local UI

## Definition

The Screen / Local UI subsystem is the architectural component responsible for generating and controlling all visual output presented on the robot's physical display.

This subsystem produces graphical information, textual content, visual indicators, and interactive interface elements visible on the robot screen.

Within the Action and Expression module, the Screen / Local UI subsystem defines the visual output channel through which NORA communicates information and state to human users.

## Architectural Role

The Screen / Local UI subsystem realizes visual communication between NORA and human users through the robot display.

The subsystem receives structured visual output requests from upstream modules and transforms them into rendered visual elements.

The operational flow of the subsystem can be represented as:

visual request → visual composition → graphical rendering → display signal → screen output → human observer

The subsystem therefore connects internal system information with the physical display hardware of the robot.

## Core Architectural Concepts

### visual message

A visual message is structured information presented through the robot screen.

Visual messages communicate textual, graphical, or symbolic information to the user.

Examples include:

* textual responses
* notifications
* instructions

### graphical element

A graphical element is a visual component rendered on the display surface.

Examples include:

* text blocks
* images
* icons
* charts
* indicators

### visual state indicator

A visual state indicator is a graphical signal representing the internal state of the system.

Examples include:

* listening indicator
* thinking indicator
* speaking indicator
* connection status

### interactive interface element

An interactive interface element is a visual component that allows user interaction through the screen.

Examples include:

* buttons
* menus
* lists
* navigation panels

### visual layout

A visual layout is the spatial arrangement of graphical elements displayed on the screen.

Layouts organize visual information into structured interfaces.

## Subsystem Components

### Rendering Engine

The Rendering Engine generates graphical frames from structured visual descriptions.

The engine converts interface definitions into pixel data suitable for display.

### Layout Manager

The Layout Manager determines the spatial organization of visual elements on the display.

This component arranges text, images, widgets, and indicators within the screen space.

### UI Element Library

The UI Element Library defines reusable visual components used to build interface layouts.

Examples include:

* text components
* image containers
* buttons
* lists
* indicators

### Media Renderer

The Media Renderer displays images or video content on the screen.

This component handles the rendering of multimedia visual data.

### Display Interface

The Display Interface transmits rendered graphical frames to the physical screen hardware.

This component performs the final delivery of visual output.

## Types of Visual Output

### Text Display

The subsystem displays textual information produced by dialogue or agent modules.

Examples include:

* answers to questions
* instructions
* summaries
* notifications

### Image Display

Images may be presented on the screen to provide visual context or illustrate information.

Examples include:

* illustrative images
* recognition results
* captured photos

### Video Display

Video playback allows continuous visual media to be shown on the display.

Examples include:

* demonstrations
* streaming content
* camera preview

### Camera Visualization

Camera visualization displays the live feed produced by the robot camera.

The subsystem may render overlays such as detection labels or bounding boxes on top of the video stream.

### Interactive Interface

The subsystem renders interface structures that allow user interaction through the screen.

Examples include:

* menus
* buttons
* navigation panels

### System State Visualization

The subsystem displays graphical indicators representing the internal status of the robot.

Examples include:

* listening state
* processing state
* speaking state

### Emotional Visual Expression

The display may present graphical representations of the robot emotional state.

Examples include:

* animated facial expressions
* eye animations
* mood indicators

### Graphical Information

The subsystem may present structured visual data.

Examples include:

* charts
* progress indicators
* maps
* diagrams

### QR Code Display

The subsystem may generate QR codes that encode information for external devices.

Examples include:

* device pairing
* link sharing
* authentication

## Visual Execution Pipeline

Visual output follows a structured execution sequence.

1. reception of visual request
2. visual layout composition
3. graphical rendering
4. frame transmission to display

## Synchronization With Other Outputs

Visual output is coordinated with other expression channels.

Examples of coordination include:

* subtitles synchronized with speech output
* emotional animations synchronized with voice tone
* camera preview during photo capture
* maps displayed during spoken navigation instructions

## Typical Actions

Typical actions produced by this subsystem include:

* displaying text messages
* showing images
* playing video on the screen
* rendering menus
* presenting charts or diagrams
* displaying QR codes

## Typical Outputs

Outputs produced by the subsystem include:

* text messages
* images
* video frames
* camera feeds
* interface elements
* state indicators
* visual animations

## Relationship With Other Modules

Dialogue and Session System

Provides textual responses and interaction content displayed on the screen.

Planning, Interpretation and Agents

Produces requests for visual output or interface changes.

Voice Output

Coordinates subtitles and visual feedback with spoken responses.

Infrastructure and Hardware

Provides the physical display device used for visual output.

Action and Expression Module

Defines the screen interface as part of the system output architecture.

## Architectural Importance

The Screen / Local UI subsystem provides the primary visual communication channel between NORA and human users.

Through text, graphics, video, and interactive elements, the subsystem enables the robot to communicate structured information that cannot be easily conveyed through speech alone.

This visual channel complements speech, sound, and physical movement to support multimodal human-robot interaction.

# 7.4 Emotional Expression

## Definition

The Emotional Expression subsystem is the architectural component responsible for expressing the internal emotional state of NORA through observable behaviours.

This subsystem translates internal emotional states into coordinated signals emitted through visual, auditory, and physical output channels.

Within the Action and Expression module, the Emotional Expression subsystem defines how emotional states produced by the Cognitive Core become externally perceivable behaviours.

## Architectural Role

The Emotional Expression subsystem materializes the emotional state of the system as observable expressions.

The emotional state itself is produced by the Emotional State model located in the Cognitive Core. The Emotional Expression subsystem receives that state representation and produces coordinated expressive outputs.

The operational flow of the subsystem can be represented as:

emotional state → expression mapping → multimodal output signals → human perception

This separation defines two distinct architectural responsibilities:

* the Cognitive Core determines the internal emotional state
* the Emotional Expression subsystem determines how that state is externally expressed

## Core Architectural Concepts

### emotional state

An emotional state is an internal system condition representing affective or behavioural modulation within the Cognitive Core.

Examples include:

* curiosity
* focus
* satisfaction
* alertness

### emotional expression

An emotional expression is a coordinated set of observable signals that represent an internal emotional state.

Expressions communicate affective cues to human observers.

### expression pattern

An expression pattern is the structured mapping between an internal emotional state and the set of output signals used to represent it.

Expression patterns define which channels are activated and how those channels behave.

### expression intensity

Expression intensity defines the magnitude or strength of an expressive signal.

Intensity determines the visual, auditory, or physical prominence of the expression.

### multimodal expression

A multimodal expression is an emotional expression produced through multiple output channels simultaneously.

Channels may include:

* visual display
* voice modulation
* LED signals
* physical movement

## Subsystem Components

### Expression Mapping Engine

The Expression Mapping Engine associates internal emotional states with expression patterns.

The engine determines which output signals correspond to each emotional state.

### Expression Coordinator

The Expression Coordinator synchronizes expressive signals across multiple output channels.

This component ensures that visual, auditory, and physical expressions remain consistent.

### Expression Intensity Controller

The Expression Intensity Controller regulates the magnitude of expressive behaviour.

This component determines the strength of animations, voice tone modulation, lighting intensity, or motion amplitude.

### Channel Expression Interfaces

Channel Expression Interfaces connect emotional expression with specific output subsystems.

Examples include:

* screen animation interface
* voice modulation interface
* LED control interface
* motion control interface

## Expression Channels

Emotional expressions may be emitted through several output channels.

### Visual facial expression

Graphical elements displayed on the robot screen represent expressive facial states.

Examples include:

* animated eyes
* facial icons
* attention indicators

### Voice modulation

Speech output may vary vocal characteristics to reflect emotional expression.

Examples include:

* energetic tone
* calm tone
* alert tone

### LED signalling

LED lighting patterns represent emotional or operational states.

Examples include:

* color changes
* pulsing effects
* flashing signals

### Physical movement

Robot body movement reinforces expressive behaviour.

Examples include:

* head tilt
* nodding
* posture changes

## Expression Mapping

The subsystem maintains mappings between emotional states and expression patterns.

Example mapping:

Emotional state: curiosity

Expression pattern:

* animated attentive eyes
* slight head tilt
* soft voice tone
* pulsing LED signal

Expression mappings ensure consistent representation of emotional states.

## Context Adaptation

Expression behaviour adapts to the current interaction context.

Context variables may include:

* interaction type
* system state
* environment conditions

Context adaptation regulates the visibility or intensity of expressive behaviour.

## Synchronization With System State

Emotional expression operates in coordination with system operational states.

Examples include:

Listening state:

* attentive visual indicators
* subtle LED activity

Processing state:

* thinking animation

Error state:

* warning visual signals

## Typical Actions

Typical actions produced by this subsystem include:

* displaying facial animations
* adjusting speech tone
* emitting LED patterns
* performing expressive movements

## Typical Outputs

Outputs produced by the subsystem include:

* facial animations
* eye movements
* LED color patterns
* voice tone modulation
* expressive body movement

## Relationship With Other Modules

Cognitive Core

Provides the internal emotional state used as input for expression.

Voice Output

Receives voice modulation parameters derived from emotional expression.

Screen / Local UI

Displays graphical expressions associated with emotional states.

Infrastructure and Hardware

Provides LEDs and mechanical components used for expressive signals.

Action and Expression Module

Defines the emotional expression subsystem as part of the system output architecture.

## Architectural Importance

The Emotional Expression subsystem allows NORA to communicate internal state information through observable behaviours.

By exposing emotional cues through multiple output channels, the subsystem improves interpretability of system behaviour and enhances human-robot interaction.

The subsystem therefore provides the expressive layer through which internal emotional states become perceivable to human users.

# 7.5 LEDs

## Definition

The LEDs subsystem is the architectural component responsible for controlling all LED-based visual signals produced by NORA.

This subsystem generates light signals through the robot LED hardware in order to communicate system information, operational states, and expressive cues.

Within the Action and Expression module, the LEDs subsystem defines the light-based visual output channel of the system.

## Architectural Role

The LEDs subsystem produces visual signals that are observable in the robot physical environment.

The subsystem receives structured LED control requests and transforms them into light emissions generated by the robot LED hardware.

The operational flow of the subsystem can be represented as:

LED request → pattern selection → signal generation → LED hardware emission → human perception

The subsystem therefore connects internal system information with the robot light signaling interface.

## Core Architectural Concepts

### LED signal

An LED signal is a visual light emission produced by the robot LED hardware.

LED signals communicate system state, interaction feedback, or expressive cues.

### LED color

LED color defines the chromatic value emitted by the LED hardware.

Colors are used as symbolic indicators of system conditions or expressive states.

### LED pattern

An LED pattern is a temporal sequence of light changes generated by the subsystem.

Patterns define how color and brightness evolve over time.

### LED intensity

LED intensity defines the brightness level of the emitted light signal.

Intensity determines the visual prominence of the signal.

### LED event

An LED event is a trigger that produces a change in LED behavior.

Events may originate from system state transitions, user interactions, or operational alerts.

## Subsystem Components

### Pattern Controller

The Pattern Controller selects and activates the LED pattern corresponding to the requested signal.

### Color Controller

The Color Controller manages the chromatic configuration of the LED hardware.

### Brightness Controller

The Brightness Controller regulates the intensity level of the emitted light.

### LED Driver Interface

The LED Driver Interface transmits control signals to the LED hardware components.

## Types of LED Signals

### Emotional signals

LED signals may represent expressive cues associated with the emotional state of the robot.

Examples include:

* green glow representing positive feedback
* soft pulsing blue representing calm idle state
* warm yellow representing attention or curiosity

### Interaction feedback

LED signals may indicate recognition or completion of user actions.

Examples include:

* flash when wakeword detection occurs
* pulse when listening state begins
* confirmation flash after command execution

### System status indicators

LED signals may represent operational states of the system.

Examples include:

* breathing pattern during idle state
* pulsing signal during processing
* steady illumination during active interaction

### Alerts and errors

LED signals may represent abnormal or warning conditions.

Examples include:

* red flashing signal for critical error
* orange blinking signal for warning state
* white flash during system startup

## LED Pattern Types

The subsystem supports multiple pattern structures.

Examples include:

* static color
* blinking
* pulsing
* breathing effect
* rotating pattern
* progressive brightness variation

## Synchronization With Other Outputs

LED signals operate in coordination with other output subsystems.

Examples include:

* listening LED pattern activated when microphones enter listening state
* LED color synchronized with emotional facial animation
* warning LED pattern combined with audio alerts

## Typical Actions

Typical actions produced by this subsystem include:

* setting LED color
* activating LED pattern
* adjusting LED brightness
* triggering LED event signals

## Typical Outputs

Outputs produced by the subsystem include:

* color changes
* blinking signals
* pulsing light
* breathing patterns
* warning flashes

## Relationship With Other Modules

Cognitive Core

Provides emotional state information used to determine expressive LED signals.

Dialogue and Session System

May trigger LED signals associated with conversational interaction.

Planning, Interpretation and Agents

Produces execution requests that activate LED signals.

Infrastructure and Hardware

Provides the LED hardware used to emit visual signals.

Action and Expression Module

Defines the LED subsystem as part of the system visual output architecture.

## Architectural Importance

The LEDs subsystem provides a lightweight visual signaling channel for the robot.

Through color, brightness, and dynamic patterns, the subsystem communicates system state, interaction feedback, and expressive cues.

This signaling mechanism allows users to perceive system behaviour rapidly and even from a distance.

# 7.6 Movement / Servos

## Definition

The Movement / Servos subsystem is the architectural component responsible for controlling the mechanical motion of NORA through servomotors and other actuators.

This subsystem produces physical movement of the robot body, allowing the system to orient sensors, perform gestures, maintain postures, and execute embodied behaviours.

Within the Action and Expression module, the Movement / Servos subsystem defines the physical motion output channel of the robot.

## Architectural Role

The Movement / Servos subsystem connects internal system decisions with the robot mechanical hardware.

The subsystem receives structured motion requests and transforms them into actuator control signals executed by servomotors and other motion devices.

The operational flow of the subsystem can be represented as:

motion request → motion primitive selection → actuator command generation → servo actuation → physical movement → human perception

This subsystem therefore provides the physical embodiment layer through which the robot produces observable mechanical behaviour.

## Core Architectural Concepts

### mechanical element

A mechanical element is a movable component of the robot body controlled by the subsystem.

Examples include:

* head
* camera mount
* arms
* torso
* base rotation mechanism

### degree of freedom

A degree of freedom is an independent axis of motion available to a mechanical element.

Degrees of freedom define the possible orientations or positions that a mechanical element can achieve.

### motion primitive

A motion primitive is a standardized movement operation that can be executed by the subsystem.

Motion primitives represent basic physical actions that can be combined to form more complex behaviours.

Examples include:

* rotate head
* tilt head
* nod
* shake head
* reset posture

### posture

A posture is a stable configuration of multiple mechanical elements.

Postures represent predefined body positions used during different operational states.

### motion trajectory

A motion trajectory is the temporal sequence of positions followed by a mechanical element during movement.

Trajectories define smooth transitions between starting and target positions.

## Subsystem Components

### Motion Controller

The Motion Controller manages the execution of motion primitives and trajectories.

### Actuator Driver

The Actuator Driver converts motion commands into electrical control signals for servomotors and actuators.

### Posture Manager

The Posture Manager maintains predefined robot body configurations associated with operational states.

### Motion Safety Controller

The Motion Safety Controller enforces safety constraints during movement execution.

This component prevents unsafe motions and ensures controlled transitions.

## Controlled Mechanical Elements

The subsystem controls the articulated components of the robot body.

Typical elements include:

* head
* eye mechanisms
* arms
* torso
* camera mount
* rotating base

Each element may provide one or more degrees of freedom controlled through servomotors.

## Types of Movement

### Orientation

Orientation movements direct sensors or body parts toward a target.

Examples include:

* turning the head toward a user
* pointing the camera toward an object

### Conversational gestures

Conversational gestures support interaction with subtle body movements.

Examples include:

* nodding
* head shaking
* attentive head tilt

### Emotional gestures

Physical motion may reinforce emotional expression.

Examples include:

* curious head tilt
* relaxed idle posture
* energetic movement patterns

### Target tracking

Target tracking maintains orientation toward a detected person or object.

Examples include:

* following a speaking person
* maintaining camera alignment with a document

### Predefined postures

Predefined postures represent stable configurations associated with system states.

Examples include:

* idle posture
* conversation posture
* attention posture
* shutdown posture

## Motion Execution Pipeline

Movement execution follows a structured sequence.

1. reception of motion request
2. selection of motion primitive or posture
3. trajectory generation
4. actuator command generation
5. servo actuation

## Synchronization With Other Outputs

Motion behaviour operates in coordination with other expression channels.

Examples include:

* nodding synchronized with affirmative speech
* orientation toward the user before speaking
* gestures coordinated with LED signals

## Typical Actions

Typical actions produced by this subsystem include:

* moving the head
* tilting the head
* nodding
* shaking the head
* resetting posture
* orienting toward a target
* tracking a person

## Typical Outputs

Outputs produced by the subsystem include:

* head movement
* eye movement
* arm movement
* torso movement
* posture transitions
* orientation changes

## Relationship With Other Modules

Cognitive Core

Provides emotional or behavioural context influencing motion behaviour.

Planning, Interpretation and Agents

Produces motion requests associated with tasks or interaction behaviours.

Perception Modules

Provide target locations used for orientation or tracking.

Infrastructure and Hardware

Provides the servomotors and actuators used for physical movement.

Action and Expression Module

Defines the movement subsystem as part of the robot physical output architecture.

## Architectural Importance

The Movement / Servos subsystem enables physical embodiment of the robot.

Through controlled motion of mechanical elements, the subsystem allows NORA to express attention, intention, and interaction cues in the physical environment.

This capability transforms the system from a purely informational agent into an embodied interactive system.

# 7.7 Active Camera

## Definition

The Active Camera subsystem is the architectural component responsible for the deliberate and goal‑directed use of the robot camera as an operational action channel.

This subsystem executes intentional camera operations such as image capture, video recording, document acquisition, visual streaming, and task‑driven frame acquisition.

Within the Action and Expression module, the Active Camera subsystem defines the camera as an instrument used to perform actions that produce visual assets or visual streams.

## Architectural Role

The Active Camera subsystem performs camera operations that are explicitly requested by system decisions.

The subsystem receives structured camera action requests and transforms them into controlled camera device operations.

The operational flow of the subsystem can be represented as:

camera action request → capture mode selection → camera activation → frame or stream acquisition → output generation

This subsystem therefore converts a high‑level goal involving visual acquisition into a concrete camera operation.

## Distinction From Vision Perception

The system architecture separates passive perception from deliberate camera usage.

### Vision subsystem (Perception layer)

The Vision subsystem processes visual input from the environment.

Typical functions include:

* detecting people
* detecting objects
* detecting gestures
* detecting text
* interpreting scene context

The Vision subsystem answers the question:

"What is visible in the environment?"

### Active Camera subsystem (Action and Expression layer)

The Active Camera subsystem performs deliberate camera operations.

Typical functions include:

* capturing an image
* recording video
* scanning a document
* opening a live camera stream

The subsystem answers the question:

"What operation is intentionally performed with the camera?"

## Core Architectural Concepts

### camera action

A camera action is an intentional operation that activates the camera device in order to produce a visual result.

### capture asset

A capture asset is a visual data object produced by a camera action.

Examples include:

* photo file
* video file
* captured frame
* document scan image

### capture mode

Capture mode defines the operational configuration used during camera activation.

Examples include:

* photo mode
* video mode
* scan mode
* stream mode

### capture session

A capture session is the time‑bounded operation during which the camera device remains active for a specific task.

### capture metadata

Capture metadata contains contextual information associated with a captured asset.

Examples include:

* timestamp
* requesting user
* capture location
* associated task identifier

## Subsystem Components

### Camera Controller

The Camera Controller manages activation and configuration of the camera device.

### Capture Pipeline

The Capture Pipeline performs acquisition of frames, images, or video streams.

### Mode Manager

The Mode Manager selects the capture mode required by the requested action.

### Asset Generator

The Asset Generator produces structured outputs representing captured visual data.

### Stream Manager

The Stream Manager handles live visual streams generated by the camera.

## Types of Camera Actions

### Photo capture

Photo capture produces a still image file representing a single frame acquired by the camera.

### Video recording

Video recording produces a sequence of frames stored as a video asset.

### Document scanning

Document scanning captures images optimized for document acquisition.

The resulting asset may be forwarded to document processing modules.

### OCR acquisition

OCR acquisition captures an image intended for text extraction by reading or OCR modules.

### Recognition capture

Recognition capture produces an image used by recognition subsystems such as object detection or face recognition.

### Live stream or preview

Live streaming produces a continuous sequence of frames accessible to other modules or interfaces.

## Camera Action Pipeline

Camera operations follow a structured execution sequence.

1. reception of camera action request
2. permission validation
3. capture mode selection
4. camera activation
5. frame or stream acquisition
6. asset generation
7. metadata recording
8. completion event emission

## Typical Inputs

Typical triggers that generate camera action requests include:

* photo capture requests
* video recording requests
* document scan requests
* OCR acquisition requests
* recognition capture requests

## Typical Outputs

Outputs produced by the subsystem include:

* photo asset
* video asset
* captured frame
* document scan image
* live stream handle
* capture metadata

Event‑style outputs may include:

* EVT_PHOTO_CAPTURED
* EVT_VIDEO_RECORDING_STARTED
* EVT_VIDEO_RECORDING_STOPPED
* EVT_DOCUMENT_SCANNED
* EVT_CAMERA_STREAM_OPENED
* EVT_CAMERA_ACTION_FAILED

## Relationship With Other Modules

Perception / Vision

Consumes captured frames for analysis when required.

Reading or OCR modules

Receive captured images used for text extraction.

Frontend and Local UI

May display camera previews or capture results.

Persistence and Memory

Stores captured assets and metadata.

Identity, Access and Security

Validates permissions associated with camera operations.

Action and Expression module

Defines the Active Camera subsystem as the camera action channel of the robot.

## Architectural Importance

The Active Camera subsystem transforms the robot camera from a passive sensing device into an operational instrument used to perform tasks.

Through controlled camera actions, the system acquires visual assets that support recognition, document processing, communication, and task execution.

This capability forms an important bridge between perception, action, and real‑world task completion.

# 7.8 Home Automation / IoT

## Definition

The Home Automation / IoT subsystem is the architectural component responsible for controlling and coordinating external connected devices through home automation systems and IoT networks.

This subsystem allows the robot to interact with devices that exist in the surrounding environment but are not physically part of the robot hardware.

Within the Action and Expression module, the Home Automation / IoT subsystem defines the external device actuation channel of the system.

## Architectural Role

The Home Automation / IoT subsystem executes operations that modify the state of external devices connected through automation platforms or IoT networks.

The subsystem receives structured device control requests and transforms them into communication operations directed toward external systems or devices.

The operational flow of the subsystem can be represented as:

control request → device resolution → protocol translation → command transmission → device state update

This subsystem therefore enables the robot to perform actions that affect the surrounding physical environment beyond the robot body.

## Core Architectural Concepts

### external device

An external device is a connected system component located in the environment and controlled through network communication.

Examples include:

* smart lights
* smart plugs
* thermostats
* door locks
* smart speakers

### device capability

A device capability represents an operation or parameter that a device exposes for control.

Examples include:

* power on
* power off
* brightness level
* temperature setpoint

### device state

Device state represents the current operational condition of a device as reported by the automation system.

Examples include:

* power status
* temperature value
* lock status

### device action

A device action is a control operation sent to a device to change its state.

### automation routine

An automation routine is a predefined sequence of device actions triggered by conditions, schedules, or system events.

### scene

A scene is a predefined configuration that applies coordinated state changes to multiple devices.

## Subsystem Components

### Device Registry

The Device Registry maintains information about connected devices and their capabilities.

### Command Dispatcher

The Command Dispatcher sends device actions to the appropriate communication interface.

### Protocol Adapter

The Protocol Adapter translates generic device commands into specific IoT communication protocols.

### State Monitor

The State Monitor retrieves and maintains device state information.

### Automation Engine

The Automation Engine executes predefined routines and scene activations.

## Types of Controlled Devices

Typical external devices may include:

* smart lighting systems
* smart plugs
* coffee machines
* motorized blinds
* thermostats
* robot vacuum cleaners
* smart televisions
* smart speakers
* door locks
* doorbells

## Categories of Device Actions

### power control

Power control changes the power state of a device.

Examples include:

* turning lights on
* turning lights off
* activating smart plugs

### parameter adjustment

Parameter adjustment modifies a configurable value exposed by the device.

Examples include:

* adjusting brightness
* setting thermostat temperature
* adjusting fan speed

### scene activation

Scene activation applies a predefined configuration across multiple devices.

Examples include:

* movie mode
* night mode
* work mode

### automation execution

Automation execution triggers predefined routines that coordinate several device actions based on conditions or schedules.

## IoT Communication Mechanisms

The subsystem may interact with external devices through several communication protocols.

Examples include:

* REST APIs
* MQTT messaging
* WebSocket communication
* local device APIs
* vendor specific protocols

Automation platforms such as Home Assistant may provide unified control over heterogeneous devices.

## Typical Inputs

Typical triggers that generate device control operations include:

* user device control requests
* scheduled automation events
* contextual triggers
* planner generated device actions

## Typical Outputs

Outputs produced by the subsystem include:

* device state change commands
* automation routine execution
* scene activation events
* device state reports

## Relationship With Other Modules

Planning, Interpretation and Agents

Produces device control requests derived from user goals.

Dialogue and Session System

Provides natural language commands interpreted as device actions.

Frontend and Visualization

Displays device states and automation feedback.

Persistence and Memory

Stores device configurations and automation rules.

Identity, Access and Security

Validates permissions associated with device control operations.

Infrastructure and Hardware

Provides network connectivity used for IoT communication.

## Architectural Importance

The Home Automation / IoT subsystem enables the system to influence the surrounding environment by controlling connected devices.

Through device actions, automation routines, and scene activations, the subsystem extends the robot operational capabilities beyond the robot hardware and into the physical space in which the system operates.

# 7.9 Notifications and Communication

## Definition

The Notifications and Communication subsystem is the architectural component responsible for transmitting information, alerts, and messages from the system to external users, services, or platforms.

This subsystem enables the system to deliver outbound communication beyond local interaction channels such as speech, screen display, lighting signals, or physical movement.

Within the Action and Expression module, the Notifications and Communication subsystem defines the outbound digital communication channel of the system.

## Architectural Role

The Notifications and Communication subsystem executes operations that deliver messages or alerts to external recipients through digital communication channels.

The subsystem receives structured notification requests and transforms them into outbound communication operations directed toward remote users, services, or monitoring systems.

The operational flow of the subsystem can be represented as:

notification request → message construction → channel selection → message transmission → delivery confirmation

This subsystem therefore enables the system to communicate events, information, or alerts to entities located outside the robot physical environment.

## Core Architectural Concepts

### notification

A notification is a message generated by the system to inform an external recipient about an event, condition, or task result.

### recipient

A recipient is an external user, administrator, or system endpoint that receives a notification.

### communication channel

A communication channel is the delivery mechanism used to transmit a message.

Examples include:

* mobile application notification
* email message
* web interface alert
* messaging platform API

### alert event

An alert event is a system condition that requires immediate notification of a recipient.

Examples include:

* hardware failure
* service interruption
* critical system error

### message payload

A message payload contains the structured information transmitted through the communication channel.

Examples include:

* notification text
* event metadata
* system identifiers

## Subsystem Components

### Notification Manager

The Notification Manager coordinates the creation and dispatch of notifications.

### Message Builder

The Message Builder constructs structured message payloads from system events or requests.

### Channel Dispatcher

The Channel Dispatcher selects the appropriate communication channel and performs message transmission.

### Recipient Directory

The Recipient Directory maintains information about recipients and their preferred communication channels.

### Delivery Logger

The Delivery Logger records transmitted messages and delivery outcomes for auditing and monitoring.

## Types of Notifications

### user notifications

User notifications communicate information intended for the primary user of the system.

Examples include:

* reminders
* scheduled alerts
* task completion messages

### administrative alerts

Administrative alerts communicate technical events that require administrator attention.

Examples include:

* hardware failures
* system service interruptions

### system event reports

System event reports forward significant system events to external monitoring systems.

Examples include:

* device state changes
* automation execution events

### messaging integration

Messaging integration allows the system to transmit messages through external communication platforms.

Examples include:

* mobile application notifications
* email delivery
* messaging service APIs

## Communication Channels

The subsystem may support several communication mechanisms.

Examples include:

* mobile application notifications
* email delivery
* web interface alerts
* messaging APIs
* system event logging endpoints

## Typical Inputs

Typical triggers that generate outbound communication operations include:

* planner generated notifications
* dialogue system messaging requests
* system monitoring alerts
* automation rule triggers

## Typical Outputs

Outputs produced by the subsystem include:

* outbound notifications
* administrator alerts
* system event reports
* delivery log records

## Relationship With Other Modules

Planning, Interpretation and Agents

Generates notification requests associated with user goals or task outcomes.

Dialogue and Session System

Produces communication requests derived from user interactions.

Frontend and Visualization

Displays delivered messages within local or remote interfaces.

Persistence and Memory

Stores message logs and notification history.

Identity, Access and Security

Validates permissions associated with communication operations.

Infrastructure and Hardware

Provides network connectivity required for message transmission.

## Architectural Importance

The Notifications and Communication subsystem enables the system to communicate events, alerts, and information to external entities beyond the local interaction environment.

Through outbound messaging, alert transmission, and integration with external services, the subsystem connects the system to the wider digital ecosystem in which it operates.

## Architectural Importance

The Action and Expression module provides the mechanisms through which the NORA system performs observable operations in the physical and digital environment.

While the cognitive and planning subsystems determine what the system should do, the Action and Expression module is responsible for executing those decisions through concrete output channels.

Through this module the architecture gains:

* embodied interaction capabilities
* multimodal communication with users
* physical behavior execution
* environmental actuation
* digital ecosystem communication

By separating reasoning from execution, the architecture ensures that cognitive processes remain modular while the system can still produce coordinated actions in the world.

## Architectural Structure

```
Action and Expression
│
├── Voice Output
│ ├── speech synthesis
│ ├── text-to-speech processing
│ ├── voice generation control
│ ├── language voice selection
│ ├── speech pacing control
│ ├── pronunciation adjustment
│ ├── audio playback generation
│ ├── speech interruption handling
│ ├── speech queue management
│ ├── conversational speech delivery
│ ├── speech output synchronization
│ └── spoken response output
│
├── Sound and Multimedia
│ ├── audio playback
│ ├── music playback
│ ├── multimedia streaming
│ ├── media library access
│ ├── sound effect triggering
│ ├── volume control
│ ├── playback state management
│ ├── media device integration
│ ├── playback queue management
│ ├── audio source selection
│ ├── multimedia output routing
│ └── media playback output
│
├── Screen / Local UI
│ ├── text display rendering
│ ├── image visualization
│ ├── video playback
│ ├── camera preview display
│ ├── graphical interface rendering
│ ├── menu and widget display
│ ├── system state indicators
│ ├── emotion visualization
│ ├── chart and data visualization
│ ├── QR code generation
│ ├── visual interaction feedback
│ └── display output generation
│
├── Emotional Expression
│ ├── emotional state mapping
│ ├── expression rule management
│ ├── multimodal expression coordination
│ ├── expression intensity control
│ ├── context-aware expression adaptation
│ ├── visual emotion rendering
│ ├── voice tone modulation
│ ├── movement expression integration
│ ├── LED emotion synchronization
│ ├── emotional transition management
│ ├── expressive behavior orchestration
│ └── emotional expression output
│
├── LEDs
│ ├── LED color control
│ ├── brightness adjustment
│ ├── blinking pattern generation
│ ├── pulsing pattern generation
│ ├── breathing light effects
│ ├── interaction feedback indicators
│ ├── system state indicators
│ ├── alert signal generation
│ ├── emotion color synchronization
│ ├── LED animation control
│ ├── LED hardware communication
│ └── light signal output
│
├── Movement / Servos
│ ├── motion primitive execution
│ ├── head orientation control
│ ├── posture control
│ ├── conversational gesture execution
│ ├── emotional gesture execution
│ ├── target tracking behavior
│ ├── trajectory generation
│ ├── servo command generation
│ ├── motion safety validation
│ ├── movement synchronization
│ ├── actuator hardware control
│ └── physical movement execution
│
├── Active Camera
│ ├── camera device activation
│ ├── capture mode selection
│ ├── photo capture
│ ├── video recording
│ ├── document scan acquisition
│ ├── OCR image acquisition
│ ├── recognition capture generation
│ ├── live stream generation
│ ├── camera configuration control
│ ├── visual asset generation
│ ├── capture metadata recording
│ └── camera action execution
│
├── Home Automation / IoT
│ ├── device registry management
│ ├── device capability resolution
│ ├── device command dispatch
│ ├── protocol translation
│ ├── device state monitoring
│ ├── power control actions
│ ├── parameter adjustment actions
│ ├── scene activation
│ ├── automation routine execution
│ ├── IoT platform integration
│ ├── external device coordination
│ └── environmental actuation
│
└── Notifications and Communication
  ├── notification generation
  ├── message construction
  ├── channel selection
  ├── message dispatch
  ├── recipient management
  ├── user notification delivery
  ├── administrative alert transmission
  ├── system event reporting
  ├── messaging platform integration
  ├── communication logging
  ├── delivery confirmation handling
  └── outbound communication execution
```

## Architectural Layers

The Action and Expression module is organized as a layered execution architecture that transforms planned operations into concrete physical or digital actions.

| Layer                         | Responsibility                                                                                                   |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| Interaction Expression Layer  | Produces user-facing multimodal outputs such as speech, sound, visual display, lighting, and expressive behavior |
| Physical Embodiment Layer     | Executes physical robot behavior through mechanical movement and orientation                                     |
| Visual Acquisition Layer      | Performs deliberate camera operations to capture visual information required for tasks                           |
| Environmental Actuation Layer | Controls external devices and smart environments through IoT systems                                             |
| External Communication Layer  | Sends notifications, alerts, and messages to external users, services, or monitoring systems                     |

Together these layers establish the execution architecture of NORA, allowing the system to transform internal plans and decisions into coordinated multimodal actions that affect the user, the robot body, the surrounding environment, and the broader digital ecosystem.
