import { useState } from 'react'
import useSubmitTestCase from './hooks/useSubmitTestCase'
import './App.css'

function App() {
  const [requirement, setRequirement] = useState('')
  const { loading, response, handleSubmit } = useSubmitTestCase()

  const handleFormSubmit = (e: any) => {
    handleSubmit(requirement, e)
  }

  return (
    <>
      <h1>AI Chat</h1>
      <p>AI Chat Application</p>
      <form onSubmit={handleFormSubmit}>
        <textarea
          value={requirement}
          onChange={(e) => setRequirement(e.target.value)}
          placeholder="Enter your requirement"
          rows={4}
          style={{ width: '100%', padding: '10px', marginBottom: '10px' }}
        />
        <button type="submit" disabled={loading}>
          {loading ? 'Sending...' : 'Send'}
        </button>
      </form>
      {response && (
        <div style={{ marginTop: '20px', padding: '15px', backgroundColor: '#f5f5f5', borderRadius: '5px' }}>
          <h3>Response:</h3>
          <pre>{JSON.stringify(response, null, 2)}</pre>
        </div>
      )}
    </>
  )
}

export default App
