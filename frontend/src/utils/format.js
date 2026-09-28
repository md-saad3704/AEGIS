export function formatEta(seconds) {
  if (!Number.isFinite(seconds)) return '—'
  if (seconds < 60) return `${Math.round(seconds)}s`
  const minutes = Math.floor(seconds / 60)
  const remainder = Math.round(seconds % 60)
  return `${minutes}m ${String(remainder).padStart(2, '0')}s`
}

export function formatPercent(value) {
  if (!Number.isFinite(value)) return '—'
  return `${Math.round(value * 100)}%`
}

export function formatCoordinate(value) {
  if (!Number.isFinite(value)) return '—'
  return value.toFixed(4)
}
