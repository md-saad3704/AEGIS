import { getDashboardSnapshot } from '../../api/client'

export const apiDashboardAdapter = {
  async getSnapshot() {
    return getDashboardSnapshot()
  },
}
