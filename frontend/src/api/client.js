const DEFAULT_API_BASE_URL = 'http://127.0.0.1:5000'

function resolveApiBaseUrl() {
  const configured = import.meta.env.VITE_API_BASE_URL || DEFAULT_API_BASE_URL

  let parsed
  try {
    parsed = new URL(configured)
  } catch {
    throw new Error('VITE_API_BASE_URL must be a valid absolute URL.')
  }

  if (!['http:', 'https:'].includes(parsed.protocol)) {
    throw new Error('VITE_API_BASE_URL must use HTTP or HTTPS.')
  }

  return parsed.toString().replace(/\/$/, '')
}

const API_BASE_URL = resolveApiBaseUrl()

async function requestJson(path, options = {}) {
  const response = await fetch(`${API_BASE_URL}${path}`, {
    ...options,
    headers: {
      Accept: 'application/json',
      ...(options.headers || {}),
    },
  })

  if (!response.ok) {
    throw new Error(`API request failed with status ${response.status}`)
  }

  return response.json()
}

export function getHealth() {
  return requestJson('/api/health')
}

export function getDashboardSnapshot() {
  return requestJson('/api/dashboard')
}

export { API_BASE_URL }
