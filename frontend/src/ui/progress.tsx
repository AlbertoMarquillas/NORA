import * as React from "react"
import * as ProgressPrimitive from "@radix-ui/react-progress"
import { cn } from "@/lib/utils"

const getColorByValue = (value: number) => {
  if (value >= 80) return "bg-red-500"
  if (value >= 50) return "bg-yellow-400"
  return "bg-cyan-500"
}

const Progress = React.forwardRef<
  React.ElementRef<typeof ProgressPrimitive.Root>,
  React.ComponentPropsWithoutRef<typeof ProgressPrimitive.Root> & { value: number }
>(({ className, value = 0, ...props }, ref) => (
  <ProgressPrimitive.Root
    ref={ref}
    className={cn(
      "relative h-2 w-full overflow-hidden rounded-full bg-gray-700",
      className
    )}
    {...props}
  >
    <ProgressPrimitive.Indicator
      className={cn("h-full transition-all", getColorByValue(value))}
      style={{ width: `${value}%` }}
    />
  </ProgressPrimitive.Root>
))
Progress.displayName = ProgressPrimitive.Root.displayName

export { Progress }
