import { clsx } from "clsx";
import { twMerge } from "tailwind-merge";

/**
 * Merge Tailwind CSS classes with clsx logic and tailwind-merge deduplication.
 */
export function cn(...inputs: any[]) {
  return twMerge(clsx(...inputs));
}