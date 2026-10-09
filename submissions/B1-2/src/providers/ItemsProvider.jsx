import useItems from "../hooks/useItems.js";
import { Store } from "../lib/store.js";

export default function ItemsProvider({ children }) {
  const itemsStore = useItems();
  return <Store.Provider value={itemsStore}>{children}</Store.Provider>;
}
