# 6. Planning, Interpretation and Agents

#definition: architectural layer responsible for transforming interpreted inputs, goals, contextual conditions, and system events into structured execution strategies composed of plans, tools, agents, and decision steps.

## Definition

The Planning, Interpretation and Agents module is the architectural layer that determines how NORA converts interpreted inputs and active objectives into organized system behaviour.

This module defines the reasoning structures through which the system:

* interprets the meaning of already-normalized inputs
* identifies the operative objective associated with those inputs
* selects the internal or external capabilities required to address that objective
* constructs a structured execution strategy
* delegates execution to tools, agents, and downstream action layers

Within the global architecture, this module does not perform raw sensing, does not maintain the global operational state machine, and does not directly materialize output effects in the world.

Instead, it defines the architectural domain in which interpreted information becomes intentional, goal-oriented, and executable system behaviour.

This module is therefore the architectural reasoning layer that connects understanding with execution.

---

## Architectural Purpose

The purpose of the Planning, Interpretation and Agents module is to provide NORA with an explicit internal layer for transforming meaning into organized action.

A multimodal embodied system does not operate correctly if it only:

* perceives signals
* stores context
* maintains operational state
* executes isolated commands

The architecture also requires a layer capable of answering questions such as:

* What objective is represented by this input?
* Which system capability corresponds to that objective?
* Is the request complete or incomplete?
* Which information is missing?
* Which reasoning path is required?
* Which tools must be invoked?
* Which specialized component must handle the task?
* In what order must the steps be executed?
* What result must be returned to the user or to the system?

The Planning, Interpretation and Agents module exists to define those structures explicitly.

Without this layer, the system would remain limited to disconnected reactions, hardcoded behaviour mappings, or shallow command execution.

With this layer, NORA becomes capable of structured task reasoning, capability selection, multi-step decision flow, and domain-specific problem handling.

---

## Architectural Role

Within the global architecture, the Planning, Interpretation and Agents module acts as the bridge between:

* interpreted system meaning
* executable system strategy

Conceptually, its role can be represented as:

**Perception / Dialogue / Cognitive Context / External Requests → Interpretation and Planning Structures → Tools / Agents / Action Execution**

This means the module receives structured upstream inputs and transforms them into structured downstream execution strategies.

It occupies the architectural position between:

* the modules that determine what has been perceived, said, requested, triggered, or activated
* the modules that perform physical action, digital action, communication, output generation, or external service invocation

The module therefore acts as the reasoning and orchestration layer through which NORA determines what operational path corresponds to a given situation.

---

## Why This Module Is Necessary

The architecture of NORA includes perception, dialogue continuity, operational state, persistent memory, action channels, backend services, and external integrations.

However, none of those layers alone defines how the system converts an interpreted situation into a structured course of action.

For example:

* Perception may provide a speech transcript, but does not determine the full execution strategy.
* The Dialogue and Session System may provide conversation history, but does not determine which tool must be called next.
* The Cognitive Core may maintain behavioural state, but does not define task decomposition.
* The Action and Expression layer may execute outputs, but does not determine the reasoning chain that justifies them.

A separate architectural layer is therefore required to define:

* semantic interpretation structures
* intent structures
* planning structures
* tool-selection structures
* specialized problem-solving structures

This separation is necessary to preserve modularity and to avoid collapsing understanding, reasoning, and execution into a single undifferentiated subsystem.

---

## Core Concepts

The Planning, Interpretation and Agents module is defined through several explicit architectural concepts.

### interpreted input

structured input already normalized by upstream modules and ready for reasoning.

An interpreted input is not raw sensor data. It is a representation that already carries recognizable content such as transcribed language, normalized gesture meaning, classified event type, or structured external request.

Examples include:

* recognized speech transcript
* normalized dialogue turn
* gesture command representation
* scheduled reminder trigger
* API request mapped to an internal event

### semantic representation

structured description of the meaning contained in an interpreted input.

A semantic representation includes the informational structure extracted from an input, such as dialogue act, entities, references, contextual anchors, and linguistic metadata.

### intent

structured representation of the goal, purpose, or operative objective associated with a semantic representation.

An intent identifies what the system is being asked to achieve or what objective is implied by an event or input.

### planning context

structured set of contextual variables required to determine how an intent or event must be handled.

Planning context may include:

* active user identity
* permissions
* active session
* project context
* dialogue history
* current FSM state
* available tools
* subsystem availability
* safety constraints
* environmental conditions

### plan

structured representation of the execution strategy required to achieve a goal.

A plan contains an ordered or conditionally organized set of planning steps together with the resources, dependencies, and outputs associated with those steps.

### planning step

atomic reasoning or execution unit contained inside a plan.

A planning step may represent operations such as:

* requesting clarification
* retrieving information
* validating permissions
* invoking a tool
* delegating to an agent
* performing a computation
* generating a response
* triggering a downstream action

### execution strategy

formal decision describing how the system will transform an intent or trigger into completed behaviour.

The execution strategy defines:

* sequence
* dependencies
* branches
* conditions
* outputs
* delegation paths

### tool

internal or external capability that performs a bounded operational function.

A tool may correspond to:

* a search mechanism
* a calculator
* a database retrieval function
* a hardware control capability
* a web service integration
* a messaging function
* a document handler

### tool invocation

structured action through which the plan activates a specific tool with defined inputs and expected outputs.

### agent

specialized reasoning component responsible for handling a class of tasks requiring focused logic, domain knowledge, or structured internal coordination.

Examples include:

* tutoring agent
* document analysis agent
* route planning agent
* scheduling agent
* coding agent
* explanation agent

### capability mapping

architectural correspondence between an identified intent and the set of tools, agents, or execution patterns able to satisfy it.

### clarification requirement

explicit representation that the current input, context, or intent lacks sufficient information for safe or correct execution.

### planning result

structured output of the module containing the selected intent, plan, required tools, delegated agents, unresolved parameters, and execution metadata.

These concepts define the structural vocabulary of the module.

---

## Scope of the Module

The Planning, Interpretation and Agents module includes all architectural mechanisms responsible for transforming interpreted inputs and contextual goals into structured execution strategies.

Its scope includes:

* semantic interpretation of normalized inputs
* intent identification
* contextual reasoning for task understanding
* mapping between requests and system capabilities
* plan construction
* multi-step task decomposition
* clarification detection
* tool selection
* agent selection and delegation
* plan adaptation based on context and restrictions

Its scope does not include:

* raw signal acquisition
* raw sensor preprocessing
* low-level perception pipelines
* persistent session storage itself
* global operational state control itself
* direct output rendering
* direct actuator control
* low-level external API transport implementation

Those concerns belong to Perception, Dialogue and Session System, Cognitive Core, Action and Expression, Backend and Application, or Persistence and Memory.

This distinction is essential because the module is responsible for strategy and structured reasoning, not for sensing or final execution mechanics.

---

## Inputs to the Module

The module receives structured inputs originating from several architectural domains.

### Conversational inputs

These inputs originate from human interaction and dialogue processing.

Examples include:

* user questions
* explicit commands
* requests for help
* corrections
* confirmations
* rejections
* interruptions
* follow-up instructions
* casual conversation turns

These inputs typically arrive as normalized dialogue turns with associated context.

### Session-derived inputs

These inputs originate from the Dialogue and Session System.

Examples include:

* active session context
* session continuation state
* dialogue summaries
* active project references
* recovered conversational context

### Cognitive-context inputs

These inputs originate from the Cognitive Core.

Examples include:

* active FSM state
* behavioural constraints
* active operational context
* current interaction mode
* subsystem restrictions
* safety conditions

### Event-driven inputs

These inputs originate from system events produced by other modules.

Examples include:

* wake word event
* speech recognized event
* gesture command event
* schedule trigger event
* timeout event
* planner follow-up trigger
* external notification event

### External system requests

These inputs originate from external interfaces or connected services.

Examples include:

* API commands
* frontend actions
* remote administrative requests
* IoT messages
* webhook-triggered events

### Project and long-horizon inputs

These inputs originate from persistent project structures or planned ongoing tasks.

Examples include:

* project continuation request
* pending task activation
* study workflow continuation
* scheduled learning objective
* deferred action requirement

---

## Outputs of the Module

The output of this module is not a direct world effect. It is a structured decision object that defines how execution must proceed.

Typical outputs include:

* semantic representation
* selected intent
* confidence information
* planning result
* ordered or conditional execution steps
* selected tools
* selected specialized agent
* clarification request requirements
* unresolved parameters
* delegation instructions
* expected execution outputs

Downstream modules consume these outputs in order to:

* execute actions
* generate dialogue responses
* invoke external services
* present clarifications to the user
* produce multimodal output

---

## Main Responsibilities

The Planning, Interpretation and Agents module performs several distinct architectural responsibilities.

### 1. Semantic Interpretation

The module transforms normalized inputs into semantic representations that describe meaning, structure, entities, and dialogue role.

This responsibility includes:

* dialogue act identification
* entity extraction
* reference resolution
* language-related semantic normalization
* contextual enrichment of interpreted input

### 2. Intent Identification

The module determines the operative goal associated with a semantic representation.

This responsibility includes:

* identifying what the system is being asked to achieve
* distinguishing among capability classes
* mapping goals into structured intent categories
* distinguishing complete requests from incomplete requests

### 3. Capability Mapping

The module maps detected intents and planning situations to executable system capabilities.

This includes identifying whether a task requires:

* a direct response
* an information retrieval tool
* an external integration
* a specialized agent
* a multi-step internal workflow

### 4. Plan Construction

The module constructs a structured plan describing how the goal will be achieved.

This includes:

* step ordering
* dependency handling
* conditional branches
* selection of intermediate actions
* output expectations

### 5. Clarification Detection

The module determines whether the current information is sufficient for execution.

This includes detecting:

* missing parameters
* ambiguous targets
* uncertain references
* required confirmations
* incomplete constraints

### 6. Tool Selection

The module identifies which internal or external operational capabilities must be invoked.

This includes:

* choosing the appropriate tool type
* selecting the appropriate provider or backend capability
* matching inputs to tool requirements
* coordinating multiple tools when required

### 7. Specialized Agent Delegation

The module determines whether a task belongs to a specialized reasoning component.

This includes:

* recognizing task domains
* selecting the corresponding agent
* defining the handoff structure
* receiving the agent output back into the broader execution strategy

### 8. Contextual Adaptation

The module adapts interpretation and planning based on runtime context.

This includes adaptation to:

* user identity
* permissions
* active project
* conversation history
* operational mode
* hardware or service availability
* safety conditions

### 9. Replanning and Flow Adjustment

The module updates or reconstructs a plan when new information modifies the original reasoning path.

This includes:

* interruption handling
* correction handling
* confirmation results
* failure recovery
* changed environmental conditions
* changed user goal

---

