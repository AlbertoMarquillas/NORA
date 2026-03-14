# 01 - Frontend Project Initialization with React and Vite

This document describes the steps taken to initialize the `frontend/` module of the NORA system using React, Vite, and TypeScript. At this stage, **no configuration** of styles, components, websockets, or backend communication is performed. The goal is to set up a clean base environment for future development.

## Objective

Initialize a clean and modular environment for NORA's graphical interface using modern technologies (React + Vite) with JSX and TypeScript support.

## Expected Structure

The result of this stage is a base structure as follows:

```
frontend/
├── index.html
├── package.json
├── tsconfig.json
├── vite.config.ts
├── src/
│   ├── main.tsx
│   ├── App.tsx
│   └── index.css
└── node_modules/
```

## Commands Used

From the root directory of the repository:

```bash
npm create vite@latest frontend -- --template react-ts
cd frontend
npm install
```

> The `react-ts` template was chosen to enable TypeScript support from the start.

## Outcome

* The base environment was successfully created.
* The `npm run dev` command was verified to launch a development server at `http://localhost:5173`.
* Tailwind CSS, components, and custom configurations have not been added yet.

## Next Steps

* Configure Tailwind CSS.
* Define the internal folder structure (`components/`, `views/`, `state/`, etc.).
* Integrate WebSocket and FSM state updates.
* Begin development of visual components and backend interaction.
