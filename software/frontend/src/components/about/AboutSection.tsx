import React from "react";

interface AboutSectionProps {
  title?: string;
  description?: string;
}

const AboutSection = ({
  title = "What is NORA?",
  description = "NORA is a sleek physical AI assistant that seamlessly integrates into your environment, providing intelligent support while maintaining a minimalist aesthetic and respecting your physical space.",
}: AboutSectionProps) => {
  return (
    <section className="w-full py-16 px-4 md:px-8 bg-black text-white">
      <div className="max-w-4xl mx-auto">
        <h2 className="text-3xl md:text-4xl font-bold mb-6 text-center">
          {title}
        </h2>
        <p className="text-lg md:text-xl text-gray-300 leading-relaxed text-center max-w-3xl mx-auto">
          {description}
        </p>
      </div>
    </section>
  );
};

export default AboutSection;
