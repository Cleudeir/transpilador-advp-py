import React, { useState, useEffect, useRef } from 'react';
import axios from 'axios';
import { 
  CheckCircle2, Rocket, Copy, RefreshCcw, 
  GitFork, ExternalLink, AlertCircle, 
  Upload, Download, FileCode, Cpu,
  Code2, Zap, Layout
} from 'lucide-react';

const API_URL = 'http://localhost:8040/api';

// ── Capabilities Data ──────────────────────────────────────────────────────────
const CAPABILITIES = [
  { label: 'DB Logic', desc: 'Table.go_top() → SA1->(DbGoTop())', icon: <Cpu size={14} /> },
  { label: 'UI Sync', desc: 'MsgAlert, MsgInfo, MsgYesNo mapping', icon: <Layout size={14} /> },
  { label: 'OOP / Methods', desc: 'METHOD mapping with self/:: syntax', icon: <Code2 size={14} /> },
  { label: 'Modern Python', desc: 'f-strings, list comprehension, loops', icon: <Zap size={14} /> },
];

const App: React.FC = () => {
  const [inputCode, setInputCode] = useState<string>(
    '# Exemplo de consulta Protheus em Python\n' +
    'from pyadvpl import Table\n' +
    'from pyadvpl import MsgAlert\n\n' +
    'def u_ConsultaCliente():\n' +
    '    SA1 = Table("SA1")\n' +
    '    SA1.go_top()\n\n' +
    '    if not SA1.eof():\n' +
    '        nome = SA1.A1_NOME\n' +
    '        MsgAlert(f"Cliente encontrado: {nome}")\n' +
    '    else:\n' +
    '        print("Nenhum cliente na base")\n\n' +
    '    return None'
  );
  const [outputCode, setOutputCode] = useState<string>('');
  const [isTranspiling, setIsTranspiling] = useState<boolean>(false);
  const [direction, setDirection] = useState<'advpl-to-python' | 'python-to-advpl'>('python-to-advpl');
  const [error, setError] = useState<string | null>(null);
  const [copied, setCopied] = useState(false);
  const fileInputRef = useRef<HTMLInputElement>(null);

  const handleTranspile = async () => {
    if (!inputCode.trim()) return;
    setIsTranspiling(true);
    setError(null);
    try {
      const response = await axios.post(`${API_URL}/transpile`, { code: inputCode, direction });
      if (response.data.success) {
        setOutputCode(response.data.output);
      } else {
        setError(response.data.error || 'Transpilation failed');
        setOutputCode('');
      }
    } catch (err: any) {
      setError(err.response?.data?.detail || 'API não disponível. Rode "pyadvpl serve" na porta 8040.');
      setOutputCode('');
    } finally {
      setIsTranspiling(false);
    }
  };

  useEffect(() => {
    const timer = setTimeout(handleTranspile, 600);
    return () => clearTimeout(timer);
  }, [inputCode, direction]);

  const copyToClipboard = () => {
    navigator.clipboard.writeText(outputCode);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  const toggleDirection = () => {
    setDirection(prev => prev === 'advpl-to-python' ? 'python-to-advpl' : 'advpl-to-python');
    setInputCode(outputCode || '');
    setOutputCode('');
  };

  const handleFileUpload = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;
    const reader = new FileReader();
    reader.onload = (re) => {
      setInputCode(re.target?.result as string);
    };
    reader.readAsText(file);
  };

  const downloadOutput = () => {
    const extension = direction === 'python-to-advpl' ? 'prw' : 'py';
    const blob = new Blob([outputCode], { type: 'text/plain' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `transpiled_code.${extension}`;
    a.click();
    URL.revokeObjectURL(url);
  };

  const srcLabel = direction === 'advpl-to-python' ? 'ADVPL' : 'Python';
  const dstLabel = direction === 'advpl-to-python' ? 'Python' : 'ADVPL';

  return (
    <div className="app">
      <div className="glow-bg"></div>

      <header className="main-header">
        <div className="logo-area">
          <div className="logo-icon"><Zap fill="currentColor" /></div>
          <div>
            <h1>Python <span>ADVPL</span></h1>
            <p>Modern Development Framework for Protheus</p>
          </div>
        </div>
        <div className="header-actions">
          <a href="https://github.com/Cleudeir/transpilador-advp-py" target="_blank" rel="noreferrer" className="github-link">
            <GitFork size={16} /> GitHub
          </a>
        </div>
      </header>

      <main className="dashboard">
        <section className="form-section">
          <div className="form-card glass">
            <div className="card-header">
              <div className="direction-toggle">
                <span className={direction === 'python-to-advpl' ? 'active' : ''}>Python</span>
                <button className="swap-btn" onClick={toggleDirection} title="Trocar Direção">
                  <RefreshCcw size={16} />
                </button>
                <span className={direction === 'advpl-to-python' ? 'active' : ''}>ADVPL</span>
              </div>
              <div className="file-actions">
                <button className="icon-btn" onClick={() => fileInputRef.current?.click()} title="Upload Arquivo">
                  <Upload size={18} />
                </button>
                <input type="file" ref={fileInputRef} onChange={handleFileUpload} style={{ display: 'none' }} accept=".py,.prw" />
              </div>
            </div>

            <div className="editors-grid">
              {/* Input Area */}
              <div className="editor-container">
                <div className="editor-label">Code Editor ({srcLabel})</div>
                <textarea 
                  value={inputCode} 
                  onChange={(e) => setInputCode(e.target.value)}
                  spellCheck={false}
                  placeholder={`Paste your ${srcLabel} code here...`}
                />
              </div>

              {/* Output Area */}
              <div className="editor-container">
                <div className="editor-label">
                  Generated Output ({dstLabel})
                  {isTranspiling && <span className="loader-dots">transpilando</span>}
                </div>
                <div className={`output-preview ${error ? 'error' : ''}`}>
                  {error ? (
                    <div className="error-msg">
                      <AlertCircle size={20} />
                      <p>{error}</p>
                    </div>
                  ) : (
                    <pre><code>{outputCode || 'O código transpilado aparecerá aqui...'}</code></pre>
                  )}
                </div>
                <div className="output-actions">
                  <button className="btn-secondary" onClick={copyToClipboard} disabled={!outputCode}>
                    <Copy size={16} /> {copied ? 'Copiado!' : 'Copiar'}
                  </button>
                  <button className="btn-primary" onClick={downloadOutput} disabled={!outputCode}>
                    <Download size={16} /> Exportar .{direction === 'python-to-advpl' ? 'prw' : 'py'}
                  </button>
                </div>
              </div>
            </div>
          </div>
        </section>

        <aside className="sidebar">
          <div className="info-card glass">
            <h3><Rocket size={18} /> Reusing Framework</h3>
            <p>Esta interface utiliza o pacote <code>pyadvpl</code> diretamente no backend via FastAPI, garantindo paridade total com a CLI.</p>
          </div>

          <div className="features-card glass">
            <h3>Capabilities</h3>
            <div className="cap-list">
              {CAPABILITIES.map((cap, i) => (
                <div key={i} className="cap-item">
                  <div className="cap-icon">{cap.icon}</div>
                  <div className="cap-text">
                    <strong>{cap.label}</strong>
                    <span>{cap.desc}</span>
                  </div>
                </div>
              ))}
            </div>
          </div>

          <div className="footer-links">
            <p>&copy; 2026 pyadvpl Framework</p>
            <p>Versão Engine: 2.5.0</p>
          </div>
        </aside>
      </main>

      <style>{`
        :root {
          --bg: #0a0b10;
          --card: rgba(20, 22, 32, 0.7);
          --accent: #6366f1;
          --accent-glow: rgba(99, 102, 241, 0.3);
          --text: #e2e8f0;
          --text-dim: #94a3b8;
          --success: #22c55e;
          --error: #ef4444;
          --border: rgba(255, 255, 255, 0.1);
        }

        .app {
          min-height: 100vh;
          background: var(--bg);
          color: var(--text);
          font-family: 'Inter', -apple-system, sans-serif;
          padding: 2rem;
          position: relative;
          overflow-x: hidden;
        }

        .glow-bg {
          position: fixed;
          top: -10%;
          right: -10%;
          width: 50%;
          height: 60%;
          background: radial-gradient(circle, var(--accent-glow) 0%, transparent 70%);
          z-index: 0;
          pointer-events: none;
        }

        .main-header {
          display: flex;
          justify-content: space-between;
          align-items: center;
          margin-bottom: 3rem;
          position: relative;
          z-index: 1;
        }

        .logo-area { display: flex; align-items: center; gap: 1rem; }
        .logo-icon { background: var(--accent); color: white; padding: 0.8rem; border-radius: 12px; box-shadow: 0 0 20px var(--accent-glow); }
        .logo-area h1 { font-size: 1.8rem; margin: 0; font-weight: 800; }
        .logo-area h1 span { color: var(--accent); }
        .logo-area p { margin: 0; color: var(--text-dim); font-size: 0.9rem; }

        .github-link { display: flex; align-items: center; gap: 0.5rem; color: var(--text-dim); text-decoration: none; padding: 0.5rem 1rem; border-radius: 8px; border: 1px solid var(--border); transition: all 0.2s; }
        .github-link:hover { color: white; border-color: var(--accent); background: rgba(255,255,255,0.05); }

        .dashboard {
          display: grid;
          grid-template-columns: 1fr 300px;
          gap: 2rem;
          position: relative;
          z-index: 1;
        }

        .glass {
          background: var(--card);
          backdrop-filter: blur(12px);
          border: 1px solid var(--border);
          border-radius: 20px;
          box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        }

        .form-card { display: flex; flex-direction: column; overflow: hidden; }
        
        .card-header {
          padding: 1.5rem;
          border-bottom: 1px solid var(--border);
          display: flex;
          justify-content: space-between;
          align-items: center;
        }

        .direction-toggle { display: flex; align-items: center; gap: 1.5rem; font-weight: 600; font-size: 1rem; }
        .direction-toggle span { color: var(--text-dim); }
        .direction-toggle span.active { color: var(--accent); text-shadow: 0 0 10px var(--accent-glow); }
        
        .swap-btn { background: rgba(255,255,255,0.05); border: 1px solid var(--border); color: white; padding: 0.6rem; border-radius: 50%; cursor: pointer; transition: all 0.3s; }
        .swap-btn:hover { background: var(--accent); transform: rotate(180deg); }

        .editors-grid {
          display: grid;
          grid-template-columns: 1fr 1fr;
          height: 600px;
        }

        .editor-container {
          display: flex;
          flex-direction: column;
          border-right: 1px solid var(--border);
        }

        .editor-label { padding: 0.8rem 1.5rem; font-size: 0.8rem; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; color: var(--text-dim); display: flex; justify-content: space-between; align-items: center; }

        textarea {
          flex: 1;
          background: transparent;
          border: none;
          color: #a5b4fc;
          padding: 1.5rem;
          font-family: 'Fira Code', monospace;
          font-size: 0.95rem;
          line-height: 1.6;
          resize: none;
          outline: none;
        }

        .output-preview {
          flex: 1;
          padding: 1.5rem;
          background: rgba(0,0,0,0.2);
          overflow-y: auto;
          font-family: 'Fira Code', monospace;
          font-size: 0.95rem;
          position: relative;
        }

        pre { margin: 0; white-space: pre-wrap; color: #818cf8; }

        .output-actions {
          padding: 1rem 1.5rem;
          display: flex;
          gap: 1rem;
          border-top: 1px solid var(--border);
        }

        .btn-primary, .btn-secondary {
          display: flex;
          align-items: center;
          gap: 0.5rem;
          padding: 0.8rem 1.5rem;
          border-radius: 10px;
          font-weight: 600;
          cursor: pointer;
          transition: all 0.2s;
          border: none;
        }

        .btn-primary { background: var(--accent); color: white; }
        .btn-primary:hover { transform: translateY(-2px); box-shadow: 0 5px 15px var(--accent-glow); }
        .btn-primary:disabled { background: #334155; transform: none; box-shadow: none; opacity: 0.5; }

        .btn-secondary { background: rgba(255,255,255,0.05); color: white; border: 1px solid var(--border); }
        .btn-secondary:hover { background: rgba(255,255,255,0.1); }

        .error-msg { color: var(--error); display: flex; gap: 1rem; align-items: center; background: rgba(239, 68, 68, 0.1); padding: 1.5rem; border-radius: 12px; }

        .sidebar { display: flex; flex-direction: column; gap: 1.5rem; }
        .sidebar .glass { padding: 1.5rem; }
        .sidebar h3 { margin: 0 0 1rem 0; display: flex; align-items: center; gap: 0.6rem; font-size: 1.1rem; }
        .sidebar code { background: rgba(0,0,0,0.3); padding: 0.2rem 0.4rem; border-radius: 4px; color: var(--accent); }

        .cap-list { display: flex; flex-direction: column; gap: 1rem; }
        .cap-item { display: flex; gap: 1rem; align-items: flex-start; }
        .cap-icon { color: var(--accent); background: var(--accent-glow); padding: 0.4rem; border-radius: 8px; }
        .cap-text strong { display: block; font-size: 0.9rem; }
        .cap-text span { font-size: 0.8rem; color: var(--text-dim); }

        .loader-dots::after {
          content: '...';
          animation: dots 1.5s infinite;
        }

        @keyframes dots {
          0% { content: '.'; }
          33% { content: '..'; }
          66% { content: '...'; }
        }

        @media (max-width: 1000px) {
          .dashboard { grid-template-columns: 1fr; }
          .editors-grid { grid-template-columns: 1fr; height: auto; }
          textarea { height: 300px; border-bottom: 1px solid var(--border); }
        }
      `}</style>
    </div>
  );
};

export default App;
