# 01 - System Architecture: NORA

This document describes the logical and physical architecture of the NORA system, detailing the modular structure of hardware and software components and how they interact.

---

## 1. Overview

NORA is built using a layered, modular architecture where each component (hardware or software) operates semi-independently and communicates through well-defined interfaces. This promotes reusability, extensibility, and clarity.

---

## 2. Architecture Layers

### a. Physical Layer (Hardware)

* Sensors: PIR, temperature, tilt, microphone, NFC, etc.
* Actuators: RGB LED, display, servos/motors.
* Processing Unit: Raspberry Pi 4 (8 GB RAM)
* Optional: future custom PCB with STM32 or similar for signal handling.

### b. Driver Layer

* GPIO control and low-level communication (I2C, UART, SPI)
* Specific driver modules for each device: `adc.py`, `pwm.py`, `gpio_led.py`, etc.

### c. Agent Layer

* Perception agents: presence, voice, gesture.
* Behavior agents: FSM-based or rule-based logic.
* Decision agents: respond to goals, sensor input and triggers.
* Interface agents: manage external communication (GUI, voice).

### d. Control Layer

* Central event dispatcher
* FSM controller (`fsm_controller.py`)
* Task scheduler (cooperative model)

### e. Interface Layer

* GUI (React frontend)
* Audio interface (microphone + speaker)
* External connectors (mobile app, REST API planned)

---

## 3. Software Modules

| Module      | Responsibility                                   |
| ----------- | ------------------------------------------------ |
| `backend/`  | FSM logic, control loop, agents, data interfaces |
| `frontend/` | Web interface, event display, real-time feedback |
| `sensors/`  | Wrappers for each physical input                 |
| `voz/`      | STT, TTS, keyword detection                      |
| `vision/`   | Pose detection, camera processing                |
| `gui/`      | Visual representation of FSM and status          |
| `agents/`   | Perception, planning, and behavior modules       |

---

## 4. Communication Between Modules

* Internal software modules communicate via event queue.
* Voice and vision events are parsed and forwarded to the FSM.
* FSM determines system response and activates appropriate module.
* GUI syncs with state changes via socket or polling.

---

## 5. Deployment Topology

* Local execution on Raspberry Pi with virtual environments.
* External React frontend served via internal network or localhost.
* All modules run as services or long-running processes.
* Shared data (logs, configs) stored in `data/` directory.

---

## 6. Future Integration Points

* MQTT for inter-device communication.
* Remote configuration via web dashboard.
* Cloud or LAN integration for distributed sensor nodes.
* Expansion to multi-core execution on future embedded boards.

---

## 7. Notes

* All components must be replaceable or mockable.
* Minimal hard dependencies between modules.
* Emphasis on cooperative multitasking and explicit state transitions.
