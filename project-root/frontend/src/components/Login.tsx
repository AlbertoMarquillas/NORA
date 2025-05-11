import { useState } from "react";
import { motion } from "framer-motion";
import { Button } from "./ui/button";
import { AlertCircle } from "lucide-react";
import { cn } from "@/lib/utils";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";



interface LoginProps {
  onLogin?: (email: string, password: string) => Promise<void>;
}

const Login = ({ onLogin }: LoginProps = {}) => {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState<string | null>(null);
    const [isLoading, setIsLoading] = useState(false);
    const navigate = useNavigate();
    const { login } = useAuth();

    const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault();
    setError(null);
    setIsLoading(true);

    try {
        await login(email, password); // Llama a tu login real
        navigate("/"); // Redirige al home
    } catch (err) {
        setError(
        err instanceof Error ? err.message : "Login failed. Please try again."
        );
    } finally {
        setIsLoading(false);
    }
    };

    return (
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
                <span className="text-cyan-400">NORA</span> Login
            </motion.h2>
            <motion.p
                className="text-gray-400"
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                transition={{ delay: 0.4, duration: 0.4 }}
            >
                Sign in to your account
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

            <form onSubmit={handleLogin} className="space-y-6">
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
                    "transition-all duration-200",
                )}
                placeholder="you@example.com"
                />
            </div>

            <div className="space-y-2">
                <div className="flex justify-between">
                <label
                    htmlFor="password"
                    className="block text-sm font-medium text-gray-300"
                >
                    Password
                </label>
                <a
                    href="#"
                    className="text-sm text-cyan-400 hover:text-cyan-300 transition-colors"
                >
                    Forgot password?
                </a>
                </div>
                <input
                id="password"
                name="password"
                type="password"
                autoComplete="current-password"
                required
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                className={cn(
                    "w-full px-4 py-3 rounded-md bg-[#252525] border border-gray-700",
                    "text-white placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-cyan-500/50 focus:border-cyan-500",
                    "transition-all duration-200",
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
                {isLoading ? "Signing in..." : "Sign in"}
                </Button>
            </div>
            </form>

            <div className="mt-6 text-center">
            <p className="text-gray-400">
                Don't have an account?{" "}
                <a
                href="#"
                className="text-cyan-400 hover:text-cyan-300 transition-colors"
                >
                Sign up
                </a>
            </p>
            </div>
        </motion.div>
        </motion.div>
    );
};

export default Login;
