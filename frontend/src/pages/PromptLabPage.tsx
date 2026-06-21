import { Braces, GitCommitHorizontal, SplitSquareVertical } from "lucide-react";

export function PromptLabPage() {
  return (
    <section className="page-stack">
      <div className="page-intro">
        <div>
          <span className="eyebrow">Prompt management</span>
          <h2>Versioned agent instructions</h2>
        </div>
        <span className="status-pill">Git-backed</span>
      </div>
      <div className="page-grid">
        <div className="panel prompt-card">
          <GitCommitHorizontal size={20} />
          <span className="eyebrow">Baseline</span>
          <h3>support_answer_v1</h3>
          <p>Concise grounded answer behavior with source awareness.</p>
        </div>
        <div className="panel prompt-card">
          <SplitSquareVertical size={20} />
          <span className="eyebrow">Experiment</span>
          <h3>support_answer_v2</h3>
          <p>Structured answer format prepared for evaluation comparison.</p>
        </div>
      </div>
      <div className="panel code-panel">
        <div className="rail-title"><Braces size={16} /><strong>Instruction preview</strong></div>
        <pre>{`Rules:
  - use retrieved knowledge only
  - cite relevant sources
  - refuse unsupported details
  - capture prompt version in metadata`}</pre>
      </div>
    </section>
  );
}
