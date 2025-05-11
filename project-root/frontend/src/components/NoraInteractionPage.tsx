import { useState, useEffect } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { Button } from "@/components/ui/button";
import { cn } from "@/lib/utils";
import Navbar from "@/components/Navbar"; // ✅ añadimos el Navbar

// Define FSM states and events
type NoraState =
  | "IDLE"
  | "ACTIVE"
  | "LISTENING"
  | "PROCESSING"
  | "RESPONDING"
  | "ERROR"
  | "SLEEP";

type NoraEvent =
  | "EVT_WAKEWORD"
  | "EVT_PHYSICAL_TILT"
  | "EVT_PRESENCE"
  | "EVT_GUI_CLICK"
  | "EVT_VOICE_COMMAND"
  | "EVT_NFC_VALID"
  | "EVT_NFC_INVALID"
  | "EVT_TIMEOUT"
  | "EVT_ERROR"
  | "EVT_COMPLETE"
  | "EVT_SLEEP";

interface EventLog {
  id: number;
  event: NoraEvent;
  timestamp: Date;
  fromState: NoraState;
  toState: NoraState;
}

const fsmTransitions: Record<NoraState, Partial<Record<NoraEvent, NoraState>>> = {
  IDLE: {
    EVT_WAKEWORD: "ACTIVE",
    EVT_PHYSICAL_TILT: "ACTIVE",
    EVT_PRESENCE: "ACTIVE",
    EVT_GUI_CLICK: "ACTIVE",
    EVT_SLEEP: "SLEEP",
  },
  ACTIVE: {
    EVT_VOICE_COMMAND: "LISTENING",
    EVT_GUI_CLICK: "LISTENING",
    EVT_NFC_VALID: "PROCESSING",
    EVT_NFC_INVALID: "ERROR",
    EVT_TIMEOUT: "IDLE",
    EVT_ERROR: "ERROR",
    EVT_SLEEP: "SLEEP",
  },
  LISTENING: {
    EVT_VOICE_COMMAND: "PROCESSING",
    EVT_TIMEOUT: "IDLE",
    EVT_ERROR: "ERROR",
    EVT_SLEEP: "SLEEP",
  },
  PROCESSING: {
    EVT_COMPLETE: "RESPONDING",
    EVT_ERROR: "ERROR",
    EVT_TIMEOUT: "IDLE",
    EVT_SLEEP: "SLEEP",
  },
  RESPONDING: {
    EVT_COMPLETE: "IDLE",
    EVT_VOICE_COMMAND: "LISTENING",
    EVT_GUI_CLICK: "LISTENING",
    EVT_ERROR: "ERROR",
    EVT_SLEEP: "SLEEP",
  },
  ERROR: {
    EVT_GUI_CLICK: "IDLE",
    EVT_PHYSICAL_TILT: "IDLE",
    EVT_SLEEP: "SLEEP",
  },
  SLEEP: {
    EVT_WAKEWORD: "IDLE",
    EVT_PHYSICAL_TILT: "IDLE",
    EVT_GUI_CLICK: "IDLE",
  },
};

const eventGroups = {
  Voice: ["EVT_WAKEWORD", "EVT_VOICE_COMMAND"],
  Physical: ["EVT_PHYSICAL_TILT", "EVT_PRESENCE"],
  Interface: ["EVT_GUI_CLICK", "EVT_NFC_VALID", "EVT_NFC_INVALID"],
  System: ["EVT_TIMEOUT", "EVT_ERROR", "EVT_COMPLETE", "EVT_SLEEP"],
};

const nodePositions: Record<NoraState, { x: number; y: number }> = {
  IDLE: { x: 40, y: 30 },
  ACTIVE: { x: 320, y: 60 },
  LISTENING: { x: 700, y: 30 },
  PROCESSING: { x: 700, y: 300 },
  RESPONDING: { x: 320, y: 250 },
  ERROR: { x: 160, y: 180 },
  SLEEP: { x: 40, y: 300 },
};

const stateColors: Record<NoraState, string> = {
  IDLE: "bg-slate-700",
  ACTIVE: "bg-cyan-600",
  LISTENING: "bg-cyan-400",
  PROCESSING: "bg-purple-500",
  RESPONDING: "bg-green-500",
  ERROR: "bg-red-500",
  SLEEP: "bg-slate-900",
};

