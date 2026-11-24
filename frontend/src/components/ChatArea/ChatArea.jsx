import Message from '../Message/Message';
import './ChatArea.css';

const messages = [
  {
    message_id: 1,
    sender: { username: 'Чел1' },
    created_at: '2027-09-26T20:00:00Z',
    content: 'Ка-52 — добавлен БКО радарного типа «Ар...',
    reply_to: null,
    grouped: false,
    is_deleted: false,
  },
  {
    message_id: 2,
    sender: { username: 'Kamper' },
    created_at: '2027-09-26T20:01:00Z',
    content: 'А я не ебу что там стояло. Скорее всего да',
    reply_to: {
      sender: { username: 'Чел1' },
      content: 'Ка-52 — добавлен БКО радарного типа «Ар...',
    },
    grouped: false,
    is_deleted: false,
  },
  {
    message_id: 3,
    sender: { username: 'Чел1' },
    created_at: '2027-09-26T20:02:00Z',
    content: 'Ответ на своё сообщение',
    reply_to: {
      sender: { username: 'Чел1' },
      content: 'Ка-52 — добавлен БКО радарного типа «Ар...',
    },
    grouped: false,
    is_deleted: false,
  },
  {
    message_id: 4,
    sender: { username: 'Чел2' },
    created_at: '2027-09-26T20:03:00Z',
    content: 'Сообщение',
    reply_to: {
      sender: { username: 'Kamper' },
      content: 'А я не ебу что там стояло...',
    },
    grouped: false,
    is_deleted: false,
  },
  {
    message_id: 5,
    sender: { username: 'Чел2' },
    created_at: '2027-09-26T20:04:00Z',
    content: 'Ка-52 — добавлен БКО радарного типа «Ар...',
    reply_to: null,
    grouped: true,
    is_deleted: false,
  },
  {
    message_id: 6,
    sender: { username: 'Чел2' },
    created_at: '2027-09-26T20:04:00Z',
    content: 'Ка-52 — добавлен БКО радарного типа «Ар...',
    reply_to: null,
    grouped: true,
    is_deleted: false,
  },
];

function ChatArea() {
  return (
    <div className="chat-area">
      <div className="chat-area-header">
        <div className="chat-area-title">Группа 1</div>
        <div className="chat-area-subtitle">3 участника</div>
      </div>
      <div className="messages-container">
        {messages.map(msg => (
          <Message key={msg.message_id} {...msg} />
        ))}
      </div>
    </div>
  );
}

export default ChatArea;