## Architectural Entities Managed by the Module

To make the architecture fully explicit, this module introduces and manipulates a set of concrete architectural entities.

### semantic input object

Structured object representing the semantic interpretation of an input.

Typical fields may include:

* normalized content
* language
* dialogue act
* extracted entities
* references
* confidence score
* contextual metadata

### intent object

Structured object representing the identified goal associated with a semantic input.

Typical fields may include:

* intent label
* intent family
* confidence score
* required parameters
* extracted argument values
* completeness status

### plan object

Structured object representing the execution strategy.

Typical fields may include:

* target goal
* selected intent
* ordered steps
* conditional branches
* required tools
* delegated agents
* preconditions
* blocking dependencies
* expected outputs
* fallback path

### planning step object

Structured object representing one step in the plan.

Typical fields may include:

* step identifier
* step type
* step purpose
* required input
* produced output
* dependency references
* blocking or non-blocking execution property

### tool binding

Structured association between a planning step and a concrete tool.

### agent assignment

Structured association between a planning requirement and a specialized agent.

### clarification request object

Structured representation of the information that must be requested before execution can continue.

### planning outcome

Structured final output produced by the module and passed to downstream execution layers.

---

## Planning Complexity Levels

The module supports multiple levels of reasoning complexity.

### Single-step planning

A single-step plan represents a request that maps directly to a simple capability path.

Example:

User input: "What time is it?"

Possible reasoning structure:

1. detect informational intent
2. select time retrieval capability
3. retrieve current time
4. generate response

### Parameter-completion planning

A parameter-completion plan represents a request whose objective is identifiable but whose execution parameters are incomplete.

Example:

User input: "Navigate to a restaurant"

Possible reasoning structure:

1. detect navigation intent
2. identify missing destination specification
3. generate clarification requirement
4. request missing parameter
5. wait for follow-up input
6. continue planning when clarification arrives

### Conditional planning

A conditional plan represents a request whose execution depends on guards, permissions, or branching logic.

Example:

User input: "Delete this session"

Possible reasoning structure:

1. identify destructive operation intent
2. resolve session target
3. verify access rights
4. request confirmation
5. execute deletion on confirmation branch
6. cancel action on rejection branch

### Multi-step planning

A multi-step plan represents a goal requiring several coordinated reasoning and execution steps.

Example:

User input: "Plan a study session for tomorrow"

Possible reasoning structure:

1. retrieve calendar availability
2. retrieve active study project or topic preference
3. estimate available time blocks
4. construct possible study schedule
5. present proposal
6. adjust schedule if needed
7. create reminders
8. summarize plan

### Agent-assisted planning

An agent-assisted plan represents a task requiring domain-specific reasoning.

Example:

User input: "Help me understand this document and summarize the key ideas"

Possible reasoning structure:

1. detect document-analysis task
2. select document analysis agent
3. retrieve document content
4. delegate summarization and thematic extraction
5. receive agent result
6. generate final explanation

### Long-horizon planning

A long-horizon plan represents a structured objective extended across time, sessions, or project states.

Example:

User input: "Help me prepare for my exam this month"

Possible reasoning structure:

1. identify tutoring and project-oriented goal
2. create or reuse study project
3. decompose objective into milestones
4. assign study sessions over time
5. maintain progress state
6. re-enter plan during future sessions

---

## Context Dependence of Planning

Planning is context-dependent rather than input-dependent alone.

The same textual or event input may correspond to different intents and different plans depending on runtime context.

Examples of context factors include:

* active task state
* current session topic
* current user identity
* prior turn history
* selected device
* system mode
* current hardware availability
* active permissions
* environmental restrictions

Example:

User says: "Stop"

The planning meaning of this input depends on context.

Possible interpretations include:

* stop speaking
* stop music playback
* stop navigation
* stop motion
* stop current conversation workflow

The module therefore never reasons over isolated text alone. It reasons over interpreted input plus planning context.

---

## Clarification and Incompleteness Handling

A key responsibility of the module is to represent incompleteness explicitly.

A request may be incomplete even when its general intent is clear.

Typical causes of incompleteness include:

* missing target
* missing destination
* missing time
* unresolved reference
* under-specified device
* conflicting parameters
* ambiguous prior context

The module does not treat these cases as failures of the architecture. It treats them as explicit planning states.

The architecture therefore includes the notion of a clarification requirement as a first-class planning output.

This allows the system to continue operating coherently even when the first input is insufficient for final execution.

---

## Tool Use as an Architectural Concept

Within this module, a tool is not merely an implementation detail. It is a defined architectural capability unit.

A tool exists as a bounded execution mechanism that the planner can reference and invoke.

Tool categories may include:

* retrieval tools
* knowledge tools
* computation tools
* scheduling tools
* file tools
* communication tools
* hardware tools
* integration tools

The planner and tool selector are responsible for binding plans to these capability units.

This means the architecture explicitly distinguishes between:

* understanding the request
* identifying the goal
* selecting the operational capability able to satisfy the goal

---

## Specialized Agents as Architectural Components

Specialized agents are domain-specific reasoning components contained within this module.

A specialized agent is not equivalent to the global planner.

The planner determines the execution strategy.

A specialized agent handles one specialized reasoning domain inside that strategy.

Examples of possible agent domains include:

* tutoring
* scheduling
* route planning
* coding assistance
* data interpretation
* summarization
* multimodal explanation
* project continuation

This separation allows the architecture to preserve:

* centralized planning structure
* distributed specialized reasoning
* modular extensibility of problem-solving domains

---

## Relationship With Other Modules

The Planning, Interpretation and Agents module interacts with several major architectural domains.

### Relationship With Perception System

The Perception System provides structured perception results and perception events.

The planning layer does not process raw signals. It receives already-interpreted or normalized inputs derived from perception.

Examples include:

* recognized speech
* recognized gesture command
* detected environmental event
* user-presence signal used for context

### Relationship With Dialogue and Session System

The Dialogue and Session System provides conversational continuity structures.

These include:

* active dialogue turns
* conversation history
* session context
* project references
* summaries
* recovery state

This information is required for context-aware interpretation and for multi-turn planning.

### Relationship With Cognitive Core

The Cognitive Core provides:

* current operational state
* behavioural constraints
* contextual restrictions
* active interaction mode
* short-term operational continuity

This information conditions which plans are valid and which actions are currently permissible.

### Relationship With Identity, Access and Security

Planning decisions may depend on:

* identity
* permissions
* access restrictions
* safety rules
* authorization requirements

The module does not define the security model, but it must reason within that model.

### Relationship With Action and Expression

The Action and Expression layer materializes the outputs selected by the plan.

The planning module determines:

* what must be executed
* in which order
* with which dependencies
* under which conditions

The Action and Expression layer then performs the output behaviour.

### Relationship With Backend and Application

Backend services provide application-level interfaces, orchestrators, event dispatch pathways, and integration surfaces that the planning layer may invoke through tools or execution services.

### Relationship With Persistence and Memory

Persistent data may influence planning.

Examples include:

* user preferences
* project state
* stored facts
* prior summaries
* available artifacts

The module may retrieve persistent knowledge as part of plan construction.

### Relationship With Integrations and External Services

External engines and services provide many of the capabilities that plans rely on.

These may include:

* web search
* language models
* navigation services
* productivity integrations
* media services
* smart-home platforms

---

## Internal Structure of the Module

To preserve clarity, the Planning, Interpretation and Agents module is divided into several internal submodules.

### 6.1 Semantic Interpretation

Submodule responsible for transforming normalized inputs into structured semantic representations.

### 6.2 Intent Detection

Submodule responsible for identifying the operative goal associated with a semantic representation.

### 6.3 Planner

Submodule responsible for constructing the execution strategy required to achieve a goal.

### 6.4 Tool Selector

Submodule responsible for selecting the concrete capabilities required by the plan.

### 6.5 Specialized Agents

Submodule grouping domain-specific reasoning components invoked by the planner when a task requires specialized handling.

These submodules define a reasoning pipeline in which interpretation, goal identification, planning, capability binding, and specialized delegation remain distinct architectural responsibilities.

---

## Representative Examples

The following examples illustrate the architectural role of the module.

### Example 1: factual question

Input:

"What is the capital of France?"

Architectural flow:

1. semantic interpretation identifies a knowledge-oriented question
2. intent detection classifies the request as informational
3. planner constructs a direct retrieval plan
4. tool selector binds the plan to an information capability
5. final response is generated and passed to output layers

### Example 2: incomplete command

Input:

"Turn on the light"

Architectural flow:

1. semantic interpretation extracts action and object
2. intent detection identifies a device-control objective
3. planner detects missing target specificity if multiple lights exist
4. clarification requirement is generated
5. system requests disambiguation before execution

### Example 3: contextual follow-up

Dialogue:

User: "Open the document"
User: "Summarize it"

Architectural flow:

1. semantic interpretation resolves the reference "it" using dialogue context
2. intent detection classifies the second turn as summarization of the active document
3. planner constructs a document-analysis workflow
4. specialized agent may be selected
5. summarized result is returned

### Example 4: long-horizon task

Input:

"Help me organize a study plan for the next three weeks"

Architectural flow:

1. intent detection identifies a planning and tutoring objective
2. planner selects long-horizon task structure
3. project-aware context is created or reused
4. specialized scheduling and tutoring logic is applied
5. reminders, sessions, and summaries may be generated over time

---

## Design Principles

Several principles guide the design of this module.

### Separation Between Meaning and Execution

The architecture separates:

* interpretation of meaning
* identification of goal
* construction of strategy
* material execution

This prevents reasoning logic from collapsing into output logic.

### Explicit Planning Structures

Plans, intents, tools, agents, and clarification requirements are explicit architectural entities rather than implicit implementation details.

### Context-Aware Reasoning

Interpretation and planning always depend on runtime context, not on isolated input strings alone.

### Capability-Based Execution

Requests are mapped to bounded system capabilities through tools and specialized agents.

### Extensibility

The architecture allows new tools, new intent categories, and new specialized agents to be added without redefining the full reasoning structure.

### Controlled Delegation

The planner remains the coordinating reasoning structure even when downstream agents or tools perform specialized work.

### Traceability

Interpretation results, detected intents, selected plans, and delegated capabilities must remain structurally inspectable for debugging, observability, and system analysis.

---

## Architectural Importance

The Planning, Interpretation and Agents module is the architectural layer that transforms NORA from a system that merely perceives and responds into a system that reasons about how to act.

Through this module, the architecture gains:

* explicit semantic interpretation
* explicit goal identification
* explicit execution strategy construction
* structured capability selection
* specialized reasoning delegation
* support for clarification and incompleteness
* multi-step task organization
* context-aware task execution

Without this module, NORA would still be able to perceive, store, and execute, but it would lack the explicit architectural layer that determines how interpreted situations become organized action.

