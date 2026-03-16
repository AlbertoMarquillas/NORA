# 5. Dialogue and Session System

## Definition

The Dialogue and Session System is the architectural subsystem that represents and organizes conversational interaction over time within NORA.

This subsystem defines the structural elements that model dialogue as a persistent interaction process between users and the system.

The Dialogue and Session System introduces the following conceptual entities:

* session
* dialogue turn
* conversational context
* conversational project
* dialogue summary
* recovery state

A session represents a bounded interaction period between a user and NORA.

A dialogue turn represents a single conversational contribution produced by either the user or the system.

Conversational context represents the structured information required to interpret and continue the dialogue.

A conversational project represents a persistent objective or topic that spans multiple dialogue sessions.

A dialogue summary represents a compressed representation of previous dialogue content used to preserve continuity.

A recovery state represents the reconstructed conversational context used when a previous session or project is resumed.

Together, these entities define the architectural representation of conversational continuity within the system.

Dialogue interaction is therefore modeled as sequences of dialogue turns grouped into sessions and associated with conversational context and optional persistent projects.

This subsystem defines the structures that allow conversational interaction to persist across time, sessions, and user activities.

# 5.1 Sessions

## Definition

A session is a bounded conversational interaction between a user and NORA.

A session represents the primary temporal structure used to organize dialogue interaction within the Dialogue and Session System.

A session groups the following elements into a single interaction unit:

* dialogue turns
* conversational context
* session metadata
* optional conversational project association

A session begins when an interaction with the system is initiated and ends when the interaction terminates or becomes inactive.

A session therefore represents the temporal container in which conversational interaction occurs.

---

## Core Concepts

The Sessions submodule is defined through several explicit concepts.

### Session

A session is a bounded interaction period between a user and the system.

A session contains the dialogue exchange, context state, and metadata associated with a specific interaction episode.

### Session Identifier

A session identifier is a unique identifier associated with a session.

The identifier allows the system to reference, store, and retrieve session data.

### Session Status

Session status represents the operational state of a session.

Typical session states include:

* active
* suspended
* terminated

### Session Metadata

Session metadata represents descriptive information associated with a session.

Typical metadata elements include:

* session identifier
* associated user identity
* start timestamp
* end timestamp
* interaction channel
* associated conversational project

### Session Boundary

A session boundary represents the beginning or termination point of a session.

Session boundaries define when conversational interaction begins and when it ends.

---

## Session Lifecycle

A session progresses through a structured lifecycle.

### Session Creation

Session creation occurs when a new interaction with the system begins.

Interaction initiation events include:

* wake word detection
* direct user speech input
* graphical interface interaction
* tactile interaction
* remote interface request

During session creation the system generates a new session identifier and initializes session metadata.

### Session Activation

After creation the session becomes the active conversational container for the interaction.

All dialogue turns and context updates are associated with the active session.

### Multi-Turn Interaction

During the active phase the session accumulates dialogue turns and context updates.

Dialogue interaction within a session is represented as an ordered sequence of dialogue turns.

### Session Suspension

A session may enter a suspended state when interaction activity stops temporarily.

Suspension represents a state in which the session remains recoverable but is not currently active.

### Session Termination

A session terminates when the interaction ends.

Termination conditions include:

* explicit user termination
* inactivity timeout
* system shutdown or reset

When terminated the session becomes part of the stored interaction history.

---

## Session Structure

A session contains several structural components.

### Dialogue Turns

Dialogue turns represent the ordered sequence of conversational contributions exchanged between the user and the system.

### Conversational Context

Conversational context represents the semantic and interaction state required to interpret the dialogue within the session.

### Metadata

Metadata describes properties of the interaction session.

Metadata elements include:

* session identifier
* user identity reference
* interaction channel
* timestamps
* associated conversational project

### Session Summary

A session summary represents a compressed representation of the dialogue history associated with a session.

Session summaries allow previous dialogue information to be preserved without maintaining the full dialogue history in active context.

---

## Session Association With Users

A session may be associated with a specific user identity.

User association allows the system to:

* maintain user-specific interaction continuity
* restore previous sessions for a user
* separate interaction histories belonging to different users

If no user identity is available the session is treated as an anonymous session.

---

## Session Inputs

Session-related inputs originate from interaction and perception modules.

Examples include:

* wake word detection events
* speech transcripts
* graphical interface input
* gesture interaction signals
* remote interaction requests

