import { BadgeCheck, GitCompare, Gauge, TestTube2 } from "lucide-react";

export function EvaluationsPage() {
  return (
    <section className="page-stack">
      <div className="page-intro">
        <div>
          <span className="eyebrow">Structured experiments</span>
          <h2>Evaluation dashboard</h2>
        </div>
        <span className="status-pill amber">Foundry evaluators planned</span>
      </div>
      <div className="metric-grid">
        <div className="metric accent-teal"><TestTube2 size={18} /><span>Dataset</span><strong>5 cases</strong></div>
        <div className="metric accent-blue"><Gauge size={18} /><span>Groundedness</span><strong>Queued</strong></div>
        <div className="metric accent-amber"><BadgeCheck size={18} /><span>Citations</span><strong>Queued</strong></div>
        <div className="metric accent-rose"><GitCompare size={18} /><span>Prompt compare</span><strong>2 versions</strong></div>
      </div>
      <section className="panel">
        <div className="table headered-table">
          <div className="table-row eval-row table-head">
            <span>Run</span>
            <span>Prompt</span>
            <span>Quality</span>
            <span>Status</span>
          </div>
          <div className="table-row eval-row">
            <strong>local-placeholder</strong>
            <span>support_answer_v1</span>
            <span>Baseline pending</span>
            <span className="badge amber">Scaffolded</span>
          </div>
        </div>
      </section>
    </section>
  );
}
