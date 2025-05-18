/**
 * Utility module to centralize access to environment variables.
 * Ensures type safety and fallback handling where necessary.
 */

const getEnv = (key: string, fallback?: string): string => {
  const value = import.meta.env[key];
  if (!value && fallback === undefined) {
    throw new Error(`Environment variable ${key} is not defined`);
  }
  return value ?? fallback!;
};

// Exported constants
export const BACKEND_URL = getEnv('VITE_BACKEND_URL');
export const WS_URL = getEnv('VITE_WS_URL');