These inputs may initiate or update a session.

---

## Session Outputs

The Sessions submodule produces structured outputs used by other architectural modules.

Outputs include:

* active session context
* session metadata
* session history
* session summary
* session lifecycle events

These outputs are consumed by interpretation, planning, action, and persistence modules.

---

## Interaction With Other Modules

### Dialogue and Context Subsystems

Dialogue turns and conversational context are stored within sessions.

### Cognitive Core

Operational system states occur within the temporal scope of a session.

### Identity, Access and Security

User identity information may be associated with a session.

### Persistence and Memory

Session data may be stored for later retrieval, analysis, or recovery.

---

## Architectural Importance

Sessions define the temporal organization of conversational interaction within NORA.

By grouping dialogue turns, context state, and metadata into bounded interaction units, sessions provide the structural foundation for persistent and recoverable dialogue interaction.

# 5.2 Conversational Projects

## Definition

A conversational project is a persistent conversational structure representing a goal-oriented activity carried out through dialogue interaction with NORA.

A conversational project represents a long-lived objective or collaborative activity that extends across multiple dialogue turns and may extend across multiple sessions.

Conversational projects organize dialogue interaction, project state, resources, and artifacts associated with a specific objective.

A conversational project therefore represents the structural container used to model goal-oriented conversational work.

---

## Core Concepts

The Conversational Projects submodule is defined through several explicit architectural concepts.

### Conversational Project

A conversational project is a persistent entity representing a structured activity performed through dialogue interaction.

A project contains the conversational context, tasks, artifacts, and state associated with a specific goal.

### Project Identifier

A project identifier is a unique identifier assigned to a conversational project.

The identifier allows the system to reference, store, retrieve, and update project data.

### Project Goal

A project goal represents the objective associated with a conversational project.

The goal defines the purpose and direction of the project interaction.

### Project Context

Project context represents structured background information associated with the project.

Project context may include assumptions, scope information, reference material, and relevant domain knowledge.

### Project Tasks

Project tasks represent structured units of work associated with the project goal.

Tasks represent steps or activities required to advance the project.

### Project Artifacts

Project artifacts represent outputs generated during project interaction.

Artifacts may include documents, code files, diagrams, datasets, plans, or other generated materials.

### Project State

Project state represents the current operational condition of a conversational project.

Typical project states include:

* created
* initializing
* active
* in_progress
* waiting_for_input
* paused
* completed
* archived

---

## Project Lifecycle

A conversational project progresses through a structured lifecycle.

### Project Creation

Project creation occurs when a new goal-oriented conversational activity is initiated.

During creation the system generates a project identifier and registers the project entity.

### Project Initialization

Project initialization establishes the initial structure of the project.

Initialization defines the project goal, initial context, and initial tasks.

### Active Project Interaction

During the active phase the project accumulates dialogue interaction, task updates, artifacts, and project state changes.

Dialogue interaction related to the project is associated with the project entity.

### Project Continuation

A project may extend across multiple sessions.

Project continuation occurs when an existing project is resumed during a later interaction session.

### Project Suspension

A project may enter a paused state while preserving its current state and associated information.

### Project Completion

Project completion occurs when the project goal has been achieved or the project is finalized.

### Project Archival

Project archival represents the persistent storage of completed or inactive projects.

Archived projects remain retrievable but are no longer active.

---

## Project Structure

A conversational project contains several structured components.

### Project Goal

The project goal represents the objective pursued through the project interaction.

### Project Context

Project context represents structured information required to understand the project scope and background.

### Task Structure

The task structure represents the set of tasks associated with the project.

Tasks may contain subtasks and status information describing project progress.

### Artifacts

Artifacts represent outputs produced during project interaction.

Artifacts may include documents, code, datasets, diagrams, or generated content.

### Project Notes

Project notes represent recorded observations, decisions, or intermediate reasoning produced during interaction.

### Project Conversation History

Project conversation history represents the subset of dialogue turns associated with the project.

---

## Multi-Project Management

The architecture supports multiple conversational projects.

Each project maintains its own context, state, and associated resources.

The system maintains a project selection mechanism used to determine which project is currently active within a dialogue interaction.

---

## Project Inputs

Inputs affecting conversational projects originate from interaction, planning, and execution subsystems.

Examples include:

