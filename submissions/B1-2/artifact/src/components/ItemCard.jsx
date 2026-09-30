import { Link } from "react-router-dom";
import ItemMeta from "./ItemMeta.jsx";

export default function ItemCard({ item }) {
  return (
    <Link className="card" to={`/items/${item.id}`}>
      <ItemMeta tag={item.tag} updated={item.updated} />
      <h3>{item.title}</h3>
      <p>{item.body}</p>
      <span className="arrow">↗</span>
    </Link>
  );
}
