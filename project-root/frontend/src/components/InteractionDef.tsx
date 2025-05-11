import React, { useState, useEffect } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { Button } from "@/components/ui/button";
import { cn } from "@/lib/utils";
import Navbar from "@/components/Navbar";

const eventLabels: Record<NoraEvent, string> = {
  EVT_NFC_ACTIVATE: "Activación NFC",
  EVT_WAKEWORD: "Palabra clave detectada",
  EVT_PRESENCE_CONFIRMED: "Presencia confirmada",
  EVT_ATTENTION_GAINED: "Atención visual ganada",
  EVT_SCHEDULE_TRIGGERED: "Evento programado",
  EVT_SPEECH_START: "Inicio de voz",
  EVT_ATTENTION_CONFIRMED: "Atención confirmada",
  EVT_SPEECH_RECOGNIZED: "Voz reconocida",
  EVT_GESTURE_COMMAND: "Comando gestual",
  EVT_IDLE_TIMEOUT: "Tiempo de inactividad",
  EVT_ATTENTION_LOST: "Atención perdida",
  EVT_LISTEN_TIMEOUT: "Timeout de escucha",
  EVT_MODULE_FAILURE: "Fallo en módulo",
  EVT_MIC_FAILURE: "Fallo de micrófono",
  EVT_PROCESS_FAILURE: "Error de proceso",
  EVT_PROCESS_COMPLETED: "Proceso completado",
  EVT_RECOVERY_SUCCESS: "Recuperación exitosa",
  T_ERROR_RECOVERY_TIMEOUT: "Timeout recuperación error",
  CMD_FORCE_RESUME: "Forzar reanudación",
  CMD_INHIBIR_ACTIVACION: "Inhibir activación",
  CMD_INHIBIR_ESCUCHA: "Inhibir escucha",
  CMD_CANCEL_LISTENING: "Cancelar escucha",
};

type NoraEvent = keyof typeof eventLabels;

type NoraState =
  | "INACTIVO"
  | "ACTIVO"
  | "ESCUCHANDO"
  | "PROCESANDO"
  | "RESPONDIENDO"
  | "ERROR"
  | "DURMIENDO";

interface EventLog {
  id: number;
  event: NoraEvent;
  timestamp: Date;
  fromState: NoraState;
  toState: NoraState;
}

const eventGroups: Record<string, NoraEvent[]> = {
  Activación: [
    "EVT_NFC_ACTIVATE",
    "EVT_WAKEWORD",
    "EVT_PRESENCE_CONFIRMED",
    "EVT_ATTENTION_GAINED",
    "EVT_SCHEDULE_TRIGGERED",
  ],
  Interacción: [
    "EVT_SPEECH_START",
    "EVT_ATTENTION_CONFIRMED",
    "EVT_SPEECH_RECOGNIZED",
    "EVT_GESTURE_COMMAND",
  ],
  Suspensión: [
    "EVT_IDLE_TIMEOUT",
    "EVT_ATTENTION_LOST",
    "EVT_LISTEN_TIMEOUT",
  ],
  Error: [
    "EVT_MODULE_FAILURE",
    "EVT_MIC_FAILURE",
    "EVT_PROCESS_FAILURE",
  ],
  Resolución: [
    "EVT_PROCESS_COMPLETED",
    "EVT_RECOVERY_SUCCESS",
    "T_ERROR_RECOVERY_TIMEOUT",
  ],
  Comandos: [
    "CMD_FORCE_RESUME",
    "CMD_INHIBIR_ACTIVACION",
    "CMD_INHIBIR_ESCUCHA",
    "CMD_CANCEL_LISTENING",
  ],
};

const fsmTransitions: Record<NoraState, Partial<Record<NoraEvent, NoraState>>> = {
  INACTIVO: {
    EVT_WAKEWORD: "ACTIVO",
    EVT_PRESENCE_CONFIRMED: "ACTIVO",
    EVT_NFC_ACTIVATE: "ACTIVO",
  },
  ACTIVO: {
    EVT_SPEECH_START: "ESCUCHANDO",
    EVT_GESTURE_COMMAND: "PROCESANDO",
    CMD_INHIBIR_ACTIVACION: "DURMIENDO",
    EVT_IDLE_TIMEOUT: "INACTIVO",
  },
  ESCUCHANDO: {
    EVT_SPEECH_RECOGNIZED: "PROCESANDO",
    EVT_LISTEN_TIMEOUT: "INACTIVO",
    CMD_CANCEL_LISTENING: "INACTIVO",
  },
  PROCESANDO: {
    EVT_PROCESS_COMPLETED: "RESPONDIENDO",
    EVT_PROCESS_FAILURE: "DURMIENDO",
  },
  RESPONDIENDO: {
    EVT_RECOVERY_SUCCESS: "INACTIVO",
    CMD_FORCE_RESUME: "ACTIVO",
  },
  ERROR: {
    T_ERROR_RECOVERY_TIMEOUT: "INACTIVO",
  },
  DURMIENDO: {
    CMD_FORCE_RESUME: "ACTIVO",
  },
};

const nodePositions: Record<NoraState, { x: number; y: number }> = {
  INACTIVO: { x: 40, y: 30 },
  ACTIVO: { x: 320, y: 60 },
  ESCUCHANDO: { x: 700, y: 30 },
  PROCESANDO: { x: 700, y: 300 },
  RESPONDIENDO: { x: 320, y: 250 },
  ERROR: { x: 160, y: 180 },
  DURMIENDO: { x: 40, y: 300 },
};

const stateColors: Record<NoraState, string> = {
  INACTIVO: "bg-slate-700",
  ACTIVO: "bg-cyan-600",
  ESCUCHANDO: "bg-cyan-400",
  PROCESANDO: "bg-purple-500",
  RESPONDIENDO: "bg-green-500",
  ERROR: "bg-red-500",
  DURMIENDO: "bg-slate-900",
};


export {
  eventLabels,
  eventGroups,
  fsmTransitions,
  nodePositions,
  stateColors,
};

export type {
  NoraEvent,
  NoraState,
  EventLog,
  
};