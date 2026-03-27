import os
import re

file_path = "e:/websites/NTW/index.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Replace Core Capabilities
new_capabilities = """            <div class="grid grid-4" style="gap: 24px;">
                <div class="svc-card svc-dark" style="background: #0f172a; border: 1px solid #1e293b; padding: 40px 32px;">
                    <div class="svc-icon-wrap" style="color: #fff; margin-bottom: 24px;"><svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path><polyline points="3.27 6.96 12 12.01 20.73 6.96"></polyline><line x1="12" y1="22.08" x2="12" y2="12"></line></svg></div>
                    <h3 style="font-size: 20px; color: #fff; margin-bottom: 12px; line-height: 1.3;">Structured Cabling Systems</h3>
                    <p style="color: #94a3b8; font-size: 15px; line-height: 1.6;">High-density fiber and copper backbones. Strict labeling and certified Fluke arrays.</p>
                </div>
                <div class="svc-card svc-dark" style="background: #0f172a; border: 1px solid #1e293b; padding: 40px 32px;">
                    <div class="svc-icon-wrap" style="color: #fff; margin-bottom: 24px;"><svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="4" width="20" height="16" rx="2" ry="2"></rect><path d="M12 16v-4"></path><path d="M8 12h8"></path></svg></div>
                    <h3 style="font-size: 20px; color: #fff; margin-bottom: 12px; line-height: 1.3;">Surveillance &<br>Security Systems</h3>
                    <p style="color: #94a3b8; font-size: 15px; line-height: 1.6;">Precision IP camera mounting. Direct FOV mapping and multi-server VMS storage architecture.</p>
                </div>
                <div class="svc-card svc-dark" style="background: #0f172a; border: 1px solid #1e293b; padding: 40px 32px;">
                    <div class="svc-icon-wrap" style="color: #fff; margin-bottom: 24px;"><svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg></div>
                    <h3 style="font-size: 20px; color: #fff; margin-bottom: 12px; line-height: 1.3;">Access Control &<br>Entry Systems</h3>
                    <p style="color: #94a3b8; font-size: 15px; line-height: 1.6;">Total physical barrier mitigation. OSDP readers, logic panel termination, and electrified routing.</p>
                </div>
                <div class="svc-card svc-dark" style="background: #0f172a; border: 1px solid #1e293b; padding: 40px 32px;">
                    <div class="svc-icon-wrap" style="color: #fff; margin-bottom: 24px;"><svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="4" y="4" width="16" height="16" rx="2" ry="2"></rect><rect x="9" y="9" width="6" height="6"></rect><line x1="9" y1="1" x2="9" y2="4"></line><line x1="15" y1="1" x2="15" y2="4"></line><line x1="9" y1="20" x2="9" y2="23"></line><line x1="15" y1="20" x2="15" y2="23"></line><line x1="20" y1="9" x2="23" y2="9"></line><line x1="20" y1="14" x2="23" y2="14"></line><line x1="1" y1="9" x2="4" y2="9"></line><line x1="1" y1="14" x2="4" y2="14"></line></svg></div>
                    <h3 style="font-size: 20px; color: #fff; margin-bottom: 12px; line-height: 1.3;">Network & IT<br>Infrastructure</h3>
                    <p style="color: #94a3b8; font-size: 15px; line-height: 1.6;">Enterprise MDF/IDF rack buildouts. Switch chassis elevation, UPS installation, and staging environments.</p>
                </div>
                <div class="svc-card svc-dark" style="background: #0f172a; border: 1px solid #1e293b; padding: 40px 32px;">
                    <div class="svc-icon-wrap" style="color: #fff; margin-bottom: 24px;"><svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M2 12h4l3-9 5 18 3-9h5"></path></svg></div>
                    <h3 style="font-size: 20px; color: #fff; margin-bottom: 12px; line-height: 1.3;">Conduit & Pathway<br>Installation</h3>
                    <p style="color: #94a3b8; font-size: 15px; line-height: 1.6;">Above-ceiling and subterranean pathway routing. EMT, rigid conduit, and specialized cable tray execution.</p>
                </div>
                <div class="svc-card svc-dark" style="background: #0f172a; border: 1px solid #1e293b; padding: 40px 32px;">
                    <div class="svc-icon-wrap" style="color: #fff; margin-bottom: 24px;"><svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 2 7 12 12 22 7 12 2"></polygon><polyline points="2 17 12 22 22 17"></polyline><polyline points="2 12 12 17 22 12"></polyline></svg></div>
                    <h3 style="font-size: 20px; color: #fff; margin-bottom: 12px; line-height: 1.3;">Multi-Site Rollouts &<br>Field Deployment</h3>
                    <p style="color: #94a3b8; font-size: 15px; line-height: 1.6;">Scalable infrastructure provisioning. Zero-variance replication for vast enterprise environments.</p>
                </div>
                <div class="svc-card svc-dark" style="background: #0f172a; border: 1px solid #1e293b; padding: 40px 32px;">
                    <div class="svc-icon-wrap" style="color: #fff; margin-bottom: 24px;"><svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 9.36l-7.1 7.1a1 1 0 0 1-1.4 0l-2.8-2.8a1 1 0 0 1 0-1.4l7.1-7.1a6 6 0 0 1 9.36-7.94l-3.77 3.77z"></path></svg></div>
                    <h3 style="font-size: 20px; color: #fff; margin-bottom: 12px; line-height: 1.3;">Maintenance, Repair<br>& Optimization</h3>
                    <p style="color: #94a3b8; font-size: 15px; line-height: 1.6;">Preventative physical layer auditing. Immediate remediation of compliance violations and degradation.</p>
                </div>
                <div class="svc-card svc-dark" style="background: #0f172a; border: 1px solid #1e293b; padding: 40px 32px;">
                    <div class="svc-icon-wrap" style="color: #fff; margin-bottom: 24px;"><svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg></div>
                    <h3 style="font-size: 20px; color: #fff; margin-bottom: 12px; line-height: 1.3;">Technical Field<br>Services & Dispatch</h3>
                    <p style="color: #94a3b8; font-size: 15px; line-height: 1.6;">On-demand dispatch of highly trained technicians. Rapid response for critical infrastructure triage.</p>
                </div>
            </div>"""

