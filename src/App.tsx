import { useState } from 'react'

import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>

      <h1>Deployment Day</h1>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
        <p>
          Please follow the directions on the <a>deployment day repo</a> to learn how you can deploy this website to the internet!
        </p>
        <p>Happy deploying </p>
      </div>
      <p>@copy; 2026 acmCSUF Dev</p>
    </>
  )
}

export default App
