import { apiDashboardAdapter } from './adapters/apiDashboardAdapter'
import { mockDashboardAdapter } from './adapters/mockDashboardAdapter'

const mode = (import.meta.env.VITE_DASHBOARD_DATA_MODE || 'mock').toLowerCase()

const adapters = {
  api: apiDashboardAdapter,
  mock: mockDashboardAdapter,
}

export const dashboardDataMode = adapters[mode] ? mode : 'mock'
export const dashboardAdapter = adapters[dashboardDataMode]

export async function getDashboardSnapshot() {
  return dashboardAdapter.getSnapshot()
}
