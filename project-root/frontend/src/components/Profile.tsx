import React from "react";
import { motion } from "framer-motion";
import Navbar from "./Navbar";
import { Button } from "./ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "./ui/card";
import { Separator } from "./ui/separator";
import { useAuth } from "@/context/AuthContext";

const Profile = () => {
    const { user, logout, deleteAccount } = useAuth();

  const handleLogout = async () => {
    await logout();
  };

  return (
    <div className="min-h-screen bg-black text-white">
      <Navbar />

      <div className="container mx-auto px-4 pt-24 pb-12">
        <motion.div
          initial={{ opacity: 0, y: -20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.5 }}
          className="mb-10"
        >
          <h1 className="text-4xl font-bold text-center mb-2">Your Profile</h1>
          <div className="w-20 h-1 bg-cyan-400 mx-auto"></div>
        </motion.div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
          <motion.div
            initial={{ opacity: 0, x: -20 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.5, delay: 0.2 }}
            className="col-span-1"
          >
            <Card className="bg-[#1a1a1a] border border-gray-800 rounded-xl shadow-inner">
              <CardHeader>
                <CardTitle className="text-2xl text-cyan-400">
                  Profile Information
                </CardTitle>
              </CardHeader>
              <CardContent className="space-y-6 p-6">
                <div>
                  <h3 className="text-gray-400 mb-1">Username</h3>
                  <p className="text-xl font-medium">{user.name}</p>
                </div>
                <Separator className="bg-gray-800" />
                <div>
                  <h3 className="text-gray-400 mb-1">Email</h3>
                  <p className="text-xl font-medium">{user.email}</p>
                </div>
                <Separator className="bg-gray-800" />
                <div>
                  <h3 className="text-gray-400 mb-1">Role</h3>
                  <p className="text-xl font-medium">{user.role}</p>
                </div>
              </CardContent>
            </Card>
          </motion.div>

          <motion.div
            initial={{ opacity: 0, x: 20 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.5, delay: 0.4 }}
            className="col-span-1 space-y-8"
          >
            <Card className="bg-[#1a1a1a] border border-gray-800 rounded-xl shadow-inner">
              <CardHeader>
                <CardTitle className="text-2xl text-cyan-400">
                  Preferences
                </CardTitle>
              </CardHeader>
              <CardContent className="p-6">
                <p className="text-gray-300 mb-4">
                  Customize how NORA interacts with you and your environment.
                </p>
                <div className="space-y-4">
                  <div className="p-4 bg-[#121212] rounded-lg border border-gray-800">
                    <h3 className="font-medium mb-1">Interaction Mode</h3>
                    <p className="text-sm text-gray-400">
                      Voice and gesture recognition enabled
                    </p>
                  </div>
                  <div className="p-4 bg-[#121212] rounded-lg border border-gray-800">
                    <h3 className="font-medium mb-1">Privacy Settings</h3>
                    <p className="text-sm text-gray-400">
                      Standard data collection
                    </p>
                  </div>
                  <div className="p-4 bg-[#121212] rounded-lg border border-gray-800">
                    <h3 className="font-medium mb-1">
                      Notification Preferences
                    </h3>
                    <p className="text-sm text-gray-400">
                      All notifications enabled
                    </p>
                  </div>
                </div>
              </CardContent>
            </Card>

            <Card className="bg-[#1a1a1a] border border-gray-800 rounded-xl shadow-inner">
              <CardHeader>
                <CardTitle className="text-2xl text-cyan-400">
                  Account Actions
                </CardTitle>
              </CardHeader>
              <CardContent className="p-6 space-y-4">
                <Button
                  onClick={handleLogout}
                  className="w-full border border-cyan-600 bg-transparent hover:bg-cyan-600 text-white transition-all duration-300"
                >
                  Logout
                </Button>
                <Button
                  onClick={deleteAccount}
                  variant="outline"
                  className="w-full border-red-600 text-red-500 hover:bg-red-900/20 hover:text-red-400 transition-all duration-300"
                >
                  Delete Account
                </Button>
              </CardContent>
            </Card>
          </motion.div>
        </div>
      </div>
    </div>
  );
};

export default Profile;