For that reason, the Planning, Interpretation and Agents module is one of the central reasoning pillars of the full NORA architecture.

# 6.1 Semantic Interpretation

#definition: subsystem responsible for transforming normalized inputs, interaction signals, and already-classified events into structured semantic representations that can be consumed by intent detection, planning, and downstream reasoning components.

## Definition

Semantic Interpretation is the first internal reasoning submodule of the Planning, Interpretation and Agents layer.

Its role is to transform already-normalized inputs into explicit semantic structures that describe what the input means, how it is organized, what elements it contains, and how it relates to the current conversational and operational context.

This submodule does not perform raw sensing, does not execute actions, and does not decide the final objective or execution strategy of the system.

Instead, it defines the architectural stage at which recognizable input becomes structured meaning.

Within the architecture of NORA, Semantic Interpretation is the subsystem that converts interpretable input into semantic form.

---

## Architectural Purpose

The purpose of Semantic Interpretation is to provide the architecture with an explicit layer that separates:

* signal recognition
* meaning extraction
* goal identification

A multimodal cognitive system cannot reason directly over raw strings, isolated gesture labels, or loosely structured events if it aims to preserve architectural clarity.

The system requires an intermediate representational layer capable of answering questions such as:

* What kind of communicative act does this input represent?
* Which entities are mentioned?
* Which references depend on prior context?
* What part of the input is explicit and what part is implicit?
* Which contextual variables are required to understand the meaning?
* Which semantic ambiguities remain unresolved?
* Which structured representation should be forwarded to intent detection?

Semantic Interpretation exists to answer those questions explicitly.

Without this layer, meaning extraction would be mixed together with either perception or planning.

With this layer, NORA gains a formal semantic stage in which inputs are transformed into structured representations suitable for downstream reasoning.

---

## Architectural Role

Within the global NORA architecture, Semantic Interpretation acts as the meaning-extraction layer positioned between normalized input acquisition and goal-oriented reasoning.

Conceptually, its architectural role can be represented as:

**Perception / Interaction Normalization / System Event Classification → Semantic Interpretation → Intent Detection / Planner / Specialized Reasoning**

This means the submodule receives inputs that are already recognizable in form, but not yet fully structured in meaning.

Its architectural responsibility is to transform those inputs into semantic objects that expose:

* dialogue role
* semantic content
* extracted entities
* resolved references
* contextual anchors
* uncertainty markers
* completeness information

The subsystem therefore acts as the semantic interface between recognized input and intentional reasoning.

---

## Why This Submodule Is Necessary

NORA includes multiple upstream sources capable of producing interpretable inputs:

* speech recognition outputs
* typed text messages
* normalized gesture commands
* classified system events
* structured external requests
* project-derived follow-up prompts

However, these inputs do not by themselves define a complete semantic structure.

For example:

* a speech transcript is text, but not yet a semantic object
* a gesture label is classified, but not yet integrated with context
* a conversational "yes" is understandable as language, but not yet linked to the target it confirms
* an external event label may be structured, but not yet mapped into the meaning space required for planning

A dedicated semantic interpretation layer is therefore necessary to define:

* how inputs are represented semantically
* how dialogue acts are identified
* how entities are extracted
* how references are resolved
* how contextual enrichment occurs
* how ambiguity is represented
* how completeness is assessed

This prevents downstream modules from having to reconstruct meaning repeatedly and keeps the architecture modular.

---

## Core Concepts

The Semantic Interpretation submodule is defined through several explicit architectural concepts.

### normalized input

input already transformed by upstream modules into a recognizable symbolic or structured form suitable for meaning extraction.

Examples include:

* text produced by speech recognition
* typed user message
* normalized gesture command
* classified system event
* structured external API request

### semantic representation

structured description of the meaning extracted from a normalized input.

A semantic representation contains the informational structure required for downstream reasoning.

### dialogue act

structured classification of the communicative role performed by an input within an interaction.

Examples include:

* question
* command
* request
* confirmation
* rejection
* interruption
* correction
* clarification
* continuation
* social conversation

### semantic entity

meaning-bearing element extracted from an input and represented as structured data.

Examples include:

* person
* place
* device
* object
* date
* time
* quantity
* action
* media type
* topic

### reference

input element whose meaning depends on context rather than on explicit standalone content.

Examples include:

* it
* that
* there
* again
* the same one
* this project

### reference resolution

process through which a contextual reference is linked to a specific interpreted target.

### semantic slot

named position in a semantic structure that stores a relevant extracted value.

Examples include:

* action
* target_device
* location
* topic
* destination
* time_expression

### semantic completeness

property indicating whether the extracted meaning contains enough information for downstream intent identification and planning to proceed without additional clarification.

### semantic ambiguity

state in which an input admits more than one plausible interpretation or contains unresolved uncertainty.

### semantic context enrichment

process of attaching contextual metadata to the semantic representation so that downstream reasoning operates over meaning-in-context rather than isolated input.

### semantic confidence

confidence metadata associated with interpretation outputs such as entity extraction, dialogue act classification, reference resolution, or language identification.

### semantic object

the final structured output produced by the submodule and forwarded to intent detection or other reasoning components.

These concepts define the representational vocabulary of Semantic Interpretation.

---

## Scope of the Submodule

Semantic Interpretation includes the architectural mechanisms responsible for converting normalized inputs into structured semantic representations.

Its scope includes:

* dialogue act identification
* semantic segmentation of input
* entity extraction
* reference detection
* reference resolution
* language identification when relevant to semantic processing
* semantic normalization of input content
* contextual enrichment
* ambiguity marking
* completeness evaluation
* production of formal semantic objects

Its scope does not include:

* raw audio capture
* speech-to-text itself
* raw computer vision inference
* gesture sensing itself
* final intent selection
* plan construction
* tool selection
* action execution
* frontend rendering

These responsibilities belong to Perception, Interaction Interfaces, Intent Detection, Planner, Tool Selector, Action and Expression, or other modules.

This separation is essential because Semantic Interpretation is concerned with structured meaning, not with sensing or final decision execution.

---

## Position in the Architecture

Within the Planning, Interpretation and Agents layer, Semantic Interpretation is the first reasoning stage.

Its architectural position can be represented as:

**Perception → normalization / classification → Semantic Interpretation → Intent Detection → Planner**

This separation establishes a clear internal reasoning pipeline.

### Perception

Perception acquires and processes physical signals.

It transforms:

* speech into text
* image data into recognized objects or gestures
* environmental observations into classified events

### Semantic Interpretation

Semantic Interpretation receives these already-recognizable outputs and converts them into structured meaning.

### Intent Detection

Intent Detection uses that semantic structure to determine the operative goal associated with the input.

### Planner

The Planner constructs an execution strategy based on the detected intent and the semantic-contextual representation.

This staged separation prevents the architecture from collapsing sensing, meaning extraction, and goal identification into a single opaque process.

---

## Inputs Processed by the Submodule

Semantic Interpretation can process several categories of normalized input.

### Natural language input

This category includes textual user input originating from spoken or typed interaction.

Examples include:

* "Play some music"
* "What is the weather tomorrow?"
* "Help me practice English"
* "Turn on the kitchen lights"
* "Summarize this document"
* "Remind me tomorrow at five"

These inputs require extraction of semantic structure from natural language.

### Conversational control signals

This category includes short-form conversational inputs that regulate an ongoing interaction.

Examples include:

* "yes"
* "no"
* "stop"
* "repeat"
* "wait"
* "continue"
* "cancel"
* "not that one"

These inputs often contain limited lexical content but strong interactional meaning.

### Context-dependent follow-up responses

This category includes inputs whose meaning cannot be determined without previous context.

Examples include:

* "there"
* "that one"
* "use the second option"
* "do it again"
* "open it"
* "yes, that project"

These inputs require strong context integration and reference resolution.

### Gesture-derived commands

This category includes gesture outputs that have already been recognized upstream and normalized into symbolic form.

Examples include:

* stop gesture
* pointing gesture toward an object
* confirmation gesture
* wave-to-initiate interaction

The semantic interpretation layer maps these normalized gesture forms into semantic objects compatible with dialogue and planning logic.

### Structured system events

This category includes already-classified events generated by other subsystems.

Examples include:

* schedule trigger event
* project continuation event
* external command event
* reminder activation event
* detected visual target event

These events may need semantic representation if they are to enter the same reasoning pathway used for user-generated inputs.

### External structured requests

This category includes requests originating from external systems or interfaces in already-structured form.

Examples include:

* API command payload
* frontend interaction event
* administrative structured request
* webhook-translated task signal

Even when already structured, these requests may require semantic normalization into a common interpretive format.

---

## Main Responsibilities

Semantic Interpretation performs several distinct architectural responsibilities.

### 1. Meaning Structuring

The submodule transforms normalized input into an explicit semantic form.

This means identifying which parts of the input correspond to:

* communicative function
* action-related content
* referenced targets
* argument structure
* contextual dependencies

### 2. Dialogue Act Classification

The submodule identifies the communicative role of the input within the interaction.

This allows downstream reasoning to distinguish between different forms of meaning even when lexical content overlaps.

For example, the utterance "Can you open the window?" may structurally appear as a question but function semantically as a request or command.

Dialogue act classification captures this interactional role.

### 3. Entity Extraction

The submodule extracts relevant semantic entities from the input and maps them into structured fields.

This includes identifying:

* actions
* objects
* devices
* places
* times
* people
* topics
* quantities
* media categories
* document references

### 4. Reference Detection and Resolution

The submodule identifies expressions that depend on prior context and attempts to resolve them into explicit targets.

This includes references to:

* previously mentioned objects
* earlier user choices
* active documents
* ongoing projects
* visible scene targets
* recently executed actions

### 5. Input Normalization at Semantic Level

The submodule normalizes equivalent expressions into a unified semantic representation.

For example:

* "switch on the lights"
* "turn on the lights"
* "activate the lights"

may be normalized into a shared action representation.

This is not lexical normalization at the perception layer, but semantic normalization at the meaning layer.

### 6. Language Identification and Linguistic Metadata

When multilingual interaction is supported, the submodule identifies the language and attaches linguistic metadata relevant for downstream interpretation.

This information can later influence:

* response generation
* speech synthesis
* tutoring mode
* language-specific clarification behaviour

### 7. Context Enrichment

The submodule enriches the semantic object with contextual information coming from other architectural modules.

This allows later reasoning to operate over the input within its real runtime situation.

### 8. Ambiguity Representation

The submodule explicitly represents unresolved uncertainty instead of forcing premature disambiguation.

This may include:

* ambiguous references
* multiple plausible entities
* incomplete argument structure
* under-specified targets

### 9. Completeness Assessment

The submodule determines whether the extracted meaning is semantically sufficient for intent detection and planning to proceed.

This does not yet produce the final clarification plan, but it exposes where semantic gaps exist.

