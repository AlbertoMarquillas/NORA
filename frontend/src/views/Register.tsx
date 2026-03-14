import { useState } from "react";
import { motion } from "framer-motion";
import { Button } from "../ui/button";
import { AlertCircle, CheckCircle } from "lucide-react";
import { cn } from "@/lib/utils";
import Navbar from "../layout/Navbar";
import { useAuth } from "@/context/AuthContext";

interface RegisterProps {
  onRegister?: (
    username: string,
    email: string,
    password: string,
    confirmPassword: string
  ) => Promise<void>;
}

const Register = ({ onRegister }: RegisterProps = {}) => {
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [error, setError] = useState<string | null>(null);
  const [success, setSuccess] = useState<string | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const { register } = useAuth();


  const handleRegister = async (e: React.FormEvent) => {
    e.preventDefault();
    setError(null);
    setSuccess(null);
    setIsLoading(true);

    if (!username.trim()) {
      setError("Username is required");
      setIsLoading(false);
      return;
    }

    if (!email.includes("@")) {
      setError("Please enter a valid email address");
      setIsLoading(false);
      return;
    }

    if (password.length < 6) {
      setError("Password must be at least 6 characters");
      setIsLoading(false);
      return;
    }

    if (password !== confirmPassword) {
      setError("Passwords do not match");
      setIsLoading(false);
      return;
    }

    try {
      await register(username, email, password, confirmPassword);
      setSuccess("Account created successfully!");
      setUsername("");
      setEmail("");
      setPassword("");
      setConfirmPassword("");
      setTimeout(() => {
        window.location.href = "/login";
      }, 2000);
    } catch (err) {
      setError(
        err instanceof Error
          ? err.message
          : "Registration failed. Please try again."
      );
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-[#121212] text-white pt-24">
    <Navbar /> {}
    <motion.div
      className="min-h-screen w-full flex items-center justify-center bg-[#121212] p-4"
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      transition={{ duration: 0.5 }}
    >
      <motion.div
        className="w-full max-w-md p-8 space-y-8 bg-[#1a1a1a] rounded-xl shadow-2xl border border-gray-800"
        initial={{ scale: 0.9, y: 20 }}
        animate={{ scale: 1, y: 0 }}
        transition={{ delay: 0.2, duration: 0.4 }}
      >
        <div className="text-center">
          <motion.h2
            className="text-3xl font-bold text-white mb-2"
            initial={{ opacity: 0, y: -10 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.3, duration: 0.4 }}
          >
            <span className="text-cyan-400">NORA</span> Register
          </motion.h2>
          <motion.p
            className="text-gray-400"
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ delay: 0.4, duration: 0.4 }}
          >
            Create your account
          </motion.p>
        </div>

        {error && (
          <motion.div
            className="p-3 rounded-md bg-red-900/20 border border-red-800 text-red-200 flex items-center gap-2"
            initial={{ opacity: 0, height: 0 }}
            animate={{ opacity: 1, height: "auto" }}
            transition={{ duration: 0.3 }}
          >
            <AlertCircle className="h-4 w-4 text-red-400" />
            <span>{error}</span>
          </motion.div>
        )}

        {success && (
          <motion.div
            className="p-3 rounded-md bg-green-900/20 border border-green-800 text-green-200 flex items-center gap-2"
            initial={{ opacity: 0, height: 0 }}
            animate={{ opacity: 1, height: "auto" }}
            transition={{ duration: 0.3 }}
          >
            <CheckCircle className="h-4 w-4 text-green-400" />
            <span>{success}</span>
          </motion.div>
        )}

        <form onSubmit={handleRegister} className="space-y-6">
          <div className="space-y-2">
            <label
              htmlFor="username"
              className="block text-sm font-medium text-gray-300"
            >
              Username
            </label>
            <input
              id="username"
              name="username"
              type="text"
              autoComplete="username"
              required
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              className={cn(
                "w-full px-4 py-3 rounded-md bg-[#252525] border border-gray-700",
                "text-white placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-cyan-500/50 focus:border-cyan-500",
                "transition-all duration-200"
              )}
              placeholder="johndoe"
            />
          </div>

          <div className="space-y-2">
            <label
              htmlFor="email"
              className="block text-sm font-medium text-gray-300"
            >
              Email
            </label>
            <input
              id="email"
              name="email"
              type="email"
              autoComplete="email"
              required
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              className={cn(
                "w-full px-4 py-3 rounded-md bg-[#252525] border border-gray-700",
                "text-white placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-cyan-500/50 focus:border-cyan-500",
                "transition-all duration-200"
              )}
              placeholder="you@example.com"
            />
          </div>

          <div className="space-y-2">
            <label
              htmlFor="password"
              className="block text-sm font-medium text-gray-300"
            >
              Password
            </label>
            <input
              id="password"
              name="password"
              type="password"
              autoComplete="new-password"
              required
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className={cn(
                "w-full px-4 py-3 rounded-md bg-[#252525] border border-gray-700",
                "text-white placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-cyan-500/50 focus:border-cyan-500",
                "transition-all duration-200"
              )}
              placeholder="••••••••"
            />
          </div>

          <div className="space-y-2">
            <label
              htmlFor="confirmPassword"
              className="block text-sm font-medium text-gray-300"
            >
              Confirm Password
            </label>
            <input
              id="confirmPassword"
              name="confirmPassword"
              type="password"
              autoComplete="new-password"
              required
              value={confirmPassword}
              onChange={(e) => setConfirmPassword(e.target.value)}
              className={cn(
                "w-full px-4 py-3 rounded-md bg-[#252525] border border-gray-700",
                "text-white placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-cyan-500/50 focus:border-cyan-500",
                "transition-all duration-200"
              )}
              placeholder="••••••••"
            />
          </div>

          <div>
            <Button
              type="submit"
              className="w-full py-6 bg-cyan-600 hover:bg-cyan-700 text-white font-medium rounded-md"
              disabled={isLoading}
            >
              {isLoading ? "Creating account..." : "Create account"}
            </Button>
          </div>
        </form>

        <div className="mt-6 text-center">
          <p className="text-gray-400">
            Already have an account?{" "}
            <a
              href="/login"
              className="text-cyan-400 hover:text-cyan-300 transition-colors"
            >
              Sign in
            </a>
          </p>
        </div>
      </motion.div>
    </motion.div>
    </div>
  );
};

export default Register;
