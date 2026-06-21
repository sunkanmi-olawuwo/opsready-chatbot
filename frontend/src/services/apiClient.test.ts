import { afterEach, describe, expect, it, vi } from "vitest";

import { apiGet, apiPost } from "./apiClient";

describe("apiClient", () => {
  afterEach(() => {
    vi.unstubAllGlobals();
  });

  it("parses successful GET responses", async () => {
    vi.stubGlobal(
      "fetch",
      vi.fn().mockResolvedValue({
        ok: true,
        json: async () => ({ status: "ok" })
      })
    );

    await expect(apiGet<{ status: string }>("/api/health")).resolves.toEqual({ status: "ok" });
  });

  it("throws for failed POST responses", async () => {
    vi.stubGlobal(
      "fetch",
      vi.fn().mockResolvedValue({
        ok: false,
        status: 500
      })
    );

    await expect(apiPost("/api/chat", { question: "test" })).rejects.toThrow("POST /api/chat failed with 500");
  });
});
