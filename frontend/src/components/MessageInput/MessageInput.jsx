import { useState } from 'react';
import './MessageInput.css';

function MessageInput() {
  const [message, setMessage] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (message.trim()) {
      console.log('Send message:', message);
      setMessage('');
    }
  };

  return (
    <form className="message-input" onSubmit={handleSubmit}>
      <button type="button" className="attach-button">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
          <path d="M21.44 11.05l-9.19 9.19a6 6 0 0 1-8.49-8.49l9.19-9.19a4 4 0 0 1 5.66 5.66l-9.2 9.19a2 2 0 0 1-2.83-2.83l8.49-8.48" />
        </svg>
      </button>
      <input
        type="text"
        placeholder="Сообщение"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        className="input-field"
      />
    </form>
  );
}

export default MessageInput;