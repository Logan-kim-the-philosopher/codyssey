import { useContext } from "react";
import { Store } from "../lib/store.js";

export default function useStore() {
  const store = useContext(Store);
  if (!store) throw new Error("useStore must be used within ItemsProvider.");
  return store;
}
