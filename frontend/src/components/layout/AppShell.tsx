import {
  Activity,
  BadgeCheck,
  Bot,
  BrainCircuit,
  ChartNoAxesCombined,
  ChevronRight,
  Database,
  GitBranch,
  MessageSquareText,
  Search,
  ShieldCheck,
  Sparkles
} from "lucide-react";
import { ReactNode } from "react";

export type PageKey = "chat" | "knowledge" | "prompts" | "evaluations" | "monitoring" | "traces" | "learning";

type NavItem = {
  key: PageKey;
  label: string;
  icon: ReactNode;
};

const navItems: NavItem[] = [
  { key: "chat", label: "Chat", icon: <MessageSquareText size={18} /> },
  { key: "knowledge", label: "Knowledge", icon: <Search size={18} /> },
  { key: "prompts", label: "Prompt Lab", icon: <BrainCircuit size={18} /> },
  { key: "evaluations", label: "Evaluations", icon: <ChartNoAxesCombined size={18} /> },
  { key: "monitoring", label: "Monitoring", icon: <Activity size={18} /> },
  { key: "traces", label: "Traces", icon: <GitBranch size={18} /> },
  { key: "learning", label: "Learning Path", icon: <Sparkles size={18} /> }
];

type AppShellProps = {
  activePage: PageKey;
  onPageChange: (page: PageKey) => void;
  children: ReactNode;
};

export function AppShell({ activePage, onPageChange, children }: AppShellProps) {
  return (
    <div className="app-shell">
      <aside className="sidebar">
        <div className="brand">
          <div className="brand-mark">
            <Bot size={22} />
          </div>
          <div>
            <strong>GenAIOps</strong>
            <span>Support Copilot</span>
          </div>
        </div>
        <div className="environment-card">
          <div>
            <span className="mini-label">Runtime</span>
            <strong>Local adapter</strong>
          </div>
          <BadgeCheck size={18} />
        </div>
        <nav className="nav-list" aria-label="Main navigation">
          {navItems.map((item) => (
            <button
              key={item.key}
              className={item.key === activePage ? "nav-item active" : "nav-item"}
              type="button"
              onClick={() => onPageChange(item.key)}
            >
              {item.icon}
              <span>{item.label}</span>
              <ChevronRight className="nav-chevron" size={16} />
            </button>
          ))}
        </nav>
        <div className="sidebar-status">
          <div className="status-row">
            <Database size={16} />
            <span>Knowledge: local</span>
          </div>
          <div className="status-row">
            <ShieldCheck size={16} />
            <span>Target: Foundry</span>
          </div>
        </div>
      </aside>
      <div className="workspace">
        <header className="topbar">
          <div>
            <span className="eyebrow">Microsoft Foundry Agents · Knowledge base grounding</span>
            <h1>Azure AI Search Support Copilot</h1>
          </div>
          <div className="topbar-actions">
            <a className="secondary-link" href="/wiki/README.md">Wiki</a>
            <div className="status-pill">Operational scaffold</div>
          </div>
        </header>
        <main className="content">{children}</main>
      </div>
    </div>
  );
}
