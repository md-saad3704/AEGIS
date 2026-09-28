import { Panel } from '../common/Panel'
import { formatPercent } from '../../utils/format'

export function RouteProgressPanel({ route }) {
  return (
    <Panel title="Active route" eyebrow={route.name}>
      <div className="route-endpoints">
        <div><span>Origin</span><strong>{route.origin}</strong></div>
        <div><span>Destination</span><strong>{route.destination}</strong></div>
      </div>
      <div className="progress-track" aria-label={`Route progress ${formatPercent(route.progressPercent / 100)}`}>
        <div className="progress-fill" style={{ width: `${route.progressPercent}%` }} />
      </div>
      <div className="route-meta">
        <span>{route.progressPercent}% complete</span>
        <span>{route.distanceRemainingKm} km remaining</span>
        <span>{route.intersectionsRemaining} intersections ahead</span>
      </div>
    </Panel>
  )
}
