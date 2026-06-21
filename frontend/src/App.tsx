import { ReactNode, useState } from "react";

import { AppShell, PageKey } from "./components/layout/AppShell";
import { ChatPage } from "./pages/ChatPage";
import { EvaluationsPage } from "./pages/EvaluationsPage";
import { KnowledgePage } from "./pages/KnowledgePage";
import { LearningPathPage } from "./pages/LearningPathPage";
import { MonitoringPage } from "./pages/MonitoringPage";
import { PromptLabPage } from "./pages/PromptLabPage";
import { TracesPage } from "./pages/TracesPage";

const pages: Record<PageKey, ReactNode> = {
  chat: <ChatPage />,
  knowledge: <KnowledgePage />,
  prompts: <PromptLabPage />,
  evaluations: <EvaluationsPage />,
  monitoring: <MonitoringPage />,
  traces: <TracesPage />,
  learning: <LearningPathPage />
};

export function App() {
  const [page, setPage] = useState<PageKey>("chat");
  return (
    <AppShell activePage={page} onPageChange={setPage}>
      {pages[page]}
    </AppShell>
  );
}