### 10. Semantic Output Production

The submodule constructs the formal semantic object passed to intent detection or other downstream reasoning layers.

---

## Dialogue Act Classification

Dialogue act classification is one of the core internal functions of Semantic Interpretation.

A dialogue act describes the communicative role performed by the input within an interaction.

The lexical form of an utterance alone does not fully define its role. The same surface structure may correspond to different communicative functions depending on context.

Examples of dialogue act categories include:

* question
* command
* request
* confirmation
* rejection
* interruption
* correction
* clarification
* acknowledgment
* continuation
* social conversation
* greeting
* farewell
* dictation

Examples:

Input: "What time is it?"
Dialogue act: question

Input: "Play jazz music"
Dialogue act: command

Input: "yes"
Dialogue act: confirmation

Input: "no, not that one"
Dialogue act: rejection plus correction

Input: "stop"
Dialogue act: interruption or cancellation depending on context

The output of dialogue act classification is represented as part of the semantic object rather than as a separate detached label.

---

## Entity Extraction

Entity extraction transforms semantically relevant fragments of the input into structured data fields.

Entities are not merely words. They are meaning-bearing components of the request or interaction.

Typical semantic entity categories include:

* action
* object
* media type
* device
* location
* destination
* time expression
* date expression
* duration
* person
* project reference
* document reference
* topic
* quantity
* language
* mode

Example 1:

Input:

"Play jazz music"

Possible extracted structure:

* action: play
* genre: jazz
* object: music

Example 2:

Input:

"Turn on the living room lights"

Possible extracted structure:

* action: turn_on
* device: lights
* location: living_room

Example 3:

Input:

"Remind me tomorrow at five to call Alba"

Possible extracted structure:

* action: create_reminder
* date_expression: tomorrow
* time_expression: 17:00 candidate
* reminder_content: call Alba

Entity extraction is one of the main ways in which language becomes machine-usable semantic structure.

---

## Reference Resolution

Reference resolution is the semantic process through which context-dependent expressions are linked to explicit targets.

Natural conversation frequently uses reduced or indirect expressions.

Examples include:

* "Play it again"
* "Turn that off"
* "Navigate there"
* "Open the other one"
* "Use the same settings as before"

In these cases, Semantic Interpretation must search for the intended referent using contextual sources such as:

* recent dialogue turns
* active session state
* project context
* current screen selection
* visual attention results
* recent system outputs
* most recent tool result

Reference resolution may succeed, fail, or remain partially ambiguous.

The architecture must represent these outcomes explicitly.

Possible reference-resolution states include:

* resolved reference
* unresolved reference
* multiply-matched reference
* low-confidence reference

This explicit representation prevents downstream planners from acting on false certainty.

---

## Language Identification and Linguistic Context

When multilingual interaction is supported, Semantic Interpretation identifies the language or linguistic context associated with the input.

This information is relevant because semantic interpretation does not occur in a linguistic vacuum.

Language-related metadata may include:

* detected language
* mixed-language marker
* educational language mode
* formal versus informal register indicators when relevant
* transliteration or normalized script information when relevant

This metadata may later affect:

* downstream intent interpretation
* tutoring behaviour
* response language selection
* pronunciation-oriented actions

---

## Context Enrichment

Semantic Interpretation does not produce meaning from isolated input alone.

It enriches the semantic object with contextual metadata obtained from other architectural modules.

This contextual enrichment allows meaning to be represented in relation to the live system situation.

Examples of contextual metadata include:

* active user identity
* active session identifier
* interaction modality
* current project identifier
* current topic
* active dialogue state
* current FSM state
* current interface origin
* current permissions context
* recent system prompt awaiting confirmation

Example:

Input text: "yes"

Without context, the semantic content is minimal.

With contextual enrichment, the semantic object may represent:

* dialogue_act: confirmation
* confirmation_target: delete_session_request
* session_id: 42
* active_user_id: 7
* current_fsm_state: WAITING_FOR_CONFIRMATION

This enriched structure is what makes later reasoning coherent.

---

## Ambiguity Handling

Human inputs frequently contain semantic ambiguity.

Semantic ambiguity may arise from:

* under-specified targets
* multiple valid references
* vague temporal expressions
* multiple possible actions
* incomplete entity structure
* context mismatch

Example:

Input: "Open it"

Possible unresolved questions include:

* which object is "it"
* whether "open" refers to a file, app, door, or project

Example:

Input: "Play music"

Possible missing or ambiguous parameters include:

* genre
* artist
* playlist
* device
* source provider

The semantic interpreter does not need to fully solve all ambiguity at this stage.

Its responsibility is to expose ambiguity explicitly inside the semantic representation.

Possible ambiguity markers include:

* missing parameters
* multiple candidate referents
* uncertain action class
* weak contextual linkage

This explicitness is essential for downstream clarification and planning logic.

---

## Semantic Completeness and Incompleteness

Semantic completeness indicates whether the interpreted meaning contains enough structured information for downstream goal identification and planning to proceed.

A semantically complete input includes:

* recognizable communicative role
* sufficient argument structure
* sufficiently resolved references
* adequate contextual anchoring

A semantically incomplete input may contain:

* missing target
* missing time
* missing object reference
* incomplete action arguments
* unresolved contextual dependency

Example:

Input: "Play music"

Possible semantic state:

* dialogue_act: command
* candidate_action: play_media
* object: music
* semantic_status: partially_complete
* missing_parameters:

  * genre
  * artist_or_playlist
  * output_device

This explicit representation enables later clarification behaviour without collapsing the semantic layer into the planning layer.

---

## Internal Semantic Structures

To keep the architecture explicit, Semantic Interpretation manages several internal representational structures.

### semantic input object

Structured object representing the semantic interpretation of one input.

Typical fields may include:

* original_normalized_input
* semantic_text
* modality
* language
* dialogue_act
* extracted_entities
* resolved_references
* unresolved_references
* contextual_metadata
* ambiguity_markers
* completeness_status
* confidence_scores

### entity map

Structured representation of extracted entities and their values.

### reference map

Structured representation of references detected in the input and their resolution status.

### contextual attachment

Structured contextual metadata linked to the semantic object.

### ambiguity report

Structured representation of unresolved or weakly resolved meaning elements.

### completeness report

Structured representation of whether the semantic structure is sufficient for downstream processing.

These structures may remain internal implementation details in code, but architecturally they represent explicit information forms handled by the submodule.

---

## Example Semantic Representations

The following examples illustrate the kind of structured outputs produced by Semantic Interpretation.

### Example 1: direct command

Input:

"Play jazz music"

Possible semantic object:

semantic_input

* normalized_text: play jazz music
* modality: voice
* language: en
* dialogue_act: command
* entities:

  * action: play
  * genre: jazz
  * object: music
* references: none
* completeness_status: sufficient
* confidence: 0.94

### Example 2: contextual confirmation

Input:

"yes"

Possible semantic object:

semantic_input

* normalized_text: yes
* modality: voice
* dialogue_act: confirmation
* confirmation_target: previous_question
* contextual_anchor: pending_confirmation_request
* completeness_status: sufficient_relative_to_context
* confidence: 0.98

### Example 3: ambiguous reference

Input:

"Open it"

Possible semantic object:

semantic_input

* normalized_text: open it
* dialogue_act: command
* entities:

  * action: open
* unresolved_references:

  * target_object: it
* ambiguity_markers:

  * unresolved_target_reference
* completeness_status: insufficient
* confidence: 0.81

### Example 4: gesture command

Input:

recognized gesture: stop_gesture

Possible semantic object:

semantic_input

* modality: gesture
* dialogue_act: interruption
* semantic_action: stop_current_activity
* contextual_target: current_executing_process
* completeness_status: context-dependent but usable
* confidence: 0.92

---

## Interaction With Other Modules

Semantic Interpretation interacts with several architectural components.

### Relationship With Perception System

Perception provides already-recognized or classified input forms.

Examples include:

* speech transcript
* gesture classification
* object detection result
* detected visual target
* event classification output

Semantic Interpretation does not re-sense these signals. It converts them into semantic form.

### Relationship With Interaction Interfaces

Interaction Interfaces provide the human-facing channel context associated with the input.

This may influence interpretation by contributing metadata such as:

* voice origin
* touch origin
* local screen interaction
* remote frontend request

### Relationship With Dialogue and Session System

Dialogue and Session System provides the temporal and conversational context required for semantic interpretation.

This includes:

* previous dialogue turns
* active session context
* conversation history
* project association
* active topic
* recovery context

These inputs are especially important for reference resolution and interpretation of short responses.

### Relationship With Cognitive Core

Cognitive Core provides operational context relevant to semantic interpretation.

Examples include:

* active FSM state
* interaction mode
* waiting-for-confirmation state
* active execution state
* behavioural restrictions

This information affects how the same input is interpreted under different runtime conditions.

### Relationship With Identity, Access and Security

Identity-aware context may contribute to interpretation indirectly through active-user metadata, permissions context, or channel trust information.

### Relationship With Intent Detection

Intent Detection is the direct downstream consumer of the semantic output.

Semantic Interpretation provides a structured semantic object so that Intent Detection reasons over explicit meaning representations rather than over unstructured raw input.

---

## Representative Scenarios

### Scenario 1: explicit factual question

Input:

"What is the weather tomorrow?"

Semantic Interpretation extracts:

* dialogue act: question
* topic: weather
* date expression: tomorrow
* modality: voice or text
* language
* semantic completeness: sufficient

### Scenario 2: brief conversational control signal

Input:

"stop"

Semantic Interpretation extracts:

* dialogue act: interruption or cancellation candidate
* contextual dependency: current active action required
* semantic target: unresolved until context attachment
* completeness: context-dependent

### Scenario 3: follow-up reference

Previous dialogue:

System: "I found two restaurants nearby."
User: "Navigate to the second one."

Semantic Interpretation extracts:

* dialogue act: command
* action: navigate
* ordinal_reference: second
* referent_class: restaurant option
* contextual resolution source: previous system response
* semantic completeness: sufficient after reference resolution

### Scenario 4: project continuation signal

Input:

"Continue where we left off"

Semantic Interpretation extracts:

* dialogue act: continuation request
* project or session reference: contextual
* unresolved target if multiple projects are active
* semantic completeness: potentially partial

---

## Design Principles

Several architectural principles guide the design of Semantic Interpretation.

### Separation From Perception

Semantic Interpretation begins only after upstream modules have produced normalized input.

### Separation From Intent Detection

Semantic Interpretation extracts meaning structure but does not determine the final operative goal.

### Explicit Representation

Dialogue acts, entities, references, ambiguity markers, and completeness status are represented explicitly rather than left implicit.

### Context Dependence

Semantic meaning is represented relative to conversational, operational, and interaction context.

### Modality Unification

Inputs from different modalities can be transformed into a common semantic representation format.

