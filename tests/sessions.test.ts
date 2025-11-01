import { describe, expect, it } from "vitest";
import { experimental_AstroContainer } from "astro/container";
import SessionsPage from "../src/pages/sessions.astro";

describe("Sessions page", () => {
  it("highlights pricing, fit guidance, and focus areas", async () => {
    const container = await experimental_AstroContainer.create();
    const result = await container.renderToString(SessionsPage);

    expect(result).toContain("Engineering Sessions");
    expect(result).toContain("€200/hr");
    expect(result).toContain("Is This Right for You?");
    expect(result).toContain("What We Cover in Sessions");
    expect(result).toContain("iOS Engineering");
    expect(result).toContain("Agentic Automation");
    expect(result).toContain("Rapid Validation");
  });
});
