export default function SectionHeading({ eyebrow, title, action, className }) {
  return (
    <div className={className}>
      <div>
        <p className="eyebrow">{eyebrow}</p>
        <h2>{title}</h2>
      </div>
      {action}
    </div>
  );
}
