export default function ItemMeta({ tag, updated, variant = "card" }) {
  if (variant === "detail") {
    return (
      <p className="eyebrow">
        {tag} · {updated}
      </p>
    );
  }

  return (
    <div className="card-top">
      <span className="tag">{tag}</span>
      <span>{updated}</span>
    </div>
  );
}
