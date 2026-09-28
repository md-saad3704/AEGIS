const mockSnapshot = {
  source: 'SIMULATION',
  generatedAt: '2026-09-28T10:00:00Z',
  system: {
    status: 'OPERATIONAL',
    mode: 'SIMULATION',
    backend: 'AVAILABLE',
    lastUpdate: 'Just now',
  },
  vehicle: {
    identifier: 'EV-001',
    type: 'AMBULANCE',
    status: 'ACTIVE',
    speedKph: 54,
    heading: 72,
    etaSeconds: 214,
  },
  route: {
    name: 'Emergency Route A',
    origin: 'Central Station',
    destination: 'City Medical Center',
    progressPercent: 62,
    distanceRemainingKm: 2.8,
    intersectionsRemaining: 4,
  },
  map: {
    center: { latitude: 28.6139, longitude: 77.209 },
    vehicle: { latitude: 28.6182, longitude: 77.2145 },
    route: [
      { id: 'I-01', latitude: 28.6205, longitude: 77.2115, status: 'CLEARED' },
      { id: 'I-02', latitude: 28.6189, longitude: 77.2132, status: 'ACTIVE' },
      { id: 'I-03', latitude: 28.6167, longitude: 77.2151, status: 'PENDING' },
      { id: 'I-04', latitude: 28.6148, longitude: 77.217, status: 'PENDING' },
    ],
  },
  intersections: [
    { id: 'I-01', name: 'North Junction', etaSeconds: 0, signal: 'GREEN', priority: 'CLEARED', traffic: 0.31 },
    { id: 'I-02', name: 'Central Avenue', etaSeconds: 38, signal: 'GREEN', priority: 'ACTIVE', traffic: 0.47 },
    { id: 'I-03', name: 'Hospital Road', etaSeconds: 96, signal: 'RED', priority: 'PENDING', traffic: 0.68 },
    { id: 'I-04', name: 'Medical Center Gate', etaSeconds: 172, signal: 'RED', priority: 'PENDING', traffic: 0.54 },
  ],
  decision: {
    status: 'READY',
    intersection: 'I-03',
    requestedState: 'GREEN',
    reason: 'Emergency priority window',
    confidence: null,
  },
  safety: {
    status: 'VALIDATED',
    checks: [
      { label: 'Route continuity', status: 'PASS' },
      { label: 'Intersection sequence', status: 'PASS' },
      { label: 'Priority conflict check', status: 'PASS' },
      { label: 'Simulation-only boundary', status: 'PASS' },
    ],
  },
  activity: [
    { time: '10:00:00', level: 'INFO', message: 'Simulation snapshot refreshed.' },
    { time: '09:59:42', level: 'INFO', message: 'I-02 marked as active priority intersection.' },
    { time: '09:59:12', level: 'INFO', message: 'Safety validation completed for the current corridor.' },
  ],
}

export const mockDashboardAdapter = {
  async getSnapshot() {
    return structuredClone(mockSnapshot)
  },
}
