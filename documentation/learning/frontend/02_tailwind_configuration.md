# 02 - Tailwind CSS Configuration in the Frontend Project

This document explains the configuration process of **Tailwind CSS** in the frontend module of the NORA system. This step enables modern, utility-first styling for building a responsive, accessible, and visually clean interface.

## Objective

Configure Tailwind CSS within the Vite + React + TypeScript project to allow efficient and scalable frontend development.

## Steps Followed

### 1. Install Tailwind CSS and dependencies

From the `frontend/` directory:

```bash
npm install -D tailwindcss@3.4.1 postcss autoprefixer
npx tailwindcss init -p
```

This generates:

* `tailwind.config.js`
* `postcss.config.js`

### 2. Configure `tailwind.config.js`

```js
/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}"
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

### 3. Configure `postcss.config.js`

```js
export default {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
}
```

### 4. Update `src/index.css`

```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

### 5. Import styles in `src/main.tsx`

Make sure the CSS is loaded by importing it:

```tsx
import './index.css';
```

### 6. Test Tailwind CSS

Temporary content was added to `App.tsx`:

```tsx
function App() {
  return (
    <div className="min-h-screen bg-slate-900 text-white flex items-center justify-center">
      <h1 className="text-4xl font-bold">Tailwind CSS is working!</h1>
    </div>
  );
}

export default App;
```

Running `npm run dev` shows a full-screen dark background with centered text, confirming that Tailwind is properly configured.

## Outcome

* Tailwind CSS is successfully integrated.
* Utility classes are available throughout the project.
* Ready to begin modular UI development with a responsive design system.

## Next Steps

* Organize folder structure (`components/`, `views/`, etc.).
* Create base layout and navigation.
* Start implementing dynamic and role-sensitive views.