* project creation requests
* project selection commands
* task updates
* artifact creation events
* project completion signals

---

## Project Outputs

The Conversational Projects subsystem produces structured outputs used by other architectural components.

Outputs include:

* project creation events
* project context updates
* task structure updates
* artifact references
* project state updates
* project summary information

---

## Interaction With Other Modules

### Dialogue and Session System

Dialogue turns may be associated with a conversational project.

### Planning, Interpretation and Agents

Project goals and tasks influence planning decisions and agent behavior.

### Persistence and Memory

Project data, artifacts, and state are stored for persistence and later retrieval.

### Action and Expression

Actions generated during project execution may produce artifacts or modify project state.

### Frontend and Visualization

Project information may be presented through user interfaces that expose project structure, tasks, and artifacts.

---

## Architectural Importance

Conversational projects define the architectural representation of long-term goal-oriented interaction within NORA.

By organizing dialogue interaction, tasks, context, and artifacts around persistent goals, conversational projects enable structured collaborative workflows that extend across sessions and interaction episodes.

# 5.3 Conversational History

## Definition

Conversational History is the architectural structure that records and organizes dialogue interaction occurring between users and NORA.

Conversational history represents the chronological sequence of dialogue turns produced during interaction.

The subsystem stores dialogue turns together with associated metadata, session references, and optional project references.

Conversational history therefore represents the structural record of conversational interaction.

---

## Core Concepts

The Conversational History subsystem is defined through several explicit architectural concepts.

### Dialogue Turn

A dialogue turn is a single conversational contribution produced by either the user or the system.

Dialogue turns represent the atomic interaction events that form conversational history.

### Turn Identifier

A turn identifier is a unique identifier associated with a dialogue turn.

The identifier allows the system to reference and retrieve individual turns.

### Turn Timestamp

A turn timestamp represents the time at which a dialogue turn occurs.

The timestamp defines the chronological ordering of turns.

### Speaker

Speaker represents the origin of a dialogue turn.

Typical speaker categories include:

* user
* system

### Turn Content

Turn content represents the information expressed in the dialogue turn.

Turn content may include textual messages, structured interaction commands, or system-generated responses.

### Turn Modality

Turn modality represents the interaction channel through which the dialogue turn occurs.

Typical modalities include:

* voice
* text
* gesture
* system_event

### Turn Metadata

Turn metadata represents additional contextual information associated with a dialogue turn.

Metadata may include:

* session identifier
* associated project identifier
* interpreted intent
* recognized entities
* confidence values

---

## Dialogue Turn Structure

A dialogue turn is represented through a structured model.

```
DialogueTurn
 ├── turn_id
 ├── session_id
 ├── project_id (optional)
 ├── speaker
 ├── modality
 ├── content
 ├── timestamp
 ├── interpreted_intent (optional)
 └── metadata
```

This structure allows the system to reconstruct the full sequence of conversational interaction.

---

## Turn Categories

Dialogue turns represent different interaction categories.

### User Turns

User turns represent interaction events generated by a human user.

Examples include:

* spoken input
* textual messages
* gesture-derived interaction events

### System Turns

System turns represent responses or messages generated by NORA.

Examples include:

* generated textual responses
* spoken replies
* clarification prompts

### System Event Turns

System event turns represent internal events that affect conversational interaction.

Examples include:

* planner outputs
* task execution results
* warning messages

---

## History Scope

Conversational history may be organized at several levels.

### Session-Level History

Session-level history contains dialogue turns associated with a specific session.

### Project-Level History

Project-level history contains dialogue turns associated with a conversational project.

### User-Level History

User-level history aggregates dialogue turns associated with a specific user identity.

---

## History Organization

Conversational history is organized as ordered dialogue sequences.

Dialogue turns are ordered according to their timestamps.

The ordering of turns reconstructs the interaction timeline.

Dialogue sequences may be filtered or grouped according to session identifiers, project identifiers, or user identifiers.

---

## History Retrieval

Conversational history supports retrieval operations used by other architectural subsystems.

Typical retrieval operations include:

* retrieval of recent dialogue turns
* retrieval of turns belonging to the active session
* retrieval of turns associated with a conversational project
* retrieval of summarized dialogue segments

---

## Conversation Summaries

Long dialogue histories may be summarized to maintain efficient context usage.

A conversation summary represents a compressed representation of multiple dialogue turns.

