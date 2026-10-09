import React,{useContext,useEffect,useState} from 'react';
import {createRoot} from 'react-dom/client';
import {BrowserRouter,Routes,Route,NavLink,Link} from 'react-router-dom';
import './styles.css';
import Button from './components/Button.jsx';
import Status from './components/Status.jsx';
import {Auth} from './lib/auth.js';
import ProtectedRoute from './components/ProtectedRoute.jsx';
import {auth,googleProvider} from './lib/firebase.js';
import {onAuthStateChanged,signInWithPopup,signOut} from 'firebase/auth';
import ItemsProvider from './providers/ItemsProvider.jsx';
import HomePage from './pages/Home.jsx';
import ItemsPage from './pages/Items.jsx';
import DetailPage from './pages/Detail.jsx';
import FormPage from './pages/Form.jsx';
import LoginPage from './pages/Login.jsx';
import ProfilePage from './pages/Profile.jsx';
import NotFoundPage from './pages/NotFound.jsx';

function AuthProvider({children}){const [user,setUser]=useState(null);useEffect(()=>onAuthStateChanged(auth,setUser),[]);const login=()=>signInWithPopup(auth,googleProvider);const logout=()=>signOut(auth);return <Auth.Provider value={{user,login,logout}}>{children}</Auth.Provider>}
function Layout(){const {user,logout}=useContext(Auth);return <><header><Link className="brand" to="/">pulse<span>·</span>note</Link><nav><NavLink to="/items" end>기록</NavLink></nav><Button kind="ghost" onClick={user?logout:()=>location.href='/login'}>{user?'로그아웃':'로그인'}</Button></header><main><Routes><Route path="/" element={<HomePage/>}/><Route path="/login" element={<LoginPage/>}/><Route path="/items" element={<ItemsPage/>}/><Route path="/items/:id" element={<DetailPage/>}/><Route path="/items/new" element={<FormPage/>}/><Route path="/items/:id/edit" element={<FormPage/>}/><Route path="/profile" element={<ProtectedRoute><ProfilePage/></ProtectedRoute>}/><Route path="*" element={<NotFoundPage/>}/></Routes></main></>}
function App(){return <AuthProvider><ItemsProvider><Layout/></ItemsProvider></AuthProvider>};createRoot(document.getElementById('root')).render(<BrowserRouter><App/></BrowserRouter>);
