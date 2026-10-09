import { useCallback, useContext, useEffect, useState } from "react";
import {
  addDoc,
  collection,
  deleteDoc,
  doc,
  getDocs,
  query,
  serverTimestamp,
  updateDoc,
  where,
} from "firebase/firestore";
import { Auth } from "../lib/auth.js";
import { db } from "../lib/firebase.js";

export default function useItems() {
  const { user } = useContext(Auth);
  const [items, setItems] = useState([]);
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState("");
  const [loadError, setLoadError] = useState("");

  useEffect(() => {
    let active = true;

    if (!user) {
      setItems([]);
      setBusy(false);
      setLoadError("");
      return () => {
        active = false;
      };
    }

    setItems([]);
    setBusy(true);
    setLoadError("");
    getDocs(query(collection(db, "items"), where("userId", "==", user.uid)))
      .then((snapshot) => {
        if (!active) return;
        setItems(
          snapshot.docs.map((item) => ({
            id: item.id,
            ...item.data(),
            updated:
              item.data().updated?.toDate?.().toLocaleDateString("ko-KR") ||
              "최근",
          })),
        );
      })
      .catch(() => {
        if (active) setLoadError("기록을 불러오지 못했습니다.");
      })
      .finally(() => {
        if (active) setBusy(false);
      });

    return () => {
      active = false;
    };
  }, [user]);

  const save = useCallback(
    async (data) => {
      if (!user) {
        setError("기록을 저장하려면 먼저 로그인해 주세요.");
        return false;
      }

      setBusy(true);
      setError("");
      try {
        const payload = {
          title: data.title,
          body: data.body,
          tag: data.tag,
          userId: user.uid,
          updated: serverTimestamp(),
        };
        if (data.id) {
          await updateDoc(doc(db, "items", data.id), payload);
          setItems((old) =>
            old.map((item) =>
              item.id === data.id
                ? { ...item, ...data, updated: "방금" }
                : item,
            ),
          );
        } else {
          const created = await addDoc(collection(db, "items"), payload);
          setItems((old) => [
            { ...data, id: created.id, updated: "방금" },
            ...old,
          ]);
        }
        return true;
      } catch {
        setError(
          "기록을 저장하지 못했습니다. Firestore 보안 규칙을 확인해 주세요.",
        );
        return false;
      } finally {
        setBusy(false);
      }
    },
    [user],
  );

  const remove = useCallback(async (id) => {
    setBusy(true);
    setError("");
    try {
      await deleteDoc(doc(db, "items", id));
      setItems((current) => current.filter((item) => item.id !== id));
      return true;
    } catch {
      setError("기록을 삭제하지 못했습니다.");
      return false;
    } finally {
      setBusy(false);
    }
  }, []);

  return { items, busy, error, loadError, save, remove };
}
