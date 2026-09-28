import { Panel } from '../common/Panel'
import { StatusBadge } from '../common/StatusBadge'

export function SafetyValidationPanel({ safety }) {
  return (
    <Panel title="Safety validation" eyebrow="Pre-decision checks" action={<StatusBadge status={safety.status} />}>
      <ul className="check-list">
        {safety.checks.map((check) => (
          <li key={check.label}><span>{check.label}</span><StatusBadge status={check.status} /></li>
        ))}
      </ul>
    </Panel>
  )
}
