import React from "react";
import { motion } from "framer-motion";

const Loader = () => {
  return (
    <div className="flex flex-col items-center justify-center h-screen bg-black text-white">
      <motion.div
        animate={{ rotate: 360 }}
        transition={{ repeat: Infinity, duration: 1, ease: "linear" }}
        className="rounded-full h-16 w-16 border-t-4 border-b-4 border-cyan-400"
      />
      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: [0, 1, 0] }}
        transition={{ repeat: Infinity, duration: 2 }}
        className="mt-4 text-sm text-cyan-300"
      >
        Inicializando sistema NORA...
      </motion.div>
    </div>
  );
};

export default Loader;
