import { ActivityFeed } from '../components/dashboard/ActivityFeed'
import { IntersectionTable } from '../components/dashboard/IntersectionTable'
import { MapPanel } from '../components/dashboard/MapPanel'
import { RouteProgressPanel } from '../components/dashboard/RouteProgressPanel'
import { SafetyValidationPanel } from '../components/dashboard/SafetyValidationPanel'
import { SignalDecisionPanel } from '../components/dashboard/SignalDecisionPanel'
import { SystemStatusPanel } from '../components/dashboard/SystemStatusPanel'
import { VehicleStatusPanel } from '../components/dashboard/VehicleStatusPanel'
import { useDashboardData } from '../hooks/useDashboardData'

function LoadingState() {
  return <div className="state-card"><div className="spinner" /><strong>Loading dashboard state</strong><span>Preparing the configured data adapter.</span></div>
}

function ErrorState({ error, refresh }) {
  return <div className="state-card error-state"><strong>Dashboard data unavailable</strong><span>{error.message}</span><button type="button" onClick={refresh}>Retry</button></div>
}

export function DashboardPage() {
  const { data, status, error, refresh, sourceMode } = useDashboardData()

  if (status === 'loading') return <LoadingState />
  if (status === 'error') return <ErrorState error={error} refresh={refresh} />

  return (
    <div className="dashboard-page">
      <div className="dashboard-banner"><div><strong>Operational view</strong><span>Current state is {sourceMode === 'mock' ? 'simulated development data' : 'served by the configured API adapter'}.</span></div><button type="button" onClick={refresh}>Refresh</button></div>
      <div className="dashboard-grid">
        <SystemStatusPanel system={data.system} sourceMode={sourceMode} />
        <VehicleStatusPanel vehicle={data.vehicle} />
        <RouteProgressPanel route={data.route} />
        <MapPanel map={data.map} />
        <IntersectionTable intersections={data.intersections} />
        <SignalDecisionPanel decision={data.decision} />
        <SafetyValidationPanel safety={data.safety} />
        <ActivityFeed activity={data.activity} />
      </div>
    </div>
  )
}