Summaries preserve key information while reducing the size of the active dialogue context.

---

## Persistence

Conversational history is stored in the system persistence layer.

Stored records include dialogue turns, associated metadata, and references to sessions or projects.

Persistent storage enables reconstruction of past interactions after system restart or session termination.

---

## Privacy and Security

Conversational history may contain sensitive user information.

Conversation records are therefore subject to privacy and access control mechanisms defined in the Identity, Access and Security module.

---

## Inputs

Conversational history receives dialogue events generated by interaction processing.

Typical inputs include:

* user speech transcripts
* user textual messages
* system responses
* interpreted intents
* session lifecycle events

---

## Outputs

The subsystem produces structured outputs used by other modules.

Outputs include:

* stored dialogue turn records
* retrieved dialogue sequences
* summarized conversation segments
* contextual history used for dialogue interpretation

---

## Interaction With Other Modules

### Sessions

Sessions define the temporal grouping of dialogue turns.

### Conversational Projects

Projects associate dialogue turns with persistent goal-oriented activities.

### Planning, Interpretation and Agents

Dialogue history may be referenced when interpreting user input or generating plans.

### Persistence and Memory

Conversation records are stored and retrieved through the persistence subsystem.

### Frontend and Visualization

User interfaces may display dialogue history to users and allow navigation of previous interactions.

---

## Architectural Importance

Conversational history defines the structural record of dialogue interaction within NORA.

By storing dialogue turns and associated metadata in chronological order, the subsystem enables multi-turn conversational continuity and reconstruction of interaction context.

# 5.4 Conversational Context

## Definition

Conversational Context is the architectural structure that represents the active semantic state of an ongoing dialogue interaction.

Conversational context contains the information required to interpret dialogue turns relative to previous interaction.

The subsystem maintains the set of entities, topics, goals, references, and variables that are currently relevant to the conversation.

Conversational context therefore represents the active semantic frame used during dialogue interpretation and response generation.

---

## Core Concepts

The Conversational Context subsystem is defined through several explicit architectural concepts.

### Context State

Context state represents the current semantic condition of the conversation.

The context state contains the information required to interpret incoming dialogue turns.

### Active Topic

The active topic represents the primary subject currently being discussed.

Topics represent thematic domains or subjects referenced by the dialogue.

### Referenced Entities

Referenced entities represent objects, locations, persons, resources, or concepts mentioned during dialogue interaction.

Entities may contain identifiers and attributes used for reference resolution.

### Conversational Goals

Conversational goals represent objectives currently pursued during the interaction.

Goals may correspond to information requests, problem solving tasks, or project-related activities.

### Context Variables

Context variables represent temporary parameters introduced during dialogue interaction.

Variables may store values referenced by later dialogue turns.

Examples include selected locations, devices, time periods, or documents.

### Unresolved References

Unresolved references represent dialogue elements that require additional information to complete interpretation.

Examples include unanswered system questions or incomplete parameter specifications.

---

## Context Structure

Conversational context is represented through a structured model.

```
ConversationContext
 ├── session_id
 ├── project_id (optional)
 ├── active_topic
 ├── entities
 ├── goals
 ├── variables
 ├── unresolved_references
 ├── context_window
 └── metadata
```

This structure represents the semantic information actively used during dialogue processing.

---

## Context Scope

Conversational context exists within specific interaction scopes.

### Session Context

Session context represents the conversational context associated with a specific session.

Session context is reset or reconstructed when a new session begins.

### Project Context

Project context represents contextual information associated with a conversational project.

Project context may persist across sessions.

---

## Context Window

Conversational context operates within a bounded context window.

The context window contains the subset of information actively considered during dialogue interpretation.

Typical context window elements include:

* recent dialogue turns
* active entities
* current goals
* unresolved references

Information outside the context window remains stored in conversational history and may be retrieved when necessary.

---

## Context Update

Conversational context is updated after each dialogue turn.

Context updates may include:

* addition of newly detected entities
* modification of the active topic
* updates to conversational goals
* updates to context variables
* resolution of unresolved references

Context updates maintain alignment between the context representation and the evolving dialogue.

---

## Context Expiration

Context elements may be removed when they are no longer relevant.

Expiration conditions include:

* topic change
* session termination
* project completion
* explicit context reset

Expiration prevents obsolete context elements from influencing dialogue interpretation.

---

## Inputs

