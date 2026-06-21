export type Citation = {
  title: string;
  source: string;
  chunk_id: string;
  score: number;
  provider: string;
};

export type ChatMetadata = {
  model: string;
  prompt_version: string;
  agent_provider: string;
  knowledge_provider: string;
  latency_ms: number;
  knowledge_latency_ms: number;
  agent_latency_ms: number;
  input_tokens: number;
  output_tokens: number;
  trace_id: string;
};

export type ChatResponse = {
  answer: string;
  citations: Citation[];
  metadata: ChatMetadata;
};
