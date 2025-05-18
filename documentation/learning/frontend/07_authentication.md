# 07 - Authentication System (Learning Notes)

This note documents how I implemented the authentication system in the NORA frontend. It handles user login, session management, and role validation. The authentication is fully integrated with the React Context API and interacts with the backend via Axios.

---

## Why I Needed Authentication

NORA requires user roles to control which features are available (e.g., Admin Dashboard, chat history, settings). I also needed a way to identify who was interacting with the system and provide different interfaces for guests, users, and admins.

---

## What I Implemented

### 1. Created `AuthContext`

The context exposes user info, authentication status, and login/logout functions.

```tsx
// context/AuthContext.tsx
interface User {
  name: string;
  email: string;
  avatar?: string;
  role: "admin" | "user" | "guest";
}

interface AuthContextType {
  user: User | null;
  isAuthenticated: boolean;
  isAdmin: boolean;
  isGuest: boolean;
  login: (email: string, password: string) => Promise<void>;
  logout: () => Promise<void>;
  fetchUser: () => Promise<void>;
  loading: boolean;
}
```

### 2. Managed Tokens in LocalStorage

* After login, I store `accessToken` and `refreshToken` in `localStorage`
* I use these to fetch the current user from the backend: `/auth/me`

```tsx
localStorage.setItem("accessToken", data.access);
localStorage.setItem("refreshToken", data.refresh);
```

### 3. Fetching User Data

I call `fetchUser()` on app load to check if a user is already logged in:

```tsx
useEffect(() => {
  fetchUser().finally(() => setLoading(false));
}, []);
```

### 4. Login Function

Sends email and password to backend. Parses role from response:

```tsx
const login = async (email, password) => {
  const res = await api.post("/auth/login/", { username_or_email: email, password });
  const data = res.data;
  setUser({
    name: data.username,
    email: data.email,
    avatar: data.avatar ?? null,
    role: data.is_admin ? "admin" : data.is_guest ? "guest" : "user",
  });
};
```

### 5. Logout Function

Clears tokens and resets user:

```tsx
const logout = async () => {
  try {
    await api.post("/auth/logout/", { refresh: localStorage.getItem("refreshToken") });
  } finally {
    setUser(null);
    localStorage.clear();
  }
};
```

### 6. Role Utilities

I defined helpers to simplify usage:

```tsx
const isAuthenticated = !!user && user.role !== "guest";
const isAdmin = user?.role === "admin";
const isGuest = user?.role === "guest" || !user;
```

These help conditionally render parts of the UI or protect routes.

---

## What I Learned

* React Context is enough for authentication (no need for Zustand here)
* Managing JWTs in `localStorage` works, but may later need refresh logic
* Separating user roles in the context simplifies access control logic in components

---

## To Do

* Auto-refresh access token when expired
* Add `register()` logic
* Add `/auth/refresh` endpoint handling
* Add UI feedback on invalid credentials
* Redirect from `/login` if already authenticated

---

Authentication now works and supports login, logout, guest detection, and role-based behavior. The system is extensible and cleanly integrated with the routing logic.