const NoraInteractionPage = () => {
  const [currentState, setCurrentState] = useState<NoraState>("IDLE");
  const [eventLog, setEventLog] = useState<EventLog[]>([]);
  const [highlightedTransition, setHighlightedTransition] = useState<{
    from: NoraState;
    to: NoraState;
  } | null>(null);

  const handleEvent = (event: NoraEvent) => {
    const nextState = fsmTransitions[currentState][event];
    if (nextState) {
      const newLog: EventLog = {
        id: Date.now(),
        event,
        timestamp: new Date(),
        fromState: currentState,
        toState: nextState,
      };
      setEventLog((prev) => [newLog, ...prev].slice(0, 5));
      setHighlightedTransition({ from: currentState, to: nextState });
      setTimeout(() => {
        setCurrentState(nextState);
        setTimeout(() => setHighlightedTransition(null), 500);
      }, 500);
    }
  };

  const isEventValid = (event: NoraEvent) => {
    return !!fsmTransitions[currentState][event];
  };

  const formatTime = (date: Date) => {
    return date.toLocaleTimeString([], {
      hour: "2-digit",
      minute: "2-digit",
      second: "2-digit",
    });
  };

  return (
    <div className="min-h-screen bg-black text-white font-['Roboto',sans-serif] px-6 pt-24">
      <Navbar />
      <div className="max-w-screen-xl mx-auto">
        <h1 className="text-3xl font-bold text-cyan-400 mb-6">
          NORA Interaction Simulator
        </h1>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          <div className="bg-[#1a1a1a] border border-gray-800 rounded-xl p-6 shadow-inner">
            <h2 className="text-xl font-semibold mb-4 text-cyan-300">
              Interaction Events
            </h2>
            {Object.entries(eventGroups).map(([group, events]) => (
              <div key={group} className="mb-6">
                <h3 className="text-md font-medium mb-2 text-cyan-200">{group}</h3>
                <div className="grid grid-cols-2 gap-2">
                  {events.map((evt) => (
                    <Button
                      key={evt}
                      onClick={() => handleEvent(evt as NoraEvent)}
                      disabled={!isEventValid(evt as NoraEvent)}
                      variant={isEventValid(evt as NoraEvent) ? "default" : "outline"}
                      className={cn(
                        "text-sm px-3 py-2",
                        isEventValid(evt as NoraEvent)
                          ? "hover:bg-cyan-600"
                          : "opacity-50 cursor-not-allowed"
                      )}
                    >
                      {evt.replace("EVT_", "").replace("_", " ")}
                    </Button>
                  ))}
                </div>
              </div>
            ))}
          </div>

          <div className="lg:col-span-2 bg-[#1a1a1a] border border-gray-800 rounded-xl p-6 shadow-inner">
            <h2 className="text-xl font-semibold mb-4 text-cyan-300">System State</h2>
            <div className="relative h-96 mb-6 border border-slate-700 rounded-lg bg-black overflow-hidden">
              {Object.entries(nodePositions).map(([state, pos]) => {
                const isActive = state === currentState;
                return (
                  <motion.div
                    key={state}
                    className={cn(
                      "absolute rounded-full flex items-center justify-center shadow-md text-xs font-bold",
                      stateColors[state as NoraState],
                      isActive ? "w-16 h-16 ring-4 ring-white" : "w-12 h-12"
                    )}
                    style={{
                      left: `${pos.x}px`,
                      top: `${pos.y}px`,
                      transform: "translate(-50%, -50%)",
                    }}
                    animate={{ scale: isActive ? 1.2 : 1 }}
                    transition={{ type: "spring", stiffness: 300, damping: 20 }}
                  >
                    {state}
                  </motion.div>
                );
              })}
              <svg className="absolute inset-0 w-full h-full">
                {Object.entries(fsmTransitions).flatMap(([from, trans]) =>
                  Object.entries(trans).map(([event, to]) => {
                    const a = nodePositions[from as NoraState];
                    const b = nodePositions[to as NoraState];
                    const midX = (a.x + b.x) / 2;
                    const midY = (a.y + b.y) / 2;
                    const dx = b.x - a.x;
                    const dy = b.y - a.y;
                    const norm = Math.sqrt(dx * dx + dy * dy);
                    const offset = 30;
                    const offsetX = (-dy / norm) * offset;
                    const offsetY = (dx / norm) * offset;
                    const cx = midX + offsetX;
                    const cy = midY + offsetY;
                    const isHighlighted =
                      highlightedTransition?.from === from &&
                      highlightedTransition?.to === to;

                    return (
                      <path
                        key={`${from}-${event}-${to}`}
                        d={`M ${a.x} ${a.y} Q ${cx} ${cy} ${b.x} ${b.y}`}
                        fill="none"
                        stroke={isHighlighted ? "#22d3ee" : "#475569"}
                        strokeWidth={isHighlighted ? 2 : 1}
                        strokeDasharray={isHighlighted ? "none" : "5,5"}
                      />
                    );
                  })
                )}
              </svg>
            </div>

            <div>
              <h3 className="text-lg font-medium mb-3 text-cyan-200">Event Log</h3>
              <div className="bg-black border border-gray-700 rounded-xl p-4 max-h-48 overflow-y-auto">
                <AnimatePresence>
                  {eventLog.length > 0 ? (
                    eventLog.map((log) => (
                      <motion.div
                        key={log.id}
                        initial={{ opacity: 0, y: -10 }}
                        animate={{ opacity: 1, y: 0 }}
                        exit={{ opacity: 0 }}
                        className="mb-2 p-2 bg-[#1a1a1a] rounded border-l-4 border-cyan-500"
                      >
                        <div className="flex justify-between">
                          <span className="font-medium">
                            {log.event.replace("EVT_", "")}
                          </span>
                          <span className="text-slate-400 text-sm">
                            {formatTime(log.timestamp)}
                          </span>
                        </div>
                        <div className="text-sm text-slate-300">
                          {log.fromState} → {log.toState}
                        </div>
                      </motion.div>
                    ))
                  ) : (
                    <p className="text-slate-500 text-center">No events recorded</p>
                  )}
                </AnimatePresence>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default NoraInteractionPage;
