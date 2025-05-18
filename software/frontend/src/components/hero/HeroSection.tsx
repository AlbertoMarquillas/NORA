import React from "react";
import { motion } from "framer-motion";
import noraLogo from "@/assets/nora-hero.png"; // ajusta si la imagen está en otra ruta

interface HeroSectionProps {
  title?: string;
  subtitle?: string;
}

const HeroSection = ({
  title = "NORA",
  subtitle = "Physical intelligent assistant. Minimalism. Context. Presence.",
}: HeroSectionProps) => {
  return (
    <section className="relative h-screen w-full flex flex-col items-center justify-center bg-black text-white overflow-hidden">
      <div className="absolute inset-0 bg-gradient-to-b from-black to-gray-900 z-0"></div>

      <motion.div
        className="absolute w-64 h-64 rounded-full bg-cyan-500/10 blur-3xl"
        initial={{ opacity: 0 }}
        animate={{ opacity: 0.6 }}
        transition={{ duration: 2 }}
        style={{ top: "20%", left: "60%" }}
      />
      <motion.div
        className="absolute w-96 h-96 rounded-full bg-cyan-500/5 blur-3xl"
        initial={{ opacity: 0 }}
        animate={{ opacity: 0.4 }}
        transition={{ duration: 2, delay: 0.5 }}
        style={{ bottom: "10%", right: "60%" }}
      />

      <motion.div
        className="relative z-10 mb-8"
        initial={{ y: 20, opacity: 0 }}
        animate={{ y: 0, opacity: 1 }}
        transition={{ duration: 0.8 }}
      >
        <div className="w-36 h-36 rounded-full overflow-hidden shadow-lg shadow-cyan-500/20">
          <img
            src={noraLogo}
            alt="NORA logo"
            className="w-full h-full object-cover"
          />
        </div>
      </motion.div>

      <motion.h1
        className="relative z-10 text-6xl md:text-7xl font-bold tracking-tight mb-4"
        initial={{ y: 20, opacity: 0 }}
        animate={{ y: 0, opacity: 1 }}
        transition={{ duration: 0.8, delay: 0.2 }}
      >
        {title}
      </motion.h1>

      <motion.p
        className="relative z-10 text-lg md:text-xl text-gray-300 max-w-md text-center"
        initial={{ y: 20, opacity: 0 }}
        animate={{ y: 0, opacity: 1 }}
        transition={{ duration: 0.8, delay: 0.4 }}
      >
        {subtitle}
      </motion.p>

      <motion.div
        className="absolute bottom-10 z-10"
        initial={{ opacity: 0 }}
        animate={{ opacity: 1, y: [0, 10, 0] }}
        transition={{
          opacity: { delay: 1.5, duration: 1 },
          y: { repeat: Infinity, duration: 1.5, ease: "easeInOut" },
        }}
      >
        <div className="w-6 h-10 rounded-full border-2 border-gray-400 flex justify-center pt-2">
          <div className="w-1.5 h-3 bg-cyan-400 rounded-full"></div>
        </div>
      </motion.div>
    </section>
  );
};

export default HeroSection;
