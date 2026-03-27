import os
import re

base_dir = "e:/websites/NTW"
ind_path = os.path.join(base_dir, "industries.html")
css_path = os.path.join(base_dir, "css", "styles.css")

form_html = """
    <!-- Lead Generation Block -->
    <section class="lead-collection" style="background: var(--c-surface-dark); padding: 120px 0; border-top: 1px solid rgba(255,255,255,0.05); position: relative; z-index: 99; margin-top:-50px;">
        <div class="container">
            <div class="lead-grid">
                <div class="lead-context">
                    <div class="hero-tag" style="margin-bottom: 24px;">Project Intake</div>
                    <h2 style="font-family: var(--font-heading); font-size: 56px; color: var(--c-white); line-height: 1.1; margin-bottom: 24px;">Ready to execute your next deployment?</h2>
                    <p style="font-size: 20px; color: var(--c-dark-text-body); max-width: 500px; line-height: 1.7; margin-bottom: 40px;">Our dedicated project engineers are standing by. Submit your multi-site blueprints, infrastructure requirements, or SLA contingencies below for a rapid architectural review.</p>
                    
                    <div class="contact-badges" style="display: flex; gap: 32px;">
                        <div style="display: flex; align-items: center; gap: 16px;">
                            <div style="width: 48px; height: 48px; border-radius: 50%; background: rgba(90, 103, 216, 0.1); display: flex; align-items: center; justify-content: center; border: 1px solid rgba(90, 103, 216, 0.3);">
                                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#5A67D8" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
                            </div>
                            <div>
                                <div style="font-size: 14px; color: var(--c-dark-text-body); margin-bottom: 4px;">Direct Line</div>
                                <div style="font-size: 18px; color: white; font-weight: 600;">(203) 418-1608</div>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="lead-form-wrapper">
                    <form class="lead-form">
                        <div class="form-row">
                            <div class="input-group">
                                <label>Full Name</label>
                                <input type="text" placeholder="John Doe" required>
                            </div>
                            <div class="input-group">
                                <label>Company</label>
                                <input type="text" placeholder="Organization Name" required>
                            </div>
                        </div>
                        <div class="form-row">
                            <div class="input-group">
                                <label>Work Email</label>
                                <input type="email" placeholder="john@company.com" required>
                            </div>
                            <div class="input-group">
                                <label>Sector</label>
                                <select required>
                                    <option value="" disabled selected>Select Industry...</option>
                                    <option>Retail & Logistics</option>
                                    <option>Commercial Office IT</option>
                                    <option>Data Centers</option>
                                    <option>Manufacturing</option>
                                    <option>Healthcare</option>
                                    <option>Education</option>
                                    <option>Hospitality</option>
                                </select>
                            </div>
                        </div>
                        <div class="input-group">
                            <label>Deployment Scope</label>
                            <textarea placeholder="Tell us about the project scale, multi-site counts, or critical timelines..." rows="4" required></textarea>
                        </div>
                        <button type="submit" class="btn btn-primary" style="width: 100%; justify-content: center; margin-top: 16px;">Initiate Consultation</button>
                    </form>
                </div>
            </div>
        </div>
    </section>
"""

form_css = """
/* Lead Collection Form CSS */
.lead-grid {
    display: grid;
    grid-template-columns: 1fr 1.2fr;
    gap: 80px;
    align-items: center;
}
.lead-form-wrapper {
    background: rgba(255, 255, 255, 0.02);
    border: 1px solid rgba(255, 255, 255, 0.05);
    border-radius: 16px;
    padding: 48px;
    backdrop-filter: blur(10px);
}
.lead-form {
    display: flex;
    flex-direction: column;
    gap: 24px;
}
.form-row {
    display: flex;
    gap: 24px;
}
.input-group {
    display: flex;
    flex-direction: column;
    gap: 8px;
    flex: 1;
}
.input-group label {
    font-size: 13px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 1px;
    color: var(--c-dark-text-body);
}
.input-group input, 
.input-group select, 
.input-group textarea {
    background: transparent;
    border: none;
    border-bottom: 1px solid rgba(255,255,255,0.2);
    padding: 12px 0;
    font-size: 16px;
    color: white;
    font-family: var(--font-body);
    transition: all 0.3s ease;
}
.input-group input:focus,
.input-group select:focus,
.input-group textarea:focus {
    outline: none;
    border-bottom-color: var(--c-accent);
}
.input-group select {
    color: white;
}
.input-group select option {
    background: var(--c-surface-dark);
    color: white;
}
.input-group textarea {
    resize: vertical;
}

@media (max-width: 900px) {
    .lead-grid {
        grid-template-columns: 1fr;
        gap: 48px;
    }
    .form-row {
        flex-direction: column;
        gap: 24px;
    }
    .lead-form-wrapper {
        padding: 32px 24px;
    }
}
"""

with open(css_path, "r", encoding="utf-8") as f:
    current_css = f.read()

if ".lead-form-wrapper" not in current_css:
    with open(css_path, "a", encoding="utf-8") as f:
        f.write("\n" + form_css)

with open(ind_path, "r", encoding="utf-8") as f:
    html_content = f.read()

# Insert right before the footer
if "<!-- Lead Generation Block -->" not in html_content:
    html_content = html_content.replace('<footer class="footer">', form_html + '\n<footer class="footer">')
    
    with open(ind_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print("Lead Gen form injected successfully!")
else:
    print("Lead Gen form already exists in the file.")
