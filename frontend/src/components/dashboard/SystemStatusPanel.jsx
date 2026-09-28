import { Panel } from '../common/Panel'
import { StatusBadge } from '../common/StatusBadge'

export function SystemStatusPanel({ system, sourceMode }) {
  return (
    <Panel title="System status" eyebrow="Control plane">
      <div className="status-grid">
        <div><span>System</span><StatusBadge status={system.status} /></div>
        <div><span>Backend</span><StatusBadge status={system.backend} /></div>
        <div><span>Mode</span><strong>{system.mode}</strong></div>
        <div><span>Data source</span><strong>{sourceMode.toUpperCase()}</strong></div>
      </div>
      <p className="panel-note">Simulation data is explicitly separated from future live API data.</p>
    </Panel>
  )
}