### Uncertainty Preservation

The submodule preserves ambiguity and incompleteness instead of forcing premature resolution.

### Extensibility

New input forms, entity types, dialogue acts, and contextual enrichments can be added without changing the overall architectural role of the submodule.

---

## Outputs to Downstream Reasoning

The final output of Semantic Interpretation is a normalized semantic representation containing structured meaning information.

Typical output contents include:

* normalized semantic content
* dialogue act classification
* extracted entities
* resolved and unresolved references
* contextual metadata
* ambiguity markers
* completeness status
* semantic confidence metadata

This semantic object is passed primarily to the **Intent Detection submodule (6.2)**.

Intent Detection then uses this structure to determine the operative goal or objective behind the input.

In this way, Semantic Interpretation acts as the formal handoff layer between recognized input and intentional reasoning.

---

## Architectural Importance

Semantic Interpretation is the architectural submodule that allows NORA to reason over meaning rather than over raw recognized input.

Through this submodule, the architecture gains:

* explicit semantic structuring of input
* dialogue-act awareness
* entity extraction
* context-aware reference resolution
* modality-independent semantic representation
* explicit ambiguity handling
* completeness assessment for downstream reasoning

Without Semantic Interpretation, Intent Detection and planning would have to operate directly over raw transcripts, gesture labels, and event strings, producing tighter coupling and weaker architectural clarity.

For that reason, Semantic Interpretation is a foundational reasoning submodule within the Planning, Interpretation and Agents layer.

# 6.2 Intent Detection

#definition: subsystem responsible for identifying the operative goal, objective, or task implied by a semantically interpreted input and mapping that goal into a structured intent representation usable by the planning system.

## Definition

Intent Detection is the second reasoning submodule within the Planning, Interpretation and Agents layer.

Its function is to determine what the system is expected to accomplish based on the semantic representation produced by the Semantic Interpretation subsystem.

While Semantic Interpretation extracts the meaning structure of an input, Intent Detection identifies the objective implied by that structure.

The submodule therefore transforms semantic meaning into goal-oriented representation.

Within the architecture of NORA, Intent Detection is the component responsible for converting interpreted meaning into an explicit operational objective that the system can pursue.

---

## Architectural Purpose

The architectural purpose of Intent Detection is to determine the goal that underlies a user input or system-triggered interaction.

Human communication frequently expresses intentions indirectly, implicitly, or through incomplete language. Even when the semantic structure of a sentence is known, the objective behind that sentence still needs to be determined.

For example:

Input:

"Play jazz music"

Semantic Interpretation extracts:

* action: play
* object: music
* genre: jazz

Intent Detection transforms this semantic structure into an operational goal:

intent: play_music

This goal representation allows downstream modules to construct an execution strategy capable of satisfying the request.

Intent Detection therefore bridges the gap between interpreted meaning and actionable system objectives.

---

## Architectural Role

Intent Detection acts as the goal-recognition layer of the NORA reasoning pipeline.

Within the internal reasoning chain, its role can be represented as:

Perception → Semantic Interpretation → Intent Detection → Planner → Tool Selection → Execution

Each stage in this sequence has a clearly defined responsibility.

Perception converts signals into recognizable input.

Semantic Interpretation converts recognizable input into structured meaning.

Intent Detection converts structured meaning into a goal.

Planning converts that goal into a strategy for achieving it.

This layered structure ensures that meaning extraction and goal identification remain separate architectural processes.

---

## Why This Submodule Is Necessary

Semantic meaning alone does not always specify what the system should do.

Two inputs may contain similar semantic elements while implying different objectives.

Example:

"Can you play jazz music?"

Semantically this may appear as a question, but its communicative function is usually a request to perform the action.

Example:

"I like jazz music"

Semantic content contains the same entities but expresses no actionable request.

Intent Detection determines which of these interpretations corresponds to an operative goal.

Without a dedicated Intent Detection stage, downstream planning components would need to infer goals directly from raw semantic structures, creating tighter coupling and reducing architectural clarity.

Intent Detection isolates the recognition of objectives into a dedicated reasoning layer.

---

## Core Concepts

Intent Detection is defined through several architectural concepts.

### intent

Structured representation of a goal or task that the system may attempt to accomplish.

Examples include:

* play_music
* control_device
* capture_photo
* knowledge_query
* navigation_request
* tutoring_session
* create_reminder

### intent class

Category grouping multiple related intents under a shared conceptual family.

Examples:

* information_retrieval
* device_control
* multimedia
* tutoring
* conversation
* productivity

### intent candidate

Possible intent interpretation inferred from the semantic representation before final selection.

### intent resolution

Process of selecting the most plausible intent candidate based on semantic structure, contextual information, and system capabilities.

### intent confidence

Quantitative estimate associated with the likelihood that the detected intent corresponds to the user's actual objective.

### contextual intent refinement

Process through which contextual information modifies or specializes the detected intent.

### intent parameters

Structured arguments associated with the intent that specify how the goal should be executed.

Example parameters:

* target_device
* destination
* media_genre
* time_expression
* document_reference

### intent feasibility

Assessment of whether the system is capable of executing the detected intent given current system capabilities and permissions.

### intent completeness

Indicator describing whether sufficient parameters are available to execute the detected intent or whether clarification is required.

These concepts define the representational structure of Intent Detection.

---

## Scope of the Submodule

The Intent Detection subsystem includes the architectural mechanisms responsible for recognizing the goal associated with a semantically interpreted input.

Its scope includes:

* classification of semantic inputs into intent categories
* generation of candidate intents
* contextual refinement of candidate intents
* detection of goal-oriented requests
* recognition of conversational or social intents
* mapping semantic entities to intent parameters
* evaluation of intent confidence
* detection of incomplete intent structures
* identification of clarification requirements
* production of structured intent objects

Its scope does not include:

* semantic parsing itself
* raw signal processing
* tool selection
* planning strategies
* execution of actions
* user interface responses

These responsibilities belong to Semantic Interpretation, Planner, Tool Selector, or Action and Expression modules.

---

## Position in the Architecture

Within the Planning, Interpretation and Agents layer, Intent Detection follows Semantic Interpretation and precedes planning.

Architectural position:

Perception → Semantic Interpretation → Intent Detection → Planner

This ordering ensures that goal recognition occurs only after semantic meaning has been structured.

Semantic Interpretation provides a structured description of the input.

Intent Detection determines the objective implied by that description.

Planner then determines how the objective can be achieved.

---

## Types of Intent Recognized

Intent Detection must recognize several families of user goals.

### Informational queries

Requests whose objective is to retrieve knowledge or information.

Examples:

* "What is the capital of France?"
* "What time is it?"
* "How far is Barcelona from Madrid?"

Possible classification:

intent: knowledge_query

---

### Action commands

Requests that require the system to perform a concrete action affecting the environment or system state.

Examples:

* "Play music"
* "Turn on the lights"
* "Take a picture"

Possible classifications:

* play_music
* control_device
* capture_photo

---

### Conversational intents

Inputs representing social interaction rather than operational commands.

Examples:

* "How are you?"
* "Tell me a joke"
* "Good morning"

Possible classification:

intent: casual_conversation

---

### Learning and tutoring intents

Requests involving explanation, learning support, or training interaction.

Examples:

* "Explain quantum mechanics"
* "Help me learn English"

Possible classifications:

* tutoring_session
* explanation_request

---

### Productivity intents

Requests related to organization, scheduling, or personal productivity.

Examples:

* "Create a reminder"
* "Add this to my calendar"

Possible classifications:

* create_reminder
* calendar_event

---

### Navigation and location intents

Requests related to routes, locations, or spatial movement.

Examples:

* "Navigate to the nearest restaurant"

Possible classification:

intent: navigation_request

---

### System configuration intents

Requests that modify system configuration or operational parameters.

Examples:

* "Change language to Spanish"
* "Increase volume"

Possible classifications:

* change_language
* adjust_volume

---

## Context-Aware Intent Detection

Intent recognition rarely occurs in isolation from conversational context.

Many short inputs depend on previously established interaction state.

Example interaction:

User: "Play music"

Intent detected:

play_music

Later input:

User: "Stop"

Semantic Interpretation may detect a generic interruption command.

Intent Detection must determine which activity should be stopped.

Using contextual information such as:

* active media playback
* current execution state
* previous commands

The detected intent becomes:

stop_music

Contextual reasoning may rely on:

* dialogue history
* active session state
* currently executing actions
* ongoing tasks

---

## Handling Ambiguous Inputs

Certain inputs may correspond to multiple potential goals.

Example:

"Open it"

Possible intent interpretations include:

* open_document
* open_application
* open_door

Intent Detection evaluates these possibilities using contextual signals such as:

* recent conversation history
* visual perception results
* current interface context
* system operational state

If ambiguity remains unresolved, the detected intent may remain provisional until clarification occurs.

---

## Intent Candidate Generation

Intent Detection may generate multiple candidate interpretations before selecting the final intent.

Each candidate may include:

* candidate intent class
* candidate parameters
* confidence estimate
* contextual compatibility

The final intent is selected based on combined evaluation of semantic evidence and contextual constraints.

---

## Intent Representation

The output of Intent Detection is a structured object describing the detected goal.

Example structure:

intent_object

* intent: play_music
* confidence: 0.91
* parameters:

  * genre: jazz
  * device: default_speaker

Another example:

intent_object

* intent: navigation_request
* confidence: 0.88
* parameters:

  * destination: nearest_restaurant

This structured representation becomes the input to the Planner.

---

## Confidence Scoring

Each detected intent is associated with a confidence value representing the system's estimate of interpretation reliability.

Confidence may be derived from:

* semantic extraction certainty
* contextual alignment
* classifier output
* historical interaction patterns

Example interpretation rules:

confidence > 0.85

Intent considered reliable for direct planning.

confidence between 0.6 and 0.85

Intent may require confirmation.

confidence < 0.6

Clarification likely required.

These thresholds may vary depending on system design and risk tolerance.

---

## Intent Feasibility

Intent Detection may also verify whether the detected goal corresponds to a capability available within the system.

Example:

User input:

"Fly the drone to Paris"

If the system lacks drone control capability, the detected intent may be marked as unsupported.

Possible output states include:

* supported intent
* unsupported intent
* partially supported intent

This information helps downstream modules decide how to respond.

---

## Interaction With Other Modules

Intent Detection interacts with several architectural components.

### Semantic Interpretation

Provides structured semantic representation including:

* normalized input
* dialogue act classification
* extracted entities
* contextual metadata

### Dialogue and Session System

Provides conversational context including:

* previous dialogue turns
* active session information
* conversation history

### Cognitive Core

Provides system-level contextual state including:

* operational mode
* active execution state
* interaction mode

### Planner

Receives the detected intent and constructs a strategy for achieving the goal.

---

## Representative Scenarios

