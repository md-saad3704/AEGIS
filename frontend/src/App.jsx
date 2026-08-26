import { useState } from 'react'
import heroImg from './assets/hero.png'
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import { getHealth } from './api/client'
import './App.css'

function App() {
  const [count, setCount] = useState(0)
  const [health, setHealth] = useState(null)
  const [healthError, setHealthError] = useState(null)

  async function checkBackend() {
    try {
      setHealthError(null)
      const data = await getHealth()
      setHealth(data)
    } catch (error) {
      setHealth(null)
      setHealthError(error.message)
    }
  }

  return (
    <>
      <section id="center">
        <div className="hero">
          <img className="base" src={heroImg} width="170" height="179" alt="" />
          <img className="framework" src={reactLogo} alt="React logo" />
          <img className="vite" src={viteLogo} alt="Vite logo" />
        </div>

        <div>
          <h1>AEGIS</h1>
          <p>AI-Powered Predictive Green Corridor System</p>
        </div>

        <button
          type="button"
          className="counter"
          onClick={() => setCount((current) => current + 1)}
        >
          Local test count: {count}
        </button>

        <button type="button" className="counter" onClick={checkBackend}>
          Check backend
        </button>

        {health && (
          <p>
            Backend: {health.status} — {health.service}
          </p>
        )}

        {healthError && <p>Backend error: {healthError}</p>}
      </section>

      <div className="ticks"></div>

      <section id="next-steps">
        <div id="docs">
          <h2>Backend connectivity</h2>
          <p>React can communicate with the AEGIS Flask API.</p>
        </div>

        <div id="social">
          <h2>Development status</h2>
          <p>Frontend and backend foundations are operational.</p>
        </div>
      </section>

      <div className="ticks"></div>
      <section id="spacer"></section>
    </>
  )
}

export default App