import { useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import useItems from "../hooks/useItems.js";
import Button from "../components/Button.jsx";
import FormField from "../components/FormField.jsx";
import SectionHeading from "../components/SectionHeading.jsx";
import Status from "../components/Status.jsx";

export default function Form() {
  const { id } = useParams();
  const { items, save, busy, error } = useItems();
  const nav = useNavigate();
  const existing = items.find((item) => item.id === id);
  const [form, setForm] = useState(
    existing || { title: "", body: "", tag: "일상" },
  );
  const [err, setErr] = useState("");

  const submit = async (event) => {
    event.preventDefault();
    if (!form.title.trim() || !form.body.trim()) {
      setErr("제목과 내용을 모두 입력해 주세요.");
      return;
    }
    setErr("");
    const saved = await save(form);
    if (saved) nav("/items");
  };

  return (
    <section className="form-wrap">
      <SectionHeading
        className="form-heading"
        eyebrow={existing ? "EDIT ENTRY" : "NEW ENTRY"}
        title={existing ? "기록을 다듬어요" : "새로운 기록"}
      />
      <form onSubmit={submit}>
        {(err || error) && <Status type="error">{err || error}</Status>}
        <FormField label="제목">
          <input
            value={form.title}
            onChange={(event) =>
              setForm({ ...form, title: event.target.value })
            }
            placeholder="오늘의 제목"
          />
        </FormField>
        <FormField label="분류">
          <select
            value={form.tag}
            onChange={(event) => setForm({ ...form, tag: event.target.value })}
          >
            <option>일상</option>
            <option>아이디어</option>
            <option>배움</option>
          </select>
        </FormField>
        <FormField label="내용">
          <textarea
            rows="8"
            value={form.body}
            onChange={(event) =>
              setForm({ ...form, body: event.target.value })
            }
            placeholder="무슨 일이 있었나요?"
          />
        </FormField>
        <Button disabled={busy}>{busy ? "저장 중..." : "기록 저장"}</Button>
      </form>
    </section>
  );
}
