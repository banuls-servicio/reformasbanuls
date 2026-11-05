cookie_css = """

/* ==========================================================================
   COOKIE CONSENT BANNER (RGPD / LOPD-GDD / AEPD Compliant)
   ========================================================================== */
.cookie-banner {
  position: fixed;
  bottom: 1.5rem;
  left: 1.5rem;
  right: 1.5rem;
  max-width: 500px;
  background: rgba(15, 23, 42, 0.98);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  color: #F8FAFC;
  padding: 1.25rem 1.5rem;
  border-radius: var(--radius-lg, 16px);
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4);
  border: 1px solid rgba(255, 255, 255, 0.15);
  z-index: 999999;
  display: none;
  animation: slideUpCookie 0.35s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}

@keyframes slideUpCookie {
  from { transform: translateY(40px); opacity: 0; }
  to { transform: translateY(0); opacity: 1; }
}

.cookie-banner-title {
  font-size: 0.95rem;
  font-weight: 700;
  margin-bottom: 0.4rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  color: #FFFFFF;
}

.cookie-banner-text {
  font-size: 0.8rem;
  color: #94A3B8;
  line-height: 1.45;
  margin-bottom: 1rem;
}

.cookie-banner-text a {
  color: #38BDF8;
  text-decoration: underline;
}

.cookie-banner-actions {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  flex-wrap: wrap;
}

.btn-cookie-accept {
  background: #10B981;
  color: #FFFFFF;
  border: none;
  padding: 0.5rem 1.15rem;
  font-size: 0.825rem;
  font-weight: 700;
  border-radius: 8px;
  cursor: pointer;
  transition: background 0.2s;
}

.btn-cookie-accept:hover {
  background: #059669;
}

.btn-cookie-reject {
  background: rgba(255, 255, 255, 0.08);
  color: #CBD5E1;
  border: 1px solid rgba(255, 255, 255, 0.15);
  padding: 0.5rem 0.9rem;
  font-size: 0.825rem;
  font-weight: 600;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.2s;
}

.btn-cookie-reject:hover {
  background: rgba(255, 255, 255, 0.18);
  color: #FFFFFF;
}

@media (max-width: 640px) {
  .cookie-banner {
    left: 1rem;
    right: 1rem;
    bottom: 5.5rem; /* leave room for mobile sticky bar */
    padding: 1rem 1.15rem;
  }
}
"""

paths = [
    r'c:\Users\edgvi\Documents\webleadsagent\css\style.css',
    r'C:\Users\edgvi\Documents\ventanasbanuls\css\style.css'
]

for p in paths:
    with open(p, 'a', encoding='utf-8') as f:
        f.write(cookie_css)
    print(f'Appended cookie banner CSS to {p}')
