with open(r'c:\Users\edgvi\Documents\webleadsagent\css\style.css', 'r', encoding='utf-8') as f:
    css = f.read()

new_styles = """

/* ==========================================================================
   GEO-SATELLITE & MULTI-LOCAL ENHANCEMENTS
   ========================================================================== */
.hero-lead-card {
  background: #FFFFFF;
  border: 1px solid #E2E8F0;
  border-radius: var(--radius-lg, 16px);
  padding: 1.75rem;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
  margin-top: 1.25rem;
}

.mobile-quick-bar {
  display: none;
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  background: rgba(15, 23, 42, 0.96);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border-top: 1px solid rgba(255, 255, 255, 0.12);
  padding: 0.65rem 1rem;
  z-index: 9999;
}

.mobile-quick-inner {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0.75rem;
  max-width: 480px;
  margin: 0 auto;
}

.mobile-quick-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.4rem;
  padding: 0.65rem 0.75rem;
  font-size: 0.85rem;
  font-weight: 700;
  border-radius: 8px;
  text-decoration: none;
  text-align: center;
  white-space: nowrap;
}

.mobile-quick-call {
  background: #FFFFFF;
  color: #0F172A;
}

.mobile-quick-wa {
  background: #25D366;
  color: #FFFFFF;
}

@media (max-width: 768px) {
  .mobile-quick-bar {
    display: block;
  }
}

/* Comarcal Coverage Footer Block */
.comarcal-coverage-block {
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  padding-top: 2rem;
  margin-top: 2.5rem;
  text-align: center;
}

.comarcal-coverage-title {
  font-size: 0.875rem;
  font-weight: 700;
  color: #E2E8F0;
  text-transform: uppercase;
  letter-spacing: 1px;
  margin-bottom: 0.75rem;
}

.comarcal-links {
  font-size: 0.85rem;
  color: #94A3B8;
  line-height: 1.8;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 0.5rem 0.75rem;
}

.comarcal-links a {
  color: #CBD5E1;
  text-decoration: none;
  transition: color 0.2s;
}

.comarcal-links a:hover {
  color: #38BDF8;
  text-decoration: underline;
}

/* Guarantee Section Grid */
.guarantee-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1.5rem;
  margin-top: 2.5rem;
}

.guarantee-card {
  background: #FFFFFF;
  border: 1px solid #E2E8F0;
  border-radius: var(--radius-md, 12px);
  padding: 1.75rem;
  text-align: center;
  transition: transform var(--transition-smooth);
}

.guarantee-card:hover {
  transform: translateY(-3px);
  box-shadow: var(--shadow-card);
}

.guarantee-icon {
  font-size: 2rem;
  margin-bottom: 0.75rem;
}

.guarantee-card h4 {
  font-size: 1.05rem;
  color: var(--color-architect-dark);
  margin-bottom: 0.4rem;
}

.guarantee-card p {
  font-size: 0.875rem;
  color: var(--color-text-secondary);
  line-height: 1.5;
}

@media (max-width: 900px) {
  .guarantee-grid {
    grid-template-columns: 1fr 1fr;
  }
}

@media (max-width: 600px) {
  .guarantee-grid {
    grid-template-columns: 1fr;
  }
}
"""

if '.hero-lead-card' not in css:
    css += new_styles
    with open(r'c:\Users\edgvi\Documents\webleadsagent\css\style.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print("Appended geo-satellite styles to style.css")
else:
    print("Styles already present")
