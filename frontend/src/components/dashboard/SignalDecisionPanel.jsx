import { Panel } from '../common/Panel'
import { StatusBadge } from '../common/StatusBadge'

export function SignalDecisionPanel({ decision }) {
  return (
    <Panel title="Predictive signal decision" eyebrow={`Target ${decision.intersection}`} action={<StatusBadge status={decision.status} />}>
      <div className="decision-callout">
        <div>
          <span>Requested simulated state</span>
          <strong>{decision.requestedState}</strong>
        </div>
        <div>
          <span>Reason</span>
          <strong>{decision.reason}</strong>
        </div>
      </div>
      <p className="panel-note">No real-world traffic controller is contacted by this dashboard.</p>
    </Panel>
  )
}
