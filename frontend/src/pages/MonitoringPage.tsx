import { Activity, CircleAlert, Coins, Timer } from "lucide-react";

export function MonitoringPage() {
  return (
    <section className="page-stack">
      <div className="page-intro">
        <div>
          <span className="eyebrow">Runtime health</span>
          <h2>Monitoring</h2>
        </div>
        <span className="status-pill">Local telemetry</span>
      </div>
      <div className="metric-grid">
        <div className="metric accent-teal"><Activity size={18} /><span>Requests</span><strong>0</strong></div>
        <div className="metric accent-blue"><Timer size={18} /><span>Avg latency</span><strong>0 ms</strong></div>
        <div className="metric accent-amber"><Coins size={18} /><span>Token usage</span><strong>0</strong></div>
        <div className="metric accent-rose"><CircleAlert size={18} /><span>Errors</span><strong>0</strong></div>
      </div>
      <section className="chart-surface">
        <div className="chart-bars" aria-hidden="true">
          {[42, 58, 36, 64, 51, 72, 47, 66, 54, 78, 61, 69].map((height, index) => (
            <span key={index} style={{ height: `${height}%` }} />
          ))}
        </div>
      </section>
    </section>
  );
}
