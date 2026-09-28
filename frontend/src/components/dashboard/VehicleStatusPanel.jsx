import { MetricCard } from '../common/MetricCard'
import { Panel } from '../common/Panel'
import { StatusBadge } from '../common/StatusBadge'
import { formatEta } from '../../utils/format'

export function VehicleStatusPanel({ vehicle }) {
  return (
    <Panel title="Emergency vehicle" eyebrow={vehicle.identifier} action={<StatusBadge status={vehicle.status} />}>
      <div className="metric-grid metric-grid-3">
        <MetricCard label="Vehicle type" value={vehicle.type} />
        <MetricCard label="Speed" value={`${vehicle.speedKph} km/h`} detail={`Heading ${vehicle.heading}°`} />
        <MetricCard label="Next ETA" value={formatEta(vehicle.etaSeconds)} detail="Simulation estimate" />
      </div>
    </Panel>
  )
}
