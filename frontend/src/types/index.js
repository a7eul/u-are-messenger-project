// Пользователь
export const UserShape = {
  user_id: 'number',
  username: 'string',
  first_name: 'string',
  last_name: 'string',
  email: 'string',
  avatar_url: 'string | null',
  about: 'string | null',
  last_seen: 'string | null', // ISO datetime
};

// Чат
export const ChatShape = {
  chat_id: 'number',
  title: 'string',
  type: 'private | group',
  avatar_url: 'string | null',
  description: 'string | null',
  created_by: 'number', // user_id
  created_at: 'string',
  last_message: 'MessageShape | null', // обычно подтягивают отдельно
  unread_count: 'number',
};

// Сообщение
export const MessageShape = {
  message_id: 'number',
  chat_id: 'number',
  sender_id: 'number',
  reply_to_id: 'number | null',
  content: 'string',
  created_at: 'string',
  is_deleted: 'boolean',
  sender: 'UserShape',          // подтягивается JOIN-ом
  reply_to: 'MessageShape | null', // подтягивается JOIN-ом
  attachments: 'AttachmentShape[]',
};

// Вложение
export const AttachmentShape = {
  attachment_id: 'number',
  message_id: 'number',
  file_url: 'string',
  file_name: 'string',
  file_size: 'number',
};