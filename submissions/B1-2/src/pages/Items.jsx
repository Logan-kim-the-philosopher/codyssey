import { useMemo, useState } from "react";
import { Link } from "react-router-dom";
import useItems from "../hooks/useItems.js";
import ItemList from "../components/ItemList.jsx";
import SearchField from "../components/SearchField.jsx";
import SectionHeading from "../components/SectionHeading.jsx";
import Status from "../components/Status.jsx";

export default function Items() {
  const { items, busy, loadError } = useItems();
  const [q, setQ] = useState("");
  const filtered = useMemo(
    () =>
      items.filter((item) =>
        (item.title + item.body + item.tag)
          .toLowerCase()
          .includes(q.toLowerCase()),
      ),
    [items, q],
  );

  return (
    <section>
      <SectionHeading
        className="page-head"
        eyebrow="YOUR COLLECTION"
        title="모든 기록"
        action={
          <Link className="btn primary" to="/items/new">
            + 새 기록
          </Link>
        }
      />
      <SearchField
        value={q}
        onChange={(event) => setQ(event.target.value)}
        placeholder="기록을 검색하세요"
      />
      {loadError ? (
        <Status type="error">{loadError}</Status>
      ) : busy ? (
        <Status type="loading">기록을 불러오는 중...</Status>
      ) : filtered.length ? (
        <ItemList items={filtered} />
      ) : (
        <Status type="empty">
          {items.length ? "검색 결과가 없습니다." : "표시할 기록이 없습니다."}
        </Status>
      )}
    </section>
  );
}
