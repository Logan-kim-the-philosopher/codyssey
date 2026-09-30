export default function SearchField({ value, onChange, placeholder }) {
  return (
    <input
      aria-label="기록 검색"
      className="search"
      placeholder={placeholder}
      value={value}
      onChange={onChange}
    />
  );
}
