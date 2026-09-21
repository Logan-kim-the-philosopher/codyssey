import {Link} from 'react-router-dom';
import {useContext} from 'react';
import {Auth} from '../lib/auth.js';
export default function ProtectedRoute({children}){const {user}=useContext(Auth);return user?children:<section className="login"><p className="eyebrow">PROFILE</p><h2>로그인이 필요해요.</h2><p>내 기록과 프로필을 보려면 먼저 로그인해 주세요.</p><Link className="btn primary" to="/login">로그인하러 가기</Link></section>}
