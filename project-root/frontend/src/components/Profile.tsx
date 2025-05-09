import React from "react";
import Navbar from "../components/Navbar";
import { motion } from "framer-motion";
import { useAuth } from "../context/AuthContext";

const Profile = () => {
  const { logout } = useAuth();

  return (
    <div className="min-h-screen bg-black text-white font-['Roboto',sans-serif] overflow-y-scroll scroll-smooth">
      <Navbar />

      <motion.div
        className="pt-24 px-4 md:px-10 lg:px-20 max-w-4xl mx-auto"
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.6 }}
      >
        <h1 className="text-3xl font-bold mb-6 text-cyan-400">Your Profile</h1>

        <div className="bg-[#1a1a1a] p-6 rounded-xl shadow-inner border border-gray-800">
          <p className="text-gray-300 mb-2"><strong>Username:</strong> alberto.marquillas</p>
          <p className="text-gray-300 mb-2"><strong>Email:</strong> alberto@example.com</p>
          <p className="text-gray-300"><strong>Role:</strong> Admin</p>
        </div>

        <div className="mt-8 bg-[#1a1a1a] p-6 rounded-xl shadow-inner border border-gray-800">
          <h2 className="text-xl font-semibold text-white mb-4">Preferences</h2>
          <p className="text-gray-400 text-sm">
            Feature toggles or theme settings will go here.
          </p>
        </div>

        <div className="mt-8 bg-[#1a1a1a] p-6 rounded-xl shadow-inner border border-gray-800">
          <h2 className="text-xl font-semibold text-white mb-4">Account Actions</h2>
          <div className="flex flex-col gap-4">
            <button
              onClick={logout}
              className="flex items-center justify-center gap-2 border border-cyan-600 text-cyan-400 hover:bg-cyan-600 hover:text-white transition-colors px-4 py-2 rounded-full font-medium"
            >
              <span>Log Out</span>
            </button>
            <button
              onClick={() => {
                if (confirm("Are you sure you want to delete your account? This action cannot be undone.")) {
                  logout();
                }
              }}
              className="flex items-center justify-center gap-2 border border-red-600 text-red-400 hover:bg-red-600 hover:text-white transition-colors px-4 py-2 rounded-full font-medium"
            >
              <span>Delete Account</span>
            </button>
          </div>
        </div>
      </motion.div>
    </div>
  );
};

export default Profile;