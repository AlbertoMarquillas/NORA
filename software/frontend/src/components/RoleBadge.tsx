import React from "react";
import { motion } from "framer-motion";

interface RoleBadgeProps {
  role: "admin" | "user" | "guest";
}

const roleStyles: Record<RoleBadgeProps["role"], string> = {
  admin: "bg-red-600",
  user: "bg-blue-600",
  guest: "bg-gray-600",
};

/**
 * Renders a badge with color and label based on the user's role.
 */
const RoleBadge = ({ role }: RoleBadgeProps) => {
  return (
    <motion.span
      className={`px-2 py-1 text-xs text-white rounded-md font-semibold ${roleStyles[role]}`}
      initial={{ opacity: 0, scale: 0.8 }}
      animate={{ opacity: 1, scale: 1 }}
      transition={{ duration: 0.3 }}
    >
      {role.toUpperCase()}
    </motion.span>
  );
};

export default RoleBadge;