### Scenario 1: direct action request

Input:

"Play jazz music"

Detected intent:

intent: play_music

Parameters:

* genre: jazz

---

### Scenario 2: informational request

Input:

"What is the capital of France?"

Detected intent:

intent: knowledge_query

Parameters:

* topic: capital_of_france

---

### Scenario 3: contextual stop command

Input:

"Stop"

Context:

active task: music playback

Detected intent:

intent: stop_music

---

### Scenario 4: productivity request

Input:

"Remind me tomorrow at five to call Alba"

Detected intent:

intent: create_reminder

Parameters:

* date: tomorrow
* time: 17:00
* content: call Alba

---

## Design Principles

Several architectural principles guide the design of Intent Detection.

### Separation From Semantic Interpretation

Intent Detection operates over semantic representations rather than raw language.

### Separation From Planning

Intent Detection identifies the goal but does not determine how the goal will be executed.

### Context Awareness

Intent interpretation considers conversational and operational context.

### Explicit Representation

Goals, parameters, and confidence values are represented explicitly.

### Capability Awareness

Detected intents may be evaluated against the capabilities available to the system.

### Extensibility

New intents and intent families can be added without modifying the fundamental architecture.

---

## Output to the Planner

The final output of Intent Detection is a structured intent object containing:

* detected intent
* intent parameters
* confidence score
* contextual dependencies
* feasibility status

This intent object is passed to the **Planner submodule (6.3)**.

The Planner then determines the sequence of actions required to satisfy the detected goal.

---

## Architectural Importance

Intent Detection is the architectural mechanism that allows NORA to transform interpreted meaning into goal-oriented reasoning.

Through this subsystem, the architecture gains:

* explicit goal recognition
* classification of user objectives
* contextual refinement of requests
* detection of incomplete goals
* detection of unsupported requests
* structured input for planning

Without Intent Detection, planning systems would have to infer goals directly from semantic structures, increasing coupling and reducing modular clarity.

For this reason, Intent Detection is a central reasoning submodule within the Planning, Interpretation and Agents layer.

# 6.3 Planner

#definition: subsystem responsible for constructing a structured execution strategy that transforms a detected intent into an ordered sequence of decisions, reasoning steps, tool invocations, interactions and outputs that can be executed by downstream modules.

## Definition

The Planner is the core orchestration subsystem within the Planning, Interpretation and Agents layer.

Its responsibility is to transform a detected intent and its associated semantic representation into a structured execution strategy capable of achieving the desired objective.

Unlike Semantic Interpretation, the Planner does not attempt to understand the meaning of an input. Unlike Action and Expression modules, the Planner does not execute actions directly.

Instead, the Planner defines what must happen, in what order it must happen, under which conditions it must happen, and which system capabilities must be involved.

Within the architecture of NORA, the Planner acts as the reasoning component that converts recognized goals into coordinated operational workflows.

---

## Architectural Purpose

The architectural purpose of the Planner is to bridge the gap between goal recognition and action execution.

Human requests rarely correspond to single atomic operations. Most objectives require intermediate reasoning steps, conditional decisions, information retrieval, clarification with the user, or coordination across multiple subsystems.

The Planner exists to design the structured process through which those operations occur.

Instead of executing isolated reactions to commands, the system constructs an explicit plan describing the entire workflow required to achieve the objective.

Through this mechanism, NORA is able to operate as a coherent assistant capable of multi-step reasoning and coordinated behaviour rather than as a collection of independent responses.

---

## Architectural Role

Within the reasoning pipeline of NORA, the Planner occupies the stage that transforms goals into operational workflows.

The conceptual pipeline is:

Perception → Semantic Interpretation → Intent Detection → Planner → Tool Selector → Specialized Agents → Action and Expression

Each stage performs a distinct architectural function.

Perception transforms physical signals into interpretable inputs.

Semantic Interpretation converts inputs into structured semantic meaning.

Intent Detection identifies the objective behind that meaning.

The Planner designs the workflow required to achieve the objective.

The Tool Selector chooses the concrete technical instruments required for execution.

Specialized Agents perform domain-specific reasoning tasks.

Action and Expression executes the resulting outputs.

This layered separation ensures that planning remains a dedicated reasoning function distinct from both interpretation and execution.

---

## Why Planning Is Necessary

Many requests cannot be executed immediately because they require additional reasoning, contextual decisions or multiple coordinated operations.

For example:

User input:

"What time is it?"

Possible plan:

1 retrieve current time
2 format response
3 deliver response via voice and screen

This case is simple and requires only a minimal workflow.

However, many real interactions require more complex reasoning.

Example:

"Navigate to a restaurant"

This request requires multiple decisions before execution:

* determining which restaurant
* identifying the user's location
* choosing navigation mode
* retrieving route information
* presenting the route

Possible plan:

1 determine whether a specific restaurant was mentioned
2 if destination missing ask clarification question
3 wait for user answer
4 retrieve route information
5 generate route summary
6 display route
7 speak navigation instructions

Without planning, the system would be unable to structure such interactions coherently.

Planning allows NORA to construct explicit task workflows rather than reacting to commands in isolation.

---

## Core Concepts

The Planner subsystem is defined through several architectural concepts.

### plan

Structured description of a workflow that leads from a detected intent to a completed objective.

A plan defines the ordered sequence of steps required to achieve a goal.

### planning step

Atomic reasoning or operational unit within a plan.

Examples include:

* retrieving information
* invoking a tool
* asking a clarification question
* generating a response
* performing a device action

### plan dependency

Relationship between steps that determines execution order.

Some steps cannot begin until other steps have completed.

### plan precondition

Condition that must be satisfied before a step or the entire plan can execute.

Examples:

* device availability
* authentication
* network connectivity

### plan branch

Conditional path within a plan depending on runtime conditions.

Example:

if destination missing → ask user
else → retrieve route

### plan fallback

Alternative strategy used when a step fails.

Example:

if weather API unavailable → notify user that real-time data cannot be retrieved

### plan status

State describing whether the plan is ready for execution, waiting for clarification, paused or completed.

### clarification step

Interaction step in which the system asks the user for missing information required to continue the plan.

### confirmation step

Interaction step used when the system requires explicit user approval before performing a sensitive action.

### replanning

Process through which the Planner modifies an existing plan when new information arrives or conditions change.

These concepts define the representational vocabulary of the Planner subsystem.

---

## Scope of the Submodule

The Planner subsystem includes all architectural mechanisms responsible for constructing and managing execution strategies.

Its scope includes:

* goal decomposition
* step generation
* plan ordering
* conditional branching
* clarification logic
* confirmation logic
* context-aware plan generation
* plan adaptation
* plan interruption handling
* replanning
* coordination with downstream modules

Its scope does not include:

* semantic parsing
* goal recognition
* tool implementation
* physical actuation
* UI rendering

These functions belong to other modules such as Semantic Interpretation, Intent Detection, Tool Selector and Action and Expression.

---

## Types of Planning

The Planner must support several categories of planning complexity.

### single-step planning

Some tasks require a minimal workflow consisting of a single operational step followed by response generation.

Example:

User input: "Increase volume"

Possible plan:

1 validate permissions
2 adjust system volume
3 confirm result

### conditional planning

Some plans include conditional decisions depending on context or missing information.

Example:

User input: "Delete this session"

Possible plan:

1 identify session
2 request confirmation
3 if confirmation received delete session
4 report result

### multi-step planning

Some objectives require several coordinated actions.

Example:

User input: "Plan my study session for tomorrow"

Possible plan:

1 retrieve calendar schedule
2 identify available time blocks
3 identify relevant study topic
4 generate study schedule proposal
5 request user confirmation
6 create reminders
7 summarize schedule

### reactive planning

Planning may be triggered by internal system events rather than user requests.

Example event:

low battery detected

Possible plan:

1 evaluate active tasks
2 save session state
3 inform user
4 initiate safe shutdown or charging routine

### replanning

The Planner must modify plans when conditions change.

Examples include:

* user changes their mind
* network services become unavailable
* higher priority task interrupts current plan

---

## Inputs to the Planner

The Planner integrates information from several modules.

### from Intent Detection

* detected intent
* intent parameters
* confidence level
* feasibility indicators

### from Semantic Interpretation

* dialogue act
* extracted entities
* contextual references
* semantic completeness information

### from Dialogue and Session System

* active session identifier
* conversation history
* current project
* remembered interaction decisions

### from Cognitive Core

* current system state
* operational mode
* active finite-state machine state
* module availability

### from Identity and Permissions

* user identity
* access permissions
* personalization preferences

These inputs ensure that planning decisions are context-aware and capability-aware.

---

## Core Responsibilities

The Planner performs several reasoning tasks.

### goal decomposition

Breaking a high-level objective into smaller operational tasks.

### missing information detection

Determining whether additional information is required to execute the plan.

### clarification management

Designing interaction steps that obtain missing information from the user.

### confirmation policy

Determining when explicit confirmation is required before executing sensitive actions.

### step ordering

Ensuring that plan steps occur in a logical sequence.

### conditional branching

Designing decision points within the plan based on runtime conditions.

### failure handling

Designing fallback strategies when steps fail.

### plan coordination

Ensuring that downstream modules receive coherent instructions.

---

## Plan Structure

The Planner produces a structured plan object describing the execution strategy.

Example conceptual structure:

plan_object

plan_id: p_1042
intent: navigation_request
objective: guide user to restaurant
status: waiting_for_clarification
missing_information:

* destination

steps:

1 ask_user_for_destination
2 retrieve_route
3 summarize_route
4 display_map
5 speak_navigation

outputs:

* screen
* voice

priority: normal

Another example:

plan_object

plan_id: p_2018
intent: knowledge_query
objective: answer factual question
status: ready

steps:

1 retrieve_information
2 generate_answer
3 speak_answer

---

## Planning Policies

The Planner should follow consistent reasoning policies.

### minimum necessary execution

Plans should avoid unnecessary complexity when a direct solution exists.

### context usage

Contextual information should be used before asking clarification questions.

### safety prioritization

Sensitive actions must respect confirmation policies and permissions.

### interruptibility

Plans should remain interruptible and cancellable.

### resilience

Plans should anticipate possible execution failures.

---

## Interaction with Operational State

Planning must account for the current runtime condition of the system.

Examples include:

* system currently speaking
* hardware unavailable
* network connectivity lost
* restricted system mode

Plans generated without awareness of these conditions would be unreliable.

---

## Interaction with Tool Selector and Agents

The Planner identifies the categories of capabilities required for execution.

Examples include:

* information retrieval
* navigation
* OCR
* multimedia playback
* document analysis

The Tool Selector determines which concrete engine or integration should be used to perform those operations.

Specialized Agents may be invoked when domain-specific reasoning is required.

The architectural division therefore becomes:

