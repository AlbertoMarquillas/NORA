import React, { useState } from "react";
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
import {
  Tooltip,
  TooltipContent,
  TooltipProvider,
  TooltipTrigger,
} from "@/ui/tooltip";
import { RefreshCw, AlertTriangle, CheckCircle } from "lucide-react";
import { Button } from "@/ui/button";
import Navbar from "@/layout/Navbar";

// Types for module data
interface SystemModule {
  name: string;
  status: "online" | "offline" | "error" | "degraded";
  lastUpdated: string;
  description?: string;
}

// Sample data for system modules
const initialModules: SystemModule[] = [
  {
    name: "Voice Engine",
    status: "online",
    lastUpdated: "2025-05-23 14:12:00",
    description: "Natural language processing and voice synthesis system",
  },
  {
    name: "Vision Module",
    status: "degraded",
    lastUpdated: "2025-05-23 14:11:43",
    description: "Computer vision and image recognition capabilities",
  },
  {
    name: "NFC Reader",
    status: "offline",
    lastUpdated: "2025-05-23 14:10:21",
    description: "Near-field communication for device pairing",
  },
  {
    name: "Wi-Fi",
    status: "online",
    lastUpdated: "2025-05-23 14:12:02",
    description: "Wireless network connectivity",
  },
  {
    name: "Bluetooth",
    status: "error",
    lastUpdated: "2025-05-23 14:09:51",
    description: "Short-range wireless communication protocol",
  },
  {
    name: "Temperature Sensor",
    status: "online",
    lastUpdated: "2025-05-23 14:11:55",
    description: "Environmental temperature monitoring",
  },
  {
    name: "Microphone Array",
    status: "online",
    lastUpdated: "2025-05-23 14:12:05",
    description: "Spatial audio capture system",
  },
  {
    name: "Motion Sensors",
    status: "online",
    lastUpdated: "2025-05-23 14:11:48",
    description: "Presence and movement detection",
  },
];

// Group modules by type
const groupedModules = {
  "Core Systems": ["Voice Engine", "Vision Module"],
  Connectivity: ["Wi-Fi", "Bluetooth", "NFC Reader"],
  Sensors: ["Temperature Sensor", "Microphone Array", "Motion Sensors"],
};

