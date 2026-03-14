# 05 - UI Components in NORA Frontend

This document describes the structure, design principles, and conventions used for the user interface components within the `frontend/` module of the NORA system. It focuses on the `components/ui/` directory and the utility system used for class management.

## Objective

Ensure a coherent, minimal, and accessible design language across the application by:

* Using atomic, reusable UI components
* Following Tailwind CSS and ShadCN patterns
* Managing class merging with `clsx` and `tailwind-merge`
* Supporting conditional styling via the `cn()` utility

---

## UI Component Directory: `src/components/ui/`

This directory includes base components like:

* `button.tsx`
* `card.tsx`
* `dropdown-menu.tsx`
* `avatar.tsx`
* `separator.tsx`
* `input.tsx` (optional)

These files either wrap Radix UI primitives or define foundational UI behaviors extended across the interface.

All components:

* Are fully typed with TypeScript
* Support variant styling (e.g., `variant="outline"`, `size="lg"`)
* Use `forwardRef` for compatibility with other libraries
* Accept `className` for custom overrides

---

## Styling with `clsx` and `tailwind-merge`

To manage dynamic Tailwind classes without redundancy or conflict, two libraries are used:

* `clsx`: handles conditional inclusion of classes
* `tailwind-merge`: resolves conflicts by keeping the last matching Tailwind class

These are combined in the custom utility `cn()`.

### `src/utils/cn.ts`

```ts
import { clsx } from "clsx";
import { twMerge } from "tailwind-merge";

export function cn(...inputs: any[]) {
  return twMerge(clsx(...inputs));
}
```

Usage example in any component:

```tsx
<div className={cn("bg-black", isActive && "text-cyan-400")} />
```

---

## Export Convention

To enable simplified imports like `@/utils`, a central file `src/utils/index.ts` is used:

```ts
export * from "./cn";
```

This allows any component to use:

```ts
import { cn } from "@/utils";
```

---

## Component Example: `button.tsx`

Wraps a Radix primitive (`Slot`) and defines multiple variants:

```tsx
export const buttonVariants = cva(
  "inline-flex items-center justify-center rounded-md text-sm font-medium",
  {
    variants: {
      variant: {
        default: "bg-cyan-600 text-white hover:bg-cyan-700",
        outline: "border border-gray-700 text-white",
        ghost: "text-cyan-400 hover:bg-gray-900"
      },
      size: {
        sm: "px-2 py-1 text-xs",
        md: "px-4 py-2",
        lg: "px-6 py-3 text-base"
      }
    },
    defaultVariants: {
      variant: "default",
      size: "md"
    }
  }
);
```

---

## Guidelines for Creating New UI Components

* Use Tailwind utility classes for layout and color
* Extend Radix UI primitives where available
* Export component as `forwardRef` with type-safe props
* Apply `cn()` to `className` wherever dynamic styling is used
* Keep components atomic: buttons, inputs, cards—not full forms or views

---

## Next Steps

* Document the use of shared layout (`Navbar`, `Footer`)
* Establish animation conventions for UI feedback (e.g. `motion.div` wrappers)
* Introduce dark/light theme switching (if needed)
* Integrate accessibility testing with `@axe-core/react` in future phases
