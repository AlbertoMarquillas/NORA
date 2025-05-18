# 06 - Routing

This note documents the process of setting up routing in the NORA frontend project using `react-router-dom`. It summarizes how I structured the routes, protected pages based on roles, and linked everything to the authentication context (`AuthContext`).

---

## Why I Added a Router

Since NORA supports multiple views (home, login, profile, admin, etc.), I needed a navigation system. I chose `react-router-dom` because it integrates well with React, supports route protection, and is widely used.

I created a folder `src/router/` to isolate routing logic. This keeps routing out of `App.tsx` and allows for easier maintenance.

---

## What I Did

### 1. Installed `react-router-dom`

```bash
npm install react-router-dom
```

### 2. Created `src/router/index.tsx`

This file defines the main route tree. I used `<Routes>` and `<Route>` from `react-router-dom`:

```tsx
import { Routes, Route } from "react-router-dom";
import Home from "@/views/Home";
import Login from "@/views/Login";
import Profile from "@/views/Profile";
import ProtectedRoute from "@/router/ProtectedRoute";

const AppRoutes = () => {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/login" element={<Login />} />
      <Route
        path="/profile"
        element={<ProtectedRoute allowedRoles={["admin", "user"]}><Profile /></ProtectedRoute>}
      />
    </Routes>
  );
};

export default AppRoutes;
```

### 3. Created `src/router/ProtectedRoute.tsx`

This component wraps views that require the user to be logged in and match a certain role:

```tsx
import { Navigate } from "react-router-dom";
import { useAuth } from "@/context/AuthContext";

const ProtectedRoute = ({ children, allowedRoles }) => {
  const { isAuthenticated, user } = useAuth();

  if (!isAuthenticated || !allowedRoles.includes(user?.role)) {
    return <Navigate to="/login" replace />;
  }

  return children;
};

export default ProtectedRoute;
```

### 4. Used It in `App.tsx`

I removed any logic from `App.tsx` and just returned `<AppRoutes />`:

```tsx
import AppRoutes from "@/router";

function App() {
  return <AppRoutes />;
}

export default App;
```

---

## What I Learned

* Routing can be centralized and still stay modular.
* Protecting routes based on roles is clean with wrapper components.
* Having routes outside of `App.tsx` keeps things cleaner.
* I will probably add a `NotFound.tsx` page and layout wrappers later.

---

## To Do

* Add `/admin` route and protect it with `allowedRoles={["admin"]}`
* Show a loading screen while auth context loads
* Add fallback route: `path="*"` → NotFound
* Eventually add layout wrappers with persistent `Navbar`

---

This system is working and easily extensible. I'm keeping it simple for now, but the architecture supports future features like redirects, nested routes, and role-based dashboards.