const SystemStatus = () => {
  const [modules, setModules] = useState<SystemModule[]>(initialModules);
  const [isRefreshing, setIsRefreshing] = useState(false);

  // Check if any module has error status
  const hasErrors = modules.some((module) => module.status === "error");

  // Check if any module has degraded status
  const hasDegraded = modules.some((module) => module.status === "degraded");

  // Check if all modules are online
  const allOnline = modules.every((module) => module.status === "online");

  // Function to simulate refreshing the module statuses
  const handleRefresh = () => {
    setIsRefreshing(true);

    // Simulate API call delay
    setTimeout(() => {
      setIsRefreshing(false);
    }, 1000);
  };

  // Get status badge color based on status
  const getStatusColor = (status: string) => {
    switch (status) {
      case "online":
        return "bg-green-500 hover:bg-green-600";
      case "offline":
        return "bg-gray-500 hover:bg-gray-600";
      case "error":
        return "bg-red-500 hover:bg-red-600";
      case "degraded":
        return "bg-yellow-500 hover:bg-yellow-600";
      default:
        return "bg-gray-500 hover:bg-gray-600";
    }
  };

  // Get modules by group
  const getModulesByGroup = (groupName: string) => {
    const moduleNames =
      groupedModules[groupName as keyof typeof groupedModules] || [];
    return modules.filter((module) => moduleNames.includes(module.name));
  };

  return (
    <div>
      <Navbar />
    <div className="bg-[#121212] min-h-screen pt-24 px-4 md:px-6 lg:px-8">
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
      >
        <div className="flex justify-between items-center mb-6">
          <h1 className="text-3xl font-bold text-white">
            <span className="text-cyan-400">NORA</span> System Status
          </h1>
          <Button
            variant="outline"
            size="sm"
            className="border-gray-700 text-gray-300 hover:text-white hover:border-cyan-500"
            onClick={handleRefresh}
            disabled={isRefreshing}
          >
            <RefreshCw
              className={`h-4 w-4 mr-2 ${isRefreshing ? "animate-spin" : ""}`}
            />
            {isRefreshing ? "Refreshing..." : "Refresh Status"}
          </Button>
        </div>

        {/* System Status Overview */}
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 0.2 }}
        >
          <Card className="bg-[#1a1a1a] border-gray-800 shadow-lg mb-6">
            <CardHeader className="border-b border-gray-800 bg-[#1a1a1a]">
              <CardTitle className="text-white flex items-center">
                System Overview
              </CardTitle>
              <CardDescription className="text-gray-400">
                Current operational status of all NORA modules
              </CardDescription>
            </CardHeader>
            <CardContent className="pt-4">
              {hasErrors && (
                <motion.div
                  className="flex items-center p-3 mb-4 bg-red-900/20 border border-red-800 rounded-md text-red-300"
                  initial={{ opacity: 0, height: 0 }}
                  animate={{ opacity: 1, height: "auto" }}
                  transition={{ duration: 0.3 }}
                >
                  <AlertTriangle className="h-5 w-5 mr-2 text-red-400" />
                  <span>
                    Critical system errors detected. Immediate attention
                    required.
                  </span>
                </motion.div>
              )}

              {!hasErrors && hasDegraded && (
                <motion.div
                  className="flex items-center p-3 mb-4 bg-yellow-900/20 border border-yellow-800 rounded-md text-yellow-300"
                  initial={{ opacity: 0, height: 0 }}
                  animate={{ opacity: 1, height: "auto" }}
                  transition={{ duration: 0.3 }}
                >
                  <AlertTriangle className="h-5 w-5 mr-2 text-yellow-400" />
                  <span>Some modules are operating at reduced capacity.</span>
                </motion.div>
              )}

              {allOnline && (
                <motion.div
                  className="flex items-center p-3 mb-4 bg-green-900/20 border border-green-800 rounded-md text-green-300"
                  initial={{ opacity: 0, height: 0 }}
                  animate={{ opacity: 1, height: "auto" }}
                  transition={{ duration: 0.3 }}
                >
                  <CheckCircle className="h-5 w-5 mr-2 text-green-400" />
                  <span>All systems operational.</span>
                </motion.div>
              )}

              <div className="grid grid-cols-4 gap-4 text-sm text-gray-400 mb-2">
                <div>Module</div>
                <div>Status</div>
                <div>Last Updated</div>
                <div>Description</div>
              </div>
              <Separator className="mb-4 bg-gray-800" />

              <ScrollArea className="h-[200px] pr-4">
                <div className="space-y-4">
                  {modules.map((module, index) => (
                    <motion.div
                      key={module.name}
                      className="grid grid-cols-4 gap-4 items-center"
                      initial={{ opacity: 0, y: 10 }}
                      animate={{ opacity: 1, y: 0 }}
                      transition={{ delay: index * 0.05 }}
                    >
                      <div className="font-medium text-white">
                        {module.name}
                      </div>
                      <div>
                        <Badge className={getStatusColor(module.status)}>
                          {module.status.toUpperCase()}
                        </Badge>
                      </div>
                      <div className="text-gray-400 text-sm">
                        {module.lastUpdated}
                      </div>
                      <div className="text-gray-400 text-sm truncate">
                        {module.description}
                      </div>
                    </motion.div>
                  ))}
                </div>
              </ScrollArea>
            </CardContent>
          </Card>
        </motion.div>

        {/* Grouped Modules */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {Object.keys(groupedModules).map((groupName, groupIndex) => {
            const groupModules = getModulesByGroup(groupName);
            return (
              <motion.div
                key={groupName}
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: 0.3 + groupIndex * 0.1 }}
              >
                <Card className="bg-[#1a1a1a] border-gray-800 shadow-lg overflow-hidden h-full">
                  <CardHeader className="border-b border-gray-800 bg-[#1a1a1a]">
                    <CardTitle className="text-white">{groupName}</CardTitle>
                    <CardDescription className="text-gray-400">
                      {groupModules.length} modules
                    </CardDescription>
                  </CardHeader>
                  <CardContent className="pt-4">
                    <div className="space-y-3">
                      {groupModules.map((module, moduleIndex) => (
                        <TooltipProvider key={module.name}>
                          <Tooltip>
                            <TooltipTrigger asChild>
                              <motion.div
                                className="flex justify-between items-center p-2 rounded-md hover:bg-gray-800/50 cursor-pointer"
                                initial={{ opacity: 0 }}
                                animate={{ opacity: 1 }}
                                transition={{ delay: 0.4 + moduleIndex * 0.05 }}
                              >
                                <span className="text-white">
                                  {module.name}
                                </span>
                                <Badge
                                  className={getStatusColor(module.status)}
                                >
                                  {module.status}
                                </Badge>
                              </motion.div>
                            </TooltipTrigger>
                            <TooltipContent className="bg-gray-900 text-white border-gray-700">
                              <div className="text-sm">
                                <p>
                                  <strong>Status:</strong> {module.status}
                                </p>
                                <p>
                                  <strong>Last Updated:</strong>{" "}
                                  {module.lastUpdated}
                                </p>
                                {module.description && (
                                  <p>
                                    <strong>Description:</strong>{" "}
                                    {module.description}
                                  </p>
                                )}
                              </div>
                            </TooltipContent>
                          </Tooltip>
                        </TooltipProvider>
                      ))}
                    </div>
                  </CardContent>
                  <CardFooter className="border-t border-gray-800 bg-[#1a1a1a]/50 text-xs text-gray-500">
                    Last system check: {new Date().toLocaleString()}
                  </CardFooter>
                </Card>
              </motion.div>
            );
          })}
        </div>
      </motion.div>
    </div>
    </div>
  );
};

export default SystemStatus;
