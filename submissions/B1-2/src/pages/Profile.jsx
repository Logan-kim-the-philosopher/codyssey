import {useContext} from 'react';
import {Auth} from '../lib/auth.js';
export default function Profile(){const {user}=useContext(Auth);const name=user?.displayName||user?.email||'게스트';return <section className="profile"><p className="eyebrow">PROFILE</p><h2>{name}<br/><em>의 기록 공간</em></h2><p>{user?'오늘도 한 줄을 남겨보세요.':'로그인하면 기록을 저장할 수 있어요.'}</p></section>}
