import React from "react";
import { motion } from "framer-motion";
import { Link } from "react-router-dom";
import { Button } from "@/ui/button";
import Navbar from "@/layout/Navbar";

const NotFound = () => {
  return (
    <div className="min-h-screen bg-black text-white flex flex-col items-center justify-center">
      <Navbar />
      <motion.div
        className="text-center pt-24"
        initial={{ opacity: 0, y: -20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
      >
        <h1 className="text-6xl font-bold text-cyan-400 mb-4">404</h1>
        <p className="text-lg text-gray-400 mb-6">
          Sorry, the page you are looking for does not exist.
        </p>
        <Link to="/">
          <Button className="bg-cyan-600 hover:bg-cyan-700 text-white px-6 py-2 rounded-md">
            Back to Home
          </Button>
        </Link>
      </motion.div>
    </div>
  );
};

export default NotFound;
