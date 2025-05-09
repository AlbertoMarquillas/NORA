import React from "react";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Eye, Layers, Box } from "lucide-react";

interface FeatureCardProps {
  title: string;
  description: string;
  icon: React.ReactNode;
}

const FeatureCard = ({ title, description, icon }: FeatureCardProps) => {
  return (
    <Card className="bg-zinc-900 border-zinc-800 text-white h-full transition-all duration-300 hover:border-cyan-500/50 hover:shadow-lg hover:shadow-cyan-500/10">
      <CardHeader>
        <div className="flex items-center justify-center w-12 h-12 rounded-full bg-cyan-500/20 mb-4">
          <div className="text-cyan-400">{icon}</div>
        </div>
        <CardTitle className="text-xl font-medium text-cyan-400">
          {title}
        </CardTitle>
      </CardHeader>
      <CardContent>
        <CardDescription className="text-zinc-400 text-sm">
          {description}
        </CardDescription>
      </CardContent>
    </Card>
  );
};

const FeatureCards = () => {
  const features = [
    {
      title: "Multimodal Perception",
      description:
        "NORA understands your environment through advanced visual and audio sensors, allowing for natural interactions without disrupting your space.",
      icon: <Eye size={24} />,
    },
    {
      title: "Contextual Adaptation",
      description:
        "Seamlessly adapts to your preferences and routines, learning from interactions to provide increasingly personalized assistance.",
      icon: <Layers size={24} />,
    },
    {
      title: "Physical Presence",
      description:
        "Unlike software-only assistants, NORA exists in your physical space with a thoughtfully designed form that complements your home or office.",
      icon: <Box size={24} />,
    },
  ];

  return (
    <section className="w-full py-16 px-4 bg-zinc-950" id="features">
      <div className="max-w-6xl mx-auto">
        <h2 className="text-3xl font-bold text-center mb-12 text-white">
          Key Features
        </h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          {features.map((feature, index) => (
            <FeatureCard
              key={index}
              title={feature.title}
              description={feature.description}
              icon={feature.icon}
            />
          ))}
        </div>
      </div>
    </section>
  );
};

export default FeatureCards;
