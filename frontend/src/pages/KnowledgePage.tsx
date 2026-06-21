import { Database, FileSearch, HardDrive, SearchCheck } from "lucide-react";
import { useEffect, useState } from "react";

import { apiGet } from "../services/apiClient";

type KnowledgeSource = {
  title: string;
  source: string;
  provider: string;
  chunk_count: number;
  status: string;
  target: string;
};

export function KnowledgePage() {
  const [sources, setSources] = useState<KnowledgeSource[]>([]);

  useEffect(() => {
    apiGet<{ sources: KnowledgeSource[] }>("/api/knowledge/sources").then((payload) => setSources(payload.sources));
  }, []);

  return (
    <section className="page-stack">
      <div className="page-intro">
        <div>
          <span className="eyebrow">Knowledge operations</span>
          <h2>Grounding sources</h2>
        </div>
        <div className="intro-metrics">
          <div><span>Provider</span><strong>Local</strong></div>
          <div><span>Target</span><strong>Foundry</strong></div>
          <div><span>Backing</span><strong>Azure Search</strong></div>
        </div>
      </div>
      <div className="metric-grid">
        <div className="metric accent-teal"><Database size={18} /><span>Sources</span><strong>{sources.length}</strong></div>
        <div className="metric accent-amber"><FileSearch size={18} /><span>Chunks</span><strong>{sources.reduce((sum, source) => sum + source.chunk_count, 0)}</strong></div>
        <div className="metric accent-blue"><HardDrive size={18} /><span>Cloud source</span><strong>Blob</strong></div>
        <div className="metric accent-rose"><SearchCheck size={18} /><span>Retrieval</span><strong>File search</strong></div>
      </div>
      <section className="panel">
        <div className="table headered-table">
          <div className="table-row table-head">
            <span>Title</span>
            <span>Source</span>
            <span>Chunks</span>
            <span>Provider</span>
          </div>
          {sources.map((source) => (
            <div className="table-row" key={source.source}>
              <strong>{source.title}</strong>
              <span>{source.source}</span>
              <span>{source.chunk_count}</span>
              <span className="badge neutral">{source.provider}</span>
            </div>
          ))}
        </div>
      </section>
    </section>
  );
}
