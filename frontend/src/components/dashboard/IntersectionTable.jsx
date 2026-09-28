import { Panel } from '../common/Panel'
import { StatusBadge } from '../common/StatusBadge'
import { formatEta, formatPercent } from '../../utils/format'

export function IntersectionTable({ intersections }) {
  return (
    <Panel title="Upcoming intersections" eyebrow="Predictive corridor">
      <div className="table-wrap">
        <table>
          <thead>
            <tr><th>Intersection</th><th>ETA</th><th>Signal</th><th>Priority</th><th>Traffic</th></tr>
          </thead>
          <tbody>
            {intersections.map((intersection) => (
              <tr key={intersection.id}>
                <td><strong>{intersection.id}</strong><span>{intersection.name}</span></td>
                <td>{formatEta(intersection.etaSeconds)}</td>
                <td><StatusBadge status={intersection.signal} /></td>
                <td><StatusBadge status={intersection.priority} /></td>
                <td>{formatPercent(intersection.traffic)}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </Panel>
  )
}
