import os

html_body = """
    <!-- 3. Hero Section (Subpage Profile) -->
    <section class="hero theme-dark" style="min-height: 35vh; padding-top: 100px; padding-bottom: 50px;">
        <div class="container relative">
            <div class="hero-content">
                <div class="hero-tag" style="margin-bottom: 20px;">Partnerships</div>
                <h1 style="font-size: 52px; line-height: 1.2; margin-bottom: 16px;">Built for Integrators Who Can’t Afford Mistakes</h1>
                <p style="font-size: 18px; color: var(--c-dark-text-body); max-width: 700px; margin-bottom: 32px;">We execute your designs exactly to spec — clean, documented, and ready for inspection the first time.</p>
                <a href="/contact.html" class="btn btn-primary" style="padding: 16px 32px; font-size: 16px;">Talk to Dispatch</a>
            </div>
        </div>
    </section>

    <!-- 4. Main Content Sequence -->
    <section class="section bg-white">
        <div class="container">

            <!-- Intro Section -->
            <div style="max-width: 800px; margin: 0 auto 100px; text-align: center;">
                <h2 style="font-size: 40px; margin-bottom: 24px; font-family: var(--font-heading); color: var(--c-text-main);">We Work the Way Integrators Need Us To</h2>
                <p style="font-size: 20px; color: var(--c-text-body); line-height: 1.8;">You don’t need another contractor to manage. You need a team that shows up, follows your drawings, and gets it done without creating problems downstream. That’s how we operate.</p>
            </div>

            <!-- Why Integrators Choose Us (Using native svc-card system) -->
            <div style="margin-bottom: 100px;">
                <h2 style="font-size: 32px; margin-bottom: 48px; font-family: var(--font-heading); text-align: center;">Why Integrators Choose Us</h2>
                <div class="grid grid-3">
                    <div class="svc-card svc-dark">
                        <div class="svc-icon-wrap" style="margin-bottom: 24px;"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg></div>
                        <h3 style="font-size: 20px; margin-bottom: 12px;">We follow prints, not guesswork</h3>
                        <p style="font-size: 15px; color: var(--c-dark-text-body); line-height: 1.6;">Precision execution aligning 100% with your engineered blueprints.</p>
                    </div>
                    <div class="svc-card svc-light" style="box-shadow: 0 10px 30px rgba(0,0,0,0.08);">
                        <div class="svc-icon-wrap" style="margin-bottom: 24px;"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="4" y="4" width="16" height="16" rx="2" ry="2"></rect><rect x="9" y="9" width="6" height="6"></rect><line x1="9" y1="1" x2="9" y2="4"></line><line x1="15" y1="1" x2="15" y2="4"></line><line x1="9" y1="20" x2="9" y2="23"></line><line x1="15" y1="20" x2="15" y2="23"></line><line x1="20" y1="9" x2="23" y2="9"></line><line x1="20" y1="14" x2="23" y2="14"></line><line x1="1" y1="9" x2="4" y2="9"></line><line x1="1" y1="14" x2="4" y2="14"></line></svg></div>
                        <h3 style="font-size: 20px; margin-bottom: 12px; color: var(--c-text-main);">Clean rack builds</h3>
                        <p style="font-size: 15px; color: var(--c-text-body); line-height: 1.6;">Immaculate structured layouts, strict labeling, and flawless terminations.</p>
                    </div>
                    <div class="svc-card svc-dark">
                        <div class="svc-icon-wrap" style="margin-bottom: 24px;"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg></div>
                        <h3 style="font-size: 20px; margin-bottom: 12px;">No shortcuts</h3>
                        <p style="font-size: 15px; color: var(--c-dark-text-body); line-height: 1.6;">We never generate callbacks. Doing it right the very first time.</p>
                    </div>
                    <div class="svc-card svc-light" style="box-shadow: 0 10px 30px rgba(0,0,0,0.08);">
                        <div class="svc-icon-wrap" style="margin-bottom: 24px;"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg></div>
                        <h3 style="font-size: 20px; margin-bottom: 12px; color: var(--c-text-main);">Experienced teams</h3>
                        <p style="font-size: 15px; color: var(--c-text-body); line-height: 1.6;">Specialists trained explicitly for heavily structured, high-spec environments.</p>
                    </div>
                    <div class="svc-card svc-dark">
                        <div class="svc-icon-wrap" style="margin-bottom: 24px;"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path></svg></div>
                        <h3 style="font-size: 20px; margin-bottom: 12px;">Proper closeouts</h3>
                        <p style="font-size: 15px; color: var(--c-dark-text-body); line-height: 1.6;">Comprehensive documentation packages handed off immediately.</p>
                    </div>
                    <div class="svc-card svc-light" style="box-shadow: 0 10px 30px rgba(0,0,0,0.08);">
                        <div class="svc-icon-wrap" style="margin-bottom: 24px;"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line></svg></div>
                        <h3 style="font-size: 20px; margin-bottom: 12px; color: var(--c-text-main);">No babysitting</h3>
                        <p style="font-size: 15px; color: var(--c-text-body); line-height: 1.6;">Complete field autonomy without requiring external project management.</p>
                    </div>
                </div>
            </div>

            <!-- What We Handle -->
            <div style="background: var(--c-surface-light); border: 1px solid var(--c-border-light); padding: 60px 40px; border-radius: 16px; margin-bottom: 100px;">
                <h2 style="font-size: 28px; margin-bottom: 32px; font-family: var(--font-heading); text-align: center;">What We Handle in the Field</h2>
                <div class="grid grid-3" style="column-gap: 40px; row-gap: 24px;">
                    <div style="display: flex; align-items: center; gap: 16px;">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--c-accent)" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg>
                        <span style="font-size: 17px; font-weight: 500;">Cabling installs (fiber and copper)</span>
                    </div>
                    <div style="display: flex; align-items: center; gap: 16px;">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--c-accent)" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg>
                        <span style="font-size: 17px; font-weight: 500;">Rack buildouts (MDF/IDF)</span>
                    </div>
                    <div style="display: flex; align-items: center; gap: 16px;">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--c-accent)" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg>
                        <span style="font-size: 17px; font-weight: 500;">Camera and access control installs</span>
                    </div>
                    <div style="display: flex; align-items: center; gap: 16px;">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--c-accent)" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg>
                        <span style="font-size: 17px; font-weight: 500;">Device mounting and terminations</span>
                    </div>
                    <div style="display: flex; align-items: center; gap: 16px;">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--c-accent)" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg>
                        <span style="font-size: 17px; font-weight: 500;">Multi-site rollouts</span>
                    </div>
                    <div style="display: flex; align-items: center; gap: 16px;">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--c-accent)" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg>
                        <span style="font-size: 17px; font-weight: 500;">Cleanup and remediation</span>
                    </div>
                </div>
            </div>

            <!-- How We Show Up -->
            <div style="margin-bottom: 100px; text-align: center;">
                <h2 style="font-size: 32px; margin-bottom: 40px; font-family: var(--font-heading);">How We Show Up on Your Job</h2>
                <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 24px;">
                    <div style="background: #fff; border: 1px solid var(--c-border-light); padding: 16px 32px; border-radius: 8px; font-weight: 600; box-shadow: var(--sh-sm);">On time</div>
                    <div style="background: #fff; border: 1px solid var(--c-border-light); padding: 16px 32px; border-radius: 8px; font-weight: 600; box-shadow: var(--sh-sm);">Prepared</div>
                    <div style="background: #fff; border: 1px solid var(--c-border-light); padding: 16px 32px; border-radius: 8px; font-weight: 600; box-shadow: var(--sh-sm);">Aligned with your scope</div>
                    <div style="background: #fff; border: 1px solid var(--c-border-light); padding: 16px 32px; border-radius: 8px; font-weight: 600; box-shadow: var(--sh-sm);">Communicating clearly</div>
                    <div style="background: #fff; border: 1px solid var(--c-border-light); padding: 16px 32px; border-radius: 8px; font-weight: 600; box-shadow: var(--sh-sm);">Finishing clean</div>
                </div>
            </div>

             <!-- Testimonial -->
             <div style="margin-bottom: 100px; background: var(--c-surface-dark); padding: 60px; border-radius: 16px; position: relative;">
                <div style="position: absolute; top: 40px; left: 40px; opacity: 0.1;">
                     <svg width="80" height="80" viewBox="0 0 24 24" fill="currentColor"><path d="M10 11h-4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v4a2 2 0 0 1-2 2z"></path><path d="M22 11h-4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v4a2 2 0 0 1-2 2z"></path><path d="M12 21h-2a2 2 0 0 1-2-2v-4a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v4a2 2 0 0 1-2 2z"></path><path d="M22 21h-2a2 2 0 0 1-2-2v-4a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v4a2 2 0 0 1-2 2z"></path></svg>
                </div>
                <p style="font-size: 24px; color: #fff; line-height: 1.6; font-style: italic; max-width: 800px; margin: 0 auto; text-align: center; position: relative; z-index: 2;">“NTW came in on a job that had already gone sideways and got everything back on track. Easy to work with and got it done right.”</p>
                <div style="text-align: center; margin-top: 24px; position: relative; z-index: 2;">
                    <strong style="color: var(--c-accent); font-size: 16px; letter-spacing: 1px;">— Systems Integrator, NY</strong>
                </div>
             </div>

            <!-- Final CTA -->
            <div style="text-align: center;">
                <h2 style="font-size: 40px; margin-bottom: 16px; font-family: var(--font-heading); color: var(--c-text-main);">Need a Crew That Just Gets It Done?</h2>
                <p style="font-size: 20px; color: var(--c-text-body); max-width: 600px; margin: 0 auto 40px;">Send us the scope. We’ll take it from there.</p>
                <a href="/contact.html" class="btn btn-primary" style="padding: 16px 48px; font-size: 18px;">Talk to Dispatch</a>
            </div>

        </div>
    </section>
"""

with open('e:/websites/NTW/integrators.html', 'r', encoding='utf-8') as f:
    content = f.read()

start_idx = content.find('<!-- 3. Hero Section (Subpage Profile) -->')
end_idx = content.find('<script src="/js/main.js">')

new_content = content[:start_idx] + html_body + '\\n    ' + content[end_idx:]

with open('e:/websites/NTW/integrators.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Integrators page successfully upgraded.")
