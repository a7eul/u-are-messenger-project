import LoginForm from '../../components/LoginForm/LoginForm';
import './LoginPage.css';

function LoginPage() {
  const handleLogin = (credentials) => {
    console.log('Login attempt:', credentials);
    // Здесь будет запрос к бэкенду
  };

  return (
    <div className="login-page">
      <LoginForm onLogin={handleLogin} />
    </div>
  );
}

export default LoginPage;