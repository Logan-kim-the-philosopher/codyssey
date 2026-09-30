export default function FormField({ label, children }) {
  return (
    <label>
      {label}
      {children}
    </label>
  );
}
