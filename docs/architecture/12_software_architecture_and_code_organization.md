# 12. Software Architecture and Code Organization

## Definition

The Software Architecture and Code Organization module defines how the NORA system is materially organized as a software project.

While the other architectural documents define what NORA is, what capabilities it contains, and how its major subsystems relate conceptually, this document defines how those architectural decisions are translated into a concrete repository structure, directory hierarchy, code partitioning strategy, naming system, and implementation organization.

This module therefore describes the structural software form of NORA as a maintainable engineering system.

It defines:

* how the repository is divided into major areas
* how architectural modules are mapped into code modules
* how configuration is separated from runtime code
* how documentation is separated from implementation
* how deployment assets are separated from application logic
* how tests are organized relative to the source tree
* how frontend, mobile, firmware, and backend concerns are isolated
* how shared cross-cutting code is controlled
* how scripts, bootstrap logic, and operational tooling are structured
* how naming conventions prevent architectural drift

In architectural terms, this module answers questions such as:

* how should the NORA repository be physically organized?
* where should each class of responsibility live?
* how should code boundaries reflect architectural boundaries?
* how can the project remain scalable as the system grows?
* how can implementation clarity be preserved across a very large codebase?

This is not a minor implementation detail.

In a system as broad as NORA, repository structure is part of the architecture because code organization directly affects maintainability, scalability, comprehension, onboarding, testability, deployment clarity, and the long-term ability to evolve the system without collapsing into structural disorder.

---

## Architectural Purpose

The purpose of this module is to translate the conceptual architecture of NORA into a disciplined software structure.

NORA is not a single-purpose script, a small web application, or a narrow automation tool. It is a large cognitive, multimodal, persistent, embodied, and integration-heavy system. Because of that, implementation structure must be treated as a first-class architectural concern.

Without an explicit code organization model, the project would quickly suffer from:

* blurred domain boundaries
* oversized files with mixed responsibilities
* accidental coupling between unrelated subsystems
* duplicated logic across modules
* unclear ownership of functionality
* poor discoverability of implementation elements
* fragile growth over time
* difficult testing and refactoring
* inconsistent naming and placement of files

By introducing an explicit software architecture and code organization module, NORA gains:

* a stable repository structure
* direct traceability between architecture and code
* strong domain separation
* clearer implementation boundaries
* easier navigation for developers
* easier onboarding for future contributors
* safer long-term scalability
* better alignment between design and implementation
* improved testability and deployment clarity

For that reason, Software Architecture and Code Organization is a foundational implementation-facing architectural module of NORA.

---

## Architectural Principles of Code Organization

The software structure of NORA follows a set of architectural principles.

### 1. Architecture-first organization

The repository is organized so that the source code mirrors the conceptual architecture of the system.

The major software domains correspond to the major architectural modules already defined in the previous documents.

This means the codebase should make the architecture visible.

A developer should be able to inspect the directory tree and understand the major system domains directly from the structure.

### 2. Strong separation of concerns

Each directory, subdirectory, and file should have a narrow and explicit purpose.

The structure should avoid broad undifferentiated containers that accumulate unrelated logic.

A file should do one clearly bounded thing whenever possible.

A subdirectory should represent a coherent responsibility boundary.

### 3. Domain isolation

Each domain module should be able to evolve with minimal accidental coupling to unrelated domains.

For example, perception should not be mixed with dialogue persistence, and backend interface code should not contain physical hardware logic.

This separation protects clarity and allows individual modules to mature independently.

### 4. Explicit cross-cutting control

Shared code should exist only when it is truly transversal.

The shared layer must not become a dumping ground for arbitrary utilities, semi-domain logic, or prematurely generalized abstractions.

Cross-cutting code must remain narrowly scoped and strictly justified.

### 5. File-level granularity

The project favors many small explicit files over a few oversized files containing mixed logic.

This improves readability, discoverability, and refactoring safety.

Examples include:

* one enum per file when practical
* one service per file
* one use case per file
* one repository per file
* one adapter per file
* one policy per file

### 6. Runtime boundary clarity

Code organization must distinguish clearly between:

* source code
* configuration
* scripts
* deployment assets
* documentation
* generated or runtime data
* tests
* firmware
* frontend implementation

This prevents operational confusion and makes the repository more navigable.

### 7. Implementation follows responsibility, not framework convenience

Directories should primarily represent system responsibility rather than only technical framework defaults.

Framework-specific structures may exist, but they should remain subordinate to the architectural model whenever possible.

### 8. Naming as architectural control

File naming conventions are part of the architecture.

Consistent names reduce ambiguity, improve searchability, and preserve structural discipline.

### 9. Scalability by subdivision

As modules grow, they should split into explicit subdomains rather than accumulate complexity in a flat directory.

Growth should increase structure, not reduce it.

### 10. Documentation and implementation alignment

Every major architectural document should have a visible mapping into code organization.

The structure of the repository should make it easy to move from architectural specification to implementation and back again.

---

## Global Repository Structure

The NORA repository is organized as a multi-area software system.

Its top-level structure is the following:

```text
nora/
├── README.md
├── pyproject.toml
├── requirements.txt
├── .env.example
├── .gitignore
├── docs/
├── config/
├── scripts/
├── deployment/
├── data/
├── frontend/
├── mobile/
├── firmware/
├── tests/
└── src/
```

Each top-level element exists for a distinct architectural reason.

---

## Top-Level Repository Elements

### README.md

The README file is the primary entry point into the repository.

It defines the human-facing introduction to the project.

Its purpose is to provide:

* project identity
* system overview
* setup orientation
* execution entry points
* development guidance
* documentation links

The README is not the place for full architectural detail. Its role is repository-level orientation.

### pyproject.toml

The `pyproject.toml` file defines the Python project configuration.

It acts as the canonical project metadata and packaging configuration file when modern Python project conventions are used.

It may define:

* project metadata
* dependency metadata
* build-system configuration
* formatter settings
* linter settings
* test runner settings
* tool-specific Python configuration

Architecturally, this file defines the Python project boundary and standard tooling contract.

### requirements.txt

The `requirements.txt` file defines installable runtime or development dependencies in a simple dependency list format.

Even if `pyproject.toml` exists, this file may still be used for deployment compatibility, reproducible environment setup, or simpler installation workflows.

Its architectural role is dependency declaration for operational environments.

### .env.example

The `.env.example` file defines the example environment-variable surface expected by the system.

It documents the environment-level configuration contract without exposing real secrets.

It provides:

* variable names
* expected configuration categories
* deployment configuration guidance
* safe setup onboarding support

This file is part of secure operational architecture.

### .gitignore

The `.gitignore` file defines which files must not be version-controlled.

It protects the repository from accidental inclusion of:

* secrets
* local virtual environments
* caches
* generated data
* temporary artifacts
* build outputs
* machine-specific files

Architecturally, it helps preserve repository hygiene and reproducibility.

---

## docs/

The `docs/` directory contains the explicit human-readable documentation of the NORA system.

This directory is where architecture, deployment knowledge, API references, hardware notes, diagrams, and design decisions are stored as durable documentation artifacts.

It exists to keep conceptual and operational knowledge distinct from executable code.

### docs/architecture/

The `docs/architecture/` directory contains the formal architectural specification of NORA.

It stores the major system architecture documents that define the system by domain.

This directory is the conceptual backbone of the project.

Each file defines one architectural module.

#### 00_identity_access_security.md

Defines the architectural structure of identities, authentication, authorization, user profiles, and protection mechanisms.

#### 01_interaction_interfaces.md

Defines the human-facing input and interaction channels through which users and operators access NORA.

#### 02_perception_of_the_environment.md

Defines the perceptual architecture that allows NORA to capture and interpret environmental signals.

#### 03_cognitive_core.md

Defines the internal operational cognition of NORA, including state, runtime context, modulation, and internal control memory.

#### 04_dialogue_and_session_system.md

Defines sessions, conversational projects, conversational history, summarization, and recovery structures.

#### 05_planning_interpretation_and_agents.md

Defines semantic interpretation, intent detection, planning, tool selection, and specialized agent coordination.

#### 06_action_and_expression.md

Defines the mechanisms through which NORA emits outputs, performs actions, communicates, and affects the digital or physical environment.

#### 07_backend_and_application.md

Defines backend interfaces, orchestration, application services, event dispatch, realtime transport, and operational backend structure.

#### 08_persistence_and_memory.md

Defines the durable storage architecture of structured records, memory, file artifacts, and technical history.

#### 09_frontend_and_visualization.md

Defines visual interfaces, dashboards, observability surfaces, and human-facing frontend environments.

#### 10_infrastructure_and_hardware.md

Defines the physical substrate of the system, including compute devices, sensors, actuators, connectivity, and controllable external devices.

#### 11_integrations_engines_and_external_services.md

Defines the external engines, providers, platforms, and service integrations used by NORA.

#### 12_software_architecture_and_code_organization.md

Defines how the architecture is realized as a repository, directory tree, naming system, and code organization model.

### docs/diagrams/

The `docs/diagrams/` directory contains visual architectural diagrams.

This includes system maps, sequence flows, deployment diagrams, module relationship diagrams, state models, and other visual representations.

Its purpose is to translate textual architecture into visual understanding.

### docs/api/

The `docs/api/` directory contains API-level documentation.

This may include endpoint references, payload examples, authentication notes, WebSocket contracts, and integration examples.

Its role is interface documentation for developers and clients.

### docs/deployment/

The `docs/deployment/` directory contains deployment documentation.

It may define:

* environment setup
* deployment topologies
* container deployment notes
* runtime dependencies
* service startup order
* infrastructure assumptions

Its role is operational deployment knowledge.

### docs/hardware/

The `docs/hardware/` directory contains hardware-specific documentation.

This may include wiring notes, physical assembly references, pin maps, sensor notes, actuator integration notes, and maintenance documentation.

Its purpose is to document the embodied implementation of the system.

### docs/decisions/

The `docs/decisions/` directory contains architectural decision records or equivalent design justifications.

Its role is to preserve why specific structural choices were made.

This improves traceability and future maintainability.

---

## config/

The `config/` directory contains non-code system configuration.

Its role is to externalize operational settings from implementation logic.

This directory exists so that runtime behavior can be adjusted without rewriting application source files.

### app_settings.yaml

Defines global application configuration such as service behavior, feature toggles, system-wide defaults, and runtime controls.

### logging_settings.yaml

Defines how logging is configured across the system.

This may include log levels, handlers, sinks, formatters, retention rules, and structured logging settings.

### fsm_settings.yaml

Defines configuration for the finite-state machine layer.

This may include state activation parameters, timing thresholds, event handling options, or operational transition constraints.

### permissions_settings.yaml

Defines role, permission, and access-related configuration used by the authorization layer.

### integrations_settings.yaml

Defines connection and behavior settings for external providers, engines, APIs, and service integrations.

### hardware_settings.yaml

Defines hardware-level runtime configuration.

This may include device mappings, bus selection, calibration references, addresses, pins, thresholds, and hardware feature flags.

### frontend_settings.yaml

Defines configuration that affects visual interfaces, frontend backend-support payload behavior, UI defaults, or presentation-level options.

### config/environments/

The `config/environments/` directory contains environment-specific configuration overlays.

This makes it possible to preserve one structural configuration model while adapting values per environment.

#### development.yaml

Defines configuration values intended for local development.

#### testing.yaml

Defines configuration values intended for automated or controlled test environments.

#### staging.yaml

Defines configuration values intended for pre-production validation.

#### production.yaml

Defines configuration values intended for real deployment environments.

### config/prompts/

The `config/prompts/` directory contains structured prompt assets used by prompt-driven reasoning or language subsystems.

This keeps prompt engineering resources externalized and version-controlled.

#### system_prompts/

Contains prompts defining general system-level behavior or role instructions.

#### planner_prompts/

Contains prompts used by planning or decision-construction subsystems.

#### agent_prompts/

Contains prompts specialized for specific domain agents.

#### dialogue_prompts/

Contains prompts used to shape dialogue behavior, recovery, or conversational continuity processes.

---

## scripts/

The `scripts/` directory contains operational entry-point scripts and maintenance utilities.

These are executable repository-level actions used for startup, diagnostics, migrations, seeding, exports, health checks, and support tasks.

This directory exists to make routine system operations explicit, scriptable, and discoverable.

### start_nora_server.py

Starts the main backend application server.

### start_nora_worker.py

Starts background worker processes responsible for asynchronous or queued execution tasks.

### start_nora_scheduler.py

Starts the scheduler process responsible for timed jobs, planned triggers, or recurrent system tasks.

### start_nora_realtime_gateway.py

Starts the realtime transport service responsible for bidirectional or push-based runtime updates.

### run_database_migrations.py

Executes database schema migrations.

### seed_default_roles.py

Seeds initial authorization roles into persistent storage.

### seed_default_permissions.py

Seeds initial permission definitions into persistent storage.

### seed_default_admin.py

Creates or seeds the initial administrative identity required for privileged system access.

### reindex_vector_memory.py

Rebuilds or refreshes vector-based persistent memory indexes.

### rebuild_event_projections.py

Reconstructs read models, projections, or derived event-based views from stored event history.

### rotate_technical_logs.py

Performs maintenance over technical log storage such as archival, pruning, or rotation.

### export_system_configuration.py

Exports configuration state for backup, transfer, audit, or replication purposes.

### import_system_configuration.py

Imports previously exported system configuration into the current environment.

### run_local_diagnostics.py

Runs local health and diagnostics checks over the runtime system.

### run_hardware_connectivity_check.py

Checks connectivity with configured hardware devices, buses, or attached physical nodes.

### run_audio_device_check.py

Verifies the availability and condition of audio input and output devices.

### run_camera_device_check.py

Verifies the availability and condition of camera devices.

### run_end_to_end_smoke_test.py

Runs a minimal system-wide verification workflow intended to confirm that major runtime paths function correctly.

### generate_openapi_spec.py

Generates the OpenAPI description of the exposed HTTP API.

---

## deployment/

The `deployment/` directory contains infrastructure and deployment assets required to run NORA outside the development environment.

Its role is to separate deployment mechanics from application logic.

### deployment/docker/

Contains Dockerfiles or Docker-related build assets.

### deployment/compose/

Contains multi-service container orchestration definitions, typically for local integration or controlled deployment environments.

### deployment/systemd/

Contains service definitions for process supervision in Linux environments using systemd.

### deployment/nginx/

Contains reverse-proxy or ingress configuration used to expose NORA services through web-facing gateways.

### deployment/kubernetes/

Contains deployment manifests for Kubernetes-based orchestration environments.

### deployment/env_templates/

Contains environment configuration templates used as references for deployment setup.

---

## data/

The `data/` directory contains non-source runtime data, local storage, temporary files, exports, caches, and generated artifacts.

It represents the repository-level location for local operational data that should remain structurally distinct from source code.

### data/local/

Contains local runtime state or developer-local persistent data.

### data/cache/

Contains cacheable intermediate data, provider caches, temporary derived results, or fetch acceleration artifacts.

### data/artifacts/

Contains generated system artifacts such as documents, media, visual outputs, exports, reports, or generated deliverables.

### data/uploads/

Contains uploaded user or operator files awaiting processing, storage, or transformation.

### data/exports/

Contains exported system outputs intended for transfer, analysis, backup, or user delivery.

### data/temporary/

Contains short-lived temporary working files that should not be treated as durable assets.

---

## frontend/

The `frontend/` directory contains the standalone frontend implementation of NORA.

This directory is separate from backend support code because the frontend is its own application.

### frontend/nora_web_app/

Contains the web frontend project.

It defines the browser-based visual interface layer of NORA.

#### public/

Contains static public assets served directly by the frontend application.

#### src/

Contains the actual source code of the frontend application.

##### app/

Contains application bootstrap, root composition, and top-level application assembly logic.

##### pages/

Contains page-level route targets representing major navigable screens.

##### widgets/

Contains small reusable UI units.

##### panels/

Contains structured interface panels representing bounded pieces of UI functionality.

##### views/

Contains composed visual views that assemble multiple panels or widgets into coherent visual states.

##### dashboards/

Contains dashboard-oriented interfaces used for monitoring, administration, or operational inspection.

##### hooks/

Contains reusable frontend behavior hooks.

##### services/

Contains frontend-side service code such as API clients, transport wrappers, or state-fetch integrations.

##### stores/

Contains frontend state containers, state management logic, or client-side stores.

##### routes/

Contains explicit route configuration and navigation definitions.

##### types/

Contains TypeScript type definitions used across the frontend application.

##### styles/

Contains global styles, design tokens, layout rules, or styling utilities.

##### assets/

Contains frontend-bundled static assets such as images, icons, or local media.

#### package.json

Defines the Node-based frontend package metadata and dependency graph.

#### tsconfig.json

Defines the TypeScript compiler configuration for the frontend project.

#### vite.config.ts

Defines the Vite build and development server configuration for the frontend application.

---

## mobile/

The `mobile/` directory contains the mobile application implementation of NORA when such an application exists.

This directory is separated from the web frontend because mobile interaction, packaging, runtime constraints, and platform integrations are distinct concerns.

### mobile/nora_mobile_app/

Contains the dedicated mobile application project.

This project may eventually contain its own source tree, assets, mobile platform configuration, build definitions, and mobile-specific interaction logic.

---

## firmware/

The `firmware/` directory contains low-level embedded software projects used by hardware controllers and edge devices in the NORA ecosystem.

This directory exists because firmware is not the same thing as backend code.

Firmware targets constrained physical devices and must be structured independently.

### arduino_controller/

Contains firmware for Arduino-based controllers responsible for deterministic low-level hardware behavior.

### esp32_controller/

Contains firmware for ESP32-based controllers, typically used where WiFi, Bluetooth, or more capable embedded control is required.

### esp8266_controller/

Contains firmware for ESP8266-based network-capable embedded devices.

### raspberry_pi_edge_runtime/

Contains the edge runtime software package or deployment code intended to run directly on Raspberry Pi hardware as part of the embodied system.

---

## tests/

The `tests/` directory contains the complete validation architecture of the repository.

It is separated by test intent rather than only by module.

This directory exists to make quality strategy explicit.

### unit/

Contains isolated tests for narrowly scoped implementation units.

These tests validate individual services, models, policies, adapters, and small domain behaviors.

### integration/

Contains tests validating correct cooperation between components, subsystems, infrastructure pieces, or dependencies.

### contract/

Contains tests validating interface contracts.

These may cover HTTP payload contracts, WebSocket payload contracts, provider compatibility, or boundary expectations.

### e2e/

Contains end-to-end tests validating full operational flows across multiple system layers.

### performance/

Contains tests validating timing, throughput, latency, or scalability properties.

### hardware_in_loop/

Contains tests that run against real hardware or hardware-like physical setups.

This directory is critical for embodied-system verification.

### fixtures/

Contains reusable test data, sample payloads, mock records, and deterministic test resources.

### factories/

Contains test object builders or factory utilities used to generate repeatable test inputs.

### test_bootstrap/

Contains shared test initialization logic, environment setup helpers, and test harness bootstrapping resources.

---

## src/

The `src/` directory contains the primary source code of the NORA software system.

This is the implementation root for the Python application code.

### src/nora/

The `src/nora/` package is the core implementation package of the system.

It is organized according to the architecture-first model.

Each main directory corresponds to a major architectural domain or a cross-cutting implementation area.

---

## src/nora/bootstrap/

The `bootstrap/` module contains the startup composition logic of the system.

Its purpose is to assemble the runtime application from configuration, dependencies, infrastructure bindings, routers, event buses, stores, and lifecycle hooks.

Bootstrap is where the system becomes executable.

It should not contain deep domain logic. Its role is composition.

Typical responsibilities include:

* dependency wiring
* container initialization
* runtime initialization order
* startup orchestration
* shutdown orchestration
* infrastructure binding
* service registration

---

## src/nora/shared/

The `shared/` module contains only truly transversal code used across multiple architectural domains.

Its purpose is to host narrow cross-cutting abstractions that are generic enough to be reused without becoming domain leakage.

This module must remain disciplined.

It is not a miscellaneous storage area.

It may include:

* shared constants
* global enums
* shared identifiers
* generic operation models
* base exceptions
* narrow infrastructure protocols
* generic safety utilities

It must not absorb domain logic that properly belongs to one of the architectural modules.

---

## src/nora/identity_access_security/

The `identity_access_security/` module contains the implementation of identity resolution, authentication, authorization, user profile handling, and security control.

It is the software realization of the Identity, Access and Security architectural module.

Its role is to determine:

* who the actor is
* whether they are authenticated
* what they are allowed to do
* how their profile affects personalization
* how security events and protective responses are handled

---

## src/nora/interaction_interfaces/

The `interaction_interfaces/` module contains the implementation of the channels through which users and operators interact with NORA.

It transforms channel-specific inputs into normalized interaction events.

This includes voice, screen, web, touch, gesture, NFC, and remote interaction forms.

Its role is channel normalization rather than deep semantic reasoning.

---

## src/nora/perception/

The `perception/` module contains the implementation of environmental signal acquisition, preprocessing, feature extraction, interpretation, fusion, and perception event production.

It is responsible for transforming raw physical or device-level inputs into structured perceptual outputs usable by the rest of the system.

---

## src/nora/cognitive_core/

The `cognitive_core/` module contains the implementation of the internal operational cognition of NORA.

It includes finite-state control, operational context management, modulation state, and internal short-term control memory.

Its role is to maintain the active internal runtime condition of the system.

---

## src/nora/dialogue_and_session/

The `dialogue_and_session/` module contains the implementation of sessions, conversational projects, dialogue history, summarization, compression, and recovery structures.

It is responsible for preserving temporal continuity in user-system interaction.

---

## src/nora/planning_and_agents/

The `planning_and_agents/` module contains semantic interpretation support, intent detection, planning logic, tool selection, execution preparation, and specialized agent routing.

Its role is to determine what the system should do in response to interpreted input and contextual goals.

---

## src/nora/action_and_expression/

The `action_and_expression/` module contains the implementation of system outputs and execution effects.

It includes voice output, screen output, multimedia, emotional expression, device control, movement, communication, and other output behaviors.

Its role is to transform internal decisions into observable results.

---

## src/nora/persistence_and_memory/

The `persistence_and_memory/` module contains the implementation of durable storage.

It includes structured databases, persistent memory, vector memory support, file artifact storage, and technical history retention.

Its role is to make continuity and recoverability possible across runtime boundaries.

---

## src/nora/backend_and_application/

The `backend_and_application/` module contains the exposed application interfaces and runtime coordination layers of the backend.

It includes HTTP APIs, WebSocket realtime behavior, application use cases, coordinators, event dispatch, and backend-side observability.

Its role is to expose, coordinate, and operate system behavior as an application platform.

---

## src/nora/frontend_support/

The `frontend_support/` module contains backend-side structures specifically dedicated to helping frontend applications consume system state cleanly.

It includes view-model builders, presenters, and serializers.

This is not the frontend itself.

Its role is representation shaping for UI consumption.

---

## src/nora/integrations_and_external_services/

The `integrations_and_external_services/` module contains adapters, providers, and abstractions for external engines and platforms.

It includes linguistic engines, language models, vision engines, search providers, multimedia services, productivity integrations, IoT platforms, and embedding services.

Its role is external capability access through stable internal interfaces.

---

## src/nora/infrastructure_and_hardware/

The `infrastructure_and_hardware/` module contains the software-side representation of the embodied substrate of NORA.

It includes computation nodes, sensors, actuators, connectivity structures, external controllable devices, and runtime hardware state.

Its role is to model and coordinate the physical system boundary from the software side.

---

## src/nora/observability/

The `observability/` module contains centralized instrumentation structures.

It includes logging, tracing, metrics, and dashboard payload generation.

Its role is to make the runtime system visible, diagnosable, measurable, and operable.

---

## Architectural Mapping Rule

A critical organizational rule of NORA is the following:

Conceptual architectural module -> implementation module.

This means that the software tree should preserve visible alignment with the architecture documents.

The codebase should not drift into arbitrary framework-driven sprawl.

A developer should be able to move from:

* architecture document
* to module name
* to submodule directory
* to file implementing a specific responsibility

with minimal ambiguity.

---

## Internal Code Organization Style

Within domain modules, internal structure should follow bounded technical roles.

Typical subdirectories may include:

* enums
* models
* services
* repositories
* providers
* adapters
* policies
* handlers
* events
* queries
* dispatch
* routing
* registries
* mappers
* unit_of_work
* pipeline
* preprocessing
* feature_extraction
* interpretation

These are not interchangeable labels.

Each one should correspond to a clear implementation role.

### enums

Contains finite controlled sets of named values.

### models

Contains domain objects, state objects, payload objects, or structural representations.

### services

n
Contains single-purpose business or transformation operations.

### repositories

Contains storage access abstractions or concrete persistence implementations.

### providers

Contains capability interfaces or access layers over internal or external engines.

### adapters

Contains concrete translation layers binding provider abstractions to specific external technologies.

### policies

Contains explicit rule sets, evaluation constraints, or decision criteria.

### handlers

Contains input-triggered bounded operation handlers.

### events

Contains event object definitions emitted within the system.

### queries

Contains read-oriented operations that retrieve domain data.

### dispatch

n
Contains event or action dispatch coordination logic.

### routing

Contains routing logic that directs outputs or events toward internal targets.

### registries

Contains static or dynamic registration structures such as mappings, states, tools, or transitions.

### mappers

Contains transformation logic between persistence representations and domain representations.

### unit_of_work

Contains transactional boundary implementations coordinating multiple repository changes.

### pipeline

Contains explicit ordered processing workflows.

### preprocessing

Contains normalization or preparatory transformation steps applied before interpretation.

### feature_extraction

Contains operations that derive structured features from raw signals.

### interpretation

Contains operations that convert extracted or normalized data into semantic or operational meaning.

---

## Naming Conventions

Naming conventions act as architectural constraints in NORA.

The recommended rules are the following.

### Enums

Use the suffix `_enum.py`.

Example:

* `role_enum.py`
* `language_enum.py`

### Models

Use the direct object name.

Example:

* `dialogue_turn.py`
* `user_profile.py`
* `hardware_fault_record.py`

### Services

Use `verb + object + _service.py`.

Example:

* `create_session_service.py`
* `resolve_identity_service.py`
* `capture_image_service.py`

### Use cases

Use `verb + objective + _use_case.py`.

Example:

* `login_use_case.py`
* `archive_project_use_case.py`

### Repositories

Use the suffix `_repository.py`.

Example:

* `session_repository.py`
* `sql_user_repository.py`

### Providers

Use the suffix `_provider.py`.

Example:

* `email_provider.py`
* `ocr_provider.py`

### Adapters

Use the suffix `_adapter.py`.

Example:

* `gmail_adapter.py`
* `spacy_nlp_adapter.py`

### Policies

Use the suffix `_policy.py`.

Example:

* `planning_safety_policy.py`
* `least_privilege_policy.py`

### Handlers

Use either `handle_*.py` or `*_handler.py`, but stay consistent inside a given submodule.

### Builders

Use `build_*` or `*_builder` naming when the file exists specifically to construct objects or payloads.

### Avoided names

The following names should generally be avoided because they collapse architectural clarity:

* `utils.py`
* `helpers.py`
* `services.py`
* `models.py`
* `common.py`
* `manager.py`

These names are too broad and tend to absorb unrelated functionality.

If a file of this kind exists, its scope must be extremely narrow and unambiguous.

---

## Repository Boundaries That Must Remain Explicit

Several boundaries are especially important in NORA.

### Documentation vs implementation

Conceptual explanation belongs in `docs/`.

Executable behavior belongs in `src/`, `frontend/`, `mobile/`, or `firmware/` depending on platform.

### Source code vs configuration

Behavioral settings belong in `config/`.

Implementation logic belongs in source modules.

### Application logic vs operational tooling

Entry-point and maintenance scripts belong in `scripts/`.

Core runtime logic belongs in `src/`.

### Backend vs frontend

Backend application logic belongs in `src/nora/`.

Browser-based interface implementation belongs in `frontend/`.

### Software vs firmware

Python application code belongs in `src/`.

Device-level embedded logic belongs in `firmware/`.

### Durable assets vs source-controlled artifacts

Runtime outputs belong in `data/` or dedicated artifact storage.

They should not contaminate the source tree.

### Domain logic vs shared transversal code

Only truly generic code belongs in `shared/`.

Anything domain-specific belongs in its own domain module.

---

## Why This Structure Fits NORA

This structure is appropriate for NORA because the system is:

* multimodal
* multi-interface
* multi-runtime
* persistent
* integration-heavy
* hardware-aware
* frontend-backed
* backend-driven
* agent-capable
* expected to grow over time

A flatter or less disciplined repository would not preserve clarity under that level of complexity.

The proposed structure allows NORA to evolve as:

* a software platform
* a cognitive system
* a hardware-connected system
* a frontend product
* an integration hub
* a testable engineering project

without sacrificing architectural readability.

---

## Architectural Importance

The Software Architecture and Code Organization module provides the implementation structure that allows the rest of the NORA architecture to remain coherent as a real codebase.

While other architectural modules define identity, interaction, perception, cognition, dialogue, planning, action, persistence, frontend behavior, integrations, and hardware structure, those modules still require a disciplined repository organization in order to be implemented safely and maintained over time.

Through this module the architecture gains:

* traceable mapping from architecture to code
* explicit repository boundaries
* clearer ownership of responsibilities
* scalable subdivision of large domains
* stronger maintainability under growth
* better onboarding and discoverability
* cleaner testing and deployment separation
* reduced accidental coupling
* structural support for long-term evolution

By organizing the repository around explicit architectural domains, bounded technical roles, and strict naming conventions, NORA preserves conceptual clarity not only in documentation but also in implementation.

For that reason, Software Architecture and Code Organization is a necessary architectural module for turning NORA from a conceptual system design into a sustainable engineering system.

## Architectural Structure

```text
Software Architecture and Code Organization
│
├── Repository Root
│   ├── project metadata files
│   ├── dependency definition files
│   ├── environment templates
│   └── repository hygiene files
│
├── Documentation Layer
│   ├── architecture documents
│   ├── diagrams
│   ├── API documentation
│   ├── deployment documentation
│   ├── hardware documentation
│   └── decision records
│
├── Configuration Layer
│   ├── application settings
│   ├── logging settings
│   ├── FSM settings
│   ├── permission settings
│   ├── integration settings
│   ├── hardware settings
│   ├── frontend settings
│   ├── environment overlays
│   └── prompt assets
│
├── Operational Tooling Layer
│   ├── startup scripts
│   ├── migration scripts
│   ├── seed scripts
│   ├── maintenance scripts
│   ├── diagnostics scripts
│   └── export and import scripts
│
├── Deployment Layer
│   ├── Docker assets
│   ├── compose assets
│   ├── systemd service assets
│   ├── reverse proxy assets
│   ├── Kubernetes assets
│   └── deployment environment templates
│
├── Runtime Data Layer
│   ├── local state
│   ├── cache
│   ├── generated artifacts
│   ├── uploads
│   ├── exports
│   └── temporary files
│
├── Client Application Layer
│   ├── web frontend project
│   └── mobile application project
│
├── Firmware Layer
│   ├── Arduino firmware
│   ├── ESP32 firmware
│   ├── ESP8266 firmware
│   └── Raspberry Pi edge runtime
│
├── Validation Layer
│   ├── unit tests
│   ├── integration tests
│   ├── contract tests
│   ├── end-to-end tests
│   ├── performance tests
│   ├── hardware-in-loop tests
│   ├── fixtures
│   ├── factories
│   └── test bootstrap
│
└── Source Implementation Layer
    └── nora
        ├── bootstrap
        ├── shared
        ├── identity_access_security
        ├── interaction_interfaces
        ├── perception
        ├── cognitive_core
        ├── dialogue_and_session
        ├── planning_and_agents
        ├── action_and_expression
        ├── persistence_and_memory
        ├── backend_and_application
        ├── frontend_support
        ├── integrations_and_external_services
        ├── infrastructure_and_hardware
        └── observability
```


```
nora/
│
├── README.md
├── pyproject.toml
├── requirements.txt
├── .env.example
├── .gitignore
│
├── docs/
│   ├── architecture/
│   │   ├── 00_identity_access_security.md
│   │   ├── 01_interaction_interfaces.md
│   │   ├── 02_perception_of_the_environment.md
│   │   ├── 03_cognitive_core.md
│   │   ├── 04_dialogue_and_session_system.md
│   │   ├── 05_planning_interpretation_and_agents.md
│   │   ├── 06_action_and_expression.md
│   │   ├── 07_backend_and_application.md
│   │   ├── 08_persistence_and_memory.md
│   │   ├── 09_frontend_and_visualization.md
│   │   ├── 10_infrastructure_and_hardware.md
│   │   ├── 11_integrations_engines_and_external_services.md
│   │   └── 12_software_architecture_and_code_organization.md
│   │
│   ├── diagrams/
│   ├── api/
│   ├── deployment/
│   ├── hardware/
│   └── decisions/
│
├── config/
│   ├── app_settings.yaml
│   ├── logging_settings.yaml
│   ├── fsm_settings.yaml
│   ├── permissions_settings.yaml
│   ├── integrations_settings.yaml
│   ├── hardware_settings.yaml
│   ├── frontend_settings.yaml
│   ├── environments/
│   │   ├── development.yaml
│   │   ├── testing.yaml
│   │   ├── staging.yaml
│   │   └── production.yaml
│   └── prompts/
│       ├── system_prompts/
│       ├── planner_prompts/
│       ├── agent_prompts/
│       └── dialogue_prompts/
│
├── scripts/
│   ├── start_nora_server.py
│   ├── start_nora_worker.py
│   ├── start_nora_scheduler.py
│   ├── start_nora_realtime_gateway.py
│   ├── run_database_migrations.py
│   ├── seed_default_roles.py
│   ├── seed_default_permissions.py
│   ├── seed_default_admin.py
│   ├── reindex_vector_memory.py
│   ├── rebuild_event_projections.py
│   ├── rotate_technical_logs.py
│   ├── export_system_configuration.py
│   ├── import_system_configuration.py
│   ├── run_local_diagnostics.py
│   ├── run_hardware_connectivity_check.py
│   ├── run_audio_device_check.py
│   ├── run_camera_device_check.py
│   ├── run_end_to_end_smoke_test.py
│   └── generate_openapi_spec.py
│
├── deployment/
│   ├── docker/
│   ├── compose/
│   ├── systemd/
│   ├── nginx/
│   ├── kubernetes/
│   └── env_templates/
│
├── data/
│   ├── local/
│   ├── cache/
│   ├── artifacts/
│   ├── uploads/
│   ├── exports/
│   └── temporary/
│
├── frontend/
│   └── nora_web_app/
│       ├── public/
│       ├── src/
│       │   ├── app/
│       │   ├── pages/
│       │   ├── widgets/
│       │   ├── panels/
│       │   ├── views/
│       │   ├── dashboards/
│       │   ├── hooks/
│       │   ├── services/
│       │   ├── stores/
│       │   ├── routes/
│       │   ├── types/
│       │   ├── styles/
│       │   └── assets/
│       ├── package.json
│       ├── tsconfig.json
│       └── vite.config.ts
│
├── mobile/
│   └── nora_mobile_app/
│
├── firmware/
│   ├── arduino_controller/
│   ├── esp32_controller/
│   ├── esp8266_controller/
│   └── raspberry_pi_edge_runtime/
│
├── tests/
│   ├── unit/
│   ├── integration/
│   ├── contract/
│   ├── e2e/
│   ├── performance/
│   ├── hardware_in_loop/
│   ├── fixtures/
│   ├── factories/
│   └── test_bootstrap/
│
└── src/
    └── nora/
        ├── bootstrap/
        ├── shared/
        ├── identity_access_security/
        ├── interaction_interfaces/
        ├── perception/
        ├── cognitive_core/
        ├── dialogue_and_session/
        ├── planning_and_agents/
        ├── action_and_expression/
        ├── persistence_and_memory/
        ├── backend_and_application/
        ├── frontend_support/
        ├── integrations_and_external_services/
        ├── infrastructure_and_hardware/
        └── observability/
```

# Bootstrap Module

## Definition

The `bootstrap/` module defines how the NORA system is assembled into a runnable application.

While the architectural domain modules define identities, interaction, perception, cognition, dialogue, planning, action, persistence, integrations, hardware, and observability, those modules do not become an operational system by themselves.

A separate composition layer is required to load configuration, initialize infrastructure, connect dependencies, register interfaces, prepare runtime services, and control application startup and shutdown.

That is the role of the bootstrap module.

In architectural terms, the bootstrap module is the assembly layer of NORA.

It is responsible for translating a static codebase into a live runtime system.

This module therefore defines:

* how the runtime environment is loaded
* how settings are read and resolved
* how dependencies are registered and exposed
* how infrastructure services are initialized
* how routers and realtime interfaces are attached
* how startup order is controlled
* how shutdown order is controlled
* how runtime metadata is exposed to the rest of the system

The bootstrap module is not a domain module.

It does not own business rules for perception, dialogue, planning, memory, or hardware behavior.

Its purpose is composition, initialization, orchestration of startup, and safe system teardown.

---

## Architectural Purpose

The purpose of the bootstrap module is to guarantee that NORA starts in a controlled, explicit, reproducible, and inspectable way.

Large systems do not become stable merely by having good domain separation. They also need a disciplined initialization architecture.

Without a dedicated bootstrap layer, system startup tends to become scattered across random files, hidden side effects, import-time initialization, framework callbacks, or implicit global state. That quickly causes:

* unclear startup order
* brittle runtime dependencies
* duplicated initialization logic
* hidden configuration loading
* inconsistent environment handling
* fragile shutdown behavior
* difficult testing
* harder local development
* poor deployment reliability

By introducing a dedicated bootstrap module, NORA gains:

* explicit runtime assembly
* deterministic initialization order
* clearer dependency boundaries
* environment-aware startup behavior
* easier testing through controlled composition
* safer shutdown handling
* simpler deployment entry points
* improved maintainability of the runtime lifecycle

For that reason, the bootstrap module is a foundational technical module of `src/nora/`.

---

## Architectural Role Within `src/nora/`

Within the internal source tree, `bootstrap/` is the module that sits at the boundary between static implementation and active runtime.

It is the place where:

* configuration becomes loaded state
* providers become initialized integrations
* repositories become usable persistence connections
* routers become attached API surfaces
* event systems become active message channels
* schedulers become running time-based services
* hardware bindings become available runtime interfaces
* the application becomes ready to receive work

Because of that, bootstrap must remain highly disciplined.

It should not become:

* a second backend module
* a hidden service locator for domain logic
* a miscellaneous utilities area
* a place for business rules
* a dumping ground for operational hacks

Its job is to compose the system, not to contain the system.

---

## Internal Structure

The proposed structure is the following:

```text
bootstrap/
├── application_container.py
├── dependency_registry.py
├── environment_loader.py
├── settings_loader.py
├── logger_bootstrap.py
├── database_bootstrap.py
├── vector_store_bootstrap.py
├── event_bus_bootstrap.py
├── scheduler_bootstrap.py
├── hardware_bootstrap.py
├── integrations_bootstrap.py
├── router_bootstrap.py
├── websocket_bootstrap.py
├── lifecycle_startup.py
├── lifecycle_shutdown.py
└── runtime_metadata_provider.py
```

This structure divides bootstrap responsibilities into small explicit files, each with a narrow purpose.

That design matches the broader NORA principle of preferring many small files with bounded responsibilities instead of fewer oversized files with mixed behavior.

---

## File-by-File Architectural Definition

### application_container.py

The `application_container.py` file defines the main application container used to hold the assembled runtime dependencies of NORA.

Its role is to act as the structured object through which initialized components can be stored, accessed, and passed across startup boundaries.

This container may include references such as:

* loaded settings
* logger instances
* database clients
* vector store clients
* event bus instances
* scheduler instances
* hardware gateways
* integration adapters
* router registries
* websocket managers
* runtime metadata

Architecturally, this file defines the assembled runtime object graph boundary.

It should not contain business logic. It should define how initialized components are grouped and exposed.

Typical responsibilities include:

* defining the top-level container object
* attaching initialized dependencies
* exposing typed access to runtime resources
* supporting application-wide composition clarity

This file is the central structural holder of initialized runtime state.

### dependency_registry.py

The `dependency_registry.py` file defines how application dependencies are registered, looked up, and exposed during bootstrap.

Its purpose is to provide an explicit dependency registration mechanism instead of relying on hidden globals or uncontrolled import-time state.

Architecturally, this file defines the dependency binding layer of bootstrap.

It may be used to register:

* infrastructure clients
* repositories
* providers
* service factories
* configuration objects
* runtime state providers
* coordinator instances

Its responsibilities may include:

* dependency registration
* dependency lookup
* scoped dependency access
* collision prevention for dependency keys
* startup-time dependency wiring support

This file should not become a general-purpose global service locator used arbitrarily throughout the codebase. Its use should remain controlled and primarily tied to startup composition or framework integration boundaries.

### environment_loader.py

The `environment_loader.py` file defines how environment-level variables are loaded into the application startup process.

Its purpose is to translate process environment state into structured runtime input.

This may include:

* reading environment variables
* loading `.env` files where appropriate
* validating required environment presence
* normalizing environment values
* exposing resolved environment context

Architecturally, this file defines the boundary between the operating environment and the NORA runtime.

It is responsible for bringing deployment-provided configuration into the system safely and explicitly.

Typical responsibilities include:

* environment variable loading
* environment validation
* default handling where allowed
* resolution of active deployment mode

This file should not contain high-level application settings parsing beyond the environment layer itself.

### settings_loader.py

The `settings_loader.py` file defines how configuration files and environment-derived overrides are combined into runtime settings objects.

Its role is to resolve the effective configuration of the system.

This may include combining:

* base application configuration
* environment-specific overlays
* local runtime overrides
* secret-backed values
* feature flags
* integration settings
* hardware settings
* frontend support settings

Architecturally, this file defines the configuration resolution layer of bootstrap.

Its responsibilities may include:

* reading YAML configuration files
* merging multiple configuration sources
* validating configuration structure
* constructing typed settings objects
* exposing effective runtime settings

This file is critical because configuration resolution affects nearly every major subsystem.

### logger_bootstrap.py

The `logger_bootstrap.py` file defines how logging is initialized for the runtime system.

Its purpose is to ensure that structured logging becomes available early in startup and remains consistent across modules.

This may include:

* loading logging configuration
* initializing logger instances
* setting formatter behavior
* attaching output sinks
* configuring log levels
* preparing structured metadata support

Architecturally, this file defines the initialization of runtime observability at the logging layer.

It is important that logging become available early enough to record startup failures, configuration issues, and dependency initialization status.

### database_bootstrap.py

The `database_bootstrap.py` file defines how transactional database infrastructure is initialized.

Its purpose is to prepare the durable structured persistence layer required by many parts of NORA.

This may include:

* database engine creation
* session factory creation
* connection validation
* migration readiness checks
* repository binding support
* database health verification

Architecturally, this file defines the startup boundary of the transactional database subsystem.

It should initialize persistence access, but not implement repository business behavior.

### vector_store_bootstrap.py

The `vector_store_bootstrap.py` file defines how vector memory infrastructure is initialized.

Its role is to prepare semantic retrieval storage used by persistent memory or advanced retrieval subsystems.

This may include:

* opening vector index connections
* validating vector collection availability
* preparing embedding-backed retrieval resources
* checking similarity-search readiness
* exposing vector clients to dependent modules

Architecturally, this file defines the runtime activation of vectorized memory infrastructure.

Because semantic memory may be optional or deployment-dependent, this file may also participate in capability gating and startup diagnostics.

### event_bus_bootstrap.py

The `event_bus_bootstrap.py` file defines how the internal event distribution mechanism is initialized.

Its purpose is to prepare the messaging backbone used for decoupled communication between internal modules.

This may include:

* event bus construction
* publisher and subscriber registration
* topic mapping initialization
* event transport selection
* event middleware attachment
* diagnostics for event routing readiness

Architecturally, this file defines the activation of NORA's internal event flow substrate.

It is important because many coordinated behaviors in NORA depend on events instead of direct coupling.

### scheduler_bootstrap.py

The `scheduler_bootstrap.py` file defines how time-based execution infrastructure is initialized.

Its role is to prepare recurring jobs, deferred tasks, timed triggers, or maintenance workflows.

This may include:

* scheduler engine creation
* job registry loading
* recurring job binding
* interval or cron registration
* scheduler lifecycle setup
* startup scheduling policies

Architecturally, this file defines the temporal execution layer of runtime initialization.

It should remain focused on scheduler assembly rather than on the business semantics of scheduled jobs.

### hardware_bootstrap.py

The `hardware_bootstrap.py` file defines how hardware-facing runtime components are initialized.

Its purpose is to activate the software bindings required for sensors, actuators, buses, and device interfaces.

This may include:

* loading hardware configuration
* binding sensor providers
* binding actuator providers
* initializing serial, GPIO, I2C, SPI, or network hardware connections
* checking device reachability
* exposing hardware access objects to the application container

Architecturally, this file defines the startup bridge between software runtime and embodied hardware infrastructure.

Because hardware availability may vary across environments, this file may also support degraded startup or optional hardware capability activation.

### integrations_bootstrap.py

The `integrations_bootstrap.py` file defines how external engines and service integrations are initialized.

Its role is to prepare the system's access to external providers such as:

* language engines
* LLM services
* OCR engines
* search APIs
* productivity platforms
* IoT platforms
* multimedia services
* embedding providers

Architecturally, this file defines the activation of external capability bindings.

This may include:

* credential-aware provider initialization
* adapter construction
* connection readiness checks
* capability registration
* optional integration enabling or disabling

This file is important because NORA depends on multiple external systems that may not all be available in every deployment mode.

### router_bootstrap.py

The `router_bootstrap.py` file defines how the HTTP API surface is attached to the backend application.

Its purpose is to compose route modules into the running server.

This may include:

* router import and aggregation
* API prefix application
* versioning attachment
* dependency injection wiring for route boundaries
* route-specific middleware attachment
* administrative route gating

Architecturally, this file defines the activation of the HTTP interface boundary of the system.

It should remain focused on route composition and not contain the route logic itself.

### websocket_bootstrap.py

The `websocket_bootstrap.py` file defines how realtime bidirectional communication infrastructure is initialized.

Its purpose is to attach WebSocket or equivalent realtime channels to the application runtime.

This may include:

* websocket manager initialization
* realtime gateway setup
* subscription channel registration
* broadcast binding
* connection lifecycle setup
* authentication linkage for websocket contexts

Architecturally, this file defines the activation of the realtime interaction surface of NORA.

### lifecycle_startup.py

The `lifecycle_startup.py` file defines the ordered startup lifecycle of the application.

Its role is to coordinate the sequence in which bootstrap steps occur.

This file is one of the most important pieces of the module because startup order is itself an architectural concern.

Typical responsibilities include:

* defining startup phases
* sequencing environment loading before settings resolution
* ensuring logging exists early enough
* starting persistence before dependent services
* attaching interfaces only after dependencies are ready
* running startup checks
* marking the runtime as ready

Architecturally, this file defines the controlled initialization procedure of the whole system.

It may also define startup failure handling and partial-startup rollback behavior.

### lifecycle_shutdown.py

The `lifecycle_shutdown.py` file defines the ordered shutdown lifecycle of the application.

Its purpose is to ensure that NORA stops safely and predictably.

This may include:

* halting new ingress
* draining queues
* stopping realtime services
* stopping scheduled jobs
* flushing logs
* closing database connections
* releasing hardware resources
* closing provider clients
* persisting final runtime state when needed

Architecturally, this file defines the safe teardown path of the system.

In complex systems, shutdown is just as important as startup because uncontrolled teardown can corrupt state, lose data, or leave hardware in unsafe conditions.

### runtime_metadata_provider.py

The `runtime_metadata_provider.py` file defines how runtime metadata is constructed and exposed.

Its purpose is to make deployment and execution context available to the rest of the system in a structured way.

This metadata may include:

* application version
* build identifier
* environment name
* process start time
* host identity
* active deployment profile
* enabled capability flags
* startup mode information

Architecturally, this file defines the runtime self-description layer of bootstrap.

This information is useful for diagnostics, health reporting, observability, frontend support, and administrative interfaces.

---

## Startup Logic Separation Principle

A key design principle of the bootstrap module is that each startup concern should be isolated into its own file.

This means that bootstrap must not collapse into one large `startup.py` file doing everything.

Instead, the structure should preserve clear startup categories:

* environment loading
* settings resolution
* logging initialization
* persistence initialization
* vector infrastructure initialization
* event backbone initialization
* scheduler initialization
* hardware initialization
* integration initialization
* router initialization
* realtime initialization
* startup sequencing
* shutdown sequencing

This separation provides:

* easier testing
* easier replacement of infrastructure pieces
* easier debugging of startup failures
* safer lifecycle changes over time
* clearer onboarding for developers

---

## What Bootstrap Must Not Contain

To preserve architectural clarity, the bootstrap module should avoid absorbing responsibilities that belong elsewhere.

It should not contain:

* domain business logic
* route handler logic
* repository logic
* planner behavior
* perception pipelines
* action execution rules
* dialogue semantics
* long-term runtime state unrelated to startup composition
* miscellaneous cross-domain helper code

Bootstrap may call those systems, register them, initialize them, or wire them together, but it should not become the place where those behaviors are implemented.

---

## Interaction With Other Modules

The bootstrap module interacts with almost every other major module because it assembles the whole runtime.

### shared

Uses transversal types, exceptions, protocols, identifiers, and utility elements during initialization.

### persistence_and_memory

Initializes database and vector-store infrastructure and exposes storage-related runtime dependencies.

### backend_and_application

Attaches routers, realtime gateways, application boundaries, and operational transport surfaces.

### integrations_and_external_services

Builds and registers adapters and provider clients for external engines and platforms.

### infrastructure_and_hardware

Initializes the hardware-facing side of the system and binds available physical interfaces.

### observability

Activates logging and may help activate trace and metric export infrastructure.

### all domain modules

Provides initialized dependencies, configuration, and runtime context required for them to function.

---

## Testing Implications

The bootstrap module has strong testing importance even though it is not domain logic.

It should support testing such as:

* configuration resolution tests
* environment loading tests
* dependency registration tests
* startup ordering tests
* degraded startup tests
* missing dependency failure tests
* safe shutdown tests
* optional capability enablement tests

Because bootstrap is the assembly layer, errors here can make the entire system fail even when domain logic is correct.

---

## Why This Structure Fits NORA

This bootstrap structure fits NORA because NORA is not a minimal single-process application.

It includes:

* multiple infrastructure dependencies
* persistent storage systems
* realtime communication
* optional hardware
* multiple external integrations
* event-driven coordination
* scheduled behavior
* frontend-facing interfaces
* environment-dependent capabilities

A simple or implicit startup model would become fragile very quickly under that level of system breadth.

The proposed structure allows startup behavior to remain explicit, inspectable, replaceable, and scalable.

---

## Architectural Importance

The bootstrap module provides the composition and lifecycle foundation through which the NORA system becomes an active runtime.

While other modules define perception, cognition, dialogue, planning, action, persistence, backend behavior, integrations, hardware, and observability, those modules require a dedicated assembly layer in order to be initialized in a safe and coherent way.

Through this module the architecture gains:

* explicit runtime composition
* deterministic startup order
* controlled shutdown order
* clearer dependency wiring
* safer infrastructure initialization
* environment-aware activation of capabilities
* easier diagnostics of startup failures
* better support for deployment and testing

By separating runtime assembly from domain behavior, NORA preserves architectural clarity while still allowing the full system to be constructed and executed as one coordinated application.

For that reason, the bootstrap module is a foundational internal implementation module of `src/nora/`.

## Architectural Structure

```text
bootstrap
│
├── Runtime Composition
│   ├── application container
│   ├── dependency registry
│   └── runtime metadata provider
│
├── Configuration Initialization
│   ├── environment loader
│   └── settings loader
│
├── Infrastructure Initialization
│   ├── logger bootstrap
│   ├── database bootstrap
│   ├── vector store bootstrap
│   ├── event bus bootstrap
│   ├── scheduler bootstrap
│   ├── hardware bootstrap
│   └── integrations bootstrap
│
├── Interface Initialization
│   ├── router bootstrap
│   └── websocket bootstrap
│
└── Lifecycle Control
    ├── startup lifecycle
    └── shutdown lifecycle
```
# Shared Module

## Definition

The `shared/` module defines the limited set of implementation elements that are truly transversal across the NORA system.

While the rest of `src/nora/` is intentionally partitioned into explicit architectural domains such as identity, interaction, perception, cognition, dialogue, planning, action, persistence, backend, integrations, hardware, and observability, some software elements do not belong naturally to only one of those domains.

These elements are not domain features in themselves. Instead, they are foundational technical or structural elements reused across multiple modules.

That is the role of `shared/`.

In architectural terms, the shared module is the controlled transversal layer of NORA.

It exists to host a small and disciplined set of reusable elements that support the entire system without eroding the domain boundaries established elsewhere in the architecture.

This module therefore defines:

* system-wide constants
* globally meaningful enums
* strongly typed identifiers
* generic operation models
* base exceptions
* narrow utility functions with broad applicability
* core protocols used for dependency inversion
* minimum shared security helpers

The critical idea is that `shared/` exists to support the architecture, not to bypass it.

It is therefore one of the most dangerous modules in a large codebase if it is not controlled carefully.

A well-designed `shared/` module improves consistency, reuse, safety, and maintainability.

A poorly controlled `shared/` module becomes a dumping ground that destroys architectural clarity.

---

## Architectural Purpose

The purpose of the `shared/` module is to provide common building blocks that are sufficiently generic to be reused across multiple architectural domains without introducing conceptual ambiguity.

In a large system such as NORA, certain structures appear across many modules. For example:

* identifiers are needed in many places
* generic operation results may be reused by multiple services
* base exceptions may be raised by many layers
* protocols may be needed to decouple implementations from abstractions
* time parsing and formatting may recur across domains
* audit metadata may be attached to multiple records

If those elements are duplicated across modules, the codebase becomes inconsistent and error-prone.

If those elements are centralized too aggressively, the codebase loses domain separation and everything starts to depend on everything else.

The architectural purpose of `shared/` is therefore balance.

It must provide enough transversal reuse to avoid duplication, while remaining narrow enough to avoid becoming a structural black hole.

By introducing a disciplined `shared/` module, NORA gains:

* consistent low-level primitives across modules
* stronger typing of global concepts
* reduced duplication of generic technical structures
* clearer system-wide conventions
* safer dependency inversion through explicit protocols
* improved error consistency across layers
* controlled reuse without domain leakage

For that reason, `shared/` is a foundational support module of `src/nora/`, but it must remain constrained by strict architectural rules.

---

## Core Architectural Rule

The most important rule of the shared module is the following:

Only place something in `shared/` if it is genuinely transversal and does not belong more naturally to a single architectural domain.

This rule has several implications.

### Something belongs in `shared/` when:

* it is used across many domains
* it expresses a system-wide primitive
* it is semantically neutral with respect to domain ownership
* it supports multiple modules without importing domain logic into them
* it is stable enough to serve as a common foundation

### Something does not belong in `shared/` when:

* it is mainly used by one domain
* it encodes domain-specific business rules
* it exists only because another module has not yet been structured properly
* it is vaguely “useful” but not clearly transversal
* it mixes technical reuse with domain behavior

This rule is essential because `shared/` can very easily become the accidental center of the whole system if used lazily.

---

## Why `shared/` Must Be Strictly Limited

The `shared/` module is useful precisely because it is limited.

If it grows without discipline, several architectural problems appear very quickly:

* unrelated modules become coupled through hidden shared dependencies
* domain logic gets misplaced into supposedly generic helpers
* global utility files become vague and oversized
* ownership of behavior becomes unclear
* refactoring becomes more dangerous
* onboarding becomes harder because shared code has no obvious conceptual home
* the architecture starts drifting away from the domain model

For NORA, which is already large and multi-domain, this risk is especially serious.

That is why the shared module must be smaller, stricter, and more stable than people usually expect.

It should contain only the foundational pieces that many modules truly need.

---

## Internal Structure

The proposed structure is the following:

```text
shared/
├── constants/
│   ├── time_constants.py
│   ├── event_topic_constants.py
│   ├── header_constants.py
│   ├── pagination_constants.py
│   └── file_type_constants.py
│
├── enums/
│   ├── environment_enum.py
│   ├── language_enum.py
│   ├── timezone_enum.py
│   ├── modality_enum.py
│   ├── channel_origin_enum.py
│   └── execution_status_enum.py
│
├── types/
│   ├── entity_identifier.py
│   ├── correlation_identifier.py
│   ├── trace_identifier.py
│   ├── user_identifier.py
│   ├── session_identifier.py
│   ├── project_identifier.py
│   └── device_identifier.py
│
├── models/
│   ├── paginated_result.py
│   ├── operation_result.py
│   ├── service_health_snapshot.py
│   ├── timestamped_record.py
│   ├── geo_coordinates.py
│   └── audit_metadata.py
│
├── exceptions/
│   ├── domain_error.py
│   ├── validation_error.py
│   ├── authorization_error.py
│   ├── authentication_error.py
│   ├── resource_not_found_error.py
│   ├── conflict_error.py
│   ├── dependency_unavailable_error.py
│   └── unsafe_operation_error.py
│
├── utils/
│   ├── datetime_parser.py
│   ├── datetime_formatter.py
│   ├── slug_builder.py
│   ├── safe_json_loader.py
│   ├── safe_json_dumper.py
│   ├── hash_builder.py
│   ├── text_normalizer.py
│   ├── enum_value_extractor.py
│   └── retry_backoff_builder.py
│
├── protocols/
│   ├── event_publisher_protocol.py
│   ├── event_subscriber_protocol.py
│   ├── unit_of_work_protocol.py
│   ├── clock_protocol.py
│   ├── id_generator_protocol.py
│   └── file_storage_protocol.py
│
└── security/
    ├── secret_redactor.py
    ├── pii_masker.py
    └── input_sanitizer.py
```

This structure is intentionally narrow.

Each subdirectory represents a very specific class of transversal concern.

The purpose is not to centralize everything reusable, but to centralize only the most stable and architecture-safe reusable primitives.

---

## Submodule-by-Submodule Architectural Definition

## `shared/constants/`

The `constants/` submodule contains fixed values that are globally relevant across the NORA system.

These values represent stable reference points used in multiple domains.

Constants belong here only when they are genuinely cross-cutting.

If a constant is only meaningful inside one domain, it should remain inside that domain instead.

### time_constants.py

The `time_constants.py` file defines system-wide constant values related to time representation and duration semantics.

This may include:

* default timeout values
* standard interval definitions
* canonical unit conversions
* shared retry timing values
* standard expiration durations
* common clock-related reference values

Architecturally, this file exists to avoid duplicating low-level time values across modules and to preserve consistent temporal semantics.

It must not become a hidden storage location for every timeout in the system. Only broadly shared temporal constants belong here.

### event_topic_constants.py

The `event_topic_constants.py` file defines globally shared topic names, routing keys, or event-channel identifiers used by the event infrastructure.

Its purpose is to prevent event-topic naming drift and string duplication across modules.

This may include:

* event bus topic names
* broadcast channel identifiers
* projection stream names
* internal routing categories

Architecturally, this file supports consistency in event-driven coordination.

Because event naming affects multiple modules, these values are appropriate as shared constants when they are truly system-wide.

### header_constants.py

The `header_constants.py` file defines shared HTTP, transport, or metadata header names used across interfaces.

This may include:

* correlation headers
* tracing headers
* authentication-related header names
* versioning headers
* custom runtime metadata headers

Architecturally, this file prevents repeated string literals and ensures consistent transport-level metadata naming across backend and integration boundaries.

### pagination_constants.py

The `pagination_constants.py` file defines shared pagination defaults and limits.

This may include:

* default page size
* maximum page size
* minimum page size
* default cursor behavior values
* pagination boundary values

Architecturally, this file supports consistent pagination semantics across APIs, repositories, and query layers.

### file_type_constants.py

The `file_type_constants.py` file defines shared file-type identifiers or file-category constants used across file storage, upload processing, artifact generation, and content handling.

This may include:

* canonical document type labels
* media type families
* recognized artifact classes
* internal file category names

Architecturally, this file supports consistency in how file classes are represented across the system.

---

## `shared/enums/`

The `enums/` submodule contains globally meaningful enumerations that are reused across multiple architectural domains.

Enums belong here only when they represent system-wide concepts.

If an enum is strongly bound to one domain, it should live in that domain instead.

### environment_enum.py

The `environment_enum.py` file defines the set of recognized runtime environments in which NORA may operate.

This may include values such as development, testing, staging, and production.

Architecturally, this enum provides a typed representation of deployment context.

It is useful across bootstrap, deployment-sensitive logic, diagnostics, and environment-aware features.

### language_enum.py

The `language_enum.py` file defines canonical language identifiers used across the system.

This may be relevant for:

* dialogue systems
* voice output
* translation
* frontend preferences
* content generation
* metadata tagging

Architecturally, this enum ensures consistent language representation across modules.

### timezone_enum.py

The `timezone_enum.py` file defines recognized or supported timezone identifiers.

Its purpose is to provide typed timezone representation when such values recur across sessions, scheduling, profiles, or temporal formatting logic.

Architecturally, it supports consistency in time-context representation.

### modality_enum.py

The `modality_enum.py` file defines the major interaction or content modalities recognized by the system.

This may include modalities such as text, voice, image, video, gesture, touch, or sensor-based input.

Architecturally, this enum is useful because multiple modules reason about modality even though no single domain owns the concept entirely.

### channel_origin_enum.py

The `channel_origin_enum.py` file defines the recognized origins of incoming or outgoing interactions.

This may include origins such as web, mobile, local screen, voice interface, remote interface, API, or hardware trigger.

Architecturally, it provides consistent source-channel representation across interaction handling, backend routing, observability, and dialogue metadata.

### execution_status_enum.py

The `execution_status_enum.py` file defines a generic set of execution lifecycle states that may apply across services, jobs, workflows, or operations.

This may include states such as pending, running, completed, failed, canceled, or deferred.

Architecturally, this enum provides a reusable representation of operational progress without forcing each module to redefine the same status model.

---

## `shared/types/`

The `types/` submodule contains strongly typed identifiers and other primitive type wrappers that are meaningful across the system.

Its purpose is to avoid passing raw strings or loosely typed values for important cross-cutting identifiers.

These types improve clarity, safety, and traceability.

### entity_identifier.py

The `entity_identifier.py` file defines a generic identifier type for entities when a specific domain identifier is not appropriate.

Its role is to provide a system-safe abstraction for generic entity references.

### correlation_identifier.py

The `correlation_identifier.py` file defines the identifier type used to correlate actions, events, requests, and logs across a single logical operation.

Architecturally, this type is critical for distributed traceability and cross-module observability.

It may be attached to:

* HTTP requests
* internal events
* background jobs
* logs
* websocket messages

### trace_identifier.py

The `trace_identifier.py` file defines the identifier type used for tracing execution paths across services and modules.

Its purpose is observability-oriented runtime tracking.

While similar to correlation identifiers, its semantics may differ depending on tracing strategy.

### user_identifier.py

The `user_identifier.py` file defines the strongly typed identifier used for user identities across the system.

This type may be reused in dialogue, persistence, frontend support, authorization, and observability contexts.

### session_identifier.py

The `session_identifier.py` file defines the strongly typed identifier used for dialogue or interaction sessions.

It provides a consistent session reference type across session lifecycle, persistence, realtime updates, and recovery logic.

### project_identifier.py

The `project_identifier.py` file defines the strongly typed identifier used for conversational or persistent project structures.

Its purpose is to preserve type clarity when project references move across modules.

### device_identifier.py

The `device_identifier.py` file defines the strongly typed identifier used for hardware devices, linked devices, or controllable external devices.

Its role is to support consistent device references across identity, hardware, integrations, and action modules.

---

## `shared/models/`

The `models/` submodule contains generic structural models that are sufficiently neutral to be reused across multiple domains.

These are not domain-owned objects. They are broad technical or support models with system-wide value.

### paginated_result.py

The `paginated_result.py` file defines a generic structure for paginated query results.

This may include:

* returned items
* total count where applicable
* page size
* current page or cursor
* next page information
* previous page information

Architecturally, this model supports consistent pagination output across APIs, repositories, and query services.

### operation_result.py

The `operation_result.py` file defines a generic result wrapper for bounded operations.

This may include:

* success status
* result payload
* error information
* warning information
* metadata

Architecturally, this model can be useful when operations across modules need a common way to represent bounded execution outcomes.

It should remain generic and should not replace domain-specific result models when domain meaning matters.

### service_health_snapshot.py

The `service_health_snapshot.py` file defines a shared model representing the health status of a service, component, or dependency.

This may include:

* health state
* dependency name
* observed latency
* last check time
* status details

Architecturally, this model is useful across diagnostics, observability, administration, and startup health checks.

### timestamped_record.py

The `timestamped_record.py` file defines a simple shared structure for records that carry creation, update, or event time metadata.

Its role is to standardize timestamp-bearing records when a fully domain-specific model is unnecessary.

### geo_coordinates.py

The `geo_coordinates.py` file defines a shared structure representing geographic coordinates.

Its purpose is to avoid repeated ad hoc latitude-longitude structures across integrations, route planning, location-aware services, or device metadata.

### audit_metadata.py

The `audit_metadata.py` file defines shared metadata used to describe who performed an action, when it happened, from where it originated, and under what trace context.

This may include:

* actor identifier
* timestamp
* channel origin
* correlation identifier
* request source metadata

Architecturally, this model is important because audit metadata is useful in security, persistence, backend operations, and administration.

---

## `shared/exceptions/`

The `exceptions/` submodule contains base exception types reused across multiple domains.

Its purpose is to provide a consistent error vocabulary for technical and architectural error categories.

These exceptions should remain broad and foundational.

Domain-specific exceptions should stay inside their own domains when possible.

### domain_error.py

The `domain_error.py` file defines the generic base exception for domain-level failures.

Its purpose is to provide a common superclass for structured business or operational rule violations.

Architecturally, it allows consistent error handling without flattening all failure types into raw generic exceptions.

### validation_error.py

The `validation_error.py` file defines the exception raised when provided data fails structural or semantic validation.

Its role is to represent invalid input, invalid configuration values, or invalid state transitions at a validation layer.

### authorization_error.py

The `authorization_error.py` file defines the exception raised when an actor lacks the required permissions for an attempted operation.

Its purpose is to express denied access due to authorization constraints.

### authentication_error.py

The `authentication_error.py` file defines the exception raised when identity verification fails or required authentication is missing.

Its role is distinct from authorization failure.

### resource_not_found_error.py

The `resource_not_found_error.py` file defines the exception raised when a requested entity, file, record, or object does not exist or cannot be resolved.

Its purpose is to support consistent missing-resource behavior across modules.

### conflict_error.py

The `conflict_error.py` file defines the exception raised when an operation cannot proceed because of state conflict, duplicate state, concurrency clash, or incompatible existing data.

### dependency_unavailable_error.py

The `dependency_unavailable_error.py` file defines the exception raised when an internal or external dependency required for an operation is unavailable.

This may include:

* database unavailability
* provider outage
* hardware disconnection
* missing service dependency

Architecturally, this exception is especially useful in a system like NORA that depends on many integrations and runtime components.

### unsafe_operation_error.py

The `unsafe_operation_error.py` file defines the exception raised when an operation is blocked for safety reasons.

Its purpose is important in NORA because hardware, device control, and embodied behavior may require explicit refusal when conditions are unsafe.

---

## `shared/utils/`

The `utils/` submodule contains narrowly scoped helper functions that are generic enough to be safely reused across modules.

This is the most dangerous area of the shared module because utilities are where architectural discipline often collapses.

For that reason, every utility file here must be:

* small
* explicit
* generic
* narrowly named
* clearly reusable across domains

There should never be broad files such as `utils.py` or `helpers.py`.

### datetime_parser.py

The `datetime_parser.py` file defines generic logic for parsing date and time values into canonical internal representations.

Its purpose is to support consistent temporal parsing across APIs, configuration, scheduling, and persistence boundaries.

### datetime_formatter.py

The `datetime_formatter.py` file defines generic logic for formatting date and time values into standardized output forms.

Its purpose is to support consistent presentation and serialization of temporal data.

### slug_builder.py

The `slug_builder.py` file defines generic logic for generating URL-safe or identifier-safe slug values from strings.

Its purpose is broadly reusable in projects, artifacts, routes, naming, or storage paths.

### safe_json_loader.py

The `safe_json_loader.py` file defines a protected JSON loading utility focused on robust parsing behavior.

Its role may include:

* exception normalization
* encoding handling
* input validation
* controlled fallback behavior

### safe_json_dumper.py

The `safe_json_dumper.py` file defines a protected JSON serialization utility focused on predictable and safe output generation.

Its purpose is to centralize reusable JSON dumping rules where that behavior must remain consistent.

### hash_builder.py

The `hash_builder.py` file defines generic hash-generation logic for deterministic or protected hashing operations.

Its purpose may support deduplication, artifact naming, content signatures, or integrity checks.

It should not silently become the home for security-sensitive credential hashing that properly belongs to dedicated security or authentication layers.

### text_normalizer.py

The `text_normalizer.py` file defines generic normalization logic for text values.

This may include:

* whitespace normalization
* casing normalization
* accent handling
* canonical cleanup of user or system text inputs

Architecturally, it is useful because many modules process text without owning the general normalization problem.

### enum_value_extractor.py

The `enum_value_extractor.py` file defines utility logic for safely converting enums to underlying values or normalizing enum-like data.

Its role is technical and cross-cutting.

### retry_backoff_builder.py

The `retry_backoff_builder.py` file defines generic retry timing or backoff sequence construction logic.

Its purpose is to provide reusable retry behavior primitives for integrations, infrastructure clients, or resilient operational flows.

---

## `shared/protocols/`

The `protocols/` submodule contains structural interface contracts used to support dependency inversion.

These protocols define what a dependency must do without forcing modules to depend on a concrete implementation.

Architecturally, this is one of the most important parts of `shared/` because it allows the rest of the system to remain decoupled.

Protocols placed here should be truly reusable across multiple modules.

### event_publisher_protocol.py

The `event_publisher_protocol.py` file defines the interface contract for components capable of publishing events.

Its purpose is to let modules depend on event-publication capability without binding directly to a specific event bus implementation.

### event_subscriber_protocol.py

The `event_subscriber_protocol.py` file defines the interface contract for components capable of receiving or subscribing to events.

Its role supports decoupled event-driven architecture.

### unit_of_work_protocol.py

The `unit_of_work_protocol.py` file defines the interface contract for transactional boundary coordination.

Its purpose is to allow services to depend on transaction semantics without depending on a specific persistence backend.

Architecturally, this is especially important in persistence-facing workflows.

### clock_protocol.py

The `clock_protocol.py` file defines the interface contract for obtaining time values from a clock source.

Its purpose is to support deterministic testing and time abstraction.

Instead of calling wall-clock time directly everywhere, modules can depend on this protocol.

### id_generator_protocol.py

The `id_generator_protocol.py` file defines the interface contract for generating identifiers.

Its role is to decouple identifier creation from specific generation strategies.

This improves consistency and testability.

### file_storage_protocol.py

The `file_storage_protocol.py` file defines the interface contract for storing, retrieving, and managing file artifacts.

Its purpose is to decouple file handling logic from a specific storage backend.

This may support local storage, cloud storage, or alternative file persistence strategies.

---

## `shared/security/`

The `security/` submodule contains a minimal set of transversal security-support helpers that are broadly applicable across modules.

These helpers must remain generic and should not replace the dedicated `identity_access_security/security/` domain logic.

Their purpose is defensive support, not full security ownership.

### secret_redactor.py

The `secret_redactor.py` file defines generic logic for removing, masking, or redacting secret values from logs, diagnostics, payload dumps, or observability outputs.

Its role is to reduce accidental secret leakage across the system.

### pii_masker.py

The `pii_masker.py` file defines generic logic for masking personally identifiable information in outputs, logs, previews, or debug traces.

Its role is to support privacy-aware handling across multiple modules.

### input_sanitizer.py

The `input_sanitizer.py` file defines generic input sanitization logic for cross-cutting protection against malformed or unsafe raw input.

Its role is to provide a first-line generic sanitization layer where such behavior is broadly applicable.

It should remain general-purpose and must not become a replacement for domain-specific validation.

---

## Design Constraints of the Shared Module

The shared module should obey several strict constraints.

### 1. No domain ownership theft

If an element clearly belongs to identity, perception, dialogue, planning, persistence, hardware, or any other specific module, it must remain there.

### 2. No catch-all files

Files such as `common.py`, `helpers.py`, `misc.py`, or `utils.py` should not exist here.

Every file must have a narrow explicit purpose.

### 3. No hidden business logic

Business rules should not be disguised as generic helpers.

### 4. No unstable abstractions

If something is still evolving heavily inside one domain, it should not be promoted to `shared/` prematurely.

### 5. Prefer duplication over bad centralization

A small amount of local duplication is better than placing a concept in `shared/` when it does not truly belong there.

This is one of the most important architectural disciplines in a project like NORA.

---

## Interaction With Other Modules

The `shared/` module interacts with nearly all modules, but only as a support layer.

### bootstrap

Uses shared enums, protocols, exceptions, and generic models during system composition and startup.

### identity_access_security

n
Uses shared identifiers, audit metadata, exceptions, and sanitization support.

### interaction_interfaces

Uses shared modality, channel-origin values, identifiers, and generic validation structures.

### perception

Uses shared identifiers, execution statuses, timestamp structures, and event-related protocols.

### cognitive_core

Uses shared identifiers, time utilities, generic operation structures, and exceptions.

### dialogue_and_session

Uses shared identifiers, pagination models, timestamp structures, and language-related enums.

### planning_and_agents

Uses shared operation models, execution statuses, retry helpers, and protocols.

### action_and_expression

Uses shared identifiers, file-type concepts, operation results, and safety-related exceptions.

### persistence_and_memory

Uses shared timestamps, identifiers, unit-of-work protocol, file-storage protocol, and generic exceptions.

### backend_and_application

Uses shared pagination structures, header constants, correlation types, health snapshots, and common exceptions.

### integrations_and_external_services

Uses shared retry/backoff utilities, environment enums, dependency errors, and protocols.

### infrastructure_and_hardware

Uses shared device identifiers, timestamps, operation results, and unsafe-operation errors.

### observability

Uses correlation identifiers, trace identifiers, health snapshots, audit metadata, and redaction or masking helpers.

The key architectural rule is that interaction with `shared/` should be foundational, not ownership-replacing.

---

## What Should Not Be Added to `shared/`

To preserve architectural clarity, the following categories should generally not be added to `shared/` unless there is an exceptional and very clear reason:

* domain services
* domain repositories
* domain event definitions
* feature-specific DTOs
* business rules
* workflow coordinators
* framework-specific application handlers
* integration-specific adapters
* domain-specific validation logic
* hardware-specific safety logic
* planner-specific reasoning helpers

These belong in the modules that actually own them.

---

## Testing Implications

Because `shared/` provides common building blocks, defects here can propagate widely.

This means the shared module has high leverage in testing.

Important test categories include:

* identifier-type correctness tests
* enum serialization tests
* pagination model tests
* operation result behavior tests
* exception mapping tests
* utility correctness tests
* protocol compatibility tests
* security helper masking and redaction tests

Even though many files in `shared/` are small, they are structurally important because they are reused in many places.

---

## Why This Structure Fits NORA

This shared structure fits NORA because NORA is large enough to need transversal primitives, but also complex enough that careless reuse would damage the architecture.

The proposed structure gives NORA:

* a place for global technical primitives
* a place for reusable low-level typing
* a place for stable cross-cutting abstractions
* a place for minimum safe utilities
* a place for dependency inversion protocols

while still preserving the rule that domain logic must remain inside domain modules.

That balance is exactly what a system like NORA needs.

---

## Architectural Importance

The `shared/` module provides the transversal technical foundation that allows the rest of the NORA architecture to remain consistent without collapsing domain boundaries.

While each major architectural module owns its own logic, several low-level concepts such as identifiers, result structures, exceptions, protocols, and safety-oriented utility helpers must remain consistent across the system.

Through this module the architecture gains:

* consistent global primitives
* reusable typed identifiers
* common technical models
* standardized exception vocabulary
* controlled low-level utility reuse
* explicit dependency inversion contracts
* cross-cutting safety support for logging and input handling

By keeping these transversal elements narrow, explicit, and architecture-safe, NORA avoids duplication without turning the shared layer into a structural dumping ground.

For that reason, `shared/` is a necessary foundational module of `src/nora/`, but one whose value depends entirely on strong discipline.

## Architectural Structure

```text
shared
│
├── Constants
│   ├── time constants
│   ├── event topic constants
│   ├── header constants
│   ├── pagination constants
│   └── file type constants
│
├── Global Enums
│   ├── environment enum
│   ├── language enum
│   ├── timezone enum
│   ├── modality enum
│   ├── channel origin enum
│   └── execution status enum
│
├── Typed Identifiers and Primitive Types
│   ├── generic entity identifier
│   ├── correlation identifier
│   ├── trace identifier
│   ├── user identifier
│   ├── session identifier
│   ├── project identifier
│   └── device identifier
│
├── Generic Shared Models
│   ├── paginated result
│   ├── operation result
│   ├── service health snapshot
│   ├── timestamped record
│   ├── geographic coordinates
│   └── audit metadata
│
├── Base Exceptions
│   ├── domain error
│   ├── validation error
│   ├── authorization error
│   ├── authentication error
│   ├── resource not found error
│   ├── conflict error
│   ├── dependency unavailable error
│   └── unsafe operation error
│
├── Narrow Shared Utilities
│   ├── datetime parser
│   ├── datetime formatter
│   ├── slug builder
│   ├── safe JSON loader
│   ├── safe JSON dumper
│   ├── hash builder
│   ├── text normalizer
│   ├── enum value extractor
│   └── retry backoff builder
│
├── Dependency Inversion Protocols
│   ├── event publisher protocol
│   ├── event subscriber protocol
│   ├── unit of work protocol
│   ├── clock protocol
│   ├── ID generator protocol
│   └── file storage protocol
│
└── Transversal Security Helpers
    ├── secret redactor
    ├── PII masker
    └── input sanitizer
```


# Identity, Access and Security Module

## Definition

The `identity_access_security/` module defines how NORA represents actors, verifies identity, controls access, personalizes behavior, and protects the system against misuse, abuse, and unsafe privileged operation.

While other architectural modules define perception, cognition, dialogue, planning, action, persistence, frontend behavior, integrations, and hardware interaction, none of those capabilities can operate safely without a clear answer to five foundational questions:

* who is interacting with the system
* how that identity is verified
* what that actor is allowed to do
* how that actor’s preferences affect system behavior
* how the system detects and responds to risky or malicious activity

That is the role of `identity_access_security/`.

In architectural terms, this module defines the trust layer of NORA.

It is the module that determines how human and device actors become recognized identities, how trust is established, how privileges are assigned and enforced, how personalization is grounded in profile state, and how security events are observed and controlled.

This module therefore defines:

* identity representation
* anonymous and registered user handling
* linked device association
* authentication methods and session trust
* token issuance and validation
* authorization policy and permission evaluation
* role assignment and protected resource access
* user profile and personalization preferences
* security event registration and auditability
* suspicious activity detection and incident response
* boundary middleware for authentication, authorization, and rate limiting

This module is not merely a technical access layer.

In NORA, identity and security are structurally central because the system may:

* persist user-specific history
* recover prior sessions and projects
* execute external actions
* control hardware or IoT devices
* access personal integrations
* expose administrative interfaces
* adapt behavior to user preferences

Because of that, the `identity_access_security/` module is a foundational domain module, not an auxiliary feature.

---

## Architectural Purpose

The purpose of the `identity_access_security/` module is to ensure that NORA operates as a safe, accountable, personalized, and access-controlled system.

Without a dedicated identity and security architecture, the rest of the system would suffer from major structural risks:

* inability to distinguish between anonymous and trusted actors
* inconsistent authentication decisions
* unclear permission enforcement
* unsafe access to hardware or administrative functions
* missing auditability for sensitive actions
* weak personalization consistency
* poor handling of suspicious or abusive behavior
* inability to apply differentiated privileges to different user classes

By introducing a dedicated module for identity, access, profile, and security behavior, NORA gains:

* clear user and actor representation
* explicit authentication mechanisms
* enforceable authorization rules
* structured profile-driven personalization
* stronger accountability for sensitive actions
* safer access to protected operations
* security visibility and incident handling
* trust-aware runtime behavior

This module therefore provides the trust, safety, and user-governance basis on which the rest of the NORA architecture can operate.

---

## Internal Domain Structure

The proposed internal structure is the following:

```text
identity_access_security/
├── users/
├── authentication/
├── authorization/
├── user_profile/
└── security/
```

This structure separates five different but closely related concerns.

### users

Defines who the actor is.

### authentication

Defines how identity claims are verified.

### authorization

Defines what a verified actor is allowed to do.

### user_profile

Defines how persistent user preferences and personalization settings shape system behavior.

### security

Defines how risky, abnormal, privileged, or suspicious behavior is monitored, recorded, and controlled.

This decomposition is important because identity, authentication, authorization, profile personalization, and security are related but not identical concerns.

Mixing them in one flat directory would quickly erase important trust boundaries.

---

## Architectural Logic of the Module

The internal logic of the module can be understood as a layered trust flow.

1. An actor exists or is inferred.
2. That actor may be anonymous, partially known, or fully identified.
3. Authentication determines whether identity claims are trusted.
4. Authorization determines which operations are allowed.
5. Profile data influences how NORA should adapt interaction.
6. Security mechanisms observe the entire flow for abnormal, unsafe, or malicious behavior.

This means that the module is not a set of isolated folders. It is a coordinated trust architecture.

The trust relationship between submodules is roughly this:

* `users/` establishes identity objects and identity resolution
* `authentication/` establishes credential or trust validation
* `authorization/` evaluates permissions and access scope
* `user_profile/` provides user-specific behavioral configuration
* `security/` records, detects, and mitigates risky activity across all of the above

---

# 1. users

## Definition

The `users/` submodule defines how NORA represents and manages actors as identities.

Its purpose is to model the human or device-associated entities that interact with the system, whether they are anonymous, partially known, or fully registered.

This submodule answers questions such as:

* what is a user identity in NORA
* how do anonymous actors differ from known actors
* how are devices linked to identities
* what attributes define an identity
* how is identity resolved from available signals

This is not yet authentication. It is identity representation and identity lifecycle.

### Internal Structure

```text
users/
├── enums/
├── models/
├── events/
├── repositories/
├── services/
└── queries/
```

---

## users/enums/

### user_capability_level_enum.py

Defines the abstract capability level associated with a user identity.

Its purpose is to classify users according to broad system capacity or entitlement level before fine-grained permission checks are applied.

This may support distinctions such as:

* anonymous actor
* basic user
* privileged operator
* administrator
* system-level actor

Architecturally, this enum expresses coarse trust and capability tiering at the identity level.

### identity_status_enum.py

Defines the lifecycle status of an identity.

This may include states such as:

* active
* suspended
* deactivated
* pending
* deleted or archived

Its role is to ensure identity lifecycle state is explicit and enforceable.

### device_trust_level_enum.py

Defines the trust level assigned to a device linked to an identity.

This may include classifications such as unknown, remembered, trusted, verified, or restricted.

Its purpose is especially important when device association contributes to authentication or personalization behavior.

---

## users/models/

### user_identity.py

Defines the primary structured representation of a known user identity in NORA.

This model may include:

* identity identifier
* name or label information
* email or contact references
* capability level
* identity status
* linked device references
* audit metadata

Architecturally, this is the core identity object for known actors.

### anonymous_identity.py

Defines the structured representation of an actor who is interacting with NORA without a persistent registered identity.

Its role is important because NORA may need to support guest or unauthenticated usage without confusing that with a fully trusted user.

This model makes anonymous interaction explicit rather than implicit.

### linked_device.py

Defines a device associated with a user identity.

This may represent:

* a trusted browser
* a registered mobile device
* a paired NFC token
* a local console
* a biometric-capable device

Its purpose is to make device-bound identity and trust relationships explicit.

### identity_attributes.py

Defines structured attributes attached to an identity beyond the main user object.

This may include descriptive, operational, or resolution-related attributes used in matching, personalization, or trust evaluation.

Its role is to keep identity data modular and extensible.

### identity_resolution_result.py

Defines the result of attempting to resolve an actor into a known or probable identity.

This may include:

* resolved identity
* resolution confidence
* candidate identities
* matched device information
* ambiguity state

Architecturally, this model is important because identity may sometimes be inferred rather than explicitly declared.

---

## users/events/

### identity_created_event.py

Defines the event emitted when a new identity is created in the system.

Its purpose is to make identity creation observable to other modules such as persistence, audit, personalization, or administrative monitoring.

### identity_updated_event.py

Defines the event emitted when a user identity is modified.

This may be relevant when identity attributes, status, or linked relationships change.

### identity_deactivated_event.py

Defines the event emitted when an identity is deactivated.

Its role is important for access revocation, audit logging, session termination, and security coordination.

### active_user_changed_event.py

Defines the event emitted when the currently active user context changes.

This is especially relevant in shared-device, embodied, or local-interface scenarios where the active user may shift during operation.

---

## users/repositories/

### user_identity_repository.py

Defines the persistence boundary for storing and retrieving user identities.

Its purpose is to isolate identity storage logic from the higher-level services that manipulate identities.

### linked_device_repository.py

Defines the persistence boundary for linked device records associated with identities.

Its role is to support device-aware trust and identity resolution.

### identity_event_repository.py

Defines the persistence boundary for storing identity-related event history when such event records are retained directly.

Its role supports auditability and historical reconstruction of identity lifecycle behavior.

---

## users/services/

### create_identity_service.py

Defines the operation that creates a new user identity.

Its responsibilities may include validation, initial status assignment, default capability level assignment, and publication of the identity-created event.

### update_identity_service.py

Defines the operation that updates an existing identity.

Its role is to centralize controlled mutation of identity state.

### deactivate_identity_service.py

Defines the operation that deactivates an identity without necessarily deleting its historical existence.

Its role is important for safe access revocation while preserving auditability.

### delete_identity_service.py

Defines the operation that removes or logically deletes an identity according to system policy.

Its implementation must be especially careful because identity deletion may affect persistence, session continuity, and audit history.

### resolve_identity_service.py

Defines the operation that attempts to map available evidence into a known identity or identity candidate.

This may use email, device linkage, login state, proximity data, or other context.

Architecturally, this service is key for converting raw actor evidence into user context.

### link_device_to_identity_service.py

Defines the operation that associates a device with a specific identity.

Its purpose is to support device trust, faster identity resolution, and authentication-related flows.

---

## users/queries/

### get_identity_by_id.py

Defines the read operation that retrieves a user identity by its unique identifier.

### get_identity_by_email.py

Defines the read operation that retrieves an identity from an email reference when email-based identity resolution is supported.

### list_linked_devices.py

Defines the read operation that returns the devices associated with a specific identity.

### search_identities.py

Defines the read operation used to search or filter identities according to administrative or operational criteria.

---

# 2. authentication

## Definition

The `authentication/` submodule defines how NORA verifies identity claims.

Its purpose is to determine whether an actor presenting a credential, token, biometric signal, trusted device assertion, or proximity signal should be treated as authenticated.

Authentication answers the question:

Is this actor really who they claim to be, or sufficiently verified for the requested trust level?

This is distinct from identity representation and distinct from authorization.

### Internal Structure

```text
authentication/
├── enums/
├── models/
├── services/
├── repositories/
└── providers/
```

---

## authentication/enums/

### authentication_method_enum.py

Defines the supported authentication methods recognized by NORA.

This may include methods such as:

* password or credential authentication
* token-based authentication
* biometric authentication
* device-based authentication
* proximity-based authentication

Its role is to make authentication mode explicit in session records, audit logs, and policy decisions.

### token_type_enum.py

Defines the types of authentication tokens used by the system.

This may include access tokens, refresh tokens, temporary tokens, or privileged escalation tokens.

### session_auth_status_enum.py

Defines the authentication status of a session.

This may include states such as unauthenticated, pending, partially authenticated, fully authenticated, expired, or revoked.

Its purpose is to represent trust level at the session boundary, not just at individual credential checks.

---

## authentication/models/

### login_credentials.py

Defines the structured representation of credentials submitted for login.

Its role is to normalize credential input at the authentication boundary.

### authentication_token.py

Defines the structured representation of an issued authentication token.

This may include token value, token type, subject identity, expiration, and scope-related metadata.

### refresh_token.py

Defines the structured representation of a refresh token used to obtain renewed authentication state.

Its purpose is to separate long-lived renewal artifacts from primary access tokens.

### active_auth_session.py

Defines the authenticated session object representing an ongoing verified session.

This may include:

* session identifier
* authenticated identity
* authentication method
* issued token references
* trust metadata
* last activity time
* current auth status

### biometric_auth_result.py

Defines the outcome of a biometric authentication attempt.

This may include match status, confidence, method metadata, and failure reason.

### trusted_device_assertion.py

Defines the structured assertion that a device should be treated as trusted within an authentication flow.

Its role is important in multi-factor, remembered-device, or local-control scenarios.

---

## authentication/services/

### credential_authentication_service.py

Defines the operation that authenticates an actor using explicit login credentials.

Its responsibilities may include credential verification, session creation, token issuance, and failure recording.

### token_validation_service.py

Defines the operation that validates an incoming authentication token.

Its role is to determine whether the token is structurally valid, not expired, not revoked, and bound to an acceptable trust context.

### refresh_token_service.py

Defines the operation that exchanges a refresh token for renewed authentication state.

Its purpose is to support secure session continuity.

### biometric_authentication_service.py

Defines the operation that authenticates an actor via biometric evidence.

Its implementation may rely on provider-level biometric comparison logic, but this service owns the authentication semantics of that result.

### device_authentication_service.py

Defines the operation that authenticates or upgrades trust based on a linked or trusted device.

Its role is especially relevant in embodied or multi-device deployment contexts.

### proximity_authentication_service.py

Defines the operation that authenticates or partially authenticates an actor using proximity-based evidence such as NFC, RFID, short-range device presence, or similar mechanisms.

### logout_session_service.py

Defines the operation that terminates an authenticated session.

Its purpose is to invalidate active trust state in a controlled way.

### revoke_token_service.py

Defines the operation that invalidates one or more tokens so they can no longer be used.

Its role is important for logout, incident response, and compromised-session recovery.

---

## authentication/repositories/

### auth_session_repository.py

Defines the persistence boundary for active or historical authentication sessions.

Its role is to support session trust management and revocation logic.

### token_repository.py

Defines the persistence boundary for token records where token state is explicitly stored or revocation must be tracked.

---

## authentication/providers/

### password_hasher_provider.py

Defines the abstraction over password hashing and credential verification mechanisms.

Its purpose is to separate authentication semantics from the concrete cryptographic implementation.

### jwt_token_provider.py

Defines the abstraction over token issuance, signing, decoding, and validation for JWT-based authentication flows.

### biometric_match_provider.py

Defines the abstraction over biometric matching technology.

Its role is to let NORA depend on biometric capability without coupling the authentication submodule to one specific biometric engine.

---

# 3. authorization

## Definition

The `authorization/` submodule defines how NORA decides whether an authenticated or otherwise known actor is allowed to perform a requested action.

If authentication answers who the actor is, authorization answers what they may do.

This submodule is responsible for:

* role definition
* permission definition
* permission evaluation
* protected resource access control
* context-aware access decisions
* least-privilege enforcement
* safety-sensitive authorization for hardware or other dangerous capabilities

### Internal Structure

```text
authorization/
├── enums/
├── models/
├── policies/
├── services/
└── repositories/
```

---

## authorization/enums/

### role_enum.py

Defines the recognized role categories used by the authorization system.

Its purpose is to represent coarse permission groupings such as user, operator, admin, or other system-defined roles.

### permission_scope_enum.py

Defines the scope categories under which permissions are evaluated.

This may include global, session-level, project-level, device-level, resource-level, or administrative scope.

Its role is important because permissions are often not absolute; they depend on scope.

### protected_resource_enum.py

Defines the categories of resources that may be protected by authorization policy.

This may include:

* sessions
* projects
* user records
* configuration surfaces
* hardware commands
* administrative dashboards
* integrations

Its purpose is to make protected target classes explicit.

---

## authorization/models/

### role_definition.py

Defines the structured representation of a role in the system.

This may include role identifier, role name, description, and relationship to permission sets.

### permission_definition.py

Defines the structured representation of a permission.

This may include action category, protected resource, scope, and descriptive metadata.

### access_request.py

Defines the structured representation of an attempted access operation.

This model may include:

* requesting actor
* requested action
* target resource
* context information
* scope information

Architecturally, this is the key input to authorization evaluation.

### access_decision.py

Defines the structured result of authorization evaluation.

This may include allow or deny status, decision reason, applied policies, and context-sensitive restrictions.

### authorization_context.py

Defines the contextual information used during authorization evaluation.

This may include runtime state, session state, hardware safety state, relationship to resource ownership, and environmental constraints.

---

## authorization/policies/

### role_permission_policy.py

Defines the policy that maps roles to permissions.

Its purpose is to provide the core static authorization structure of the system.

### context_aware_authorization_policy.py

Defines the policy that adjusts authorization decisions based on contextual factors.

This may include session state, ownership, environment, location of request origin, or active project context.

### least_privilege_policy.py

Defines the policy that constrains access decisions to the minimum privileges necessary.

Its purpose is to prevent excessive or accidental over-authorization.

### hardware_safety_authorization_policy.py

Defines the policy that combines authorization with hardware safety constraints.

Its role is especially important in NORA because some commands may be both privilege-sensitive and physically risky.

---

## authorization/services/

### authorize_action_service.py

Defines the primary operation that evaluates whether an attempted action should be authorized.

This service is the core execution point of authorization semantics.

### resolve_permission_set_service.py

Defines the operation that resolves the effective permission set for an actor based on roles, assignments, and contextual constraints.

### assign_role_service.py

Defines the operation that assigns a role to an identity.

Its implementation must preserve auditability and administrative control.

### revoke_role_service.py

Defines the operation that removes a role assignment from an identity.

Its role is essential for privilege reduction and access correction.

### evaluate_resource_access_service.py

Defines the operation that evaluates access to a specific protected resource instance or category.

Its purpose is to support resource-sensitive authorization decisions beyond broad role checking.

---

## authorization/repositories/

### role_repository.py

Defines the persistence boundary for role definitions.

### permission_repository.py

Defines the persistence boundary for permission definitions.

### role_permission_repository.py

Defines the persistence boundary for the relationship between roles and permissions, and potentially for identity-to-role assignment data depending on overall persistence structure.

---

# 4. user_profile

## Definition

The `user_profile/` submodule defines how NORA stores and applies user-specific preferences, personalization settings, and interface adaptation parameters.

Its purpose is to separate who a user is from how the system should behave for that user.

This distinction matters because identity alone does not determine preferred interaction style.

The profile submodule therefore governs:

* voice preference
* interface mode preference
* feedback style preference
* personalization settings
* effective profile resolution
* resetting and updating preference state

### Internal Structure

```text
user_profile/
├── enums/
├── models/
├── services/
└── repositories/
```

---

## user_profile/enums/

### preferred_voice_enum.py

Defines the allowed or recognized voice preference categories for a user profile.

Its purpose is to support consistent voice personalization across action and expression layers.

### preferred_interface_mode_enum.py

Defines the preferred interface mode for a user.

This may refer to visual style, interaction mode emphasis, simplified or advanced interface preference, or primary channel preference.

### preferred_feedback_style_enum.py

Defines the preferred style of system feedback.

This may capture preferences such as concise, detailed, formal, supportive, visual, auditory, or guided feedback patterns.

---

## user_profile/models/

### user_profile.py

Defines the primary structured representation of a persistent user profile.

This may include:

* profile identifier
* associated user identity
* preference collections
* personalization settings
* profile-level metadata

### user_preferences.py

Defines the specific collection of explicit user preferences.

Its role is to keep preference state grouped and structured.

### personalization_settings.py

Defines the additional personalization parameters that may shape runtime behavior beyond explicit preferences.

This may include adaptive behavior toggles, default channels, or personalization intensity settings.

### linked_profile_device.py

Defines the relationship between a profile and a device in contexts where profile preferences may apply differently depending on the device used.

---

## user_profile/services/

### create_user_profile_service.py

Defines the operation that creates a new user profile, potentially alongside identity creation or first-time user initialization.

### update_user_preferences_service.py

Defines the operation that updates explicit user preferences.

Its purpose is to centralize controlled preference mutation.

### update_personalization_service.py

Defines the operation that updates broader personalization settings beyond direct preference fields.

### get_effective_profile_settings_service.py

Defines the operation that resolves the final effective settings NORA should apply for a user in a given context.

This may involve combining profile defaults, device-specific overrides, session context, and system-level fallback rules.

### reset_user_preferences_service.py

Defines the operation that resets preference state back to system defaults or profile defaults according to policy.

---

## user_profile/repositories/

### user_profile_repository.py

Defines the persistence boundary for storing and retrieving user profiles and profile-related state.

Its purpose is to isolate profile storage concerns from higher-level personalization services.

---

# 5. security

## Definition

The `security/` submodule defines how NORA records security-relevant events, detects suspicious activity, applies defensive controls, evaluates rate limiting, and manages incidents.

Its purpose is broader than authentication and authorization.

Authentication and authorization control trust decisions.

The security submodule observes the operational trust surface itself.

It is therefore responsible for:

* audit trail generation
* security event registration
* suspicious activity detection
* rate limiting decisions
* protective response triggering
* incident tracking and resolution
* request-boundary protection middleware

### Internal Structure

```text
security/
├── enums/
├── models/
├── services/
├── repositories/
└── middleware/
```

---

## security/enums/

### security_event_type_enum.py

Defines the recognized categories of security-relevant events.

This may include login failure, access denial, suspicious pattern detection, rate limit breach, privilege escalation attempt, or incident transition.

Its purpose is to standardize security event classification.

### threat_level_enum.py

Defines the severity or risk level associated with a security signal, event, or incident.

This may include low, medium, high, or critical levels.

### incident_status_enum.py

Defines the lifecycle status of a security incident.

This may include open, investigating, mitigated, resolved, or dismissed.

---

## security/models/

### security_event.py

Defines the structured representation of a security-relevant event.

This model may include type, timestamp, actor, request context, trace identifiers, severity, and descriptive metadata.

### audit_record.py

Defines the structured representation of an auditable action record.

Its role is broader than security incidents because it may record privileged, sensitive, or compliance-relevant actions even when no attack or anomaly is present.

### suspicious_activity_signal.py

Defines the structured representation of a detected suspicious pattern prior to full incident creation.

Its purpose is to model intermediate security concern states.

### security_incident.py

Defines the structured representation of a formal security incident under investigation or response.

Its role is to preserve structured incident lifecycle management.

### rate_limit_decision.py

Defines the result of evaluating a request or actor against rate-limiting policy.

This may include allow, throttle, or block decisions together with reason metadata.

---

## security/services/

### write_audit_record_service.py

Defines the operation that writes audit records for sensitive or relevant actions.

Its purpose is accountability and forensic traceability.

### detect_suspicious_activity_service.py

Defines the operation that analyzes behavior and determines whether suspicious activity signals should be generated.

Its logic may consider failed authentications, abnormal request rates, privilege anomalies, or suspicious interaction patterns.

### register_security_event_service.py

Defines the operation that records a security event in structured form.

Its role is to ensure security-relevant observations are durable and queryable.

### evaluate_rate_limit_service.py

Defines the operation that evaluates whether a request or actor exceeds allowed behavior rates.

Its purpose is protective control against abuse or overload.

### trigger_protective_response_service.py

Defines the operation that triggers an immediate defensive action when security policy requires it.

This may include blocking access, revoking tokens, throttling requests, forcing re-authentication, or escalating an incident.

### resolve_security_incident_service.py

Defines the operation that marks a security incident as resolved, mitigated, or otherwise transitioned according to incident policy.

Its role supports formal security lifecycle closure.

---

## security/repositories/

### audit_record_repository.py

Defines the persistence boundary for audit records.

### security_event_repository.py

Defines the persistence boundary for security event records.

### security_incident_repository.py

Defines the persistence boundary for security incidents and their lifecycle state.

---

## security/middleware/

### authentication_boundary_middleware.py

Defines the middleware responsible for enforcing authentication requirements at boundary interfaces.

Its role is to ensure that protected endpoints or transport surfaces cannot be accessed without required authentication state.

### authorization_boundary_middleware.py

Defines the middleware responsible for enforcing authorization decisions at interface boundaries.

Its purpose is to ensure that request flows are halted when permission requirements are not satisfied.

### rate_limit_middleware.py

Defines the middleware responsible for applying request-rate controls before deeper processing proceeds.

Its role is a first-line operational protection mechanism.

### request_trace_middleware.py

Defines the middleware responsible for attaching or propagating request trace context.

Its purpose is observability, auditability, and cross-system trace correlation.

---

## Cross-Submodule Relationships

The five submodules are distinct, but they are deeply connected.

### users -> authentication

Authentication depends on identity objects, linked devices, and identity resolution outcomes.

### authentication -> authorization

Authorization decisions rely on the trust state produced by authentication.

### users -> user_profile

Profiles are anchored to user identities and shape user-specific behavior.

### authentication -> security

Authentication failures, unusual trust assertions, and session anomalies are security-relevant.

### authorization -> security

Access denials, privilege escalation attempts, and protected resource misuse may produce security signals or audit records.

### user_profile -> security

Profile changes, especially sensitive preference changes or linked-device changes, may require auditing.

These relationships show why the entire module is best treated as a unified trust architecture rather than as five unrelated directories.

---

## Design Constraints of the Module

The `identity_access_security/` module should obey several strict architectural constraints.

### 1. Authentication and authorization must remain distinct

The system must not blur the difference between verifying identity and deciding permissions.

### 2. Identity and profile must remain distinct

A user identity defines who the actor is.

A profile defines how the system should adapt to that actor.

These concerns must not collapse into one object without care.

### 3. Security must observe the trust system, not replace it

The security submodule should not become a vague wrapper over all trust behavior.

Authentication and authorization still own their own decisions.

Security owns detection, recording, protective reaction, and auditability.

### 4. Hardware-sensitive access must be explicitly protected

Because NORA may execute physical actions, privileged hardware control must be subject to explicit authorization and safety-aware policy.

### 5. Auditability must be preserved for sensitive operations

Changes to roles, identity state, session trust, linked devices, and incident handling should remain traceable.

### 6. Anonymous interaction must be explicit

Guest or anonymous use should never be treated as an implicit version of a full identity.

---

## Interaction With Other Modules

The `identity_access_security/` module interacts with many other architectural domains.

### bootstrap

Provides initialized providers, repositories, settings, and middleware bindings required for trust and security enforcement.

### shared

Uses shared identifiers, exceptions, audit metadata, channel-origin values, and sanitization helpers.

### interaction_interfaces

Receives user-originating and device-originating interaction signals that may need identity resolution, trust evaluation, or boundary protection.

### perception

May consume perception-derived identity cues such as face recognition, speaker identification, device presence, or proximity signals as part of identity resolution or authentication flows.

### cognitive_core

Provides active user trust state and authorization-relevant context to the runtime control system.

### dialogue_and_session

Anchors sessions and conversational continuity to user identity and session trust state.

### planning_and_agents

May constrain or shape plan generation based on permission scope, active user capabilities, or tool-access restrictions.

### action_and_expression

Controls whether privileged actions, device commands, outbound communication, or risky operations may proceed.

### persistence_and_memory

Stores identities, sessions, roles, permissions, profiles, audit records, and security incidents.

### backend_and_application

Applies authentication and authorization at API, websocket, and administrative boundaries.

### frontend_support

Shapes frontend-visible security state, user context, and profile-based presentation data.

### integrations_and_external_services

Protects access to external accounts, productivity services, and third-party capabilities through trust-aware policies.

### infrastructure_and_hardware

Controls access to hardware commands, device associations, and physically sensitive operations.

### observability

Supplies audit data, trace context, security event information, and incident status for system observability.

---

## Testing Implications

This module is central to trust correctness, so it requires especially careful testing.

Important test categories include:

* identity lifecycle tests
* anonymous identity behavior tests
* linked-device trust tests
* credential authentication tests
* token issuance and revocation tests
* session authentication-state tests
* role and permission resolution tests
* context-aware authorization tests
* hardware-safety authorization tests
* profile preference resolution tests
* audit record generation tests
* suspicious activity detection tests
* incident lifecycle tests
* rate limiting tests
* middleware boundary enforcement tests

Failures here can lead not just to bugs but to unsafe or unauthorized system behavior.

---

## Why This Structure Fits NORA

This structure fits NORA because the system is both personalized and operationally powerful.

NORA is not just a passive interface. It may:

* remember users
* recover prior projects
* trigger digital actions
* control external devices
* expose privileged administration
* adapt output style to user preference
* operate across web, local, voice, and embedded channels

A system with those properties needs a trust architecture that is not superficial.

The proposed structure provides that by separating:

* identity representation
* trust verification
* permission enforcement
* user personalization
* defensive security operations

while still allowing them to work together as one coherent module.

---

## Architectural Importance

The `identity_access_security/` module provides the trust, access-control, and protection foundation of the NORA system.

While other modules define how NORA perceives, reasons, dialogues, plans, acts, remembers, visualizes, and integrates with the outside world, all of those capabilities depend on a reliable answer to who is interacting with the system, how that identity is verified, what privileges are available, how the system should adapt to that actor, and how risky behavior is detected and controlled.

Through this module the architecture gains:

* explicit user and actor representation
* controlled authentication flows
* structured authorization and permission enforcement
* persistent user personalization support
* auditability for sensitive operations
* security event visibility
* suspicious activity detection and response
* safer access to administrative and hardware capabilities

By separating users, authentication, authorization, profile management, and security operations into explicit subdomains, NORA preserves conceptual clarity while still operating through a unified trust architecture.

For that reason, `identity_access_security/` is one of the most foundational domain modules of `src/nora/`.

## Architectural Structure

```text
identity_access_security
│
├── Users
│   ├── capability levels
│   ├── identity lifecycle states
│   ├── device trust levels
│   ├── known and anonymous identities
│   ├── linked devices
│   ├── identity attributes
│   ├── identity resolution results
│   ├── identity lifecycle events
│   ├── identity repositories
│   ├── identity lifecycle services
│   └── identity queries
│
├── Authentication
│   ├── authentication methods
│   ├── token types
│   ├── session authentication states
│   ├── credentials and tokens
│   ├── authenticated sessions
│   ├── biometric results
│   ├── trusted device assertions
│   ├── authentication services
│   ├── authentication repositories
│   └── authentication providers
│
├── Authorization
│   ├── roles
│   ├── permission scopes
│   ├── protected resources
│   ├── role and permission definitions
│   ├── access requests
│   ├── access decisions
│   ├── authorization context
│   ├── authorization policies
│   ├── authorization services
│   └── authorization repositories
│
├── User Profile
│   ├── preferred voice settings
│   ├── preferred interface modes
│   ├── preferred feedback styles
│   ├── user profile models
│   ├── user preference models
│   ├── personalization settings
│   ├── linked profile devices
│   ├── profile services
│   └── profile repositories
│
└── Security
    ├── security event types
    ├── threat levels
    ├── incident statuses
    ├── security events
    ├── audit records
    ├── suspicious activity signals
    ├── security incidents
    ├── rate limit decisions
    ├── security services
    ├── security repositories
    └── boundary middleware
```

```
identity_access_security/
├── users/
│   ├── enums/
│   │   ├── user_capability_level_enum.py
│   │   ├── identity_status_enum.py
│   │   └── device_trust_level_enum.py
│   ├── models/
│   │   ├── user_identity.py
│   │   ├── anonymous_identity.py
│   │   ├── linked_device.py
│   │   ├── identity_attributes.py
│   │   └── identity_resolution_result.py
│   ├── events/
│   │   ├── identity_created_event.py
│   │   ├── identity_updated_event.py
│   │   ├── identity_deactivated_event.py
│   │   └── active_user_changed_event.py
│   ├── repositories/
│   │   ├── user_identity_repository.py
│   │   ├── linked_device_repository.py
│   │   └── identity_event_repository.py
│   ├── services/
│   │   ├── create_identity_service.py
│   │   ├── update_identity_service.py
│   │   ├── deactivate_identity_service.py
│   │   ├── delete_identity_service.py
│   │   ├── resolve_identity_service.py
│   │   └── link_device_to_identity_service.py
│   └── queries/
│       ├── get_identity_by_id.py
│       ├── get_identity_by_email.py
│       ├── list_linked_devices.py
│       └── search_identities.py
│
├── authentication/
│   ├── enums/
│   │   ├── authentication_method_enum.py
│   │   ├── token_type_enum.py
│   │   └── session_auth_status_enum.py
│   ├── models/
│   │   ├── login_credentials.py
│   │   ├── authentication_token.py
│   │   ├── refresh_token.py
│   │   ├── active_auth_session.py
│   │   ├── biometric_auth_result.py
│   │   └── trusted_device_assertion.py
│   ├── services/
│   │   ├── credential_authentication_service.py
│   │   ├── token_validation_service.py
│   │   ├── refresh_token_service.py
│   │   ├── biometric_authentication_service.py
│   │   ├── device_authentication_service.py
│   │   ├── proximity_authentication_service.py
│   │   ├── logout_session_service.py
│   │   └── revoke_token_service.py
│   ├── repositories/
│   │   ├── auth_session_repository.py
│   │   └── token_repository.py
│   └── providers/
│       ├── password_hasher_provider.py
│       ├── jwt_token_provider.py
│       └── biometric_match_provider.py
│
├── authorization/
│   ├── enums/
│   │   ├── role_enum.py
│   │   ├── permission_scope_enum.py
│   │   └── protected_resource_enum.py
│   ├── models/
│   │   ├── role_definition.py
│   │   ├── permission_definition.py
│   │   ├── access_request.py
│   │   ├── access_decision.py
│   │   └── authorization_context.py
│   ├── policies/
│   │   ├── role_permission_policy.py
│   │   ├── context_aware_authorization_policy.py
│   │   ├── least_privilege_policy.py
│   │   └── hardware_safety_authorization_policy.py
│   ├── services/
│   │   ├── authorize_action_service.py
│   │   ├── resolve_permission_set_service.py
│   │   ├── assign_role_service.py
│   │   ├── revoke_role_service.py
│   │   └── evaluate_resource_access_service.py
│   └── repositories/
│       ├── role_repository.py
│       ├── permission_repository.py
│       └── role_permission_repository.py
│
├── user_profile/
│   ├── enums/
│   │   ├── preferred_voice_enum.py
│   │   ├── preferred_interface_mode_enum.py
│   │   └── preferred_feedback_style_enum.py
│   ├── models/
│   │   ├── user_profile.py
│   │   ├── user_preferences.py
│   │   ├── personalization_settings.py
│   │   └── linked_profile_device.py
│   ├── services/
│   │   ├── create_user_profile_service.py
│   │   ├── update_user_preferences_service.py
│   │   ├── update_personalization_service.py
│   │   ├── get_effective_profile_settings_service.py
│   │   └── reset_user_preferences_service.py
│   └── repositories/
│       └── user_profile_repository.py
│
└── security/
    ├── enums/
    │   ├── security_event_type_enum.py
    │   ├── threat_level_enum.py
    │   └── incident_status_enum.py
    ├── models/
    │   ├── security_event.py
    │   ├── audit_record.py
    │   ├── suspicious_activity_signal.py
    │   ├── security_incident.py
    │   └── rate_limit_decision.py
    ├── services/
    │   ├── write_audit_record_service.py
    │   ├── detect_suspicious_activity_service.py
    │   ├── register_security_event_service.py
    │   ├── evaluate_rate_limit_service.py
    │   ├── trigger_protective_response_service.py
    │   └── resolve_security_incident_service.py
    ├── repositories/
    │   ├── audit_record_repository.py
    │   ├── security_event_repository.py
    │   └── security_incident_repository.py
    └── middleware/
        ├── authentication_boundary_middleware.py
        ├── authorization_boundary_middleware.py
        ├── rate_limit_middleware.py
        └── request_trace_middleware.py
```

# Interaction Interfaces Module

## Definition

The `interaction_interfaces/` module defines the human and operator-facing access channels through which input enters NORA and through which immediate interaction control signals are expressed.

While other architectural modules define perception, cognition, dialogue, planning, action, persistence, backend behavior, frontend environments, integrations, and hardware structure, those modules do not by themselves define the concrete channels through which a person or operator reaches the system.

That is the role of `interaction_interfaces/`.

In architectural terms, this module defines the structured entry surfaces of NORA.

It is the layer that receives interaction intent from concrete human-access channels such as speech, screens, touch, gestures, proximity credentials, browser actions, and remote operator interfaces, then transforms those channel-specific inputs into normalized interaction events or control signals that the rest of the architecture can understand.

This module therefore defines:

* voice-based interaction entry
* local screen interaction entry
* browser-based frontend interaction entry
* touch and physical control input
* NFC and RFID proximity-based interaction entry
* gesture-based interaction entry
* remote operator and remote client interaction entry
* channel-specific normalization logic
* channel-specific control-signal interpretation
* conversion from raw interface input into structured interaction events

This module is not the same as perception.

Perception transforms raw sensor input into interpreted environmental information.

Interaction interfaces define the intentional channels through which users and operators explicitly interact with the system.

This module is also not the same as dialogue.

Dialogue manages conversational continuity over time.

Interaction interfaces define how interaction first enters the system from specific channels.

For that reason, `interaction_interfaces/` is the channel-boundary module of NORA.

---

## Architectural Purpose

The purpose of the `interaction_interfaces/` module is to make every supported human-access channel explicit, bounded, and structurally normalized.

Without a dedicated interaction-interface module, multi-channel input tends to become scattered across backend routes, hardware drivers, frontend callbacks, perception pipelines, and ad hoc event handlers.

That quickly creates structural problems such as:

* inconsistent treatment of different input channels
* hidden channel-specific assumptions
* duplicated normalization logic
* fragile coupling between concrete interfaces and deeper reasoning layers
* unclear ownership of control signals such as stop, confirm, cancel, or interrupt
* difficulty adding new access channels later
* poor auditability of interaction origin

By introducing a dedicated interaction-interface architecture, NORA gains:

* explicit modeling of all supported interaction channels
* clear normalization boundaries between channel input and system events
* separation between interface capture and deeper semantic reasoning
* safer handling of interruption and emergency control signals
* easier addition of new modalities and interface forms
* consistent representation of channel origin across the system
* clearer interaction tracing and debugging

This module therefore gives NORA a disciplined multi-interface access architecture.

---

## Architectural Role Within the Full System

The `interaction_interfaces/` module sits near the outer boundary of the NORA runtime.

It is one of the first modules involved after raw human interaction occurs.

Its role is not to fully understand the meaning of everything a user does.

Its role is to convert channel-specific input into structured interface events that can then be processed by:

* identity and trust mechanisms
* perception or validation flows when needed
* cognitive control systems
* dialogue systems
* planning systems
* backend coordinators

This means the module acts as a boundary translation layer between:

* concrete user access channels
  and
* channel-agnostic internal interaction representations

It is therefore a normalization layer, a channel-boundary layer, and a control-signal interpretation layer.

---

## Core Architectural Principle

The most important architectural principle of `interaction_interfaces/` is the following:

Each human-access channel should have its own explicit submodule, and each submodule should convert channel-native input into structured interaction events without absorbing responsibilities that belong to dialogue, planning, authentication, or perception.

This means:

* voice interface handles spoken interaction entry, not dialogue management
* local screen interface handles local UI interaction entry, not frontend application rendering
* web frontend interface handles browser-originated commands, not backend business logic
* touch and physical interaction handles tactile or physical control entry, not hardware actuation itself
* NFC and RFID interface handles proximity credential and scan events, not full identity policy ownership
* gesture interface handles gesture-originated commands, not full visual perception ownership
* remote interfaces handle remote-originated operational commands, not all backend administration

This separation preserves architectural clarity.

---

## Internal Module Structure

The proposed structure is the following:

```text
interaction_interfaces/
├── voice_interface/
├── local_screen_interface/
├── web_frontend_interface/
├── touch_and_physical_interaction/
├── nfc_rfid_interface/
├── gesture_interface/
└── remote_interfaces/
```

Each submodule represents a distinct interaction channel or channel family.

This is important because the semantics, timing, trust implications, and control characteristics of these channels are not identical.

A spoken interruption is not the same kind of input as a dashboard request.

A physical stop button is not the same as a web admin action.

An NFC scan is not the same as a gesture recognition result.

By separating channels explicitly, the architecture keeps channel-specific behavior visible and manageable.

---

## Internal Logic Pattern of Each Interface Submodule

Each interaction submodule follows a similar pattern:

```text
submodule/
├── models/
├── services/
└── handlers/
```

This pattern has a specific architectural logic.

### models

Define the structured channel-native input objects, control-signal objects, or interface-context objects.

### services

Define normalization, mapping, validation, or signal-construction logic that translates channel-native input into stable interaction-layer structures.

### handlers

Define concrete bounded entry handlers for important control events or interaction triggers produced by that interface.

This pattern gives each interface submodule:

* structural data definitions
* transformation logic
* bounded entry-point handling

without collapsing everything into a single flat directory.

---

# 1. voice_interface

## Definition

The `voice_interface/` submodule defines the spoken interaction channel of NORA.

Its purpose is to represent and normalize interaction that enters the system through speech-oriented user intent and spoken control signals.

This includes not only general spoken interaction input, but also explicit control utterances such as confirmations, rejections, wake phrase triggers, and interruptions.

This submodule does not own speech recognition itself at the engine level. That belongs to perception and integrations.

Instead, this submodule owns the interaction-boundary representation of spoken input once it is available as an interface event.

### Internal Structure

```text
voice_interface/
├── models/
├── services/
└── handlers/
```

## voice_interface/models/

### spoken_interaction_input.py

Defines the structured representation of spoken input entering the interaction layer.

This model may include:

* recognized utterance content
* source metadata
* language metadata
* timestamp
* speaker context where available
* confidence or recognition metadata
* session or channel context

Architecturally, this model is the primary container for spoken user input as an interaction event candidate.

### spoken_control_signal.py

Defines the structured representation of a spoken control-oriented signal rather than a full conversational utterance.

This may include signals such as:

* confirm
* reject
* cancel
* stop
* interrupt
* wake or reactivate

Its role is important because control signals need to be handled differently from ordinary speech content.

### voice_interaction_context.py

Defines contextual information relevant to interpreting voice interaction at the interface layer.

This may include:

* active session context
* wake-state context
* expected reply context
* active speaker context
* voice channel mode
* interruption sensitivity

Its purpose is to help voice input be interpreted appropriately at the interface boundary before deeper planning or dialogue layers take over.

## voice_interface/services/

### normalize_spoken_interaction_service.py

Defines the operation that normalizes spoken interaction input into a stable internal structure.

Its role may include cleaning metadata, unifying recognition outputs, standardizing timestamps, and preparing channel-consistent spoken input objects.

### build_voice_control_signal_service.py

Defines the operation that converts spoken input or voice-state evidence into a structured spoken control signal when the input represents interaction control rather than free-form conversational content.

Its purpose is to make voice control semantics explicit.

### map_voice_input_to_interaction_event_service.py

Defines the operation that maps normalized spoken input into a system-level interaction event suitable for routing to dialogue, control, identity, or planning layers.

This is one of the key translation points of the voice interface.

## voice_interface/handlers/

### handle_wake_phrase_trigger.py

Defines the bounded handler for wake phrase activation events.

Its role is to react when the system is explicitly invoked through its wake mechanism.

### handle_spoken_confirmation.py

Defines the bounded handler for spoken confirmation signals.

Its purpose is to support fast affirmative control without forcing all confirmations through full dialogue interpretation.

### handle_spoken_rejection.py

Defines the bounded handler for spoken rejection or negative confirmation signals.

Its role is important for clarifications, canceling proposed actions, or rejecting pending choices.

### handle_spoken_interruption.py

Defines the bounded handler for spoken interruption signals.

Its purpose is to allow speech to stop, interrupt, or redirect active behavior safely and promptly.

---

# 2. local_screen_interface

## Definition

The `local_screen_interface/` submodule defines the interaction channel for screens physically associated with the local NORA device or local runtime environment.

Its purpose is to represent direct local visual interaction that occurs through buttons, menus, selections, prompts, and emergency controls on a nearby screen-based interface.

This is distinct from the browser-based frontend because the local screen may be part of the embodied or directly attached interface surface of NORA.

### Internal Structure

```text
local_screen_interface/
├── models/
├── services/
└── handlers/
```

## local_screen_interface/models/

### local_screen_action.py

Defines the structured representation of a direct action taken through the local screen interface.

This may include button presses, command taps, direct control actions, or bounded UI operations.

### local_screen_selection.py

Defines the structured representation of a selection made from local screen content such as menus, lists, prompts, or option grids.

Its role is to distinguish general action input from choice-selection input.

### local_screen_feedback_signal.py

Defines a local screen-oriented feedback signal that may be used to communicate acknowledgment, state changes, or prompt results immediately at the interaction layer.

Its purpose is to support tight local interaction loops.

## local_screen_interface/services/

### normalize_local_screen_action_service.py

Defines the operation that normalizes raw local-screen actions into stable internal action representations.

Its role is to standardize UI-originated action input regardless of concrete widget or physical screen implementation.

### map_local_selection_to_interaction_event_service.py

Defines the operation that translates a screen selection into a system-level interaction event.

Its purpose is to convert UI-local selections into channel-agnostic input events usable by the rest of the system.

### build_local_screen_feedback_service.py

Defines the operation that constructs immediate local-screen feedback payloads or feedback signals associated with local interaction handling.

Its role is especially useful for confirmation, error acknowledgment, or local-state cues.

## local_screen_interface/handlers/

### handle_local_button_press.py

Defines the bounded handler for button-press interactions on the local screen system.

### handle_local_menu_selection.py

Defines the bounded handler for local menu or option-selection interactions.

Its purpose is to convert local selection events into deeper system actions in a controlled way.

### handle_local_emergency_stop.py

Defines the bounded handler for an emergency stop request issued from the local screen interface.

Its role is highly important because locally available stop controls often require higher immediacy and safety priority than ordinary UI events.

---

# 3. web_frontend_interface

## Definition

The `web_frontend_interface/` submodule defines the browser-based interaction channel through which users or operators interact with NORA via the web frontend.

Its purpose is to represent commands, actions, and requests originating from the web application as interface-layer objects before they are routed deeper into the backend or application modules.

This submodule is not the same as the frontend application itself.

The frontend application lives elsewhere.

This submodule exists inside `src/nora/` because the backend still needs a channel-boundary representation of browser-originated interaction.

### Internal Structure

```text
web_frontend_interface/
├── models/
├── services/
└── handlers/
```

## web_frontend_interface/models/

### web_interaction_command.py

Defines the structured representation of a command sent from the web frontend to the interaction layer.

This may include command type, payload, actor context, route context, and UI-origin metadata.

### web_session_action.py

Defines the structured representation of a session-related action originating from the web frontend.

This may include open, resume, rename, switch, or terminate session actions.

### web_dashboard_request.py

Defines the structured representation of a dashboard-oriented data or action request coming from the browser interface.

Its purpose is to make observability, admin, and monitoring requests explicit at the interaction boundary.

## web_frontend_interface/services/

### normalize_web_command_service.py

Defines the operation that normalizes browser-originated commands into stable internal interaction structures.

Its role is to absorb frontend-specific payload variation and produce consistent backend-facing command objects.

### map_web_action_to_interaction_event_service.py

Defines the operation that maps a web-originated action into a system-level interaction event suitable for routing across modules.

### build_web_feedback_payload_service.py

Defines the operation that constructs immediate feedback payloads destined for the web interface in response to interaction processing.

Its role is to support tight browser interaction loops while preserving backend-side channel clarity.

## web_frontend_interface/handlers/

### handle_web_command_submission.py

Defines the bounded handler for general command submission from the web frontend.

### handle_web_project_open_request.py

Defines the bounded handler for requests to open, continue, or focus a project from the browser interface.

Its role is important because project-oriented interaction may be one of the primary browser workflows.

### handle_web_admin_action_request.py

Defines the bounded handler for privileged or administrative action requests originating from the web frontend.

Its purpose is to keep admin-channel browser interactions explicit and controllable.

---

# 4. touch_and_physical_interaction

## Definition

The `touch_and_physical_interaction/` submodule defines interaction signals that arise from tactile controls, physical buttons, and direct physical interruption surfaces.

Its purpose is to model low-latency and often high-priority interaction paths that do not necessarily pass through richer screen or conversational interfaces.

This submodule is important because physical interaction may have stronger immediacy and safety relevance than other channels.

### Internal Structure

```text
touch_and_physical_interaction/
├── models/
├── services/
└── handlers/
```

## touch_and_physical_interaction/models/

### touch_interaction_signal.py

Defines the structured representation of a touch-based interaction signal.

This may include tap, long press, multi-touch pattern, or other tactile interaction primitive depending on hardware capabilities.

### button_press_signal.py

Defines the structured representation of a physical or dedicated button press.

Its purpose is to preserve button-origin semantics independently from general touch events.

### physical_interrupt_signal.py

Defines the structured representation of a physical interruption or stop signal.

Its role is important because such signals often require fast routing and safety-aware handling.

## touch_and_physical_interaction/services/

### normalize_touch_signal_service.py

Defines the operation that normalizes raw touch or button-origin interaction into stable signal structures.

Its purpose is to hide hardware or UI-specific event variation from deeper layers.

### map_touch_signal_to_interaction_event_service.py

Defines the operation that maps normalized touch or physical interaction signals into system-level interaction events.

### validate_physical_interrupt_service.py

Defines the operation that validates and classifies physical interruption requests before they are forwarded as high-priority control events.

Its role is especially important for distinguishing ordinary physical input from emergency or safety-sensitive stop requests.

## touch_and_physical_interaction/handlers/

### handle_touch_confirm_signal.py

Defines the bounded handler for touch-based confirmation signals.

### handle_touch_cancel_signal.py

Defines the bounded handler for touch-based cancellation signals.

### handle_physical_stop_signal.py

Defines the bounded handler for physical stop or interruption input.

Its purpose is to make immediate physical override paths explicit in the architecture.

---

# 5. nfc_rfid_interface

## Definition

The `nfc_rfid_interface/` submodule defines the interaction boundary for proximity-based credential and activation mechanisms such as NFC and RFID.

Its purpose is to represent scans, credential signals, and proximity-based identity or interaction triggers in a structured way.

This submodule is important because proximity interfaces often participate in both interaction and trust flows.

They may:

* trigger identity lookup
* unlock a mode
* signal nearby user presence
* activate a local interaction mode
* contribute to authentication context

For that reason, this interface channel sits close to both interaction and identity concerns while still remaining a distinct boundary module.

### Internal Structure

```text
nfc_rfid_interface/
├── models/
├── services/
└── handlers/
```

## nfc_rfid_interface/models/

### nfc_scan_signal.py

Defines the structured representation of an NFC scan at the interaction boundary.

This may include scanned token identifier, reader metadata, timestamp, and channel context.

### rfid_credential_signal.py

Defines the structured representation of an RFID credential event.

Its role is to make RFID-origin trust or access assertions explicit and separate from generic proximity events.

### proximity_identity_candidate.py

Defines the structured representation of a possible identity candidate inferred from proximity evidence.

Its purpose is to support identity resolution and interaction activation without prematurely claiming full identity certainty.

## nfc_rfid_interface/services/

### normalize_nfc_scan_service.py

Defines the operation that normalizes raw NFC scan input into stable scan objects.

### map_rfid_signal_to_identity_lookup_service.py

Defines the operation that translates an RFID-origin signal into an identity lookup request or identity-candidate resolution input.

Its role is to bridge proximity interaction and identity handling safely.

### build_proximity_interaction_event_service.py

Defines the operation that constructs a structured interaction event from proximity-based activation or scan evidence.

Its purpose is to make proximity-origin interaction explicit at the system boundary.

## nfc_rfid_interface/handlers/

### handle_nfc_identity_scan.py

Defines the bounded handler for NFC scans intended to identify or contextualize the active user.

### handle_rfid_access_signal.py

Defines the bounded handler for RFID-origin access or activation signals.

### handle_proximity_activation_signal.py

Defines the bounded handler for proximity-based interaction activation events.

Its role is to support near-device interaction flows without requiring richer initial input.

---

# 6. gesture_interface

## Definition

The `gesture_interface/` submodule defines the interaction boundary for gesture-based control.

Its purpose is to represent gestures as intentional interaction signals once gesture evidence has already been recognized.

This is distinct from visual perception.

Visual perception detects or infers gestures from visual input.

The gesture interface takes recognized gesture results and treats them as user interaction commands or signals.

That distinction is architecturally important.

### Internal Structure

```text
gesture_interface/
├── models/
├── services/
└── handlers/
```

## gesture_interface/models/

### gesture_interaction_signal.py

Defines the structured representation of a gesture-origin interaction signal.

This may include recognized gesture type, timestamp, confidence, spatial context, and source metadata.

### gesture_control_command.py

Defines the structured representation of a gesture interpreted specifically as a control command.

Its purpose is to make control-oriented gestures explicit rather than treating all gestures as generic interaction.

### gesture_confidence_metadata.py

Defines structured confidence and reliability information attached to gesture-origin signals.

Its role is especially important because gesture input may require stronger ambiguity handling than some other channels.

## gesture_interface/services/

### normalize_gesture_signal_service.py

Defines the operation that normalizes recognized gesture results into stable interaction-layer gesture signals.

### map_gesture_to_interaction_event_service.py

Defines the operation that maps a recognized gesture signal into a system-level interaction event.

### resolve_gesture_control_intent_service.py

Defines the operation that determines whether a recognized gesture should be treated as a control command and, if so, which one.

Its role is important in differentiating expressive gesture presence from actionable control gestures.

## gesture_interface/handlers/

### handle_stop_gesture.py

Defines the bounded handler for stop gestures.

Its role is especially important because gesture-based stop controls may function as quick interruption paths.

### handle_confirm_gesture.py

Defines the bounded handler for confirm or approve gestures.

### handle_pointing_gesture.py

Defines the bounded handler for pointing gestures.

Its role may support selection, object reference, or attention-directing interaction depending on broader system context.

---

# 7. remote_interfaces

## Definition

The `remote_interfaces/` submodule defines the interaction boundary for remote-origin commands and actions issued by operators, clients, or remote systems.

Its purpose is to represent interaction that does not originate from local direct human access surfaces but still enters NORA as intentional control or operational input.

This may include:

* remote administration commands
* remote monitoring requests
* remote client actions
* remote operational control flows

This submodule is important because remote interaction often has different trust, latency, and control semantics than local interaction.

### Internal Structure

```text
remote_interfaces/
├── models/
├── services/
└── handlers/
```

## remote_interfaces/models/

### remote_admin_command.py

Defines the structured representation of a privileged remote administrative command.

Its purpose is to make remote admin actions explicit and auditable at the interaction boundary.

### remote_client_action.py

Defines the structured representation of a general remote-origin client action.

This may include API-like remote requests, remote control actions, or remote workflow triggers.

### remote_interaction_origin.py

Defines the structured representation of the origin characteristics of remote interaction.

This may include source system, client type, trust metadata, location metadata, or transport-origin information.

Its role is to preserve origin-sensitive handling of remote commands.

## remote_interfaces/services/

### normalize_remote_command_service.py

Defines the operation that normalizes remote-origin commands into stable internal interaction structures.

Its purpose is to reduce transport-specific or client-specific variation at the boundary.

### map_remote_action_to_interaction_event_service.py

Defines the operation that maps normalized remote actions into system-level interaction events.

### validate_remote_interaction_context_service.py

Defines the operation that validates whether the remote-origin context is coherent, acceptable, and safe enough for deeper processing.

Its role is especially important because remote channels may require stronger validation of origin assumptions.

## remote_interfaces/handlers/

### handle_remote_admin_command.py

Defines the bounded handler for remote administrative commands.

Its role is to make privileged remote control paths explicit and controllable.

### handle_remote_monitoring_request.py

Defines the bounded handler for remote monitoring or inspection requests.

### handle_remote_client_interaction.py

Defines the bounded handler for general remote client-origin interaction.

Its purpose is to support controlled remote access paths that are not necessarily administrative.

---

## Cross-Channel Architectural Relationships

Although each interaction channel is represented separately, the module as a whole must preserve system-wide consistency.

Several cross-channel relationships are especially important.

### Shared control semantics

Different channels may express the same control intent.

Examples include:

* spoken confirmation
* touch confirmation
* gesture confirmation
* web confirmation action

The channel-specific input differs, but the deeper system intent may converge.

This is why normalization and event mapping are core responsibilities of the module.

### Shared interruption semantics

Multiple channels may express interruption or stop behavior.

Examples include:

* spoken interruption
* physical stop signal
* stop gesture
* local emergency stop
* remote stop command

Because interruption semantics may affect safety or active execution state, the architecture must make these paths explicit.

### Shared origin tracking

Even when interaction intent converges, the system still needs to know where it came from.

A stop gesture, a stop button, and a remote stop command are not operationally identical even if all map to related control semantics.

### Trust-sensitive channels

Some channels sit closer to identity and access behavior than others.

NFC, RFID, remote admin actions, and some web-origin actions may require stronger trust integration than an ordinary local screen selection.

This does not mean they belong in the identity module, but it does mean their interface representations must preserve enough metadata for trust-aware downstream handling.

---

## What This Module Must Not Contain

To preserve architectural clarity, `interaction_interfaces/` should not absorb responsibilities that belong to other modules.

It should not contain:

* speech recognition engines
* wake word detection engines
* face recognition engines
* gesture detection engines
* full dialogue management
* intent classification logic
* planning logic
* authorization policy logic
* frontend rendering logic
* hardware actuation logic
* persistence logic

It may receive outputs from those systems or forward inputs toward them, but it must remain the interaction-channel boundary layer.

---

## Interaction With Other Modules

The `interaction_interfaces/` module interacts with many other parts of NORA.

### shared

Uses shared identifiers, modality values, channel-origin values, timestamps, validation structures, and base exceptions.

### identity_access_security

Passes channel-origin metadata, proximity-derived identity candidates, and remote-origin context into trust and access-related flows where needed.

### perception

Consumes already interpreted perception results in channels such as voice and gesture, without owning raw perception itself.

### cognitive_core

Provides normalized interaction events and control signals that can influence operational state or trigger state transitions.

### dialogue_and_session

Forwards conversational or session-relevant interaction input into dialogue handling and session continuity mechanisms.

### planning_and_agents

Supplies normalized user or operator intent entry events that may later be semantically interpreted and planned over.

### action_and_expression

May receive immediate control-related feedback requirements and may trigger expression acknowledgments or local feedback loops.

### backend_and_application

Integrates with HTTP, websocket, coordinator, and application-service layers that distribute interface-originated interaction events across the runtime.

### frontend_support

Works with frontend-facing payload shaping where interface-origin feedback must be represented cleanly to client applications.

### infrastructure_and_hardware

Depends on physical interface devices such as microphones, local screens, buttons, NFC readers, or gesture-capture hardware, but does not own their low-level hardware modeling.

### observability

Provides origin-aware interaction traces, event context, and debug visibility into how user input entered the system.

---

## Design Constraints of the Module

The `interaction_interfaces/` module should obey several strict design constraints.

### 1. One channel, one boundary

Each interaction channel should remain explicit and structurally separate.

### 2. Normalize early

Channel-specific variation should be reduced early so the deeper system receives stable interaction structures.

### 3. Preserve channel origin

Normalization must not erase the fact that an event came from voice, touch, web, gesture, NFC, or remote interaction.

### 4. Control signals must remain explicit

Stop, cancel, confirm, reject, interrupt, and emergency semantics should not be hidden inside generic free-form interaction content.

### 5. Do not steal perception responsibilities

If a channel depends on recognition from raw sensory input, that recognition belongs upstream in perception or integration layers.

### 6. Do not steal dialogue or planning responsibilities

This module should forward normalized interaction events into deeper reasoning layers rather than becoming a miniature reasoning engine.

### 7. Safety-sensitive controls require visibility

Emergency and interruption paths must remain visible, bounded, and high-priority in the architecture.

---

## Testing Implications

Because this module sits at the channel boundary, it has strong validation importance.

Important testing categories include:

* voice normalization tests
* spoken control-signal mapping tests
* local screen action mapping tests
* local emergency stop tests
* web command normalization tests
* remote-origin validation tests
* touch and button signal tests
* NFC and RFID scan normalization tests
* proximity-activation tests
* gesture confidence handling tests
* stop and interrupt path tests across channels
* channel-origin preservation tests
* interaction event mapping consistency tests

Errors in this module can propagate widely because they change how the rest of the system interprets incoming interaction.

---

## Why This Structure Fits NORA

This structure fits NORA because NORA is intentionally multi-interface.

It is not limited to one access form.

It may be used through:

* spoken interaction
* local physical or screen controls
* browser-based interfaces
* proximity interactions
* gesture-based controls
* remote operational channels

A unified but undifferentiated input layer would not preserve the different semantics, trust needs, and control properties of those channels.

The proposed structure allows NORA to:

* support multiple channels simultaneously
* preserve origin-aware behavior
* normalize input consistently
* keep safety-critical paths explicit
* add new channels later without destabilizing existing ones

That makes it a strong fit for the architecture of NORA.

---

## Architectural Importance

The `interaction_interfaces/` module provides the structured human and operator access surface through which interaction enters the NORA system.

While other modules define perception, dialogue, planning, action, persistence, and runtime control, those modules depend on a dedicated interface-boundary layer that receives input from real channels such as voice, screens, touch, proximity, gesture, web interfaces, and remote control surfaces.

Through this module the architecture gains:

* explicit modeling of all supported interaction channels
* clear separation between channel-specific input and deeper reasoning layers
* structured normalization of user and operator input
* origin-aware control of confirmations, cancellations, interruptions, and stop signals
* safer handling of emergency and high-priority interaction controls
* cleaner expansion path for future access channels

By separating voice, local screen, web, touch, proximity, gesture, and remote interaction into explicit submodules, NORA preserves channel clarity while still converging those inputs into coherent system-level interaction events.

For that reason, `interaction_interfaces/` is a foundational domain module of `src/nora/`.

## Architectural Structure

```text
interaction_interfaces
│
├── Voice Interface
│   ├── spoken interaction inputs
│   ├── spoken control signals
│   ├── voice interaction context
│   ├── normalization services
│   ├── control-signal construction services
│   ├── interaction-event mapping services
│   └── spoken control handlers
│
├── Local Screen Interface
│   ├── local actions
│   ├── local selections
│   ├── local feedback signals
│   ├── normalization services
│   ├── selection-to-event mapping services
│   ├── local feedback construction services
│   └── local interaction handlers
│
├── Web Frontend Interface
│   ├── web interaction commands
│   ├── web session actions
│   ├── web dashboard requests
│   ├── web command normalization services
│   ├── action-to-event mapping services
│   ├── web feedback payload builders
│   └── web interaction handlers
│
├── Touch and Physical Interaction
│   ├── touch interaction signals
│   ├── button press signals
│   ├── physical interrupt signals
│   ├── touch normalization services
│   ├── signal-to-event mapping services
│   ├── interrupt validation services
│   └── tactile and physical handlers
│
├── NFC and RFID Interface
│   ├── NFC scan signals
│   ├── RFID credential signals
│   ├── proximity identity candidates
│   ├── scan normalization services
│   ├── identity lookup mapping services
│   ├── proximity event builders
│   └── proximity handlers
│
├── Gesture Interface
│   ├── gesture interaction signals
│   ├── gesture control commands
│   ├── gesture confidence metadata
│   ├── gesture normalization services
│   ├── gesture-to-event mapping services
│   ├── control-intent resolution services
│   └── gesture handlers
│
└── Remote Interfaces
    ├── remote admin commands
    ├── remote client actions
    ├── remote interaction origin metadata
    ├── remote normalization services
    ├── remote action-to-event mapping services
    ├── remote context validation services
    └── remote interaction handlers
```

```
interaction_interfaces/
├── voice_interface/
│   ├── models/
│   │   ├── spoken_interaction_input.py
│   │   ├── spoken_control_signal.py
│   │   └── voice_interaction_context.py
│   ├── services/
│   │   ├── normalize_spoken_interaction_service.py
│   │   ├── build_voice_control_signal_service.py
│   │   └── map_voice_input_to_interaction_event_service.py
│   └── handlers/
│       ├── handle_wake_phrase_trigger.py
│       ├── handle_spoken_confirmation.py
│       ├── handle_spoken_rejection.py
│       └── handle_spoken_interruption.py
│
├── local_screen_interface/
│   ├── models/
│   │   ├── local_screen_action.py
│   │   ├── local_screen_selection.py
│   │   └── local_screen_feedback_signal.py
│   ├── services/
│   │   ├── normalize_local_screen_action_service.py
│   │   ├── map_local_selection_to_interaction_event_service.py
│   │   └── build_local_screen_feedback_service.py
│   └── handlers/
│       ├── handle_local_button_press.py
│       ├── handle_local_menu_selection.py
│       └── handle_local_emergency_stop.py
│
├── web_frontend_interface/
│   ├── models/
│   │   ├── web_interaction_command.py
│   │   ├── web_session_action.py
│   │   └── web_dashboard_request.py
│   ├── services/
│   │   ├── normalize_web_command_service.py
│   │   ├── map_web_action_to_interaction_event_service.py
│   │   └── build_web_feedback_payload_service.py
│   └── handlers/
│       ├── handle_web_command_submission.py
│       ├── handle_web_project_open_request.py
│       └── handle_web_admin_action_request.py
│
├── touch_and_physical_interaction/
│   ├── models/
│   │   ├── touch_interaction_signal.py
│   │   ├── button_press_signal.py
│   │   └── physical_interrupt_signal.py
│   ├── services/
│   │   ├── normalize_touch_signal_service.py
│   │   ├── map_touch_signal_to_interaction_event_service.py
│   │   └── validate_physical_interrupt_service.py
│   └── handlers/
│       ├── handle_touch_confirm_signal.py
│       ├── handle_touch_cancel_signal.py
│       └── handle_physical_stop_signal.py
│
├── nfc_rfid_interface/
│   ├── models/
│   │   ├── nfc_scan_signal.py
│   │   ├── rfid_credential_signal.py
│   │   └── proximity_identity_candidate.py
│   ├── services/
│   │   ├── normalize_nfc_scan_service.py
│   │   ├── map_rfid_signal_to_identity_lookup_service.py
│   │   └── build_proximity_interaction_event_service.py
│   └── handlers/
│       ├── handle_nfc_identity_scan.py
│       ├── handle_rfid_access_signal.py
│       └── handle_proximity_activation_signal.py
│
├── gesture_interface/
│   ├── models/
│   │   ├── gesture_interaction_signal.py
│   │   ├── gesture_control_command.py
│   │   └── gesture_confidence_metadata.py
│   ├── services/
│   │   ├── normalize_gesture_signal_service.py
│   │   ├── map_gesture_to_interaction_event_service.py
│   │   └── resolve_gesture_control_intent_service.py
│   └── handlers/
│       ├── handle_stop_gesture.py
│       ├── handle_confirm_gesture.py
│       └── handle_pointing_gesture.py
│
└── remote_interfaces/
    ├── models/
    │   ├── remote_admin_command.py
    │   ├── remote_client_action.py
    │   └── remote_interaction_origin.py
    ├── services/
    │   ├── normalize_remote_command_service.py
    │   ├── map_remote_action_to_interaction_event_service.py
    │   └── validate_remote_interaction_context_service.py
    └── handlers/
        ├── handle_remote_admin_command.py
        ├── handle_remote_monitoring_request.py
        └── handle_remote_client_interaction.py
```

# Perception Module

## Definition

The `perception/` module defines how NORA acquires, normalizes, interprets, and transforms signals from the surrounding environment into structured internal representations that the rest of the system can use.

While other architectural modules define identity, interaction channels, cognition, dialogue, planning, action, persistence, backend behavior, integrations, hardware structure, and observability, those modules depend on a dedicated subsystem capable of answering a more basic question:

What is happening in the environment around the system right now?

That is the role of `perception/`.

In architectural terms, the perception module is the environmental interpretation layer of NORA.

It is the module that converts raw or semi-raw incoming sensory information into meaningful perceptual outputs such as:

* spoken content
* wake-word activations
* speaker identity candidates
* environmental sound detections
* faces and facial identity candidates
* recognized gestures
* pose estimates
* detected objects
* scene interpretations
* motion and proximity states
* ambient environmental conditions
* fused multimodal context
* perception events routed toward the rest of the architecture

This module therefore defines:

* sensor abstraction
* input acquisition normalization
* preprocessing pipelines
* feature extraction stages
* interpretation stages
* event generation from perceptual results
* multimodal fusion logic
* downstream routing of perception events

The perception module is not the same as the interaction interface layer.

Interaction interfaces describe intentional access channels through which users and operators explicitly communicate with NORA.

Perception describes how the system senses and interprets its environment, whether or not that environment is explicitly trying to communicate.

The perception module is also not the same as planning or dialogue.

Perception produces environmental understanding.

Planning decides what to do about that understanding.

Dialogue decides how conversational continuity should evolve in response to it.

For that reason, `perception/` is one of the most foundational domain modules in NORA.

---

## Architectural Purpose

The purpose of the `perception/` module is to provide NORA with a structured, modular, and extensible sensory interpretation architecture.

Without a dedicated perception module, raw inputs from microphones, cameras, proximity sources, and environmental sensors would either remain low-level and unusable or become interpreted in fragmented, inconsistent, and tightly coupled ways across the system.

That would create severe architectural problems such as:

* inconsistent treatment of sensor data
* hidden coupling between hardware drivers and higher-level behavior
* mixed responsibilities between acquisition, preprocessing, and meaning extraction
* difficulty debugging perceptual failures
* poor extensibility when new sensors or interpretations are added
* weak confidence handling across modalities
* inability to combine multiple sensor sources coherently
* unclear routing from perception outputs into cognition, identity, or dialogue

By introducing a dedicated and internally structured perception module, NORA gains:

* explicit sensor abstraction boundaries
* modular preprocessing and feature extraction stages
* explicit interpretation layers per modality
* structured perception events
* multimodal fusion support
* clear separation between raw sensing and semantic use
* better debuggability and extensibility
* consistent downstream routing of perceptual results

This module therefore gives NORA a proper sensory architecture rather than a collection of ad hoc input-processing routines.

---

## Core Architectural Principle

The most important design principle of the perception module is this:

Perception must be separated into acquisition, preprocessing, feature extraction, interpretation, event generation, and downstream routing.

This means perception is not a single monolithic pipeline.

It is a layered architecture in which each stage has a distinct role.

### Acquisition

Raw or standardized sensor signals enter the system.

### Preprocessing

Signals are cleaned, aligned, normalized, or reduced to a stable working form.

### Feature extraction

Relevant structured features are derived from the processed signal.

### Interpretation

Features are transformed into meaningful perceptual results.

### Event generation

Perceptual results are converted into explicit internal events.

### Downstream routing

Perception events are distributed toward the modules that need them.

This separation is essential because perception quality depends not only on algorithms, but on architectural clarity.

---

## Internal Module Structure

The proposed structure is the following:

```text
perception/
├── sensor_abstraction/
├── audio_perception/
├── visual_perception/
├── environmental_sensors/
├── sensor_fusion/
└── perception_event_processing/
```

This structure divides the perception architecture into six major areas.

### sensor_abstraction

Defines how sensor outputs are represented and standardized before modality-specific perception begins.

### audio_perception

Defines the full perception flow for sound and speech-related input.

### visual_perception

Defines the full perception flow for camera-based visual input.

### environmental_sensors

Defines perception over non-audio, non-visual environmental sensor readings.

### sensor_fusion

Defines how outputs from multiple perceptual channels are combined into unified perceptual conclusions.

### perception_event_processing

Defines how perceptual results become normalized internal events and how they are routed to other modules.

This decomposition is important because perception is both modality-specific and system-wide.

Some concerns belong to particular sensory channels. Others exist only after multiple channels are combined.

---

## Architectural Role Within the Full System

The `perception/` module sits near the outer edge of the system, but slightly deeper than raw hardware or low-level interfaces.

Its role is to stand between:

* physical or sensor-level reality
  and
* internal system reasoning

It does not own the hardware itself. That belongs to infrastructure and hardware.

It does not own the user-facing interface channels. That belongs to interaction interfaces.

It does not decide what the system should do about perceptual information. That belongs to cognition, dialogue, planning, and action.

Its role is to transform sensed reality into structured internal knowledge about the current environment.

---

# 1. sensor_abstraction

## Definition

The `sensor_abstraction/` submodule defines how heterogeneous sensor sources are represented, standardized, calibrated, temporally aligned, and buffered before higher-level modality-specific perception consumes them.

Its purpose is to prevent each modality pipeline from depending directly on raw hardware-specific signal formats.

This submodule therefore provides a shared abstraction boundary between physical sensing infrastructure and perception pipelines.

### Internal Structure

```text
sensor_abstraction/
├── models/
├── services/
└── providers/
```

## sensor_abstraction/models/

### sensor_descriptor.py

Defines the structured description of a sensor known to the system.

This model may include:

* sensor identifier
* sensor type
* modality classification
* source device metadata
* sampling characteristics
* calibration references
* operational capabilities

Architecturally, this model provides a consistent way to describe sensors across modalities.

### sensor_reading.py

Defines the structured representation of a raw or minimally standardized reading from a sensor.

Its purpose is to provide a common abstraction for incoming signal data regardless of concrete sensor implementation.

### synchronized_sensor_frame.py

Defines a temporally aligned bundle of readings from one or more sensors.

Its role is especially important when multimodal perception depends on time consistency between channels.

### calibration_profile.py

Defines the structured representation of calibration data used to correct or standardize sensor outputs.

This may include offsets, scaling factors, alignment metadata, and modality-specific calibration parameters.

## sensor_abstraction/services/

### standardize_sensor_output_service.py

Defines the operation that converts raw sensor outputs into stable internal reading structures.

Its role is to absorb low-level source heterogeneity and present a consistent input boundary to perception pipelines.

### align_sensor_timestamps_service.py

Defines the operation that aligns timestamps across readings from different sensors.

Its purpose is to support synchronized multimodal interpretation.

### apply_sensor_calibration_service.py

Defines the operation that applies calibration profiles to raw or standardized sensor readings.

Its role is to make sensor output more physically or operationally reliable before interpretation proceeds.

### buffer_sensor_signal_service.py

Defines the operation that stores sensor output in a bounded buffer for temporal processing, smoothing, windowing, or delayed fusion.

Its purpose is to support streaming and time-aware perception.

## sensor_abstraction/providers/

### microphone_sensor_provider.py

Defines the provider boundary through which microphone-origin sensor output is obtained.

Its role is not high-level speech interpretation, but provision of audio sensor data in a form usable by perception.

### camera_sensor_provider.py

Defines the provider boundary through which camera-origin visual frames are obtained for perception.

### proximity_sensor_provider.py

Defines the provider boundary through which proximity-related sensor readings are obtained.

Its role may support presence detection, range threshold behavior, or identity-adjacent context cues.

### environmental_sensor_provider.py

Defines the provider boundary through which environmental condition readings such as temperature, humidity, or light level are obtained.

### tactile_sensor_provider.py

Defines the provider boundary through which tactile or contact-oriented sensor data is obtained when relevant to perception.

---

# 2. audio_perception

## Definition

The `audio_perception/` submodule defines the full perceptual pipeline for audio-based sensing.

Its purpose is to interpret sound arriving through microphones and transform it into meaningful results such as:

* speech segments
* wake-word detections
* recognized speech content
* speaker identity candidates
* environmental sound detections

This submodule is a complete perception stack for audio, divided into models, preprocessing, feature extraction, interpretation, events, and pipeline orchestration.

### Internal Structure

```text
audio_perception/
├── models/
├── preprocessing/
├── feature_extraction/
├── interpretation/
├── events/
└── pipeline/
```

## audio_perception/models/

### audio_stream_chunk.py

Defines the structured representation of a bounded chunk of audio stream data used during processing.

Its purpose is to give the audio pipeline a stable working unit for streaming analysis.

### speech_segment.py

Defines a bounded segment of audio believed to contain speech activity.

Its role is important because many later audio tasks operate on speech-containing windows rather than raw continuous stream data.

### wake_word_detection_result.py

Defines the structured result of wake-word detection.

This may include detected phrase, confidence, timestamp, segment reference, and source metadata.

### speech_recognition_result.py

Defines the structured result of speech-to-text interpretation.

This may include recognized text, confidence, language, timing boundaries, and recognition metadata.

### speaker_identification_result.py

Defines the structured result of speaker identification or speaker matching.

Its purpose is to represent candidate speaker identity information derived from voice characteristics.

### environmental_sound_detection_result.py

Defines the structured result of detecting meaningful non-speech sounds in the environment.

This may include alarms, knocks, doors, machine sounds, or other relevant events.

## audio_perception/preprocessing/

### audio_noise_reduction_service.py

Defines the operation that reduces unwanted noise from incoming audio signals before higher-level analysis.

Its purpose is to improve robustness of downstream detection and interpretation.

### audio_signal_normalization_service.py

Defines the operation that normalizes the signal characteristics of incoming audio.

This may include amplitude normalization, dynamic range handling, or standardization of channel formats.

### audio_channel_alignment_service.py

Defines the operation that aligns channels or microphone sources in multi-channel audio setups.

Its role is important for coherent downstream processing in multi-microphone environments.

## audio_perception/feature_extraction/

### speech_activity_feature_extractor.py

Defines the operation that extracts features relevant to speech-activity detection or segmentation.

Its role is to separate speech-bearing regions from silence or non-speech sound.

### speaker_voice_feature_extractor.py

Defines the operation that extracts voice-characteristic features useful for speaker identification.

### sound_event_feature_extractor.py

Defines the operation that extracts features relevant to environmental sound classification or detection.

## audio_perception/interpretation/

### wake_word_interpreter.py

Defines the interpretation logic that determines whether a wake phrase has been detected.

Its purpose is to convert audio features or provider outputs into structured wake-word results.

### speech_to_text_interpreter.py

Defines the interpretation logic that produces recognized speech content from audio input or speech segments.

### speaker_identity_interpreter.py

Defines the interpretation logic that resolves speaker identity candidates or speaker matches from extracted voice features.

### sound_event_interpreter.py

Defines the interpretation logic that classifies or identifies non-speech sound events in the environment.

## audio_perception/events/

### wake_word_detected_event.py

Defines the internal event emitted when a wake word is detected.

### speech_recognized_event.py

Defines the internal event emitted when speech is recognized as text.

### speaker_identified_event.py

Defines the internal event emitted when a speaker identity candidate or match is produced.

### environmental_sound_detected_event.py

Defines the internal event emitted when a relevant environmental sound is detected.

## audio_perception/pipeline/

### run_audio_perception_pipeline.py

Defines the orchestration entry point for the audio perception pipeline.

Its purpose is to coordinate preprocessing, feature extraction, interpretation, and event production for audio input.

---

# 3. visual_perception

## Definition

The `visual_perception/` submodule defines the full perception stack for camera-based visual input.

Its purpose is to transform video frames into meaningful visual interpretations such as:

* detected faces
* facial identity candidates
* recognized gestures
* pose estimates
* detected objects
* scene understanding results

This submodule mirrors the layered logic of audio perception but applies it to visual input.

### Internal Structure

```text
visual_perception/
├── models/
├── preprocessing/
├── feature_extraction/
├── interpretation/
├── events/
└── pipeline/
```

## visual_perception/models/

### video_frame.py

Defines the structured representation of a visual frame used in perception processing.

Its role is to provide a stable input unit for frame-based or sequence-based visual analysis.

### detected_face.py

Defines the structured representation of a face detected in a frame.

This may include spatial bounds, confidence, landmarks, and frame references.

### facial_identity_result.py

Defines the structured result of attempting to identify or match a face to a known identity.

### detected_gesture.py

Defines the structured representation of a recognized gesture in visual input.

Its purpose is to separate gesture perception output from later gesture-interface semantics.

### pose_estimation_result.py

Defines the structured representation of inferred body pose or pose landmarks.

### detected_object.py

Defines the structured representation of an object detected in the scene.

### scene_understanding_result.py

Defines the structured representation of broader interpreted scene meaning.

This may include scene category, salient entities, spatial context, or activity cues.

## visual_perception/preprocessing/

### image_resize_service.py

Defines the operation that resizes frames into forms suitable for downstream visual processing.

### image_normalization_service.py

Defines the operation that normalizes image values, formats, or channel behavior prior to feature extraction.

### image_frame_sampling_service.py

Defines the operation that samples frames from a visual stream according to configured rate or relevance criteria.

Its purpose is to control processing load and temporal resolution.

## visual_perception/feature_extraction/

### facial_feature_extractor.py

Defines the operation that extracts facial features used for detection or recognition.

### pose_feature_extractor.py

Defines the operation that extracts pose-related features from visual frames.

### gesture_feature_extractor.py

Defines the operation that extracts features relevant to gesture recognition.

### object_feature_extractor.py

Defines the operation that extracts features relevant to object detection or classification.

## visual_perception/interpretation/

### face_detection_interpreter.py

Defines the interpretation logic that resolves whether and where faces are present in visual input.

### face_recognition_interpreter.py

Defines the interpretation logic that produces facial identity candidates from detected facial features.

### gesture_recognition_interpreter.py

Defines the interpretation logic that converts gesture-related features into recognized gesture results.

### pose_estimation_interpreter.py

Defines the interpretation logic that produces pose estimation results.

### object_detection_interpreter.py

Defines the interpretation logic that produces object detections.

### scene_understanding_interpreter.py

Defines the interpretation logic that derives broader scene context or scene meaning from visual input.

## visual_perception/events/

### face_detected_event.py

Defines the internal event emitted when one or more faces are detected.

### face_identified_event.py

Defines the internal event emitted when a facial identity result is produced.

### gesture_recognized_event.py

Defines the internal event emitted when a gesture is recognized visually.

### pose_estimated_event.py

Defines the internal event emitted when a pose estimate is produced.

### object_detected_event.py

Defines the internal event emitted when a relevant object is detected.

### scene_understood_event.py

Defines the internal event emitted when a scene understanding result is produced.

## visual_perception/pipeline/

### run_visual_perception_pipeline.py

Defines the orchestration entry point for the visual perception pipeline.

Its purpose is to coordinate frame preparation, feature extraction, interpretation, and event generation over camera-origin input.

---

# 4. environmental_sensors

## Definition

The `environmental_sensors/` submodule defines perception over non-audio, non-visual environmental sensor readings.

Its purpose is to transform structured environmental measurements into meaningful environmental state conclusions.

This may include:

* temperature state
* humidity state
* ambient light state
* motion state
* proximity state
* presence-related environmental cues

This submodule matters because not all useful perception is audio or visual.

Simple environmental sensors may be critical to context awareness, safety, and interaction readiness.

### Internal Structure

```text
environmental_sensors/
├── models/
├── interpretation/
├── events/
└── pipeline/
```

## environmental_sensors/models/

### temperature_reading.py

Defines the structured representation of a temperature reading.

### humidity_reading.py

Defines the structured representation of a humidity reading.

### light_level_reading.py

Defines the structured representation of an ambient light reading.

### motion_detection_signal.py

Defines the structured representation of a motion-related sensor signal.

### proximity_reading.py

Defines the structured representation of a proximity reading.

### environmental_state_snapshot.py

Defines a structured snapshot of interpreted or partially interpreted environmental conditions at a moment in time.

Its purpose is to provide a coherent environmental context object rather than scattered sensor values.

## environmental_sensors/interpretation/

### ambient_light_interpreter.py

Defines the interpretation logic that translates light readings into meaningful light-state conclusions.

### motion_state_interpreter.py

Defines the interpretation logic that translates motion signals into motion-state conclusions.

### presence_interpreter.py

Defines the interpretation logic that infers presence-related conclusions from environmental sensor evidence.

### temperature_state_interpreter.py

Defines the interpretation logic that classifies or interprets temperature state.

### humidity_state_interpreter.py

Defines the interpretation logic that classifies or interprets humidity state.

## environmental_sensors/events/

### motion_detected_event.py

Defines the internal event emitted when meaningful motion is detected.

### proximity_threshold_reached_event.py

Defines the internal event emitted when proximity readings cross a configured or meaningful threshold.

### ambient_light_state_changed_event.py

Defines the internal event emitted when interpreted light state changes.

### temperature_state_changed_event.py

Defines the internal event emitted when interpreted temperature state changes.

### humidity_state_changed_event.py

Defines the internal event emitted when interpreted humidity state changes.

## environmental_sensors/pipeline/

### run_environmental_perception_pipeline.py

Defines the orchestration entry point for environmental-sensor perception.

Its purpose is to coordinate interpretation and event generation over low-bandwidth environmental sensor inputs.

---

# 5. sensor_fusion

## Definition

The `sensor_fusion/` submodule defines how outputs from multiple perception channels are combined into richer, more reliable, and more context-aware perceptual conclusions.

Its purpose is to move beyond isolated modality outputs and create unified interpretation where multiple signals together support a stronger inference.

This may include:

* fused presence conclusions
* fused user identity candidates
* fused scene context
* fused interaction context

Sensor fusion is important because many real-world conclusions are not best derived from only one signal source.

### Internal Structure

```text
sensor_fusion/
├── models/
├── services/
└── events/
```

## sensor_fusion/models/

### fused_presence_result.py

Defines the structured result of combining multiple presence-related signals into one presence conclusion.

Its purpose is to produce a more reliable answer to whether someone is present.

### fused_user_identity_candidate.py

Defines the structured result of combining multiple identity-relevant signals into a user identity candidate.

This may combine face, voice, proximity, or device-origin evidence.

### fused_scene_context.py

Defines a structured multimodal scene context derived from multiple perceptual channels.

Its role is to provide a richer situational understanding than any one modality alone.

### fused_interaction_context.py

Defines a structured context object representing fused interaction-relevant perception across modalities.

Its purpose is especially useful when downstream dialogue or cognition needs a unified interaction situation model.

## sensor_fusion/services/

### fuse_presence_signals_service.py

Defines the operation that combines multiple presence-related perceptual signals into one fused presence result.

### fuse_identity_candidates_service.py

Defines the operation that combines multiple identity candidates or identity clues into a stronger fused identity candidate.

Its role is especially important in embodied systems where identity may be inferred from multiple weak signals.

### fuse_multimodal_context_service.py

Defines the operation that combines multiple perceptual outputs into a broader multimodal context representation.

### resolve_fused_perception_result_service.py

Defines the operation that resolves, ranks, or finalizes the fused perceptual outcome that should be exposed downstream.

## sensor_fusion/events/

### fused_presence_detected_event.py

Defines the internal event emitted when a fused presence conclusion is produced.

### fused_identity_candidate_event.py

Defines the internal event emitted when a fused identity candidate is produced.

### fused_context_updated_event.py

Defines the internal event emitted when multimodal fused context changes or is updated.

---

# 6. perception_event_processing

## Definition

The `perception_event_processing/` submodule defines how perceptual outputs become normalized internal events and how those events are published, stored selectively, and routed toward the modules that need them.

Its purpose is to separate modality-specific interpretation from system-wide event semantics.

Without this layer, perception results would remain trapped inside submodule-local structures or be distributed in inconsistent ways.

This submodule therefore acts as the bridge between perceptual conclusion and system integration.

### Internal Structure

```text
perception_event_processing/
├── models/
├── services/
└── routing/
```

## perception_event_processing/models/

### perception_event_envelope.py

Defines the outer structured container for perception events before or during publication.

This may include source modality, event type, timestamp, payload, correlation data, and routing metadata.

### normalized_perception_event.py

Defines the normalized internal representation of a perception event after modality-specific results have been translated into the shared event form expected by downstream modules.

### perception_confidence_metadata.py

Defines structured confidence metadata attached to perception events.

Its role is important because downstream modules may need to reason about uncertainty, ambiguity, or reliability.

## perception_event_processing/services/

### normalize_perception_result_service.py

Defines the operation that converts modality-specific perception results into normalized perception-event structures.

### build_perception_event_service.py

Defines the operation that constructs fully formed perception events ready for publication or routing.

### publish_perception_event_service.py

Defines the operation that publishes normalized perception events into the wider system event infrastructure.

### store_selected_perception_result_service.py

Defines the operation that selectively persists perception results or perception-event data when storage is required for history, debugging, or later reasoning.

## perception_event_processing/routing/

### route_perception_event_to_fsm.py

Defines the routing logic that forwards relevant perception events to the finite-state control layer.

Its purpose is to allow environmental signals to affect operational state.

### route_perception_event_to_dialogue.py

Defines the routing logic that forwards perception events relevant to dialogue or conversational interpretation.

Its role is important when perceived speech, presence, interruption, or identity cues affect ongoing dialogue handling.

### route_perception_event_to_identity.py

Defines the routing logic that forwards perception events relevant to identity resolution or trust-related context.

Its purpose is especially important for voice, face, or proximity-derived identity signals.

---

## Cross-Submodule Architectural Flow

The full architectural flow of the perception module can be understood as follows:

1. Sensors are abstracted and standardized.
2. Modality-specific pipelines process audio, visual, and environmental input.
3. Interpretation results are produced within each modality.
4. Multimodal fusion combines related outputs where useful.
5. Perception event processing normalizes and publishes the resulting information.
6. Downstream modules receive perception-derived events according to their needs.

This means the module is not merely a set of disconnected perception tools.

It is a structured perception architecture with clear internal progression from sensing to eventful system knowledge.

---

## What This Module Must Not Contain

To preserve architectural clarity, the perception module should not absorb responsibilities that belong elsewhere.

It should not contain:

* frontend interaction handling
* dialogue management logic
* intent classification logic
* planning logic
* authorization policy logic
* hardware device registration ownership
* final action execution logic
* profile personalization logic

It may produce inputs relevant to those modules, but it must remain the sensory interpretation layer.

---

## Interaction With Other Modules

The `perception/` module interacts with many other parts of NORA.

### shared

Uses shared identifiers, modality information, timestamps, exceptions, confidence-support structures, and generic models.

### interaction_interfaces

Provides perception results that may later become intentional interaction signals in channels such as voice or gesture once recognized.

### identity_access_security

Supplies identity-relevant perception such as face matches, speaker matches, or proximity clues for downstream identity resolution or trust-aware handling.

### cognitive_core

Supplies environmental and interaction-relevant perception events that may influence runtime state or control decisions.

### dialogue_and_session

Supplies speech recognition results, interruption cues, user presence cues, or identity-related perception that may affect dialogue continuity.

### planning_and_agents

Supplies interpreted environmental context that may shape task planning, ambiguity resolution, or situational reasoning.

### action_and_expression

May indirectly influence action triggering when perception events lead to action decisions elsewhere in the system.

### persistence_and_memory

May store selected perceptual results, histories, or traces for debugging, audit, replay, or memory purposes.

### backend_and_application

Publishes perception-derived events into coordinators, event buses, and application services for runtime distribution.

### integrations_and_external_services

Depends on external engines for speech recognition, vision inference, OCR, or other perceptual capabilities, while owning the perception semantics above those engines.

### infrastructure_and_hardware

Depends on sensors and device interfaces provided by the hardware layer, while remaining above the hardware modeling boundary.

### observability

Provides traceable perception events, confidence metadata, and pipeline visibility for diagnostics and monitoring.

---

## Design Constraints of the Module

The `perception/` module should obey several strict design constraints.

### 1. Preserve layered perception stages

Acquisition, preprocessing, feature extraction, interpretation, event generation, and routing should remain structurally distinct.

### 2. Keep modality-specific logic local

Audio-specific and visual-specific interpretation should not be mixed into one undifferentiated pipeline.

### 3. Fusion happens after interpretation, not instead of it

Sensor fusion should combine meaningful modality outputs, not replace modality-specific processing.

### 4. Confidence must remain explicit

Perception is inherently uncertain.

Confidence, ambiguity, and reliability metadata must remain visible in outputs.

### 5. Hardware abstraction should remain below perception semantics

Perception should use sensor abstractions, not depend directly on hardware-specific details everywhere.

### 6. Downstream routing must remain explicit

Perception should not invisibly mutate deeper system state.

Relevant perception outputs should become explicit events routed through controlled paths.

### 7. Do not collapse perception into interaction

A recognized voice command may later become an interaction event, but raw audio interpretation still belongs to perception first.

---

## Testing Implications

Because perception is layered and uncertainty-heavy, it requires especially strong structural testing.

Important testing categories include:

* sensor standardization tests
* timestamp alignment tests
* calibration application tests
* buffering and streaming tests
* audio preprocessing tests
* speech segmentation tests
* wake-word interpretation tests
* speech recognition result mapping tests
* speaker-identification output tests
* environmental sound detection tests
* visual preprocessing tests
* face detection and face-recognition tests
* gesture-recognition tests
* pose-estimation tests
* object-detection tests
* scene-understanding tests
* environmental sensor interpretation tests
* multimodal fusion tests
* confidence propagation tests
* perception event normalization tests
* downstream routing tests to FSM, dialogue, and identity

Failures in this module can distort everything downstream because perception changes what the system believes about reality.

---

## Why This Structure Fits NORA

This structure fits NORA because NORA is a multimodal and environment-aware system.

It needs to interpret:

* audio
* visual scenes
* environmental conditions
* user presence
* identity-related sensory cues
* multimodal interaction context

A flatter or less layered design would make it much harder to preserve signal-processing clarity, modality separation, and downstream event consistency.

The proposed structure allows NORA to:

* support multiple perception channels coherently
* keep sensor handling modular
* separate preprocessing from interpretation
* fuse modalities only when appropriate
* route perceptual conclusions safely into the rest of the architecture

That makes it an excellent fit for the system.

---

## Architectural Importance

The `perception/` module provides the sensory interpretation foundation through which NORA becomes aware of its environment.

While other modules define interaction, cognition, dialogue, planning, action, persistence, backend behavior, and integrations, those modules all depend on a dedicated architecture that can acquire signals from the world, preprocess them, extract meaningful features, interpret those features into perceptual conclusions, and expose the resulting knowledge to the rest of the system in structured form.

Through this module the architecture gains:

* explicit sensor abstraction boundaries
* modular audio, visual, and environmental perception pipelines
* separation between preprocessing, feature extraction, and interpretation
* multimodal fusion capabilities
* structured perception event generation
* confidence-aware environmental interpretation
* controlled routing of perception outputs toward cognition, dialogue, and identity flows

By separating acquisition, preprocessing, extraction, interpretation, fusion, and event processing into explicit internal layers, NORA preserves both perceptual power and architectural clarity.

For that reason, `perception/` is one of the core domain modules of `src/nora/`.

## Architectural Structure

```text
perception
│
├── Sensor Abstraction
│   ├── sensor descriptors
│   ├── sensor readings
│   ├── synchronized sensor frames
│   ├── calibration profiles
│   ├── standardization services
│   ├── timestamp alignment services
│   ├── calibration application services
│   ├── buffering services
│   └── sensor providers
│
├── Audio Perception
│   ├── audio stream chunks
│   ├── speech segments
│   ├── wake-word results
│   ├── speech-recognition results
│   ├── speaker-identification results
│   ├── environmental sound results
│   ├── audio preprocessing
│   ├── audio feature extraction
│   ├── audio interpretation
│   ├── audio events
│   └── audio pipeline orchestration
│
├── Visual Perception
│   ├── video frames
│   ├── detected faces
│   ├── facial identity results
│   ├── detected gestures
│   ├── pose estimation results
│   ├── detected objects
│   ├── scene understanding results
│   ├── visual preprocessing
│   ├── visual feature extraction
│   ├── visual interpretation
│   ├── visual events
│   └── visual pipeline orchestration
│
├── Environmental Sensors
│   ├── temperature readings
│   ├── humidity readings
│   ├── light readings
│   ├── motion signals
│   ├── proximity readings
│   ├── environmental state snapshots
│   ├── environmental interpretation
│   ├── environmental events
│   └── environmental pipeline orchestration
│
├── Sensor Fusion
│   ├── fused presence results
│   ├── fused identity candidates
│   ├── fused scene context
│   ├── fused interaction context
│   ├── presence fusion services
│   ├── identity fusion services
│   ├── multimodal context fusion services
│   ├── fused-result resolution services
│   └── fusion events
│
└── Perception Event Processing
    ├── perception event envelopes
    ├── normalized perception events
    ├── perception confidence metadata
    ├── normalization services
    ├── event builders
    ├── event publishing services
    ├── selected-result storage services
    └── routing toward FSM, dialogue, and identity
```

```
perception/
├── sensor_abstraction/
│   ├── models/
│   │   ├── sensor_descriptor.py
│   │   ├── sensor_reading.py
│   │   ├── synchronized_sensor_frame.py
│   │   └── calibration_profile.py
│   ├── services/
│   │   ├── standardize_sensor_output_service.py
│   │   ├── align_sensor_timestamps_service.py
│   │   ├── apply_sensor_calibration_service.py
│   │   └── buffer_sensor_signal_service.py
│   └── providers/
│       ├── microphone_sensor_provider.py
│       ├── camera_sensor_provider.py
│       ├── proximity_sensor_provider.py
│       ├── environmental_sensor_provider.py
│       └── tactile_sensor_provider.py
│
├── audio_perception/
│   ├── models/
│   │   ├── audio_stream_chunk.py
│   │   ├── speech_segment.py
│   │   ├── wake_word_detection_result.py
│   │   ├── speech_recognition_result.py
│   │   ├── speaker_identification_result.py
│   │   └── environmental_sound_detection_result.py
│   ├── preprocessing/
│   │   ├── audio_noise_reduction_service.py
│   │   ├── audio_signal_normalization_service.py
│   │   └── audio_channel_alignment_service.py
│   ├── feature_extraction/
│   │   ├── speech_activity_feature_extractor.py
│   │   ├── speaker_voice_feature_extractor.py
│   │   └── sound_event_feature_extractor.py
│   ├── interpretation/
│   │   ├── wake_word_interpreter.py
│   │   ├── speech_to_text_interpreter.py
│   │   ├── speaker_identity_interpreter.py
│   │   └── sound_event_interpreter.py
│   ├── events/
│   │   ├── wake_word_detected_event.py
│   │   ├── speech_recognized_event.py
│   │   ├── speaker_identified_event.py
│   │   └── environmental_sound_detected_event.py
│   └── pipeline/
│       └── run_audio_perception_pipeline.py
│
├── visual_perception/
│   ├── models/
│   │   ├── video_frame.py
│   │   ├── detected_face.py
│   │   ├── facial_identity_result.py
│   │   ├── detected_gesture.py
│   │   ├── pose_estimation_result.py
│   │   ├── detected_object.py
│   │   └── scene_understanding_result.py
│   ├── preprocessing/
│   │   ├── image_resize_service.py
│   │   ├── image_normalization_service.py
│   │   └── image_frame_sampling_service.py
│   ├── feature_extraction/
│   │   ├── facial_feature_extractor.py
│   │   ├── pose_feature_extractor.py
│   │   ├── gesture_feature_extractor.py
│   │   └── object_feature_extractor.py
│   ├── interpretation/
│   │   ├── face_detection_interpreter.py
│   │   ├── face_recognition_interpreter.py
│   │   ├── gesture_recognition_interpreter.py
│   │   ├── pose_estimation_interpreter.py
│   │   ├── object_detection_interpreter.py
│   │   └── scene_understanding_interpreter.py
│   ├── events/
│   │   ├── face_detected_event.py
│   │   ├── face_identified_event.py
│   │   ├── gesture_recognized_event.py
│   │   ├── pose_estimated_event.py
│   │   ├── object_detected_event.py
│   │   └── scene_understood_event.py
│   └── pipeline/
│       └── run_visual_perception_pipeline.py
│
├── environmental_sensors/
│   ├── models/
│   │   ├── temperature_reading.py
│   │   ├── humidity_reading.py
│   │   ├── light_level_reading.py
│   │   ├── motion_detection_signal.py
│   │   ├── proximity_reading.py
│   │   └── environmental_state_snapshot.py
│   ├── interpretation/
│   │   ├── ambient_light_interpreter.py
│   │   ├── motion_state_interpreter.py
│   │   ├── presence_interpreter.py
│   │   ├── temperature_state_interpreter.py
│   │   └── humidity_state_interpreter.py
│   ├── events/
│   │   ├── motion_detected_event.py
│   │   ├── proximity_threshold_reached_event.py
│   │   ├── ambient_light_state_changed_event.py
│   │   ├── temperature_state_changed_event.py
│   │   └── humidity_state_changed_event.py
│   └── pipeline/
│       └── run_environmental_perception_pipeline.py
│
├── sensor_fusion/
│   ├── models/
│   │   ├── fused_presence_result.py
│   │   ├── fused_user_identity_candidate.py
│   │   ├── fused_scene_context.py
│   │   └── fused_interaction_context.py
│   ├── services/
│   │   ├── fuse_presence_signals_service.py
│   │   ├── fuse_identity_candidates_service.py
│   │   ├── fuse_multimodal_context_service.py
│   │   └── resolve_fused_perception_result_service.py
│   └── events/
│       ├── fused_presence_detected_event.py
│       ├── fused_identity_candidate_event.py
│       └── fused_context_updated_event.py
│
└── perception_event_processing/
    ├── models/
    │   ├── perception_event_envelope.py
    │   ├── normalized_perception_event.py
    │   └── perception_confidence_metadata.py
    ├── services/
    │   ├── normalize_perception_result_service.py
    │   ├── build_perception_event_service.py
    │   ├── publish_perception_event_service.py
    │   └── store_selected_perception_result_service.py
    └── routing/
        ├── route_perception_event_to_fsm.py
        ├── route_perception_event_to_dialogue.py
        └── route_perception_event_to_identity.py
```

# Cognitive Core Module

## Definition

The `cognitive_core/` module defines the internal runtime cognition of NORA.

While other architectural modules define identity, interaction channels, perception, dialogue continuity, planning, action, persistence, backend behavior, integrations, hardware structure, and observability, those modules still require a central internal layer that maintains the active operational mind of the system at runtime.

That is the role of `cognitive_core/`.

In architectural terms, the cognitive core is the internal control and runtime interpretation center of NORA.

It is the module that determines the current operational state of the system, maintains the active runtime context in which all other modules operate, modulates behavioral style and response energy, and preserves short-horizon cognitive continuity required for stable execution across consecutive events.

This module therefore defines:

* finite-state operational control
* event prioritization and transition logic
* state guards and state-transition actions
* active operational context representation
* subsystem-availability awareness
* hardware-condition awareness
* active-user, active-session, and active-project runtime context
* behavioral modulation state
* response-style shaping signals
* internal short-term cognitive memory
* recent event traces and temporary execution continuity

This module is not the same as planning.

Planning determines what the system should do in response to interpreted goals or requests.

The cognitive core determines what state the system is currently in, what conditions are active, what transitions are permitted, and how runtime continuity should be preserved across events.

This module is also not the same as dialogue.

Dialogue manages conversational continuity across turns and sessions.

The cognitive core manages immediate runtime continuity of system operation.

For that reason, `cognitive_core/` is one of the deepest and most central domain modules of NORA.

---

## Architectural Purpose

The purpose of the `cognitive_core/` module is to give NORA a structured internal runtime mind rather than a loose collection of event handlers and ad hoc control variables.

In a complex multimodal system, many things happen at once:

* interaction events arrive
* perception results appear
* sessions open and close
* projects become active or inactive
* planning outputs become available
* action execution starts or stops
* hardware conditions change
* trust state changes
* interruptions occur
* environmental conditions may force behavioral adaptation

Without a dedicated internal cognition layer, those conditions would be handled in fragmented ways across many modules, creating architectural problems such as:

* unclear operational state
* inconsistent transition logic
* hidden control assumptions
* duplicated state checks
* poor coordination across subsystems
* fragile interruption handling
* difficulty preserving short-term runtime continuity
* weak adaptation of behavior to current system conditions

By introducing a dedicated cognitive core, NORA gains:

* explicit operational-state control
* structured transition evaluation
* centralized runtime context tracking
* behavioral modulation support
* short-term internal continuity memory
* better coordination between perception, dialogue, planning, and action
* clearer safety-aware execution control
* more interpretable runtime behavior

This module therefore provides the immediate internal governing structure of the live system.

---

## Core Architectural Principle

The most important design principle of the cognitive core is this:

Runtime cognition must be separated into state control, operational context, behavioral modulation, and short-term internal memory.

These four concerns are related, but they are not identical.

### Finite-state control

Determines what operational state the system is currently in and what transitions are allowed.

### Operational context

Determines what runtime conditions are currently true about users, sessions, projects, subsystem availability, hardware condition, and latest interaction context.

### Emotional or behavioral modulation

Determines how the system should shape its tone, responsiveness, and behavioral energy under current conditions.

### Internal cognitive memory

Determines what short-term traces of recent runtime activity must be preserved for continuity of execution.

This separation is essential because runtime control is not only about state transitions. It is also about context coherence, behavioral adaptation, and continuity over short horizons.

---

## Internal Module Structure

The proposed structure is the following:

```text
cognitive_core/
├── finite_state_machine/
├── operational_context/
├── emotional_state/
└── internal_cognitive_memory/
```

This structure divides runtime cognition into four major internal subdomains.

### finite_state_machine

Defines the operational-state machine governing allowed states, transitions, event priority, guards, and transition actions.

### operational_context

Defines the structured runtime context in which those states and transitions should be interpreted.

### emotional_state

Defines how NORA modulates response style and behavioral energy at runtime.

### internal_cognitive_memory

Defines the short-term internal memory structures that preserve continuity between closely related runtime events.

These four parts together form the live internal control substrate of NORA.

---

## Architectural Role Within the Full System

The `cognitive_core/` module sits near the center of the whole architecture.

Many modules provide inputs into it.

Many modules also depend on its outputs.

The cognitive core receives signals from:

* perception
* interaction interfaces
* identity and trust state
* dialogue activity
* planner outputs
* hardware conditions
* event dispatch systems

It then maintains the internal runtime condition under which the rest of the system operates.

The cognitive core influences:

* whether perception should be active
* whether planning should be invoked
* whether action execution may proceed
* how interruptions are handled
* how frontend state should be reflected
* how response style should be shaped
* how recent event continuity should be preserved

This means the cognitive core is not one more ordinary domain module.

It is the internal runtime coordination mind of NORA.

---

# 1. finite_state_machine

## Definition

The `finite_state_machine/` submodule defines the operational finite-state machine that governs the active state of NORA and controls how the system transitions from one runtime condition to another.

Its purpose is to make system operation explicit rather than letting behavior emerge from uncontrolled combinations of flags and event handlers.

This submodule answers questions such as:

* what operational state is the system currently in
* what events are waiting to be processed
* what transitions are allowed from the current state
* what conditions must be true before a transition can occur
* what actions must run when a transition is applied
* how transition history should be recorded

This is one of the most critical control structures in the entire architecture.

### Internal Structure

```text
finite_state_machine/
├── enums/
├── models/
├── guards/
├── actions/
├── registries/
├── services/
└── dispatch/
```

---

## finite_state_machine/enums/

### operational_state_enum.py

Defines the recognized operational states of NORA.

This enum gives explicit names to the major runtime states through which the system may move.

These states may include categories such as idle, listening, interpreting, planning, acting, waiting, suspended, degraded, recovery, or fault-related states depending on the final system design.

Architecturally, this enum is the backbone of explicit operational control.

### transition_type_enum.py

Defines the different classes of transitions that may occur between operational states.

Its purpose is to distinguish transition semantics such as:

* normal progression
* interruption-driven transition
* recovery transition
* failure transition
* externally forced transition
* safety-driven transition

This allows transitions to be categorized rather than treated as an undifferentiated change of state.

### event_priority_enum.py

Defines the relative priority of queued system events used by the state machine.

Its role is important because not all runtime events should be processed equally.

For example, emergency stops, safety faults, and interruptions may require higher priority than ordinary informational events.

---

## finite_state_machine/models/

### state_definition.py

Defines the structured representation of a state known to the finite-state machine.

This model may include:

* state identity
* state name
* descriptive meaning
* state-level constraints
* allowed entry behavior
* allowed exit behavior
* metadata for frontend or observability

Its purpose is to give each operational state an explicit structural definition.

### transition_definition.py

Defines the structured representation of a possible transition between states.

This may include:

* source state
* target state
* triggering event type
* transition type
* required guards
* bound transition actions
* priority or ordering metadata

Architecturally, this model gives transition behavior explicit structure rather than embedding it implicitly in service code.

### transition_guard_result.py

Defines the structured result of evaluating a transition guard.

This may include pass or fail status, reason metadata, and possibly contextual diagnostics explaining why a transition may or may not proceed.

Its role is important because blocked transitions should be explainable and traceable.

### transition_action_definition.py

Defines the structured representation of an action that should occur when a transition is applied.

Its purpose is to separate transition control from the concrete side effects associated with entering or leaving a state.

### queued_system_event.py

Defines the structured representation of an event waiting in the finite-state machine event queue.

This may include event type, payload reference, priority, arrival time, correlation metadata, and source information.

Its role is important because queued events are the operational units through which state changes are triggered.

### current_state_snapshot.py

Defines the structured snapshot of the current active state of the finite-state machine.

This may include:

* current state
* entry timestamp
* triggering cause of current state
* pending transition metadata
* relevant contextual summaries

Its purpose is to provide an inspectable representation of runtime control state.

### transition_history_record.py

Defines the structured record of a previously applied transition.

This may include source state, target state, trigger event, timestamp, applied actions, and guard results.

Its role supports runtime traceability, observability, debugging, and historical reasoning.

---

## finite_state_machine/guards/

### microphone_available_guard.py

Defines the guard that checks whether microphone capability is available when a transition depends on audio interaction or listening behavior.

Its role is to prevent invalid transitions into states requiring unavailable audio input.

### subsystem_available_guard.py

Defines the guard that checks whether a required subsystem is currently available before permitting a transition.

Its purpose is to make subsystem health a first-class constraint in operational control.

### user_authenticated_guard.py

Defines the guard that checks whether the current user or actor satisfies required authentication conditions before the transition may proceed.

Its role is important for trust-aware state transitions.

### safety_condition_satisfied_guard.py

Defines the guard that checks whether required safety conditions are currently satisfied.

Its purpose is especially important for transitions that may lead toward action execution or physical-world effects.

### planner_result_valid_guard.py

Defines the guard that checks whether a planner result is available, coherent, and acceptable before transitions depending on planning outcomes are allowed.

### hardware_safe_to_execute_guard.py

Defines the guard that checks whether hardware-related conditions make execution safe enough to proceed.

Its role is particularly important in embodied or device-control scenarios.

---

## finite_state_machine/actions/

### update_operational_context_action.py

Defines the transition action that updates the operational context as part of a state transition.

Its purpose is to keep context and state aligned.

### activate_perception_pipeline_action.py

Defines the transition action that activates or enables relevant perception processing as part of entering a state that requires it.

### invoke_planner_action.py

Defines the transition action that requests planner invocation when the state machine enters a state requiring plan generation or plan refresh.

### trigger_action_execution_action.py

Defines the transition action that begins downstream action execution when a transition authorizes movement into execution-related behavior.

### notify_frontend_state_change_action.py

Defines the transition action that notifies frontend or realtime consumers that the operational state has changed.

Its purpose is to keep interfaces synchronized with internal control state.

### record_transition_history_action.py

Defines the transition action that persists or registers the applied transition in the transition history.

Its role supports observability and runtime trace reconstruction.

---

## finite_state_machine/registries/

### state_registry.py

Defines the registry of known states available to the finite-state machine.

Its purpose is to centralize state definitions and make them explicitly inspectable.

### transition_registry.py

Defines the registry of known transition definitions between states.

Its role is to centralize transition structure and avoid scattering transition logic across the codebase.

### guard_registry.py

Defines the registry of available guard implementations used during transition evaluation.

Its purpose is to decouple transition definitions from concrete guard binding.

### transition_action_registry.py

Defines the registry of transition actions that may be attached to state changes.

Its role is to keep transition action resolution explicit and configurable.

---

## finite_state_machine/services/

### enqueue_system_event_service.py

Defines the operation that inserts a system event into the finite-state event queue.

Its purpose is to ensure new runtime events are registered in a controlled and priority-aware way.

### dequeue_system_event_service.py

Defines the operation that removes the next event from the queue for processing.

Its role is to control the progression of event-driven state updates.

### evaluate_state_transition_service.py

Defines the operation that determines whether a state transition should occur in response to a queued event.

This service is one of the core decision points of the FSM.

It may consult current state, transition definitions, guards, and contextual conditions.

### apply_state_transition_service.py

Defines the operation that actually applies a valid state transition, including state update and execution of transition actions.

Its purpose is to separate transition evaluation from transition application.

### get_allowed_transitions_service.py

Defines the operation that returns the transitions currently available from the present state under current conditions.

Its role is useful for diagnostics, explainability, and frontend reflection.

### get_current_operational_state_service.py

Defines the operation that returns the current operational state of the system.

Its purpose is to expose current control state to other runtime modules.

---

## finite_state_machine/dispatch/

### system_event_dispatcher.py

Defines the dispatcher responsible for routing or presenting runtime events to the FSM evaluation flow.

Its purpose is to give the state machine a clear intake mechanism for queued or incoming system events.

### prioritized_event_queue_manager.py

Defines the manager responsible for maintaining a priority-aware event queue for the finite-state machine.

Its role is especially important in systems where interruption, safety, and urgent runtime control events must preempt less important ones.

---

# 2. operational_context

## Definition

The `operational_context/` submodule defines the structured runtime context in which NORA is currently operating.

Its purpose is to provide the live contextual substrate required for state transitions, planner invocation, behavioral modulation, frontend reflection, and safe system operation.

The finite-state machine defines what state the system is in.

Operational context defines what is true around that state.

This includes:

* active user context
* active session context
* active project context
* subsystem availability
* hardware condition
* latest interaction context
* general runtime context snapshot

### Internal Structure

```text
operational_context/
├── models/
├── services/
└── repositories/
```

---

## operational_context/models/

### operational_context_snapshot.py

Defines the structured snapshot of the total active operational context.

This model may aggregate multiple lower-level context models into one unified runtime context object.

Its purpose is to give the cognitive core a coherent view of current operating conditions.

### active_user_context.py

Defines the runtime context associated with the currently active user or actor.

This may include identity reference, trust state, active preference hints, or user-specific runtime conditions.

### active_session_context.py

Defines the runtime context associated with the currently active dialogue or interaction session.

Its role is to keep current session identity and session-level conditions explicit.

### active_project_context.py

Defines the runtime context associated with the currently active conversational or task project.

Its purpose is to let runtime cognition know whether a project is active and what high-level project continuity is in play.

### subsystem_availability_snapshot.py

Defines the structured snapshot of subsystem readiness and availability.

This may include audio availability, perception availability, planner availability, storage availability, integration readiness, and other runtime service conditions.

### hardware_condition_snapshot.py

Defines the structured snapshot of relevant hardware conditions.

This may include power state, fault state, thermal state, actuator readiness, or other execution-relevant hardware constraints.

### current_interaction_context.py

Defines the structured representation of the most recent or currently active interaction context.

This may include latest event metadata, modality, origin channel, pending clarification state, or interaction focus cues.

---

## operational_context/services/

### initialize_operational_context_service.py

Defines the operation that creates or initializes the operational context when the runtime starts or when a new control cycle is established.

### update_active_user_context_service.py

Defines the operation that updates the active user portion of operational context.

Its role is important when user identity changes, trust state changes, or a different actor becomes active.

### update_active_session_context_service.py

Defines the operation that updates the active session portion of operational context.

Its purpose is to keep runtime control aware of which session is currently governing interaction continuity.

### update_subsystem_availability_service.py

Defines the operation that updates subsystem-availability context based on startup, health, degradation, or recovery information.

### update_hardware_condition_service.py

Defines the operation that updates hardware-condition context based on current device state, fault signals, or safety-relevant readings.

### update_latest_event_context_service.py

Defines the operation that updates the current interaction context based on the latest relevant event entering the cognitive core.

Its purpose is to keep runtime cognition anchored to the most recent meaningful trigger context.

### get_operational_context_service.py

Defines the operation that retrieves the current effective operational context for the rest of the system.

---

## operational_context/repositories/

### operational_context_repository.py

Defines the persistence or runtime-storage boundary through which operational context snapshots are stored and retrieved.

Its role may be in-memory, persistent, or hybrid depending on runtime needs, but architecturally it exists to isolate storage of active context from context-manipulation services.

---

# 3. emotional_state

## Definition

The `emotional_state/` submodule defines the internal behavioral modulation layer of NORA.

Its purpose is not to simulate human emotion literally, but to control how the system modulates tone, responsiveness, expressive energy, and behavioral style at runtime.

This submodule matters because the same planning result may need to be expressed differently depending on current operating conditions such as:

* interruption sensitivity
* urgency
* calm or intense runtime mode
* user preference context
* environmental conditions
* task criticality
* safety-sensitive situations

This is therefore better understood as behavioral modulation architecture rather than as naive anthropomorphic emotion.

### Internal Structure

```text
emotional_state/
├── enums/
├── models/
├── services/
└── repositories/
```

---

## emotional_state/enums/

### behavioral_modulation_state_enum.py

Defines the recognized categories of behavioral modulation state.

This may include states such as calm, focused, alert, supportive, constrained, or urgency-oriented depending on final system semantics.

Its role is to make behavioral modulation explicit rather than implicit.

### response_energy_level_enum.py

Defines the energy or intensity level with which the system should express responses or interactions.

This may influence pacing, verbosity, assertiveness, urgency, or multimodal expression intensity.

---

## emotional_state/models/

### emotional_modulation_state.py

Defines the structured representation of the current behavioral modulation state.

This may include current modulation category, energy level, activation reason, and contextual metadata.

### response_style_profile.py

Defines the structured representation of the response-style profile currently applicable to system output.

Its purpose is to translate modulation state into actionable style guidance for downstream expression systems.

### modulation_update_signal.py

Defines the structured signal that requests or explains a change in behavioral modulation.

Its role is important because modulation may shift in response to events, safety concerns, user preference, or operational mode.

---

## emotional_state/services/

### update_behavioral_modulation_service.py

Defines the operation that updates the current behavioral modulation state.

Its role is to centralize the logic by which the system changes its internal behavioral posture.

### resolve_response_style_service.py

Defines the operation that determines the effective response style profile that downstream action and expression systems should use.

Its purpose is to transform internal modulation state into output-relevant behavioral style.

### get_current_modulation_state_service.py

Defines the operation that retrieves the current behavioral modulation state.

Its role is useful for expression, dialogue, frontend reflection, and diagnostics.

---

## emotional_state/repositories/

### emotional_state_repository.py

Defines the storage boundary for current or recent behavioral modulation state.

Its purpose is to isolate the state-holding mechanism from modulation services.

---

# 4. internal_cognitive_memory

## Definition

The `internal_cognitive_memory/` submodule defines the short-term internal memory structures used by NORA to preserve continuity across closely related runtime events.

Its purpose is not long-term persistence.

That belongs to persistence and memory.

Its purpose is not session-level conversational history.

That belongs to dialogue and session.

Its purpose is not long-horizon project context.

That also belongs elsewhere.

Instead, this submodule preserves the immediate internal traces required for stable runtime cognition over short time horizons.

This includes:

* recent event traces
* short-term control memory entries
* active intent traces
* temporary execution context

This submodule is important because a live system often needs to remember what just happened a moment ago in order to act coherently now.

### Internal Structure

```text
internal_cognitive_memory/
├── models/
├── services/
└── repositories/
```

---

## internal_cognitive_memory/models/

### short_term_control_memory_entry.py

Defines the structured representation of a short-term memory entry relevant to runtime control.

This may include transient state cues, recent decision references, pending execution hints, or temporary control facts.

### recent_event_trace.py

Defines the structured trace of recently processed runtime events.

Its purpose is to give the cognitive core a short-horizon memory of what has happened very recently.

### active_intent_trace.py

Defines the structured representation of the currently active or recently active intent trace relevant to runtime continuity.

Its role is especially useful when the system must preserve continuity across successive interpretation, planning, and action steps.

### temporary_execution_context.py

Defines the structured temporary context associated with an in-progress or recently triggered execution sequence.

This may include pending action references, unresolved execution metadata, or transient continuation state.

---

## internal_cognitive_memory/services/

### store_short_term_memory_entry_service.py

Defines the operation that stores or updates a short-term control memory entry.

Its role is to ensure transient runtime memory is captured explicitly rather than through scattered temporary variables.

### retrieve_recent_event_trace_service.py

Defines the operation that retrieves recent runtime event traces relevant to current cognitive processing.

Its purpose is to support continuity-aware control and interpretation.

### clear_expired_control_memory_service.py

Defines the operation that removes short-term cognitive memory entries that are no longer relevant.

Its role is important because internal cognitive memory must remain bounded and current.

### build_runtime_continuity_context_service.py

Defines the operation that assembles a continuity-aware short-term context from recent memory traces and temporary execution state.

Its purpose is to provide the live runtime system with a coherent immediate past when evaluating current behavior.

---

## internal_cognitive_memory/repositories/

### internal_cognitive_memory_repository.py

Defines the storage boundary for short-term internal cognitive memory structures.

Its role is to isolate the memory-holding mechanism from memory-oriented services.

---

## Cross-Submodule Architectural Relationships

The cognitive core is best understood as four interacting internal layers rather than four separate folders.

### finite_state_machine -> operational_context

State transitions depend heavily on current operational context.

Guards and transition decisions often consult user context, subsystem availability, hardware condition, and current interaction focus.

### operational_context -> finite_state_machine

Operational context is also updated by state transitions and transition actions.

This means state and context continuously inform one another.

### emotional_state -> action and dialogue behavior

Behavioral modulation does not decide plans directly, but it influences how system behavior is expressed and sometimes how aggressively or cautiously interaction proceeds.

### internal_cognitive_memory -> transition and continuity logic

Short-term internal memory supports coherent runtime behavior across multiple closely related events, especially when the system must remember recent triggers, intent traces, or execution continuity.

### finite_state_machine -> internal_cognitive_memory

Transitions and event processing may write traces into short-term memory.

### operational_context -> emotional_state

n
Current runtime conditions may influence behavioral modulation.

### emotional_state -> operational presentation

n
The current modulation state may affect frontend-visible system posture or downstream response shaping.

These relationships show why the cognitive core is a coordinated runtime mind rather than a set of isolated support utilities.

---

## What This Module Must Not Contain

To preserve architectural clarity, the cognitive core should not absorb responsibilities that belong elsewhere.

It should not contain:

* semantic intent classification
* full task planning logic
* domain-specific action implementations
* session-history persistence
* long-term memory storage
* frontend rendering logic
* direct hardware-driver ownership
* authentication policy logic
* perception-engine implementation

It may coordinate with these things, gate them, or react to their outputs, but it must remain the runtime cognition and control layer.

---

## Interaction With Other Modules

The `cognitive_core/` module interacts with nearly every major architectural domain.

### shared

Uses shared identifiers, operation models, exceptions, time utilities, execution statuses, and generic support structures.

### identity_access_security

Consumes trust state, active-user information, and authorization-relevant context for guarded transitions and operational decisions.

### interaction_interfaces

Consumes normalized user and operator interaction events that may trigger state changes or context updates.

### perception

Consumes perception-derived events, presence signals, identity cues, interruption signals, and environmental context updates.

### dialogue_and_session

Uses active session and active project context, and may influence dialogue continuity through current operational state and interaction focus.

### planning_and_agents

Invokes planning through transition actions and evaluates planner-result validity through FSM guards.

### action_and_expression

Triggers downstream action execution and provides behavioral modulation state that may shape expression style.

### persistence_and_memory

May persist selected transition history, context snapshots, or short-term traces when architectural policy requires it.

### backend_and_application

Provides current operational state, context, and runtime control signals to coordinators, APIs, and realtime layers.

### frontend_support

Provides state and modulation information that can be transformed into frontend-facing view models.

### integrations_and_external_services

May depend on subsystem availability signals for external engines and provider-backed capabilities.

### infrastructure_and_hardware

Consumes hardware-condition data and safety-related execution constraints.

### observability

Exposes transition history, current state, queue behavior, and runtime modulation state for diagnostics and monitoring.

---

## Design Constraints of the Module

The `cognitive_core/` module should obey several strict architectural constraints.

### 1. State, context, modulation, and short-term memory must remain distinct

These concerns are deeply related, but they should not collapse into one vague runtime-state object.

### 2. FSM logic must remain explicit

Allowed states, transitions, guards, and actions should remain inspectable and structured rather than hidden in scattered conditional code.

### 3. Runtime context must be queryable

The system must be able to expose current operational context in a structured form to other modules and interfaces.

### 4. Behavioral modulation must remain operational, not theatrical

The emotional-state layer should shape output style and behavior sensibly without becoming a vague simulation layer detached from real runtime needs.

### 5. Internal cognitive memory must remain short-term and bounded

It should preserve runtime continuity, not become an accidental second long-term memory system.

### 6. Safety and interruption must be first-class

Because NORA may act in the physical or digital world, interruption, hardware safety, and subsystem availability must be visible in cognitive control.

### 7. Transition side effects must remain explicit

Actions triggered by state changes should remain defined and inspectable rather than hidden inside opaque transition code.

---

## Testing Implications

The cognitive core requires especially strong structural testing because errors here affect the global runtime behavior of the system.

Important testing categories include:

* operational-state definition tests
* transition-definition consistency tests
* guard evaluation tests
* event-priority and queue-order tests
* transition-application tests
* transition-history recording tests
* active-user-context update tests
* subsystem-availability update tests
* hardware-condition-context tests
* latest-event-context tests
* behavioral modulation update tests
* response-style resolution tests
* short-term memory storage tests
* recent-event-trace retrieval tests
* expiration and cleanup tests for cognitive memory
* runtime continuity context assembly tests
* interaction between FSM state and context tests
* interruption and safety-transition tests

Failures here are especially dangerous because they can make the system behave incoherently even when individual upstream or downstream modules are correct.

---

## Why This Structure Fits NORA

This structure fits NORA because NORA is not a stateless responder.

It is a persistent, multimodal, event-driven, safety-aware, and context-dependent system.

A system like that needs:

* explicit operational-state control
* coherent runtime context
* adaptive behavioral modulation
* short-term memory for immediate continuity

A flatter architecture would make runtime behavior much harder to understand, test, and extend.

The proposed structure allows NORA to:

* govern system operation explicitly through states and transitions
* maintain awareness of current users, sessions, projects, and subsystem conditions
* adapt response style to current runtime posture
* preserve continuity across recent events without confusing that with long-term memory

That makes it a strong and appropriate cognitive architecture for the system.

---

## Architectural Importance

The `cognitive_core/` module provides the internal runtime mind through which NORA maintains coherent operational behavior.

While other modules define interaction, perception, dialogue, planning, action, memory, backend behavior, integrations, and hardware structure, the live system still requires a central internal architecture that determines its current operational state, maintains the active runtime context in which decisions occur, modulates how behavior should be expressed, and preserves short-term internal continuity across successive events.

Through this module the architecture gains:

* explicit operational-state control through a finite-state machine
* structured runtime context for users, sessions, projects, subsystem availability, hardware condition, and interaction focus
* behavioral modulation support for response style and runtime posture
* bounded short-term cognitive memory for immediate continuity
* clearer safety-aware control over execution and interruption
* better coordination between perception, dialogue, planning, and action
* stronger interpretability of live system behavior

By separating state control, operational context, behavioral modulation, and internal cognitive memory into explicit internal layers, NORA preserves both runtime flexibility and architectural clarity.

For that reason, `cognitive_core/` is one of the core internal domain modules of `src/nora/`.

## Architectural Structure

```text
cognitive_core
│
├── Finite State Machine
│   ├── operational states
│   ├── transition types
│   ├── event priorities
│   ├── state definitions
│   ├── transition definitions
│   ├── guard results
│   ├── transition action definitions
│   ├── queued system events
│   ├── current state snapshots
│   ├── transition history records
│   ├── transition guards
│   ├── transition actions
│   ├── state registries
│   ├── transition registries
│   ├── guard registries
│   ├── transition action registries
│   ├── queue services
│   ├── transition evaluation services
│   ├── transition application services
│   ├── state-query services
│   └── event dispatch and priority queue management
│
├── Operational Context
│   ├── total context snapshots
│   ├── active user context
│   ├── active session context
│   ├── active project context
│   ├── subsystem availability snapshots
│   ├── hardware condition snapshots
│   ├── current interaction context
│   ├── context initialization services
│   ├── context update services
│   ├── context query services
│   └── context repository
│
├── Emotional State
│   ├── behavioral modulation states
│   ├── response energy levels
│   ├── emotional modulation state models
│   ├── response style profiles
│   ├── modulation update signals
│   ├── modulation update services
│   ├── response-style resolution services
│   ├── modulation query services
│   └── modulation repository
│
└── Internal Cognitive Memory
    ├── short-term control memory entries
    ├── recent event traces
    ├── active intent traces
    ├── temporary execution context
    ├── short-term memory storage services
    ├── recent-trace retrieval services
    ├── expiration cleanup services
    ├── runtime continuity-context builders
    └── cognitive memory repository
```


```
cognitive_core/
├── finite_state_machine/
│   ├── enums/
│   │   ├── operational_state_enum.py
│   │   ├── transition_type_enum.py
│   │   └── event_priority_enum.py
│   ├── models/
│   │   ├── state_definition.py
│   │   ├── transition_definition.py
│   │   ├── transition_guard_result.py
│   │   ├── transition_action_definition.py
│   │   ├── queued_system_event.py
│   │   ├── current_state_snapshot.py
│   │   └── transition_history_record.py
│   ├── guards/
│   │   ├── microphone_available_guard.py
│   │   ├── subsystem_available_guard.py
│   │   ├── user_authenticated_guard.py
│   │   ├── safety_condition_satisfied_guard.py
│   │   ├── planner_result_valid_guard.py
│   │   └── hardware_safe_to_execute_guard.py
│   ├── actions/
│   │   ├── update_operational_context_action.py
│   │   ├── activate_perception_pipeline_action.py
│   │   ├── invoke_planner_action.py
│   │   ├── trigger_action_execution_action.py
│   │   ├── notify_frontend_state_change_action.py
│   │   └── record_transition_history_action.py
│   ├── registries/
│   │   ├── state_registry.py
│   │   ├── transition_registry.py
│   │   ├── guard_registry.py
│   │   └── transition_action_registry.py
│   ├── services/
│   │   ├── enqueue_system_event_service.py
│   │   ├── dequeue_system_event_service.py
│   │   ├── evaluate_state_transition_service.py
│   │   ├── apply_state_transition_service.py
│   │   ├── get_allowed_transitions_service.py
│   │   └── get_current_operational_state_service.py
│   └── dispatch/
│       ├── system_event_dispatcher.py
│       └── prioritized_event_queue_manager.py
│
├── operational_context/
│   ├── models/
│   │   ├── operational_context_snapshot.py
│   │   ├── active_user_context.py
│   │   ├── active_session_context.py
│   │   ├── active_project_context.py
│   │   ├── subsystem_availability_snapshot.py
│   │   ├── hardware_condition_snapshot.py
│   │   └── current_interaction_context.py
│   ├── services/
│   │   ├── initialize_operational_context_service.py
│   │   ├── update_active_user_context_service.py
│   │   ├── update_active_session_context_service.py
│   │   ├── update_subsystem_availability_service.py
│   │   ├── update_hardware_condition_service.py
│   │   ├── update_latest_event_context_service.py
│   │   └── get_operational_context_service.py
│   └── repositories/
│       └── operational_context_repository.py
│
├── emotional_state/
│   ├── enums/
│   │   ├── behavioral_modulation_state_enum.py
│   │   └── response_energy_level_enum.py
│   ├── models/
│   │   ├── emotional_modulation_state.py
│   │   ├── response_style_profile.py
│   │   └── modulation_update_signal.py
│   ├── services/
│   │   ├── update_behavioral_modulation_service.py
│   │   ├── resolve_response_style_service.py
│   │   └── get_current_modulation_state_service.py
│   └── repositories/
│       └── emotional_state_repository.py
│
└── internal_cognitive_memory/
    ├── models/
    │   ├── short_term_control_memory_entry.py
    │   ├── recent_event_trace.py
    │   ├── active_intent_trace.py
    │   └── temporary_execution_context.py
    ├── services/
    │   ├── store_short_term_memory_entry_service.py
    │   ├── retrieve_recent_event_trace_service.py
    │   ├── clear_expired_control_memory_service.py
    │   └── build_runtime_continuity_context_service.py
    └── repositories/
        └── internal_cognitive_memory_repository.py
```

# Dialogue and Session Module

## Definition

The `dialogue_and_session/` module defines how NORA represents, preserves, compresses, and recovers conversational continuity over time.

While other architectural modules define identity, interaction channels, perception, runtime cognition, planning, action, persistence, backend behavior, integrations, hardware structure, and observability, none of those modules by themselves define how a conversation becomes a durable structured process rather than a sequence of disconnected messages.

That is the role of `dialogue_and_session/`.

In architectural terms, this module defines the temporal conversational continuity layer of NORA.

It is the module that determines:

* how a dialogue session begins, becomes active, is suspended, and ends
* how long-running conversational objectives are represented as persistent projects
* how individual dialogue turns are stored and related to sessions and projects
* how extended conversation history is compressed into bounded summaries
* how previous conversational state is reconstructed when a user returns

This module therefore defines:

* sessions and their lifecycle
* conversational projects and their lifecycle
* dialogue history and turn representation
* summary and compression structures
* recovery-state construction and validation
* continuity restoration mechanisms across sessions and projects

This module is not the same as the cognitive core.

The cognitive core manages the immediate runtime operational mind of the system.

The dialogue and session module manages continuity of interaction across time.

This module is also not the same as long-term persistence in the abstract.

Persistence and memory define where information can live durably.

The dialogue and session module defines the conversational structures that should be preserved, summarized, and recovered.

For that reason, `dialogue_and_session/` is one of the core continuity modules of NORA.

---

## Architectural Purpose

The purpose of the `dialogue_and_session/` module is to ensure that NORA can operate as a continuous conversational system rather than as a stateless responder.

In a system like NORA, users may:

* return after interruptions
* continue work across multiple sessions
* maintain long-running projects
* revisit earlier decisions
* ask follow-up questions based on prior conversation
* switch temporarily to another topic and then come back
* expect the system to remember not only facts, but conversational structure

Without a dedicated dialogue and session architecture, these continuity needs would collapse into fragile ad hoc message history handling.

That would create serious problems such as:

* no explicit session boundaries
* no distinction between one-off chats and persistent multi-session projects
* uncontrolled growth of dialogue history
* poor recovery after interruption or restart
* lack of structure for summaries and compressed context
* weak continuity when multiple projects coexist
* difficulty reconstructing the right context when a user resumes an earlier thread

By introducing a dedicated dialogue and session module, NORA gains:

* explicit session lifecycle control
* structured conversational projects
* organized dialogue history storage
* bounded summarization and compression mechanisms
* recoverable context after interruptions or long gaps
* clearer separation between raw dialogue, summarized dialogue, and reconstructed dialogue state

This module therefore provides the architecture of conversational continuity.

---

## Core Architectural Principle

The most important design principle of the dialogue and session module is this:

Conversational continuity must be separated into active sessions, persistent conversational projects, raw dialogue history, compressed summaries, and recovery state.

These concerns are related, but they are not the same.

### Sessions

Define bounded periods of interaction.

### Conversational projects

Define persistent objectives or topics that may span multiple sessions.

### Conversational history

Defines the recorded sequence of dialogue turns and associated annotations.

### Summarization and compression

Defines bounded representations that preserve semantic continuity without retaining unlimited raw context at runtime.

### Recovery state

Defines how previously known context is reconstructed into a usable form when interaction resumes.

This separation is essential because continuity over time is not a single problem. It is a layered problem.

---

## Internal Module Structure

The proposed structure is the following:

```text
dialogue_and_session/
├── sessions/
├── conversational_projects/
├── conversational_history/
├── summarization_and_compression/
└── recovery_state/
```

This structure divides conversational continuity into five major subdomains.

### sessions

Defines the lifecycle and representation of bounded interaction sessions.

### conversational_projects

Defines persistent conversation-linked objectives that can span many sessions.

### conversational_history

Defines the storage and representation of dialogue turns.

### summarization_and_compression

Defines mechanisms for bounded dialogue memory and semantic compression.

### recovery_state

Defines structures and services that rebuild meaningful context when a session or project is resumed.

This decomposition is especially important because large conversational systems fail when they treat “history” as one flat undifferentiated blob.

---

## Architectural Role Within the Full System

The `dialogue_and_session/` module sits between immediate runtime interaction and long-horizon continuity.

It receives or depends on:

* interaction events
* user identity context
* active project selection
* session state changes
* dialogue turns produced over time
* summarization triggers
* recovery triggers when a prior context must be resumed

It then provides continuity structures that affect:

* what the system understands as the current conversation
* what project is active
* what history is relevant
* what compressed context should be injected into downstream reasoning
* what should be restored after interruptions or return visits

This means the module is not merely archival.

It is an active continuity-management system.

---

# 1. sessions

## Definition

The `sessions/` submodule defines the lifecycle, structure, and retrieval of dialogue sessions.

A session represents a bounded interval of interaction between a user and NORA.

Its purpose is to give conversational time explicit structure.

Without sessions, all conversation would blur into one endless undifferentiated stream.

The sessions submodule therefore answers questions such as:

* when does a conversation session begin
* when is it active
* when is it suspended
* when is it terminated
* how is an old session restored
* what metadata defines a session
* which session is currently active

### Internal Structure

```text
sessions/
├── enums/
├── models/
├── services/
└── repositories/
```

---

## sessions/enums/

### session_status_enum.py

Defines the lifecycle states of a dialogue session.

This may include states such as:

* created
* active
* suspended
* terminated
* restored
* archived

Its purpose is to make session lifecycle explicit and queryable.

---

## sessions/models/

### dialogue_session.py

Defines the primary structured representation of a dialogue session.

This model may include:

* session identifier
* associated user identity
* associated project pointer where relevant
* creation time
* activation time
* status
* summary references
* recovery metadata

Architecturally, this is the central object of the sessions submodule.

### session_metadata.py

Defines supplemental metadata describing a session.

This may include interface origin, device context, language context, runtime environment details, or lifecycle annotations.

Its role is to keep the main session model from becoming overloaded while preserving useful contextual information.

### session_boundary.py

Defines the structural representation of the temporal or logical boundary of a session.

This may include start time, end time, suspension markers, resume points, or termination cause.

Its purpose is to make session delimitation explicit.

### session_summary.py

Defines the structured summary attached specifically to a session.

Its role is to represent the compressed understanding of what happened during the session without storing only raw turns.

### active_session_pointer.py

Defines the structured pointer that identifies which session is currently active for a user, channel, or runtime context.

Its role is important because the system may need to resolve active-session identity quickly and consistently.

---

## sessions/services/

### create_session_service.py

Defines the operation that creates a new dialogue session.

Its purpose is to initialize the bounded interaction container in which future dialogue turns will live.

### activate_session_service.py

Defines the operation that marks a session as active.

Its role is important when switching between sessions or restoring a prior session into current runtime focus.

### suspend_session_service.py

Defines the operation that suspends a currently active session without terminating it.

Its purpose is to support interruption, deferred continuation, or temporary focus shifts.

### terminate_session_service.py

Defines the operation that ends a session definitively.

Its role is to close the bounded interaction interval in a controlled and traceable way.

### restore_session_service.py

Defines the operation that restores a previously existing session into a usable state.

Its purpose is to reactivate a prior session while re-establishing the context required for continuity.

### list_sessions_for_user_service.py

Defines the operation that returns the sessions associated with a user.

Its role supports browsing, session selection, administrative inspection, and recovery workflows.

---

## sessions/repositories/

### session_repository.py

Defines the persistence boundary for dialogue sessions.

Its purpose is to isolate session-storage behavior from session lifecycle services.

---

# 2. conversational_projects

## Definition

The `conversational_projects/` submodule defines persistent conversational objectives or topics that may span multiple sessions.

A conversational project is not merely a session and not merely a file or artifact.

It is a structured continuity unit representing an ongoing goal, topic, or piece of work that may continue across many user interactions.

This submodule is important because users often do not think in terms of sessions. They think in terms of projects, goals, and ongoing work.

### Internal Structure

```text
conversational_projects/
├── enums/
├── models/
├── services/
└── repositories/
```

---

## conversational_projects/enums/

### project_state_enum.py

Defines the lifecycle state of a conversational project.

This may include states such as:

* created
* initialized
* active
* paused
* completed
* archived

Its purpose is to make long-horizon conversational work explicit and governable.

---

## conversational_projects/models/

### conversational_project.py

Defines the primary structured representation of a conversational project.

This model may include:

* project identifier
* associated user identity
* project title or label
* current project state
* goal references
* context references
* related tasks
* notes and artifacts

Architecturally, this is the core object representing persistent conversation-linked work.

### project_goal.py

Defines the structured representation of a project goal.

Its purpose is to represent what the project is trying to achieve at a high level.

### project_context.py

Defines the structured contextual information associated with the project.

This may include scope notes, background assumptions, constraints, or remembered context necessary for project continuity.

### project_task.py

Defines the structured representation of a task within a conversational project.

Its role is important because projects often contain actionable or trackable sub-goals.

### project_note.py

Defines the structured representation of an internal note associated with a project.

Its purpose is to preserve useful supporting context, remarks, or intermediate findings.

### project_artifact_reference.py

Defines the structured reference to an artifact associated with the project.

This may refer to generated documents, files, links, analyses, or other outputs connected to project work.

---

## conversational_projects/services/

### create_project_service.py

Defines the operation that creates a new conversational project.

Its purpose is to create a persistent continuity unit distinct from any one session.

### initialize_project_service.py

Defines the operation that performs initial project setup after creation.

Its role may include goal attachment, initial context construction, or default state preparation.

### continue_project_service.py

Defines the operation that continues an existing project by bringing it back into active conversational focus.

Its purpose is important for multi-session continuity.

### pause_project_service.py

Defines the operation that pauses a project without completing or deleting it.

Its role is to support deferred work.

### complete_project_service.py

Defines the operation that marks a project as completed.

Its purpose is to close the lifecycle of a project when its objective has been fulfilled.

### archive_project_service.py

Defines the operation that archives a project for long-term retention without keeping it active.

### select_active_project_service.py

Defines the operation that selects which project should currently be treated as active in the conversation.

Its role is especially important when multiple projects coexist for one user.

---

## conversational_projects/repositories/

### project_repository.py

Defines the persistence boundary for conversational projects.

### project_task_repository.py

Defines the persistence boundary for project tasks.

### project_note_repository.py

Defines the persistence boundary for project notes.

These repositories keep persistent project structures separated and maintainable.

---

# 3. conversational_history

## Definition

The `conversational_history/` submodule defines the representation, storage, retrieval, and filtering of dialogue turns.

Its purpose is to preserve the raw or near-raw sequence of conversational exchanges that occur within sessions and across projects.

This submodule is the historical substrate of dialogue continuity.

It is not the same as summarization.

It is not the same as recovery.

It is the structured turn history itself.

### Internal Structure

```text
conversational_history/
├── enums/
├── models/
├── services/
└── repositories/
```

---

## conversational_history/enums/

### dialogue_speaker_enum.py

Defines the speaker categories associated with dialogue turns.

This may include user, assistant, system, or operator categories depending on the conversation model.

Its purpose is to make turn ownership explicit and queryable.

---

## conversational_history/models/

### dialogue_turn.py

Defines the primary structured representation of an individual dialogue turn.

This model may include:

* turn identifier
* speaker category
* session association
* project association where relevant
* timestamp
* content reference
* modality record
* annotations

Architecturally, this is the central unit of recorded dialogue history.

### turn_metadata.py

Defines metadata associated with a dialogue turn.

This may include timestamps, channel origin, trace identifiers, user context hints, or processing metadata.

### turn_content.py

Defines the structured content of a dialogue turn.

Its purpose is to separate the semantic payload of the turn from surrounding metadata.

### turn_modality_record.py

Defines the record of which modality or channel the turn used.

This may include text, voice-derived text, UI action, multimodal input, or other conversationally relevant forms.

### interpreted_turn_annotation.py

Defines structured annotations attached to a turn after interpretation.

This may include detected intent, extracted entities, ambiguity markers, summary relevance signals, or other dialogue-analysis metadata.

---

## conversational_history/services/

### append_dialogue_turn_service.py

Defines the operation that appends a new turn to the dialogue history.

Its purpose is to ensure turn insertion remains explicit, ordered, and associated with the correct session and project contexts.

### get_session_history_service.py

Defines the operation that retrieves the history associated with a specific session.

### get_project_history_service.py

Defines the operation that retrieves the history associated with a project, potentially across multiple sessions.

Its role is important for long-running conversational work.

### get_user_history_service.py

Defines the operation that retrieves dialogue history associated with a user across sessions or projects according to policy.

### filter_dialogue_turns_service.py

Defines the operation that filters dialogue turns according to relevance, timeframe, modality, project, speaker, or other criteria.

Its purpose is to support bounded retrieval and context selection.

---

## conversational_history/repositories/

### dialogue_turn_repository.py

Defines the persistence boundary for dialogue turns.

Its role is to isolate turn-storage behavior from higher-level history operations.

---

# 4. summarization_and_compression

## Definition

The `summarization_and_compression/` submodule defines how extended dialogue or project history is transformed into bounded semantic representations suitable for efficient continuity.

Its purpose is to make conversation scalable over time.

Raw history alone is not enough for an ongoing system, because unrestricted raw context grows too large and becomes inefficient or noisy for downstream reasoning.

This submodule therefore defines how continuity is compressed without being lost.

### Internal Structure

```text
summarization_and_compression/
├── models/
├── services/
└── providers/
```

---

## summarization_and_compression/models/

### dialogue_summary.py

Defines the structured summary of dialogue content.

Its purpose is to represent the most important semantic content of a bounded dialogue segment in compressed form.

### project_summary.py

Defines the structured summary of a conversational project.

Its role is especially important because project continuity often spans too much history to load raw every time.

### summary_window_definition.py

Defines the structured specification of what range or window of history should be summarized.

This may include session boundaries, turn ranges, time ranges, or project-linked segments.

### compressed_context_payload.py

Defines the structured compressed payload generated from summaries or context compression logic.

Its purpose is to provide a bounded continuity object that can be injected into downstream reasoning or recovery flows.

---

## summarization_and_compression/services/

### summarize_session_service.py

Defines the operation that generates a summary for a session.

Its purpose is to compress a bounded dialogue interval into durable semantic form.

### summarize_project_service.py

Defines the operation that generates a summary for a project.

Its role is important for preserving long-horizon project continuity.

### compress_dialogue_context_service.py

Defines the operation that compresses selected dialogue context into a reduced representation for runtime reuse.

Its purpose is to keep continuity bounded and usable.

### rebuild_context_from_summary_service.py

Defines the operation that reconstructs a usable contextual representation from previously generated summaries.

Its role is to bridge compression and later recovery.

---

## summarization_and_compression/providers/

### dialogue_summarization_provider.py

Defines the provider boundary responsible for producing dialogue or project summaries.

Its purpose is to decouple summary-generation services from any specific summarization technology or engine.

---

# 5. recovery_state

## Definition

The `recovery_state/` submodule defines how prior conversational continuity is reconstructed when a user, session, or project must be resumed.

Its purpose is to translate stored session data, project data, history, and summaries into a coherent active context suitable for present interaction.

Recovery is not the same as raw retrieval.

It is the structured reconstruction of what the system should know right now in order to continue meaningfully.

### Internal Structure

```text
recovery_state/
├── models/
├── services/
└── repositories/
```

---

## recovery_state/models/

### recovery_state.py

Defines the primary structured representation of a recovery-ready conversational state.

This model may include session references, project references, summaries, selected history, and continuity metadata.

### recovered_context_bundle.py

Defines the structured bundle of contextual information produced by a recovery operation.

Its purpose is to provide downstream modules with a ready-to-use recovery result.

### project_recovery_bundle.py

Defines the structured recovery bundle specifically associated with project continuation.

Its role is to preserve project-specific recovery information distinctly from session-only recovery.

### session_recovery_bundle.py

Defines the structured recovery bundle specifically associated with session continuation.

Its role is to preserve session-specific recovery information distinctly from broader project continuity.

---

## recovery_state/services/

### build_recovery_state_service.py

Defines the operation that assembles a recovery state from stored session, project, summary, and history components.

Its purpose is to create the coherent state object needed for resumption.

### recover_last_session_service.py

Defines the operation that reconstructs the most recent relevant session for continuation.

Its role is important for common “resume where we left off” behavior.

### recover_project_context_service.py

Defines the operation that reconstructs the relevant project continuity context for a project being resumed.

### validate_recovery_state_service.py

Defines the operation that checks whether a candidate recovery state is coherent, complete enough, and safe to activate.

Its purpose is to prevent invalid or misleading reconstruction.

---

## recovery_state/repositories/

### recovery_state_repository.py

Defines the persistence boundary for stored recovery-state artifacts or recovery-support structures.

Its role is to isolate recovery-oriented storage from recovery-construction logic.

---

## Cross-Submodule Architectural Relationships

The dialogue and session module is best understood as a continuity pipeline rather than as five isolated directories.

### sessions -> conversational_history

Dialogue turns belong to sessions, so history is anchored in session structure.

### conversational_projects -> sessions

Projects may span many sessions, so sessions and projects must remain linked without becoming the same thing.

### conversational_history -> summarization_and_compression

Raw turn history provides the substrate from which summaries and compressed continuity are generated.

### summarization_and_compression -> recovery_state

Recovery often depends on summaries and compressed context rather than on raw history alone.

### sessions -> recovery_state

When restoring a conversation, session structures provide the temporal container for recovery.

### conversational_projects -> recovery_state

When continuing long-horizon work, project structures provide the goal-oriented continuity frame.

These relationships show that the module is a structured continuity architecture:

* sessions bound time
* projects bind purpose
* history binds detail
* summaries bind compression
* recovery binds reconstruction

---

## What This Module Must Not Contain

To preserve architectural clarity, the dialogue and session module should not absorb responsibilities that belong elsewhere.

It should not contain:

* low-level transport or API route logic
* planner implementation logic
* state-machine control logic
* authentication policy logic
* hardware-control logic
* frontend rendering logic
* generic long-term memory unrelated to dialogue continuity
* sensor-perception pipelines

It may interact with all of those, but it must remain focused on conversational continuity over time.

---

## Interaction With Other Modules

The `dialogue_and_session/` module interacts with many other architectural domains.

### shared

Uses shared identifiers, timestamps, pagination structures, exceptions, modality metadata, and generic operation models.

### identity_access_security

Anchors sessions and projects to users, trust context, and access-sensitive continuity boundaries.

### interaction_interfaces

Receives interaction events that may result in dialogue turns, session activation, or session switching.

### perception

Consumes perception-derived speech, interruption cues, presence cues, and identity hints that may affect dialogue continuity and turn construction.

### cognitive_core

Coordinates with active-session context, active-project context, and runtime control state.

### planning_and_agents

Provides historical and compressed context required for planning, clarification, and project continuation.

### action_and_expression

Provides response continuity context so that outputs remain coherent with prior dialogue and project state.

### persistence_and_memory

Stores sessions, projects, turns, summaries, and recovery artifacts durably.

### backend_and_application

Exposes session and project lifecycle operations, history retrieval, and recovery flows through application boundaries.

### frontend_support

Provides session, project, and history structures that can be transformed into frontend-friendly representations.

### integrations_and_external_services

May use summarization providers or external engines for dialogue compression and recovery support.

### observability

Provides continuity-related traces, session transitions, recovery behavior, and history access diagnostics.

---

## Design Constraints of the Module

The `dialogue_and_session/` module should obey several strict architectural constraints.

### 1. Sessions and projects must remain distinct

A session is a bounded interval of interaction.

A project is a persistent continuity unit that may span many sessions.

These should not collapse into one concept.

### 2. Raw history and summaries must remain distinct

Summaries are not a replacement for history.

They are a bounded semantic compression of it.

### 3. Recovery must remain reconstructive, not naive replay

Recovery should assemble what is relevant and usable now, not merely reload everything blindly.

### 4. Conversational continuity must remain explicit

The system should know what session is active, what project is active, and what historical material is relevant.

### 5. Compression must remain bounded and intentional

Summarization should preserve continuity while reducing runtime load, not produce vague or untraceable abstractions.

### 6. Recovery validation must be explicit

Recovered context must be checked for coherence before it becomes active.

### 7. Conversational structure must remain queryable

The system should be able to retrieve history by session, project, and user in structured ways.

---

## Testing Implications

This module requires especially strong continuity-oriented testing.

Important testing categories include:

* session lifecycle tests
* active-session pointer tests
* session restoration tests
* project lifecycle tests
* active-project selection tests
* dialogue-turn append tests
* session-history retrieval tests
* project-history retrieval tests
* dialogue filtering tests
* session-summary generation tests
* project-summary generation tests
* context-compression tests
* context-rebuild-from-summary tests
* recovery-state construction tests
* last-session recovery tests
* project-context recovery tests
* recovery validation tests
* multi-session project continuity tests

Failures here can make NORA appear forgetful, incoherent, or structurally confused even if other modules behave correctly.

---

## Why This Structure Fits NORA

This structure fits NORA because NORA is intended to be a persistent, project-aware, multi-session conversational system.

Users are not only asking isolated questions.

They may:

* continue a long document over many sessions
* resume prior tasks after interruption
* maintain several concurrent projects
* expect context compression instead of total forgetting
* return after time gaps and expect meaningful recovery

A flatter architecture would make these continuity demands much harder to satisfy in a reliable and explainable way.

The proposed structure allows NORA to:

* separate bounded interaction from persistent goals
* preserve raw dialogue while also compressing it
* recover relevant context intelligently
* manage multiple continuity layers without confusion

That makes it an excellent fit for the system.

---

## Architectural Importance

The `dialogue_and_session/` module provides the conversational continuity architecture through which NORA can maintain structured interaction over time.

While other modules define identity, interaction channels, perception, runtime cognition, planning, action, persistence, and integrations, the live conversational system still requires an explicit architecture that can bound interaction into sessions, preserve ongoing work as persistent conversational projects, store turn history, compress extended context into summaries, and reconstruct usable context when interaction resumes.

Through this module the architecture gains:

* explicit session lifecycle control
* persistent multi-session conversational projects
* structured dialogue-turn history
* bounded summarization and compression mechanisms
* recoverable continuity across interruptions and returns
* clearer separation between raw history, compressed context, and recovered active state
* better support for long-running conversational work

By separating sessions, projects, history, summarization, and recovery into explicit internal subdomains, NORA preserves both conversational depth and architectural clarity.

For that reason, `dialogue_and_session/` is one of the core continuity modules of `src/nora/`.

## Architectural Structure

```text
dialogue_and_session
│
├── Sessions
│   ├── session lifecycle states
│   ├── session models
│   ├── session metadata
│   ├── session boundaries
│   ├── session summaries
│   ├── active session pointers
│   ├── session lifecycle services
│   └── session repository
│
├── Conversational Projects
│   ├── project lifecycle states
│   ├── conversational project models
│   ├── project goals
│   ├── project context
│   ├── project tasks
│   ├── project notes
│   ├── project artifact references
│   ├── project lifecycle services
│   └── project repositories
│
├── Conversational History
│   ├── dialogue speaker categories
│   ├── dialogue turns
│   ├── turn metadata
│   ├── turn content
│   ├── turn modality records
│   ├── interpreted turn annotations
│   ├── history append services
│   ├── history retrieval services
│   ├── history filtering services
│   └── dialogue turn repository
│
├── Summarization and Compression
│   ├── dialogue summaries
│   ├── project summaries
│   ├── summary window definitions
│   ├── compressed context payloads
│   ├── session summarization services
│   ├── project summarization services
│   ├── dialogue-context compression services
│   ├── context reconstruction services
│   └── summarization provider
│
└── Recovery State
    ├── recovery-state models
    ├── recovered context bundles
    ├── project recovery bundles
    ├── session recovery bundles
    ├── recovery-state builders
    ├── last-session recovery services
    ├── project-context recovery services
    ├── recovery validation services
    └── recovery-state repository
```


```
dialogue_and_session/
├── sessions/
│   ├── enums/
│   │   └── session_status_enum.py
│   ├── models/
│   │   ├── dialogue_session.py
│   │   ├── session_metadata.py
│   │   ├── session_boundary.py
│   │   ├── session_summary.py
│   │   └── active_session_pointer.py
│   ├── services/
│   │   ├── create_session_service.py
│   │   ├── activate_session_service.py
│   │   ├── suspend_session_service.py
│   │   ├── terminate_session_service.py
│   │   ├── restore_session_service.py
│   │   └── list_sessions_for_user_service.py
│   └── repositories/
│       └── session_repository.py
│
├── conversational_projects/
│   ├── enums/
│   │   └── project_state_enum.py
│   ├── models/
│   │   ├── conversational_project.py
│   │   ├── project_goal.py
│   │   ├── project_context.py
│   │   ├── project_task.py
│   │   ├── project_note.py
│   │   └── project_artifact_reference.py
│   ├── services/
│   │   ├── create_project_service.py
│   │   ├── initialize_project_service.py
│   │   ├── continue_project_service.py
│   │   ├── pause_project_service.py
│   │   ├── complete_project_service.py
│   │   ├── archive_project_service.py
│   │   └── select_active_project_service.py
│   └── repositories/
│       ├── project_repository.py
│       ├── project_task_repository.py
│       └── project_note_repository.py
│
├── conversational_history/
│   ├── enums/
│   │   └── dialogue_speaker_enum.py
│   ├── models/
│   │   ├── dialogue_turn.py
│   │   ├── turn_metadata.py
│   │   ├── turn_content.py
│   │   ├── turn_modality_record.py
│   │   └── interpreted_turn_annotation.py
│   ├── services/
│   │   ├── append_dialogue_turn_service.py
│   │   ├── get_session_history_service.py
│   │   ├── get_project_history_service.py
│   │   ├── get_user_history_service.py
│   │   └── filter_dialogue_turns_service.py
│   └── repositories/
│       └── dialogue_turn_repository.py
│
├── summarization_and_compression/
│   ├── models/
│   │   ├── dialogue_summary.py
│   │   ├── project_summary.py
│   │   ├── summary_window_definition.py
│   │   └── compressed_context_payload.py
│   ├── services/
│   │   ├── summarize_session_service.py
│   │   ├── summarize_project_service.py
│   │   ├── compress_dialogue_context_service.py
│   │   └── rebuild_context_from_summary_service.py
│   └── providers/
│       └── dialogue_summarization_provider.py
│
└── recovery_state/
    ├── models/
    │   ├── recovery_state.py
    │   ├── recovered_context_bundle.py
    │   ├── project_recovery_bundle.py
    │   └── session_recovery_bundle.py
    ├── services/
    │   ├── build_recovery_state_service.py
    │   ├── recover_last_session_service.py
    │   ├── recover_project_context_service.py
    │   └── validate_recovery_state_service.py
    └── repositories/
        └── recovery_state_repository.py
```

# Planning and Agents Module

## Definition

The `planning_and_agents/` module defines how NORA interprets meaning, identifies user intent, constructs executable plans, selects tools, delegates domain-specific reasoning to specialized agents, and prepares resolved work for downstream execution.

While other architectural modules define identity, interaction channels, perception, runtime cognition, dialogue continuity, action, persistence, backend behavior, integrations, hardware structure, and observability, those modules still do not answer one of the most important questions in the system:

Given what the user or environment has expressed, what should NORA actually do next, and how should it do it?

That is the role of `planning_and_agents/`.

In architectural terms, this module defines the deliberative and task-structuring layer of NORA.

It is the module that transforms interpreted input into action-oriented internal direction.

It determines:

* what the input means at a semantic level
* what the user or system intent most likely is
* whether enough information exists to proceed
* what plan should be constructed
* what tools or capabilities are required
* whether a specialized reasoning agent should handle the task
* how the final result should be prepared for execution downstream

This module therefore defines:

* semantic interpretation structures
* intent detection structures
* planning context and plan objects
* clarification detection and fallback behavior
* tool selection and tool-binding logic
* specialized agent routing and domain-specific reasoning support
* execution-preparation structures that convert planning output into downstream instructions

This module is not the same as dialogue.

Dialogue preserves conversational continuity over time.

Planning and agents determine how meaning becomes actionable direction.

This module is also not the same as the cognitive core.

The cognitive core maintains runtime control state.

Planning and agents determine what to do within that runtime control frame.

For that reason, `planning_and_agents/` is one of the most important reasoning modules in the whole NORA architecture.

---

## Architectural Purpose

The purpose of the `planning_and_agents/` module is to give NORA a structured internal deliberation architecture rather than a shallow direct-response system.

In a system like NORA, incoming input is often not immediately executable.

It may be:

* ambiguous
* incomplete
* multi-step
* tool-dependent
* safety-sensitive
* dependent on prior context
* domain-specific
* interruptible
* partially feasible
* better handled by a specialist than by a generic path

Without a dedicated planning and agents architecture, the system would be forced into brittle direct mappings such as input -> output or request -> tool call.

That would create major architectural weaknesses:

* shallow intent handling
* poor ambiguity management
* weak multi-step execution design
* uncontrolled tool invocation
* difficult recovery after interruption or failure
* no clean delegation to specialized domain reasoning
* lack of clarity around clarification vs execution
* tight coupling between input interpretation and concrete action

By introducing a dedicated planning and agents module, NORA gains:

* structured semantic interpretation
* explicit intent modeling
* bounded detection of missing parameters
* single-step and multi-step planning support
* tool-aware execution preparation
* specialized agent delegation
* failure-aware and interruption-aware replanning
* safer and more explainable task construction

This module therefore provides the architecture of deliberative action selection.

---

## Core Architectural Principle

The most important design principle of this module is the following:

Planning must be separated into semantic interpretation, intent formation, plan construction, tool selection, specialized reasoning delegation, and execution preparation.

These stages are deeply connected, but they are not identical.

### Semantic interpretation

Determines what the input semantically contains.

### Intent detection

Determines what the user or system appears to be trying to achieve.

### Planner

Determines how the objective should be accomplished.

### Tool selector

Determines which available capabilities should be bound to the plan.

### Specialized agents

Determines whether a domain-specific reasoning path should handle the task or a portion of it.

### Execution preparation

Determines how the final planning result becomes a concrete downstream instruction, task, or clarification prompt.

This separation matters because the system should not jump directly from interpreted input to tool execution without passing through explicit internal reasoning structure.

---

## Internal Module Structure

The proposed structure is the following:

```text
planning_and_agents/
├── semantic_interpretation/
├── intent_detection/
├── planner/
├── tool_selector/
├── specialized_agents/
└── execution_preparation/
```

This structure divides the deliberative architecture into six major internal subdomains.

### semantic_interpretation

Defines how input is converted into structured semantic meaning.

### intent_detection

Defines how semantic material is converted into explicit intent objects.

### planner

Defines how actionable plans are built, adapted, validated, and finalized.

### tool_selector

Defines how internal or external capabilities are mapped onto the plan.

### specialized_agents

Defines how domain-specific reasoning or task handling can be delegated.

### execution_preparation

Defines how finalized planning output becomes execution-ready downstream instructions or clarification requests.

This decomposition is crucial because a robust planning architecture must preserve explicit reasoning layers.

---

## Architectural Role Within the Full System

The `planning_and_agents/` module sits between understanding and action.

It receives or depends on:

* interpreted user input
* dialogue context
* active project context
* operational state
* trust and permission context
* environmental and perception-derived context
* tool registries and capability availability
* prior execution outcomes

It then produces:

* semantic representations
* intent objects
* plans or partial plans
* tool-selection results
* specialist-agent delegations
* clarification requests
* fallback strategies
* downstream execution instructions

This means the module is not merely “LLM reasoning.”

It is a structured internal deliberation architecture that sits between conversational understanding and system execution.

---

# 1. semantic_interpretation

## Definition

The `semantic_interpretation/` submodule defines how incoming interpreted input is transformed into structured semantic meaning.

Its purpose is to move from surface input toward an internal representation of meaning that can later support intent detection and planning.

This submodule addresses questions such as:

* what entities are present in the input
* what references are being made
* what dialogue act is being performed
* what ambiguities remain unresolved
* what structured semantic representation best captures the interpreted input

It is not full planning.

It is the semantic grounding step that precedes it.

### Internal Structure

```text
semantic_interpretation/
├── models/
├── services/
└── providers/
```

---

## semantic_interpretation/models/

### semantic_input_object.py

Defines the structured input object entering the semantic interpretation stage.

This may include:

* normalized user input
* dialogue context references
* modality metadata
* speaker or actor context
* relevant prior-turn references
* project or session context

Its role is to provide a consistent semantic-processing entry boundary.

### semantic_representation.py

Defines the structured semantic representation produced from the interpreted input.

This may include extracted entities, resolved references, dialogue-act classification, ambiguity markers, and semantic-role information.

Architecturally, this is one of the key outputs of the submodule.

### extracted_entity.py

Defines the structured representation of an entity extracted from the input.

This may include entity type, surface form, normalized value, confidence, and contextual role.

### reference_resolution_result.py

Defines the structured result of attempting to resolve references in the input.

This may include pronoun resolution, contextual reference linking, object references, session-linked references, or project-linked references.

### dialogue_act_result.py

Defines the structured result of identifying the dialogue act expressed by the input.

This may include acts such as question, command, request, clarification, confirmation, refusal, or continuation.

### semantic_ambiguity_marker.py

Defines the structured representation of unresolved semantic ambiguity.

Its purpose is to keep ambiguity explicit rather than silently collapsing uncertainty into premature assumptions.

---

## semantic_interpretation/services/

### tokenize_interpreted_input_service.py

Defines the operation that tokenizes or segments interpreted input into a form usable for downstream semantic analysis.

Its role is foundational but bounded.

### extract_entities_service.py

Defines the operation that extracts semantic entities from the input.

Its purpose is to identify the objects, people, concepts, places, artifacts, or values relevant to later planning.

### resolve_references_service.py

Defines the operation that resolves references appearing in the input.

Its role is particularly important in multi-turn interaction where users frequently refer to prior items implicitly.

### detect_dialogue_act_service.py

Defines the operation that determines what type of communicative act the input represents.

Its purpose is to distinguish, for example, a question from a command or a clarification from a confirmation.

### enrich_semantic_representation_service.py

Defines the operation that enriches the semantic representation with contextual, relational, or inferred information derived from current conversation state.

### build_semantic_representation_service.py

Defines the operation that assembles the final semantic representation from extracted entities, resolved references, dialogue-act results, and ambiguity markers.

Its purpose is to produce the coherent semantic object consumed by intent detection.

---

## semantic_interpretation/providers/

### entity_extraction_provider.py

Defines the provider boundary through which entity extraction capability is obtained.

Its role is to decouple semantic services from specific NLP or model implementations.

### reference_resolution_provider.py

Defines the provider boundary through which reference-resolution capability is obtained.

Its purpose is to abstract over specific reference-linking technology while preserving consistent semantic-interpretation semantics.

---

# 2. intent_detection

## Definition

The `intent_detection/` submodule defines how semantic meaning is converted into an explicit intent object representing what the user or system is trying to achieve.

Its purpose is to move from “what the input means” to “what objective should be pursued.”

This submodule is responsible for:

* intent-family classification
* intent-parameter discovery
* intent-confidence representation
* completeness evaluation
* missing-parameter detection
* construction of explicit intent objects

### Internal Structure

```text
intent_detection/
├── enums/
├── models/
├── services/
└── providers/
```

---

## intent_detection/enums/

### intent_family_enum.py

Defines the recognized families of intent in the NORA system.

This may include categories such as information request, task execution, planning request, scheduling action, document operation, coding request, navigation request, control request, or conversational continuation.

Its purpose is to give intent classification an explicit ontology.

### intent_completeness_status_enum.py

Defines the status of intent completeness.

This may include states such as complete, partially specified, ambiguous, underdetermined, or clarification required.

Its role is especially important because planning should not proceed as if an incomplete intent were fully specified.

---

## intent_detection/models/

### intent_object.py

Defines the primary structured representation of an intent.

This model may include:

* intent family
* resolved parameters
* missing parameters
* confidence information
* contextual constraints
* completeness state

Architecturally, this is one of the most important internal objects in the module.

### required_parameter_definition.py

Defines a parameter that is required for a given intent family or plan type.

Its purpose is to make intent completeness rules explicit.

### intent_argument_value.py

Defines the structured value of an argument associated with an intent.

Its role is to preserve normalized parameter values, value confidence, and possible uncertainty.

### intent_confidence_score.py

Defines the structured representation of intent confidence.

Its purpose is to preserve uncertainty and allow the planner to distinguish strong intent identification from weak or uncertain classification.

---

## intent_detection/services/

### classify_intent_service.py

Defines the operation that classifies the most likely intent family from the semantic representation.

Its role is to provide the initial explicit task orientation for later planning.

### detect_missing_parameters_service.py

Defines the operation that identifies which required parameters are missing from the current intent representation.

Its purpose is essential for deciding whether clarification is needed.

### evaluate_intent_completeness_service.py

Defines the operation that determines the completeness status of the current intent.

Its role is to decide whether the planner can proceed, should request clarification, or should defer.

### build_intent_object_service.py

Defines the operation that assembles the final intent object from classified intent family, resolved arguments, confidence values, and completeness assessment.

Its purpose is to produce the explicit planning input.

---

## intent_detection/providers/

### intent_classification_provider.py

Defines the provider boundary through which intent-classification capability is obtained.

Its purpose is to abstract over the concrete classification engine while preserving stable intent-detection semantics.

---

# 3. planner

## Definition

The `planner/` submodule defines how NORA constructs a plan for achieving an identified intent under current contextual constraints.

Its purpose is to transform explicit intent into a structured plan that may be single-step or multi-step, direct or clarification-first, optimistic or fallback-aware.

This submodule is the deliberative core of the module.

It is responsible for:

* planning context construction
* single-step planning
* multi-step planning
* clarification detection
* interruption-aware replanning
* failure-aware replanning
* final planning-result construction
* planning feasibility and safety constraints

### Internal Structure

```text
planner/
├── models/
├── services/
└── policies/
```

---

## planner/models/

### plan_object.py

Defines the primary structured representation of a plan.

This model may include:

* plan identifier
* associated intent
* planning steps
* selected strategy
* required tools
* clarification requirements
* fallback options
* feasibility and safety metadata

Architecturally, this is the central planning artifact.

### planning_step_object.py

Defines the structured representation of an individual step within a plan.

Its purpose is to make multi-step planning explicit and inspectable.

### planning_context.py

Defines the structured context in which planning occurs.

This may include dialogue context, project state, operational conditions, permissions, subsystem availability, environmental constraints, and recent execution history.

Its role is to ensure the planner operates with the correct situational frame.

### planning_result.py

Defines the structured output of the planning process.

This may include plan status, finalized plan object, clarification requests, feasibility decisions, and fallback or replan information.

### clarification_request_object.py

Defines the structured representation of a clarification request that must be asked before safe or meaningful execution can proceed.

Its role is important because planning often detects that execution should not start yet.

### execution_strategy.py

Defines the structured representation of how the plan should be executed.

This may include direct execution, staged execution, deferred execution, monitored execution, or agent-routed execution.

### fallback_strategy.py

Defines the structured representation of how the system should respond when the preferred plan cannot be executed as intended.

Its purpose is to preserve robustness and graceful degradation.

---

## planner/services/

### build_planning_context_service.py

Defines the operation that assembles the planning context from upstream modules and current runtime state.

Its purpose is to ensure planning does not occur in an informational vacuum.

### construct_single_step_plan_service.py

Defines the operation that constructs a direct single-step plan when the intent is straightforward and execution can be represented in one bounded action.

### construct_multi_step_plan_service.py

Defines the operation that constructs a multi-step plan when the task requires ordered subtasks, dependencies, or staged execution.

Its role is crucial for more complex tasks.

### detect_clarification_requirement_service.py

Defines the operation that determines whether clarification is required before a plan can be safely or meaningfully finalized.

Its purpose is to prevent false certainty and premature execution.

### replan_after_interruption_service.py

Defines the operation that constructs a revised plan after an interruption alters the execution context.

Its role is important in a live interactive system where tasks may be paused, redirected, or interrupted.

### replan_after_failure_service.py

Defines the operation that constructs a revised plan after a prior plan or step fails.

Its purpose is to provide resilience and adaptive recovery.

### finalize_planning_result_service.py

Defines the operation that assembles the final planning result object from candidate plans, clarification needs, feasibility checks, and fallback logic.

Its purpose is to produce the authoritative planner output.

---

## planner/policies/

### planning_feasibility_policy.py

Defines the policy that evaluates whether a candidate plan is feasible under current conditions.

This may include capability availability, parameter sufficiency, dependency readiness, or contextual constraints.

### planning_safety_policy.py

Defines the policy that evaluates whether a candidate plan is safe to pursue.

Its role is especially important when plans may lead to external communication, file changes, scheduling side effects, or hardware-related action.

### planning_context_adaptation_policy.py

Defines the policy that adapts planning behavior based on current context.

Its purpose is to let the planning system change its structure or conservatism depending on runtime conditions such as urgency, interruption state, user preferences, or system constraints.

---

# 4. tool_selector

## Definition

The `tool_selector/` submodule defines how plans are mapped to available capabilities, tools, or execution backends.

Its purpose is to make capability binding explicit rather than embedding tool decisions implicitly inside the planner or downstream execution layers.

This submodule is responsible for:

* identifying candidate tools from intent and plan structure
* selecting primary and secondary tools
* validating tool availability
* binding selected tools into execution-ready tool associations
* maintaining registries of available internal and external tools

### Internal Structure

```text
tool_selector/
├── models/
├── services/
└── registries/
```

---

## tool_selector/models/

### tool_binding.py

Defines the structured representation of a binding between a plan or task and a selected tool.

Its purpose is to make capability assignment explicit and inspectable.

### tool_selection_request.py

Defines the structured request given to the tool selector.

This may include intent family, plan shape, required capabilities, constraints, and context information.

### tool_selection_result.py

Defines the structured result of the tool-selection process.

This may include selected primary tool, secondary tools, rejected candidates, availability status, and binding metadata.

### tool_capability_descriptor.py

Defines the structured representation of what a tool is capable of doing.

Its purpose is to support capability-aware matching between tasks and tools.

---

## tool_selector/services/

### map_intent_to_tool_candidates_service.py

Defines the operation that maps an intent or plan requirement into a set of candidate tools.

Its role is to narrow the capability search space before final selection.

### select_primary_tool_service.py

Defines the operation that chooses the main tool best suited for executing the required task.

Its purpose is to identify the principal capability binding.

### select_secondary_tools_service.py

Defines the operation that chooses supporting or fallback tools that may assist or substitute for the primary tool.

### validate_tool_availability_service.py

Defines the operation that checks whether the selected tool candidates are actually available and usable under current runtime conditions.

Its role is essential because registered capability is not the same as currently available capability.

### build_tool_binding_service.py

Defines the operation that constructs the final tool-binding structures used downstream.

Its purpose is to turn selection results into execution-usable form.

---

## tool_selector/registries/

### internal_tool_registry.py

Defines the registry of internal capabilities and tools available within NORA itself.

Its purpose is to expose built-in execution capabilities to the selection system.

### external_tool_registry.py

Defines the registry of external capabilities and service-backed tools available through integrations.

Its role is to preserve explicit visibility into externally provided tool options.

---

# 5. specialized_agents

## Definition

The `specialized_agents/` submodule defines how NORA delegates certain classes of work to domain-specific reasoning or execution agents.

Its purpose is to preserve modular expertise instead of forcing all tasks through one general planning path.

This submodule is especially important because some tasks benefit from specialized internal behavior, specialized reasoning structure, or domain-tuned outputs.

This area therefore includes:

* tutoring-oriented reasoning
* document-analysis reasoning
* scheduling-oriented reasoning
* coding-oriented reasoning
* route-planning reasoning
* agent-routing and dispatch logic

### Internal Structure

```text
specialized_agents/
├── tutoring_agent/
├── document_analysis_agent/
├── scheduling_agent/
├── coding_agent/
├── route_planning_agent/
└── agent_router/
```

Each agent family contains bounded request/result models and services specific to that domain.

---

## tutoring_agent/

### tutoring_agent_request.py

Defines the structured request object passed to the tutoring agent.

Its purpose is to make tutoring-specific reasoning input explicit.

### tutoring_agent_result.py

Defines the structured result produced by the tutoring agent.

This may include explanation content, scaffolding decisions, pedagogical structure, or next-step suggestions.

### tutoring_explanation_service.py

Defines the service that builds tutoring-oriented explanations.

Its role is to provide educationally shaped reasoning or explanation output.

### tutoring_followup_builder_service.py

Defines the service that builds follow-up prompts, checks, or continuation suggestions appropriate to a tutoring context.

---

## document_analysis_agent/

### document_analysis_request.py

Defines the structured request object passed to the document-analysis agent.

### document_analysis_result.py

Defines the structured result produced by the document-analysis agent.

This may include summaries, themes, extracted findings, or structural analysis.

### document_summary_service.py

Defines the service that generates document-oriented summaries within the specialized document-analysis path.

### document_theme_extraction_service.py

Defines the service that extracts document themes, topics, or structural semantic groupings.

---

## scheduling_agent/

### scheduling_agent_request.py

Defines the structured request object passed to the scheduling agent.

### scheduling_agent_result.py

Defines the structured result produced by the scheduling agent.

This may include resolved availability, proposed options, constraints, or scheduled outcomes.

### availability_resolution_service.py

Defines the service that resolves availability-related information in the scheduling path.

### schedule_proposal_builder_service.py

Defines the service that constructs proposed schedule options or scheduling recommendations.

---

## coding_agent/

### coding_agent_request.py

Defines the structured request object passed to the coding agent.

### coding_agent_result.py

Defines the structured result produced by the coding agent.

This may include generated code, refactoring results, implementation recommendations, or code-structure outputs.

### code_generation_service.py

Defines the service that generates or drafts code within the coding-agent path.

### code_refactor_service.py

Defines the service that performs or proposes structured refactoring within the coding-agent path.

---

## route_planning_agent/

### route_planning_agent_request.py

Defines the structured request object passed to the route-planning agent.

### route_planning_agent_result.py

Defines the structured result produced by the route-planning agent.

This may include route options, travel constraints, ordering choices, and route recommendations.

### route_option_builder_service.py

Defines the service that constructs candidate route options.

### route_explanation_service.py

Defines the service that explains route choices or route tradeoffs.

---

## agent_router/

### agent_assignment.py

Defines the structured representation of an agent assignment decision.

Its purpose is to make agent delegation explicit and inspectable.

### resolve_agent_assignment_service.py

Defines the service that determines which specialized agent, if any, should receive a given request.

Its role is to preserve clear delegation rules.

### dispatch_request_to_agent_service.py

Defines the service that dispatches a structured request to the chosen specialized agent path.

Its purpose is to make actual agent delegation operational.

---

# 6. execution_preparation

## Definition

The `execution_preparation/` submodule defines how finalized planning output becomes something that downstream execution layers can act on directly.

Its purpose is to bridge planning and execution without forcing downstream systems to reinterpret planner objects from scratch.

This submodule is responsible for:

* representing execution-ready work
* representing unresolved-parameter bundles
* building downstream execution instructions
* building clarification prompts when execution cannot proceed yet
* publishing finalized planning results downstream

### Internal Structure

```text
execution_preparation/
├── models/
└── services/
```

---

## execution_preparation/models/

### execution_ready_task.py

Defines the structured representation of a task that is ready to be executed downstream.

This may include tool bindings, resolved parameters, execution strategy, and execution metadata.

### unresolved_parameter_bundle.py

Defines the structured representation of parameters still missing or unresolved after planning.

Its purpose is to preserve why execution cannot yet proceed fully.

### downstream_execution_instruction.py

Defines the structured instruction object produced for downstream execution systems.

Its role is to provide a clean execution-facing contract.

---

## execution_preparation/services/

### build_downstream_execution_instruction_service.py

Defines the operation that transforms finalized planning results into execution-facing instruction objects.

Its purpose is to make execution preparation explicit and bounded.

### build_clarification_prompt_service.py

Defines the operation that transforms unresolved planning requirements into a clarification prompt suitable for dialogue continuation.

Its role is crucial because not every planning result should lead directly to execution.

### publish_planning_result_service.py

Defines the operation that publishes or forwards the planning result into the relevant downstream layers.

Its purpose is to bridge the planner and the rest of the runtime in a structured way.

---

## Cross-Submodule Architectural Relationships

The planning and agents module is best understood as a deliberative pipeline rather than as six isolated folders.

### semantic_interpretation -> intent_detection

Semantic interpretation provides the structured meaning from which intent is built.

### intent_detection -> planner

Intent detection provides the explicit objective that the planner must act on.

### planner -> tool_selector

The planner determines what must be done.

The tool selector determines what capabilities should do it.

### planner -> specialized_agents

Some planning contexts may require delegation to specialized agents for better domain performance.

### specialized_agents -> execution_preparation

Specialized agent results may need to be packaged into execution-ready or dialogue-ready outputs.

### tool_selector -> execution_preparation

Execution preparation depends on selected tools and their bindings when building downstream instructions.

### planner -> execution_preparation

Clarification needs, fallback strategies, and execution strategies all feed into execution preparation.

These relationships show the overall logic clearly:

* meaning is interpreted
* intent is made explicit
* a plan is built
* tools and specialist paths are resolved
* execution-ready output is prepared

---

## What This Module Must Not Contain

To preserve architectural clarity, the planning and agents module should not absorb responsibilities that belong elsewhere.

It should not contain:

* direct frontend rendering logic
* raw transport-layer request handling
* long-term memory storage ownership
* finite-state-machine control ownership
* low-level hardware-driver logic
* persistence repository logic unrelated to planning state
* final action execution implementation
* raw perception-engine implementation

It may depend on all of those inputs or produce outputs for them, but it must remain the deliberative planning and delegation layer.

---

## Interaction With Other Modules

The `planning_and_agents/` module interacts with many other architectural domains.

### shared

Uses shared identifiers, operation models, exceptions, modality metadata, retry structures, and common support abstractions.

### identity_access_security

Consumes permission context, active user capability information, and trust-sensitive constraints that may affect feasible or allowed planning paths.

### interaction_interfaces

Consumes normalized interaction-origin input that becomes semantic and intent-level planning material.

### perception

Consumes perception-derived contextual signals, speech results, identity cues, and environment information that may influence intent resolution or planning context.

### cognitive_core

Depends on operational state, active context, interruption signals, and runtime control conditions when building or adapting plans.

### dialogue_and_session

Uses session context, project continuity, recent dialogue structure, summaries, and recovery context to ground planning in ongoing conversation.

### action_and_expression

Produces outputs that eventually become expressions, actions, communications, or device-control sequences downstream.

### persistence_and_memory

May store selected planning artifacts, agent outputs, or execution-preparation traces depending on overall architecture.

### backend_and_application

Provides planning results, clarification requirements, and downstream instructions to coordinators, application services, and event dispatch systems.

### frontend_support

May supply planning-state representations, clarification structures, or explainability information for frontend consumption.

### integrations_and_external_services

Depends on external engines, LLMs, search services, productivity tools, and other capability providers when selecting tools or routing agent work.

### infrastructure_and_hardware

Consumes hardware-availability and hardware-safety information indirectly through planning context and may produce plans that eventually involve embodied execution.

### observability

Exposes plan construction traces, tool-selection decisions, fallback behavior, and agent-delegation paths for diagnostics and monitoring.

---

## Design Constraints of the Module

The `planning_and_agents/` module should obey several strict architectural constraints.

### 1. Semantic interpretation and intent detection must remain distinct

Meaning extraction is not the same as objective determination.

### 2. Planning must remain explicit

Plans, steps, strategies, and fallback behavior should be structured and inspectable rather than hidden in opaque direct-response logic.

### 3. Clarification must be first-class

If information is missing or ambiguity is too high, the module should preserve that explicitly rather than hallucinating premature certainty.

### 4. Tool selection must remain explicit and capability-aware

The system should not invoke tools as a hidden side effect of vague planning behavior.

### 5. Specialized agents must remain bounded and domain-specific

Agents should exist where they add meaningful modular expertise, not as arbitrary duplication of the generic planner.

### 6. Execution preparation must remain separate from execution itself

This module may prepare downstream work, but it should not become the final action-execution layer.

### 7. Replanning must be supported explicitly

Interruptions and failures are normal in a live system, so the architecture must make replanning a first-class concept.

### 8. Safety and feasibility constraints must be visible

A plan is not valid merely because it is logically possible.

It must also be feasible and safe under current conditions.

---

## Testing Implications

This module requires especially strong reasoning-structure testing because errors here affect the system’s ability to choose appropriate next actions.

Important testing categories include:

* semantic-representation construction tests
* entity-extraction tests
* reference-resolution tests
* dialogue-act detection tests
* intent classification tests
* missing-parameter detection tests
* intent completeness tests
* planning-context construction tests
* single-step planning tests
* multi-step planning tests
* clarification-detection tests
* replan-after-interruption tests
* replan-after-failure tests
* feasibility-policy tests
* safety-policy tests
* tool-candidate mapping tests
* primary and secondary tool-selection tests
* tool-availability validation tests
* agent-assignment tests
* agent-dispatch tests
* execution-instruction building tests
* clarification-prompt building tests

Failures here can make NORA sound fluent while still behaving incorrectly, which is one of the most dangerous architectural failure modes in a system like this.

---

## Why This Structure Fits NORA

This structure fits NORA because NORA is not only reactive, and it is not only conversational.

It is a system that must often:

* interpret nontrivial user requests
* recover meaning from context
* decide whether enough information is available
* build single-step or multi-step plans
* select available tools intelligently
* delegate to domain-specialized reasoning paths
* recover from interruption or failure
* prepare execution without collapsing into direct tool invocation

A flatter architecture would make these functions difficult to inspect, test, and extend.

The proposed structure allows NORA to:

* preserve an explicit reasoning pipeline
* separate meaning, intent, and planning clearly
* integrate tools and specialist agents in a modular way
* support clarification and replanning as first-class behaviors
* produce clean execution-ready downstream instructions

That makes it an excellent fit for the system.

---

## Architectural Importance

The `planning_and_agents/` module provides the deliberative reasoning architecture through which NORA decides what to do and how to do it.

While other modules define interaction, perception, runtime control, conversational continuity, action, persistence, and integrations, the live system still requires an explicit internal architecture that can transform interpreted meaning into intent, transform intent into plans, map plans onto available tools, route domain-specific problems to specialized agents, and prepare final results for downstream execution or clarification.

Through this module the architecture gains:

* structured semantic interpretation
* explicit intent modeling
* single-step and multi-step planning support
* clarification-aware execution gating
* tool-aware capability binding
* modular specialized-agent delegation
* failure-aware and interruption-aware replanning
* clean preparation of downstream execution instructions

By separating semantic interpretation, intent detection, planning, tool selection, specialized agents, and execution preparation into explicit internal subdomains, NORA preserves both deliberative power and architectural clarity.

For that reason, `planning_and_agents/` is one of the most important reasoning modules of `src/nora/`.

## Architectural Structure

```text
planning_and_agents
│
├── Semantic Interpretation
│   ├── semantic input objects
│   ├── semantic representations
│   ├── extracted entities
│   ├── reference-resolution results
│   ├── dialogue-act results
│   ├── semantic ambiguity markers
│   ├── tokenization services
│   ├── entity-extraction services
│   ├── reference-resolution services
│   ├── dialogue-act detection services
│   ├── semantic-enrichment services
│   ├── semantic-representation builders
│   └── semantic providers
│
├── Intent Detection
│   ├── intent families
│   ├── intent completeness states
│   ├── intent objects
│   ├── required parameter definitions
│   ├── intent argument values
│   ├── intent confidence scores
│   ├── intent-classification services
│   ├── missing-parameter detection services
│   ├── completeness-evaluation services
│   ├── intent-object builders
│   └── intent-classification provider
│
├── Planner
│   ├── plan objects
│   ├── planning steps
│   ├── planning context
│   ├── planning results
│   ├── clarification request objects
│   ├── execution strategies
│   ├── fallback strategies
│   ├── planning-context builders
│   ├── single-step planning services
│   ├── multi-step planning services
│   ├── clarification-detection services
│   ├── interruption-replanning services
│   ├── failure-replanning services
│   ├── planning-result finalization services
│   └── planning policies
│
├── Tool Selector
│   ├── tool bindings
│   ├── tool-selection requests
│   ├── tool-selection results
│   ├── tool capability descriptors
│   ├── intent-to-tool mapping services
│   ├── primary-tool selection services
│   ├── secondary-tool selection services
│   ├── tool-availability validation services
│   ├── tool-binding builders
│   └── tool registries
│
├── Specialized Agents
│   ├── tutoring agent
│   ├── document-analysis agent
│   ├── scheduling agent
│   ├── coding agent
│   ├── route-planning agent
│   └── agent router
│
└── Execution Preparation
    ├── execution-ready tasks
    ├── unresolved-parameter bundles
    ├── downstream execution instructions
    ├── execution-instruction builders
    ├── clarification-prompt builders
    └── planning-result publication services
```

```
planning_and_agents/
├── semantic_interpretation/
│   ├── models/
│   │   ├── semantic_input_object.py
│   │   ├── semantic_representation.py
│   │   ├── extracted_entity.py
│   │   ├── reference_resolution_result.py
│   │   ├── dialogue_act_result.py
│   │   └── semantic_ambiguity_marker.py
│   ├── services/
│   │   ├── tokenize_interpreted_input_service.py
│   │   ├── extract_entities_service.py
│   │   ├── resolve_references_service.py
│   │   ├── detect_dialogue_act_service.py
│   │   ├── enrich_semantic_representation_service.py
│   │   └── build_semantic_representation_service.py
│   └── providers/
│       ├── entity_extraction_provider.py
│       └── reference_resolution_provider.py
│
├── intent_detection/
│   ├── enums/
│   │   ├── intent_family_enum.py
│   │   └── intent_completeness_status_enum.py
│   ├── models/
│   │   ├── intent_object.py
│   │   ├── required_parameter_definition.py
│   │   ├── intent_argument_value.py
│   │   └── intent_confidence_score.py
│   ├── services/
│   │   ├── classify_intent_service.py
│   │   ├── detect_missing_parameters_service.py
│   │   ├── evaluate_intent_completeness_service.py
│   │   └── build_intent_object_service.py
│   └── providers/
│       └── intent_classification_provider.py
│
├── planner/
│   ├── models/
│   │   ├── plan_object.py
│   │   ├── planning_step_object.py
│   │   ├── planning_context.py
│   │   ├── planning_result.py
│   │   ├── clarification_request_object.py
│   │   ├── execution_strategy.py
│   │   └── fallback_strategy.py
│   ├── services/
│   │   ├── build_planning_context_service.py
│   │   ├── construct_single_step_plan_service.py
│   │   ├── construct_multi_step_plan_service.py
│   │   ├── detect_clarification_requirement_service.py
│   │   ├── replan_after_interruption_service.py
│   │   ├── replan_after_failure_service.py
│   │   └── finalize_planning_result_service.py
│   └── policies/
│       ├── planning_feasibility_policy.py
│       ├── planning_safety_policy.py
│       └── planning_context_adaptation_policy.py
│
├── tool_selector/
│   ├── models/
│   │   ├── tool_binding.py
│   │   ├── tool_selection_request.py
│   │   ├── tool_selection_result.py
│   │   └── tool_capability_descriptor.py
│   ├── services/
│   │   ├── map_intent_to_tool_candidates_service.py
│   │   ├── select_primary_tool_service.py
│   │   ├── select_secondary_tools_service.py
│   │   ├── validate_tool_availability_service.py
│   │   └── build_tool_binding_service.py
│   └── registries/
│       ├── internal_tool_registry.py
│       └── external_tool_registry.py
│
├── specialized_agents/
│   ├── tutoring_agent/
│   │   ├── tutoring_agent_request.py
│   │   ├── tutoring_agent_result.py
│   │   ├── tutoring_explanation_service.py
│   │   └── tutoring_followup_builder_service.py
│   ├── document_analysis_agent/
│   │   ├── document_analysis_request.py
│   │   ├── document_analysis_result.py
│   │   ├── document_summary_service.py
│   │   └── document_theme_extraction_service.py
│   ├── scheduling_agent/
│   │   ├── scheduling_agent_request.py
│   │   ├── scheduling_agent_result.py
│   │   ├── availability_resolution_service.py
│   │   └── schedule_proposal_builder_service.py
│   ├── coding_agent/
│   │   ├── coding_agent_request.py
│   │   ├── coding_agent_result.py
│   │   ├── code_generation_service.py
│   │   └── code_refactor_service.py
│   ├── route_planning_agent/
│   │   ├── route_planning_agent_request.py
│   │   ├── route_planning_agent_result.py
│   │   ├── route_option_builder_service.py
│   │   └── route_explanation_service.py
│   └── agent_router/
│       ├── agent_assignment.py
│       ├── resolve_agent_assignment_service.py
│       └── dispatch_request_to_agent_service.py
│
└── execution_preparation/
    ├── models/
    │   ├── execution_ready_task.py
    │   ├── unresolved_parameter_bundle.py
    │   └── downstream_execution_instruction.py
    ├── services/
    │   ├── build_downstream_execution_instruction_service.py
    │   ├── build_clarification_prompt_service.py
    │   └── publish_planning_result_service.py
```

# Action and Expression Module

## Definition

The `action_and_expression/` module defines how NORA produces observable outputs and performs effective operations in the physical and digital environment.

While other architectural modules define identity, interaction channels, perception, runtime cognition, dialogue continuity, planning, persistence, backend behavior, integrations, hardware structure, and observability, those modules still do not by themselves make the system do anything visible, audible, tangible, or externally consequential.

That is the role of `action_and_expression/`.

In architectural terms, this module defines the execution and outward manifestation layer of NORA.

It is the module that transforms internal decisions into concrete external effects such as:

* spoken responses
* multimedia playback
* screen updates
* emotional or expressive feedback
* physical movement
* image and video capture
* device-control operations
* external notifications and communications

This module therefore defines:

* voice output generation and playback
* sound and multimedia behavior
* screen and visual output composition
* emotional and expressive signaling
* physical movement and posture control
* camera-triggered media capture
* IoT and external device control
* outbound communication through messaging, email, or webhook channels

This module is not the same as planning.

Planning determines what should be done.

Action and expression determine how that decision becomes an externally visible effect.

This module is also not the same as frontend rendering.

Frontend and visualization define interactive visual environments.

Action and expression define output behavior and execution channels whether those outputs are frontend-facing, embodied, auditory, or externally dispatched.

For that reason, `action_and_expression/` is one of the core execution modules of NORA.

---

## Architectural Purpose

The purpose of the `action_and_expression/` module is to give NORA a disciplined and modular output architecture.

A system like NORA does not merely reason internally.

It must eventually:

* speak
* display
* notify
* move
* capture media
* actuate devices
* send messages
* express internal state outwardly

Without a dedicated execution-and-expression module, outward behavior tends to become fragmented across backend handlers, planner logic, hardware drivers, UI code, and integration-specific utilities.

That creates major architectural problems such as:

* unclear ownership of output behavior
* poor separation between decision and execution
* mixed digital and physical actuation logic
* difficult safety control over movement or device operations
* weak coordination between voice, visual output, and emotional expression
* inconsistent communication handling across channels
* poor extensibility for new output mechanisms

By introducing a dedicated action and expression architecture, NORA gains:

* explicit output channels
* separation between internal reasoning and external execution
* cleaner multimodal response composition
* safer embodied action boundaries
* more consistent external communication behavior
* better reuse of execution abstractions across channels
* easier coordination of physical and digital outputs

This module therefore gives NORA a proper expression and actuation architecture rather than a scattered set of side effects.

---

## Core Architectural Principle

The most important design principle of this module is the following:

Execution and outward expression must be separated by channel and by effect type.

This means the module should not collapse all outputs into one generic “execute” layer.

Different output and action channels have different constraints.

### Voice output

Requires speech construction, voice selection, synthesis, and playback.

### Multimedia output

Requires playback sourcing, queueing, and audio coordination.

### Screen output

Requires visual composition, rendering, and display updating.

### Emotional expression

Requires coordinated expressive signaling across voice and visual behavior.

### Physical movement

Requires safety validation and actuator-command construction.

### Camera actions

Require capture requests, media artifact creation, and storage.

### IoT and device control

Require permission checks, target resolution, and protocol-specific control.

### External communication

Requires delivery-channel logic, messaging structures, and auditability.

This separation matters because “output” is not one thing.

NORA needs a modular execution architecture capable of spanning voice, interface, embodiment, capture, control, and communication.

---

## Internal Module Structure

The proposed structure is the following:

```text
action_and_expression/
├── voice_output/
├── sound_and_multimedia/
├── screen_and_visual_output/
├── emotional_expression/
├── movement_and_physical_behavior/
├── camera_actions/
├── iot_and_device_control/
└── external_communication/
```

This structure divides execution and expression into eight explicit subdomains.

### voice_output

Defines spoken output generation and playback.

### sound_and_multimedia

Defines sound cues, media playback, and audio-mixing behavior.

### screen_and_visual_output

Defines screen-bound visual output and display updates.

### emotional_expression

Defines expressive or emotionally modulated output signaling.

### movement_and_physical_behavior

Defines movement and posture-related embodied behavior.

### camera_actions

Defines image and video capture behavior.

### iot_and_device_control

Defines external device-control actions.

### external_communication

Defines outbound digital communication across external channels.

This decomposition is important because outward effect channels are operationally different and should remain inspectable and separable.

---

## Architectural Role Within the Full System

The `action_and_expression/` module sits downstream of planning, runtime control, and contextual reasoning.

It receives or depends on:

* planning results
* execution strategies
* operational-state permissions
* behavioral modulation state
* active user and profile preferences
* hardware safety constraints
* tool and integration availability
* communication targets and payloads

It then produces concrete effects in the world.

These effects may be:

* auditory
* visual
* physical
* device-directed
* media-capture oriented
* digitally communicative

This means the module is not a passive renderer of text.

It is the architecture of externalized system behavior.

---

# 1. voice_output

## Definition

The `voice_output/` submodule defines how NORA produces spoken output.

Its purpose is to convert internal response content into speech-ready structures, apply voice-specific formatting or markup, resolve the correct voice profile, synthesize speech, and play it back to the user.

This submodule is essential because spoken interaction is one of the main outward expression channels of NORA.

### Internal Structure

```text
voice_output/
├── models/
├── services/
└── providers/
```

---

## voice_output/models/

### spoken_response.py

Defines the structured representation of a spoken response prior to synthesis.

This model may include:

* response text
* speaking intent or category
* target language
* speaking pace hints
* emphasis hints
* interruption policy
* associated expressive metadata

Its purpose is to separate spoken-output semantics from low-level synthesis details.

### speech_markup_payload.py

Defines the structured payload containing speech-specific markup or prosody instructions.

This may include pauses, emphasis, pronunciation guidance, pacing directives, or synthesis-control metadata.

Its role is to make speech rendering richer and more controllable.

### voice_profile.py

Defines the structured representation of the voice profile to be used.

This may include voice identity, language, timbre category, pacing defaults, emotional compatibility, and playback preferences.

### speech_playback_request.py

Defines the structured request used to trigger playback of synthesized speech.

Its role is to separate synthesis output from playback behavior.

---

## voice_output/services/

### build_spoken_response_service.py

Defines the operation that constructs the spoken response object from upstream response content and runtime context.

Its purpose is to produce speech-oriented output rather than generic text.

### apply_speech_markup_service.py

Defines the operation that applies speech markup to a spoken response.

Its role is to enrich raw verbal content with prosodic or pronunciation control.

### resolve_voice_profile_service.py

Defines the operation that selects the effective voice profile for the current output.

Its purpose is to incorporate user preferences, language requirements, and modulation state.

### synthesize_speech_service.py

Defines the operation that converts speech-ready content into synthesized audio.

Its role is to bridge high-level spoken-response structure and low-level speech-generation capability.

### play_synthesized_speech_service.py

Defines the operation that plays synthesized speech through the active audio output channel.

Its purpose is to finalize spoken output delivery.

---

## voice_output/providers/

### text_to_speech_provider.py

Defines the provider boundary through which text-to-speech capability is obtained.

Its purpose is to decouple voice-output semantics from specific TTS engines.

### speech_playback_provider.py

Defines the provider boundary through which synthesized speech is played back.

Its role is to abstract playback hardware or playback-engine specifics.

---

# 2. sound_and_multimedia

## Definition

The `sound_and_multimedia/` submodule defines how NORA plays sounds, media, and mixed audio outputs beyond pure speech.

Its purpose is to support media-oriented and nonverbal audio expression such as:

* music playback
* sound cues
* media queueing
* ambient audio
* multi-source audio coordination

This submodule is important because auditory output is broader than speech.

### Internal Structure

```text
sound_and_multimedia/
├── models/
├── services/
└── providers/
```

---

## sound_and_multimedia/models/

### media_playback_request.py

Defines the structured request to play a media source.

This may include media identifier, source type, playback mode, volume hints, and queueing behavior.

### sound_signal_request.py

Defines the structured request to play a bounded sound signal or sound cue.

Its purpose is to represent short nonverbal audio effects distinctly from general media playback.

### media_queue_item.py

Defines the structured representation of an item stored in a media playback queue.

Its role is important for ordered or deferred multimedia behavior.

### playback_state_snapshot.py

Defines the structured snapshot of current playback state.

This may include currently playing source, queue state, elapsed time, paused status, and output routing information.

---

## sound_and_multimedia/services/

### resolve_media_source_service.py

Defines the operation that resolves a requested media reference into a concrete playable source.

Its purpose is to translate abstract media requests into operational playback inputs.

### enqueue_media_playback_service.py

Defines the operation that inserts requested media into the playback queue.

### start_media_playback_service.py

Defines the operation that starts playback of media or sound output.

### pause_media_playback_service.py

Defines the operation that pauses active playback.

### stop_media_playback_service.py

Defines the operation that stops playback.

Its purpose is to support explicit control over multimedia output state.

### mix_audio_output_service.py

Defines the operation that coordinates or mixes multiple audio output streams when such behavior is supported.

Its role is especially important when voice, cues, and media may overlap or need controlled coexistence.

---

## sound_and_multimedia/providers/

### media_stream_provider.py

Defines the provider boundary through which media streams or playable media content are obtained.

### audio_output_provider.py

Defines the provider boundary through which general non-speech audio output is delivered.

Its role is broader than speech playback and covers media-oriented audio output.

---

# 3. screen_and_visual_output

## Definition

The `screen_and_visual_output/` submodule defines how NORA produces visual output on local or directly managed display surfaces.

Its purpose is to compose visual messages, build state indicators, render screen payloads, and update or clear the display.

This submodule is important because visible system feedback is a primary expression channel in multimodal environments.

### Internal Structure

```text
screen_and_visual_output/
├── models/
├── services/
└── providers/
```

---

## screen_and_visual_output/models/

### visual_message.py

Defines the structured representation of a visual message to be shown.

This may include text, layout hints, priority, icon associations, and message category.

### graphical_element.py

Defines the structured representation of an individual graphical element used in visual composition.

Its role is to represent visual building blocks such as icons, badges, charts, indicators, or widgets.

### visual_state_indicator.py

Defines the structured representation of a state indicator intended to communicate runtime posture, status, or condition visually.

### rendered_screen_payload.py

Defines the structured rendered payload ready to be pushed to a display surface.

Its purpose is to separate visual composition logic from actual display update delivery.

### display_update_request.py

Defines the structured request used to apply a visual update to the display system.

---

## screen_and_visual_output/services/

### compose_visual_message_service.py

Defines the operation that composes visual messages from upstream content and state information.

Its purpose is to convert abstract information into display-oriented structures.

### render_screen_payload_service.py

Defines the operation that renders visual structures into a payload suitable for the local display system.

### build_state_indicator_service.py

Defines the operation that constructs visual status indicators for runtime state, health, activity, or mode representation.

### update_display_service.py

Defines the operation that pushes an update to the display surface.

### clear_display_service.py

Defines the operation that clears or resets the display surface.

Its role is important when visual state must be explicitly removed or refreshed.

---

## screen_and_visual_output/providers/

### local_display_provider.py

Defines the provider boundary through which local display updates are delivered.

Its purpose is to abstract display hardware or display-driver implementation details.

---

# 4. emotional_expression

## Definition

The `emotional_expression/` submodule defines how internal behavioral modulation becomes outward expressive feedback.

Its purpose is not to invent feelings, but to make the system’s current expressive posture visible or audible in a coherent, modulated way.

This may include:

* expressive tone selection
* synchronized visual affect cues
* coordinated voice-expression alignment
* multimodal expressive feedback construction

This submodule is important because the same informational content may need to be expressed differently depending on urgency, calmness, supportiveness, or runtime sensitivity.

### Internal Structure

```text
emotional_expression/
├── models/
├── services/
└── providers/
```

---

## emotional_expression/models/

### emotional_expression_signal.py

Defines the structured signal representing a desired expressive mode or expressive adjustment in outward behavior.

Its role is to bridge internal modulation and external expression.

### visual_emotion_profile.py

Defines the structured visual-expression profile used for emotion-like or affective presentation on visual surfaces.

This may include color, animation category, iconography, or posture-linked display guidance.

### expressive_feedback_request.py

Defines the structured request for expressive feedback generation.

Its purpose is to represent the desired expressive effect independently from any one output channel.

---

## emotional_expression/services/

### resolve_emotional_expression_service.py

Defines the operation that determines the effective expressive output profile from current modulation state, context, and output channel.

### build_expressive_feedback_service.py

Defines the operation that constructs expressive feedback payloads or instructions.

Its purpose is to translate internal modulation into channel-aware expressive behavior.

### synchronize_expression_with_voice_service.py

Defines the operation that aligns expressive signaling with spoken output.

Its role is important for avoiding incoherent multimodal expression.

---

## emotional_expression/providers/

### emotion_expression_provider.py

Defines the provider boundary through which expressive visual or multimodal effect capability is delivered.

Its purpose is to abstract concrete expressive-rendering technology.

---

# 5. movement_and_physical_behavior

## Definition

The `movement_and_physical_behavior/` submodule defines how NORA performs embodied movement and posture-related action.

Its purpose is to translate movement requests into validated actuator commands while enforcing safety controls.

This may include:

* body movement
* posture adjustments
* motor actuation
* servo control
* stopping active physical behavior

This submodule is especially important because physical behavior has stronger safety consequences than purely digital output.

### Internal Structure

```text
movement_and_physical_behavior/
├── models/
├── services/
└── providers/
```

---

## movement_and_physical_behavior/models/

### movement_request.py

Defines the structured representation of a requested movement behavior.

This may include movement type, target direction, intensity, timing, and contextual constraints.

### posture_change_request.py

Defines the structured representation of a requested posture adjustment.

Its role is to distinguish broader posture control from generic movement requests.

### motor_command.py

Defines the structured motor-level command produced for execution.

Its purpose is to represent low-level actuation instructions after safety and translation logic have run.

### servo_command.py

Defines the structured servo-level command produced for execution.

### movement_execution_result.py

Defines the structured result of a movement execution attempt.

This may include success status, partial execution, failure reason, and safety-related metadata.

---

## movement_and_physical_behavior/services/

### validate_movement_safety_service.py

Defines the operation that checks whether a requested movement is safe to execute.

Its purpose is to ensure embodied behavior is gated by explicit safety validation.

### build_motor_command_service.py

Defines the operation that constructs motor commands from higher-level movement requests.

### build_servo_command_service.py

Defines the operation that constructs servo commands from posture or movement requests.

### execute_movement_request_service.py

Defines the operation that coordinates the execution of a movement request through the relevant actuator-control path.

### stop_physical_behavior_service.py

Defines the operation that stops active physical movement or posture behavior.

Its role is critical for interruption and safety handling.

---

## movement_and_physical_behavior/providers/

### motor_controller_provider.py

Defines the provider boundary through which motor-control commands are delivered.

### servo_controller_provider.py

Defines the provider boundary through which servo-control commands are delivered.

Its purpose is to abstract concrete actuator hardware interfaces.

---

# 6. camera_actions

## Definition

The `camera_actions/` submodule defines how NORA actively captures images and video as an intentional output-side operation.

Its purpose is distinct from visual perception.

Visual perception consumes camera-origin input to understand the environment.

Camera actions intentionally trigger capture and produce media artifacts.

This submodule therefore covers:

* image capture requests
* video capture requests
* captured media artifacts
* storage of captured media

### Internal Structure

```text
camera_actions/
├── models/
├── services/
└── providers/
```

---

## camera_actions/models/

### image_capture_request.py

Defines the structured request to capture an image.

This may include target camera, resolution preferences, capture reason, timing, and storage directives.

### video_capture_request.py

Defines the structured request to capture video.

Its role is to represent bounded video capture behavior with explicit parameters.

### captured_image_artifact.py

Defines the structured artifact produced by an image capture operation.

This may include storage reference, metadata, capture timestamp, and source information.

### captured_video_artifact.py

Defines the structured artifact produced by a video capture operation.

Its purpose is to represent captured video results in a durable and queryable form.

---

## camera_actions/services/

### capture_image_service.py

Defines the operation that triggers image capture.

### capture_video_service.py

Defines the operation that triggers video capture.

### store_captured_image_service.py

Defines the operation that stores or registers captured image artifacts.

Its purpose is to ensure capture results enter the artifact and storage architecture cleanly.

### store_captured_video_service.py

Defines the operation that stores or registers captured video artifacts.

---

## camera_actions/providers/

### camera_capture_provider.py

Defines the provider boundary through which image and video capture is performed.

Its role is to abstract camera-control implementation details from capture semantics.

---

# 7. iot_and_device_control

## Definition

The `iot_and_device_control/` submodule defines how NORA issues commands to controllable external devices and IoT systems.

Its purpose is to bridge internal control intent and external device actuation in a safe, permission-aware, and protocol-aware way.

This may include:

* smart-plug control
* home automation control
* MQTT-backed device commands
* state updates from device-control operations
* device-target resolution

This submodule is important because digital command issuance to external devices is a major execution channel with real-world consequences.

### Internal Structure

```text
iot_and_device_control/
├── models/
├── services/
└── providers/
```

---

## iot_and_device_control/models/

### device_control_request.py

Defines the structured request to control an external device.

This may include requested action, target alias, target type, desired state, permissions context, and execution metadata.

### device_command_payload.py

Defines the concrete command payload sent to the device-control provider.

Its purpose is to separate device-agnostic request semantics from protocol-specific control payloads.

### device_state_update.py

Defines the structured result or state update associated with a device-control action.

### controllable_device_target.py

Defines the structured representation of the target device being controlled.

Its role is to make device targeting explicit and inspectable.

---

## iot_and_device_control/services/

### validate_device_control_permission_service.py

Defines the operation that checks whether a device-control request is permitted.

Its role is crucial because external device actuation is both security-sensitive and potentially safety-sensitive.

### resolve_device_target_service.py

Defines the operation that resolves the requested device target from aliases, identifiers, or contextual references.

### build_device_command_payload_service.py

Defines the operation that builds the concrete payload required for the selected device-control backend.

### execute_device_control_request_service.py

Defines the operation that performs the device-control action through the selected provider.

### stop_device_action_service.py

Defines the operation that stops or cancels an active device action where such semantics exist.

---

## iot_and_device_control/providers/

### mqtt_device_control_provider.py

Defines the provider boundary through which MQTT-based device commands are executed.

### home_assistant_control_provider.py

Defines the provider boundary through which home-automation platform control is performed.

### smart_plug_control_provider.py

Defines the provider boundary through which smart-plug-specific control is performed.

These providers preserve explicit separation between device-control semantics and backend protocol implementations.

---

# 8. external_communication

## Definition

The `external_communication/` submodule defines how NORA sends information outward through external communication channels.

Its purpose is to make outbound communication explicit and modular.

This may include:

* notifications
* emails
* webhooks
* messages to external platforms
* delivery-result tracking
* communication-audit construction

This submodule matters because external communication is a distinct class of action with strong operational, security, and traceability implications.

### Internal Structure

```text
external_communication/
├── models/
├── services/
└── providers/
```

---

## external_communication/models/

### outbound_message_request.py

Defines the structured representation of a generic outbound message request.

Its purpose is to provide a common abstraction across communication channels.

### notification_request.py

Defines the structured request to send a notification.

This may represent push notifications, system notices, or lightweight outbound alerts.

### email_request.py

Defines the structured request to send an email.

Its role is to preserve email-specific structure distinctly from generic messaging.

### webhook_request.py

Defines the structured request to invoke a webhook or structured outbound HTTP callback.

### communication_delivery_result.py

Defines the structured result of an outbound communication attempt.

This may include delivery status, channel used, provider feedback, and failure details.

---

## external_communication/services/

### send_notification_service.py

Defines the operation that sends a notification through the relevant provider path.

### send_email_service.py

Defines the operation that sends an email.

### trigger_webhook_service.py

Defines the operation that triggers a webhook call.

### send_platform_message_service.py

Defines the operation that sends a message through an external messaging platform.

Its purpose is to support communication channels beyond email or webhook.

### build_communication_audit_record_service.py

Defines the operation that constructs an auditable record of an outbound communication action.

Its role is especially important for traceability, compliance, and debugging.

---

## external_communication/providers/

### email_provider.py

Defines the provider boundary through which email delivery is performed.

### webhook_provider.py

Defines the provider boundary through which webhook delivery is performed.

### messaging_platform_provider.py

Defines the provider boundary through which outbound platform messaging is performed.

Its role is to abstract specific communication platform implementations from communication semantics.

---

## Cross-Submodule Architectural Relationships

The action and expression module is best understood as an execution architecture rather than a collection of unrelated output paths.

### voice_output -> emotional_expression

Voice output may depend on expressive modulation for tone, pacing, and synchronization.

### screen_and_visual_output -> emotional_expression

Visual output may be enhanced or shaped by expressive feedback state.

### movement_and_physical_behavior -> iot_and_device_control

Both are embodied action channels, but one targets NORA’s own physical behavior while the other targets external controllable devices.

### camera_actions -> persistence and communication paths

Captured media may later be stored, displayed, analyzed, or transmitted externally.

### sound_and_multimedia -> voice_output

Audio coordination may be required when speech and media output coexist.

### external_communication -> planning and audit requirements

Outbound communication often depends on upstream intent, permission, and audit construction.

These relationships show that the submodules are separate, but not isolated.

They cooperate as one outward-effect architecture.

---

## What This Module Must Not Contain

To preserve architectural clarity, the action and expression module should not absorb responsibilities that belong elsewhere.

It should not contain:

* high-level intent classification
* plan construction logic
* session-history ownership
* user-authentication policy logic
* low-level hardware registration logic
* generic frontend page architecture
* perception-engine implementation
* long-term memory ownership

It may depend on upstream planning and context, and it may depend on downstream providers and hardware interfaces, but it must remain the module that executes and expresses outcomes.

---

## Interaction With Other Modules

The `action_and_expression/` module interacts with many other architectural domains.

### shared

Uses shared identifiers, operation models, exceptions, file-type concepts, timestamps, and cross-cutting support abstractions.

### identity_access_security

Consumes permissions, trust state, and authorization outcomes before executing sensitive actions such as communication, device control, or physical behavior.

### interaction_interfaces

May provide immediate acknowledgments, confirmations, or visible responses to interaction-origin events.

### perception

May be triggered by perception-driven events indirectly, and camera actions may later produce artifacts that perception or other modules consume.

### cognitive_core

Consumes operational-state constraints, behavioral modulation, interruption signals, and safety-related runtime state.

### dialogue_and_session

Consumes continuity context so that spoken and visual responses remain coherent with ongoing dialogue and active projects.

### planning_and_agents

Receives execution-ready instructions, expressive requirements, tool-bound tasks, and clarification-related output requirements.

### persistence_and_memory

Stores captured media artifacts, communication records, action traces, and other execution results when durability is required.

### backend_and_application

Connects execution services to application use cases, coordinators, realtime propagation, and API-triggered flows.

### frontend_support

Supplies visual state, rendered payloads, and outward feedback structures for frontend consumption where relevant.

### integrations_and_external_services

Depends on external TTS, media, messaging, home automation, email, and other provider-backed capabilities.

### infrastructure_and_hardware

Depends on speakers, displays, motors, servos, cameras, and controllable device infrastructure, while remaining above the hardware modeling boundary.

### observability

Produces action traces, delivery results, execution metrics, and safety-relevant logs for monitoring and diagnostics.

---

## Design Constraints of the Module

The `action_and_expression/` module should obey several strict architectural constraints.

### 1. Expression and actuation must remain distinguishable

Speaking, displaying, expressing, moving, capturing, controlling, and communicating are all outputs, but they are not interchangeable.

### 2. Execution must remain downstream of planning

This module should receive execution direction explicitly rather than improvising high-level intent resolution on its own.

### 3. Safety must be first-class for embodied actions

Movement and device control must remain safety-aware and permission-aware.

### 4. Output coordination must remain explicit

Voice, visual output, and emotional expression may need synchronization.

This coordination should be structured rather than incidental.

### 5. Capture and perception must remain distinct

Capturing media intentionally is not the same as perceiving and interpreting media.

### 6. External communication must remain auditable

Emails, notifications, webhooks, and platform messages should preserve delivery results and auditability.

### 7. Providers must abstract execution backends cleanly

Output semantics should not be tightly coupled to a specific TTS engine, media system, messaging platform, or actuator backend.

---

## Testing Implications

This module requires especially strong execution-oriented testing because it is where internal decisions become real external effects.

Important testing categories include:

* spoken-response construction tests
* speech-markup application tests
* voice-profile resolution tests
* speech synthesis and playback flow tests
* media-source resolution tests
* playback queue and playback-state tests
* audio-mixing coordination tests
* visual-message composition tests
* rendered screen payload tests
* expressive-feedback synchronization tests
* movement-safety validation tests
* motor and servo command construction tests
* movement-stop tests
* image and video capture tests
* captured-artifact storage tests
* device-target resolution tests
* device-control permission tests
* device-command payload tests
* device-action stop tests
* notification, email, webhook, and messaging tests
* communication-delivery result tests
* communication-audit record tests

Failures here are especially consequential because they can create unsafe movement, unintended communication, broken multimodal output, or uncontrolled device actuation.

---

## Why This Structure Fits NORA

This structure fits NORA because NORA is not only an interpreter of information.

It is also a system that must make things happen.

It may need to:

* speak to users
* display visual state
* emit expressive feedback
* move or change posture
* capture photos or video
* control smart devices
* send messages and notifications
* coordinate multiple output channels together

A flatter architecture would make these responsibilities hard to separate, hard to secure, and hard to test.

The proposed structure allows NORA to:

* separate major outward-effect channels cleanly
* preserve explicit safety and permission boundaries
* coordinate multimodal expression
* support embodied and digital action together
* remain extensible as new action or expression channels are added

That makes it an excellent fit for the system.

---

## Architectural Importance

The `action_and_expression/` module provides the outward execution architecture through which NORA becomes observable and effective in the world.

While other modules define interaction, perception, runtime control, dialogue continuity, planning, persistence, backend behavior, and integrations, the live system still requires an explicit architecture that can turn internal decisions into spoken output, multimedia playback, visual feedback, expressive signaling, embodied movement, media capture, device-control operations, and external communication.

Through this module the architecture gains:

* explicit voice, multimedia, visual, expressive, physical, capture, device-control, and communication channels
* cleaner separation between decision and execution
* safer embodied and device-control behavior
* better coordination across multimodal output channels
* auditable external communication behavior
* clearer extensibility for new output and action mechanisms

By separating voice output, multimedia, visual output, emotional expression, physical behavior, camera actions, IoT control, and external communication into explicit internal subdomains, NORA preserves both execution power and architectural clarity.

For that reason, `action_and_expression/` is one of the core execution modules of `src/nora/`.

## Architectural Structure

```text
action_and_expression
│
├── Voice Output
│   ├── spoken responses
│   ├── speech markup payloads
│   ├── voice profiles
│   ├── speech playback requests
│   ├── spoken-response builders
│   ├── markup application services
│   ├── voice-profile resolution services
│   ├── speech synthesis services
│   ├── speech playback services
│   └── voice providers
│
├── Sound and Multimedia
│   ├── media playback requests
│   ├── sound signal requests
│   ├── media queue items
│   ├── playback state snapshots
│   ├── media-source resolution services
│   ├── playback queue services
│   ├── playback control services
│   ├── audio-mixing services
│   └── multimedia providers
│
├── Screen and Visual Output
│   ├── visual messages
│   ├── graphical elements
│   ├── visual state indicators
│   ├── rendered screen payloads
│   ├── display update requests
│   ├── visual-composition services
│   ├── rendering services
│   ├── state-indicator builders
│   ├── display update services
│   ├── display clearing services
│   └── display provider
│
├── Emotional Expression
│   ├── emotional expression signals
│   ├── visual emotion profiles
│   ├── expressive feedback requests
│   ├── expression-resolution services
│   ├── expressive feedback builders
│   ├── voice-expression synchronization services
│   └── expression provider
│
├── Movement and Physical Behavior
│   ├── movement requests
│   ├── posture change requests
│   ├── motor commands
│   ├── servo commands
│   ├── movement execution results
│   ├── movement-safety validation services
│   ├── motor-command builders
│   ├── servo-command builders
│   ├── movement execution services
│   ├── physical stop services
│   └── movement providers
│
├── Camera Actions
│   ├── image capture requests
│   ├── video capture requests
│   ├── captured image artifacts
│   ├── captured video artifacts
│   ├── image-capture services
│   ├── video-capture services
│   ├── capture-storage services
│   └── camera provider
│
├── IoT and Device Control
│   ├── device control requests
│   ├── device command payloads
│   ├── device state updates
│   ├── controllable device targets
│   ├── permission-validation services
│   ├── device-target resolution services
│   ├── command-payload builders
│   ├── device-control execution services
│   ├── device stop services
│   └── device-control providers
│
└── External Communication
    ├── outbound message requests
    ├── notification requests
    ├── email requests
    ├── webhook requests
    ├── communication delivery results
    ├── notification services
    ├── email services
    ├── webhook trigger services
    ├── platform-messaging services
    ├── communication-audit builders
    └── communication providers
```


Tu módulo 06 define salida por voz, multimedia, pantalla, expresión emocional, movimiento, cámara, IoT y comunicación externa.
```
action_and_expression/
├── voice_output/
│   ├── models/
│   │   ├── spoken_response.py
│   │   ├── speech_markup_payload.py
│   │   ├── voice_profile.py
│   │   └── speech_playback_request.py
│   ├── services/
│   │   ├── build_spoken_response_service.py
│   │   ├── apply_speech_markup_service.py
│   │   ├── resolve_voice_profile_service.py
│   │   ├── synthesize_speech_service.py
│   │   └── play_synthesized_speech_service.py
│   └── providers/
│       ├── text_to_speech_provider.py
│       └── speech_playback_provider.py
│
├── sound_and_multimedia/
│   ├── models/
│   │   ├── media_playback_request.py
│   │   ├── sound_signal_request.py
│   │   ├── media_queue_item.py
│   │   └── playback_state_snapshot.py
│   ├── services/
│   │   ├── resolve_media_source_service.py
│   │   ├── enqueue_media_playback_service.py
│   │   ├── start_media_playback_service.py
│   │   ├── pause_media_playback_service.py
│   │   ├── stop_media_playback_service.py
│   │   └── mix_audio_output_service.py
│   └── providers/
│       ├── media_stream_provider.py
│       └── audio_output_provider.py
│
├── screen_and_visual_output/
│   ├── models/
│   │   ├── visual_message.py
│   │   ├── graphical_element.py
│   │   ├── visual_state_indicator.py
│   │   ├── rendered_screen_payload.py
│   │   └── display_update_request.py
│   ├── services/
│   │   ├── compose_visual_message_service.py
│   │   ├── render_screen_payload_service.py
│   │   ├── build_state_indicator_service.py
│   │   ├── update_display_service.py
│   │   └── clear_display_service.py
│   └── providers/
│       └── local_display_provider.py
│
├── emotional_expression/
│   ├── models/
│   │   ├── emotional_expression_signal.py
│   │   ├── visual_emotion_profile.py
│   │   └── expressive_feedback_request.py
│   ├── services/
│   │   ├── resolve_emotional_expression_service.py
│   │   ├── build_expressive_feedback_service.py
│   │   └── synchronize_expression_with_voice_service.py
│   └── providers/
│       └── emotion_expression_provider.py
│
├── movement_and_physical_behavior/
│   ├── models/
│   │   ├── movement_request.py
│   │   ├── posture_change_request.py
│   │   ├── motor_command.py
│   │   ├── servo_command.py
│   │   └── movement_execution_result.py
│   ├── services/
│   │   ├── validate_movement_safety_service.py
│   │   ├── build_motor_command_service.py
│   │   ├── build_servo_command_service.py
│   │   ├── execute_movement_request_service.py
│   │   └── stop_physical_behavior_service.py
│   └── providers/
│       ├── motor_controller_provider.py
│       └── servo_controller_provider.py
│
├── camera_actions/
│   ├── models/
│   │   ├── image_capture_request.py
│   │   ├── video_capture_request.py
│   │   ├── captured_image_artifact.py
│   │   └── captured_video_artifact.py
│   ├── services/
│   │   ├── capture_image_service.py
│   │   ├── capture_video_service.py
│   │   ├── store_captured_image_service.py
│   │   └── store_captured_video_service.py
│   └── providers/
│       └── camera_capture_provider.py
│
├── iot_and_device_control/
│   ├── models/
│   │   ├── device_control_request.py
│   │   ├── device_command_payload.py
│   │   ├── device_state_update.py
│   │   └── controllable_device_target.py
│   ├── services/
│   │   ├── validate_device_control_permission_service.py
│   │   ├── resolve_device_target_service.py
│   │   ├── build_device_command_payload_service.py
│   │   ├── execute_device_control_request_service.py
│   │   └── stop_device_action_service.py
│   └── providers/
│       ├── mqtt_device_control_provider.py
│       ├── home_assistant_control_provider.py
│       └── smart_plug_control_provider.py
│
└── external_communication/
    ├── models/
    │   ├── outbound_message_request.py
    │   ├── notification_request.py
    │   ├── email_request.py
    │   ├── webhook_request.py
    │   └── communication_delivery_result.py
    ├── services/
    │   ├── send_notification_service.py
    │   ├── send_email_service.py
    │   ├── trigger_webhook_service.py
    │   ├── send_platform_message_service.py
    │   └── build_communication_audit_record_service.py
    └── providers/
        ├── email_provider.py
        ├── webhook_provider.py
        └── messaging_platform_provider.py
```

# Persistence and Memory Module

## Definition

The `persistence_and_memory/` module defines how NORA stores, preserves, retrieves, and organizes durable information across runtime boundaries.

While other architectural modules define identity, interaction, perception, runtime cognition, dialogue continuity, planning, action, backend behavior, integrations, hardware structure, and observability, those modules still require a dedicated persistence architecture that answers a more fundamental question:

What information survives beyond the current moment of execution, and how is that information structured so the system can recover, remember, audit, and continue coherently over time?

That is the role of `persistence_and_memory/`.

In architectural terms, this module defines the durable information substrate of NORA.

It is the module that ensures that operational state, user-related state, conversational continuity, memory entries, file artifacts, and technical records do not disappear when the active runtime cycle ends.

This module therefore defines:

* transactional structured storage
* long-lived semantic memory
* vectorized retrieval support
* durable storage of generated or uploaded file artifacts
* technical historical records for observability and debugging
* the structural boundaries between operational data, memory knowledge, files, and technical traces

This module is not a single generic storage layer.

It is intentionally separated into four distinct domains because not all persisted information is the same.

Structured transactional state, semantic memory, file artifacts, and technical history have different lifecycles, retrieval patterns, consistency requirements, and architectural meanings.

For that reason, `persistence_and_memory/` is one of the foundational infrastructure-facing domain modules of NORA.

---

## Architectural Purpose

The purpose of the `persistence_and_memory/` module is to give NORA durable continuity, recoverability, and historical traceability.

A system like NORA needs to persist many kinds of information over time, including:

* user and permission state
* sessions and projects
* dialogue turns
* configuration state
* memory entries extracted from interaction
* embeddings and retrieval metadata
* uploaded or generated files
* technical logs and metrics
* execution traces and action history

Without a dedicated persistence and memory architecture, these needs would collapse into improvised storage behavior spread across the codebase.

That would create major structural problems such as:

* no clear distinction between operational records and memory knowledge
* misuse of one storage system for incompatible data types
* weak recovery after restart or interruption
* poor traceability for technical behavior
* no durable artifact model
* inconsistent retrieval semantics
* difficulty scaling history and memory separately
* confusion between dialogue history and semantic memory

By introducing a dedicated persistence and memory architecture, NORA gains:

* explicit structured persistence boundaries
* durable long-term memory support
* semantic retrieval through vector storage
* stable artifact-storage behavior
* technical observability history
* clearer separation between business continuity and technical trace storage
* more reliable recovery and explainability over time

This module therefore provides the durable backbone of the system.

---

## Core Architectural Principle

The most important design principle of this module is the following:

Persistence must be separated into transactional database storage, persistent semantic memory, file artifact storage, and technical history.

These four domains are all forms of persistence, but they are not architecturally equivalent.

### Transactional database

Stores structured operational entities that require consistency, relations, and transactional integrity.

### Persistent memory

Stores semantic memory items that represent remembered knowledge rather than merely normalized operational records.

### File storage

Stores files and artifact objects whose primary identity is not relational structure but durable artifact existence.

### Technical history

Stores records useful for monitoring, debugging, traceability, and operational diagnosis.

This separation matters because forcing all durability into one storage model would distort the architecture and make retrieval, scaling, and reasoning less coherent.

---

## Internal Module Structure

The proposed structure is the following:

```text
persistence_and_memory/
├── transactional_database/
├── persistent_memory/
├── file_storage/
└── technical_history/
```

This structure reflects literally the conceptual separation required by the architecture.

### transactional_database

Defines durable storage for operational entities and normalized structured records.

### persistent_memory

Defines semantic memory entries and embedding-backed retrieval.

### file_storage

Defines storage and retrieval of file artifacts.

### technical_history

Defines durable retention of logs, traces, metrics, and operational history.

This decomposition is essential because each of these persistence areas answers a different architectural question.

---

## Architectural Role Within the Full System

The `persistence_and_memory/` module sits beneath almost every major part of NORA.

Many modules depend on it indirectly or directly.

It stores what the rest of the system needs to preserve, remember, recover, analyze, or audit later.

It receives content from:

* identity and security modules
* dialogue and session continuity
* planning and execution flows
* file-generating actions
* technical observability systems
* memory-extraction or memory-update flows

It then provides durable continuity for:

* runtime restart recovery
* user continuity
* project continuity
* memory retrieval
* artifact access
* historical diagnosis
* auditability

This means the module is not just “the database layer.”

It is the architecture of durability itself.

---

# 1. transactional_database

## Definition

The `transactional_database/` submodule defines the structured relational or transactional storage layer of NORA.

Its purpose is to store operational entities that require strong consistency, structured relationships, transactional updates, and stable CRUD-oriented access semantics.

This submodule is the persistence home for normalized system records such as users, roles, permissions, sessions, messages, projects, configuration, and events.

### Internal Structure

```text
transactional_database/
├── models/
├── mappers/
├── repositories/
└── unit_of_work/
```

---

## transactional_database/models/

### db_user_record.py

Defines the structured database record model representing a persisted user entity.

Its purpose is to provide the storage-side representation of user data in the transactional database.

### db_role_record.py

Defines the structured database record model representing a persisted role definition.

Its role is to support access-control persistence in normalized form.

### db_permission_record.py

Defines the structured database record model representing a persisted permission definition.

### db_session_record.py

Defines the structured database record model representing a persisted dialogue or interaction session.

Its purpose is to store session continuity in relational form.

### db_message_record.py

Defines the structured database record model representing a persisted dialogue message or turn record.

Its role is to anchor conversation history in normalized storage.

### db_project_record.py

Defines the structured database record model representing a persisted project.

Its purpose is to provide durable project continuity in structured form.

### db_configuration_record.py

Defines the structured database record model representing persisted configuration state when configuration snapshots or managed configuration records are stored transactionally.

### db_event_record.py

Defines the structured database record model representing a persisted event record.

Its role may support event history, replay, audit, or operational reconstruction depending on wider system choices.

---

## transactional_database/mappers/

### user_record_mapper.py

Defines the mapping logic between storage-side user records and domain-side user models.

Its purpose is to prevent direct leakage of persistence schema into domain logic.

### session_record_mapper.py

Defines the mapping logic between session records and domain session structures.

### project_record_mapper.py

Defines the mapping logic between project records and domain project structures.

### message_record_mapper.py

Defines the mapping logic between message or dialogue-turn records and domain history models.

These mappers are architecturally important because they preserve separation between persistence representation and domain representation.

---

## transactional_database/repositories/

### sql_user_repository.py

Defines the repository that stores and retrieves user records from the transactional database.

### sql_role_repository.py

Defines the repository that stores and retrieves role definitions.

### sql_permission_repository.py

Defines the repository that stores and retrieves permission definitions.

### sql_session_repository.py

Defines the repository that stores and retrieves session records.

### sql_message_repository.py

Defines the repository that stores and retrieves message or turn records.

### sql_project_repository.py

Defines the repository that stores and retrieves project records.

### sql_configuration_repository.py

Defines the repository that stores and retrieves configuration records managed through transactional persistence.

### sql_event_repository.py

Defines the repository that stores and retrieves event records.

These repositories are the persistence-access boundary for structured operational records.

---

## transactional_database/unit_of_work/

### sql_unit_of_work.py

Defines the transactional unit-of-work boundary coordinating a set of repository operations as one coherent persistence operation.

Its purpose is to preserve consistency across related changes.

### transaction_manager.py

Defines the component responsible for opening, committing, rolling back, and closing transactional scopes.

Its role is to make transaction lifecycle explicit and controlled.

---

# 2. persistent_memory

## Definition

The `persistent_memory/` submodule defines the long-lived semantic memory layer of NORA.

Its purpose is to preserve remembered knowledge that should remain available beyond the immediate runtime and beyond raw dialogue history.

This includes memory entries representing:

* user preferences remembered over time
* knowledge connected to ongoing projects
* conversation-derived facts worth retaining
* embeddings that support retrieval of relevant memory

This submodule is distinct from transactional storage because memory is not just normalized record persistence.

It is knowledge persistence.

### Internal Structure

```text
persistent_memory/
├── models/
├── services/
├── repositories/
└── vector_store/
```

---

## persistent_memory/models/

### persistent_memory_entry.py

Defines the primary structured representation of a semantic memory entry.

This model may include:

* memory identifier
* memory content
* memory category
* associated user or project references
* creation metadata
* retention metadata
* retrieval metadata

Architecturally, this is the central object of the memory layer.

### user_preference_memory_entry.py

Defines a semantic memory entry specifically representing remembered user preferences.

Its purpose is to keep preference memory explicit and distinguishable from other memory categories.

### project_knowledge_memory_entry.py

Defines a semantic memory entry representing knowledge associated with a project.

Its role is important for long-horizon project continuity.

### conversation_fact_memory_entry.py

Defines a semantic memory entry representing a fact extracted from conversation that should be retained as durable memory.

### semantic_embedding_record.py

Defines the structured record representing an embedding associated with a memory entry.

Its purpose is to support semantic retrieval and ranking.

### memory_retrieval_result.py

Defines the structured result of retrieving memory entries from the persistent-memory system.

This may include matched entries, similarity or ranking information, and retrieval metadata.

---

## persistent_memory/services/

### store_memory_entry_service.py

Defines the operation that stores a new memory entry in the persistent-memory layer.

Its purpose is to make memory creation explicit and controlled.

### retrieve_relevant_memory_service.py

Defines the operation that retrieves memory entries relevant to a current context or query.

Its role is one of the most important memory behaviors in the system.

### update_memory_entry_service.py

Defines the operation that updates an existing memory entry.

Its purpose is to support correction, refinement, or lifecycle evolution of memory.

### delete_memory_entry_service.py

Defines the operation that deletes or deactivates a memory entry according to system policy.

### generate_memory_embedding_service.py

Defines the operation that generates a semantic embedding associated with a memory entry.

Its purpose is to support vector-backed retrieval.

### rank_memory_retrieval_results_service.py

Defines the operation that ranks candidate retrieved memories according to relevance, confidence, recency, or other retrieval criteria.

Its role ensures memory retrieval remains useful and not merely approximate.

---

## persistent_memory/repositories/

### memory_entry_repository.py

Defines the persistence boundary for memory entries themselves.

### memory_embedding_repository.py

Defines the persistence boundary for embedding records associated with memory entries.

These repositories preserve clean separation between memory objects and embedding/index support structures.

---

## persistent_memory/vector_store/

### vector_memory_store.py

Defines the vector-backed memory storage or access layer used for semantic retrieval.

Its role is to provide an embedding-oriented persistence surface distinct from traditional relational storage.

### vector_similarity_search_service.py

Defines the operation that performs similarity search over vectorized memory representations.

Its purpose is to retrieve semantically related memories rather than only exact-key records.

---

# 3. file_storage

## Definition

The `file_storage/` submodule defines how NORA stores, retrieves, deletes, and describes durable file artifacts.

Its purpose is to preserve files whose identity is primarily as artifacts rather than as normalized structured records.

This may include:

* uploaded files
* generated images
* generated audio
* generated video
* documents
* downloadable artifacts linked to projects or sessions

This submodule is distinct from both transactional database storage and semantic memory.

It is the durable artifact layer.

### Internal Structure

```text
file_storage/
├── models/
├── services/
└── repositories/
```

---

## file_storage/models/

### file_artifact.py

Defines the primary structured representation of a file artifact.

This model may include storage location, artifact identifier, type, ownership, timestamps, and access metadata.

### image_artifact.py

Defines a file artifact representing an image.

Its role is to preserve image-specific artifact identity distinctly from general files.

### audio_artifact.py

Defines a file artifact representing an audio output or audio upload.

### video_artifact.py

Defines a file artifact representing a video artifact.

### document_artifact.py

Defines a file artifact representing a document-type artifact.

### artifact_metadata.py

Defines metadata associated with a file artifact.

This may include file size, content type, generation origin, checksum, creator, linked project, or linked session.

---

## file_storage/services/

### store_file_artifact_service.py

Defines the operation that stores a file artifact durably.

Its purpose is to move an artifact from transient existence into managed durable storage.

### retrieve_file_artifact_service.py

Defines the operation that retrieves a stored file artifact or its access path.

### delete_file_artifact_service.py

Defines the operation that deletes or removes a file artifact according to policy.

### generate_artifact_path_service.py

Defines the operation that determines the durable storage path or logical location of an artifact.

Its role is to make artifact path generation explicit and consistent.

### build_artifact_download_descriptor_service.py

Defines the operation that constructs a download-oriented descriptor for a stored artifact.

Its purpose is to support secure and structured artifact delivery to downstream consumers.

---

## file_storage/repositories/

### file_artifact_repository.py

Defines the persistence boundary for file artifact records and references.

Its role is to isolate artifact-index behavior from artifact-storage services.

---

# 4. technical_history

## Definition

The `technical_history/` submodule defines how NORA preserves technical records useful for diagnosis, monitoring, auditing of runtime behavior, and historical operational analysis.

Its purpose is to retain technical history as a first-class durable domain rather than treating logs and traces as disposable side effects only.

This may include:

* technical logs
* runtime traces
* metrics
* action history
* error history

This submodule is distinct from business continuity, semantic memory, and artifact storage.

It is the technical retrospective layer of the system.

### Internal Structure

```text
technical_history/
├── models/
├── services/
└── repositories/
```

---

## technical_history/models/

### technical_log_record.py

Defines the structured representation of a technical log record.

Its purpose is to preserve machine-readable or structured logging information durably when required.

### runtime_trace_record.py

Defines the structured representation of a runtime trace record.

This may include trace identifiers, correlated execution events, timing information, and cross-module linkage metadata.

### metric_record.py

Defines the structured representation of a metric observation or metric history entry.

Its role is to preserve metric values durably for later analysis or diagnostics.

### action_history_record.py

Defines the structured representation of an action-history record.

Its purpose is to preserve what actions were attempted, executed, completed, or failed over time.

### error_history_record.py

Defines the structured representation of an error-history record.

Its role is to preserve a durable account of operational failures, exceptions, or fault events.

---

## technical_history/services/

### write_technical_log_service.py

Defines the operation that writes a durable technical log record.

### write_runtime_trace_service.py

Defines the operation that writes a durable runtime trace record.

### write_metric_record_service.py

Defines the operation that writes a durable metric record.

### retrieve_action_history_service.py

Defines the operation that retrieves action-history records for analysis, debugging, or audit.

### retrieve_error_history_service.py

Defines the operation that retrieves error-history records for diagnosis or historical review.

---

## technical_history/repositories/

### technical_log_repository.py

Defines the persistence boundary for technical log records.

### runtime_trace_repository.py

Defines the persistence boundary for runtime trace records.

### metric_repository.py

Defines the persistence boundary for metric records.

These repositories keep technical-history retrieval and storage cleanly separated from service behavior.

---

## Cross-Submodule Architectural Relationships

The persistence and memory module is best understood as a durable information architecture rather than as four unrelated storage folders.

### transactional_database -> dialogue, identity, and project continuity

Structured operational continuity depends on the transactional database for normalized system records.

### persistent_memory -> long-horizon reasoning continuity

Persistent memory stores remembered knowledge that can later enrich reasoning, personalization, and project continuity.

### file_storage -> artifact continuity

File storage preserves the durable existence of artifacts that may be linked from sessions, projects, communications, or outputs.

### technical_history -> retrospective operational visibility

Technical history preserves how the system actually behaved over time.

### persistent_memory -> vector_store

Semantic memory retrieval depends on embeddings and vector similarity as a dedicated support structure.

### transactional_database -> mappers and unit_of_work

Structured operational persistence depends on clean mapping and explicit transactional coordination.

These relationships show the internal logic clearly:

* structured records preserve system state
* memory preserves semantic knowledge
* artifact storage preserves files
* technical history preserves operational traceability

---

## What This Module Must Not Contain

To preserve architectural clarity, the persistence and memory module should not absorb responsibilities that belong elsewhere.

It should not contain:

* intent-classification logic
* plan-construction logic
* dialogue-turn interpretation logic
* frontend rendering logic
* hardware-driver logic
* direct communication-delivery logic
* perception-engine logic
* behavioral-modulation logic

It may store outputs from all of those modules, but it must remain the durability architecture rather than a hidden business-logic layer.

---

## Interaction With Other Modules

The `persistence_and_memory/` module interacts with nearly every major architectural domain.

### shared

Uses shared identifiers, timestamps, file-type concepts, audit metadata, pagination structures, and storage-related abstractions.

### identity_access_security

Stores users, roles, permissions, profile-related data, audit records, and security incidents or related durable structures.

### interaction_interfaces

May store interface-origin artifacts or access-relevant file traces when required.

### perception

May store selected perceptual results, embeddings, media artifacts, and event history depending on policy.

### cognitive_core

May store transition history, operational context snapshots, or selected short-term traces that become durable for debugging or recovery.

### dialogue_and_session

Stores sessions, projects, dialogue turns, summaries, and recovery-related structures.

### planning_and_agents

May store planning results, memory updates, agent outputs, and execution-preparation artifacts depending on system policy.

### action_and_expression

Stores captured media, generated artifacts, communication records, and action-history traces.

### backend_and_application

n
Provides the durable storage surface used by application services, coordinators, APIs, and background workflows.

### frontend_support

Provides artifact descriptors, downloadable payload references, and continuity-related storage access needed for UI-facing views.

### integrations_and_external_services

Uses provider-backed vector systems, storage backends, and external file or memory-support capabilities where configured.

### observability

Stores technical logs, traces, metrics, and technical historical records that support diagnostics and monitoring.

---

## Design Constraints of the Module

The `persistence_and_memory/` module should obey several strict architectural constraints.

### 1. Transactional records and memory entries must remain distinct

A normalized user record is not the same thing as a remembered semantic fact.

### 2. File artifacts must remain distinct from structured records

Files should not be treated as if they were merely database rows with no artifact identity.

### 3. Technical history must remain distinct from business continuity

A metric record is not the same kind of durable information as a session or project.

### 4. Mapping boundaries must remain explicit

Domain models and storage models should not collapse into one persistence-coupled structure without care.

### 5. Transactional coordination must remain explicit

Structured operational changes requiring consistency should flow through unit-of-work or equivalent transaction boundaries.

### 6. Semantic retrieval must remain intentional

Embedding generation, similarity search, and retrieval ranking should remain explicit parts of the persistent-memory architecture.

### 7. Durability policies should be category-aware

Not all data should be stored, retained, or deleted in the same way.

---

## Testing Implications

This module requires especially strong durability-oriented testing because failures here threaten continuity, traceability, and recoverability.

Important testing categories include:

* record-model mapping tests
* repository CRUD tests
* unit-of-work commit and rollback tests
* transaction-boundary consistency tests
* memory-entry storage tests
* relevant-memory retrieval tests
* embedding-generation tests
* vector-similarity retrieval tests
* retrieval-ranking tests
* artifact-storage tests
* artifact-path-generation tests
* artifact-download-descriptor tests
* technical-log writing tests
* runtime-trace writing tests
* metric-record writing tests
* action-history retrieval tests
* error-history retrieval tests
* cross-category retention-policy tests

Failures here can make NORA forget, misremember, lose artifacts, or become impossible to diagnose after errors.

---

## Why This Structure Fits NORA

This structure fits NORA because NORA is a persistent, memory-bearing, artifact-producing, technically observable system.

It needs to preserve:

* normalized operational state
* semantic memory
* durable files
* technical behavior history

A flatter architecture would blur these concerns and create incorrect storage assumptions.

The proposed structure allows NORA to:

* preserve structured state transactionally
* remember semantically useful knowledge over time
* store and retrieve durable artifacts cleanly
* retain operational traces for diagnosis and audit
* scale different persistence categories according to their nature

That makes it an excellent fit for the system.

---

## Architectural Importance

The `persistence_and_memory/` module provides the durable information foundation through which NORA can persist state, remember knowledge, preserve artifacts, and retain operational history over time.

While other modules define identity, interaction, perception, runtime control, conversational continuity, planning, action, backend behavior, and integrations, the live system still requires an explicit architecture that can store structured operational entities transactionally, retain semantic memory beyond the current session, preserve file artifacts durably, and maintain technical history for diagnostics and audit.

Through this module the architecture gains:

* explicit transactional storage for structured operational records
* durable semantic memory with embedding-backed retrieval
* dedicated artifact-storage structures for files and generated media
* technical-history retention for logs, traces, metrics, and action history
* clearer separation between business continuity, remembered knowledge, artifacts, and diagnostic history
* stronger recovery, traceability, and long-term continuity across runtime cycles

By separating transactional database storage, persistent memory, file storage, and technical history into explicit internal subdomains, NORA preserves both durability and architectural clarity.

For that reason, `persistence_and_memory/` is one of the foundational durability modules of `src/nora/`.

## Architectural Structure

```text
persistence_and_memory
│
├── Transactional Database
│   ├── user records
│   ├── role records
│   ├── permission records
│   ├── session records
│   ├── message records
│   ├── project records
│   ├── configuration records
│   ├── event records
│   ├── record mappers
│   ├── SQL repositories
│   ├── unit-of-work boundary
│   └── transaction manager
│
├── Persistent Memory
│   ├── persistent memory entries
│   ├── user preference memory entries
│   ├── project knowledge memory entries
│   ├── conversation fact memory entries
│   ├── semantic embedding records
│   ├── memory retrieval results
│   ├── memory-entry services
│   ├── memory repositories
│   ├── vector memory store
│   └── vector similarity search
│
├── File Storage
│   ├── file artifacts
│   ├── image artifacts
│   ├── audio artifacts
│   ├── video artifacts
│   ├── document artifacts
│   ├── artifact metadata
│   ├── artifact storage services
│   ├── artifact retrieval services
│   ├── artifact deletion services
│   ├── artifact path generation
│   ├── artifact download descriptors
│   └── file artifact repository
│
└── Technical History
    ├── technical log records
    ├── runtime trace records
    ├── metric records
    ├── action history records
    ├── error history records
    ├── technical-log writing services
    ├── runtime-trace writing services
    ├── metric-writing services
    ├── action-history retrieval services
    ├── error-history retrieval services
    └── technical-history repositories
```

```
persistence_and_memory/
├── transactional_database/
│   ├── models/
│   │   ├── db_user_record.py
│   │   ├── db_role_record.py
│   │   ├── db_permission_record.py
│   │   ├── db_session_record.py
│   │   ├── db_message_record.py
│   │   ├── db_project_record.py
│   │   ├── db_configuration_record.py
│   │   └── db_event_record.py
│   ├── mappers/
│   │   ├── user_record_mapper.py
│   │   ├── session_record_mapper.py
│   │   ├── project_record_mapper.py
│   │   └── message_record_mapper.py
│   ├── repositories/
│   │   ├── sql_user_repository.py
│   │   ├── sql_role_repository.py
│   │   ├── sql_permission_repository.py
│   │   ├── sql_session_repository.py
│   │   ├── sql_message_repository.py
│   │   ├── sql_project_repository.py
│   │   ├── sql_configuration_repository.py
│   │   └── sql_event_repository.py
│   └── unit_of_work/
│       ├── sql_unit_of_work.py
│       └── transaction_manager.py
│
├── persistent_memory/
│   ├── models/
│   │   ├── persistent_memory_entry.py
│   │   ├── user_preference_memory_entry.py
│   │   ├── project_knowledge_memory_entry.py
│   │   ├── conversation_fact_memory_entry.py
│   │   ├── semantic_embedding_record.py
│   │   └── memory_retrieval_result.py
│   ├── services/
│   │   ├── store_memory_entry_service.py
│   │   ├── retrieve_relevant_memory_service.py
│   │   ├── update_memory_entry_service.py
│   │   ├── delete_memory_entry_service.py
│   │   ├── generate_memory_embedding_service.py
│   │   └── rank_memory_retrieval_results_service.py
│   ├── repositories/
│   │   ├── memory_entry_repository.py
│   │   └── memory_embedding_repository.py
│   └── vector_store/
│       ├── vector_memory_store.py
│       └── vector_similarity_search_service.py
│
├── file_storage/
│   ├── models/
│   │   ├── file_artifact.py
│   │   ├── image_artifact.py
│   │   ├── audio_artifact.py
│   │   ├── video_artifact.py
│   │   ├── document_artifact.py
│   │   └── artifact_metadata.py
│   ├── services/
│   │   ├── store_file_artifact_service.py
│   │   ├── retrieve_file_artifact_service.py
│   │   ├── delete_file_artifact_service.py
│   │   ├── generate_artifact_path_service.py
│   │   └── build_artifact_download_descriptor_service.py
│   └── repositories/
│       └── file_artifact_repository.py
│
└── technical_history/
    ├── models/
    │   ├── technical_log_record.py
    │   ├── runtime_trace_record.py
    │   ├── metric_record.py
    │   ├── action_history_record.py
    │   └── error_history_record.py
    ├── services/
    │   ├── write_technical_log_service.py
    │   ├── write_runtime_trace_service.py
    │   ├── write_metric_record_service.py
    │   ├── retrieve_action_history_service.py
    │   └── retrieve_error_history_service.py
    └── repositories/
        ├── technical_log_repository.py
        ├── runtime_trace_repository.py
        └── metric_repository.py
```
# Backend and Application Module

## Definition

The `backend_and_application/` module defines the runtime application surface and orchestration layer through which NORA is exposed, coordinated, and operated as a live software system.

While other architectural modules define identity, interaction, perception, runtime cognition, dialogue continuity, planning, action, persistence, integrations, hardware structure, and observability foundations, those modules still require an application-facing layer that can do three essential things:

* expose system capabilities through stable interfaces
* coordinate flows across multiple internal modules
* operate the system as a coherent backend platform

That is the role of `backend_and_application/`.

In architectural terms, this module defines the operational backend shell of NORA.

It is the module that turns internal capabilities into an application that can be accessed, controlled, observed, and coordinated in real time.

This module therefore defines:

* HTTP API boundaries
* realtime WebSocket communication surfaces
* application use cases
* coordinators and orchestrators for multi-module workflows
* internal event dispatch behavior
* backend-local observability, health, and operational telemetry

This module is not the same as the core domain modules.

The domain modules define what the system is capable of doing.

The backend and application module defines how those capabilities are exposed, composed, and run as an application.

This module is also not the same as frontend support.

Frontend support shapes data for UI consumption.

Backend and application define the server-side boundaries, orchestration flows, and runtime application behavior behind those interfaces.

For that reason, `backend_and_application/` is one of the main operational modules of `src/nora/`.

---

## Architectural Purpose

The purpose of the `backend_and_application/` module is to provide NORA with a coherent runtime operating surface rather than a set of disconnected domain modules.

A system like NORA needs more than internal intelligence. It also needs an application layer capable of:

* receiving requests
* validating and routing them
* invoking the right use cases
* coordinating multiple subsystems
* pushing realtime updates
* dispatching events internally
* exposing diagnostics and operational health

Without a dedicated backend and application architecture, this work would become fragmented across routers, random services, infrastructure hooks, and domain modules. That would create problems such as:

* domain leakage into transport boundaries
* duplicated orchestration logic
* poor separation between use cases and HTTP handling
* inconsistent realtime behavior
* unclear event-routing structure
* weak operational observability
* difficult testing of application workflows
* poor extensibility when new interfaces are added

By introducing a dedicated backend and application module, NORA gains:

* explicit application boundaries
* cleaner separation between transport, use cases, and orchestration
* structured realtime communication support
* explicit event ingress and dispatch behavior
* operational coordinators for multi-module workflows
* backend-side observability and health visibility
* improved maintainability of application behavior

This module therefore provides the runtime application architecture that turns NORA into an operable platform.

---

## Core Architectural Principle

The most important design principle of this module is the following:

Transport boundaries, application use cases, orchestration flows, internal event dispatch, and operational observability must remain structurally distinct.

These concerns are closely related, but they are not the same.

### HTTP API

Defines request-response transport exposure.

### WebSocket realtime

Defines push-oriented and bidirectional live update behavior.

### Application services

n
Defines explicit use cases representing backend application operations.

### Coordinators and orchestrators

Defines multi-module runtime flows that do not belong to any single domain service.

### Event dispatcher

Defines how ingress events are normalized, routed, and published.

### Backend observability

Defines logs, traces, metrics, and health probes at the backend runtime level.

This separation matters because an application backend is not just a web server. It is a structured operational layer.

---

## Internal Module Structure

The proposed structure is the following:

```text
backend_and_application/
├── http_api/
├── websocket_realtime/
├── application_services/
├── coordinators_orchestrators/
├── event_dispatcher/
└── observability/
```

This structure divides the backend runtime layer into six major internal subdomains.

### http_api

Defines synchronous request-response application boundaries.

### websocket_realtime

Defines realtime subscription and broadcast behavior.

### application_services

Defines the backend use-case layer.

### coordinators_orchestrators

Defines cross-module coordination flows.

### event_dispatcher

Defines internal event ingress normalization and routing.

### observability

Defines backend-local operational visibility.

This decomposition is essential because the backend must both expose and coordinate the system, while still remaining testable and modular.

---

## Architectural Role Within the Full System

The `backend_and_application/` module sits at the server-side operational boundary of NORA.

It receives or exposes:

* HTTP requests
* WebSocket connections
* application commands
* admin operations
* monitoring requests
* ingress events
* realtime subscriptions

It then connects those boundaries to the internal modules that actually define system behavior.

This means it sits between:

* external consumers and interfaces
  and
* internal domain capabilities

It is therefore not merely transport glue.

It is the operational server architecture through which NORA runs as an application.

---

# 1. http_api

## Definition

The `http_api/` submodule defines the HTTP-based request-response interface of NORA.

Its purpose is to expose backend capabilities through structured routes, typed request models, typed response models, explicit dependencies, and centralized exception handling.

This submodule is the primary synchronous application boundary for web, administrative, and programmatic access.

### Internal Structure

```text
http_api/
├── routers/
├── request_models/
├── response_models/
├── dependencies/
└── handlers/
```

---

## http_api/routers/

### auth_router.py

Defines the HTTP routes related to authentication operations.

Its purpose is to expose login, logout, token refresh, or identity-retrieval endpoints through a dedicated boundary.

### users_router.py

Defines the HTTP routes related to user and identity-oriented operations.

Its role is to expose user-facing or admin-facing access to user records or identity context where appropriate.

### sessions_router.py

Defines the HTTP routes related to session lifecycle operations.

Its purpose is to expose creation, restoration, suspension, termination, or retrieval of sessions.

### projects_router.py

Defines the HTTP routes related to conversational project operations.

Its role is to expose project creation, continuation, completion, archive, or retrieval flows.

### events_router.py

Defines the HTTP routes related to event ingress, event inspection, or debug event operations.

Its purpose is to make event-facing backend capabilities explicit.

### fsm_router.py

Defines the HTTP routes related to finite-state-machine visibility or control operations.

Its role may include current-state inspection, transition visibility, or operational state monitoring.

### hardware_router.py

Defines the HTTP routes related to hardware state inspection or hardware command operations.

Its purpose is to expose embodied-system interactions through a bounded server-side interface.

### configuration_router.py

Defines the HTTP routes related to configuration retrieval or configuration updates.

Its role is important for controlled administration of runtime settings.

### monitoring_router.py

Defines the HTTP routes related to diagnostics, system monitoring, or health-oriented operational visibility.

### admin_router.py

Defines the HTTP routes related to privileged administrative actions.

Its purpose is to make high-trust operational control paths explicit and separately governable.

---

## http_api/request_models/

### login_request_model.py

Defines the typed HTTP request model for login operations.

Its purpose is to normalize and validate authentication ingress payloads.

### create_session_request_model.py

Defines the typed HTTP request model for session-creation operations.

### create_project_request_model.py

Defines the typed HTTP request model for project-creation operations.

### dispatch_event_request_model.py

Defines the typed HTTP request model for event-dispatch operations.

Its role is to give explicit shape to event-ingress requests.

### hardware_command_request_model.py

Defines the typed HTTP request model for hardware-command operations.

Its purpose is especially important because embodied commands require structured and auditable ingress.

### update_configuration_request_model.py

Defines the typed HTTP request model for runtime configuration updates.

Its role is to normalize and validate configuration-changing requests.

---

## http_api/response_models/

### auth_response_model.py

Defines the typed HTTP response model for authentication-related operations.

### session_response_model.py

Defines the typed HTTP response model for session-related operations.

### project_response_model.py

Defines the typed HTTP response model for project-related operations.

### fsm_state_response_model.py

Defines the typed HTTP response model representing finite-state-machine status.

### hardware_state_response_model.py

Defines the typed HTTP response model representing hardware status.

### error_response_model.py

Defines the typed HTTP response model used for application-level error reporting.

Its purpose is to keep API error semantics explicit and consistent.

---

## http_api/dependencies/

### auth_dependency.py

Defines the dependency that enforces or injects authentication state at route boundaries.

### admin_dependency.py

Defines the dependency that enforces privileged administrative access at relevant routes.

### user_context_dependency.py

Defines the dependency that resolves and injects user-context information for route handling.

### request_trace_dependency.py

Defines the dependency that establishes or injects request-trace context.

Its role supports observability and cross-request correlation.

---

## http_api/handlers/

### api_exception_handler.py

Defines the centralized exception handler for application-level API errors.

Its purpose is to convert backend failures into structured HTTP responses.

### validation_exception_handler.py

Defines the centralized exception handler for validation-related errors at the API boundary.

Its role is to make invalid-request behavior explicit and consistent.

---

# 2. websocket_realtime

## Definition

The `websocket_realtime/` submodule defines the realtime communication layer of the backend.

Its purpose is to support live subscription-based or push-based distribution of state changes, notifications, and updates that should not depend solely on polling or synchronous request-response interaction.

This submodule is especially important for dashboards, live session state, hardware monitoring, and operational observability.

### Internal Structure

```text
websocket_realtime/
├── models/
├── services/
└── gateways/
```

---

## websocket_realtime/models/

### websocket_connection_context.py

Defines the structured context associated with a live WebSocket connection.

This may include identity, subscription state, connection metadata, authorization state, and routing metadata.

### realtime_state_payload.py

Defines the structured payload used to deliver realtime state updates.

Its purpose is to represent current or changed state in a channel-consumable way.

### realtime_notification_payload.py

Defines the structured payload used to send realtime notifications or events.

Its role is distinct from broader state payloads and focuses on event-like live updates.

### subscription_request.py

Defines the structured request by which a connection subscribes to one or more realtime channels or update categories.

---

## websocket_realtime/services/

### register_websocket_connection_service.py

Defines the operation that registers a newly established WebSocket connection.

Its purpose is to create a managed realtime connection context.

### remove_websocket_connection_service.py

Defines the operation that removes a WebSocket connection from the active realtime set.

### broadcast_fsm_state_update_service.py

Defines the operation that broadcasts finite-state-machine updates over realtime channels.

### broadcast_session_update_service.py

Defines the operation that broadcasts session-related updates over realtime channels.

### broadcast_project_update_service.py

Defines the operation that broadcasts project-related updates over realtime channels.

### broadcast_hardware_status_service.py

Defines the operation that broadcasts hardware-status updates over realtime channels.

Its role is especially important for operational monitoring and embodied runtime visibility.

---

## websocket_realtime/gateways/

### realtime_gateway_router.py

Defines the gateway route or entry surface that handles realtime WebSocket traffic.

Its purpose is to provide the transport-side entry point for realtime connection handling.

### websocket_connection_manager.py

Defines the manager responsible for tracking, organizing, and coordinating active WebSocket connections.

Its role is central to subscription-aware realtime delivery.

---

# 3. application_services

## Definition

The `application_services/` submodule defines the use-case layer of the backend.

Its purpose is to represent backend operations as explicit application use cases rather than allowing routers or coordinators to call domain logic in ad hoc ways.

Each use case here corresponds to an application-level operation exposed or required by the running system.

### Internal Structure

```text
application_services/
├── auth/
├── sessions/
├── projects/
├── dialogue/
├── hardware/
├── events/
└── administration/
```

These subdirectories group use cases by application concern.

---

## application_services/auth/

### login_use_case.py

Defines the use case that performs login through the backend application layer.

### logout_use_case.py

Defines the use case that performs logout through the backend application layer.

### refresh_auth_token_use_case.py

Defines the use case that refreshes authentication state via token renewal.

### get_current_identity_use_case.py

Defines the use case that returns the currently authenticated or active identity context.

---

## application_services/sessions/

### create_session_use_case.py

Defines the use case that creates a dialogue session through the backend application layer.

### restore_session_use_case.py

Defines the use case that restores an existing session into active backend-facing continuity.

### suspend_session_use_case.py

Defines the use case that suspends a session.

### terminate_session_use_case.py

Defines the use case that terminates a session.

---

## application_services/projects/

### create_project_use_case.py

Defines the use case that creates a conversational project.

### open_project_use_case.py

Defines the use case that opens or activates a project for continued work.

### continue_project_use_case.py

Defines the use case that continues a project from prior context.

### archive_project_use_case.py

Defines the use case that archives a project.

### complete_project_use_case.py

Defines the use case that completes a project.

---

## application_services/dialogue/

### append_dialogue_turn_use_case.py

Defines the use case that appends a new dialogue turn through the backend application layer.

### summarize_dialogue_use_case.py

Defines the use case that triggers or retrieves dialogue summarization.

### recover_dialogue_context_use_case.py

Defines the use case that reconstructs dialogue context for continuation.

---

## application_services/hardware/

### get_hardware_status_use_case.py

Defines the use case that retrieves hardware status.

### execute_hardware_command_use_case.py

Defines the use case that executes a hardware command.

### stop_hardware_action_use_case.py

Defines the use case that stops an active hardware action.

Its role is especially important for embodied safety and interruption.

---

## application_services/events/

### dispatch_system_event_use_case.py

Defines the use case that dispatches a system event into the backend runtime.

### get_recent_events_use_case.py

Defines the use case that retrieves recent events.

### replay_event_for_debug_use_case.py

Defines the use case that replays an event for debugging or diagnostic purposes.

---

## application_services/administration/

### restart_module_use_case.py

Defines the use case that triggers controlled restart of a module or subsystem.

### get_runtime_diagnostics_use_case.py

Defines the use case that retrieves runtime diagnostics.

### list_security_incidents_use_case.py

Defines the use case that retrieves security incidents for administrative inspection.

### update_runtime_configuration_use_case.py

Defines the use case that updates runtime configuration through a controlled application path.

---

# 4. coordinators_orchestrators

## Definition

The `coordinators_orchestrators/` submodule defines runtime coordination flows that span multiple internal modules and do not naturally belong inside a single domain service.

Its purpose is to make cross-module operational workflows explicit.

This is especially important in NORA because many important behaviors cross domain boundaries.

### Internal Structure

```text
coordinators_orchestrators/
├── input_to_planning_coordinator.py
├── planning_to_action_coordinator.py
├── session_project_coordinator.py
├── perception_to_fsm_coordinator.py
├── identity_context_coordinator.py
├── recovery_context_coordinator.py
├── multimodal_output_coordinator.py
└── realtime_state_distribution_coordinator.py
```

---

### input_to_planning_coordinator.py

Defines the coordinator that moves normalized input toward the planning pipeline.

Its purpose is to bridge input-origin events, semantic interpretation, and planning invocation.

### planning_to_action_coordinator.py

Defines the coordinator that moves finalized planning results into execution and expression paths.

Its role is to preserve explicit bridging between deliberation and execution.

### session_project_coordinator.py

Defines the coordinator that manages the interaction between active sessions and active projects.

Its purpose is important because session continuity and project continuity often overlap.

### perception_to_fsm_coordinator.py

Defines the coordinator that routes relevant perception outputs into finite-state-machine control flows.

### identity_context_coordinator.py

Defines the coordinator that keeps identity-related context synchronized across runtime flows.

### recovery_context_coordinator.py

Defines the coordinator that manages recovery-state activation and continuity re-entry into active runtime context.

### multimodal_output_coordinator.py

Defines the coordinator that synchronizes multimodal output behavior across voice, visual output, expressive signaling, and related channels.

Its role is especially important for coherent user-facing behavior.

### realtime_state_distribution_coordinator.py

Defines the coordinator that determines how important runtime state changes should be distributed over realtime channels.

---

# 5. event_dispatcher

## Definition

The `event_dispatcher/` submodule defines how ingress events are normalized, routed to the appropriate internal targets, and published onto the wider event infrastructure.

Its purpose is to make internal event flow explicit and structured.

This submodule is important because NORA is not purely request-response driven. It also relies on event-driven coordination.

### Internal Structure

```text
event_dispatcher/
├── models/
├── services/
└── registries/
```

---

## event_dispatcher/models/

### system_event_envelope.py

Defines the structured envelope representing an ingress system event.

This may include event type, payload, timestamps, correlation metadata, source information, and routing hints.

### event_dispatch_result.py

Defines the structured result of an event dispatch operation.

Its purpose is to record whether dispatch succeeded, where it went, and what happened during routing.

### event_route_definition.py

Defines the structured representation of an event route.

Its role is to make routing rules explicit and inspectable.

---

## event_dispatcher/services/

### normalize_ingress_event_service.py

Defines the operation that normalizes external or incoming events into the internal event structure expected by the dispatcher.

### dispatch_event_to_fsm_service.py

Defines the operation that routes relevant events into the finite-state-machine control layer.

### dispatch_event_to_dialogue_service.py

Defines the operation that routes relevant events into dialogue continuity flows.

### dispatch_event_to_planning_service.py

Defines the operation that routes relevant events into the planning architecture.

### publish_event_to_bus_service.py

Defines the operation that publishes a normalized event into the internal event bus or wider event system.

Its purpose is to connect explicit event routing with decoupled downstream propagation.

---

## event_dispatcher/registries/

### event_route_registry.py

Defines the registry of event-route definitions used by the dispatcher.

Its role is to centralize routing knowledge rather than hiding it inside scattered conditionals.

---

# 6. observability

## Definition

The `observability/` submodule inside `backend_and_application/` defines backend-local instrumentation, health reporting, and telemetry structures used to operate the backend as a live application service.

This is distinct from the top-level `src/nora/observability/` module, which centralizes broader observability architecture across the whole system.

The backend-local observability area exists to keep application-runtime visibility explicit where transport, request handling, realtime behavior, and backend execution flows are concerned.

### Internal Structure

```text
observability/
├── logs/
├── traces/
├── metrics/
└── health/
```

---

## observability/logs/

### application_log_writer.py

Defines the component responsible for writing backend application logs.

Its purpose is to capture server-side operational behavior in structured form.

### access_log_writer.py

Defines the component responsible for writing access logs related to incoming requests or transport-level interactions.

### security_log_writer.py

Defines the component responsible for writing security-relevant backend logs.

Its role is important for trust-boundary auditability at the application surface.

---

## observability/traces/

### trace_context_builder.py

Defines the component that builds trace context for backend request and execution flows.

Its purpose is to support correlation and distributed tracing across backend pathways.

### request_trace_writer.py

Defines the component that writes request-oriented trace records.

### event_trace_writer.py

Defines the component that writes event-oriented trace records.

Its role is to make event-driven backend behavior traceable.

---

## observability/metrics/

### request_latency_metric_service.py

Defines the metric service that records request latency.

### websocket_connection_metric_service.py

Defines the metric service that records WebSocket connection-related metrics.

### fsm_transition_metric_service.py

Defines the metric service that records finite-state-machine transition metrics as observed at the backend application layer.

### hardware_health_metric_service.py

Defines the metric service that records hardware-health-oriented metrics exposed through backend operational monitoring.

---

## observability/health/

### readiness_probe_service.py

Defines the service that reports whether the backend is ready to serve requests safely.

### liveness_probe_service.py

Defines the service that reports whether the backend runtime is alive.

### dependency_health_check_service.py

Defines the service that checks whether backend-critical dependencies are healthy enough for runtime operation.

Its role is important for deployment orchestration and operational supervision.

---

## Cross-Submodule Architectural Relationships

The backend and application module is best understood as an application-runtime architecture rather than as six unrelated directories.

### http_api -> application_services

HTTP routes should invoke explicit use cases rather than directly implementing domain logic.

### websocket_realtime -> coordinators_orchestrators

Realtime updates often depend on coordination decisions about what should be distributed and when.

### application_services -> coordinators_orchestrators

Some use cases remain bounded, while others require coordination across multiple modules.

### event_dispatcher -> cognitive, dialogue, and planning flows

Event dispatch is an important runtime bridge into deeper internal behavior.

### observability -> all backend surfaces

Transport boundaries, event dispatch, coordinators, and use cases all benefit from backend-local logs, traces, metrics, and health visibility.

### coordinators_orchestrators -> action and frontend state

n
Some orchestrators bridge planning to action and internal state to realtime UI distribution.

These relationships show the overall logic clearly:

* interfaces receive requests
* use cases structure backend operations
* coordinators connect modules when flows cross boundaries
* events propagate through explicit dispatch paths
* observability makes backend behavior visible

---

## What This Module Must Not Contain

To preserve architectural clarity, the backend and application module should not absorb responsibilities that belong elsewhere.

It should not contain:

* raw domain business rules for identity, dialogue, planning, action, or memory
* frontend page logic
* low-level hardware-driver implementation
* semantic-intent reasoning internals
* long-term memory extraction logic
* storage-schema ownership outside backend-specific needs
* perception-pipeline implementation

It may call, expose, coordinate, and monitor those capabilities, but it must remain the backend application layer.

---

## Interaction With Other Modules

The `backend_and_application/` module interacts with nearly every major architectural domain.

### shared

Uses shared identifiers, operation models, pagination structures, exceptions, trace metadata, and common support abstractions.

### identity_access_security

Uses authentication, authorization, security incidents, and trust-boundary enforcement at API and realtime surfaces.

### interaction_interfaces

Receives normalized interface-origin commands or exposes application operations used by interface layers.

### perception

Receives perception-origin events, distributes perception-derived state, and exposes monitoring or control surfaces for perceptual runtime behavior where needed.

### cognitive_core

Exposes operational state, dispatches events into FSM control, and retrieves runtime state for frontend or monitoring surfaces.

### dialogue_and_session

Exposes session and project operations, dialogue history operations, summarization behavior, and recovery flows.

### planning_and_agents

Invokes planning through use cases or coordinators and routes relevant ingress events toward planning paths.

### action_and_expression

Triggers action execution through application workflows and distributes output-related state over realtime channels when relevant.

### persistence_and_memory

Uses persistent storage for application-level records, event history, diagnostics, and continuity operations.

### frontend_support

Consumes view-model builders and serializers when backend outputs need to be shaped for frontend consumers.

### integrations_and_external_services

Depends on provider-backed capabilities exposed through domain modules and backend orchestration paths.

### infrastructure_and_hardware

Exposes hardware state and hardware commands through backend surfaces and operational use cases.

### observability

Coordinates with the broader observability architecture while maintaining backend-local instrumentation responsibilities.

---

## Design Constraints of the Module

The `backend_and_application/` module should obey several strict architectural constraints.

### 1. Routers must remain thin

Transport-layer code should validate, delegate, and shape responses, not implement deep domain behavior.

### 2. Use cases must remain explicit

Application operations should be represented as named use cases rather than scattered controller logic.

### 3. Cross-module flows should be coordinated explicitly

When a runtime workflow spans multiple modules, it should live in a coordinator or orchestrator rather than being improvised inside a route or use case.

### 4. Event ingress and routing must remain visible

Event-driven behavior should be structured through explicit dispatcher models, routes, and registries.

### 5. Realtime behavior must remain subscription-aware and bounded

Live updates should not become uncontrolled state broadcast noise.

### 6. Backend observability must remain first-class

Logs, traces, metrics, and health checks are part of the backend architecture, not optional extras.

### 7. Backend application logic must not steal domain ownership

This module should expose and coordinate domain capabilities, not reimplement them.

---

## Testing Implications

This module requires especially strong application-runtime testing because it is the operational surface through which many system capabilities are actually used.

Important testing categories include:

* router-boundary tests
* request-model validation tests
* response-model consistency tests
* dependency-enforcement tests
* exception-handler tests
* websocket connection lifecycle tests
* realtime broadcast tests
* application use-case tests
* coordinator workflow tests
* event-dispatch normalization tests
* event-route registry tests
* dispatch-to-FSM, dialogue, and planning tests
* access-log and request-trace tests
* latency-metric tests
* readiness and liveness tests
* dependency-health-check tests

Failures here can make the backend appear inconsistent, opaque, or operationally unreliable even when the underlying domain modules are correct.

---

## Why This Structure Fits NORA

This structure fits NORA because NORA is not just a set of libraries or internal services.

It is a live application platform that must:

* expose capabilities over HTTP
* distribute live state in realtime
* support use-case-oriented backend operations
* coordinate multi-module workflows
* dispatch internal events cleanly
* remain observable and health-checkable in operation

A flatter architecture would make it harder to preserve transport clarity, use-case explicitness, realtime structure, and backend operational visibility.

The proposed structure allows NORA to:

* expose clean application interfaces
* separate transport from use cases
* coordinate complex workflows explicitly
* support event-driven runtime behavior
* maintain backend-local observability as a first-class concern

That makes it an excellent fit for the system.

---

## Architectural Importance

The `backend_and_application/` module provides the operational application architecture through which NORA is exposed, coordinated, and run as a live backend system.

While other modules define identity, interaction, perception, runtime cognition, dialogue continuity, planning, action, persistence, integrations, and hardware structure, the live system still requires an explicit backend architecture that can expose structured HTTP APIs, maintain realtime communication surfaces, represent application operations as explicit use cases, coordinate cross-module workflows, route ingress events into the appropriate internal layers, and maintain backend-local observability and health visibility.

Through this module the architecture gains:

* explicit HTTP and realtime application boundaries
* structured backend use cases
* clear cross-module coordinators and orchestrators
* explicit event ingress and routing behavior
* backend-local logs, traces, metrics, and health probes
* cleaner separation between domain logic and application operation
* better runtime operability and maintainability

By separating HTTP APIs, WebSocket realtime behavior, application services, coordinators, event dispatch, and backend observability into explicit internal subdomains, NORA preserves both operational power and architectural clarity.

For that reason, `backend_and_application/` is one of the central runtime modules of `src/nora/`.

## Architectural Structure

```text
backend_and_application
│
├── HTTP API
│   ├── routers
│   ├── request models
│   ├── response models
│   ├── dependencies
│   └── exception handlers
│
├── WebSocket Realtime
│   ├── realtime models
│   ├── connection and broadcast services
│   └── gateways and connection manager
│
├── Application Services
│   ├── auth use cases
│   ├── session use cases
│   ├── project use cases
│   ├── dialogue use cases
│   ├── hardware use cases
│   ├── event use cases
│   └── administration use cases
│
├── Coordinators and Orchestrators
│   ├── input-to-planning coordination
│   ├── planning-to-action coordination
│   ├── session-project coordination
│   ├── perception-to-FSM coordination
│   ├── identity-context coordination
│   ├── recovery-context coordination
│   ├── multimodal-output coordination
│   └── realtime-state distribution coordination
│
├── Event Dispatcher
│   ├── event envelopes
│   ├── dispatch results
│   ├── route definitions
│   ├── ingress normalization
│   ├── dispatch to FSM
│   ├── dispatch to dialogue
│   ├── dispatch to planning
│   ├── event-bus publication
│   └── route registry
│
└── Backend Observability
    ├── backend logs
    ├── backend traces
    ├── backend metrics
    └── backend health probes
```

```
backend_and_application/
├── http_api/
│   ├── routers/
│   │   ├── auth_router.py
│   │   ├── users_router.py
│   │   ├── sessions_router.py
│   │   ├── projects_router.py
│   │   ├── events_router.py
│   │   ├── fsm_router.py
│   │   ├── hardware_router.py
│   │   ├── configuration_router.py
│   │   ├── monitoring_router.py
│   │   └── admin_router.py
│   ├── request_models/
│   │   ├── login_request_model.py
│   │   ├── create_session_request_model.py
│   │   ├── create_project_request_model.py
│   │   ├── dispatch_event_request_model.py
│   │   ├── hardware_command_request_model.py
│   │   └── update_configuration_request_model.py
│   ├── response_models/
│   │   ├── auth_response_model.py
│   │   ├── session_response_model.py
│   │   ├── project_response_model.py
│   │   ├── fsm_state_response_model.py
│   │   ├── hardware_state_response_model.py
│   │   └── error_response_model.py
│   ├── dependencies/
│   │   ├── auth_dependency.py
│   │   ├── admin_dependency.py
│   │   ├── user_context_dependency.py
│   │   └── request_trace_dependency.py
│   └── handlers/
│       ├── api_exception_handler.py
│       └── validation_exception_handler.py
│
├── websocket_realtime/
│   ├── models/
│   │   ├── websocket_connection_context.py
│   │   ├── realtime_state_payload.py
│   │   ├── realtime_notification_payload.py
│   │   └── subscription_request.py
│   ├── services/
│   │   ├── register_websocket_connection_service.py
│   │   ├── remove_websocket_connection_service.py
│   │   ├── broadcast_fsm_state_update_service.py
│   │   ├── broadcast_session_update_service.py
│   │   ├── broadcast_project_update_service.py
│   │   └── broadcast_hardware_status_service.py
│   └── gateways/
│       ├── realtime_gateway_router.py
│       └── websocket_connection_manager.py
│
├── application_services/
│   ├── auth/
│   │   ├── login_use_case.py
│   │   ├── logout_use_case.py
│   │   ├── refresh_auth_token_use_case.py
│   │   └── get_current_identity_use_case.py
│   ├── sessions/
│   │   ├── create_session_use_case.py
│   │   ├── restore_session_use_case.py
│   │   ├── suspend_session_use_case.py
│   │   └── terminate_session_use_case.py
│   ├── projects/
│   │   ├── create_project_use_case.py
│   │   ├── open_project_use_case.py
│   │   ├── continue_project_use_case.py
│   │   ├── archive_project_use_case.py
│   │   └── complete_project_use_case.py
│   ├── dialogue/
│   │   ├── append_dialogue_turn_use_case.py
│   │   ├── summarize_dialogue_use_case.py
│   │   └── recover_dialogue_context_use_case.py
│   ├── hardware/
│   │   ├── get_hardware_status_use_case.py
│   │   ├── execute_hardware_command_use_case.py
│   │   └── stop_hardware_action_use_case.py
│   ├── events/
│   │   ├── dispatch_system_event_use_case.py
│   │   ├── get_recent_events_use_case.py
│   │   └── replay_event_for_debug_use_case.py
│   └── administration/
│       ├── restart_module_use_case.py
│       ├── get_runtime_diagnostics_use_case.py
│       ├── list_security_incidents_use_case.py
│       └── update_runtime_configuration_use_case.py
│
├── coordinators_orchestrators/
│   ├── input_to_planning_coordinator.py
│   ├── planning_to_action_coordinator.py
│   ├── session_project_coordinator.py
│   ├── perception_to_fsm_coordinator.py
│   ├── identity_context_coordinator.py
│   ├── recovery_context_coordinator.py
│   ├── multimodal_output_coordinator.py
│   └── realtime_state_distribution_coordinator.py
│
├── event_dispatcher/
│   ├── models/
│   │   ├── system_event_envelope.py
│   │   ├── event_dispatch_result.py
│   │   └── event_route_definition.py
│   ├── services/
│   │   ├── normalize_ingress_event_service.py
│   │   ├── dispatch_event_to_fsm_service.py
│   │   ├── dispatch_event_to_dialogue_service.py
│   │   ├── dispatch_event_to_planning_service.py
│   │   └── publish_event_to_bus_service.py
│   └── registries/
│       └── event_route_registry.py
│
└── observability/
    ├── logs/
    │   ├── application_log_writer.py
│   │   ├── access_log_writer.py
│   │   └── security_log_writer.py
│   ├── traces/
│   │   ├── trace_context_builder.py
│   │   ├── request_trace_writer.py
│   │   └── event_trace_writer.py
│   ├── metrics/
│   │   ├── request_latency_metric_service.py
│   │   ├── websocket_connection_metric_service.py
│   │   ├── fsm_transition_metric_service.py
│   │   └── hardware_health_metric_service.py
│   └── health/
│       ├── readiness_probe_service.py
│       ├── liveness_probe_service.py
│       └── dependency_health_check_service.py
```

# Frontend Support Module

## Definition

The `frontend_support/` module defines the backend-side representation layer that prepares NORA’s internal state and domain outputs for frontend consumption.

While the actual frontend application lives outside `src/nora/` in its own dedicated project, the backend still requires a structured internal area responsible for shaping backend information into forms that visual clients can consume cleanly, consistently, and efficiently.

That is the role of `frontend_support/`.

In architectural terms, this module defines the presentation-adaptation layer of the backend.

It is the module that stands between:

* rich internal domain structures
  and
* frontend-facing payloads, view models, and serialized representations

This module therefore defines:

* backend-side view-model construction
* presenter logic for selected domain objects
* serialization of realtime payloads
* serialization of dashboard payloads
* serialization of artifact descriptors
* UI-oriented representation shaping without moving UI ownership into the backend

This module is not the frontend itself.

It does not define pages, components, layouts, routes, client state stores, or visual rendering logic.

That belongs to the actual frontend application.

This module is also not the same as the backend transport layer.

The backend transport layer exposes APIs and realtime channels.

The frontend support module defines how backend data is shaped so those interfaces can deliver frontend-usable structures without leaking raw internal domain complexity.

For that reason, `frontend_support/` is a representation-support module of the backend, not a UI module and not a general domain module.

---

## Architectural Purpose

The purpose of the `frontend_support/` module is to prevent frontend clients from coupling directly to the full complexity of internal backend models.

A system like NORA contains many rich internal structures:

* sessions
* projects
* dialogue turns
* hardware state
* monitoring information
* security incidents
* artifacts
* realtime state updates

These internal structures often contain more information than a given frontend view actually needs, and they may be organized around backend concerns rather than UI concerns.

Without a dedicated frontend-support layer, several architectural problems appear quickly:

* frontend clients become tightly coupled to domain models
* transport payloads expose too much internal structure
* UI-oriented aggregation logic gets duplicated across routes or frontend code
* backend responses become inconsistent across endpoints
* dashboard payloads become ad hoc and difficult to evolve
* realtime messages become noisy, unstable, or overly raw

By introducing a dedicated frontend-support module, NORA gains:

* stable UI-facing representation structures
* cleaner separation between domain models and frontend payloads
* explicit view-model construction logic
* reusable presentation transformations
* more consistent realtime and dashboard serialization
* easier frontend evolution without forcing domain-model changes
* clearer ownership of backend-side UI shaping concerns

This module therefore provides the backend representation architecture that makes frontend integration cleaner and safer.

---

## Core Architectural Principle

The most important design principle of this module is the following:

Backend representation shaping for frontend consumption must be separated into view-model building, presentation formatting, and serialization.

These concerns are related, but they are not identical.

### View models

Define UI-oriented backend data structures shaped around how frontend screens or panels need to consume information.

### Presenters

Define transformation logic that turns selected domain objects into frontend-friendly representational forms.

### Serializers

Define the final conversion into transport-ready payload structures for realtime channels, dashboards, and artifact delivery.

This separation matters because not every frontend-facing object is the same kind of representation task.

A view model may aggregate information across several domains.

A presenter may adapt one domain object.

A serializer may convert an already shaped representation into a stable wire format.

---

## Internal Module Structure

The proposed structure is the following:

```text
frontend_support/
├── view_models/
├── presenters/
└── serializers/
```

This structure divides backend-side frontend support into three major internal subdomains.

### view_models

Defines builders for frontend-oriented structured data models.

### presenters

Defines object-level presentation transformations.

### serializers

Defines transport-ready serialization of frontend-facing payloads.

This decomposition is intentionally narrow.

The module should remain focused on representation shaping and should not become a second backend orchestration layer or a shadow frontend implementation.

---

## Architectural Role Within the Full System

The `frontend_support/` module sits between domain/application output and frontend transport consumption.

It receives inputs from:

* backend application services
* coordinators and orchestrators
* dialogue and session structures
* hardware status structures
* monitoring and observability structures
* artifact metadata
* security and administration structures

It then shapes those inputs into frontend-usable forms for:

* HTTP responses
* dashboard endpoints
* realtime payloads
* artifact descriptors
* admin views
* monitoring panels
* conversation views

This means the module does not own business decisions.

It owns representational adaptation.

---

# 1. view_models

## Definition

The `view_models/` submodule defines backend-side builders that create structured data models shaped around frontend views or frontend feature areas.

Its purpose is to provide explicit UI-oriented representations that may aggregate, simplify, reorder, or enrich internal information for frontend use.

These builders are especially useful when a frontend view depends on several internal structures at once.

### Internal Structure

```text
view_models/
├── conversation_view_model_builder.py
├── project_view_model_builder.py
├── session_history_view_model_builder.py
├── hardware_dashboard_view_model_builder.py
├── monitoring_dashboard_view_model_builder.py
└── admin_dashboard_view_model_builder.py
```

---

### conversation_view_model_builder.py

Defines the builder that constructs the frontend-facing view model for conversation-oriented UI surfaces.

Its purpose is to shape dialogue, session, speaker, summary, and context information into a form convenient for conversation views.

This may include:

* visible turn lists
* speaker labels
* message grouping
* summary banners
* active-session cues
* pending clarification markers
* conversation-level metadata

Its role is especially important because raw dialogue history often does not map directly to how a conversation UI should consume data.

### project_view_model_builder.py

Defines the builder that constructs the frontend-facing view model for project-oriented UI surfaces.

Its purpose is to shape project state, goals, tasks, notes, artifacts, and continuity metadata into a coherent project representation.

This may support project dashboards, project detail views, or project-switching interfaces.

### session_history_view_model_builder.py

Defines the builder that constructs the frontend-facing view model for session history views.

Its role is to organize session metadata, summaries, boundaries, statuses, and continuity pointers into a structure suitable for historical browsing.

### hardware_dashboard_view_model_builder.py

Defines the builder that constructs the frontend-facing view model for hardware dashboards.

Its purpose is to shape hardware status, subsystem availability, device condition, and runtime hardware indicators into a coherent monitoring surface.

### monitoring_dashboard_view_model_builder.py

Defines the builder that constructs the frontend-facing view model for monitoring dashboards.

This may include health indicators, runtime metrics, alerts, trace summaries, and state summaries prepared for backend or operator-facing monitoring interfaces.

### admin_dashboard_view_model_builder.py

Defines the builder that constructs the frontend-facing view model for administrative dashboards.

Its purpose is to aggregate administrative state such as privileged actions, configuration summaries, security incidents, health visibility, and management controls into a coherent admin-facing structure.

---

# 2. presenters

## Definition

The `presenters/` submodule defines focused presentation transformers for selected domain objects.

Its purpose is to adapt individual backend objects into frontend-friendly representational forms without forcing view-model builders to handle all transformation detail internally.

Presenters are narrower than full view-model builders.

They typically operate at the level of one domain object or one object family.

### Internal Structure

```text
presenters/
├── session_presenter.py
├── project_presenter.py
├── dialogue_turn_presenter.py
├── hardware_state_presenter.py
└── security_incident_presenter.py
```

---

### session_presenter.py

Defines the presenter that adapts session-domain objects into presentation-oriented session representations.

Its purpose is to convert internal session structures into stable frontend-consumable forms with the right level of detail.

This may include:

* session identifiers
* lifecycle status labels
* summary fragments
* timestamp formatting
* active or inactive indicators
* UI-friendly boundary information

### project_presenter.py

Defines the presenter that adapts project-domain objects into presentation-oriented project representations.

Its purpose is to make project state usable for frontend display without leaking raw backend structures.

This may include:

* project title and status
* active-goal representation
* visible task summaries
* artifact counts or descriptors
* continuity cues

### dialogue_turn_presenter.py

Defines the presenter that adapts dialogue-turn objects into frontend-friendly message representations.

Its role is especially important because raw dialogue turns may contain metadata or internal annotations not intended for direct frontend use.

This presenter may shape:

* speaker labels
* content formatting
* modality hints
* timestamps
* UI flags such as pending, summarized, or system-generated markers

### hardware_state_presenter.py

Defines the presenter that adapts hardware-state structures into frontend-facing hardware representations.

Its purpose is to turn hardware condition, availability, or device-status data into clear UI-oriented output forms.

### security_incident_presenter.py

Defines the presenter that adapts security-incident objects into administrative or monitoring-friendly frontend representations.

Its role is important because security data often needs careful frontend shaping to remain useful and not overly raw.

---

# 3. serializers

## Definition

The `serializers/` submodule defines the final serialization layer that converts already shaped frontend-support structures into transport-ready payloads.

Its purpose is to establish stable, explicit output serialization for selected frontend-facing delivery contexts.

Serialization here is not about generic persistence serialization.

It is about backend-to-frontend delivery formatting.

### Internal Structure

```text
serializers/
├── realtime_payload_serializer.py
├── dashboard_payload_serializer.py
└── artifact_descriptor_serializer.py
```

---

### realtime_payload_serializer.py

Defines the serializer that converts backend-side realtime representations into transport-ready realtime payloads.

Its purpose is to ensure live updates are delivered in a stable, frontend-consumable format.

This may include:

* state updates
* notification payloads
* event-driven deltas
* channel-tagged realtime messages

Its role is especially important because realtime consumers are sensitive to payload instability.

### dashboard_payload_serializer.py

Defines the serializer that converts dashboard-oriented representations into transport-ready dashboard payloads.

Its purpose is to support monitoring, hardware, and admin dashboards through consistent backend serialization.

### artifact_descriptor_serializer.py

Defines the serializer that converts artifact references or artifact metadata into frontend-ready descriptor payloads.

Its role is to support file previews, download links, artifact listings, or artifact metadata views.

---

## Cross-Submodule Architectural Relationships

The frontend support module is best understood as a representation pipeline rather than as three isolated folders.

### view_models -> presenters

View-model builders may depend on presenters to adapt specific domain objects before aggregating them into larger frontend-facing structures.

### presenters -> serializers

n
Presented objects often become the inputs to serializers when transport-ready payloads are required.

### view_models -> serializers

Some view-model outputs may be serialized directly into dashboard or realtime payloads depending on delivery context.

These relationships show the internal logic clearly:

* presenters adapt objects
* view models assemble frontend-oriented structures
* serializers finalize transport payloads

---

## What This Module Must Not Contain

To preserve architectural clarity, the frontend support module should not absorb responsibilities that belong elsewhere.

It should not contain:

* React components
* frontend routes or layouts
* browser-side state management
* backend domain business rules
* transport-router logic
* direct database access unrelated to representation shaping
* planner logic
* hardware-driver logic
* long-term memory logic

It may consume outputs from all of those layers, but it must remain a backend-side representation-support module.

---

## Interaction With Other Modules

The `frontend_support/` module interacts with many other architectural domains.

### shared

Uses shared identifiers, timestamps, pagination structures, file-type metadata, and common support abstractions for shaping frontend-facing payloads.

### identity_access_security

Presents user context, trust-related state, and security-incident information for frontend or administrative views.

### interaction_interfaces

May shape interface-origin state or channel-origin indicators for frontend display.

### perception

May present perception-derived state, presence signals, or monitored perception context in dashboards where relevant.

### cognitive_core

Presents operational state, modulation cues, and runtime context information for frontend or monitoring interfaces.

### dialogue_and_session

Presents sessions, projects, dialogue turns, summaries, and recovery-related continuity structures.

### planning_and_agents

May present planning state, clarification requests, or execution-preparation results in frontend-facing views.

### action_and_expression

Presents visual-output state, hardware command outcomes, communication results, or artifact descriptors where needed.

### persistence_and_memory

Uses artifact references, session history data, project history data, and stored continuity structures as representation inputs.

### backend_and_application

Serves as a support layer for backend APIs, realtime services, dashboards, and application responses.

### integrations_and_external_services

May expose representation-friendly views of integrated capabilities, provider-backed artifacts, or external service state when required.

### infrastructure_and_hardware

Presents hardware and device state through frontend-oriented dashboards and status views.

### observability

Shapes metrics, health indicators, traces, and incident-related visibility into dashboard-oriented payloads.

---

## Design Constraints of the Module

The `frontend_support/` module should obey several strict architectural constraints.

### 1. Representation shaping must remain separate from frontend implementation

This module prepares backend data for the frontend but must not become the frontend itself.

### 2. Presenters and view models must not own business rules

They may shape outputs, but they should not become a hidden domain-logic layer.

### 3. Serialization must remain explicit

Frontend-facing transport payloads should be stable and intentionally defined rather than emerging accidentally from domain models.

### 4. Aggregation should remain UI-oriented, not domain-distorting

View-model builders may aggregate data for UI convenience, but they should not invent contradictory domain semantics.

### 5. Reuse should remain bounded

This module should not become a dumping ground for generic transformation code unrelated to frontend representation.

### 6. Frontend consumers should be shielded from raw backend complexity

One of the main values of this module is reducing coupling between frontend clients and internal backend structures.

---

## Testing Implications

This module requires especially strong representation-focused testing because payload instability or presentation leakage can break frontend behavior even when the underlying domain logic is correct.

Important testing categories include:

* conversation view-model construction tests
* project view-model construction tests
* session-history view-model tests
* hardware-dashboard view-model tests
* monitoring-dashboard view-model tests
* admin-dashboard view-model tests
* session-presenter tests
* project-presenter tests
* dialogue-turn presentation tests
* hardware-state presentation tests
* security-incident presentation tests
* realtime payload serialization tests
* dashboard payload serialization tests
* artifact descriptor serialization tests
* frontend-payload backward-compatibility tests where relevant

Failures here can make the frontend inconsistent, over-coupled, or difficult to evolve.

---

## Why This Structure Fits NORA

This structure fits NORA because NORA is a backend-heavy system with rich internal structures and multiple frontend-oriented consumption surfaces.

It needs backend-side support for:

* conversation views
* project views
* history views
* hardware dashboards
* monitoring dashboards
* admin dashboards
* realtime state distribution
* artifact access

A flatter backend would either expose raw domain structures directly or duplicate representation logic across routers and frontend clients.

The proposed structure allows NORA to:

* keep backend representation shaping explicit
* reduce frontend coupling to internal models
* support multiple dashboard and view contexts cleanly
* serialize frontend payloads consistently
* evolve frontend-facing structures with less architectural friction

That makes it an excellent fit for the system.

---

## Architectural Importance

The `frontend_support/` module provides the backend-side representation architecture through which NORA’s internal state becomes consumable by frontend clients without exposing raw domain complexity directly.

While the actual frontend application lives outside the backend source tree, the backend still requires an explicit module that can build UI-oriented view models, present selected domain objects in stable frontend-facing forms, and serialize those representations into realtime, dashboard, and artifact-delivery payloads.

Through this module the architecture gains:

* explicit backend-side view-model construction
* focused object presenters for frontend-oriented representation
* stable serialization of realtime, dashboard, and artifact payloads
* reduced coupling between frontend clients and raw internal domain models
* cleaner support for conversation, project, hardware, monitoring, and administrative interfaces

By separating view-model builders, presenters, and serializers into explicit internal subdomains, NORA preserves both frontend-consumption clarity and backend architectural discipline.

For that reason, `frontend_support/` is an important backend-support module of `src/nora/`.

## Architectural Structure

```text
frontend_support
│
├── View Models
│   ├── conversation view-model builders
│   ├── project view-model builders
│   ├── session-history view-model builders
│   ├── hardware dashboard view-model builders
│   ├── monitoring dashboard view-model builders
│   └── admin dashboard view-model builders
│
├── Presenters
│   ├── session presenters
│   ├── project presenters
│   ├── dialogue-turn presenters
│   ├── hardware-state presenters
│   └── security-incident presenters
│
└── Serializers
    ├── realtime payload serializers
    ├── dashboard payload serializers
    └── artifact descriptor serializers
```

```
frontend_support/
├── view_models/
│   ├── conversation_view_model_builder.py
│   ├── project_view_model_builder.py
│   ├── session_history_view_model_builder.py
│   ├── hardware_dashboard_view_model_builder.py
│   ├── monitoring_dashboard_view_model_builder.py
│   └── admin_dashboard_view_model_builder.py
│
├── presenters/
│   ├── session_presenter.py
│   ├── project_presenter.py
│   ├── dialogue_turn_presenter.py
│   ├── hardware_state_presenter.py
│   └── security_incident_presenter.py
│
└── serializers/
    ├── realtime_payload_serializer.py
    ├── dashboard_payload_serializer.py
    └── artifact_descriptor_serializer.py
```
# Integrations and External Services Module

## Definition

The `integrations_and_external_services/` module defines how NORA connects to external engines, third-party platforms, provider-backed capabilities, and replaceable technology backends that supply specialized functionality to the system.

While other architectural modules define identity, interaction channels, perception, runtime cognition, dialogue continuity, planning, action, persistence, backend behavior, frontend support, hardware structure, and observability, those modules do not by themselves implement every capability internally.

A system like NORA depends on many external engines and services for tasks such as:

* speech recognition
* text-to-speech
* wake-word detection
* natural-language processing
* entity extraction
* summarization
* translation
* large-language-model reasoning
* vision inference and OCR
* web and map search
* media access
* productivity-platform integration
* IoT platform access
* embedding generation and vector indexing

That is the role of `integrations_and_external_services/`.

In architectural terms, this module defines the external capability boundary of NORA.

It is the module that makes it possible for the rest of the system to use external technologies through stable internal abstractions instead of hard-coding direct vendor or library dependence into domain modules.

This module therefore defines:

* provider interfaces for external capabilities
* adapter implementations for specific engines, APIs, or libraries
* capability groupings by domain
* substitution boundaries between abstract capability and concrete technology
* a controlled dependency boundary between NORA and the outside ecosystem

This module is not the same as planning.

Planning decides which capabilities should be used.

Integrations and external services provide the actual external capability bindings.

This module is also not the same as action, perception, or memory.

Those modules consume these capabilities.

This module defines how such capabilities are reached through explicit external-service architecture.

For that reason, `integrations_and_external_services/` is one of the most strategically important infrastructure-facing modules in NORA.

---

## Architectural Purpose

The purpose of the `integrations_and_external_services/` module is to prevent NORA’s core architecture from being tightly coupled to specific vendors, model providers, SDKs, APIs, or local libraries.

A system like NORA needs to be able to evolve over time.

It may need to:

* replace one speech engine with another
* switch from a cloud LLM to a local one
* use different OCR engines in different environments
* route between multiple model providers
* integrate with several productivity ecosystems
* support multiple IoT platforms
* change embedding or vector-index technology

Without a dedicated integration architecture, those dependencies would leak directly into domain modules and create serious architectural problems such as:

* vendor lock-in at the code level
* poor testability
* difficult local/offline deployment options
* duplicated integration logic across modules
* hidden coupling between domain behavior and specific APIs
* brittle migration when technologies change
* unclear failure boundaries for external capabilities

By introducing a dedicated integrations and external services module, NORA gains:

* stable provider abstractions
* explicit adapter implementations
* clearer boundaries between internal semantics and external technologies
* easier substitution of engines and vendors
* cleaner testing through provider mocking
* better deployment flexibility
* more disciplined control over external dependencies

This module therefore provides the architecture of replaceable external capability.

---

## Core Architectural Principle

The most important design principle of this module is the following:

External capability must be separated into provider abstractions and concrete adapters, organized by capability family.

This means the module should not be treated as a random collection of vendor wrappers.

Instead, it should preserve a consistent architecture:

### Providers

Define what the system expects a capability to do.

### Adapters

Define how a specific external engine, SDK, API, or library fulfills that capability.

### Capability families

Group related providers and adapters according to the type of external functionality they support.

This separation is essential because the rest of NORA should depend on capability semantics, not on one specific implementation technology.

---

## Internal Module Structure

The proposed structure is the following:

```text
integrations_and_external_services/
├── audio_and_language_engines/
├── linguistic_intelligence/
├── language_models/
├── vision_and_ocr/
├── search_and_internet/
├── multimedia_services/
├── productivity_services/
├── iot_platforms/
└── semantic_embeddings/
```

This structure divides the external-capability architecture into nine major subdomains.

### audio_and_language_engines

Defines external capabilities related to speech and spoken-language signal processing.

### linguistic_intelligence

Defines classical or structured NLP capabilities beyond general-purpose LLMs.

### language_models

Defines general and specialized large-language-model capability boundaries.

### vision_and_ocr

Defines external vision, detection, gesture, face, and OCR capabilities.

### search_and_internet

Defines information-retrieval capabilities from web and internet services.

### multimedia_services

Defines external media and streaming capabilities.

### productivity_services

Defines integrations with calendars, email, notes, tasks, storage, and document tools.

### iot_platforms

Defines integrations with home automation, smart devices, and IoT ecosystems.

### semantic_embeddings

Defines capabilities for embeddings, reranking, and vector indexing.

This decomposition is important because external-service integration is not one concern. It is a family of concerns organized by capability domain.

---

## Architectural Role Within the Full System

The `integrations_and_external_services/` module sits at the external capability boundary of NORA.

It receives requests for capabilities from internal modules such as:

* perception
* planning and agents
* action and expression
* persistence and memory
* backend and application
* frontend support in limited representation contexts

It then exposes those capabilities through stable internal interfaces, while delegating actual execution to concrete adapter implementations.

This means the module stands between:

* internal domain needs
  and
* external technologies or platforms

It is therefore a mediation layer, a substitution layer, and a dependency-isolation layer.

---

# 1. audio_and_language_engines

## Definition

The `audio_and_language_engines/` submodule defines provider abstractions and concrete adapters for external speech and spoken-language signal technologies.

Its purpose is to support capabilities such as:

* speech-to-text
* text-to-speech
* wake-word detection
* voice activity detection
* speaker identification
* speaker diarization

This submodule is especially important because audio interaction in NORA depends heavily on replaceable third-party or local engines.

### Internal Structure

```text
audio_and_language_engines/
├── providers/
└── adapters/
```

---

## audio_and_language_engines/providers/

### speech_to_text_provider.py

Defines the provider interface for converting spoken audio into text.

Its purpose is to give the rest of the system a stable speech-recognition capability boundary.

### text_to_speech_provider.py

Defines the provider interface for converting text into synthesized speech.

Its role is to abstract voice-generation technology from voice-output semantics.

### wake_word_provider.py

Defines the provider interface for wake-word detection capability.

Its purpose is to separate wake-trigger logic from specific wake-word engines.

### voice_activity_detection_provider.py

Defines the provider interface for detecting speech activity or voiced segments within audio streams.

### speaker_identification_provider.py

Defines the provider interface for speaker-identification or speaker-matching capability.

### speaker_diarization_provider.py

Defines the provider interface for speaker diarization capability, meaning the segmentation of speech by speaker across audio streams.

---

## audio_and_language_engines/adapters/

### whisper_stt_adapter.py

Defines the concrete adapter that fulfills the speech-to-text provider contract using Whisper-based speech-recognition capability.

### pyttsx_tts_adapter.py

Defines the concrete adapter that fulfills the text-to-speech provider contract using a pyttsx-based synthesis engine.

### porcupine_wake_word_adapter.py

Defines the concrete adapter that fulfills the wake-word provider contract using Porcupine-based wake detection.

These adapters make the chosen technology explicit while preserving provider-level abstraction.

---

# 2. linguistic_intelligence

## Definition

The `linguistic_intelligence/` submodule defines provider abstractions and concrete adapters for structured language-processing capabilities that are not necessarily equivalent to full generative LLM behavior.

Its purpose is to expose capabilities such as:

* NLP parsing or linguistic analysis
* entity recognition
* intent classification
* summarization
* translation

This submodule is important because many language tasks benefit from specialized tooling distinct from general-purpose language models.

### Internal Structure

```text
linguistic_intelligence/
├── providers/
└── adapters/
```

---

## linguistic_intelligence/providers/

### nlp_engine_provider.py

Defines the provider interface for general NLP-engine capability.

Its purpose is to expose structured linguistic-processing support such as parsing, tokenization, tagging, or linguistic annotation.

### entity_recognition_provider.py

Defines the provider interface for entity-recognition capability.

Its role is to abstract named-entity or concept-extraction technology.

### intent_classifier_provider.py

Defines the provider interface for intent-classification capability.

Its purpose is to expose structured intent recognition without hard-coding one specific model family.

### summarization_provider.py

Defines the provider interface for summarization capability.

Its role is to support bounded summary generation through replaceable technologies.

### translation_provider.py

Defines the provider interface for translation capability.

Its purpose is to expose multilingual transformation support through stable internal semantics.

---

## linguistic_intelligence/adapters/

### spacy_nlp_adapter.py

Defines the concrete adapter that fulfills the NLP-engine provider contract using spaCy-based functionality.

### transformers_ner_adapter.py

Defines the concrete adapter that fulfills the entity-recognition provider contract using transformer-based named-entity recognition capability.

### deepl_translation_adapter.py

Defines the concrete adapter that fulfills the translation provider contract using DeepL-based translation capability.

---

# 3. language_models

## Definition

The `language_models/` submodule defines provider abstractions and concrete adapters for large-language-model capabilities used by NORA.

Its purpose is to support:

* general LLM completion or generation
* structured-output generation
* reasoning-oriented model use
* routing across multiple model backends

This submodule is important because LLM usage in NORA may vary by task, deployment mode, privacy constraint, or performance requirement.

### Internal Structure

```text
language_models/
├── providers/
└── adapters/
```

---

## language_models/providers/

### llm_provider.py

Defines the provider interface for general large-language-model capability.

Its purpose is to expose broad generative language capability without binding directly to one provider.

### structured_output_llm_provider.py

Defines the provider interface for LLM capability specialized in producing structured outputs.

Its role is important where downstream systems depend on schema-like or constrained responses.

### reasoning_llm_provider.py

Defines the provider interface for reasoning-oriented LLM usage.

Its purpose is to separate generic text generation from deeper deliberative model invocation.

### model_router_provider.py

Defines the provider interface for routing requests across multiple model backends.

Its role is important in systems where different model classes may be used depending on task, latency, privacy, or capability needs.

---

## language_models/adapters/

### openai_llm_adapter.py

Defines the concrete adapter that fulfills relevant LLM provider contracts using OpenAI-backed language models.

### ollama_llm_adapter.py

Defines the concrete adapter that fulfills relevant LLM provider contracts using Ollama-based local or routed model execution.

### local_transformers_llm_adapter.py

Defines the concrete adapter that fulfills relevant LLM provider contracts using locally hosted transformer models.

### llm_router_adapter.py

Defines the concrete adapter that fulfills the model-router provider contract by choosing between multiple available model backends.

---

# 4. vision_and_ocr

## Definition

The `vision_and_ocr/` submodule defines provider abstractions and concrete adapters for external visual inference and OCR capabilities.

Its purpose is to support capabilities such as:

* general vision inference
* object detection
* face recognition
* gesture recognition
* optical character recognition

This submodule is especially important because perception-related visual capabilities often depend on specialized external libraries or engines.

### Internal Structure

```text
vision_and_ocr/
├── providers/
└── adapters/
```

---

## vision_and_ocr/providers/

### vision_inference_provider.py

Defines the provider interface for general visual inference capability.

Its purpose is to expose image- or frame-based interpretation support abstractly.

### object_detection_provider.py

Defines the provider interface for object-detection capability.

### face_recognition_provider.py

Defines the provider interface for face-recognition capability.

Its role is to abstract external face-analysis technology from perception semantics.

### gesture_recognition_provider.py

Defines the provider interface for gesture-recognition capability.

### ocr_provider.py

Defines the provider interface for optical character recognition capability.

Its purpose is to support text extraction from visual inputs through replaceable engines.

---

## vision_and_ocr/adapters/

### opencv_vision_adapter.py

Defines the concrete adapter that fulfills visual-inference-related provider contracts using OpenCV-based capability.

### mediapipe_gesture_adapter.py

Defines the concrete adapter that fulfills gesture-recognition provider contracts using MediaPipe-based functionality.

### yolovision_adapter.py

Defines the concrete adapter that fulfills object-detection or visual-detection provider contracts using YOLO-based capability.

### tesseract_ocr_adapter.py

Defines the concrete adapter that fulfills OCR provider contracts using Tesseract-based OCR functionality.

---

# 5. search_and_internet

## Definition

The `search_and_internet/` submodule defines provider abstractions and concrete adapters for external information-retrieval and internet-facing capability.

Its purpose is to support access to:

* web search
* page fetching
* news search
* map search
* weather data

This submodule is important because many tasks in NORA require external informational grounding beyond internal memory.

### Internal Structure

```text
search_and_internet/
├── providers/
└── adapters/
```

---

## search_and_internet/providers/

### web_search_provider.py

Defines the provider interface for general web-search capability.

Its purpose is to expose external web retrieval through a stable contract.

### page_fetch_provider.py

Defines the provider interface for retrieving page content or page-level source material.

### news_search_provider.py

Defines the provider interface for searching current or indexed news sources.

### map_search_provider.py

Defines the provider interface for map or place-search capability.

Its role supports location-aware informational tasks.

### weather_provider.py

Defines the provider interface for weather data retrieval.

Its purpose is to expose forecast or current-condition capability cleanly.

---

## search_and_internet/adapters/

### serpapi_search_adapter.py

Defines the concrete adapter that fulfills web-search-related provider contracts using SerpAPI-backed capability.

### requests_page_fetch_adapter.py

Defines the concrete adapter that fulfills page-fetch provider contracts using request-based page retrieval.

### maps_service_adapter.py

Defines the concrete adapter that fulfills map-search provider contracts using a maps-capable external service.

### weather_api_adapter.py

Defines the concrete adapter that fulfills weather-provider contracts using a weather API.

---

# 6. multimedia_services

## Definition

The `multimedia_services/` submodule defines provider abstractions and concrete adapters for external media and streaming capabilities.

Its purpose is to support access to:

* media streaming
* audio catalogs
* video catalogs
* remote speaker or playback surfaces

This submodule is important because media-related functionality often depends on external platforms, catalogs, or output services.

### Internal Structure

```text
multimedia_services/
├── providers/
└── adapters/
```

---

## multimedia_services/providers/

### media_streaming_provider.py

Defines the provider interface for streaming-oriented media access.

### audio_catalog_provider.py

Defines the provider interface for audio catalog access.

Its purpose is to expose browsable or resolvable audio content through a stable contract.

### video_catalog_provider.py

Defines the provider interface for video catalog access.

### remote_speaker_provider.py

Defines the provider interface for remote speaker or external audio-sink control.

Its role supports playback routed beyond local hardware where such capability is available.

---

## multimedia_services/adapters/

### spotify_adapter.py

Defines the concrete adapter that fulfills relevant multimedia-provider contracts using Spotify-backed capability.

### youtube_adapter.py

Defines the concrete adapter that fulfills relevant multimedia-provider contracts using YouTube-backed capability.

### local_media_library_adapter.py

Defines the concrete adapter that fulfills multimedia-provider contracts using a local media library source.

---

# 7. productivity_services

## Definition

The `productivity_services/` submodule defines provider abstractions and concrete adapters for external productivity ecosystems and tools.

Its purpose is to support capabilities such as:

* calendar access
* email access
* notes access
* task access
* cloud storage access
* document-editing access

This submodule is especially important because many assistant-like tasks require integration with personal or organizational productivity systems.

### Internal Structure

```text
productivity_services/
├── providers/
└── adapters/
```

---

## productivity_services/providers/

### calendar_provider.py

Defines the provider interface for calendar capability.

Its purpose is to abstract scheduling and calendar access from concrete calendar platforms.

### email_provider.py

Defines the provider interface for email capability.

Its role supports reading, drafting, sending, or otherwise interacting with email systems under the correct higher-level module policies.

### notes_provider.py

Defines the provider interface for notes capability.

### tasks_provider.py

Defines the provider interface for tasks capability.

### cloud_storage_provider.py

Defines the provider interface for cloud-storage capability.

### document_editor_provider.py

Defines the provider interface for document-editing capability.

Its purpose is to abstract document-creation or document-editing systems from internal application semantics.

---

## productivity_services/adapters/

### google_calendar_adapter.py

Defines the concrete adapter that fulfills calendar-provider contracts using Google Calendar capability.

### gmail_adapter.py

Defines the concrete adapter that fulfills email-provider contracts using Gmail capability.

### notion_adapter.py

Defines the concrete adapter that fulfills notes- or workspace-oriented provider contracts using Notion capability.

### google_drive_adapter.py

Defines the concrete adapter that fulfills cloud-storage provider contracts using Google Drive capability.

### office_docs_adapter.py

Defines the concrete adapter that fulfills document-editor provider contracts using office-document tooling.

---

# 8. iot_platforms

## Definition

The `iot_platforms/` submodule defines provider abstractions and concrete adapters for external IoT and home-automation ecosystems.

Its purpose is to support platform-level access to:

* general IoT backends
* home-automation systems
* smart lights
* smart plugs
* thermostats

This submodule is important because NORA may need to interact with external device ecosystems through protocol- or platform-specific gateways.

### Internal Structure

```text
iot_platforms/
├── providers/
└── adapters/
```

---

## iot_platforms/providers/

### iot_platform_provider.py

Defines the provider interface for general IoT platform capability.

### home_automation_provider.py

Defines the provider interface for home-automation capability.

Its purpose is to expose broader domestic or environmental control ecosystems through a stable contract.

### smart_light_provider.py

Defines the provider interface for smart-light capability.

### smart_plug_provider.py

Defines the provider interface for smart-plug capability.

### thermostat_provider.py

Defines the provider interface for thermostat capability.

---

## iot_platforms/adapters/

### mqtt_platform_adapter.py

Defines the concrete adapter that fulfills IoT-platform provider contracts using MQTT-backed capability.

### home_assistant_adapter.py

Defines the concrete adapter that fulfills home-automation provider contracts using Home Assistant capability.

### tuya_adapter.py

Defines the concrete adapter that fulfills relevant smart-device provider contracts using Tuya-backed capability.

### shelly_adapter.py

Defines the concrete adapter that fulfills relevant smart-device provider contracts using Shelly-backed capability.

---

# 9. semantic_embedding

## Definition

The `semantic_embeddings/` submodule defines provider abstractions and concrete adapters for embedding generation, result reranking, and vector indexing.

Its purpose is to support semantic retrieval infrastructure required by memory, retrieval, ranking, and relevance-aware reasoning flows.

This submodule is especially important because vector-based reasoning support is not one capability but a small family of related capabilities.

### Internal Structure

```text
semantic_embeddings/
├── providers/
└── adapters/
```

---

## semantic_embeddings/providers/

### embedding_provider.py

Defines the provider interface for generating semantic embeddings.

Its purpose is to abstract vector-generation technology from the rest of the architecture.

### reranking_provider.py

Defines the provider interface for reranking candidate retrieval results.

Its role is important where retrieval quality depends on secondary scoring beyond raw vector similarity.

### vector_index_provider.py

Defines the provider interface for vector indexing and vector-store operations.

Its purpose is to expose index-backed semantic retrieval capability through a stable internal contract.

---

## semantic_embeddings/adapters/

### sentence_transformers_embedding_adapter.py

Defines the concrete adapter that fulfills embedding-provider contracts using Sentence Transformers capability.

### openai_embedding_adapter.py

Defines the concrete adapter that fulfills embedding-provider contracts using OpenAI-backed embedding capability.

### faiss_vector_index_adapter.py

Defines the concrete adapter that fulfills vector-index provider contracts using FAISS-backed indexing capability.

---

## Cross-Submodule Architectural Relationships

The integrations and external services module is best understood as a capability-boundary architecture rather than as a flat collection of adapters.

### audio_and_language_engines -> perception and action

Speech-related providers support both perception-side audio interpretation and action-side voice output.

### linguistic_intelligence -> semantic and dialogue layers

Structured language-processing providers support semantic interpretation, summarization, translation, and related language reasoning paths.

### language_models -> planning and generation flows

LLM providers support planning, structured reasoning, explanation generation, and other higher-level generative tasks.

### vision_and_ocr -> perception and document analysis

Vision and OCR providers support visual perception, text extraction, and image-based interpretation pathways.

### search_and_internet -> planning and information retrieval

Internet-facing providers support fact retrieval, grounding, location-related tasks, and current-information access.

### multimedia_services -> action and media control

Multimedia providers support playback and media-access behaviors.

### productivity_services -> action, planning, and backend use cases

Productivity providers support scheduling, email, document operations, and storage-backed workflows.

### iot_platforms -> device-control execution paths

IoT providers support action-and-expression flows that interact with external controllable ecosystems.

### semantic_embeddings -> memory and retrieval

Embedding and vector-index providers support persistent memory, retrieval, reranking, and semantic search behavior.

These relationships show the internal logic clearly:

* providers define capability families
* adapters implement them concretely
* domain modules consume them through stable internal contracts

---

## What This Module Must Not Contain

To preserve architectural clarity, the integrations and external services module should not absorb responsibilities that belong elsewhere.

It should not contain:

* high-level domain planning logic
* session-management logic
* direct frontend rendering logic
* runtime FSM ownership
* dialogue continuity ownership
* long-term memory semantics ownership
* hardware-model ownership
* action-policy ownership

It may provide capabilities to all of those areas, but it must remain the external-service boundary rather than a hidden domain-logic layer.

---

## Interaction With Other Modules

The `integrations_and_external_services/` module interacts with nearly every major architectural domain.

### shared

Uses shared identifiers, exceptions, retry/backoff utilities, environment metadata, and generic provider-oriented abstractions.

### identity_access_security

May provide external identity-adjacent services such as biometric matching, remote auth helpers, or account-linked platform access under higher-level trust policies.

### interaction_interfaces

Provides backend capability support for interface-adjacent channels such as voice support, translation, or remote communication-related integration pathways.

### perception

n
Provides speech, vision, OCR, and related external inference capability consumed by perceptual pipelines.

### cognitive_core

May affect subsystem availability context when provider readiness or external capability health changes.

### dialogue_and_session

Provides summarization, translation, and language-related capabilities that can support continuity and compression workflows.

### planning_and_agents

Consumes LLMs, linguistic providers, search providers, productivity providers, and other external capability families as core planning resources.

### action_and_expression

Consumes TTS, multimedia, IoT, communication, and productivity integrations when executing outward effects.

### persistence_and_memory

Consumes embedding, reranking, vector-index, and sometimes cloud-storage capability as part of durable memory and artifact infrastructure.

### backend_and_application

Depends on provider readiness, integration health, and external capability access as part of application workflows and operational behavior.

### frontend_support

May surface integrated-capability state, provider-backed artifact descriptors, or external status information when needed for frontend views.

### infrastructure_and_hardware

May cooperate with hardware-facing modules where external platform control is mediated through both software and device infrastructure.

### observability

Requires logging, tracing, metrics, and failure visibility around external provider usage, latency, and degradation.

---

## Design Constraints of the Module

The `integrations_and_external_services/` module should obey several strict architectural constraints.

### 1. Providers and adapters must remain distinct

The system should depend on provider contracts, not directly on adapter implementations.

### 2. Capability families must remain clear

Audio, language, vision, internet, productivity, IoT, and embeddings should remain visibly separated.

### 3. External dependency substitution must be possible

The architecture should make it feasible to replace one provider implementation with another without destabilizing domain modules.

### 4. Adapter logic must remain capability-focused

n
Adapters should implement provider contracts, not absorb domain-level policy or orchestration behavior.

### 5. Vendor assumptions must remain bounded

The rest of NORA should not become semantically shaped around one vendor’s quirks when a provider contract can preserve cleaner internal semantics.

### 6. Availability and failure must be expected

n
External services can degrade, fail, rate-limit, or disappear.

The architecture should treat external dependency fragility as normal rather than exceptional.

### 7. Sensitive integrations must remain policy-controlled upstream

This module may expose capability, but higher-level trust and authorization decisions must remain outside it.

---

## Testing Implications

This module requires especially strong adapter and provider testing because failures here can silently degrade major system capabilities.

Important testing categories include:

* provider contract conformance tests
* adapter substitution tests
* provider-failure behavior tests
* degraded-capability tests
* environment-specific adapter selection tests
* speech-engine integration tests
* NLP and translation adapter tests
* LLM adapter and routing tests
* vision and OCR adapter tests
* search and weather adapter tests
* multimedia adapter tests
* productivity-service adapter tests
* IoT platform adapter tests
* embedding and vector-index adapter tests
* retry and timeout behavior tests
* latency and observability instrumentation tests

Failures here can make large parts of NORA appear unavailable, inaccurate, or inconsistent even if the internal architecture is sound.

---

## Why This Structure Fits NORA

This structure fits NORA because NORA is designed as a multimodal, extensible, tool-capable, integration-rich cognitive system.

It needs to interface with many external capability families while keeping the core architecture stable and modular.

The proposed structure allows NORA to:

* isolate third-party and engine dependence cleanly
* group external capabilities by function
* replace providers over time
* support both local and cloud-backed execution paths
* keep core modules focused on internal semantics rather than vendor specifics
* scale capability breadth without collapsing architectural clarity

That makes it an excellent fit for the system.

---

## Architectural Importance

The `integrations_and_external_services/` module provides the external capability architecture through which NORA can use specialized engines, online services, productivity platforms, media systems, IoT ecosystems, and semantic infrastructure without coupling its core logic directly to specific vendors or libraries.

While other modules define identity, interaction, perception, runtime cognition, dialogue continuity, planning, action, persistence, backend behavior, frontend support, and hardware structure, the live system still requires an explicit architecture that can expose replaceable external capabilities for speech, language, large-language-model reasoning, vision, OCR, internet retrieval, multimedia, productivity workflows, IoT platforms, and embedding-backed semantic retrieval.

Through this module the architecture gains:

* explicit provider contracts for external capability families
* concrete adapters for specific technologies and services
* cleaner substitution of engines and vendors over time
* reduced coupling between domain logic and third-party implementations
* stronger support for local, cloud, and hybrid capability strategies
* clearer operational boundaries around external dependency usage

By separating audio and language engines, linguistic intelligence, language models, vision and OCR, search and internet, multimedia services, productivity services, IoT platforms, and semantic embeddings into explicit internal subdomains, NORA preserves both capability breadth and architectural clarity.

For that reason, `integrations_and_external_services/` is one of the most important external-boundary modules of `src/nora/`.

## Architectural Structure

```text
integrations_and_external_services
│
├── Audio and Language Engines
│   ├── speech-to-text providers
│   ├── text-to-speech providers
│   ├── wake-word providers
│   ├── voice-activity-detection providers
│   ├── speaker-identification providers
│   ├── speaker-diarization providers
│   └── concrete speech/audio adapters
│
├── Linguistic Intelligence
│   ├── NLP-engine providers
│   ├── entity-recognition providers
│   ├── intent-classification providers
│   ├── summarization providers
│   ├── translation providers
│   └── concrete language-intelligence adapters
│
├── Language Models
│   ├── general LLM providers
│   ├── structured-output LLM providers
│   ├── reasoning LLM providers
│   ├── model-router providers
│   └── concrete LLM adapters
│
├── Vision and OCR
│   ├── vision-inference providers
│   ├── object-detection providers
│   ├── face-recognition providers
│   ├── gesture-recognition providers
│   ├── OCR providers
│   └── concrete vision and OCR adapters
│
├── Search and Internet
│   ├── web-search providers
│   ├── page-fetch providers
│   ├── news-search providers
│   ├── map-search providers
│   ├── weather providers
│   └── concrete internet adapters
│
├── Multimedia Services
│   ├── media-streaming providers
│   ├── audio-catalog providers
│   ├── video-catalog providers
│   ├── remote-speaker providers
│   └── concrete multimedia adapters
│
├── Productivity Services
│   ├── calendar providers
│   ├── email providers
│   ├── notes providers
│   ├── tasks providers
│   ├── cloud-storage providers
│   ├── document-editor providers
│   └── concrete productivity adapters
│
├── IoT Platforms
│   ├── IoT-platform providers
│   ├── home-automation providers
│   ├── smart-light providers
│   ├── smart-plug providers
│   ├── thermostat providers
│   └── concrete IoT adapters
│
└── Semantic Embeddings
    ├── embedding providers
    ├── reranking providers
    ├── vector-index providers
    └── concrete embedding and indexing adapters
```

```
integrations_and_external_services/
├── audio_and_language_engines/
│   ├── providers/
│   │   ├── speech_to_text_provider.py
│   │   ├── text_to_speech_provider.py
│   │   ├── wake_word_provider.py
│   │   ├── voice_activity_detection_provider.py
│   │   ├── speaker_identification_provider.py
│   │   └── speaker_diarization_provider.py
│   └── adapters/
│       ├── whisper_stt_adapter.py
│       ├── pyttsx_tts_adapter.py
│       └── porcupine_wake_word_adapter.py
│
├── linguistic_intelligence/
│   ├── providers/
│   │   ├── nlp_engine_provider.py
│   │   ├── entity_recognition_provider.py
│   │   ├── intent_classifier_provider.py
│   │   ├── summarization_provider.py
│   │   └── translation_provider.py
│   └── adapters/
│       ├── spacy_nlp_adapter.py
│       ├── transformers_ner_adapter.py
│       └── deepl_translation_adapter.py
│
├── language_models/
│   ├── providers/
│   │   ├── llm_provider.py
│   │   ├── structured_output_llm_provider.py
│   │   ├── reasoning_llm_provider.py
│   │   └── model_router_provider.py
│   └── adapters/
│       ├── openai_llm_adapter.py
│       ├── ollama_llm_adapter.py
│       ├── local_transformers_llm_adapter.py
│       └── llm_router_adapter.py
│
├── vision_and_ocr/
│   ├── providers/
│   │   ├── vision_inference_provider.py
│   │   ├── object_detection_provider.py
│   │   ├── face_recognition_provider.py
│   │   ├── gesture_recognition_provider.py
│   │   └── ocr_provider.py
│   └── adapters/
│       ├── opencv_vision_adapter.py
│       ├── mediapipe_gesture_adapter.py
│       ├── yolovision_adapter.py
│       └── tesseract_ocr_adapter.py
│
├── search_and_internet/
│   ├── providers/
│   │   ├── web_search_provider.py
│   │   ├── page_fetch_provider.py
│   │   ├── news_search_provider.py
│   │   ├── map_search_provider.py
│   │   └── weather_provider.py
│   └── adapters/
│       ├── serpapi_search_adapter.py
│       ├── requests_page_fetch_adapter.py
│       ├── maps_service_adapter.py
│       └── weather_api_adapter.py
│
├── multimedia_services/
│   ├── providers/
│   │   ├── media_streaming_provider.py
│   │   ├── audio_catalog_provider.py
│   │   ├── video_catalog_provider.py
│   │   └── remote_speaker_provider.py
│   └── adapters/
│       ├── spotify_adapter.py
│       ├── youtube_adapter.py
│       └── local_media_library_adapter.py
│
├── productivity_services/
│   ├── providers/
│   │   ├── calendar_provider.py
│   │   ├── email_provider.py
│   │   ├── notes_provider.py
│   │   ├── tasks_provider.py
│   │   ├── cloud_storage_provider.py
│   │   └── document_editor_provider.py
│   └── adapters/
│       ├── google_calendar_adapter.py
│       ├── gmail_adapter.py
│       ├── notion_adapter.py
│       ├── google_drive_adapter.py
│       └── office_docs_adapter.py
│
├── iot_platforms/
│   ├── providers/
│   │   ├── iot_platform_provider.py
│   │   ├── home_automation_provider.py
│   │   ├── smart_light_provider.py
│   │   ├── smart_plug_provider.py
│   │   └── thermostat_provider.py
│   └── adapters/
│       ├── mqtt_platform_adapter.py
│       ├── home_assistant_adapter.py
│       ├── tuya_adapter.py
│       └── shelly_adapter.py
│
└── semantic_embeddings/
    ├── providers/
    │   ├── embedding_provider.py
    │   ├── reranking_provider.py
    │   └── vector_index_provider.py
    └── adapters/
        ├── sentence_transformers_embedding_adapter.py
        ├── openai_embedding_adapter.py
        └── faiss_vector_index_adapter.py
```

# Infrastructure and Hardware Module

## Definition

The `infrastructure_and_hardware/` module defines the physical substrate, device topology, connectivity surfaces, and runtime hardware condition of NORA.

While other architectural modules define identity, interaction, perception, cognition, dialogue continuity, planning, action, persistence, backend behavior, frontend support, integrations, and observability, those modules all ultimately depend on a more fundamental layer:

the material and technical substrate through which the system actually exists and operates.

That is the role of `infrastructure_and_hardware/`.

In architectural terms, this module defines the embodied and technical substrate of NORA.

It is the module that represents:

* computation nodes
* hosts and edge runtimes
* sensors
* actuators
* buses and communication links
* controllable external devices
* current hardware operating condition

This module therefore defines:

* compute-node descriptors and workload targets
* sensor descriptors and calibration support
* actuator descriptors and stop behavior
* connectivity descriptors for network and hardware buses
* external device descriptors for smart or controllable equipment
* runtime hardware-state monitoring and fault detection

This module is not the same as perception.

Perception interprets signals coming from sensors.

Infrastructure and hardware define what sensors physically exist, how they are connected, and what hardware state they are in.

This module is also not the same as action and expression.

Action and expression decide how to produce outward effects.

Infrastructure and hardware define the physical devices and low-level technical substrate through which those effects become materially possible.

For that reason, `infrastructure_and_hardware/` is one of the foundational embodiment modules of NORA.

---

## Architectural Purpose

The purpose of the `infrastructure_and_hardware/` module is to make the material structure of NORA explicit, inspectable, and governable.

A system like NORA is not purely abstract software.

It may run across:

* host machines
* edge devices
* microphones
* cameras
* NFC readers
* environmental sensors
* displays
* speakers
* motors
* servos
* relays
* network links
* serial buses
* GPIO maps
* external smart devices

Without a dedicated infrastructure and hardware module, physical and technical substrate concerns tend to become fragmented across bootstrap code, action services, perception code, integration adapters, and deployment configuration.

That creates major architectural problems such as:

* unclear device inventory
* hidden hardware dependencies
* weak separation between domain logic and physical substrate
* poor runtime visibility into hardware availability
* fragile handling of buses, sensors, and actuator state
* difficulty modeling external devices separately from local actuators
* poor hardware-safety diagnosis
* weak support for heterogeneous or distributed deployment targets

By introducing a dedicated infrastructure and hardware module, NORA gains:

* explicit representation of physical and technical assets
* cleaner boundaries between hardware existence and hardware usage
* structured runtime tracking of hardware condition
* clearer modeling of compute topology and edge execution
* explicit connectivity and bus-level representation
* better support for hardware-aware diagnostics and safety
* stronger extensibility for additional devices and deployment targets

This module therefore provides the architectural body of NORA.

---

## Core Architectural Principle

The most important design principle of this module is the following:

Physical substrate must be separated into computation devices, sensors, actuators, connectivity, external controllable devices, and hardware runtime state.

These concerns are related, but they are not identical.

### Computation devices

Define where NORA or parts of NORA run.

### Sensors

n
Define what physical inputs exist.

### Actuators

Define what physical outputs or movements can be produced directly by NORA’s own hardware.

### Connectivity

Define the network links and hardware buses through which components communicate.

### External controllable devices

Define devices outside NORA’s own body that NORA may command.

### Hardware runtime state

Define how the physical substrate is currently behaving at runtime.

This separation matters because “hardware” is not one thing.

A camera, a motor, a Wi-Fi link, a Raspberry Pi, and a smart plug are all infrastructure-related, but they have very different architectural roles.

---

## Internal Module Structure

The proposed structure is the following:

```text
infrastructure_and_hardware/
├── computation_devices/
├── sensors/
├── actuators/
├── connectivity/
├── external_controllable_devices/
└── hardware_runtime_state/
```

This structure divides the material substrate into six major internal subdomains.

### computation_devices

Defines the machines and compute targets that host or execute NORA workloads.

### sensors

Defines physical sensing devices.

### actuators

Defines direct physical effectors.

### connectivity

Defines network links and low-level communication buses.

### external_controllable_devices

Defines external smart or controllable equipment addressed by NORA.

### hardware_runtime_state

Defines current operational state, faults, and condition snapshots of the hardware substrate.

This decomposition is essential because each of these areas has different lifecycle, safety, and operational semantics.

---

## Architectural Role Within the Full System

The `infrastructure_and_hardware/` module sits below perception, action, integrations, and backend operational monitoring.

It receives or models information about:

* physical devices present in the system
* execution hosts and edge nodes
* bus-level and network-level connectivity
* controllable external devices
* hardware health and fault state

It then provides the material substrate on which other modules rely.

This means it stands between:

* actual embodied and networked technical reality
  and
* the software modules that consume or operate over that reality

It is therefore not a behavior module.

It is the substrate-description and hardware-state module.

---

# 1. computation_devices

## Definition

The `computation_devices/` submodule defines the computing nodes, hosts, accelerators, and edge-runtime execution targets that make up the computational substrate of NORA.

Its purpose is to represent where workloads run, what kind of node each execution target is, and what compute capabilities are available.

This is important because NORA may not be a single-process, single-host system.

It may span local hosts, edge devices, or specialized accelerator-backed nodes.

### Internal Structure

```text
computation_devices/
├── models/
├── services/
└── repositories/
```

---

## computation_devices/models/

### compute_node_descriptor.py

Defines the structured representation of a compute node available to NORA.

This model may include:

* node identifier
* node type
* host role
* available compute resources
* location or deployment profile
* capability metadata

Its purpose is to make compute topology explicit.

### runtime_host_descriptor.py

Defines the structured representation of the main runtime host or a host-class execution environment.

Its role is to distinguish host-level characteristics from more abstract node identity.

### edge_node_status.py

Defines the structured runtime status of an edge node.

This may include availability, connectivity, workload readiness, thermal or power status, and execution health.

Its purpose is especially important in distributed or embodied deployments.

### accelerator_descriptor.py

Defines the structured representation of an accelerator resource associated with a compute node.

This may include GPU, TPU, NPU, or other specialized compute-capability metadata.

---

## computation_devices/services/

### register_compute_node_service.py

Defines the operation that registers a compute node in the hardware/infrastructure model.

Its purpose is to make node availability explicit and durable within the system description.

### update_compute_node_status_service.py

Defines the operation that updates the runtime status of a compute node.

Its role is important for distributed runtime awareness and workload decisions.

### resolve_workload_target_node_service.py

Defines the operation that determines which compute node should receive a given workload.

Its purpose is to map runtime or capability requirements onto available compute topology.

---

## computation_devices/repositories/

### compute_node_repository.py

Defines the persistence or registry boundary for compute-node descriptors and compute-node status data.

Its role is to isolate compute-topology storage from compute-related services.

---

# 2. sensors

## Definition

The `sensors/` submodule defines the physical sensors attached to or associated with NORA.

Its purpose is to represent what sensing devices exist, what their characteristics are, whether they are available, and how they should be calibrated.

This submodule is the physical inventory and state layer for sensing hardware.

### Internal Structure

```text
sensors/
├── models/
├── services/
└── repositories/
```

---

## sensors/models/

### microphone_descriptor.py

Defines the structured representation of a microphone sensor.

This may include channel count, sampling properties, mount position, device identifier, and readiness metadata.

### camera_descriptor.py

Defines the structured representation of a camera sensor.

Its role is to make camera identity, capability, and operational characteristics explicit.

### nfc_reader_descriptor.py

Defines the structured representation of an NFC-reading device.

Its purpose is to model short-range credential or proximity-reading hardware explicitly.

### proximity_sensor_descriptor.py

Defines the structured representation of a proximity sensor.

### light_sensor_descriptor.py

Defines the structured representation of an ambient-light sensor.

### temperature_sensor_descriptor.py

Defines the structured representation of a temperature sensor.

### humidity_sensor_descriptor.py

Defines the structured representation of a humidity sensor.

### tactile_sensor_descriptor.py

Defines the structured representation of a tactile or contact-oriented sensor.

### imu_descriptor.py

Defines the structured representation of an inertial measurement unit.

Its purpose is to model motion, orientation, or stabilization-relevant sensing hardware where applicable.

---

## sensors/services/

### register_sensor_service.py

Defines the operation that registers a sensor in the hardware model.

Its role is to maintain an explicit inventory of available sensing hardware.

### update_sensor_state_service.py

Defines the operation that updates current sensor state, readiness, or health metadata.

### check_sensor_availability_service.py

Defines the operation that checks whether a sensor is currently available for use.

Its purpose is to support runtime gating of perception and interaction paths.

### calibrate_sensor_service.py

Defines the operation that applies or coordinates calibration for a sensor.

Its role is important because physical sensors often require explicit calibration state.

---

## sensors/repositories/

### sensor_repository.py

Defines the persistence or registry boundary for sensor descriptors and sensor-state information.

Its purpose is to isolate physical sensor records from service behavior.

---

# 3. actuators

## Definition

The `actuators/` submodule defines the physical effectors directly associated with NORA’s own hardware body or immediate output substrate.

Its purpose is to represent what local physical output devices exist and what their current state is.

This may include:

* speakers
* displays
* LED controllers
* servos
* motors
* relays
* haptic actuators

This submodule is distinct from external controllable devices because actuators here are part of NORA’s own local hardware substrate.

### Internal Structure

```text
actuators/
├── models/
├── services/
└── repositories/
```

---

## actuators/models/

### speaker_descriptor.py

Defines the structured representation of a speaker or local audio-output actuator.

### display_descriptor.py

Defines the structured representation of a display actuator or display surface.

### led_controller_descriptor.py

Defines the structured representation of an LED-control actuator.

Its purpose is to model local light-based output hardware explicitly.

### servo_descriptor.py

Defines the structured representation of a servo actuator.

### motor_descriptor.py

Defines the structured representation of a motor actuator.

### relay_descriptor.py

Defines the structured representation of a relay-based actuator or controllable relay output.

### haptic_actuator_descriptor.py

Defines the structured representation of a haptic actuator.

Its role is to model tactile-output hardware explicitly.

---

## actuators/services/

### register_actuator_service.py

Defines the operation that registers an actuator in the infrastructure model.

### update_actuator_state_service.py

Defines the operation that updates current actuator state or readiness metadata.

### check_actuator_availability_service.py

Defines the operation that checks whether an actuator is available for use.

Its purpose is important for safe execution planning and runtime gating.

### stop_all_actuators_service.py

Defines the operation that stops or disables all relevant actuators in a coordinated way.

Its role is especially important for safety, shutdown, or emergency-stop behavior.

---

## actuators/repositories/

### actuator_repository.py

Defines the persistence or registry boundary for actuator descriptors and actuator-state information.

Its role is to isolate actuator inventory and actuator-state storage from actuator services.

---

# 4. connectivity

## Definition

The `connectivity/` submodule defines the network links, hardware buses, GPIO mappings, and broker connections through which hardware and distributed runtime components communicate.

Its purpose is to represent the communication substrate that connects compute nodes, peripherals, buses, and external control surfaces.

This submodule is important because NORA may depend on multiple kinds of connectivity simultaneously:

* Wi-Fi
* Bluetooth
* Ethernet
* serial links
* I2C
* SPI
* GPIO
* MQTT broker connections

### Internal Structure

```text
connectivity/
├── models/
├── services/
└── repositories/
```

---

## connectivity/models/

### wifi_link_descriptor.py

Defines the structured representation of a Wi-Fi connectivity link.

### bluetooth_link_descriptor.py

Defines the structured representation of a Bluetooth connectivity link.

### ethernet_link_descriptor.py

Defines the structured representation of an Ethernet connectivity link.

### serial_link_descriptor.py

Defines the structured representation of a serial communication link.

Its role is especially important for microcontroller and peripheral integration.

### i2c_bus_descriptor.py

Defines the structured representation of an I2C bus.

### spi_bus_descriptor.py

Defines the structured representation of an SPI bus.

### gpio_map_descriptor.py

Defines the structured representation of GPIO mapping and pin-assignment structure.

Its purpose is to make low-level digital I/O configuration explicit.

### mqtt_broker_connection_descriptor.py

Defines the structured representation of a connection to an MQTT broker.

Its role is important where device control or distributed messaging relies on MQTT infrastructure.

---

## connectivity/services/

### check_network_connectivity_service.py

Defines the operation that checks network connectivity and network-link availability.

### check_serial_link_service.py

Defines the operation that checks the health or availability of a serial communication link.

### check_i2c_bus_service.py

Defines the operation that checks the health or accessibility of an I2C bus.

### check_spi_bus_service.py

Defines the operation that checks the health or accessibility of an SPI bus.

### resolve_best_connectivity_path_service.py

Defines the operation that determines the most appropriate connectivity path under current conditions.

Its purpose is to support adaptive communication choices in heterogeneous hardware environments.

---

## connectivity/repositories/

### connectivity_repository.py

Defines the persistence or registry boundary for connectivity descriptors and connectivity-state information.

Its purpose is to isolate communication-substrate records from connectivity services.

---

# 5. external_controllable_devices

## Definition

The `external_controllable_devices/` submodule defines the smart or controllable devices that are not part of NORA’s own body, but that NORA may discover, describe, address, and command.

Its purpose is to represent external target devices as first-class infrastructure objects.

This may include:

* smart lights
* smart plugs
* smart TVs
* thermostats
* door locks
* robot vacuums
* printers

This submodule is distinct from local actuators because these devices exist outside NORA’s immediate physical embodiment.

### Internal Structure

```text
external_controllable_devices/
├── models/
├── services/
└── repositories/
```

---

## external_controllable_devices/models/

### controllable_device_descriptor.py

Defines the primary structured representation of an external controllable device.

This model may include:

* device identifier
* device type
* alias or human-facing name
* platform association
* connectivity metadata
* current availability state

### smart_light_descriptor.py

Defines the structured representation of an external smart light.

### smart_plug_descriptor.py

Defines the structured representation of an external smart plug.

### smart_tv_descriptor.py

Defines the structured representation of an external smart TV.

### thermostat_descriptor.py

Defines the structured representation of an external thermostat.

### door_lock_descriptor.py

Defines the structured representation of an external controllable door lock.

Its role is especially important because some external devices may be safety- or security-sensitive.

### robot_vacuum_descriptor.py

Defines the structured representation of an external robot vacuum.

### printer_descriptor.py

Defines the structured representation of an external printer.

---

## external_controllable_devices/services/

### register_external_device_service.py

Defines the operation that registers an external controllable device in the infrastructure model.

### update_external_device_state_service.py

Defines the operation that updates state information for an external controllable device.

### resolve_external_device_by_alias_service.py

Defines the operation that resolves a human-facing alias into a concrete external device target.

Its role is especially useful for device-control flows driven by natural language or simplified control surfaces.

### check_external_device_reachability_service.py

Defines the operation that checks whether an external device is currently reachable.

Its purpose is to support safe control behavior and availability awareness.

---

## external_controllable_devices/repositories/

### external_device_repository.py

Defines the persistence or registry boundary for external controllable device descriptors and state records.

Its role is to isolate device inventory and state storage from device-management services.

---

# 6. hardware_runtime_state

## Definition

The `hardware_runtime_state/` submodule defines how NORA represents and monitors the current operating condition of its hardware substrate.

Its purpose is to provide runtime visibility into the actual physical health and readiness of the system.

This may include:

* overall hardware operational state
* power condition
* thermal condition
* connectivity condition
* fault records

This submodule is especially important because hardware existence alone is not enough.

The system also needs to know whether that hardware is currently healthy and safe.

### Internal Structure

```text
hardware_runtime_state/
├── models/
├── services/
└── repositories/
```

---

## hardware_runtime_state/models/

### hardware_operational_state_snapshot.py

Defines the structured snapshot of overall hardware operational state.

This may aggregate multiple lower-level hardware condition indicators into one runtime-oriented state view.

### power_state_snapshot.py

Defines the structured snapshot of current power state.

This may include battery condition, supply state, low-power warnings, or power-source metadata.

### thermal_state_snapshot.py

Defines the structured snapshot of thermal state.

Its role is important because overheating conditions can directly affect safe operation.

### connectivity_state_snapshot.py

Defines the structured snapshot of runtime connectivity condition.

This may include network reachability, bus health, broker reachability, or degraded communication condition.

### hardware_fault_record.py

Defines the structured representation of a hardware fault or hardware anomaly observed at runtime.

Its purpose is to preserve fault state explicitly for diagnosis, alerting, and safety response.

---

## hardware_runtime_state/services/

### collect_hardware_runtime_state_service.py

Defines the operation that collects current hardware-state information into a coherent snapshot.

Its purpose is to provide active runtime visibility over the physical substrate.

### detect_hardware_fault_service.py

Defines the operation that identifies hardware faults from current state data.

Its role is to make fault detection an explicit runtime behavior.

### detect_overheat_condition_service.py

Defines the operation that detects overheat conditions from thermal data.

Its purpose is especially important for safe operation and protective response.

### detect_low_power_condition_service.py

Defines the operation that detects low-power or degraded power conditions.

### publish_hardware_state_update_service.py

Defines the operation that publishes hardware-state updates to the wider runtime for monitoring, safety control, or frontend visibility.

---

## hardware_runtime_state/repositories/

### hardware_runtime_state_repository.py

Defines the persistence or registry boundary for current and historical hardware runtime-state information.

Its role is to isolate runtime-state storage from state-collection and state-detection services.

---

## Cross-Submodule Architectural Relationships

The infrastructure and hardware module is best understood as a material-substrate architecture rather than as six isolated folders.

### computation_devices -> connectivity

Compute nodes depend on connectivity surfaces to communicate with each other, with peripherals, or with external systems.

### sensors -> perception

Sensor descriptors and sensor availability provide the physical basis for perception, but do not perform perception themselves.

### actuators -> action and expression

Actuator descriptors and availability provide the physical basis for execution channels, but do not perform execution logic themselves.

### external_controllable_devices -> iot and integrations

External controllable devices provide the infrastructure objects later addressed through device-control and IoT platform modules.

### hardware_runtime_state -> safety and execution gating

Runtime hardware state is essential for safe action, safe perception activation, and operational monitoring.

### connectivity -> distributed runtime and device reachability

Connectivity state influences whether compute nodes, buses, sensors, actuators, or external devices are actually reachable.

These relationships show the internal logic clearly:

* infrastructure describes what exists
* connectivity describes how it is linked
* runtime-state tracking describes whether it is healthy now

---

## What This Module Must Not Contain

To preserve architectural clarity, the infrastructure and hardware module should not absorb responsibilities that belong elsewhere.

It should not contain:

* perception interpretation logic
* movement-planning logic
* spoken-dialogue logic
* high-level action policy logic
* tool-selection logic
* backend transport logic
* long-term memory semantics
* frontend UI behavior

It may provide substrate information to all of those modules, but it must remain the material and hardware-structure layer.

---

## Interaction With Other Modules

The `infrastructure_and_hardware/` module interacts with many other architectural domains.

### shared

Uses shared identifiers, timestamps, operation models, exceptions, and generic support abstractions.

### identity_access_security

May provide device descriptors, linked-device context, and hardware-sensitive trust surfaces where relevant.

### interaction_interfaces

Provides the physical substrate for microphones, local screens, NFC readers, tactile sensors, and related interface hardware.

### perception

Provides the sensor inventory and runtime availability on which perception depends.

### cognitive_core

Provides subsystem and hardware-condition input used for runtime context and safety-aware state transitions.

### dialogue_and_session

Usually interacts indirectly, but active device or hardware context may still influence session continuity in embodied deployments.

### planning_and_agents

Provides feasibility-related substrate information, such as hardware availability or execution-capable target nodes.

### action_and_expression

Provides the local actuators, capture devices, and hardware state on which physical or multimodal action depends.

### persistence_and_memory

May store durable descriptors, runtime-state history, hardware faults, or infrastructure topology records.

### backend_and_application

Exposes hardware state, hardware control surfaces, and hardware diagnostics through backend interfaces and monitoring flows.

### frontend_support

Provides hardware and device information shaped into dashboards, status views, and monitoring payloads.

### integrations_and_external_services

Connects external platforms and IoT ecosystems to the actual device and connectivity substrate they ultimately address.

### observability

Provides hardware and infrastructure state, faults, and condition metrics to system observability flows.

---

## Design Constraints of the Module

The `infrastructure_and_hardware/` module should obey several strict architectural constraints.

### 1. Description and usage must remain distinct

This module describes the hardware substrate and its runtime condition. It should not become the place where all hardware-using logic is implemented.

### 2. Local actuators and external devices must remain distinct

NORA’s own body is not the same thing as third-party devices it can control.

### 3. Sensors and perception must remain distinct

A microphone descriptor is not speech recognition.

A camera descriptor is not gesture interpretation.

### 4. Connectivity must remain explicit

Network links, buses, and GPIO mappings should remain first-class parts of the infrastructure model rather than hidden inside provider code.

### 5. Runtime hardware condition must remain visible

The system should know not only what hardware exists but what condition it is currently in.

### 6. Safety-relevant conditions must be first-class

Thermal faults, power issues, and hardware faults should remain explicit and not be treated as incidental metadata.

### 7. Compute topology should be modeled when it matters

If workloads can move across hosts or edge nodes, that should be explicit in the infrastructure model.

---

## Testing Implications

This module requires especially strong substrate-oriented testing because failures here can distort the system’s assumptions about what hardware exists and whether it is safe or reachable.

Important testing categories include:

* compute-node registration tests
* compute-node status update tests
* workload-target resolution tests
* sensor registration tests
* sensor availability tests
* sensor calibration tests
* actuator registration tests
* actuator stop-all behavior tests
* connectivity-check tests
* bus-health check tests
* best-connectivity-path resolution tests
* external-device registration tests
* external-device alias-resolution tests
* external-device reachability tests
* hardware-state collection tests
* hardware-fault detection tests
* overheat detection tests
* low-power detection tests
* hardware-state publication tests

Failures here can lead to unsafe behavior, unavailable functionality, or misleading assumptions in higher-level modules.

---

## Why This Structure Fits NORA

This structure fits NORA because NORA is designed as a potentially embodied, multimodal, device-aware system rather than as a purely abstract software assistant.

It needs to model:

* compute hosts and edge nodes
* sensors
* actuators
* buses and communication paths
* external smart devices
* current hardware health and fault state

A flatter architecture would blur these physical distinctions and make it much harder to reason clearly about hardware availability, safety, and reachability.

The proposed structure allows NORA to:

* describe its physical and technical substrate explicitly
* separate local embodiment from external controllable ecosystems
* monitor runtime hardware condition cleanly
* support distributed or edge-aware deployment structures
* provide hardware-aware inputs to perception, action, planning, and monitoring

That makes it an excellent fit for the system.

---

## Architectural Importance

The `infrastructure_and_hardware/` module provides the material and technical substrate through which NORA becomes physically realizable as a system.

While other modules define interaction, perception, runtime cognition, dialogue continuity, planning, action, persistence, backend behavior, frontend support, integrations, and observability, the live system still requires an explicit architecture that can describe its computation devices, sensors, actuators, connectivity surfaces, external controllable devices, and current hardware operating condition.

Through this module the architecture gains:

* explicit modeling of computation hosts and edge nodes
* structured representation of sensors and actuators
* first-class representation of network links, buses, and GPIO connectivity
* distinct treatment of external controllable devices
* runtime visibility into power, thermal, connectivity, and fault conditions
* better support for safe, embodied, and distributed operation

By separating computation devices, sensors, actuators, connectivity, external controllable devices, and hardware runtime state into explicit internal subdomains, NORA preserves both embodiment realism and architectural clarity.

For that reason, `infrastructure_and_hardware/` is one of the foundational substrate modules of `src/nora/`.

## Architectural Structure

```text
infrastructure_and_hardware
│
├── Computation Devices
│   ├── compute node descriptors
│   ├── runtime host descriptors
│   ├── edge node status
│   ├── accelerator descriptors
│   ├── compute-node registration services
│   ├── compute-node status-update services
│   ├── workload-target resolution services
│   └── compute-node repository
│
├── Sensors
│   ├── microphone descriptors
│   ├── camera descriptors
│   ├── NFC reader descriptors
│   ├── proximity sensor descriptors
│   ├── light sensor descriptors
│   ├── temperature sensor descriptors
│   ├── humidity sensor descriptors
│   ├── tactile sensor descriptors
│   ├── IMU descriptors
│   ├── sensor-registration services
│   ├── sensor-state update services
│   ├── sensor-availability checks
│   ├── sensor-calibration services
│   └── sensor repository
│
├── Actuators
│   ├── speaker descriptors
│   ├── display descriptors
│   ├── LED controller descriptors
│   ├── servo descriptors
│   ├── motor descriptors
│   ├── relay descriptors
│   ├── haptic actuator descriptors
│   ├── actuator-registration services
│   ├── actuator-state update services
│   ├── actuator-availability checks
│   ├── stop-all-actuators services
│   └── actuator repository
│
├── Connectivity
│   ├── Wi-Fi link descriptors
│   ├── Bluetooth link descriptors
│   ├── Ethernet link descriptors
│   ├── serial link descriptors
│   ├── I2C bus descriptors
│   ├── SPI bus descriptors
│   ├── GPIO map descriptors
│   ├── MQTT broker connection descriptors
│   ├── connectivity-check services
│   ├── bus-health services
│   ├── connectivity-path resolution services
│   └── connectivity repository
│
├── External Controllable Devices
│   ├── controllable device descriptors
│   ├── smart-light descriptors
│   ├── smart-plug descriptors
│   ├── smart-TV descriptors
│   ├── thermostat descriptors
│   ├── door-lock descriptors
│   ├── robot-vacuum descriptors
│   ├── printer descriptors
│   ├── external-device registration services
│   ├── external-device state-update services
│   ├── alias-resolution services
│   ├── reachability-check services
│   └── external-device repository
│
└── Hardware Runtime State
    ├── hardware operational-state snapshots
    ├── power-state snapshots
    ├── thermal-state snapshots
    ├── connectivity-state snapshots
    ├── hardware fault records
    ├── state-collection services
    ├── fault-detection services
    ├── overheat-detection services
    ├── low-power detection services
    ├── hardware-state publication services
    └── hardware-runtime-state repository
```

```
infrastructure_and_hardware/
├── computation_devices/
│   ├── models/
│   │   ├── compute_node_descriptor.py
│   │   ├── runtime_host_descriptor.py
│   │   ├── edge_node_status.py
│   │   └── accelerator_descriptor.py
│   ├── services/
│   │   ├── register_compute_node_service.py
│   │   ├── update_compute_node_status_service.py
│   │   └── resolve_workload_target_node_service.py
│   └── repositories/
│       └── compute_node_repository.py
│
├── sensors/
│   ├── models/
│   │   ├── microphone_descriptor.py
│   │   ├── camera_descriptor.py
│   │   ├── nfc_reader_descriptor.py
│   │   ├── proximity_sensor_descriptor.py
│   │   ├── light_sensor_descriptor.py
│   │   ├── temperature_sensor_descriptor.py
│   │   ├── humidity_sensor_descriptor.py
│   │   ├── tactile_sensor_descriptor.py
│   │   └── imu_descriptor.py
│   ├── services/
│   │   ├── register_sensor_service.py
│   │   ├── update_sensor_state_service.py
│   │   ├── check_sensor_availability_service.py
│   │   └── calibrate_sensor_service.py
│   └── repositories/
│       └── sensor_repository.py
│
├── actuators/
│   ├── models/
│   │   ├── speaker_descriptor.py
│   │   ├── display_descriptor.py
│   │   ├── led_controller_descriptor.py
│   │   ├── servo_descriptor.py
│   │   ├── motor_descriptor.py
│   │   ├── relay_descriptor.py
│   │   └── haptic_actuator_descriptor.py
│   ├── services/
│   │   ├── register_actuator_service.py
│   │   ├── update_actuator_state_service.py
│   │   ├── check_actuator_availability_service.py
│   │   └── stop_all_actuators_service.py
│   └── repositories/
│       └── actuator_repository.py
│
├── connectivity/
│   ├── models/
│   │   ├── wifi_link_descriptor.py
│   │   ├── bluetooth_link_descriptor.py
│   │   ├── ethernet_link_descriptor.py
│   │   ├── serial_link_descriptor.py
│   │   ├── i2c_bus_descriptor.py
│   │   ├── spi_bus_descriptor.py
│   │   ├── gpio_map_descriptor.py
│   │   └── mqtt_broker_connection_descriptor.py
│   ├── services/
│   │   ├── check_network_connectivity_service.py
│   │   ├── check_serial_link_service.py
│   │   ├── check_i2c_bus_service.py
│   │   ├── check_spi_bus_service.py
│   │   └── resolve_best_connectivity_path_service.py
│   └── repositories/
│       └── connectivity_repository.py
│
├── external_controllable_devices/
│   ├── models/
│   │   ├── controllable_device_descriptor.py
│   │   ├── smart_light_descriptor.py
│   │   ├── smart_plug_descriptor.py
│   │   ├── smart_tv_descriptor.py
│   │   ├── thermostat_descriptor.py
│   │   ├── door_lock_descriptor.py
│   │   ├── robot_vacuum_descriptor.py
│   │   └── printer_descriptor.py
│   ├── services/
│   │   ├── register_external_device_service.py
│   │   ├── update_external_device_state_service.py
│   │   ├── resolve_external_device_by_alias_service.py
│   │   └── check_external_device_reachability_service.py
│   └── repositories/
│       └── external_device_repository.py
│
└── hardware_runtime_state/
    ├── models/
    │   ├── hardware_operational_state_snapshot.py
│   │   ├── power_state_snapshot.py
│   │   ├── thermal_state_snapshot.py
│   │   ├── connectivity_state_snapshot.py
│   │   └── hardware_fault_record.py
│   ├── services/
│   │   ├── collect_hardware_runtime_state_service.py
│   │   ├── detect_hardware_fault_service.py
│   │   ├── detect_overheat_condition_service.py
│   │   ├── detect_low_power_condition_service.py
│   │   └── publish_hardware_state_update_service.py
│   └── repositories/
│       └── hardware_runtime_state_repository.py
```

# Observability Module

## Definition

The `observability/` module defines the centralized instrumentation architecture through which NORA becomes inspectable, diagnosable, measurable, and operationally transparent.

While other architectural modules define identity, interaction, perception, runtime cognition, dialogue continuity, planning, action, persistence, backend behavior, frontend support, integrations, and hardware substrate, those modules still require a transversal capability that makes their behavior visible in a structured way.

That is the role of `observability/`.

In architectural terms, this module defines the cross-cutting telemetry and diagnostic visibility layer of NORA.

It is the module that allows the system to answer questions such as:

* what is the system doing right now
* what happened just before a failure
* which requests, events, or transitions were slow
* which subsystem is degraded
* what hardware state changed and when
* what security-relevant activity occurred
* how runtime health evolves over time
* what operators should see in system dashboards

This module therefore defines:

* structured logging
* domain-oriented log channels
* trace-context creation and propagation
* distributed trace export
* metrics collection and registration
* metrics exposure
* centralized dashboard-payload construction for system health, FSM state, hardware state, and security status

This module is not the same as the backend-local observability area.

The backend-local observability section inside `backend_and_application/` focuses on server-runtime instrumentation at the application-surface level.

The top-level `observability/` module centralizes system-wide instrumentation patterns, telemetry structures, cross-domain logging channels, shared tracing primitives, metric infrastructure, and dashboard-building logic.

This module is therefore broader, more transversal, and more architectural.

For that reason, `observability/` is one of the foundational cross-cutting modules of `src/nora/`.

---

## Architectural Purpose

The purpose of the `observability/` module is to ensure that NORA can be operated, debugged, monitored, and improved as a complex live system.

A system like NORA is inherently multi-domain and potentially distributed.

It includes:

* runtime state transitions
* perception pipelines
* external integrations
* dialogue continuity
* planning flows
* action execution
* hardware conditions
* security-sensitive behavior
* file and memory persistence
* realtime application boundaries

Without a centralized observability architecture, these behaviors would remain opaque or only partially visible.

That would create serious operational problems such as:

* failures that cannot be explained
* degraded subsystems that are hard to detect
* poor performance visibility
* missing correlation between requests and downstream events
* hidden hardware or security issues
* inconsistent telemetry conventions across modules
* dashboards built ad hoc from incompatible data sources

By introducing a centralized observability module, NORA gains:

* structured operational transparency
* shared telemetry conventions across modules
* correlated logging and tracing
* measurable runtime behavior
* operator-facing diagnostic payloads
* stronger debugging and incident analysis capability
* clearer health visibility across subsystems

This module therefore provides the diagnostic nervous system of NORA.

---

## Core Architectural Principle

The most important design principle of this module is the following:

Observability must be separated into logging, tracing, metrics, and dashboard-payload construction.

These concerns are closely related, but they are not interchangeable.

### Logging

Captures structured records of noteworthy system behavior.

### Tracing

Captures causal flow across requests, events, and internal execution paths.

### Metrics

Captures numerical measurements of system behavior over time.

### Dashboards

Capture operator-facing aggregated visibility structures derived from telemetry and runtime state.

This separation matters because a log line is not a trace span, a trace is not a metric, and a metric is not a dashboard payload.

A strong observability architecture keeps those telemetry forms distinct while allowing them to reinforce each other.

---

## Internal Module Structure

The proposed structure is the following:

```text
observability/
├── logging/
├── tracing/
├── metrics/
└── dashboards/
```

This structure divides centralized observability into four major internal subdomains.

### logging

Defines structured and domain-specific log channels.

### tracing

Defines trace context, propagation, and export behavior.

### metrics

Defines metric collection primitives, registration, and export.

### dashboards

Defines payload builders for operator-facing visibility surfaces.

This decomposition is essential because different forms of observability have different semantics, storage patterns, and consumption audiences.

---

## Architectural Role Within the Full System

The `observability/` module is a transversal architectural layer.

Unlike many domain modules, it does not exist mainly to represent one business area.

Instead, it exists to make the rest of the system visible.

It receives or consumes information from:

* backend request handling
* security events
* hardware condition updates
* finite-state-machine transitions
* planning operations
* application runtime behavior
* external integrations
* health and metric sources

It then emits or constructs:

* structured logs
* trace contexts and exported traces
* metrics and metric registries
* dashboard payloads for operators and monitoring surfaces

This means the module is not merely a support utility.

It is a first-class cross-cutting operational architecture.

---

# 1. logging

## Definition

The `logging/` submodule defines how NORA records structured log information across major technical and operational domains.

Its purpose is to provide log channels that are both machine-usable and domain-distinguishable.

Instead of one undifferentiated logging surface, this submodule defines explicit loggers for key operational areas.

### Internal Structure

```text
logging/
├── structured_logger.py
├── security_logger.py
├── hardware_logger.py
├── fsm_logger.py
└── planning_logger.py
```

---

### structured_logger.py

Defines the foundational structured logger used for general system logging.

Its purpose is to ensure that log output follows a machine-readable and schema-consistent structure rather than being only ad hoc plain text.

This logger may support fields such as:

* timestamp
* severity
* module name
* correlation identifier
* trace identifier
* event name
* structured metadata

Architecturally, this file provides the baseline logging convention for the rest of the system.

### security_logger.py

Defines the specialized logger for security-relevant events.

Its purpose is to separate security-observability signals from ordinary application logs.

This may include:

* authentication failures
* authorization denials
* suspicious activity
* security incidents
* rate-limit breaches
* privileged actions

Its role is especially important for auditability and incident analysis.

### hardware_logger.py

Defines the specialized logger for hardware and infrastructure-related behavior.

Its purpose is to capture logs relevant to sensors, actuators, buses, device availability, faults, and runtime hardware anomalies.

This logger is especially important in an embodied or hardware-aware deployment.

### fsm_logger.py

Defines the specialized logger for finite-state-machine behavior.

Its purpose is to capture state transitions, blocked transitions, guard failures, queue behavior, and runtime control-state changes.

Its role is especially valuable when diagnosing complex runtime-control issues.

### planning_logger.py

Defines the specialized logger for planning and deliberative behavior.

Its purpose is to capture planning context, clarification requirements, tool selection, fallback decisions, replanning events, and related reasoning-path information.

This logger is important because planning failures often look plausible externally while being structurally wrong internally.

---

# 2. tracing

## Definition

The `tracing/` submodule defines how NORA constructs, propagates, and exports trace information across execution paths.

Its purpose is to preserve causal visibility across requests, events, backend flows, domain transitions, external integrations, and downstream side effects.

This is especially important in a system where behavior may span many modules and where one user action may trigger multiple asynchronous or multi-step downstream flows.

### Internal Structure

```text
tracing/
├── trace_context.py
├── trace_context_factory.py
├── distributed_trace_propagator.py
└── trace_export_service.py
```

---

### trace_context.py

Defines the structured representation of trace context.

This may include:

* trace identifier
* parent span information
* correlation metadata
* source metadata
* propagation metadata

Its purpose is to make execution-flow context explicit and transportable.

### trace_context_factory.py

Defines the component responsible for creating trace contexts.

Its role is to ensure trace creation follows consistent rules rather than being improvised across modules.

This may include root-trace creation, child-trace derivation, or event-linked trace generation.

### distributed_trace_propagator.py

Defines the component responsible for propagating trace context across module boundaries, event flows, or network boundaries.

Its purpose is to preserve causal continuity even when work moves across transports or subsystems.

This is especially important for event-driven and distributed execution paths.

### trace_export_service.py

Defines the service responsible for exporting trace information to an external trace sink or observability backend.

Its role is to make trace data operationally usable outside in-memory runtime scope.

---

# 3. metrics

## Definition

The `metrics/` submodule defines how NORA collects, registers, organizes, and exports quantitative measurements about system behavior.

Its purpose is to provide a structured metric infrastructure that supports performance monitoring, health visibility, trend analysis, and operational alerting.

Metrics differ from logs and traces because they provide compact numerical signals suitable for aggregation over time.

### Internal Structure

```text
metrics/
├── metric_counter_service.py
├── metric_gauge_service.py
├── metric_histogram_service.py
├── runtime_metric_registry.py
└── prometheus_export_service.py
```

---

### metric_counter_service.py

Defines the service responsible for counter-style metrics.

Its purpose is to record cumulative quantities such as counts of requests, events, errors, or transitions.

### metric_gauge_service.py

Defines the service responsible for gauge-style metrics.

Its role is to represent values that rise and fall over time, such as current connection count, active sessions, queue depth, or subsystem readiness level.

### metric_histogram_service.py

Defines the service responsible for histogram-style metrics.

Its purpose is to record distributions of measured values such as latency, duration, or payload sizes.

### runtime_metric_registry.py

Defines the registry of metrics known to the runtime observability system.

Its purpose is to centralize metric definitions, labels, and registration rather than scattering them across modules.

### prometheus_export_service.py

Defines the service responsible for exposing metrics in a Prometheus-compatible form.

Its role is especially important for standard operational monitoring infrastructure.

---

# 4. dashboards

## Definition

The `dashboards/` submodule defines how telemetry and runtime state are transformed into operator-facing dashboard payloads.

Its purpose is not to render frontend dashboards directly, but to construct backend-side payloads or aggregate state structures suitable for dashboard consumption.

This submodule is important because dashboards should not have to reconstruct complex system-state views from raw logs, metrics, and scattered domain queries on their own.

### Internal Structure

```text
dashboards/
├── build_system_health_dashboard_payload.py
├── build_fsm_dashboard_payload.py
├── build_hardware_dashboard_payload.py
└── build_security_dashboard_payload.py
```

---

### build_system_health_dashboard_payload.py

Defines the builder that constructs a dashboard payload representing overall system health.

Its purpose is to aggregate readiness, liveness, dependency condition, subsystem status, and other global health signals into one operator-consumable payload.

### build_fsm_dashboard_payload.py

Defines the builder that constructs a dashboard payload representing finite-state-machine status.

This may include current state, recent transitions, blocked transitions, transition rates, and related runtime-control visibility.

### build_hardware_dashboard_payload.py

Defines the builder that constructs a dashboard payload representing hardware and infrastructure state.

Its role is especially important for embodied deployments where operators need visibility into sensors, actuators, connectivity, thermal conditions, and hardware faults.

### build_security_dashboard_payload.py

Defines the builder that constructs a dashboard payload representing security-relevant operational state.

This may include recent incidents, security-event counts, suspicious-activity visibility, and trust-boundary status summaries.

---

## Cross-Submodule Architectural Relationships

The observability module is best understood as an instrumentation architecture rather than as four isolated folders.

### logging -> tracing

Logs often become much more valuable when tied to trace and correlation context.

### tracing -> metrics

Trace-derived timing or flow information may inform quantitative measurements and latency visibility.

### metrics -> dashboards

Metrics frequently become key inputs to operator-facing dashboard payloads.

### logging -> dashboards

Structured logs can contribute event summaries or recent-warning visibility for dashboards.

### tracing -> dashboards

Trace visibility may support incident diagnosis and drill-down from dashboard state.

These relationships show the overall logic clearly:

* logs record events
* traces record flow
* metrics record measured behavior
* dashboards aggregate visible operator state

---

## What This Module Must Not Contain

To preserve architectural clarity, the observability module should not absorb responsibilities that belong elsewhere.

It should not contain:

* domain business rules
* planner logic
* dialogue continuity logic
* transport-router logic
* hardware-control logic
* frontend rendering code
* memory retrieval logic
* external vendor-specific domain decisions

It may instrument all of those areas, but it must remain the visibility layer, not the behavior-owning layer.

---

## Interaction With Other Modules

The `observability/` module interacts with nearly every major architectural domain.

### shared

Uses shared identifiers, trace identifiers, correlation identifiers, timestamps, and common support abstractions.

### identity_access_security

Captures security-relevant logging, traces, and dashboard visibility related to authentication, authorization, incidents, and suspicious activity.

### interaction_interfaces

May instrument interface-origin events, origin-channel behavior, interruption signals, and user-input paths.

### perception

May instrument perception pipelines, confidence signals, inference durations, and perceptual event visibility.

### cognitive_core

Captures FSM transitions, runtime state changes, control-queue behavior, and modulation-relevant telemetry.

### dialogue_and_session

Captures session lifecycle events, recovery behavior, summarization operations, and continuity-related diagnostics.

### planning_and_agents

Captures semantic interpretation timing, planning behavior, clarification rates, tool-selection paths, and agent-delegation visibility.

### action_and_expression

Captures execution traces, device-control behavior, communication delivery outcomes, and multimodal-output diagnostics.

### persistence_and_memory

Captures storage-related telemetry, retrieval latency, artifact access, and technical-history signals where needed.

### backend_and_application

Works alongside backend-local observability to provide generalized logging, tracing, metrics infrastructure, and dashboard payload logic.

### frontend_support

Supplies operator-facing payload structures for dashboards and monitoring interfaces.

### integrations_and_external_services

Captures provider latency, error rates, degraded external dependency behavior, and integration health visibility.

### infrastructure_and_hardware

Captures hardware condition, connectivity state, fault records, and thermal or power visibility for operations and diagnosis.

---

## Design Constraints of the Module

The `observability/` module should obey several strict architectural constraints.

### 1. Logging, tracing, metrics, and dashboards must remain distinct

The system should not collapse all observability into one vague telemetry mechanism.

### 2. Instrumentation must remain structured

Logs, traces, and metrics should follow explicit conventions rather than ad hoc output habits.

### 3. Correlation must be first-class

Observability should preserve the ability to connect events, requests, actions, and failures across boundaries.

### 4. Dashboards must be built from intentional visibility models

Operator-facing visibility should come from explicit builders, not accidental leakage of raw backend structures.

### 5. Observability must remain transversal, not domain-owning

This module should instrument other modules, not absorb their logic.

### 6. Safety- and security-relevant telemetry should remain explicit

Hardware faults, incidents, and trust-boundary events should be clearly instrumented and not hidden inside general logs only.

### 7. Export paths should remain replaceable

Trace and metric export mechanisms should be structured so infrastructure choices can evolve over time.

---

## Testing Implications

This module requires especially strong instrumentation-focused testing because bad observability can make every other module harder to operate even when those modules are functioning correctly.

Important testing categories include:

* structured-log shape tests
* security-log routing tests
* hardware-log coverage tests
* FSM-log transition tests
* planning-log event tests
* trace-context creation tests
* trace-propagation tests
* trace-export tests
* counter, gauge, and histogram metric tests
* metric-registry consistency tests
* Prometheus export tests
* system-health dashboard payload tests
* FSM dashboard payload tests
* hardware dashboard payload tests
* security dashboard payload tests
* cross-correlation tests between logs, traces, and metrics

Failures here can leave NORA effectively blind during incidents, degradation, or performance problems.

---

## Why This Structure Fits NORA

This structure fits NORA because NORA is a complex, multi-domain, potentially distributed, hardware-aware, tool-using system that cannot be operated safely or effectively without strong telemetry.

It needs to provide visibility into:

* backend requests
* FSM behavior
* planning decisions
* hardware state
* security incidents
* external-provider health
* system-wide performance

A flatter or purely backend-local instrumentation model would not be enough for a system of this complexity.

The proposed structure allows NORA to:

* centralize telemetry conventions
* instrument multiple domains coherently
* support both machine-facing and operator-facing observability
* build dashboards from structured visibility models
* diagnose failures and performance regressions more effectively

That makes it an excellent fit for the system.

---

## Architectural Importance

The `observability/` module provides the centralized visibility architecture through which NORA can be monitored, diagnosed, measured, and operated as a complex live system.

While other modules define identity, interaction, perception, runtime cognition, dialogue continuity, planning, action, persistence, backend behavior, frontend support, integrations, and hardware substrate, the live system still requires an explicit architecture that can record structured logs, preserve trace context across flows, collect quantitative metrics, and construct operator-facing dashboard payloads for system health, runtime control, hardware condition, and security visibility.

Through this module the architecture gains:

* centralized structured logging
* explicit trace-context creation and propagation
* reusable metric collection and export infrastructure
* backend-side dashboard payload construction for operators
* stronger diagnostic visibility across runtime flows
* clearer instrumentation of hardware, security, FSM, and planning behavior
* improved operational transparency and incident response capability

By separating logging, tracing, metrics, and dashboard-payload construction into explicit internal subdomains, NORA preserves both observability power and architectural clarity.

For that reason, `observability/` is one of the most important transversal modules of `src/nora/`.

## Architectural Structure

```text
observability
│
├── Logging
│   ├── structured logging
│   ├── security logging
│   ├── hardware logging
│   ├── FSM logging
│   └── planning logging
│
├── Tracing
│   ├── trace contexts
│   ├── trace-context factories
│   ├── distributed trace propagation
│   └── trace export
│
├── Metrics
│   ├── counters
│   ├── gauges
│   ├── histograms
│   ├── runtime metric registry
│   └── Prometheus export
│
└── Dashboards
    ├── system health dashboard payloads
    ├── FSM dashboard payloads
    ├── hardware dashboard payloads
    └── security dashboard payloads
```

```
observability/
├── logging/
│   ├── structured_logger.py
│   ├── security_logger.py
│   ├── hardware_logger.py
│   ├── fsm_logger.py
│   └── planning_logger.py
│
├── tracing/
│   ├── trace_context.py
│   ├── trace_context_factory.py
│   ├── distributed_trace_propagator.py
│   └── trace_export_service.py
│
├── metrics/
│   ├── metric_counter_service.py
│   ├── metric_gauge_service.py
│   ├── metric_histogram_service.py
│   ├── runtime_metric_registry.py
│   └── prometheus_export_service.py
│
└── dashboards/
    ├── build_system_health_dashboard_payload.py
    ├── build_fsm_dashboard_payload.py
    ├── build_hardware_dashboard_payload.py
    └── build_security_dashboard_payload.py
```

# Testing Directories

## Definition

The `tests/` directory defines the verification architecture of NORA.

While the source tree defines what the system is supposed to do, the testing tree defines how those expectations are verified, protected, and continuously validated across levels of abstraction.

In architectural terms, the testing directories are not a secondary appendix to the project.

They define the quality-assurance structure through which the behavior, safety, correctness, performance, compatibility, and runtime reliability of NORA are checked.

The `tests/` tree therefore exists to answer questions such as:

* does each module behave correctly in isolation
* do multiple modules work together correctly
* do interfaces preserve stable contracts
* do complete user workflows succeed end to end
* does the system remain performant under realistic load
* does the software behave correctly when connected to real hardware
* can test environments be reproduced consistently

This testing architecture therefore defines:

* isolated unit verification
* cross-module integration verification
* contract verification for interfaces and providers
* end-to-end behavioral verification
* performance and scalability verification
* hardware-in-the-loop validation
* reusable fixtures and factories
* common test bootstrap logic

This testing structure is not the same as observability.

Observability makes the running system visible.

The testing tree defines how the system is intentionally exercised and verified under controlled conditions.

It is also not the same as backend diagnostics.

Diagnostics help explain runtime problems.

Tests help prevent them and detect regressions before deployment.

For that reason, the `tests/` tree is part of the architecture of reliability, not just project hygiene.

---

## Architectural Purpose

The purpose of the `tests/` directory is to ensure that NORA can evolve without losing correctness, safety, continuity, or operational stability.

A system like NORA is architecturally broad and behaviorally complex.

It includes:

* trust and access control
* multimodal interaction entry
* perception pipelines
* runtime cognition
* dialogue continuity
* planning and agent routing
* action execution
* persistence and memory
* backend APIs and realtime flows
* external integrations
* hardware-aware behavior

Without a structured testing architecture, such a system becomes fragile very quickly.

That would create major problems such as:

* regressions hidden inside large refactors
* accidental interface breakage
* weak confidence in deployment changes
* unsafe hardware behavior reaching runtime
* poor reproducibility of bug fixes
* inability to validate performance or scaling behavior
* no clear distinction between isolated failures and systemic failures

By introducing an explicit testing directory architecture, NORA gains:

* layered verification at multiple scopes
* clearer ownership of different categories of correctness
* reusable test data and test setup
* safer iteration on domain modules and infrastructure
* explicit validation of contracts and performance
* more reliable deployment and maintenance workflows

This directory tree therefore provides the structural foundation for trust in the codebase itself.

---

## Core Architectural Principle

The most important design principle of the testing tree is the following:

Tests must be separated by verification scope.

This means different types of quality checks should not be mixed into one flat test directory.

### Unit tests

Verify isolated behavior of one module, class, function, or bounded service.

### Integration tests

Verify cooperation between multiple components or systems.

### Contract tests

Verify that interfaces preserve agreed shape and behavior.

### End-to-end tests

Verify complete user or operator workflows through realistic execution paths.

### Performance tests

Verify throughput, latency, and scaling behavior.

### Hardware-in-the-loop tests

Verify behavior against real hardware or hardware-like execution paths.

### Shared support directories

Provide reusable fixtures, object factories, and bootstrap support for the rest of the test architecture.

This separation is essential because not every failure means the same thing.

A failing unit test, a failing contract test, and a failing end-to-end test each indicate a different class of architectural problem.

---

## Global Test Structure

The proposed structure is the following:

```text
tests/
├── unit/
├── integration/
├── contract/
├── e2e/
├── performance/
├── hardware_in_loop/
├── fixtures/
├── factories/
└── test_bootstrap/
```

This structure divides verification into major architectural layers.

### unit

Defines isolated verification of internal modules.

### integration

Defines tests where multiple subsystems cooperate.

### contract

Defines compatibility guarantees at explicit boundaries.

### e2e

Defines complete workflow verification.

### performance

Defines non-functional performance validation.

### hardware_in_loop

Defines validation against real or near-real hardware conditions.

### fixtures

Defines reusable prepared test resources.

### factories

Defines reusable test-object builders.

### test_bootstrap

Defines common test initialization and environment preparation.

This decomposition is essential because large systems require layered trust, not just many test files.

---

## Architectural Role Within the Full Project

The `tests/` tree is a transversal verification layer across the entire project.

It does not belong to one source module only.

Instead, it overlays the whole architecture and verifies it from multiple perspectives.

It interacts conceptually with:

* every domain module in `src/nora/`
* frontend-facing backend representation layers
* persistence and memory behavior
* external integrations
* runtime application boundaries
* hardware-aware flows

This means the testing architecture is not only about code coverage.

It is about preserving architectural integrity across change.

---

# 1. unit/

## Definition

The `unit/` directory defines isolated tests for individual modules and their internal bounded behaviors.

Its purpose is to verify the smallest meaningful units of logic without depending on broad system integration.

Unit tests should run quickly, fail locally, and make regressions easy to identify.

### Internal Structure

```text
unit/
├── identity_access_security/
├── interaction_interfaces/
├── perception/
├── cognitive_core/
├── dialogue_and_session/
├── planning_and_agents/
├── action_and_expression/
├── persistence_and_memory/
├── backend_and_application/
├── integrations_and_external_services/
└── infrastructure_and_hardware/
```

This structure mirrors the main source architecture so that verification responsibility remains aligned with module ownership.

---

## unit/identity_access_security/

Defines isolated tests for identity representation, authentication logic, authorization decisions, profile behavior, and security services.

These tests may verify:

* identity lifecycle services
* permission resolution
* access-denial behavior
* suspicious-activity detection rules
* profile preference resolution

Its role is to validate trust logic independently from transport or persistence-heavy flows.

## unit/interaction_interfaces/

Defines isolated tests for channel normalization, control-signal mapping, handler-level interface behavior, and interface-origin metadata preservation.

These tests may verify voice, screen, web, touch, gesture, NFC, and remote interaction adaptation logic.

## unit/perception/

Defines isolated tests for preprocessing, feature extraction, interpretation stages, confidence handling, fusion logic, and perception-event normalization.

Its purpose is to validate perceptual logic without requiring full live hardware or broad orchestration.

## unit/cognitive_core/

Defines isolated tests for finite-state-machine logic, transition guards, operational context updates, modulation logic, and short-term cognitive memory behavior.

Its role is especially important because the cognitive core coordinates runtime behavior broadly.

## unit/dialogue_and_session/

Defines isolated tests for session lifecycle, project lifecycle, history append and retrieval, summarization logic, and recovery-state construction.

## unit/planning_and_agents/

Defines isolated tests for semantic interpretation, intent detection, planning logic, tool selection, agent routing, and execution preparation.

These tests are especially important because plausible outputs can still hide broken internal reasoning structure.

## unit/action_and_expression/

Defines isolated tests for spoken-response building, visual-payload composition, movement-safety validation, capture-request handling, IoT command construction, and outbound communication preparation.

## unit/persistence_and_memory/

Defines isolated tests for repository logic, mappers, memory-entry services, vector retrieval support, artifact-path generation, and technical-history writing behavior.

## unit/backend_and_application/

Defines isolated tests for request model validation, router helpers, application use cases, event-dispatch normalization, coordinator logic, and backend-local instrumentation behavior.

## unit/integrations_and_external_services/

Defines isolated tests for provider contracts, adapter behavior, routing logic between provider abstractions and adapters, and failure-handling around external dependencies.

## unit/infrastructure_and_hardware/

Defines isolated tests for device descriptors, availability checks, calibration logic, connectivity checks, hardware fault detection, and runtime state collection.

---

# 2. integration/

## Definition

The `integration/` directory defines tests that verify cooperation between multiple internal components, external services, or infrastructure layers.

Its purpose is to confirm that components which work individually also work together correctly across real boundaries.

These tests are broader than unit tests and usually involve more realistic system wiring.

### Internal Structure

```text
integration/
├── api/
├── websocket/
├── database/
├── vector_store/
├── integrations/
└── hardware_adapters/
```

---

## integration/api/

Defines tests for backend API routes together with their use cases, dependencies, serializers, and domain integration.

These tests may verify:

* route-to-use-case behavior
* auth boundary enforcement
* response-model correctness
* error handling across layers

Its purpose is to validate the request-response stack as a cooperating system.

## integration/websocket/

Defines tests for realtime connection management, subscription handling, and broadcast distribution across connected clients.

These tests verify that live state distribution behaves correctly across actual backend wiring.

## integration/database/

Defines tests for transactional repositories, unit-of-work behavior, mappers, and persistence consistency against a real or realistic database environment.

Its role is to validate structured persistence beyond mocked repository behavior.

## integration/vector_store/

Defines tests for embedding-backed retrieval and vector-index interaction across actual memory and vector components.

Its purpose is to verify that semantic memory retrieval works across real integration points, not just in isolated ranking logic.

## integration/integrations/

Defines tests for real or sandboxed interaction with external-service adapters and provider layers.

These tests may validate external API behavior, adapter conformance, timeout handling, and provider selection under realistic conditions.

## integration/hardware_adapters/

Defines tests for software integration with hardware-facing adapters or device-communication layers.

Its role is to validate that software components can communicate correctly with hardware-side interfaces without yet requiring full end-to-end embodied operation.

---

# 3. contract/

## Definition

The `contract/` directory defines tests that verify the stability and correctness of explicit interface contracts.

Its purpose is to ensure that boundaries which other components depend on remain consistent in structure, semantics, and compatibility.

Contract tests are especially important where multiple clients, modules, or replaceable providers rely on an agreed shape.

### Internal Structure

```text
contract/
├── api_contracts/
├── websocket_contracts/
└── provider_contracts/
```

---

## contract/api_contracts/

Defines tests that verify HTTP API request and response contract stability.

These tests may validate:

* field presence and naming
* error-shape consistency
* backward compatibility expectations
* schema conformance

Its purpose is to protect API consumers from accidental boundary breakage.

## contract/websocket_contracts/

Defines tests that verify realtime payload and subscription contract stability.

These tests are especially important because realtime consumers are often sensitive to payload drift or event-type inconsistency.

## contract/provider_contracts/

Defines tests that verify provider abstractions and adapter implementations conform to expected capability contracts.

Its role is crucial in an architecture built around provider-adapter separation, because adapter substitution is only safe if contracts are actually enforced.

---

# 4. e2e/

## Definition

The `e2e/` directory defines end-to-end tests that exercise complete workflows across realistic system boundaries.

Its purpose is to validate that the system behaves correctly from the perspective of a real user, operator, or external client performing a complete scenario.

These tests are broader and slower than unit or integration tests, but they are essential for validating total architectural behavior.

### Internal Structure

```text
e2e/
├── user_dialogue_flows/
├── project_continuation_flows/
├── hardware_control_flows/
├── admin_monitoring_flows/
└── recovery_flows/
```

---

## e2e/user_dialogue_flows/

Defines end-to-end tests for complete conversational user flows.

These tests may include:

* user message entry
* semantic interpretation
* planning
* response generation
* dialogue history update
* session continuity effects

Its purpose is to validate the end-to-end conversational path.

## e2e/project_continuation_flows/

Defines end-to-end tests for workflows where a user continues, pauses, resumes, or completes a project across sessions.

Its role is important because long-horizon continuity is one of NORA’s defining architectural features.

## e2e/hardware_control_flows/

Defines end-to-end tests for workflows that involve hardware control, device interaction, or embodied action paths.

Its purpose is to validate the complete route from command ingress to safe execution and visible result.

## e2e/admin_monitoring_flows/

Defines end-to-end tests for administrative and monitoring workflows.

These tests may include diagnostics retrieval, incident visibility, state dashboards, configuration updates, and privileged controls.

## e2e/recovery_flows/

Defines end-to-end tests for recovery scenarios.

These may include interrupted sessions, resumed projects, reconstructed dialogue state, and restart-continuity behavior.

Its role is especially important because recovery is a system-level property, not just a local service behavior.

---

# 5. performance/

## Definition

The `performance/` directory defines non-functional tests focused on latency, throughput, scaling, and resource-behavior characteristics.

Its purpose is to verify that NORA remains operationally viable under realistic or stressed workloads.

Performance tests are not primarily about correctness of results.

They are about correctness of runtime behavior under load.

### Internal Structure

```text
performance/
├── api_latency/
├── websocket_scaling/
├── fsm_throughput/
├── memory_retrieval_latency/
└── perception_pipeline_latency/
```

---

## performance/api_latency/

Defines tests that measure or assert latency characteristics of backend API operations.

Its purpose is to detect regressions in request-response performance.

## performance/websocket_scaling/

Defines tests that evaluate how realtime infrastructure behaves as connection count, subscription count, or update frequency increases.

Its role is to validate operational scalability of live communication surfaces.

## performance/fsm_throughput/

Defines tests that measure how efficiently the finite-state-machine layer processes events and transitions under load.

This is important because control bottlenecks here can affect the entire live system.

## performance/memory_retrieval_latency/

Defines tests that measure retrieval speed in persistent-memory and vector-store flows.

Its purpose is to ensure that semantic memory remains operationally usable at runtime.

## performance/perception_pipeline_latency/

Defines tests that measure latency across perception pipelines or perception-stage execution.

Its role is important because perception delay can degrade interaction quality and responsiveness.

---

# 6. hardware_in_loop/

## Definition

The `hardware_in_loop/` directory defines tests that execute against real hardware or near-real hardware-integrated setups rather than purely simulated software boundaries.

Its purpose is to validate that embodied and device-connected behavior works correctly when actual physical interfaces are involved.

These tests are especially important in systems where software correctness is not enough without physical correctness.

### Internal Structure

```text
hardware_in_loop/
├── arduino_integration/
├── esp_integration/
├── raspberry_pi_integration/
└── sensor_actuator_integration/
```

---

## hardware_in_loop/arduino_integration/

Defines tests that validate interaction with Arduino-based hardware components.

Its purpose is to confirm correct communication, state handling, and control behavior in real integrated setups.

## hardware_in_loop/esp_integration/

Defines tests that validate interaction with ESP-family hardware components such as ESP32 or ESP8266-based environments.

Its role is to verify device communication and control paths under realistic embedded conditions.

## hardware_in_loop/raspberry_pi_integration/

Defines tests that validate interaction with Raspberry Pi-based runtime or peripheral-control environments.

Its purpose is especially important when edge execution or GPIO-related behavior is part of deployment.

## hardware_in_loop/sensor_actuator_integration/

Defines tests that validate integrated behavior across real sensors and actuators.

This may include sensing, actuation, calibration, movement safety, and signal capture across actual hardware pathways.

---

# 7. fixtures/

## Definition

The `fixtures/` directory defines reusable prepared test resources shared across multiple test suites.

Its purpose is to reduce duplication and make test environments more reproducible.

Fixtures may include:

* seeded user data
* session snapshots
* project examples
* sample dialogue histories
* fake provider outputs
* serialized payload samples
* temporary file resources
* mock hardware-state snapshots

Architecturally, fixtures provide stable reusable test context.

They should represent prepared state, not hidden business logic.

---

# 8. factories/

## Definition

The `factories/` directory defines reusable builders that construct test-domain objects, DTOs, records, requests, or runtime structures on demand.

Its purpose is to create flexible and readable test setup while avoiding manual object construction everywhere.

Factories are especially useful when tests need many variants of:

* identities
* sessions
* projects
* dialogue turns
* planning results
* execution instructions
* hardware-state snapshots
* provider results

Architecturally, factories improve test maintainability and clarity by making object construction explicit and reusable.

---

# 9. test_bootstrap/

## Definition

The `test_bootstrap/` directory defines shared test-environment initialization and common low-level setup used across the testing architecture.

Its purpose is to establish:

* common test configuration
* environment-variable loading for tests
* shared test app initialization
* database setup or teardown hooks
* mock provider registration
* common dependency overrides
* global safety guards for tests

This directory is especially important because a large system like NORA needs test runs to begin from controlled and reproducible initial conditions.

Architecturally, `test_bootstrap/` should centralize environment preparation, not hide test behavior.

---

## Cross-Directory Architectural Relationships

The testing architecture is best understood as a layered verification system rather than as a set of unrelated test folders.

### unit -> fast local correctness

Unit tests verify isolated logic and usually fail closest to the source of the bug.

### integration -> cooperation correctness

Integration tests verify that modules and systems work together once boundaries are crossed.

### contract -> interface stability

Contract tests protect shared boundaries from drift.

### e2e -> user-visible behavioral correctness

End-to-end tests verify complete scenarios the way users or operators experience them.

### performance -> non-functional operational correctness

Performance tests ensure the system remains usable under realistic load.

### hardware_in_loop -> embodied correctness

Hardware-in-the-loop tests verify that software correctness survives contact with real physical systems.

### fixtures, factories, and test_bootstrap -> support infrastructure

These shared directories make the other test layers maintainable, reproducible, and scalable.

Together, they create a progression from isolated confidence to systemic confidence.

---

## What This Testing Tree Must Not Become

To preserve architectural clarity, the `tests/` tree should not become a dumping ground.

It should not contain:

* undocumented random scripts with no clear scope
* mixed unit and e2e behavior in the same file
* hidden environment assumptions
* production logic copied into tests
* unstable fixtures that encode accidental behavior
* integration tests disguised as unit tests
* performance tests that depend on non-reproducible setup without declaring it

The structure should preserve scope clarity so that test failures remain meaningful.

---

## Interaction With The Rest of the Architecture

The `tests/` tree conceptually interacts with the whole source architecture.

### src/nora domain modules

Each major domain should have isolated and cross-layer verification coverage.

### backend surfaces

APIs, realtime channels, event dispatch, and admin operations must be tested at appropriate scopes.

### persistence and memory

Database, vector store, and artifact flows need both correctness and latency verification.

### integrations

Provider contracts and adapter behavior require both contract and integration verification.

### infrastructure and hardware

Hardware-aware behavior requires both simulation-level and hardware-in-the-loop validation.

### observability

Telemetry and dashboard payloads should also be verifiable so that operators can trust what they see.

---

## Design Constraints Of The Testing Architecture

The testing directories should obey several strict architectural constraints.

### 1. Scope must remain explicit

Every test should belong clearly to one verification level.

### 2. Module alignment should remain visible

At least the unit-test tree should continue mirroring the source architecture so ownership stays clear.

### 3. Shared setup should remain centralized

Fixtures, factories, and bootstrap code should reduce duplication without hiding important test assumptions.

### 4. Hardware-aware testing should remain separated from pure software testing

Real hardware dependencies should be visible and isolated.

### 5. Performance testing should remain intentionally non-functional

Performance directories should not become random integration tests with timing assertions added as an afterthought.

### 6. Contract stability should be treated as first-class

APIs, realtime payloads, and provider contracts all deserve explicit compatibility verification.

### 7. End-to-end tests should represent meaningful user or operator journeys

They should validate complete flows, not just duplicate lower-level tests.

---

## Testing Importance

The testing architecture is architecturally important because it protects the rest of the architecture from silent decay.

NORA is a system with many interacting domains, external dependencies, realtime behavior, persistence layers, and potentially physical hardware.

In such a system, correctness cannot be guaranteed by informal inspection alone.

The layered testing tree gives the project:

* confidence in isolated module behavior
* confidence in boundary stability
* confidence in integrated workflows
* confidence in performance characteristics
* confidence in embodied behavior with real devices
* confidence that future changes will not quietly break fundamental assumptions

For that reason, the `tests/` directory is not ancillary.

It is part of the architectural machinery that keeps NORA reliable over time.

## Architectural Structure

```text
tests
│
├── Unit
│   ├── identity, trust, and security tests
│   ├── interaction-interface tests
│   ├── perception tests
│   ├── cognitive-core tests
│   ├── dialogue and session tests
│   ├── planning and agent tests
│   ├── action and expression tests
│   ├── persistence and memory tests
│   ├── backend and application tests
│   ├── integration-provider abstraction tests
│   └── infrastructure and hardware tests
│
├── Integration
│   ├── API integration tests
│   ├── realtime websocket integration tests
│   ├── database integration tests
│   ├── vector-store integration tests
│   ├── external-integration tests
│   └── hardware-adapter integration tests
│
├── Contract
│   ├── API contract tests
│   ├── websocket contract tests
│   └── provider contract tests
│
├── End to End
│   ├── user dialogue flows
│   ├── project continuation flows
│   ├── hardware control flows
│   ├── admin and monitoring flows
│   └── recovery flows
│
├── Performance
│   ├── API latency tests
│   ├── websocket scaling tests
│   ├── FSM throughput tests
│   ├── memory retrieval latency tests
│   └── perception pipeline latency tests
│
├── Hardware in Loop
│   ├── Arduino integration tests
│   ├── ESP integration tests
│   ├── Raspberry Pi integration tests
│   └── sensor and actuator integration tests
│
├── Fixtures
│   └── reusable prepared test resources
│
├── Factories
│   └── reusable test object builders
│
└── Test Bootstrap
    └── shared test-environment initialization
```

```
tests/
├── unit/
│   ├── identity_access_security/
│   ├── interaction_interfaces/
│   ├── perception/
│   ├── cognitive_core/
│   ├── dialogue_and_session/
│   ├── planning_and_agents/
│   ├── action_and_expression/
│   ├── persistence_and_memory/
│   ├── backend_and_application/
│   ├── integrations_and_external_services/
│   └── infrastructure_and_hardware/
│
├── integration/
│   ├── api/
│   ├── websocket/
│   ├── database/
│   ├── vector_store/
│   ├── integrations/
│   └── hardware_adapters/
│
├── contract/
│   ├── api_contracts/
│   ├── websocket_contracts/
│   └── provider_contracts/
│
├── e2e/
│   ├── user_dialogue_flows/
│   ├── project_continuation_flows/
│   ├── hardware_control_flows/
│   ├── admin_monitoring_flows/
│   └── recovery_flows/
│
├── performance/
│   ├── api_latency/
│   ├── websocket_scaling/
│   ├── fsm_throughput/
│   ├── memory_retrieval_latency/
│   └── perception_pipeline_latency/
│
├── hardware_in_loop/
│   ├── arduino_integration/
│   ├── esp_integration/
│   ├── raspberry_pi_integration/
│   └── sensor_actuator_integration/
│
├── fixtures/
├── factories/
└── test_bootstrap/
```


# Naming and File Conventions

## Definition

The naming system of NORA is not a cosmetic preference.

It is part of the architecture.

In a project of this size, file names are one of the main mechanisms by which structure remains visible, responsibilities remain bounded, and future refactoring remains possible without confusion.

When the codebase grows across many modules, submodules, services, providers, adapters, repositories, policies, handlers, and test layers, naming stops being a minor style issue and becomes an architectural control mechanism.

For that reason, naming conventions should be treated as part of the global software architecture and not merely as incidental coding style.

---

## Architectural Purpose

The purpose of a strict naming system is to make responsibility legible.

A good file name should answer, as directly as possible, at least one of these questions:

* what kind of thing is this
* what role does it play
* what architectural layer does it belong to
* what object does it operate on
* what action does it perform
* what boundary does it define

In a large system like NORA, naming conventions must help with:

* fast navigation of the repository
* reducing ambiguity
* preserving architectural boundaries
* making refactors safer
* avoiding god files and junk drawers
* helping new contributors infer structure quickly
* improving grepability and searchability
* keeping file purpose aligned with module design

The rule is simple:

A person should be able to infer the approximate architectural role of a file before opening it.

That is the real objective of naming.

---

## Core Architectural Principle

The most important naming principle for NORA is this:

File names should reflect architectural role first, implementation detail second.

That means names should not be chosen because they are short, vague, or casually convenient.

They should be chosen because they communicate:

* the object represented
* the transformation performed
* the contract exposed
* the policy enforced
* the boundary implemented
* the type of artifact contained in the file

This is especially important in NORA because the project is intentionally decomposed into many small files with narrow responsibilities.

If names are weak, that decomposition becomes noise.

If names are strong, that decomposition becomes clarity.

---

## General Naming Philosophy

The naming system should follow these global rules.

### 1. One file, one architectural role

A file should usually contain one clearly identifiable thing.

If a file contains multiple unrelated responsibilities, the problem is usually not naming. The problem is that the file should be split.

### 2. Names should be explicit, not clever

Prefer clear descriptive names over short names, playful names, or internally understood abbreviations.

### 3. Suffixes should communicate role

Suffixes such as `_service.py`, `_repository.py`, or `_provider.py` are not decoration.

They are signals that communicate how the file fits into the architecture.

### 4. Prefixes should communicate action when relevant

Where the file represents an operation, the leading verb should explain what the file does.

### 5. Direct object names should be used for pure data structures

Where the file represents a domain object, the file should normally be named after the object directly.

### 6. Avoid generic containers

Generic names hide architectural intent and gradually become dumping grounds.

---

## Recommended File Naming Rules

Below is the detailed naming system that best fits the architecture already defined for NORA.

---

## 1. Enums

### Rule

Use:

`*_enum.py`

### Purpose

This makes it immediately clear that the file defines a constrained symbolic value set rather than a model, service, or policy.

### Examples

* `operational_state_enum.py`
* `intent_family_enum.py`
* `session_status_enum.py`
* `threat_level_enum.py`

### Why this works

Enum files usually represent classification systems, lifecycle states, categories, or modes.

The `_enum.py` suffix makes those files easy to detect in the tree and easy to separate from ordinary models.

### Recommended practice

Use singular names that describe the conceptual enum, not the collection of values.

Good:

* `language_enum.py`
* `role_enum.py`

Avoid:

* `languages.py`
* `roles.py`

Because those names can easily be mistaken for repositories, lists, or utility files.

---

## 2. Models

### Rule

Use the direct name of the object:

`object_name.py`

### Purpose

A model file should represent the thing itself, not the fact that it is a model.

### Examples

* `dialogue_turn.py`
* `user_profile.py`
* `planning_result.py`
* `hardware_fault_record.py`
* `voice_profile.py`

### Why this works

If the file exists inside a `models/` directory, then the role is already clear from the directory context.

Adding `_model.py` inside `models/` is often redundant and visually noisy.

### Recommended practice

Use the actual domain object name in singular form.

Good:

* `dialogue_session.py`
* `access_decision.py`
* `project_goal.py`

Avoid:

* `dialogue_session_model.py`
* `project_goal_model.py`

unless the directory is not already communicating that the file contains models.

---

## 3. Services

### Rule

Use:

`verb + object + _service.py`

### Purpose

Service files represent operations.

Their names should communicate the action they perform and the object or concept they operate on.

### Examples

* `create_session_service.py`
* `resolve_voice_profile_service.py`
* `detect_missing_parameters_service.py`
* `publish_hardware_state_update_service.py`
* `retrieve_relevant_memory_service.py`

### Why this works

This style makes service roles readable at a glance.

It distinguishes them from models, repositories, and policies.

### Recommended practice

Use a verb that describes the operation as specifically as possible.

Prefer:

* `create_`
* `update_`
* `resolve_`
* `build_`
* `detect_`
* `retrieve_`
* `publish_`
* `validate_`
* `synthesize_`

Avoid vague verbs such as:

* `handle_` when the file is not actually a handler
* `process_` when the specific operation can be named more precisely
* `manage_` when a more exact verb exists

Good:

* `validate_movement_safety_service.py`
* `build_planning_context_service.py`

Weak:

* `process_movement_service.py`
* `manage_planning_service.py`

---

## 4. Use Cases

### Rule

Use:

`verb + target + _use_case.py`

### Purpose

Use-case files represent application-level operations, not generic services.

They should be named around what the application is trying to achieve.

### Examples

* `login_use_case.py`
* `create_project_use_case.py`
* `recover_dialogue_context_use_case.py`
* `execute_hardware_command_use_case.py`
* `update_runtime_configuration_use_case.py`

### Why this works

The `_use_case.py` suffix clearly marks application-layer orchestration or operation entry points.

This prevents confusion with lower-level domain services.

### Recommended practice

Use names that reflect user-visible or application-visible operations.

Good:

* `suspend_session_use_case.py`
* `get_runtime_diagnostics_use_case.py`

Avoid names that are too implementation-specific for the application layer.

Weak:

* `validate_token_use_case.py` if it is really a lower-level authentication service

---

## 5. Repositories

### Rule

Use:

`*_repository.py`

### Purpose

Repository files define storage-facing access boundaries.

The suffix should be explicit and uniform.

### Examples

* `session_repository.py`
* `memory_entry_repository.py`
* `role_repository.py`
* `hardware_runtime_state_repository.py`
* `sql_project_repository.py`

### Why this works

Repository naming is one of the easiest places to preserve architectural clarity.

A repository should never look like a service, a mapper, or a model.

### Recommended practice

Use the stored thing or storage specialization in the file name.

Good:

* `file_artifact_repository.py`
* `sql_user_repository.py`

Avoid:

* `storage.py`
* `project_store.py` if the project consistently uses repository terminology elsewhere

---

## 6. Adapters

### Rule

Use:

`*_adapter.py`

### Purpose

Adapter files connect internal capability contracts to concrete external technologies or implementations.

The adapter suffix should be preserved rigorously.

### Examples

* `openai_llm_adapter.py`
* `google_calendar_adapter.py`
* `faiss_vector_index_adapter.py`
* `porcupine_wake_word_adapter.py`
* `tesseract_ocr_adapter.py`

### Why this works

Adapters are one of the most important boundary patterns in the architecture.

Naming them clearly helps keep provider contracts and vendor-specific implementations separate.

### Recommended practice

Make the concrete technology visible in the name.

Good:

* `whisper_stt_adapter.py`
* `home_assistant_adapter.py`

Avoid generic names such as:

* `speech_adapter.py`
* `calendar_adapter.py`

unless there is only one implementation and no realistic ambiguity.

---

## 7. Providers

### Rule

Use:

`*_provider.py`

### Purpose

Provider files define capability contracts or provider-facing abstractions.

### Examples

* `llm_provider.py`
* `embedding_provider.py`
* `text_to_speech_provider.py`
* `calendar_provider.py`
* `ocr_provider.py`

### Why this works

The `_provider.py` suffix marks capability boundaries clearly.

It distinguishes interface-like capability definitions from concrete adapters.

### Recommended practice

Name the provider after the capability, not after a vendor.

Good:

* `weather_provider.py`
* `speech_to_text_provider.py`

Avoid:

* `openai_provider.py` if the file is actually a contract and not the concrete adapter

---

## 8. Policies

### Rule

Use:

`*_policy.py`

### Purpose

Policy files define rules, constraints, or evaluation logic that represent governable decision criteria.

### Examples

* `planning_safety_policy.py`
* `role_permission_policy.py`
* `least_privilege_policy.py`
* `planning_feasibility_policy.py`

### Why this works

Policy is a specific architectural role.

The naming should make it obvious that the file is not simply an arbitrary helper or service, but a rule-governing component.

### Recommended practice

Use the name of the rule domain, not a vague adjective.

Good:

* `hardware_safety_authorization_policy.py`

Weak:

* `safe_policy.py`
* `smart_policy.py`

---

## 9. Handlers

### Rule

Use one of these patterns:

* `handle_* .py`
* `*_handler.py`

The preferred choice depends on whether the project wants handlers named primarily by action or by object.

### Purpose

Handlers represent bounded entry-response behavior, usually tied to one event, one ingress case, or one direct trigger.

### Examples

* `handle_spoken_confirmation.py`
* `handle_remote_admin_command.py`
* `handle_touch_cancel_signal.py`
* `wake_phrase_handler.py`
* `api_exception_handler.py`

### Why this works

Handlers are usually tied to a clearly scoped trigger.

Their names should expose that trigger as directly as possible.

### Recommended practice

For event-like or trigger-like files, prefer `handle_*`.

Good:

* `handle_stop_gesture.py`
* `handle_web_command_submission.py`

For more general technical boundary handlers, `*_handler.py` can also work well.

Good:

* `validation_exception_handler.py`
* `api_exception_handler.py`

### Recommendation for consistency

Choose one main convention per subdomain where possible.

For example:

* interaction handlers -> `handle_*`
* technical exception handlers -> `*_handler.py`

That keeps the naming system internally coherent.

---

## 10. Builders

### Rule

Use one of these patterns:

* `build_* .py`
* `*_builder.py`

### Purpose

Builder files exist to construct structured objects, payloads, descriptors, prompts, or view models.

### Examples

* `build_spoken_response_service.py`
* `build_hardware_dashboard_payload.py`
* `conversation_view_model_builder.py`
* `schedule_proposal_builder_service.py`
* `build_artifact_download_descriptor_service.py`

### Why this works

Some builder roles are operational services and belong naturally in service naming.

Others are dedicated builder components and deserve explicit builder naming.

### Recommended practice

Use `build_*` when the file is fundamentally an operation.

Use `*_builder.py` when the file’s identity is primarily that it is a reusable builder object or builder component.

Good distinctions:

* `build_state_indicator_service.py` -> service operation
* `conversation_view_model_builder.py` -> dedicated builder component

---

## Extended Recommended Patterns

Because NORA is large, it helps to extend the naming logic consistently to other file roles too.

### Registries

Use:

`*_registry.py`

Examples:

* `state_registry.py`
* `transition_registry.py`
* `event_route_registry.py`

### Mappers

Use:

`*_mapper.py`

Examples:

* `user_record_mapper.py`
* `message_record_mapper.py`

### Presenters

Use:

`*_presenter.py`

Examples:

* `session_presenter.py`
* `hardware_state_presenter.py`

### Serializers

Use:

`*_serializer.py`

Examples:

* `realtime_payload_serializer.py`
* `artifact_descriptor_serializer.py`

### Dispatchers

Use:

`*_dispatcher.py`

Examples:

* `system_event_dispatcher.py`

### Coordinators

Use:

`*_coordinator.py`

Examples:

* `planning_to_action_coordinator.py`
* `session_project_coordinator.py`

### Orchestrators

Use:

`*_orchestrator.py`

Only when the file genuinely owns a broader multi-step orchestration role distinct from a narrower coordinator.

### Factories

Use:

`*_factory.py`

Examples:

* `trace_context_factory.py`

### Descriptors

Use the direct descriptor name:

* `camera_descriptor.py`
* `compute_node_descriptor.py`

### Requests and Results

Use the direct name:

* `scheduling_agent_request.py`
* `planning_result.py`
* `movement_execution_result.py`

This keeps data structures explicit and searchable.

---

## Naming Rules By Semantic Role

A practical summary looks like this.

### For things that represent data

Use the name of the thing.

Examples:

* `dialogue_turn.py`
* `project_context.py`
* `access_request.py`

### For things that perform actions

Use verb + object + suffix when relevant.

Examples:

* `retrieve_relevant_memory_service.py`
* `send_email_service.py`
* `recover_project_context_service.py`

### For things that define a contract

Use the capability name + `_provider.py` or a similarly explicit contract suffix.

Examples:

* `translation_provider.py`
* `event_publisher_protocol.py`

### For things that implement a concrete external technology

Use technology name + role + `_adapter.py`.

Examples:

* `openai_llm_adapter.py`
* `spotify_adapter.py`

### For things that define rules

Use the rule domain + `_policy.py`.

Examples:

* `planning_context_adaptation_policy.py`

### For things that expose one boundary-triggered reaction

Use `handle_*` or `*_handler.py`.

### For things that shape payloads or complex objects

Use `build_*` or `*_builder.py` depending on whether the file is an operation or a dedicated construction component.

---

## What Should Be Avoided

This part is critical.

Certain names should be avoided almost completely in a project like NORA because they destroy architectural legibility.

### Avoid

* `utils.py`
* `helpers.py`
* `services.py`
* `models.py`
* `common.py`
* `manager.py`

unless the scope is extremely narrow, explicit, and genuinely justified.

---

## Why These Names Are Dangerous

### utils.py

This usually becomes a trash can for unrelated functions.

It hides responsibility instead of clarifying it.

### helpers.py

This is usually even worse, because “helper” says almost nothing about architectural role.

### services.py

In a project built around many services, a file called `services.py` communicates no useful distinction at all.

It usually becomes a container for unrelated operations that should have been split.

### models.py

In a project with many domain models, this almost always becomes a bag of unrelated structures.

It destroys navigability.

### common.py

This tends to become a pseudo-global dumping ground whose real meaning is “things I didn’t know where to put.”

### manager.py

This is one of the most dangerous names in large codebases.

“Manager” often hides unclear ownership and inflated responsibility.

A file named `manager.py` frequently signals one of these problems:

* the object has too many responsibilities
* the architecture has not been decomposed enough
* the actual role has not been named precisely yet

---

## When Generic Names Might Be Acceptable

Sometimes one of these names can be tolerated, but only under strict conditions.

### Acceptable only if all of the following are true

* the scope is genuinely tiny
* the directory context already narrows meaning heavily
* the contents are tightly coherent
* a more precise name would be artificial rather than helpful

Examples of cases that might be acceptable:

* `text_normalizer.py` instead of `utils.py`
* `datetime_formatter.py` instead of `helpers.py`
* `request_trace_dependency.py` instead of `common.py`

In practice, precise naming almost always wins.

---

## Architectural Smells Revealed By Bad Names

Weak file names usually signal deeper architectural issues.

If you feel tempted to create one of these files:

* `manager.py`
* `helpers.py`
* `utils.py`
* `misc.py`
* `common.py`

it is often a sign that one of these is true:

* the file has too many responsibilities
* the architectural role is still unclear
* you are hiding cross-cutting behavior in the wrong place
* the directory structure is not being used properly
* you are about to create a dumping ground

In other words, naming problems are often architecture problems in disguise.

---

## Naming Consistency Rules

The following consistency rules are strongly recommended across the whole project.

### 1. Use lowercase snake_case everywhere for file names

This keeps naming uniform across Python code.

### 2. Use singular nouns for object files

Prefer:

* `dialogue_turn.py`
* `project_goal.py`

not:

* `dialogue_turns.py`
* `project_goals.py`

unless the file truly defines a collection abstraction.

### 3. Keep suffixes semantically stable

Do not use `_service.py` for one kind of thing in one module and a totally different kind of thing in another.

### 4. Keep verbs operationally meaningful

If the file is action-oriented, the verb should communicate a real operation.

### 5. Avoid abbreviations unless they are project-wide and unambiguous

Examples that may be acceptable if standardized:

* `fsm`
* `ocr`
* `llm`

But random abbreviations should be avoided.

### 6. Prefer longer clear names over shorter vague names

A long explicit name is usually easier to maintain than a short ambiguous one.

---

## Recommended Decision Rule For Naming A New File

Before creating a file, answer these questions.

### 1. What is this file architecturally

Is it a model, service, provider, adapter, policy, handler, builder, repository, registry, presenter, serializer, or something else.

### 2. Is it representing a thing or performing an action

If it represents a thing, name the thing.

If it performs an action, name the operation.

### 3. What object or concept does it act on

Use that as the core noun.

### 4. What suffix makes its role obvious

Apply the appropriate architectural suffix.

### 5. Would someone understand its role without opening it

If not, the name is still too weak.

---

## Practical Examples Of Good Naming Transformations

Weak names and better alternatives:

* `utils.py` -> `datetime_parser.py`, `slug_builder.py`, `safe_json_loader.py`
* `helpers.py` -> `build_clarification_prompt_service.py`
* `manager.py` -> `websocket_connection_manager.py` only if it really manages connection lifecycle explicitly; otherwise choose something narrower
* `services.py` -> split into `create_project_service.py`, `archive_project_service.py`, `continue_project_service.py`
* `models.py` -> split into `dialogue_turn.py`, `turn_metadata.py`, `turn_content.py`
* `common.py` -> `request_trace_dependency.py`, `audit_metadata.py`, or other precise file depending on the real role

This is exactly the kind of discipline that keeps a very decomposed architecture from collapsing back into ambiguity.

---

## Architectural Importance

The naming system is architecturally important because it preserves the legibility of the entire codebase.

In a project as large and intentionally decomposed as NORA, the file tree is one of the primary interfaces through which developers understand the system.

If names are precise, the tree itself teaches the architecture.

If names are vague, the tree becomes noise and every navigation step requires opening files just to discover their purpose.

A strong naming system gives NORA:

* clearer architectural boundaries
* better navigability
* easier refactoring
* lower risk of dumping-ground files
* more readable module decomposition
* better onboarding for future contributors
* stronger alignment between file structure and conceptual design

For that reason, naming conventions should be treated as a formal part of the software architecture and not as optional style preferences.

## Naming Summary

```text
Enums        -> *_enum.py
Models       -> direct object name
Services     -> verb + object + _service.py
Use cases    -> verb + target + _use_case.py
Repositories -> *_repository.py
Adapters     -> *_adapter.py
Providers    -> *_provider.py
Policies     -> *_policy.py
Handlers     -> handle_* or *_handler.py
Builders     -> build_* or *_builder.py
Registries   -> *_registry.py
Mappers      -> *_mapper.py
Presenters   -> *_presenter.py
Serializers  -> *_serializer.py
Factories    -> *_factory.py
Dispatchers  -> *_dispatcher.py
Coordinators -> *_coordinator.py
```