Planner → workflow design
Tool Selector → capability selection
Specialized Agents → domain reasoning

---

## Handling Interruptions and Cancellations

Plans must support dynamic interaction changes.

Examples include:

* user interruption
* cancellation requests
* environmental events

The Planner must support:

* cancellation
* pausing
* resuming
* plan modification

---

## Representative Scenarios

### factual query

User: "What is the weather today?"

Possible plan:

1 determine user location
2 retrieve weather information
3 generate answer
4 deliver response

### document summarization

User: "Read this paper and summarize it"

Possible plan:

1 retrieve document
2 extract text
3 perform summarization
4 present summary

### secure device action

User: "Open the front door"

Possible plan:

1 verify authentication
2 verify device availability
3 request confirmation
4 send device command
5 report result

### tutoring interaction

User: "Help me practice English"

Possible plan:

1 identify learning mode
2 retrieve user proficiency level
3 initiate tutoring session
4 track progress
5 store learning results

---

## Output to Downstream Modules

The final output of the Planner is a structured execution strategy describing:

* steps
* conditions
* dependencies
* required capabilities
* expected outputs

This plan is then transmitted to:

* the Tool Selector
* Specialized Agents
* Action and Expression modules

---

## Architectural Importance

The Planner is one of the most central reasoning components of the NORA architecture.

Through this subsystem, the system gains:

* multi-step task coordination
* structured goal execution
* context-aware workflows
* safe handling of sensitive actions
* dynamic adaptation to runtime changes

Without a Planner, the system would behave as a set of disconnected responses rather than as a coherent assistant capable of structured task completion.

# 6.4 Tool Selector

#definition: subsystem responsible for resolving abstract capabilities required by a plan into concrete tools, integrations, services, engines, internal modules or agents capable of executing each step of the plan.

## Definition

The Tool Selector is the capability resolution subsystem of the Planning, Interpretation and Agents layer.

Its function is to map abstract operational requirements produced by the Planner into specific executable implementations.

The Planner determines what must be done. The Tool Selector determines which concrete mechanism should do it.

In a complex cognitive system such as NORA, many operational capabilities may have multiple possible implementations. A request such as "play music" could be satisfied through different providers, devices or services. Similarly, document reading may be performed through local parsers, OCR engines or external services.

The Tool Selector exists to resolve this multiplicity into a concrete choice that respects system capabilities, runtime conditions, user preferences and security policies.

---

## Architectural Purpose

The architectural purpose of the Tool Selector is to decouple high-level planning from implementation-level execution.

Planning systems should reason in terms of capabilities rather than specific implementations. For example, the Planner may require a capability such as "retrieve_weather", "search_web" or "play_media" without specifying which particular provider must be used.

The Tool Selector translates those capability requirements into executable selections by evaluating the available tools, integrations and agents within the system.

This separation provides several benefits:

* plans remain implementation-independent
* new tools can be added without changing planning logic
* tool selection can adapt dynamically to runtime conditions
* different providers can be selected based on user preferences or system policy

Through this mechanism, NORA maintains a modular architecture where capabilities remain stable while implementations can evolve.

---

## Architectural Role

Within the internal reasoning pipeline of NORA, the Tool Selector appears after planning and before execution or domain reasoning.

Conceptual pipeline:

Perception → Semantic Interpretation → Intent Detection → Planner → Tool Selector → Specialized Agents → Action and Expression

In this chain:

Semantic Interpretation extracts structured meaning.

Intent Detection identifies the user goal.

The Planner designs the execution workflow.

The Tool Selector resolves which concrete capabilities will be used to execute each step.

Specialized Agents perform domain-specific reasoning when required.

Action and Expression executes the final outputs.

This layered structure prevents execution decisions from leaking into higher-level reasoning components.

---

## Why Tool Selection Is Necessary

Many operations in a cognitive system can be implemented in multiple ways.

Examples include:

* retrieving knowledge through local memory, vector search, web search or external APIs
* performing OCR using a local engine or a cloud service
* playing music through different providers
* retrieving weather information from multiple APIs
* performing summarization using different language models

Without a dedicated Tool Selector subsystem, the architecture would face several problems:

* planning logic would need to hardcode provider choices
* provider selection would be duplicated across modules
* replacing or upgrading integrations would become difficult
* runtime adaptation to failures or unavailable services would be limited

By introducing a dedicated capability resolution layer, the architecture separates capability requirements from implementation choices.

---

## Core Concepts

The Tool Selector is defined through several architectural concepts.

### capability

Abstract operational function required to perform a plan step.

Examples:

* retrieve_weather
* search_web
* play_media
* control_device
* read_document
* summarize_text

### tool

Concrete implementation capable of performing a capability.

Examples:

* spotify_playback
* youtube_media_player
* local_pdf_parser
* tesseract_ocr
* google_maps_api

### tool provider

External service or internal module that implements a tool.

### tool candidate

Possible tool capable of fulfilling a capability requirement.

### tool resolution

Process of selecting one tool from among available candidates.

### fallback tool

Alternative tool used if the preferred implementation is unavailable.

### tool chain

Sequence of tools required to complete a complex plan step.

### capability registry

System catalog that records available tools and the capabilities they implement.

These concepts define the representational vocabulary of the Tool Selector subsystem.

---

## Scope of the Submodule

The Tool Selector subsystem includes the architectural mechanisms responsible for resolving capability requirements into executable implementations.

Its scope includes:

* mapping plan capabilities to tools
* evaluating candidate implementations
* selecting preferred providers
* validating tool availability
* enforcing permission policies
* applying user preferences
* generating fallback strategies
* supporting multi-tool workflows

Its scope does not include:

* designing execution workflows
* performing domain reasoning
* executing tools
* rendering outputs

These responsibilities belong to the Planner, Specialized Agents and Action modules.

---

## Categories of Tools

The Tool Selector may select tools across multiple capability domains.

### information retrieval tools

Examples:

* web search engines
* vector search systems
* knowledge base retrieval
* weather APIs
* news APIs

### productivity tools

Examples:

* calendar integration
* reminder services
* email systems
* note-taking services

### multimedia tools

Examples:

* Spotify playback
* YouTube streaming
* local audio player
* text-to-speech engines

### vision and reading tools

Examples:

* OCR engines
* document parsers
* object detection models
* gesture recognition systems

### navigation tools

Examples:

* mapping services
* route planners
* places search APIs

### smart home tools

Examples:

* home automation hubs
* MQTT device control
* smart lighting APIs

### internal system tools

Examples:

* session memory access
* summarization engines
* configuration services
* permission validation modules

---

## Inputs to the Tool Selector

The Tool Selector integrates information from several upstream modules.

### from the Planner

* required capability
* plan step identifier
* expected output modality
* fallback policy

### from the Cognitive Core

* module availability
* hardware status
* operational restrictions

### from Identity and Permissions

* user access rights
* tool-level authorization

### from User Preferences

* preferred service providers
* configured defaults

### from Observability Systems

* tool health status
* recent failure events
* latency metrics
* quota availability

These inputs allow tool selection to adapt dynamically to runtime conditions.

---

## Core Responsibilities

The Tool Selector performs several reasoning tasks.

### capability resolution

Mapping abstract capabilities into concrete tool candidates.

### provider selection

Selecting the most appropriate tool among candidates.

### availability validation

Verifying that the selected tool can currently operate.

### fallback preparation

Identifying alternative tools in case the primary option fails.

### policy enforcement

Ensuring tool usage complies with security and privacy rules.

### multi-tool coordination

Selecting multiple tools when a plan step requires several operations.

---

## Selection Criteria

Tool selection decisions should follow explicit criteria.

### functional compatibility

The tool must support the required capability.

### runtime availability

The tool must be operational and reachable.

### permission compatibility

The action must be allowed under current security policies.

### contextual suitability

The tool must make sense given the current environment and request context.

### user preference alignment

User-configured providers should be preferred when possible.

### performance considerations

Latency, reliability and operational cost may influence selection.

### safety and privacy

Sensitive tasks should favor secure or local execution paths when appropriate.

---

## Tool Registry Concept

Maintaining a centralized tool registry simplifies capability resolution.

A registry entry may contain metadata such as:

* tool identifier
* capability type
* supported input formats
* supported output formats
* authentication requirements
* permission constraints
* privacy classification
* performance metrics
* priority ranking
* fallback order

Example registry entry:

tool_id: spotify_playback
capability: play_media
requires_authentication: true
privacy_level: external_service
priority_score: high
fallback_rank: 1

Such metadata allows the Tool Selector to evaluate candidate tools systematically.

---

## Tool Resolution Output

The Tool Selector produces a structured resolution describing which tool will execute each plan step.

Example structure:

tool_resolution

step_id: step_03
required_capability: route_lookup
selected_tool: maps_provider_api
fallback_tools:

* local_route_engine
* cached_route_lookup

resolution_reason:

* provider_available
* user_preference

---

## Interaction with Specialized Agents

Certain tasks may require domain-specific reasoning rather than direct tool execution.

Examples include:

* tutoring interactions
* navigation planning
* productivity assistance

In these cases, the Tool Selector may route execution to a Specialized Agent rather than selecting a low-level tool directly.

The agent then manages its own internal tools and reasoning processes.

---

## Failure Handling

The Tool Selector must remain resilient to runtime failures.

Examples include:

* authentication expiration
* network outages
* API quota limits
* hardware disconnections

Possible responses include:

* switching to fallback tools
* requesting replanning
* entering reduced capability mode
* reporting execution limitations

---

## Example Selection Scenarios

### weather request

Plan requirement: retrieve weather data

Possible resolution:

primary tool: weather_api
fallback tool: web_search_weather

### music playback

Plan requirement: play media

Possible resolution:

primary tool: spotify_player
fallback tool: youtube_player
fallback tool: local_audio_library

### document summarization

Plan requirements:

* retrieve document
* extract text
* summarize

Possible tool chain:

1 local_file_loader
2 pdf_parser
3 summarization_engine

### smart home control

Plan requirement: control device

Possible resolution:

primary tool: home_assistant_integration
fallback tool: device_vendor_api

---

## Architectural Importance

The Tool Selector is a key subsystem for maintaining modularity and flexibility within NORA.

Through this subsystem the architecture gains:

* decoupling between planning and execution
* dynamic provider selection
* integration extensibility
* runtime adaptability
* policy-aware execution

Without a Tool Selector, planning logic would become tightly coupled to implementation choices and the architecture would lose flexibility.

For this reason, the Tool Selector should be considered a fundamental component of the planning and execution pipeline.

# 6.5 Specialized Agents

#definition: modular reasoning components with domain-specific knowledge, internal workflows and contextual memory capable of solving complex tasks within a defined problem domain using tools, dialogue and planning assistance.

## Definition

Specialized Agents are domain-oriented reasoning subsystems that operate within the Planning, Interpretation and Agents layer of the NORA architecture.

