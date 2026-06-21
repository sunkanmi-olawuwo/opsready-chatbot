import { apiPost } from "./apiClient";
import { ChatResponse } from "../types/chat";

export type ChatRequest = {
  question: string;
  prompt_version: string;
  top_k: number;
};

export function askCopilot(request: ChatRequest): Promise<ChatResponse> {
  return apiPost<ChatResponse>("/api/chat", request);
}