cap_match = re.search(r'(<div class="grid grid-4"[\s\S]*?</div>\s*</div>\s*</section>)', content)
if cap_match:
    # Replace just the grid contents
    inner_grid = re.search(r'(<div class="grid grid-4">[\s\S]*?</div>\s*</div>)', cap_match.group(1))
    if inner_grid:
        pass # we will manually replace it
    
content = re.sub(r'<div class="grid grid-4">[\s\S]*?</div>\s*</div>\s*</section>', new_capabilities + '\n        </div>\n    </section>', content)

# 2. Replace Who We Work With + Contact Form
new_contact_section = """    <!-- 9. Partner / Audience Array & Form -->
    <style>
        .premium-form .form-group-p label { display: block; font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; color: #64748b; margin-bottom: 8px; }
        .premium-form .form-group-p input, .premium-form .form-group-p select, .premium-form .form-group-p textarea { width: 100%; background: transparent; border: none; border-bottom: 1px solid #334155; padding: 12px 0; color: #fff; font-size: 16px; font-family: inherit; transition: all 0.3s ease; border-radius: 0; outline: none; }
        .premium-form .form-group-p input:focus, .premium-form .form-group-p select:focus, .premium-form .form-group-p textarea:focus { border-bottom-color: #fff; }
        .premium-form .form-group-p select option { background: #0f172a; color: #fff; }
    </style>
    <section class="section" style="background: #fff; padding: 140px 0; border-top: 1px solid #e2e8f0;" id="request-service">
        <div class="container">
            <div class="grid grid-2" style="gap: 100px; align-items: flex-start;">
                <!-- Left: Copy + Audiences + Location -->
                <div>
                    <div class="sec-tag" style="background: #e2e8f0; color: #0f172a; border-color: #cbd5e1; font-weight: 700; margin-bottom: 24px;">Who We Work With</div>
                    <h2 style="font-family: var(--font-heading); font-size: 46px; color: #0f172a; margin-bottom: 40px; line-height: 1.1;">Partners in Execution</h2>
                    <ul style="list-style: none; padding: 0; display: flex; flex-direction: column; gap: 24px;">
                        <li style="display: flex; align-items: center; gap: 24px; font-size: 22px; color: #1e293b; font-weight: 600; letter-spacing: -0.5px;"><svg width="24" height="24" fill="none" stroke="#0f172a" stroke-width="3"><polyline points="20 6 9 17 4 12"></polyline></svg> System Integrators</li>
                        <li style="display: flex; align-items: center; gap: 24px; font-size: 22px; color: #1e293b; font-weight: 600; letter-spacing: -0.5px;"><svg width="24" height="24" fill="none" stroke="#0f172a" stroke-width="3"><polyline points="20 6 9 17 4 12"></polyline></svg> Enterprise IT Teams</li>
                        <li style="display: flex; align-items: center; gap: 24px; font-size: 22px; color: #1e293b; font-weight: 600; letter-spacing: -0.5px;"><svg width="24" height="24" fill="none" stroke="#0f172a" stroke-width="3"><polyline points="20 6 9 17 4 12"></polyline></svg> Property Managers</li>
                        <li style="display: flex; align-items: center; gap: 24px; font-size: 22px; color: #1e293b; font-weight: 600; letter-spacing: -0.5px;"><svg width="24" height="24" fill="none" stroke="#0f172a" stroke-width="3"><polyline points="20 6 9 17 4 12"></polyline></svg> General Contractors</li>
                        <li style="display: flex; align-items: center; gap: 24px; font-size: 22px; color: #1e293b; font-weight: 600; letter-spacing: -0.5px;"><svg width="24" height="24" fill="none" stroke="#0f172a" stroke-width="3"><polyline points="20 6 9 17 4 12"></polyline></svg> Multi-Site Operators</li>
                    </ul>
                    
                    <div style="margin-top: 64px; padding-top: 40px; border-top: 1px solid #e2e8f0;">
                        <span style="font-weight: 700; color: #94a3b8; text-transform: uppercase; letter-spacing: 1px; font-size: 13px; display: block; margin-bottom: 16px;">Primary Territories</span>
                        <div style="color: #0f172a; font-size: 20px; font-weight: 700;">Fairfield County, CT &nbsp;&middot;&nbsp; New York &nbsp;&middot;&nbsp; New Jersey</div>
                    </div>
                </div>
                
                <!-- Right: Premium Contact Form -->
                <div style="background: #0f172a; padding: 56px 48px; border-radius: 8px; box-shadow: 0 24px 50px -12px rgba(0,0,0,0.25);">
                    <h3 style="color: #fff; font-size: 32px; font-family: var(--font-heading); margin-bottom: 40px; letter-spacing: -0.5px;">Initiate Your Deployment</h3>
                    <form class="premium-form">
                        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 24px; margin-bottom: 24px;">
                            <div class="form-group-p">
                                <label>First Name</label>
                                <input type="text" required>
                            </div>
                            <div class="form-group-p">
                                <label>Last Name</label>
                                <input type="text" required>
                            </div>
                        </div>
                        <div class="form-group-p" style="margin-bottom: 24px;">
                            <label>Company Name</label>
                            <input type="text" required>
                        </div>
                        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 24px; margin-bottom: 24px;">
                            <div class="form-group-p">
                                <label>Work Email</label>
                                <input type="email" required>
                            </div>
                            <div class="form-group-p">
                                <label>Phone Number</label>
                                <input type="tel">
                            </div>
                        </div>
                        <div class="form-group-p" style="margin-bottom: 32px;">
                            <label>Project Type</label>
                            <select required>
                                <option value="" disabled selected>Select execution vertical</option>
                                <option>Cabling</option>
                                <option>Surveillance</option>
                                <option>Access Control</option>
                                <option>Network Infrastructure</option>
                                <option>Multi-Site Rollout</option>
                                <option>Other</option>
                            </select>
                        </div>
                        <div class="form-group-p" style="margin-bottom: 40px;">
                            <label>Project Details</label>
                            <textarea rows="2" required></textarea>
                        </div>
                        <button type="submit" class="btn btn-primary" style="width: 100%; padding: 20px; font-size: 15px; background: #fff; color: #020617; text-transform: uppercase; letter-spacing: 1.5px; border-radius: 4px; border: none; font-weight: 800; cursor: pointer; transition: background 0.2s;" onmouseover="this.style.background='#f1f5f9'" onmouseout="this.style.background='#fff'">Request Deployment</button>
                        
                        <div style="margin-top: 32px; text-align: center; color: #64748b; font-size: 14px; line-height: 1.6;">
                            Prefer direct communication? <br><a href="mailto:solutions@northeasttechworks.com" style="color: #fff; text-decoration: none; font-weight: 500; transition: 0.2s;" onmouseover="this.style.color='#94a3b8'" onmouseout="this.style.color='#fff'">solutions@northeasttechworks.com</a>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </section>"""

content = re.sub(r'<!-- 9\. Partner / Audience Array -->[\s\S]*?</section>', new_contact_section, content)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated index.html effortlessly!")