Their role is to perform complex reasoning and interaction tasks that cannot be handled efficiently by generic planning logic alone.

While the Planner constructs the overall execution strategy and the Tool Selector resolves which capabilities should be used, Specialized Agents execute domain-specific reasoning processes required to complete a task.

A Specialized Agent encapsulates the knowledge structures, reasoning patterns, domain workflows and contextual state required to operate effectively within a specific problem space.

Instead of forcing the central planning architecture to contain logic for every domain, NORA delegates certain tasks to agents that specialize in those domains.

---

## Architectural Purpose

The purpose of Specialized Agents is to enable scalable, modular intelligence across multiple domains without turning the central reasoning system into a monolithic structure.

Many tasks require knowledge and reasoning patterns that are unique to a domain. For example:

* tutoring requires pedagogical interaction
* navigation requires route reasoning
* productivity requires scheduling logic
* multimedia requires media selection and playback control

Embedding all of this logic in the Planner would create a rigid and complex system.

Specialized Agents solve this problem by isolating domain expertise into dedicated modules.

Through this architecture:

* the Planner coordinates tasks
* the Tool Selector resolves capabilities
* the Specialized Agent performs domain reasoning

---

## Architectural Role

Specialized Agents appear downstream from the Planner and Tool Selector in the NORA reasoning pipeline.

Conceptual pipeline:

Perception → Semantic Interpretation → Intent Detection → Planner → Tool Selector → Specialized Agents → Action and Expression

In this architecture:

Semantic Interpretation extracts meaning from inputs.

Intent Detection identifies the user objective.

The Planner constructs the workflow required to achieve the objective.

The Tool Selector resolves which capabilities will be used.

Specialized Agents execute domain-specific reasoning when required.

Action and Expression produces outputs and performs actions in the world.

The Planner may choose to delegate an entire workflow to an agent or to invoke an agent as part of a larger plan.

---

## Why Specialized Agents Are Necessary

Certain problem domains require reasoning patterns that differ substantially from generic task execution.

Examples include:

* tutoring interactions that adapt to user skill level
* route planning that considers transportation options
* document analysis requiring structured reading
* home automation involving device states

Attempting to encode all of this logic within the central Planner would produce a system that is difficult to maintain and extend.

By introducing Specialized Agents, the architecture gains a mechanism for distributing intelligence across domain-specific modules.

Each agent can evolve independently while remaining coordinated by the central planning system.

---

## Core Concepts

The Specialized Agents subsystem is defined through several architectural concepts.

### agent

A reasoning module dedicated to a specific domain capable of performing domain-aware decision making.

### domain

The problem space within which an agent operates.

Examples include learning, navigation, multimedia, or productivity.

### agent workflow

Sequence of reasoning steps performed by the agent to complete a task within its domain.

### agent state

Internal contextual information maintained during the execution of an agent task.

### agent capability

Set of tools, reasoning strategies and data sources available to an agent.

### agent delegation

Process through which the Planner assigns responsibility for a task to an agent.

These concepts define the operational model of Specialized Agents.

---

## Scope of the Submodule

The Specialized Agents subsystem includes the architectural mechanisms responsible for domain-level reasoning.

Its scope includes:

* domain reasoning
* domain-specific task decomposition
* tool orchestration within the domain
* contextual dialogue inside the domain
* domain-level state tracking
* adaptive workflows based on user interaction

Its scope does not include:

* global planning
* intent detection
* capability resolution
* low-level execution

These responsibilities belong to the Planner, Intent Detection, Tool Selector and Action modules.

---

## Agent Responsibilities

A Specialized Agent may perform several categories of tasks.

### domain reasoning

The agent understands the conceptual structure of its domain.

For example, a Navigation Agent understands concepts such as:

* route
* origin
* destination
* transportation mode
* estimated travel time

A Learning Agent understands concepts such as:

* exercises
* explanations
* difficulty levels
* progress tracking

---

### task decomposition

The agent may break a request into smaller domain-specific operations.

Example request:

"Explain quantum mechanics simply"

Possible agent workflow:

1 determine user knowledge level
2 retrieve relevant explanation
3 simplify technical concepts
4 provide examples
5 verify user understanding

---

### tool orchestration

Agents may coordinate the use of multiple tools within their domain.

Example reading workflow:

1 document retrieval
2 OCR or parsing
3 semantic analysis
4 summary generation
5 output generation

---

### dialogue management within the domain

Certain tasks require continuous conversational interaction.

Example tutoring interaction:

* ask questions
* evaluate answers
* provide corrective feedback
* adjust difficulty level

---

### state management

Agents may maintain internal state during extended tasks.

Example productivity state:

* pending reminders
* recurring schedules
* confirmation requests

This state may persist for the duration of the interaction.

---

## Agent Invocation

The Planner determines when a Specialized Agent should be invoked.

Typical situations include:

* tasks requiring domain reasoning
* multi-step workflows within a domain
* structured learning sessions
* navigation assistance
* document analysis

Example invocation:

Detected intent: practice_language

Planner decision: invoke Learning Agent

---

## Types of Domain Agents

A system such as NORA may include multiple domain agents.

### Conversation Agent

Definition: agent responsible for maintaining open-ended conversational interaction.

Responsibilities:

* manage casual dialogue
* maintain conversational continuity
* respond to general questions

---

### Knowledge Agent

Definition: agent responsible for answering factual questions and synthesizing information.

Responsibilities:

* retrieve knowledge sources
* synthesize explanations
* adapt explanation depth

---

### Learning Agent

Definition: agent responsible for tutoring and guided learning.

Responsibilities:

* present educational material
* generate exercises
* evaluate responses
* track learning progress

---

### Calculation Agent

Definition: agent responsible for mathematical reasoning.

Responsibilities:

* perform calculations
* explain steps
* manage units and conversions

---

### Navigation Agent

Definition: agent responsible for route and location reasoning.

Responsibilities:

* compute routes
* estimate travel time
* provide navigation instructions

---

### Multimedia Agent

Definition: agent responsible for media playback and content management.

Responsibilities:

* search media
* manage playlists
* control playback

---

### Smart Home Agent

Definition: agent responsible for home automation.

Responsibilities:

* manage device commands
* interpret device states
* coordinate automation workflows

---

### Productivity Agent

Definition: agent responsible for organizational tasks.

Responsibilities:

* manage reminders
* schedule events
* track tasks

---

### Reading Agent

Definition: agent responsible for document processing and analysis.

Responsibilities:

* retrieve documents
* perform text extraction
* analyze content
* generate summaries

---

### Administration Agent

Definition: agent responsible for system-level administrative tasks.

Responsibilities:

* diagnostics
* configuration management
* system monitoring

---

## Interaction with Other Modules

Specialized Agents interact with multiple architectural subsystems.

### Planner

Receives delegated tasks and objectives.

### Tool Selector

Obtains tools required for domain execution.

### Dialogue and Session System

Maintains conversation context.

### Cognitive Core

Provides operational state information.

### Action and Expression

Executes the final outputs produced by the agent.

---

## Agent Output

After completing its reasoning process, a Specialized Agent may produce several outcomes.

Examples include:

* generated responses
* executed tool operations
* updated contextual state
* stored memory entries
* delegated follow-up steps

These outputs may either be passed directly to the Action and Expression layer or returned to the Planner for further coordination.

---

## Architectural Importance

Specialized Agents enable NORA to support complex reasoning across multiple domains without centralizing all logic in a single module.

Through this subsystem the architecture gains:

* modular domain intelligence
* scalable reasoning capabilities
* easier extension with new domains
* clearer separation between generic reasoning and domain expertise

This structure allows the system to grow into a multi-domain cognitive architecture where each agent contributes expertise within its domain while remaining coordinated by the planning framework.


## Architectural Structure

```
Planning, Interpretation and Agents
│
├── Semantic Interpretation
│ ├── input semantic parsing
│ ├── linguistic structure analysis
│ ├── entity extraction
│ ├── entity normalization
│ ├── entity linking
│ ├── reference resolution
│ ├── discourse interpretation
│ ├── semantic representation construction
│ ├── dialogue act interpretation
│ ├── contextual semantic integration
│ ├── ambiguity detection
│ └── semantic structure output
│
├── Intent Detection
│ ├── user goal identification
│ ├── intent classification
│ ├── multi-intent detection
│ ├── command vs question discrimination
│ ├── conversational request detection
│ ├── intent confidence estimation
│ ├── ambiguous intent detection
│ ├── contextual intent inference
│ ├── intent disambiguation strategies
│ ├── intent-to-capability mapping
│ ├── intent validation
│ └── intent representation output
│
├── Planner
│ ├── goal interpretation
│ ├── plan generation
│ ├── task decomposition
│ ├── multi-step workflow construction
│ ├── dependency resolution
│ ├── sequential task ordering
│ ├── parallel task identification
│ ├── conditional branching logic
│ ├── replanning mechanisms
│ ├── failure recovery planning
│ ├── plan state tracking
│ └── plan execution strategy representation
│
├── Tool Selector
│ ├── capability resolution
│ ├── tool candidate discovery
│ ├── provider selection
│ ├── runtime availability validation
│ ├── permission compatibility validation
│ ├── user preference alignment
│ ├── performance-based selection
│ ├── privacy-aware tool filtering
│ ├── fallback tool preparation
│ ├── multi-tool workflow coordination
│ ├── tool registry integration
│ └── tool resolution output generation
│
└── Specialized Agents
  ├── domain reasoning modules
  ├── domain-specific task decomposition
  ├── domain workflow execution
  ├── internal agent state management
  ├── domain dialogue management
  ├── domain tool orchestration
  ├── adaptive reasoning strategies
  ├── agent invocation management
  ├── agent lifecycle management
  ├── agent coordination with planner
  ├── domain knowledge integration
  └── domain result generation
```

---

## Architectural Layers

The Planning, Interpretation and Agents module is organized as a layered reasoning architecture that transforms raw interpreted input into executable plans and domain-level reasoning processes.

| Layer                         | Responsibility                                                                                                                          |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| Semantic Interpretation Layer | Converts linguistic or multimodal input into structured semantic representations that describe entities, relations and dialogue meaning |
| Intent Recognition Layer      | Identifies the goal or objective expressed by the user and maps the request into actionable intent structures                           |
| Planning Layer                | Constructs execution strategies by decomposing goals into structured workflows composed of ordered tasks                                |
| Capability Resolution Layer   | Determines which concrete tools, integrations or internal modules should execute each planned operation                                 |
| Domain Reasoning Layer        | Delegates complex tasks to specialized agents capable of performing deep reasoning inside specific domains                              |

Together these layers establish the cognitive reasoning pipeline of NORA, enabling the system to transform interpreted inputs into structured plans, resolve the required operational capabilities, and perform domain-aware reasoning before actions are executed in the external world.
