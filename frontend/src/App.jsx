import { AppShell } from './layouts/AppShell'
import { DashboardPage } from './pages/DashboardPage'
import { PlaceholderPage } from './pages/PlaceholderPage'
import { useRouter } from './hooks/useRouter'
import { dashboardDataMode } from './services/dashboardService'
import './App.css'

function App() {
  const { path, navigate } = useRouter()

  let page
  if (path === '/') {
    page = <DashboardPage />
  } else if (path === '/simulation') {
    page = <PlaceholderPage title="Simulation workspace" description="GPS movement and route progression are intentionally deferred to Phase 4." />
  } else if (path === '/corridors') {
    page = <PlaceholderPage title="Corridor workspace" description="Corridor lifecycle controls will be connected to backend services in a later phase." />
  } else {
    page = <PlaceholderPage title="Page not found" description="The requested AEGIS route does not exist." />
  }

  return <AppShell path={path} navigate={navigate} sourceMode={dashboardDataMode}>{page}</AppShell>
}

export default App
