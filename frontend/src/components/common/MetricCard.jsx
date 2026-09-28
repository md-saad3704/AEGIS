export function MetricCard({ label, value, detail, status }) {
  return (
    <article className="metric-card">
      <p className="metric-label">{label}</p>
      <div className="metric-value-row">
        <strong>{value}</strong>
        {status}
      </div>
      {detail && <p className="metric-detail">{detail}</p>}
    </article>
  )
}
