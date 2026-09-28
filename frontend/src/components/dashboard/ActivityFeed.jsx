import { Panel } from '../common/Panel'

export function ActivityFeed({ activity }) {
  return (
    <Panel title="Activity" eyebrow="Recent simulation events">
      <ul className="activity-list">
        {activity.map((event, index) => (
          <li key={`${event.time}-${index}`}>
            <time>{event.time}</time>
            <div><strong>{event.level}</strong><span>{event.message}</span></div>
          </li>
        ))}
      </ul>
    </Panel>
  )
}
