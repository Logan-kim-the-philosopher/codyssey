import { Link, useNavigate, useParams } from "react-router-dom";
import useStore from "../hooks/useStore.js";
import Button from "../components/Button.jsx";
import Status from "../components/Status.jsx";
import ItemMeta from "../components/ItemMeta.jsx";
export default function Detail() {
  const { id } = useParams(),
    { items, remove, busy, error } = useStore(),
    nav = useNavigate(),
    item = items.find((x) => x.id === id);
  if (!item)
    return <Status type="error">요청한 기록을 찾을 수 없습니다.</Status>;
  return (
    <article className="detail">
      <Link to="/items" className="back">
        ← 모든 기록
      </Link>
      <ItemMeta tag={item.tag} updated={item.updated} variant="detail" />
      <h2>{item.title}</h2>
      <p className="detail-body">{item.body}</p>
      {error && <Status type="error">{error}</Status>}
      <div className="actions">
        <Link className="btn secondary" to={"/items/" + id + "/edit"}>
          수정
        </Link>
        <Button
          kind="danger"
          disabled={busy}
          onClick={async () => {
            if (await remove(id)) nav("/items");
          }}
        >
          삭제
        </Button>
      </div>
    </article>
  );
}
