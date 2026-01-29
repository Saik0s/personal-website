import { describe, expect, it } from "vitest";
import { experimental_AstroContainer } from "astro/container";
import SessionsPage from "../src/pages/sessions.astro";

describe("Sessions page", () => {
  it("routes visitors to the single consultancy offer", async () => {
    const container = await experimental_AstroContainer.create();
    const result = await container.renderToString(SessionsPage);

    expect(result).toContain("AI Shipping Consultancy");
    expect(result).toContain("This offer has moved.");
    expect(result).toContain("Book a Discovery Call");
    expect(result).toContain("/#offer");
  });
});
