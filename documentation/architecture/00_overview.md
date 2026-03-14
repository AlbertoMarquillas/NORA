# 00 - Project Overview: NORA

NORA (Neural Observant Responsive Assistant) is a modular AI-powered physical assistant designed to interact with users through voice, vision, and sensor-based input. It combines embedded systems, intelligent software agents, and machine learning to offer a responsive and adaptive interface for daily interaction, experimentation, and automation.

---

## 1. Purpose and Goals

The project aims to:

* Explore multimodal human-computer interaction.
* Integrate real-world sensors, actuators, and AI in a coherent assistant system.
* Serve as a personal testbed for hardware-software integration, low-level electronics, and AI models.
* Evolve into a customizable assistant framework for prototyping and education.

---

## 2. Key Features

* **Voice interaction**: Wake word detection, speech recognition (STT), speech synthesis (TTS).
* **Vision system**: Face recognition, posture analysis, presence detection.
* **Physical interface**: RGB LEDs, small motors/servos, screen output.
* **Sensor network**: Temperature, movement, tilt, touch, light, NFC.
* **Modular agents**: For dialogue, behavior, perception, decision-making.
* **Custom hardware control**: GPIO-based interactions on a Raspberry Pi.

---

## 3. Platform and Architecture

* **Base platform**: Raspberry Pi 4 Model B (8 GB) with Linux.
* **Programming languages**: Python (core + agents), C (firmware for microcontrollers), JavaScript (frontend).
* **Architecture**: Layered modular architecture with service-based interactions.
* **Execution model**: Event-driven + cooperative task scheduling.

---

## 4. Usage Scenarios

* Interactive installation or demonstration unit.
* Personal assistant for room automation.
* Educational prototype for AI, IoT and embedded systems.
* Sandbox for custom behavior scripting and experimentation.

---

## 5. Long-Term Vision

* Port NORA to a custom-designed PCB (no protoboards).
* Replace preassembled modules with bare ICs and components.
* Train specialized ML models for emotion, gestures, and dialogue control.
* Build a full metal/plastic head prototype with animated face and sensors.

---

## 6. Development Approach

* Iterative, versioned development using Git + Jira.
* Separation of software, hardware, and experimental components.
* All progress and learning documented under `documentation/`.
* Code maintained in separate domains (`backend/`, `frontend/`, `agents/`, `hardware/`).

---

## 7. Status

Current phase (May 2025): Architecture definition and initial subsystem tests.

---

## 8. Author

**Alberto Marquillas**

* Degree: Telecommunications Engineering
* Interests: AI, embedded systems, hardware integration, computer vision, project-based learning
