import os

css_path = "e:/websites/NTW/css/styles.css"

css_payload = """
/* ------------------------------------- */
/* MOBILE TRUST BAR FINAL FIX            */
/* ------------------------------------- */
@media (max-width: 900px) {
    /* Stack "Operating Environments" and the List vertically */
    .partner-strip .container > div:first-child {
        flex-direction: column !important;
        align-items: flex-start !important;
        gap: 8px !important;
        width: 100% !important;
    }
    
    /* Keep all environments on one horizontal line */
    .partner-strip .container > div:first-child > div {
        flex-wrap: nowrap !important;
        gap: 6px !important;
        width: 100% !important;
        justify-content: flex-start !important;
    }

    /* Shrink the font so it fits without running off the screen */
    .partner-strip .container > div:first-child > div > span {
        font-size: 13px !important;
        white-space: nowrap !important;
    }
    
    /* Ensure bullets match the shrunk font */
    .partner-strip .container > div:first-child > div > span:nth-child(2n) {
        margin: 0 2px !important;
        font-size: 14px !important;
    }
}
"""

with open(css_path, "a", encoding="utf-8") as f:
    f.write(css_payload)

print("Final mobile trust bar CSS applied.")
