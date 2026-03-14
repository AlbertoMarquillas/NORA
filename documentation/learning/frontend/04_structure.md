# 04 - Folder Structure of the Frontend Project

This document describes the folder structure implemented in the `frontend/` module of the NORA system. It explains the purpose and functionality of each directory. The design follows a modular, scalable layout that aligns with the architectural principles of NORA.

## Objective

Define a consistent and extensible structure to support component-based development, backend communication, user state management, and role-specific rendering.

## Structure under `frontend/src/`

```
frontend/
├── assets/          → Static resources (images, icons, audio)
├── components/      → Reusable atomic UI components (buttons, loaders, cards)
├── context/         → React Context API logic (authentication, theme, etc.)
├── layout/          → Shared structural UI (Navbar, Footer, etc.)
├── lib/             → Utility functions (e.g., classnames, formatting helpers)
├── services/        → Axios clients, backend integration logic
├── state/           → Zustand store (FSM, session, interface state)
├── ui/              → UI components imported from ShadCN or extended locally
├── views/           → Role-specific or feature-based pages (Home, Login, Profile)
├── App.tsx          → Root component mounting all views
├── main.tsx         → Application entry point
├── index.css        → Global Tailwind styles
```

## Explanation of Key Folders

### `assets/`

Used for storing static files such as the NORA logo, placeholder avatars, and any visual/audio resources.

### `components/`

Contains pure and stateless UI blocks like custom buttons, feature cards, loading indicators, and layout fragments used across views.

### `context/`

Includes React Context Providers like `AuthContext.tsx`, which expose user and session data throughout the app. This abstracts authentication and permissions logic.

### `layout/`

Hosts major structural elements such as `Navbar`, layout containers, or modal wrappers used globally.

### `lib/`

Utility scripts like `cn.ts` (class name merging), formatters, or environment access helpers. These are foundational tools used in multiple parts of the app.

### `services/`

Axios clients for each backend route (e.g., `/auth`, `/fsm`, `/sensor`). Also includes wrappers for API interactions, socket listeners, etc.

### `state/`

Stores Zustand stores for FSM state, frontend display flags, or any other transient global state shared across components.

### `ui/`

Represents the extended or locally modified ShadCN components like `button.tsx`, `dropdown-menu.tsx`, `avatar.tsx`, ensuring design consistency.

### `views/`

Contains complete views or pages: `Home.tsx`, `Login.tsx`, `Profile.tsx`, `AdminDashboard.tsx`, etc. Each one renders complete user-facing interfaces based on role or action.

## Integration with Backend

All data flows through REST API or WebSocket, managed by modules in `services/`. State related to user, FSM, or agents is synchronized with backend events.

## Final Notes

* Each folder has a **clear purpose** and boundaries.
* Design is **modular**, **scalable**, and **role-aware**.
* Tailwind and Framer Motion are consistently used for layout and animation.
* Directory aliases (e.g. `@/views`) are resolved via `vite.config.ts`.

This structure enables efficient team collaboration, predictable maintenance, and modular evolution of NORA's frontend.
