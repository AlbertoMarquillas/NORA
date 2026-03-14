import React from "react";
import { motion } from "framer-motion";
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/ui/card";
import { Badge } from "@/ui/badge";
import { ScrollArea } from "@/ui/scroll-area";
import { Separator } from "@/ui/separator";
import { Button } from "@/ui/button";
import Navbar from "@/layout/Navbar";
import {
  AlertCircle,
  Info,
  AlertTriangle,
  Activity,
  Trash2,
} from "lucide-react";

// Sample log data
const logs = [
  {
    timestamp: "2025-05-19 13:32:08",
    type: "info",
    message: "NORA started successfully.",
    user: "System",
  },
  {
    timestamp: "2025-05-19 13:33:22",
    type: "action",
    message: "User 'alberto' accessed settings.",
    user: "alberto",
  },
  {
    timestamp: "2025-05-19 13:35:00",
    type: "warning",
    message: "Vision module is not responding.",
    user: "System",
  },
  {
    timestamp: "2025-05-19 13:36:10",
    type: "error",
    message: "Failed to connect to voice server.",
    user: "System",
  },
];

interface LogEntry {
  timestamp: string;
  type: "info" | "warning" | "error" | "action";
  message: string;
  user: string;
}

const getLogIcon = (type: LogEntry["type"]) => {
  switch (type) {
    case "info":
      return <Info className="h-4 w-4 text-blue-400" />;
    case "warning":
      return <AlertTriangle className="h-4 w-4 text-yellow-400" />;
    case "error":
      return <AlertCircle className="h-4 w-4 text-red-400" />;
    case "action":
      return <Activity className="h-4 w-4 text-green-400" />;
    default:
      return <Info className="h-4 w-4 text-blue-400" />;
  }
};

const getLogBadgeVariant = (type: LogEntry["type"]) => {
  switch (type) {
    case "info":
      return "default";
    case "warning":
      return "secondary";
    case "error":
      return "destructive";
    case "action":
      return "outline";
    default:
      return "default";
  }
};

const Logs = () => {
  const handleClearLogs = () => {
    console.log("Clear logs clicked");
    // Functionality to be implemented
  };

  return (
    <div className="bg-[#121212] min-h-screen">
      <Navbar />
      <Separator className="bg-gray-800" />
    <div className="bg-[#121212] min-h-screen pt-24 px-4 md:px-6 lg:px-8">
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
        className="max-w-5xl mx-auto"
      >
        <Card className="bg-[#1a1a1a] border-gray-800 shadow-lg overflow-hidden">
          <CardHeader className="border-b border-gray-800 bg-[#1a1a1a]">
            <div className="flex justify-between items-center">
              <div>
                <CardTitle className="text-white flex items-center">
                  <Activity className="mr-2 h-5 w-5 text-cyan-400" /> System
                  Logs
                </CardTitle>
                <CardDescription className="text-gray-400">
                  History of system events and user actions
                </CardDescription>
              </div>
              <Button
                variant="outline"
                size="sm"
                className="bg-transparent border-gray-700 text-gray-300 hover:bg-white-800 hover:text-white"
                onClick={handleClearLogs}
              >
                <Trash2 className="h-4 w-4 mr-2" /> Clear logs
              </Button>
            </div>
          </CardHeader>
          <CardContent className="p-0">
            <ScrollArea className="h-[500px] w-full">
              {logs.length > 0 ? (
                <div className="divide-y divide-white-800">
                  {logs.map((log, index) => (
                    <motion.div
                      key={index}
                      initial={{ opacity: 0 }}
                      animate={{ opacity: 1 }}
                      transition={{ delay: index * 0.05 }}
                      className="p-4 hover:bg-gray-800/30"
                    >
                      <div className="flex items-start justify-between">
                        <div className="flex items-center">
                          {getLogIcon(log.type)}
                          <Badge
                            variant={getLogBadgeVariant(log.type)}
                            className="ml-2 capitalize text-white"
                          >
                            {log.type}
                          </Badge>
                        </div>
                        <span className="text-xs text-gray-500">
                          {log.timestamp}
                        </span>
                      </div>
                      <p className="text-sm text-gray-300 mt-2 pl-6">
                        {log.message}
                      </p>
                      <div className="flex justify-end mt-1">
                        <span className="text-xs text-cyan-400">
                          {log.user}
                        </span>
                      </div>
                    </motion.div>
                  ))}
                </div>
              ) : (
                <div className="flex flex-col items-center justify-center h-full p-8">
                  <Info className="h-12 w-12 text-gray-500 mb-4" />
                  <p className="text-gray-400 text-center">
                    No logs recorded yet.
                  </p>
                </div>
              )}
            </ScrollArea>
          </CardContent>
          <CardFooter className="border-t border-gray-800 bg-[#1a1a1a]/50 text-xs text-gray-500 flex justify-between">
            <span>Showing all system logs</span>
            <span>{logs.length} entries</span>
          </CardFooter>
        </Card>
      </motion.div>
    </div>
    </div>
  );
};

export default Logs;
