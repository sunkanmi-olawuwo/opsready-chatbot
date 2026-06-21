const modules = [
  "Plan and prepare a GenAIOps solution",
  "Manage prompts for agents in Microsoft Foundry with GitHub",
  "Evaluate and optimize AI agents through structured experiments",
  "Automate AI evaluations with Microsoft Foundry and GitHub Actions",
  "Monitor your generative AI application",
  "Analyze and debug your generative AI app with tracing"
];

export function LearningPathPage() {
  return (
    <section className="page-stack">
      <div className="page-intro">
        <div>
          <span className="eyebrow">Microsoft Learn sync</span>
          <h2>Operationalize generative AI applications</h2>
        </div>
        <span className="status-pill">6 modules</span>
      </div>
      <div className="learning-list">
        {modules.map((module, index) => (
          <div className="learning-item" key={module}>
            <span>{String(index + 1).padStart(2, "0")}</span>
            <strong>{module}</strong>
            <small>{index === 0 ? "In progress" : "Planned evidence"}</small>
          </div>
        ))}
      </div>
    </section>
  );
}
