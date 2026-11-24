import { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import './RegisterPage.css';

function UserIcon() {
  return (
    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round">
      <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2" />
      <circle cx="12" cy="7" r="4" />
    </svg>
  );
}

function LockIcon() {
  return (
    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round">
      <rect x="3" y="11" width="18" height="11" rx="2" ry="2" />
      <path d="M7 11V7a5 5 0 0 1 10 0v4" />
    </svg>
  );
}

function RegisterPage() {
  const navigate = useNavigate();
  const [form, setForm] = useState({
    firstName: '',
    lastName: '',
    email: '',
    username: '',
    password: '',
    day: '',
    month: '',
    year: '',
  });

  const handleChange = (field) => (e) => {
    setForm({ ...form, [field]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!form.firstName || !form.email || !form.username || !form.password) return;
    navigate('/login', { replace: true });
  };

  const days = Array.from({ length: 31 }, (_, i) => i + 1);
  const months = [
    'Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь',
    'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь',
  ];
  const years = Array.from({ length: 100 }, (_, i) => new Date().getFullYear() - i);

  return (
    <div className="register-page">
      <div className="register-card">
        <h1 className="register-title">Регистрация</h1>

        <form className="register-form" onSubmit={handleSubmit}>
          {/* Имя */}
          <label className="register-field">
            <span className="register-label">
              Имя <span className="required">*</span>
            </span>
            <input
              type="text"
              value={form.firstName}
              onChange={handleChange('firstName')}
              required
            />
          </label>

          {/* Фамилия */}
          <label className="register-field">
            <span className="register-label">Фамилия</span>
            <input
              type="text"
              value={form.lastName}
              onChange={handleChange('lastName')}
            />
          </label>

          {/* E-mail */}
          <label className="register-field">
            <span className="register-label">
              E-mail <span className="required">*</span>
            </span>
            <input
              type="email"
              value={form.email}
              onChange={handleChange('email')}
              required
            />
          </label>

          {/* Имя пользователя — с иконкой внутри */}
          <div className="register-field-icon">
            <span className="register-field-icon__icon">
              <UserIcon />
            </span>
            <input
              type="text"
              placeholder="Имя пользователя *"
              value={form.username}
              onChange={handleChange('username')}
              required
            />
          </div>

          {/* Пароль — с иконкой внутри */}
          <div className="register-field-icon">
            <span className="register-field-icon__icon">
              <LockIcon />
            </span>
            <input
              type="password"
              placeholder="Пароль *"
              value={form.password}
              onChange={handleChange('password')}
              required
            />
          </div>

          {/* Дата рождения */}
          <div className="register-birthdate">
            <span className="register-birthdate-label">Дата рождения</span>
            <div className="register-birthdate-selects">
              <select value={form.day} onChange={handleChange('day')}>
                <option value="">День</option>
                {days.map(d => <option key={d} value={d}>{d}</option>)}
              </select>
              <select value={form.month} onChange={handleChange('month')}>
                <option value="">Месяц</option>
                {months.map((m, i) => <option key={i} value={i + 1}>{m}</option>)}
              </select>
              <select value={form.year} onChange={handleChange('year')}>
                <option value="">Год</option>
                {years.map(y => <option key={y} value={y}>{y}</option>)}
              </select>
            </div>
          </div>

          <button type="submit" className="register-button">
            Войти
          </button>

          {/* Ссылка на авторизацию */}
          <div className="register-login-link">
            Уже есть аккаунт? <Link to="/login">Войти</Link>
          </div>
        </form>
      </div>
    </div>
  );
}

export default RegisterPage;