import React from "react";
import { motion } from "framer-motion";
import HeroSection from "@/components/hero/HeroSection";
import AboutSection from "@/components/about/AboutSection";
import FeatureCards from "@/components/feature/FeatureCards";
import Navbar from "@/layout/Navbar";

import { useEffect } from "react";

const fadeUp = (delay = 0) => ({
  initial: { opacity: 0, y: 40, scale: 0.98 },
  whileInView: { opacity: 1, y: 0, scale: 1 },
  transition: { duration: 0.7, ease: "easeOut", delay },
  viewport: { once: true, amount: 0.3 }
});

const Home = () => {
  return (

    <div className="min-h-screen bg-black text-white font-['Roboto',sans-serif] snap-y snap-mandatory overflow-y-scroll scroll-smooth">
      <Navbar />

      <motion.div className="snap-start" initial={{ opacity: 0 }} animate={{ opacity: 1 }} transition={{ duration: 0.8 }}>
        <HeroSection />
      </motion.div>

      <motion.div className="snap-start" {...fadeUp(0.1)}>
        <AboutSection />
      </motion.div>

      <motion.div className="snap-start" {...fadeUp(0.3)}>
        <FeatureCards />
      </motion.div>

      <footer className="py-8 text-center text-gray-400 text-sm snap-start">
        <p>© {new Date().getFullYear()} NORA. All rights reserved.</p>
      </footer>
    </div>
  );
};

export default Home;
