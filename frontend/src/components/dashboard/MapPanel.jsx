import { Panel } from '../common/Panel'
import { formatCoordinate } from '../../utils/format'

function projectPoint(point, bounds) {
  const x = ((point.longitude - bounds.minLng) / (bounds.maxLng - bounds.minLng)) * 100
  const y = 100 - ((point.latitude - bounds.minLat) / (bounds.maxLat - bounds.minLat)) * 100
  return { x, y }
}

export function MapPanel({ map }) {
  const points = map.route
  const bounds = {
    minLat: Math.min(...points.map((point) => point.latitude), map.vehicle.latitude) - 0.001,
    maxLat: Math.max(...points.map((point) => point.latitude), map.vehicle.latitude) + 0.001,
    minLng: Math.min(...points.map((point) => point.longitude), map.vehicle.longitude) - 0.001,
    maxLng: Math.max(...points.map((point) => point.longitude), map.vehicle.longitude) + 0.001,
  }
  const vehicle = projectPoint(map.vehicle, bounds)
  const routePath = points.map((point) => projectPoint(point, bounds))

  return (
    <Panel title="Corridor map" eyebrow="Map integration boundary" className="map-panel">
      <div className="map-stage" role="img" aria-label="Simulation map showing vehicle and route intersections">
        <svg viewBox="0 0 100 100" preserveAspectRatio="none" aria-hidden="true">
          <polyline points={routePath.map((point) => `${point.x},${point.y}`).join(' ')} className="map-route" />
          {routePath.map((point, index) => (
            <circle key={points[index].id} cx={point.x} cy={point.y} r="1.8" className={`map-node map-node-${points[index].status.toLowerCase()}`} />
          ))}
          <circle cx={vehicle.x} cy={vehicle.y} r="2.8" className="map-vehicle" />
        </svg>
        <div className="map-legend">
          <span><i className="legend-dot vehicle" /> Emergency vehicle</span>
          <span><i className="legend-dot route" /> Route</span>
          <span><i className="legend-dot intersection" /> Intersection</span>
        </div>
      </div>
      <div className="coordinate-row">
        <span>Vehicle latitude {formatCoordinate(map.vehicle.latitude)}</span>
        <span>Vehicle longitude {formatCoordinate(map.vehicle.longitude)}</span>
        <span>Provider: not configured</span>
      </div>
    </Panel>
  )
}
