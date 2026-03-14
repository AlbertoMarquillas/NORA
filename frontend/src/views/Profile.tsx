import React from "react";
import { motion } from "framer-motion";
import Navbar from "@/layout/Navbar";
import { Button } from "@/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/ui/card";
import { Separator } from "@/ui/separator";
import { Avatar, AvatarFallback, AvatarImage } from "@/ui/avatar";
import { useAuth } from "@/context/AuthContext";
import Loader from "@/ui/loader"; // ajusta la ruta si es necesario


const RoleBadge = ({ role }: { role: string }) => {
  const colorMap: Record<string, string> = {
    admin: "bg-red-600",
    user: "bg-blue-600",
    guest: "bg-gray-600",
  };

  return (
    <span className={`px-2 py-1 rounded-md text-sm text-white ${colorMap[role]}`}>
      {role.toUpperCase()}
    </span>
  );
};

const Profile = () => {
    const { user, logout, deleteAccount } = useAuth();

    if (!user || !user.name || !user.email || !user.role) {
    return (
        <div className="min-h-screen bg-black text-white">
        <Navbar />
        <Loader />
        </div>
    );
    }

    const handleLogout = async () => {
        await logout();
    };

    const handleDeleteAccount = async () => {
        const confirmed = window.confirm("Are you sure you want to delete your account?");
        if (confirmed) await deleteAccount();
    };

    return (
        <div className="min-h-screen bg-black text-white">
        <Navbar />

        <div className="container mx-auto px-4 pt-24 pb-12">
            <motion.div
            initial={{ opacity: 0, y: -20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.5 }}
            className="mb-10 text-center"
            >
            <Avatar className="h-20 w-20 border-2 border-cyan-500 mx-auto mb-4">
                <AvatarImage src={user.avatar || undefined} />
                <AvatarFallback className="bg-cyan-900 text-white font-bold">
                {user?.name?.[0] ?? "?"}
                </AvatarFallback>
            </Avatar>
            <h1 className="text-4xl font-bold mb-1">Your Profile</h1>
            <div className="w-20 h-1 bg-cyan-400 mx-auto"></div>
            </motion.div>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
            {/* Left side: user info */}
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
                    <RoleBadge role={user.role} />
                    </div>
                </CardContent>
                </Card>
            </motion.div>

            {/* Right side: preferences and actions */}
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
                    <PreferenceItem
                        title="Interaction Mode"
                        description="Voice and gesture recognition enabled"
                    />
                    <PreferenceItem
                        title="Privacy Settings"
                        description="Standard data collection"
                    />
                    <PreferenceItem
                        title="Notification Preferences"
                        description="All notifications enabled"
                    />
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
                    onClick={handleDeleteAccount}
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

const PreferenceItem = ({ title, description }: { title: string; description: string }) => (
  <div className="p-4 bg-[#121212] rounded-lg border border-gray-800">
    <h3 className="font-medium mb-1">{title}</h3>
    <p className="text-sm text-gray-400">{description}</p>
  </div>
);

export default Profile;