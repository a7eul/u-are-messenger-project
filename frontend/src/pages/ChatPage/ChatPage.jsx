import Sidebar from '../../components/Sidebar/Sidebar';
import ChatArea from '../../components/ChatArea/ChatArea';
import NarrowPanel from '../../components/NarrowPanel/NarrowPanel';
import MessageInput from '../../components/MessageInput/MessageInput';
import './ChatPage.css';

function ChatPage() {
  return (
    <div className="chat-page">
      <header className="chat-header" />
      <NarrowPanel />
      <Sidebar />
      <ChatArea />
      <footer className="composer">
        <MessageInput />
      </footer>
    </div>
  );
}

export default ChatPage;