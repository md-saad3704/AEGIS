const toneByStatus = {
  OPERATIONAL: 'success',
  AVAILABLE: 'success',
  ACTIVE: 'success',
  READY: 'success',
  VALIDATED: 'success',
  PASS: 'success',
  GREEN: 'success',
  CLEARED: 'muted',
  PENDING: 'warning',
  RED: 'danger',
  ERROR: 'danger',
  UNAVAILABLE: 'danger',
}

export function StatusBadge({ status }) {
  const normalized = String(status || 'UNKNOWN').toUpperCase()
  const tone = toneByStatus[normalized] || 'neutral'

  return <span className={`status-badge status-${tone}`}>{normalized}</span>
}
