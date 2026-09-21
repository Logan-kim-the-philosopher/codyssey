import {useContext,useEffect,useState} from 'react';
import {useNavigate} from 'react-router-dom';
import {Auth} from '../lib/auth.js';
import Button from '../components/Button.jsx';
import Status from '../components/Status.jsx';
export default function Login(){const {login,user}=useContext(Auth),nav=useNavigate(),[error,setError]=useState('');useEffect(()=>{if(user)nav('/items')},[user,nav]);return <section className="login"><p className="eyebrow">WELCOME BACK</p><h2>다시 만났네요.</h2><p>Google 계정으로 로그인하면 나만의 기록을 계속 이어갈 수 있어요.</p>{error&&<Status type="error">{error}</Status>}<Button onClick={async()=>{try{await login()}catch(e){console.error(e);setError(`로그인 실패: ${e.code||e.message}`)}}}>Google로 로그인</Button></section>}
