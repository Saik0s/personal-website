/// <reference types="vitest" />
import { getViteConfig } from "astro/config";

const createViteConfig = getViteConfig({});

export default async (...args: Parameters<typeof createViteConfig>) => {
  const config = await createViteConfig(...args);
  return {
    ...config,
    test: {
      environment: "happy-dom",
      include: ["tests/**/*.test.ts"],
    },
  };
};
