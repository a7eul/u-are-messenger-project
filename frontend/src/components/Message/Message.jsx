import './Message.css';

function Message({
  message_id,
  sender,
  reply_to,
  content,
  created_at,
  is_deleted,
  grouped,
}) {
  const formatTime = (dateStr) => {
    if (!dateStr) return '';
    const d = new Date(dateStr);
    if (!isNaN(d.getTime())) {
      return d.toLocaleTimeString('ru-RU', {
        hour: '2-digit',
        minute: '2-digit',
      });
    }
    return '';
  };

  const formatDate = (dateStr) => {
    if (!dateStr) return '';
    const d = new Date(dateStr);
    if (!isNaN(d.getTime())) {
      return d.toLocaleDateString('ru-RU', {
        day: '2-digit',
        month: '2-digit',
        year: 'numeric',
      }) + ' ' + d.toLocaleTimeString('ru-RU', {
        hour: '2-digit',
        minute: '2-digit',
      });
    }
    return dateStr;
  };

  if (is_deleted) {
    return (
      <div className="message message-deleted">
        <div className="message-avatar" />
        <div className="message-body">
          <div className="message-header">
            <span className="message-sender">{sender?.username || 'Неизвестно'}</span>
          </div>
          <span className="message-text message-text-deleted">
            Сообщение удалено
          </span>
        </div>
      </div>
    );
  }

  return (
    <div className={`message ${grouped ? 'message-grouped' : ''}`}>
      {/* Аватар — только у первого в группе */}
      {!grouped && <div className="message-avatar" />}

      {/* Время для сгруппированных сообщений — видно только при hover */}
      {grouped && (
        <div className="message-time">
          {formatTime(created_at)}
        </div>
      )}

      <div className="message-body">
        {/* Reply-цитата */}
        {reply_to && (
          <div className="message-reply">
            <div className="message-reply-bar" />
            <div className="message-reply-content">
              <span className="message-reply-sender">
                {reply_to.sender?.username}
              </span>
              <span className="message-reply-text">
                {reply_to.content}
              </span>
            </div>
          </div>
        )}

        {/* Шапка: ник + дата — только у первого в группе */}
        {!grouped && (
          <div className="message-header">
            <span className="message-sender">{sender?.username}</span>
            <span className="message-date">{formatDate(created_at)}</span>
          </div>
        )}

        {content && <div className="message-text">{content}</div>}
      </div>
    </div>
  );
}

export default Message;