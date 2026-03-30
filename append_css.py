import os

css_path = 'e:/websites/NTW/css/styles.css'
sticky_css = '''
/* Sticky Card Deck Layout for Industries */
.sticky-deck-wrapper {
  position: relative;
  width: 100%;
  padding-bottom: 150px;
  background: var(--c-surface-dark);
}
.sticky-card {
  position: sticky;
  top: 80px; /* Offset for header */
  height: 90vh;
  min-height: 800px;
  display: flex;
  align-items: center;
  border-top: 1px solid rgba(255,255,255,0.05);
  box-shadow: 0 -10px 40px rgba(0,0,0,0.5);
}
.sticky-card-inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  gap: 80px;
}
.sticky-text {
  width: 45%;
}
.sticky-tag {
  display: inline-block;
  color: var(--c-accent);
  font-family: var(--font-body);
  font-weight: 700;
  letter-spacing: 2px;
  text-transform: uppercase;
  margin-bottom: 24px;
  padding: 6px 12px;
  border: 1px solid rgba(90, 103, 216, 0.4);
  border-radius: 4px;
}
.sticky-text h2 {
  font-family: var(--font-heading);
  font-size: 56px;
  color: var(--c-white);
  line-height: 1.1;
  margin-bottom: 24px;
}
.sticky-text p {
  font-size: 20px;
  color: var(--c-dark-text-body);
  line-height: 1.7;
}
.sticky-visual {
  width: 50%;
  height: 100%;
  min-height: 500px;
  display: flex;
  justify-content: center;
  align-items: center;
}

@media (max-width: 900px) {
  .sticky-card {
    height: auto;
    position: relative;
    top: auto;
    padding: 80px 0;
  }
  .sticky-card-inner {
    flex-direction: column;
  }
  .sticky-text, .sticky-visual {
    width: 100%;
  }
  .sticky-text h2 { font-size: 40px; }
}
'''

with open(css_path, "a", encoding="utf-8") as f:
    f.write("\n" + sticky_css)
print("CSS Appended Successfully!")
