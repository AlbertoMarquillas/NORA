# 03 - Environment Variables Setup in the Frontend Project

This document explains how environment variables are defined and used in the NORA frontend module. Setting up environment variables allows for clean configuration, separation of environment-specific values, and better deployment practices.

## Objective

Centralize configuration for runtime parameters like backend endpoints and WebSocket servers using `.env` files and Vite’s environment loading mechanism.

## Files Created

### `.env`

This file defines environment variables for local development. It should not be committed to version control:

```dotenv
VITE_BACKEND_URL=http://localhost:8000
VITE_WS_URL=ws://localhost:8000/ws
```

### `.env.example`

This file documents the required environment variables and can be safely committed:

```dotenv
# Base URL for REST API communication
VITE_BACKEND_URL=http://localhost:8000

# WebSocket endpoint for real-time events
VITE_WS_URL=ws://localhost:8000/ws
```

### `.gitignore`

Ensure that the `.env` file is excluded from the repository:

```gitignore
.env
```

## Access in Code

Vite exposes variables prefixed with `VITE_` via `import.meta.env`. To access them in the code, we use:

```ts
import.meta.env.VITE_BACKEND_URL
import.meta.env.VITE_WS_URL
```

## Utility Wrapper

To centralize access and add runtime validation, a utility module was created:

**File:** `src/utils/env.ts`

```ts
const getEnv = (key: string, fallback?: string): string => {
  const value = import.meta.env[key];
  if (!value && fallback === undefined) {
    throw new Error(`Environment variable ${key} is not defined`);
  }
  return value ?? fallback!;
};

export const BACKEND_URL = getEnv('VITE_BACKEND_URL');
export const WS_URL = getEnv('VITE_WS_URL');
```

This ensures that any missing required variable will produce a clear error message.

## Outcome

* Environment variables are now properly defined and separated.
* Runtime configuration (e.g., backend URLs) can easily be updated without modifying code.
* Code that relies on external endpoints imports them cleanly from `utils/env.ts`.

## Next Steps

* Create utilities for REST and WebSocket connections.
* Begin interaction with backend endpoints.
