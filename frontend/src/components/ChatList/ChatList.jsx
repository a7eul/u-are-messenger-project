import './ChatList.css';

const chats = [
  { id: 1, name: 'Имя', message: 'Сообщение' },
  { id: 2, name: 'Имя', message: 'Сообщение' },
  { id: 3, name: 'Имя', message: 'Сообщение' },
  { id: 4, name: 'Имя', message: 'Сообщение' },
  { id: 5, name: 'Имя', message: 'Сообщение' },
  { id: 6, name: 'Имя', message: 'Сообщение' },
  { id: 7, name: 'Имя', message: 'Сообщение' },
  { id: 8, name: 'Имя', message: 'Сообщение' },
  { id: 9, name: 'Имя', message: 'Сообщение' },
  { id: 10, name: 'Имя', message: 'Сообщение' },
  { id: 11, name: 'Имя', message: 'Сообщение' },
];

function ChatList() {
  return (
    <div className="chat-list">
      <div className="search-container">
        <input
          type="text"
          placeholder="Search"
          className="search-input"
        />
      </div>
      <div className="chats-container">
        {chats.map(chat => (
          <div key={chat.id} className="chat-item">
            <div className="chat-avatar"></div>
            <div className="chat-info">
              <div className="chat-name">{chat.name}</div>
              <div className="chat-message">{chat.message}</div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default ChatList;