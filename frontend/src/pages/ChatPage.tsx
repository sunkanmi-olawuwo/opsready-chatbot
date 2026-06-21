import { Clock3, Database, FileText, Loader2, Send, Sparkles, TerminalSquare } from "lucide-react";
import { FormEvent, useState } from "react";

import { askCopilot } from "../services/chatApi";
import { ChatResponse } from "../types/chat";

export function ChatPage() {
  const [question, setQuestion] = useState("How does this project use Microsoft Foundry Agents?");
  const [promptVersion, setPromptVersion] = useState("support_answer_v1");
  const [topK, setTopK] = useState(5);
  const [response, setResponse] = useState<ChatResponse | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [isLoading, setIsLoading] = useState(false);

  async function submit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    setIsLoading(true);
    setError(null);
    try {
      setResponse(await askCopilot({ question, prompt_version: promptVersion, top_k: topK }));
    } catch (caught) {
      setError(caught instanceof Error ? caught.message : "Unexpected request failure");
    } finally {
      setIsLoading(false);
    }
  }

  return (
    <section className="chat-workspace">
      <div className="page-intro">
        <div>
          <span className="eyebrow">Chat operations</span>
          <h2>Grounded agent console</h2>
        </div>
        <div className="intro-metrics">
          <div><span>Agent</span><strong>Local mock</strong></div>
          <div><span>Knowledge</span><strong>5 docs</strong></div>
          <div><span>Trace</span><strong>Enabled</strong></div>
        </div>
      </div>

      <div className="chat-layout">
        <form className="composer-surface" onSubmit={submit}>
          <div className="panel-heading compact-heading">
            <span className="eyebrow">Question</span>
            <h3>Ask the support agent</h3>
          </div>
          <textarea
            aria-label="Question"
            value={question}
            onChange={(event) => setQuestion(event.target.value)}
            rows={7}
          />
          <div className="control-row">
            <label>
              Prompt
              <select value={promptVersion} onChange={(event) => setPromptVersion(event.target.value)}>
                <option value="support_answer_v1">support_answer_v1</option>
                <option value="support_answer_v2">support_answer_v2</option>
              </select>
            </label>
            <label>
              Top K
              <input
                min={1}
                max={10}
                type="number"
                value={topK}
                onChange={(event) => setTopK(Number(event.target.value))}
              />
            </label>
          </div>
          <button className="primary-button" type="submit" disabled={isLoading}>
            {isLoading ? <Loader2 className="spin" size={18} /> : <Send size={18} />}
            Run grounded answer
          </button>
          {error ? <p className="error-text">{error}</p> : null}
        </form>

        <div className="answer-surface">
          <div className="answer-toolbar">
            <div>
              <span className="eyebrow">Agent response</span>
              <h3>Answer</h3>
            </div>
            <span className={response ? "run-state ready" : "run-state"}>{response ? "Completed" : "Waiting"}</span>
          </div>
          <div className="answer-body">
            {response ? (
              <p>{response.answer}</p>
            ) : (
              <div className="empty-state">
                <Sparkles size={26} />
                <strong>Ready for a grounded support query</strong>
                <span>Responses will include citations, latency, token counts, and a trace ID.</span>
              </div>
            )}
          </div>
        </div>

        <aside className="run-rail">
          <div className="rail-section">
            <div className="rail-title">
              <FileText size={16} />
              <strong>Citations</strong>
            </div>
            <div className="stack">
              {response?.citations.map((citation) => (
                <div className="citation" key={citation.chunk_id}>
                  <strong>{citation.title}</strong>
                  <span>{citation.source}</span>
                  <small>{citation.chunk_id} · score {citation.score}</small>
                </div>
              )) ?? <p className="muted">No citations yet.</p>}
            </div>
          </div>

          <div className="rail-section">
            <div className="rail-title">
              <TerminalSquare size={16} />
              <strong>Request metadata</strong>
            </div>
            {response ? (
              <dl className="metadata-grid">
                <dt>Model</dt><dd>{response.metadata.model}</dd>
                <dt>Agent</dt><dd>{response.metadata.agent_provider}</dd>
                <dt>Knowledge</dt><dd>{response.metadata.knowledge_provider}</dd>
                <dt>Trace</dt><dd>{response.metadata.trace_id}</dd>
              </dl>
            ) : (
              <p className="muted">Metadata appears after a run.</p>
            )}
          </div>

          <div className="rail-metrics">
            <div>
              <Clock3 size={16} />
              <span>Latency</span>
              <strong>{response ? `${response.metadata.latency_ms} ms` : "0 ms"}</strong>
            </div>
            <div>
              <Database size={16} />
              <span>Tokens</span>
              <strong>
                {response ? `${response.metadata.input_tokens}/${response.metadata.output_tokens}` : "0/0"}
              </strong>
            </div>
          </div>
        </aside>
      </div>
    </section>
  );
}
