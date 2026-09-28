import { useCallback, useEffect, useState } from 'react'
import {
  dashboardDataMode,
  getDashboardSnapshot,
} from '../services/dashboardService'

export function useDashboardData() {
  const [data, setData] = useState(null)
  const [status, setStatus] = useState('loading')
  const [error, setError] = useState(null)

  const refresh = useCallback(async () => {
    setStatus('loading')
    setError(null)

    try {
      const snapshot = await getDashboardSnapshot()
      setData(snapshot)
      setStatus('ready')
    } catch (requestError) {
      setStatus('error')
      setError(
        requestError instanceof Error
          ? requestError
          : new Error('Unable to load dashboard data.'),
      )
    }
  }, [])

  useEffect(() => {
    let cancelled = false

    async function loadDashboard() {
      try {
        const snapshot = await getDashboardSnapshot()

        if (cancelled) {
          return
        }

        setData(snapshot)
        setStatus('ready')
        setError(null)
      } catch (requestError) {
        if (cancelled) {
          return
        }

        setStatus('error')
        setError(
          requestError instanceof Error
            ? requestError
            : new Error('Unable to load dashboard data.'),
        )
      }
    }

    loadDashboard()

    return () => {
      cancelled = true
    }
  }, [])

  return {
    data,
    status,
    error,
    refresh,
    sourceMode: dashboardDataMode,
  }
}