import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { describe, expect, it } from "vitest";

import { App } from "./App";

describe("App", () => {
  it("renders the operational dashboard shell", () => {
    render(<App />);

    expect(screen.getByRole("heading", { name: "Azure AI Search Support Copilot" })).toBeInTheDocument();
    expect(screen.getByRole("button", { name: "Chat" })).toBeInTheDocument();
    expect(screen.getByRole("heading", { name: "Grounded agent console" })).toBeInTheDocument();
  });

  it("navigates between dashboard pages", async () => {
    const user = userEvent.setup();
    render(<App />);

    await user.click(screen.getByRole("button", { name: "Evaluations" }));

    expect(screen.getByRole("heading", { name: "Evaluation dashboard" })).toBeInTheDocument();
    expect(screen.getByText("Foundry evaluators planned")).toBeInTheDocument();
  });
});
