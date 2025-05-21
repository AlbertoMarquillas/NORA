import React, { useState, useRef, useEffect } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { Button } from "@/ui/button";
import { Input } from "@/ui/input";
import { Send } from "lucide-react";
import Navbar from "@/layout/Navbar";

type Message = {
  id: string;
  text: string;
  sender: "user" | "system";
  timestamp: Date;
};

const Chat = () => {
  const [messages, setMessages] = useState<Message[]>([
    {
      id: "1",
      text: "Hello! I'm NORA. How can I assist you today?",
      sender: "system",
      timestamp: new Date(),
    },
  ]);
  const [inputValue, setInputValue] = useState("");
  const messagesEndRef = useRef<HTMLDivElement>(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSendMessage = () => {
    if (inputValue.trim() === "") return;

    const newUserMessage: Message = {
      id: Date.now().toString(),
      text: inputValue,
      sender: "user",
      timestamp: new Date(),
    };

    setMessages((prev) => [...prev, newUserMessage]);
    setInputValue("");

    // Simulate system response after a short delay
    setTimeout(() => {
      const systemResponse: Message = {
        id: (Date.now() + 1).toString(),
        text: `I received your message: "${inputValue}". This is a simulated response.`,
        sender: "system",
        timestamp: new Date(),
      };
      setMessages((prev) => [...prev, systemResponse]);
    }, 1000);
  };

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      handleSendMessage();
    }
  };

  const formatTime = (date: Date) => {
    return date.toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" });
  };

  return (
    <div className="flex flex-col h-screen bg-[#121212]">
      <Navbar />
      <div className="flex-1 overflow-hidden pt-16 pb-20 px-4 md:px-6 lg:px-8">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.5 }}
          className="max-w-4xl mx-auto h-full flex flex-col"
        >
          <div className="py-6">
            <h1 className="text-2xl font-bold text-white mb-1">
              Chat with NORA
            </h1>
            <p className="text-gray-400">Ask anything or request assistance</p>
          </div>

          <div className="flex-1 overflow-y-auto pr-2 space-y-4 pb-4">
            <AnimatePresence>
              {messages.map((message) => (
                <motion.div
                  key={message.id}
                  initial={{ opacity: 0, y: 20 }}
                  animate={{ opacity: 1, y: 0 }}
                  exit={{ opacity: 0, scale: 0.95 }}
                  transition={{ duration: 0.3 }}
                  className={`flex ${message.sender === "user" ? "justify-end" : "justify-start"}`}
                >
                  <div
                    className={`max-w-[80%] md:max-w-[70%] rounded-2xl px-4 py-3 ${
                      message.sender === "user"
                        ? "bg-blue-600 text-white rounded-tr-none"
                        : "bg-[#1a1a1a] text-white border border-gray-800 rounded-tl-none"
                    }`}
                  >
                    <div className="flex flex-col">
                      <div className="break-words">{message.text}</div>
                      <div
                        className={`text-xs mt-1 self-end ${message.sender === "user" ? "text-blue-200" : "text-gray-400"}`}
                      >
                        {formatTime(message.timestamp)}
                      </div>
                    </div>
                  </div>
                </motion.div>
              ))}
            </AnimatePresence>
            <div ref={messagesEndRef} />
          </div>
        </motion.div>
      </div>

      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5, delay: 0.2 }}
        className="fixed bottom-6 left-0 right-0 p-4"
      >
        <div className="max-w-4xl mx-auto flex items-center gap-2">
          <div className="relative flex-1">
            <Input
              value={inputValue}
              onChange={(e) => setInputValue(e.target.value)}
              onKeyDown={handleKeyDown}
              placeholder="Type your message..."
              className="bg-[#1a1a1a] border-gray-700 text-white pr-10 focus-visible:ring-cyan-500 focus-visible:ring-opacity-50"
            />
          </div>
          <Button
            onClick={handleSendMessage}
            disabled={inputValue.trim() === ""}
            className="bg-cyan-600 hover:bg-cyan-700 text-white"
            size="icon"
          >
            <Send className="h-5 w-5" />
          </Button>
        </div>
      </motion.div>
        <div className="py-2 flex flex-col items-center">
            <p className="text-gray-400">NORA</p>
        </div>
    </div>
             
  );
};

export default Chat;
