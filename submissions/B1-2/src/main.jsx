import React,{useContext,useEffect,useState} from 'react';
import {createRoot} from 'react-dom/client';
import {BrowserRouter,Routes,Route,NavLink,Link} from 'react-router-dom';
import './styles.css';
import Button from './components/Button.jsx';
import Status from './components/Status.jsx';
import {Store} from './lib/store.js';
import {Auth} from './lib/auth.js';
import ProtectedRoute from './components/ProtectedRoute.jsx';
import {auth,db,googleProvider} from './lib/firebase.js';
import {onAuthStateChanged,signInWithPopup,signOut} from 'firebase/auth';
import {addDoc,collection,deleteDoc,doc,getDocs,query,serverTimestamp,updateDoc,where} from 'firebase/firestore';
import HomePage from './pages/Home.jsx';
import ItemsPage from './pages/Items.jsx';
import DetailPage from './pages/Detail.jsx';
import FormPage from './pages/Form.jsx';
import LoginPage from './pages/Login.jsx';
import ProfilePage from './pages/Profile.jsx';
import NotFoundPage from './pages/NotFound.jsx';

function Provider({children}){const [items,setItems]=useState([]),[busy,setBusy]=useState(false),[error,setError]=useState(''),[loadError,setLoadError]=useState('');const {user}=useContext(Auth);useEffect(()=>{if(!user){setItems([]);setLoadError('');return}let active=true;setBusy(true);setLoadError('');getDocs(query(collection(db,'items'),where('userId','==',user.uid))).then(snapshot=>{if(active)setItems(snapshot.docs.map(item=>({id:item.id,...item.data(),updated:item.data().updated?.toDate?.().toLocaleDateString('ko-KR')||'최근'})))}).catch(()=>setLoadError('기록을 불러오지 못했습니다.')).finally(()=>setBusy(false));return()=>{active=false}},[user]);const save=async data=>{if(!user){setError('기록을 저장하려면 먼저 로그인해 주세요.');return false}setBusy(true);setError('');try{const payload={title:data.title,body:data.body,tag:data.tag,userId:user.uid,updated:serverTimestamp()};if(data.id){await updateDoc(doc(db,'items',data.id),payload);setItems(old=>old.map(x=>x.id===data.id?{...x,...data,updated:'방금'}:x))}else{const created=await addDoc(collection(db,'items'),payload);setItems(old=>[{...data,id:created.id,updated:'방금'},...old])}return true}catch{setError('기록을 저장하지 못했습니다. Firestore 보안 규칙을 확인해 주세요.');return false}finally{setBusy(false)}};const remove=async id=>{setBusy(true);try{await deleteDoc(doc(db,'items',id));setItems(x=>x.filter(i=>i.id!==id))}catch{setError('기록을 삭제하지 못했습니다.')}finally{setBusy(false)}};return <Store.Provider value={{items,busy,error,loadError,save,remove}}>{children}</Store.Provider>}
function AuthProvider({children}){const [user,setUser]=useState(null);useEffect(()=>onAuthStateChanged(auth,setUser),[]);const login=()=>signInWithPopup(auth,googleProvider);const logout=()=>signOut(auth);return <Auth.Provider value={{user,login,logout}}>{children}</Auth.Provider>}
function Layout(){const {user,logout}=useContext(Auth);return <><header><Link className="brand" to="/">pulse<span>·</span>note</Link><nav><NavLink to="/items" end>기록</NavLink></nav><Button kind="ghost" onClick={user?logout:()=>location.href='/login'}>{user?'로그아웃':'로그인'}</Button></header><main><Routes><Route path="/" element={<HomePage/>}/><Route path="/login" element={<LoginPage/>}/><Route path="/items" element={<ItemsPage/>}/><Route path="/items/:id" element={<DetailPage/>}/><Route path="/items/new" element={<FormPage/>}/><Route path="/items/:id/edit" element={<FormPage/>}/><Route path="/profile" element={<ProtectedRoute><ProfilePage/></ProtectedRoute>}/><Route path="*" element={<NotFoundPage/>}/></Routes></main></>}
function App(){return <AuthProvider><Provider><Layout/></Provider></AuthProvider>};createRoot(document.getElementById('root')).render(<BrowserRouter><App/></BrowserRouter>);
