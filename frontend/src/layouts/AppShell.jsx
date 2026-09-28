const navigation = [
  { path: '/', label: 'Dashboard' },
  { path: '/simulation', label: 'Simulation' },
  { path: '/corridors', label: 'Corridors' },
]

export function AppShell({ path, navigate, children, sourceMode }) {
  return (
    <div className="app-shell">
      <aside className="sidebar">
        <div className="brand"><span className="brand-mark">A</span><div><strong>AEGIS</strong><small>Predictive green corridor</small></div></div>
        <nav aria-label="Primary navigation">
          {navigation.map((item) => (
            <button key={item.path} className={path === item.path ? 'nav-item active' : 'nav-item'} onClick={() => navigate(item.path)} type="button">
              {item.label}
            </button>
          ))}
        </nav>
        <div className="sidebar-footer"><span>Environment</span><strong>{sourceMode.toUpperCase()}</strong></div>
      </aside>
      <main className="main-content">
        <header className="topbar">
          <div><p className="eyebrow">AEGIS operations</p><h1>Predictive corridor dashboard</h1></div>
          <div className="simulation-badge">SIMULATION ONLY</div>
        </header>
        {children}
      </main>
    </div>
  )
}
