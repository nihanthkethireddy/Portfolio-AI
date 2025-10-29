// src/pages/index.js
import { useState, useEffect } from 'react';

export default function Home() {
  const [message, setMessage] = useState('Loading...');

  useEffect(() => {
    fetch('/api/hello') // Calls the Python backend
      .then((res) => res.json())
      .then((data) => setMessage(data.message));
  }, []);

  return (
    <div>
      <h1>Next.js Frontend</h1>
      <p>{message}</p>
    </div>
  );
}