Conversational context receives information from dialogue interaction processing.

Typical inputs include:

* dialogue turns
* interpreted intents
* extracted entities
* system responses
* session lifecycle events

---

## Outputs

The subsystem produces structured outputs used by dialogue interpretation and planning modules.

Outputs include:

* active topic
* resolved references
* active entities
* context variables
* conversational goals

---

## Interaction With Other Modules

### Conversational History

Dialogue history provides the dialogue turns from which contextual information is derived.

### Sessions

Sessions define the temporal scope within which conversational context operates.

### Conversational Projects

Project-specific context information may be incorporated into the conversational context.

### Planning, Interpretation and Agents

Dialogue interpretation and planning subsystems use conversational context to determine meaning and generate actions.

### Persistence and Memory

Context summaries or derived knowledge may be stored in the persistence subsystem.

---

## Architectural Importance

Conversational context defines the active semantic representation used to interpret dialogue within NORA.

By maintaining entities, goals, variables, and references derived from dialogue interaction, the subsystem enables coherent multi-turn dialogue and context-aware response generation.

# 5.5 Summarization and Compression

## Definition

Summarization and Compression is the architectural subsystem responsible for transforming extended conversational histories into compact semantic representations.

The subsystem produces condensed structures that preserve essential information from dialogue interaction while reducing the volume of stored conversational data.

Summarization and compression therefore provide a mechanism for maintaining long-term conversational continuity without requiring the complete dialogue history to remain active in processing pipelines.

---

## Core Concepts

The Summarization and Compression subsystem is defined through several architectural concepts.

### Conversation Summary

A conversation summary is a condensed semantic representation derived from a sequence of dialogue turns.

Summaries represent the essential information extracted from dialogue interaction.

### Compression Unit

A compression unit represents the dialogue segment used as input for summary generation.

Compression units may correspond to dialogue segments such as sessions, topic segments, or project phases.

### Summary Identifier

A summary identifier uniquely identifies a generated summary record.

Identifiers allow summaries to be referenced by other subsystems.

### Summary Scope

Summary scope represents the conversational segment represented by the summary.

Possible scopes include session scope, topic scope, and project scope.

### Summary Metadata

Summary metadata represents contextual information associated with the summary.

Metadata may include creation timestamps, related sessions, associated projects, and references to original dialogue segments.

---

## Summary Structure

Summaries are represented through structured records.

```
ConversationSummary
 ├── summary_id
 ├── scope
 ├── related_session_ids
 ├── related_project_id
 ├── summary_content
 ├── extracted_entities
 ├── extracted_goals
 ├── referenced_artifacts
 ├── creation_timestamp
 └── metadata
```

The structure captures condensed semantic information derived from dialogue history.

---

## Summary Types

Different interaction structures produce different summary types.

### Session Summaries

Session summaries represent the key outcomes of a completed interaction session.

Session summaries typically contain:

* main discussion topics
* questions asked and answered
* decisions made
* tasks performed

### Project Summaries

Project summaries represent the current progress of a conversational project.

Project summaries may contain:

* project goals
* completed tasks
* remaining tasks
* produced artifacts

### Topic Summaries

Topic summaries represent condensed information related to a specific conversational topic segment.

Topic summaries support revisiting previously discussed subjects.

---

## Compression Strategies

Summarization and compression may be implemented using several complementary strategies.

### Semantic Summarization

Semantic summarization extracts important facts and decisions from dialogue interaction.

The resulting summary preserves meaning while reducing verbosity.

### Structural Compression

Structural compression converts dialogue segments into structured representations.

Examples include:

* task lists
* decision logs
* entity collections

### Hierarchical Summarization

Hierarchical summarization produces summaries at multiple abstraction levels.

Typical hierarchy levels include:

* turn level
* session level
* project level

Higher-level summaries represent progressively larger dialogue segments.

---

## Summary Generation Triggers

Summary generation occurs when specific interaction conditions are detected.

Typical triggers include:

* session termination
* dialogue length thresholds
* project milestone completion
* maintenance operations

These triggers ensure that conversational memory remains bounded and manageable.

---

## Summary Storage

Generated summaries are stored in the persistence layer.

Stored summary records include the summary content together with references to the original dialogue segments represented by the summary.

Persistent storage enables summary retrieval across sessions and system restarts.

---

## Context Reconstruction

