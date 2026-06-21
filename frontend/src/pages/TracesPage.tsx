import { CheckCircle2, CircleDot, GitBranch, Timer } from "lucide-react";

export function TracesPage() {
  const steps = ["receive_request", "knowledge_search", "agent_response", "format_response"];

  return (
    <section className="page-stack">
      <div className="page-intro">
        <div>
          <span className="eyebrow">Debugging</span>
          <h2>Trace timeline</h2>
        </div>
        <span className="status-pill">OpenTelemetry-ready</span>
      </div>
      <section className="trace-board">
        <div className="trace-summary">
          <GitBranch size={20} />
          <div>
            <strong>local-trace-placeholder</strong>
            <span>Sample request timeline</span>
          </div>
        </div>
        <ol className="timeline">
          {steps.map((step, index) => (
            <li key={step}>
              {index < 3 ? <CheckCircle2 size={18} /> : <CircleDot size={18} />}
              <span>{step}</span>
              <small><Timer size={14} /> 0 ms</small>
            </li>
          ))}
        </ol>
      </section>
    </section>
  );
}
