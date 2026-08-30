import { useState } from 'react'

function useSubmitTestCase() {
  const [loading, setLoading] = useState(false)
  const [response, setResponse] = useState<any>(null)

  const handleSubmit = async (requirement: string, e: any) => {
    e.preventDefault()
    setLoading(true)
    try {
      const res = await fetch('http://localhost:8000/test-cases', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ requirement }),
      })
      const data = await res.json()
      setResponse(data)
    } catch (error) {
      console.error('Error:', error)
    } finally {
      setLoading(false)
    }
  }

  return {
    loading,
    response,
    handleSubmit
  }
}

export default useSubmitTestCase
