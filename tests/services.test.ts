import { describe, expect, it } from "vitest";
import { experimental_AstroContainer } from "astro/container";
import ServicesPage from "../src/pages/services.astro";

describe("Services page", () => {
  it("highlights booking details and focus areas", async () => {
    const container = await experimental_AstroContainer.create({
      site: new URL("https://www.tarasenko.dev"),
    });
    const result = await container.renderToString(ServicesPage);

    expect(result).toContain("Engineering Sessions & Agentic Delivery");
    expect(result).toContain("€200/hr");
    expect(result).toContain("iOS Engineering");
    expect(result).toContain("Agentic Automation");
    expect(result).toContain("Developer Tooling");
  });
});
