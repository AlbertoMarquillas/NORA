import * as React from "react"
import { Switch as RadixSwitch, SwitchThumb } from "@radix-ui/react-switch"
import { cn } from "@/lib/utils"

const Switch = React.forwardRef<
  React.ElementRef<typeof RadixSwitch>,
  React.ComponentPropsWithoutRef<typeof RadixSwitch>
>(({ className, ...props }, ref) => (
  <RadixSwitch
    ref={ref}
    className={cn(
      "peer inline-flex h-5 w-9 shrink-0 cursor-pointer items-center rounded-full border-2 border-transparent shadow-sm transition-colors hover:ring-1 hover:ring-cyan-300 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-cyan-500 focus-visible:ring-offset-2 focus-visible:ring-offset-background disabled:cursor-not-allowed disabled:opacity-50 data-[state=checked]:bg-cyan-500 data-[state=unchecked]:bg-gray-700",
      className
    )}
    {...props}
  >
    <SwitchThumb
      className={cn(
        "pointer-events-none block h-4 w-4 rounded-full bg-white shadow-lg ring-0 transition-transform duration-300 ease-in-out data-[state=checked]:translate-x-4 data-[state=unchecked]:translate-x-0"
      )}
    />
  </RadixSwitch>
))

Switch.displayName = "Switch"
export { Switch }