When conversational context must be reconstructed, the system combines information from several sources.

Context reconstruction may use:

* recent dialogue turns
* conversation summaries
* project context data

This hybrid reconstruction strategy preserves conversational meaning while minimizing processing overhead.

---

## Inputs

The subsystem receives dialogue information produced by conversational interaction processing.

Typical inputs include:

* dialogue turn sequences
* session lifecycle events
* conversational project updates
* conversation length thresholds

---

## Outputs

The subsystem produces structured outputs used by other architectural components.

Outputs include:

* generated conversation summaries
* compressed context representations
* summary metadata
* references to summarized dialogue segments

---

## Interaction With Other Modules

### Conversational History

Dialogue history provides the dialogue segments used for summary generation.

### Conversational Context

Conversational context uses summaries when reconstructing relevant conversational state.

### Conversational Projects

Project summaries describe project progress and outcomes.

### Persistence and Memory

Summary records are stored in the persistence layer and may contribute to long-term memory structures.

### Planning, Interpretation and Agents

Planning and reasoning subsystems may reference summaries when interpreting ongoing tasks or objectives.

---

## Architectural Importance

Summarization and Compression provide the mechanism that maintains bounded conversational memory within the NORA system.

By transforming extended dialogue histories into compact semantic representations, the subsystem enables sustained long-running interactions and efficient conversational context reconstruction.


## Architectural Structure

```
Dialogue and Session System
│
├── Sessions
│ ├── session lifecycle management
│ ├── session creation triggers
│ ├── active interaction boundaries
│ ├── session identifiers
│ ├── session state tracking
│ ├── session activation control
│ ├── session suspension mechanisms
│ ├── session termination events
│ ├── session metadata management
│ ├── user association tracking
│ ├── interaction channel association
│ └── session scope coordination
│
├── Conversational Projects
│ ├── project goal representation
│ ├── project lifecycle management
│ ├── project state tracking
│ ├── project context structures
│ ├── project task management
│ ├── project artifact tracking
│ ├── project progress representation
│ ├── project conversation linkage
│ ├── multi-project coordination
│ ├── project context switching
│ ├── project persistence mechanisms
│ └── long-term collaboration structure
│
├── Conversational History
│ ├── dialogue turn recording
│ ├── chronological interaction storage
│ ├── dialogue turn identifiers
│ ├── dialogue turn timestamps
│ ├── dialogue turn speaker tracking
│ ├── dialogue modality representation
│ ├── dialogue metadata storage
│ ├── session-level history grouping
│ ├── project-level history grouping
│ ├── user-level interaction aggregation
│ ├── dialogue sequence reconstruction
│ └── history retrieval mechanisms
│
├── Conversational Context
│ ├── active conversation state
│ ├── topic tracking
│ ├── entity tracking
│ ├── conversational goal representation
│ ├── dialogue variable storage
│ ├── reference resolution context
│ ├── unresolved question tracking
│ ├── context window management
│ ├── context update mechanisms
│ ├── context expiration mechanisms
│ ├── semantic interaction state
│ └── dialogue interpretation support
│
└── Summarization and Compression
  ├── conversation summary generation
  ├── dialogue segment compression
  ├── summary scope management
  ├── session summary structures
  ├── project summary structures
  ├── topic summary structures
  ├── semantic summarization mechanisms
  ├── structural compression mechanisms
  ├── hierarchical summary structures
  ├── summary generation triggers
  ├── summary metadata tracking
  └── context reconstruction support
```

---

## Architectural Layers

The Dialogue and Session System operates through several complementary layers that structure how conversational interaction is organized, maintained, and evolved across time.

| Layer                                    | Responsibility                                                                                         |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| Interaction Structuring Layer            | Defines interaction boundaries through sessions and organizes dialogue into coherent interaction units |
| Collaborative Activity Layer             | Manages goal-oriented conversational projects that persist across sessions                             |
| Dialogue Recording Layer                 | Stores chronological dialogue interaction through conversational history structures                    |
| Active Context Layer                     | Maintains the semantic state required to interpret ongoing conversation                                |
| Conversational Memory Optimization Layer | Produces compressed summaries that maintain conversational continuity while controlling memory growth  |

Together, these layers establish the dialogue management architecture of NORA, enabling structured conversational interaction, persistent collaborative activities, context-aware dialogue interpretation, and scalable conversational memory management across long-running interactions.
