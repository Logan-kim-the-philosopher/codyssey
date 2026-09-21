import {useState} from 'react';
import {Link} from 'react-router-dom';
import useItems from '../hooks/useItems.js';
import Status from '../components/Status.jsx';
function Card({item}){return <Link className="card" to={'/items/'+item.id}><div className="card-top"><span className="tag">{item.tag}</span><span>{item.updated}</span></div><h3>{item.title}</h3><p>{item.body}</p><span className="arrow">↗</span></Link>}
export default function Items(){const {items,busy,loadError}=useItems();const [q,setQ]=useState('');const filtered=items.filter(x=>(x.title+x.body+x.tag).toLowerCase().includes(q.toLowerCase()));return <section><div className="page-head"><div><p className="eyebrow">YOUR COLLECTION</p><h2>모든 기록</h2></div><Link className="btn primary" to="/items/new">+ 새 기록</Link></div><input className="search" placeholder="기록을 검색하세요" value={q} onChange={e=>setQ(e.target.value)}/>{loadError&&<Status type="error">{loadError}</Status>}{busy&&<Status type="loading">저장 중...</Status>}{!loadError&&!filtered.length?<Status type="empty">표시할 기록이 없습니다.</Status>:!loadError&&<div className="grid">{filtered.map(item=><Card key={item.id} item={item}/>)}</div>}</section>}
