/// <reference types="vitest" />
import { getViteConfig } from "astro/config";

export default getViteConfig({
  // @ts-expect-error - Vitest extends Astro's config shape with a test block
  test: {
    environment: "happy-dom",
    include: ["tests/**/*.test.ts"],
  },
});
