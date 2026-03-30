import json

with open("e:/websites/NTW/index.html", "r", encoding="utf-8") as f:
    c = f.read()

# 1. Add MSPs
msp_str = '<li style="display: flex; align-items: center; gap: 24px; font-size: 22px; color: #1e293b; font-weight: 600; letter-spacing: -0.5px;"><svg width="24" height="24" fill="none" stroke="#0f172a" stroke-width="3"><polyline points="20 6 9 17 4 12"></polyline></svg> MSPs</li>'

if 'Multi-Site Operators</li>' in c:
    c = c.replace('Multi-Site Operators</li>', 'Multi-Site Operators</li>\n                        ' + msp_str)
elif 'Multi-Site Operators' in c:
    # Handle if Prettier split it
    lines = c.split('\n')
    for i, line in enumerate(lines):
        if 'Multi-Site Operators' in line:
            lines.insert(i+1, '                        ' + msp_str)
            break
    c = '\n'.join(lines)
else:
    print('Failed to find Multi-Site Operators')

# 2. Fix Territories
# Often split across lines
primary_heading = 'Primary Territories'

lines = c.split('\n')
for i, line in enumerate(lines):
    if primary_heading in line:
        # the next div contains the territories
        for j in range(i+1, i+10):
            if '<div ' in lines[j] and 'Fairfield County' in lines[j]:
                lines[j] = '                        <div style="color: #0f172a; font-size: 20px; font-weight: 700;">Connecticut &nbsp;&middot;&nbsp; New York &nbsp;&middot;&nbsp; New Jersey</div>'
                # insert secondary below it
                lines.insert(j+1, '                        <span style="font-weight: 700; color: #94a3b8; text-transform: uppercase; letter-spacing: 1px; font-size: 13px; display: block; margin-top: 32px; margin-bottom: 16px;">Secondary Territories</span>')
                lines.insert(j+2, '                        <div style="color: #0f172a; font-size: 16px; font-weight: 600; line-height: 1.6;">Pennsylvania &nbsp;&middot;&nbsp; Maryland &nbsp;&middot;&nbsp; DC &nbsp;&middot;&nbsp; Delaware &nbsp;&middot;&nbsp; Rhode Island &nbsp;&middot;&nbsp; Massachusetts &nbsp;&middot;&nbsp; New Hampshire &nbsp;&middot;&nbsp; Vermont &nbsp;&middot;&nbsp; Maine</div>')
                break
        break
c = '\n'.join(lines)

with open("e:/websites/NTW/index.html", "w", encoding="utf-8") as f:
    f.write(c)

print('Done editing index.html')
