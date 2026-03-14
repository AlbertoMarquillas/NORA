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
import { Progress } from "@/ui/progress";
import { Switch } from "@/ui/switch";
import { Label } from "@/ui/label";
import { ScrollArea } from "@/ui/scroll-area";
import { Cpu, Thermometer, MemoryStick, Clock, User, Terminal } from "lucide-react";
import Navbar from "@/layout/Navbar";

const systemStatus = {
  cpu: 42,
  ram: 68,
  temperature: 38,
  uptime: "3d 7h 22m",
};

const userCommands = [
  { id: 1, user: "User", command: "Activate voice recognition", timestamp: "2023-07-15 14:32:21" },
  { id: 2, user: "Admin", command: "System diagnostic", timestamp: "2023-07-15 13:45:09" },
  { id: 3, user: "User", command: "Set reminder for meeting", timestamp: "2023-07-15 12:30:15" },
  { id: 4, user: "Guest", command: "Weather forecast", timestamp: "2023-07-15 11:22:47" },
  { id: 5, user: "Admin", command: "Update system parameters", timestamp: "2023-07-15 10:15:33" },
  { id: 6, user: "User", command: "Play music playlist", timestamp: "2023-07-15 09:05:12" },
  { id: 7, user: "Admin", command: "Run security scan", timestamp: "2023-07-14 22:45:38" },
];

const AdminDashboard = () => {
  const [modules, setModules] = useState({
    vision: true,
    voice: true,
    motion: false,
    temperature: true,
    proximity: false,
  });

  const handleModuleToggle = (module: keyof typeof modules) => {
    setModules((prev) => ({ ...prev, [module]: !prev[module] }));
  };

  return (
    <div className="min-h-screen bg-[#121212] text-white font-['Roboto',sans-serif] snap-y snap-mandatory overflow-y-scroll scroll-smooth">
      <Navbar />
      <motion.div className="pt-24 px-4 md:px-6 lg:px-8 snap-start" initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.5 }}>
        <h1 className="text-3xl font-bold text-white mb-8">
          <span className="text-cyan-400">NORA</span> Admin Dashboard
        </h1>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          <Card className="bg-[#1a1a1a] border-gray-800 shadow-lg overflow-hidden">
            <CardHeader className="border-b border-gray-800 bg-[#1a1a1a]">
              <CardTitle className="text-white flex items-center">
                <Cpu className="mr-2 h-5 w-5 text-cyan-400" /> System Status
              </CardTitle>
              <CardDescription className="text-gray-400">Current system performance metrics</CardDescription>
            </CardHeader>
            <CardContent className="pt-6 space-y-4">
              <div className="space-y-2">
                <div className="flex justify-between text-sm">
                  <span className="text-gray-400 flex items-center"><Cpu className="mr-1 h-4 w-4 text-cyan-400" /> CPU Usage</span>
                  <span className="text-white">{systemStatus.cpu}%</span>
                </div>
                <Progress value={systemStatus.cpu} className="h-2 bg-gray-700" />
              </div>

              <div className="space-y-2">
                <div className="flex justify-between text-sm">
                  <span className="text-gray-400 flex items-center"><MemoryStick className="mr-1 h-4 w-4 text-cyan-400" /> RAM Usage</span>
                  <span className="text-white">{systemStatus.ram}%</span>
                </div>
                <Progress value={systemStatus.ram} className="h-2 bg-gray-700" />
              </div>

              <div className="space-y-2">
                <div className="flex justify-between text-sm">
                  <span className="text-gray-400 flex items-center"><Thermometer className="mr-1 h-4 w-4 text-cyan-400" /> Temperature</span>
                  <span className="text-white">{systemStatus.temperature}°C</span>
                </div>
                <Progress value={(systemStatus.temperature / 100) * 100} className="h-2 bg-gray-700" />
              </div>

              <div className="flex justify-between text-sm pt-2 border-t border-gray-800">
                <span className="text-gray-400 flex items-center"><Clock className="mr-1 h-4 w-4 text-cyan-400" /> Uptime</span>
                <span className="text-white">{systemStatus.uptime}</span>
              </div>
            </CardContent>
          </Card>

          <Card className="bg-[#1a1a1a] border-gray-800 shadow-lg overflow-hidden">
            <CardHeader className="border-b border-gray-800 bg-[#1a1a1a]">
              <CardTitle className="text-white">Module Controls</CardTitle>
              <CardDescription className="text-gray-400">Activate or deactivate NORA modules</CardDescription>
            </CardHeader>
            <CardContent className="pt-6">
              <div className="space-y-4">
                {Object.entries(modules).map(([key, value]) => (
                  <div key={key} className="flex items-center justify-between">
                    <Label htmlFor={`${key}-module`} className="text-white capitalize flex-1">{key}</Label>
                    <div className="flex items-center space-x-2">
                      <span className={`text-xs ${value ? "text-cyan-400" : "text-gray-500"}`}>{value ? "ACTIVE" : "INACTIVE"}</span>
                      <Switch
                        id={`${key}-module`}
                        checked={value}
                        onCheckedChange={() => handleModuleToggle(key as keyof typeof modules)}
                        className="data-[state=checked]:bg-cyan-500"
                      />
                    </div>
                  </div>
                ))}
              </div>
            </CardContent>
            <CardFooter className="border-t border-gray-800 bg-[#1a1a1a]/50 text-xs text-gray-500">
              Changes take effect immediately
            </CardFooter>
          </Card>

          <Card className="bg-[#1a1a1a] border-gray-800 shadow-lg overflow-hidden md:col-span-2 lg:col-span-1">
            <CardHeader className="border-b border-gray-800 bg-[#1a1a1a]">
              <CardTitle className="text-white flex items-center">
                <Terminal className="mr-2 h-5 w-5 text-cyan-400" /> Command Log
              </CardTitle>
              <CardDescription className="text-gray-400">Recent user interactions with NORA</CardDescription>
            </CardHeader>
            <CardContent className="p-0">
              <ScrollArea className="h-[300px] w-full">
                <div className="divide-y divide-gray-800">
                  {userCommands.map((cmd) => (
                    <div key={cmd.id} className="p-4 hover:bg-gray-800/30">
                      <div className="flex items-start justify-between">
                        <div className="flex items-center">
                          <User className="h-4 w-4 text-cyan-400 mr-2" />
                          <span className="text-sm font-medium text-white">{cmd.user}</span>
                        </div>
                        <span className="text-xs text-gray-500">{cmd.timestamp}</span>
                      </div>
                      <p className="text-sm text-gray-300 mt-1 pl-6">{cmd.command}</p>
                    </div>
                  ))}
                </div>
              </ScrollArea>
            </CardContent>
          </Card>
        </div>
      </motion.div>
    </div>
  );
};

export default AdminDashboard;
