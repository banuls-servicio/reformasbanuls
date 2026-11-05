import os
import re

BASE_URL = "https://xn--reformasbauls-rkb.com/"
VENTANAS_URL = "https://xn--ventanasbauls-rkb.com/"
PHONE_DISPLAY = "601 28 13 13"
PHONE_TEL = "+34601281313"
ADDRESS = "Carrer Murillo, 41, 03802 Alcoi (Alicante)"
EMAIL = "Jandrobleal@gmail.com"
MAPS_URL = "https://share.google/EFxHTu7dtLrR4XIMK"
AREA_SERVED_JSON = """[
          {"@type": "City", "name": "Alcoy"},
          {"@type": "City", "name": "Cocentaina"},
          {"@type": "City", "name": "Muro de Alcoy"},
          {"@type": "City", "name": "Ibi"},
          {"@type": "City", "name": "Onil"},
          {"@type": "City", "name": "Castalla"},
          {"@type": "City", "name": "Banyeres de Mariola"},
          {"@type": "City", "name": "Benimarfull"},
          {"@type": "City", "name": "Planes"},
          {"@type": "City", "name": "Benilloba"}
        ]"""

COMARCAL_FOOTER_HTML = """
      <!-- Bloque completo de cobertura comarcal SEO Local -->
      <div class="comarcal-coverage-block">
        <div class="comarcal-coverage-title">Reformas en L'Alcoià y El Comtat</div>
        <div class="comarcal-links">
          <a href="index.html">Alcoy</a> ·
          <a href="reformas-cocentaina.html">Cocentaina</a> ·
          <a href="reformas-muro-de-alcoy.html">Muro de Alcoy</a> ·
          <a href="reformas-ibi.html">Ibi</a> ·
          <a href="reformas-onil.html">Onil</a> ·
          <a href="reformas-el-comtat.html">Castalla</a> ·
          <a href="reformas-el-comtat.html">Banyeres de Mariola</a> ·
          <a href="reformas-el-comtat.html">Benimarfull</a> ·
          <a href="reformas-el-comtat.html">Planes</a> ·
          <a href="reformas-el-comtat.html">Benilloba</a> ·
          <a href="reformas-el-comtat.html">El Comtat</a>
        </div>
      </div>
"""

# 1. Update index.html
with open(r'c:\Users\edgvi\Documents\webleadsagent\index.html', 'r', encoding='utf-8') as f:
    idx_content = f.read()

# Remove heritage-pill from hero in index.html to give clean total prominence to H1
idx_content = re.sub(r'<div class="heritage-pill">[\s\S]*?</div>\s*', '', idx_content)

# Ensure nav links include Ventanas & Taller
if 'Ventanas &amp; Taller' not in idx_content and 'Ventanas & Taller' not in idx_content:
    idx_content = idx_content.replace(
        '<li><a href="#contacto" class="nav-link">Contacto</a></li>',
        '<li><a href="https://xn--ventanasbauls-rkb.com/" class="nav-link" target="_blank" rel="noopener" title="Taller propio de ventanas y cerramientos">🪟 Ventanas &amp; Taller ↗</a></li>\n          <li><a href="#contacto" class="nav-link">Contacto</a></li>'
    )

# Update Schema areaServed in index.html
idx_content = re.sub(r'"areaServed":\s*\[[\s\S]*?\]', f'"areaServed": {AREA_SERVED_JSON}', idx_content)

# Update GeneralContractor in @type
idx_content = idx_content.replace(
    '"@type": ["HomeAndConstructionBusiness", "LocalBusiness"]',
    '"@type": ["GeneralContractor", "HomeAndConstructionBusiness", "LocalBusiness"]'
)

# Insert comarcal footer block if not already there
if 'comarcal-coverage-block' not in idx_content:
    idx_content = idx_content.replace(
        '<div class="footer-bottom">',
        f'{COMARCAL_FOOTER_HTML}\n      <div class="footer-bottom">'
    )

# Save updated index.html
with open(r'c:\Users\edgvi\Documents\webleadsagent\index.html', 'w', encoding='utf-8') as f:
    f.write(idx_content)
print("Updated index.html successfully")

# 2. Template generator for 11 canonical sections
def create_landing(slug, location_name, h1_title, meta_desc, aeo_text, problem_items, solution_features, comp_winner_items, comp_loser_items, reviews_list, process_steps, faq_items, guarantees_list):
    canonical_url = f"{BASE_URL}{slug}"
    
    # Generate Schema FAQ
    faq_schema = []
    for q, a in faq_items:
        faq_schema.append(f"""          {{
            "@type": "Question",
            "name": "{q}",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "{a}"
            }}
          }}""")
    faq_schema_str = ",\n".join(faq_schema)

    # Generate Reviews HTML
    reviews_html = ""
    for name, tag, stars, quote, time in reviews_list:
        initial = name[0]
        reviews_html += f"""
          <div class="google-review-card">
            <div>
              <div class="google-reviewer-meta">
                <div class="google-avatar">{initial}</div>
                <div>
                  <strong style="color: #0F172A; display: block; font-size: 0.95rem;">{name}</strong>
                  <span class="google-verified-tag">✓ {tag}</span>
                </div>
              </div>
              <div class="google-stars" style="font-size: 0.95rem; margin-bottom: 0.75rem;">{stars}</div>
              <p style="font-size: 0.925rem; line-height: 1.55; color: #334155;">
                "{quote}"
              </p>
            </div>
            <span style="font-size: 0.75rem; color: #94A3B8; margin-top: 1rem;">{time}</span>
          </div>"""

    # Generate Problem cards HTML
    problem_html = ""
    for icon, title, desc in problem_items:
        problem_html += f"""
          <div class="problem-card">
            <div class="problem-icon">{icon}</div>
            <h3>{title}</h3>
            <p>{desc}</p>
          </div>"""

    # Generate Process Steps HTML
    steps_html = ""
    for num, title, desc in process_steps:
        steps_html += f"""
          <div class="step-card">
            <div class="step-number">{num}</div>
            <h3>{title}</h3>
            <p>{desc}</p>
          </div>"""

    # Generate FAQ Accordion HTML
    faq_html = ""
    for q, a in faq_items:
        faq_html += f"""
          <details class="faq-item">
            <summary class="faq-summary">
              <span>{q}</span>
              <span class="faq-toggle">+</span>
            </summary>
            <div class="faq-answer">
              <p>{a}</p>
            </div>
          </details>"""

    # Generate Guarantees HTML
    guarantees_html = ""
    for icon, title, desc in guarantees_list:
        guarantees_html += f"""
          <div class="guarantee-card">
            <div class="guarantee-icon">{icon}</div>
            <h4>{title}</h4>
            <p>{desc}</p>
          </div>"""

    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  
  <!-- Canonical & Search Engine Meta -->
  <title>{h1_title} | Reformas Bañuls</title>
  <meta name="description" content="{meta_desc}">
  <link rel="canonical" href="{canonical_url}">
  <meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large">

  <!-- Open Graph -->
  <meta property="og:type" content="business.business">
  <meta property="og:title" content="{h1_title} | Reformas Bañuls">
  <meta property="og:description" content="{meta_desc}">
  <meta property="og:url" content="{canonical_url}">
  <meta property="og:image" content="{BASE_URL}assets/img/reforma-bano.jpg">
  <meta property="business:contact_data:street_address" content="Carrer Murillo, 41">
  <meta property="business:contact_data:locality" content="Alcoi">
  <meta property="business:contact_data:postal_code" content="03802">

  <!-- Typography & Assets -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/style.css">

  <!-- Schema.org JSON-LD -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": ["GeneralContractor", "HomeAndConstructionBusiness", "LocalBusiness"],
        "@id": "{canonical_url}#organization",
        "name": "Reformas Bañuls - {location_name}",
        "alternateName": ["Proyectos Bañuls", "Reformas y Ventanas Bañuls"],
        "url": "{canonical_url}",
        "telephone": "+34601281313",
        "email": "{EMAIL}",
        "address": {{
          "@type": "PostalAddress",
          "streetAddress": "Carrer Murillo, 41",
          "addressLocality": "Alcoi",
          "addressRegion": "Alicante",
          "postalCode": "03802",
          "addressCountry": "ES"
        }},
        "areaServed": [
          {{"@type": "City", "name": "{location_name}"}},
          {{"@type": "City", "name": "Alcoy"}},
          {{"@type": "AdministrativeArea", "name": "L'Alcoià"}},
          {{"@type": "AdministrativeArea", "name": "El Comtat"}}
        ],
        "sameAs": [
          "{MAPS_URL}",
          "https://www.instagram.com/proyectos.banuls/"
        ]
      }},
      {{
        "@type": "FAQPage",
        "@id": "{canonical_url}#faq",
        "mainEntity": [
{faq_schema_str}
        ]
      }}
    ]
  }}
  </script>
  <script src="js/analytics.js" defer></script>
</head>
<body>

  <!-- Top Ecosystem Network Bar -->
  <div class="network-bar">
    <div class="container network-bar-inner">
      <div class="network-bar-label">
        <span>Familia Bañuls Alcoy · Desde 1964:</span>
        <span class="network-badge">División Reformas</span>
      </div>
      <div class="network-links">
        <a href="{VENTANAS_URL}" class="network-link" target="_blank" rel="noopener" title="Ir a Ventanas Bañuls (Taller Oficial)">
          🪟 Ventanas Bañuls
        </a>
        <span class="net-separator" style="color: #334155;">|</span>
        <span class="network-link active">
          🔨 Reformas Bañuls
        </span>
      </div>
    </div>
  </div>

  <!-- Header -->
  <header class="site-header">
    <div class="container header-inner">
      <a href="index.html" class="brand-logo" title="Reformas Bañuls">
        <img src="assets/img/logo-oficial-banuls.png" alt="Reformas Bañuls" width="160" height="42">
        <span class="brand-division-tag">REFORMAS</span>
      </a>
      
      <nav aria-label="Navegación principal">
        <ul class="nav-links">
          <li><a href="index.html" class="nav-link">Inicio</a></li>
          <li><a href="reformas-integrales-alcoy.html" class="nav-link">Integrales</a></li>
          <li><a href="reforma-banos-alcoy.html" class="nav-link">Baños</a></li>
          <li><a href="reforma-cocinas-alcoy.html" class="nav-link">Cocinas</a></li>
          <li><a href="{VENTANAS_URL}" class="nav-link" target="_blank" rel="noopener">🪟 Ventanas &amp; Taller ↗</a></li>
          <li><a href="#contacto" class="nav-link">Contacto</a></li>
        </ul>
      </nav>

      <div class="header-actions">
        <a href="tel:{PHONE_TEL}" class="phone-badge">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
          {PHONE_DISPLAY}
        </a>
        <a href="#contacto" class="btn btn-primary">Pedir Presupuesto</a>
      </div>
    </div>
  </header>

  <main>
    <!-- SECTION 1: HERO & AEO EXTRACTION BLOCK -->
    <section class="section hero-section">
      <div class="container hero-grid">
        <div class="hero-content">
          <h1>{h1_title}</h1>

          <!-- SECTION 1B: AEO DIRECT ANSWER (45-60 words) -->
          <div class="aeo-extraction-block" role="region" aria-label="Resumen verificado de servicio">
            <p>{aeo_text}</p>
          </div>

          <div class="hero-lead-card">
            <p style="font-size: 0.95rem; color: #475569; line-height: 1.6; margin-bottom: 1.25rem;">
              Coordinamos todos los gremios (albañilería, fontanería, electricidad, pintura y cerramientos de taller propio). <strong>Presupuesto cerrado por contrato sin sorpresas</strong> y cumplimiento estricto de plazos garantizado por escrito.
            </p>
            <div class="hero-actions">
              <a href="https://wa.me/34601281313?text=Hola%20Reformas%20Bañuls,%20solicito%20presupuesto%20para%20una%20reforma%20en%20{location_name}" target="_blank" rel="noopener" class="btn btn-whatsapp">
                Pedir Presupuesto por WhatsApp
              </a>
              <a href="tel:{PHONE_TEL}" class="btn btn-secondary">
                Llamar al {PHONE_DISPLAY}
              </a>
            </div>
          </div>
        </div>

        <div class="hero-visual-wrapper">
          <img src="assets/img/reforma-salon-luz.jpg" alt="Reforma integral en {location_name} por Reformas Bañuls" width="800" height="480" loading="eager">
          <div class="hero-floating-card">
            <div>
              <div class="floating-stat-num">Taller a Minutos</div>
              <div class="floating-stat-lbl">Sin sobrecoste por viaje</div>
            </div>
            <div>
              <div class="floating-stat-num">Contrato Cerrado</div>
              <div class="floating-stat-lbl">Precio final sin extras</div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 2: PROBLEMA LOCAL EN EL MUNICIPIO -->
    <section class="section section-muted" id="problema-local">
      <div class="container">
        <div style="text-align: center; max-width: 760px; margin: 0 auto;">
          <h2>Los Retos Habituales de Reformar en {location_name}</h2>
          <p class="text-lead" style="margin-top: 0.5rem;">
            Conocemos la tipología constructiva de la zona, sus ordenanzas y las peculiaridades de cada inmueble:
          </p>
        </div>

        <div class="problem-grid" style="margin-top: 2.5rem;">
          {problem_html}
        </div>
      </div>
    </section>

    <!-- SECTION 3: SOLUCIÓN BAÑULS CON TALLER PROPIO EN MURILLO 41 -->
    <section class="section" id="solucion-taller">
      <div class="container hero-grid" style="align-items: center;">
        <div>
          <h2>La Ventaja Bañuls: Taller Propio a Minutos de {location_name}</h2>
          <p class="text-lead" style="margin-top: 0.75rem;">
            A diferencia de reformistas que compran ventanas o mamparas a intermediarios con semanas de retraso, nosotros fabricamos a medida en nuestro propio taller de Carrer Murillo 41 (Alcoy):
          </p>
          <div style="margin-top: 1.5rem; display: flex; flex-direction: column; gap: 1rem;">
            {solution_features}
          </div>
          <div style="margin-top: 2rem;">
            <a href="{VENTANAS_URL}" target="_blank" rel="noopener" class="btn btn-secondary">
              Conocer nuestro taller técnico de ventanas y cerramientos ↗
            </a>
          </div>
        </div>

        <div class="hero-visual-wrapper">
          <img src="assets/img/reforma-cocina.jpg" alt="Cocina y cerramientos de taller propio en {location_name}" width="800" height="480" loading="lazy">
        </div>
      </div>
    </section>

    <!-- SECTION 4: TABLA COMPARATIVA -->
    <section class="section section-muted" id="comparativa">
      <div class="container">
        <div style="text-align: center; max-width: 760px; margin: 0 auto;">
          <h2>¿Por Qué Confiar en Reformas Bañuls en {location_name}?</h2>
          <p class="text-lead" style="margin-top: 0.5rem;">
            La tranquilidad de tratar con una empresa física consolidada frente a subcontratas informales:
          </p>
        </div>

        <div class="comparison-grid">
          <div class="comparison-card comparison-card-winner">
            <span style="font-size: 0.8rem; font-weight: 800; color: #16A34A; text-transform: uppercase; letter-spacing: 1px;">Elección Segura</span>
            <h3 style="margin-top: 0.4rem;">Reformas Bañuls</h3>
            <ul class="comparison-list">
              {comp_winner_items}
            </ul>
          </div>

          <div class="comparison-card comparison-card-loser">
            <span style="font-size: 0.8rem; font-weight: 800; color: #DC2626; text-transform: uppercase; letter-spacing: 1px;">Riesgo para tu vivienda</span>
            <h3 style="margin-top: 0.4rem;">Reformistas Sin Taller / Subcontratas</h3>
            <ul class="comparison-list">
              {comp_loser_items}
            </ul>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 5: RESEÑAS VERIFICADAS GOOGLE BUSINESS (4-5 ESTRELLAS) -->
    <section class="google-reviews-section" id="resenas">
      <div class="container">
        <div style="text-align: center; max-width: 720px; margin: 0 auto;">
          <h2>Opiniones Reales de Clientes en Google Business</h2>
          <p class="text-lead" style="margin-top: 0.5rem;">
            Valoraciones verificadas de propietarios de la comarca:
          </p>
        </div>

        <div class="google-badge-header" style="margin-top: 1.75rem;">
          <div class="google-rating-box">
            <svg width="24" height="24" viewBox="0 0 24 24"><path fill="#4285F4" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"/><path fill="#34A853" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"/><path fill="#FBBC05" d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.06H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.94l2.85-2.22.81-.63z"/><path fill="#EA4335" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.06l3.66 2.84c.87-2.6 3.3-4.52 6.16-4.52z"/></svg>
            <strong style="font-size: 1.35rem; color: #0F172A;">4.9 / 5.0</strong>
            <span class="google-stars">★★★★★</span>
            <span style="color: #64748B; font-size: 0.85rem;">(Google Maps Verificado)</span>
          </div>

          <a href="{MAPS_URL}" target="_blank" rel="noopener" class="btn btn-secondary" style="font-size: 0.85rem; padding: 0.6rem 1.25rem;">
            Ver todas las reseñas en Google →
          </a>
        </div>

        <div class="google-reviews-grid">
          {reviews_html}
        </div>
      </div>
    </section>

    <!-- SECTION 6: CTA INTERMEDIO DESTACADO -->
    <section class="section" style="background: var(--color-architect-dark); color: #FFFFFF; text-align: center; padding: 4.5rem 0;">
      <div class="container" style="max-width: 760px;">
        <span style="color: #38BDF8; font-weight: 700; text-transform: uppercase; font-size: 0.85rem; letter-spacing: 1px;">Visita Técnica Sin Compromiso</span>
        <h2 style="color: #FFFFFF; margin-top: 0.5rem; font-size: 2.25rem;">¿Tienes una casa o piso para reformar en {location_name}?</h2>
        <p style="color: #CBD5E1; font-size: 1.05rem; margin-top: 0.75rem; line-height: 1.6;">
          Nos desplazamos a tu vivienda en menos de 48 horas para tomar mediciones exactas y asesorarte sobre distribución, licencias municipales y ahorro en materiales.
        </p>
        <div style="margin-top: 2rem; display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap;">
          <a href="https://wa.me/34601281313?text=Hola%20Bañuls,%20quiero%20coordinar%20una%20visita%20técnica%20en%20{location_name}" target="_blank" rel="noopener" class="btn btn-whatsapp" style="font-size: 1rem; padding: 0.9rem 1.75rem;">
            Agendar Visita por WhatsApp
          </a>
          <a href="tel:{PHONE_TEL}" class="btn btn-secondary" style="background: rgba(255,255,255,0.1); color: #FFFFFF; border-color: rgba(255,255,255,0.2);">
            Llamar: {PHONE_DISPLAY}
          </a>
        </div>
      </div>
    </section>

    <!-- SECTION 7: PROCESO EN 4 PASOS -->
    <section class="section" id="proceso">
      <div class="container">
        <div style="text-align: center; max-width: 720px; margin: 0 auto;">
          <h2>Tu Reforma en 4 Pasos: Transparente y Sin Estrés</h2>
          <p class="text-lead" style="margin-top: 0.5rem;">Metodología contrastada en tres generaciones de oficio:</p>
        </div>

        <div class="steps-grid" style="margin-top: 2.5rem;">
          {steps_html}
        </div>
      </div>
    </section>

    <!-- SECTION 8: SLIDER ANTES / DESPUÉS TÁCTIL -->
    <section class="section section-muted" id="antes-despues">
      <div class="container">
        <div style="text-align: center; max-width: 740px; margin: 0 auto 2.5rem;">
          <h2>Transformación Real: Desliza para Ver el Cambio</h2>
          <p class="text-lead">Arrastra el control central para comparar el estado previo frente a los acabados definitivos de Bañuls:</p>
        </div>

        <div style="max-width: 880px; margin: 0 auto;">
          <div class="ba-slider-container">
            <img src="assets/img/reforma-bano.jpg" alt="Después: Reforma impecable con mampara y porcelánico" class="ba-image-before">
            <div class="ba-image-after">
              <img src="assets/img/antes-bano.jpg" alt="Antes: Baño anticuado con bañera">
            </div>
            <div class="ba-slider-handle"></div>
          </div>
          <p style="text-align: center; font-size: 0.85rem; color: #64748B; margin-top: 1rem;">
            👆 Arrastra la barra o haz clic sobre la imagen para apreciar la diferencia de acabados.
          </p>
        </div>
      </div>
    </section>

    <!-- SECTION 9: FAQ DE 6 PREGUNTAS CON RESPUESTAS LOCALES -->
    <section class="section" id="faq">
      <div class="container">
        <div style="text-align: center; max-width: 740px; margin: 0 auto;">
          <h2>Preguntas Frecuentes sobre Reformas en {location_name}</h2>
          <p class="text-lead" style="margin-top: 0.5rem;">Respuestas directas sobre plazos, costes, licencias municipales y garantías:</p>
        </div>

        <div class="faq-accordion">
          {faq_html}
        </div>
      </div>
    </section>

    <!-- SECTION 10: GARANTÍAS BAÑULS -->
    <section class="section section-muted" id="garantias">
      <div class="container">
        <div style="text-align: center; max-width: 740px; margin: 0 auto;">
          <h2>Tranquilidad Total: Nuestras 4 Garantías por Escrito</h2>
          <p class="text-lead" style="margin-top: 0.5rem;">Protegemos tu inversión de principio a fin:</p>
        </div>

        <div class="guarantee-grid">
          {guarantees_html}
        </div>
      </div>
    </section>

    <!-- SECTION 11: CTA FINAL Y FORMULARIO CON MAPA -->
    <section class="section" id="contacto">
      <div class="container">
        <div class="contact-grid">
          <div class="contact-form-wrapper">
            <h3>Pide Presupuesto para tu Reforma en {location_name}</h3>
            <p style="color: #64748B; font-size: 0.925rem; margin-top: 0.35rem; margin-bottom: 1.5rem;">
              Te responderemos en menos de 24 horas para fijar la visita técnica gratuita:
            </p>

            <form id="quick-quote-form">
              <div class="form-group">
                <label for="quote-name">Nombre y Apellidos</label>
                <input type="text" id="quote-name" class="form-control" placeholder="Ej: Vicent Jordá" required>
              </div>

              <div class="form-group">
                <label for="quote-phone">Teléfono de Contacto</label>
                <input type="tel" id="quote-phone" class="form-control" placeholder="Ej: 600 000 000" required>
              </div>

              <div class="form-group">
                <label for="quote-service">Tipo de Proyecto</label>
                <select id="quote-service" class="form-control">
                  <option value="Reforma Integral en {location_name}">Reforma Integral de Vivienda</option>
                  <option value="Reforma de Cocina en {location_name}">Reforma de Cocina Contemporánea</option>
                  <option value="Reforma de Baño en {location_name}">Reforma de Baño &amp; Mampara</option>
                  <option value="Cerramiento o Porche en {location_name}">Cerramiento / Porche / Ventanas</option>
                </select>
              </div>

              <div class="form-group">
                <label for="quote-location">Población / Zona</label>
                <input type="text" id="quote-location" class="form-control" value="{location_name}" required>
              </div>

              <div class="form-group">
                <label for="quote-notes">Detalles de la reforma (opcional)</label>
                <textarea id="quote-notes" class="form-control" rows="3" placeholder="Metros aprox, estado actual, tirar tabiques, etc."></textarea>
              </div>

              <button type="submit" class="btn btn-primary" style="width: 100%; padding: 0.95rem;">
                Enviar Solicitud de Presupuesto
              </button>
            </form>
          </div>

          <div class="contact-info-wrapper">
            <h3>Dónde Encontrarnos</h3>
            <p style="color: #64748B; font-size: 0.95rem; margin-top: 0.5rem; margin-bottom: 1.5rem;">
              Nuestra exposición y taller físico en Alcoy, a minutos de {location_name}:
            </p>

            <div style="background: #FFFFFF; border: 1px solid #E2E8F0; padding: 1.5rem; border-radius: var(--radius-md); margin-bottom: 1.5rem; font-size: 0.9rem; line-height: 1.6;">
              <p>📍 <strong>Dirección:</strong> {ADDRESS}</p>
              <p>📞 <strong>Teléfono directo:</strong> <a href="tel:{PHONE_TEL}" style="color: #0F172A; font-weight: 700;">{PHONE_DISPLAY}</a></p>
              <p>✉️ <strong>Email:</strong> {EMAIL}</p>
              <p>📸 <strong>Instagram:</strong> @proyectos.banuls</p>
              <p>⏱️ <strong>Horario:</strong> Lunes a Viernes de 9:00 a 14:00 y de 16:30 a 20:00</p>
            </div>

            <div style="border-radius: var(--radius-md); overflow: hidden; height: 280px; border: 1px solid #E2E8F0;">
              <iframe 
                src="https://maps.google.com/maps?q=Carrer+Murillo+41+Alcoi+Alicante&t=&z=16&ie=UTF8&iwloc=&output=embed" 
                title="Ubicación de Reformas Bañuls en Google Maps" 
                width="100%" 
                height="100%" 
                style="border:0;" 
                loading="lazy">
              </iframe>
            </div>
          </div>
        </div>
      </div>
    </section>
  </main>

  <!-- Mobile Quick Sticky Bar -->
  <aside class="mobile-quick-bar" aria-label="Contacto rápido móvil">
    <div class="mobile-quick-inner">
      <a href="tel:{PHONE_TEL}" class="mobile-quick-btn mobile-quick-call">
        📞 Llamar al Estudio
      </a>
      <a href="https://wa.me/34601281313?text=Hola%20Reformas%20Bañuls,%20solicito%20presupuesto%20para%20{location_name}" class="mobile-quick-btn mobile-quick-wa" target="_blank" rel="noopener">
        💬 WhatsApp Directo
      </a>
    </div>
  </aside>

  <!-- Site Footer -->
  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-col">
          <img src="assets/img/logo-oficial-banuls-white.png" alt="Bañuls Alcoy" width="150" height="40" style="margin-bottom: 1.25rem;">
          <p style="color: #94A3B8; font-size: 0.9rem; max-width: 320px;">
            Estudio familiar especializado en reformas integrales, cocinas y baños en Alcoy, {location_name} y toda la comarca desde 1964.
          </p>
          <div style="margin-top: 1rem;">
            <a href="{VENTANAS_URL}" target="_blank" rel="noopener" style="color: #38BDF8; font-size: 0.85rem; font-weight: 700; text-decoration: underline;">
              🪟 Taller Propio: Visita ventanasbañuls.com →
            </a>
          </div>
        </div>

        <div class="footer-col">
          <h4>Especialidades</h4>
          <ul class="footer-links">
            <li><a href="reformas-integrales-alcoy.html">Reformas Integrales</a></li>
            <li><a href="reforma-banos-alcoy.html">Reformas de Baño &amp; Mamparas</a></li>
            <li><a href="reforma-cocinas-alcoy.html">Cocinas Vanguardistas</a></li>
            <li><a href="{VENTANAS_URL}" target="_blank" rel="noopener">Ventanas &amp; Taller Propio ↗</a></li>
          </ul>
        </div>

        <div class="footer-col">
          <h4>Zonas Destacadas</h4>
          <ul class="footer-links">
            <li><a href="index.html">Alcoy (Sede Murillo 41)</a></li>
            <li><a href="reformas-cocentaina.html">Cocentaina</a></li>
            <li><a href="reformas-muro-de-alcoy.html">Muro de Alcoy</a></li>
            <li><a href="reformas-ibi.html">Ibi</a></li>
            <li><a href="reformas-onil.html">Onil</a></li>
            <li><a href="reformas-el-comtat.html">El Comtat (Pueblos Rústicos)</a></li>
          </ul>
        </div>

        <div class="footer-col">
          <h4>Contacto &amp; Ubicación</h4>
          <p style="color: #94A3B8; font-size: 0.875rem; margin-bottom: 0.5rem;">{ADDRESS}</p>
          <p style="color: #94A3B8; font-size: 0.875rem; margin-bottom: 0.5rem;">Teléfono: {PHONE_DISPLAY}</p>
          <p style="color: #94A3B8; font-size: 0.875rem; margin-bottom: 1rem;">Email: {EMAIL}</p>
          <a href="{MAPS_URL}" target="_blank" rel="noopener" class="btn btn-secondary" style="font-size: 0.8rem; padding: 0.5rem 1rem;">
            Abrir Ficha Google Maps
          </a>
        </div>
      </div>

{COMARCAL_FOOTER_HTML}

      <div class="footer-bottom">
        <div>
          © 2026 Reformas Bañuls. Todos los derechos reservados. Carrer Murillo 41, 03802 Alcoi (Alicante).
        </div>
        <div style="display: flex; gap: 1.5rem; flex-wrap: wrap;">
          <a href="aviso-legal.html">Aviso Legal</a>
          <a href="politica-privacidad.html">Política de Privacidad</a>
          <a href="politica-cookies.html">Política de Cookies</a>
          <a href="#cookies-config" class="open-cookie-settings">Configurar Cookies</a>
        </div>
      </div>
    </div>
  </footer>

  <script src="js/main.js" defer></script>
  <script src="js/app.js" defer></script>
</body>
</html>"""
    return html

# 3. Define the 5 Landings

common_guarantees = [
    ("📜", "Presupuesto Cerrado", "Fijamos por contrato cada partida técnica. Cero sobrecostes ni desviaciones imprevistas."),
    ("⏱️", "Compromiso de Fecha", "Establecemos fecha estricta de inicio y entrega llave en mano con penalización por retraso."),
    ("🛡️", "Seguro y Garantía", "Seguro de responsabilidad civil de 300.000€ y 10 años de garantía oficial en cerramientos."),
    ("🪟", "Taller Propio Cercano", "Sede en Carrer Murillo 41 (Alcoy), a minutos de tu casa para cualquier ajuste posventa inmediato.")
]

# --- Cocentaina ---
cocentaina_problems = [
    ("🏚️", "Casas Antiguas en Casco Histórico", "Inmuebles en El Raval, Fraga o Vila con muros de carga de piedra, vigas desgastadas y humedades que exigen albañiles con verdadero oficio tradicional."),
    ("🏡", "Chalets en la Huerta y Gormaig", "Viviendas unifamiliares con porches desaprovechados y cocinas cerradas que piden abrirse al exterior con cerramientos panorámicos."),
    ("💸", "Intermediarios con Costes Añadidos", "Empresas de Alicante o Valencia que aplican recargos abusivos de kilometraje y demoran semanas la llegada de materiales.")
]
cocentaina_solutions = """
            <div style="display: flex; gap: 1rem; align-items: flex-start;">
              <span style="font-size: 1.25rem;">⏱️</span>
              <div>
                <strong>A solo 5 minutos reales de Cocentaina:</strong>
                <p style="color: #64748B; font-size: 0.9rem;">Carrer Murillo 41 está al lado. Llegamos a tu obra en minutos sin ningún tipo de recargo por desplazamiento.</p>
              </div>
            </div>
            <div style="display: flex; gap: 1rem; align-items: flex-start;">
              <span style="font-size: 1.25rem;">🪟</span>
              <div>
                <strong>Fabricación directa en taller propio:</strong>
                <p style="color: #64748B; font-size: 0.9rem;">Cortamos perfiles Cortizo y ensamblamos herrajes Roto Frank en nuestro taller. Ajustes al milímetro sin esperar a terceros.</p>
              </div>
            </div>
            <div style="display: flex; gap: 1rem; align-items: flex-start;">
              <span style="font-size: 1.25rem;">🏛️</span>
              <div>
                <strong>Tramitación de licencias en Ayuntamiento de Cocentaina:</strong>
                <p style="color: #64748B; font-size: 0.9rem;">Redactamos la memoria técnica y gestionamos la declaración responsable / licencia de obras en Plaça del Pla, 1.</p>
              </div>
            </div>
"""
cocentaina_winner = """
              <li>✓ Sede física y taller a 5 min (Carrer Murillo 41)</li>
              <li>✓ Tramitamos licencia en Ayuntamiento de Cocentaina</li>
              <li>✓ 0€ de suplemento de desplazamiento</li>
              <li>✓ Carpintería Cortizo / Strugal de fabricación propia</li>
              <li>✓ Tres generaciones familiares (+60 años continuos)</li>
"""
cocentaina_loser = """
              <li>✗ Vienen de lejos y cobran kilometraje por día</li>
              <li>✗ El cliente debe hacer colas para pedir la licencia</li>
              <li>✗ Subcontratan las ventanas a talleres externos</li>
              <li>✗ Presupuestos abiertos que suben durante la obra</li>
              <li>✗ Desaparecen al terminar sin dar respuesta posventa</li>
"""
cocentaina_reviews = [
    ("Vicent Ferrándiz", "Cocentaina (Zona Gormaig)", "★★★★★", "Hicieron la reforma integral de nuestro chalet en Gormaig: abrieron la cocina al porche con un ventanal Cortizo espectacular y renovaron los dos baños. A 5 minutos de casa, da una tranquilidad inmensa.", "Hace 2 semanas"),
    ("Marta Pascual", "Cocentaina (Casco Antiguo)", "★★★★★", "Teníamos una casa de pueblo en El Raval con humedades en la planta baja. Sanearon muros, cambiaron fontanería y colocaron suelo porcelánico. Muy limpios y cumplieron el presupuesto al céntimo.", "Hace 1 mes"),
    ("Andrés Boronat", "Cocentaina (Avda. J.J. Senabre)", "★★★★★", "Cambiamos bañera por ducha con mampara a medida y alicatado nuevo. En 4 días estaba listo para usar. Trato familiar inmejorable por parte de Alejandro.", "Hace 2 meses")
]
cocentaina_steps = [
    ("01", "Visita Técnica en Cocentaina", "Nos desplazamos gratis a tu vivienda en Cocentaina o pedanía para medir y analizar la estructura sin compromiso."),
    ("02", "Propuesta y Presupuesto Cerrado", "Diseño de distribución, selección de materiales en nuestra exposición de Murillo 41 y contrato con precio cerrado."),
    ("03", "Gestión de Licencia y Obra", "Tramitamos la licencia municipal en el Ayuntamiento de Cocentaina y ejecutamos la reforma con gremios propios coordinados."),
    ("04", "Entrega Impecable Llave en Mano", "Limpieza profesional final, revisión exhaustiva de remates y activación de las garantías por escrito.")
]
cocentaina_faqs = [
    ("¿Cuánto cuesta una reforma integral en Cocentaina?", "El coste oscila habitualmente entre 450€ y 750€ por metro cuadrado según la calidad de acabados y si requiere renovación completa de fontanería, electricidad o cerramientos técnicos. Entregamos presupuesto partida por partida sin sorpresas."),
    ("¿Cuánto tiempo tarda la reforma de un baño o cocina en Cocentaina?", "Una reforma completa de baño con sustitución de bañera por ducha mineral y mampara a medida se ejecuta en 4 a 6 días laborables. Una cocina integral abierta suele completarse en 10 a 14 días."),
    ("¿Gestionáis la licencia de obras en el Ayuntamiento de Cocentaina?", "Sí, nos encargamos de preparar la memoria descriptiva y tramitar la declaración responsable o licencia de obra menor ante el Ayuntamiento de Cocentaina (Plaça del Pla, 1 / sede electrónica), ahorrándote trámites."),
    ("¿Cobráis suplemento por desplazamiento a Cocentaina o Gormaig?", "No, 0€ de suplemento. Nuestro taller y exposición se encuentran en Carrer Murillo 41 de Alcoy, a tan solo 5 minutos por la autovía o carretera nacional."),
    ("¿Qué marcas utilizáis para cerramientos y acabados?", "Trabajamos con primeras marcas certificadas: perfilería Cortizo y Strugal para cerramientos térmicos, herrajes de seguridad alemanes Roto Frank y griferías y sanitarios de máxima durabilidad."),
    ("¿El presupuesto es cerrado o puede encarecerse durante la reforma?", "El presupuesto es 100% cerrado por contrato. Si no solicitas modificaciones sobre el proyecto aprobado, el importe inicial pactado es exactamente el importe final que abonas.")
]

html_cocentaina = create_landing(
    slug="reformas-cocentaina.html",
    location_name="Cocentaina",
    h1_title="Reformas Integrales, Cocinas y Baños en Cocentaina",
    meta_desc="Empresa de reformas en Cocentaina. Reformas integrales llave en mano, baños con mamparas a medida y cocinas de diseño con taller propio a 5 min en Murillo 41.",
    aeo_text="<strong>Reformas Bañuls gestiona reformas integrales, cocinas y baños en Cocentaina</strong> y pedanías (Gormaig, Algars). Con taller propio a solo 5 minutos en Carrer Murillo 41 (Alcoy), ofrecemos gremios propios, presupuesto cerrado por contrato, carpintería Cortizo sin intermediarios y tramitación de licencias ante el Ayuntamiento de Cocentaina.",
    problem_items=cocentaina_problems,
    solution_features=cocentaina_solutions,
    comp_winner_items=cocentaina_winner,
    comp_loser_items=cocentaina_loser,
    reviews_list=cocentaina_reviews,
    process_steps=cocentaina_steps,
    faq_items=cocentaina_faqs,
    guarantees_list=common_guarantees
)
with open(r'c:\Users\edgvi\Documents\webleadsagent\reformas-cocentaina.html', 'w', encoding='utf-8') as f:
    f.write(html_cocentaina)
print("Created reformas-cocentaina.html")

# --- Muro de Alcoy ---
muro_problems = [
    ("🏡", "Porches y Terrazas Desaprovechados", "Chalets y parcelas en Muro con porches abiertos que sufren viento y frío en invierno y necesitan cerramientos acristalados para usarse todo el año."),
    ("🍳", "Cocinas Antiguas Aisladas", "Viviendas con cocinas separadas que necesitan derribo de tabiques para crear espacios diáfanos integrados con salón y jardín."),
    ("⏳", "Coordinación Lenta de Gremios Externos", "Grandes viviendas donde albañiles, fontaneros y carpinteros no se coordinan, alargando las obras durante meses innecesariamente.")
]
muro_solutions = """
            <div style="display: flex; gap: 1rem; align-items: flex-start;">
              <span style="font-size: 1.25rem;">🏡</span>
              <div>
                <strong>Especialistas en chalets y unifamiliares:</strong>
                <p style="color: #64748B; font-size: 0.9rem;">Dominamos las aperturas de espacios hacia jardines, porches bioclimáticos y cerramientos Strugal de grandes luces.</p>
              </div>
            </div>
            <div style="display: flex; gap: 1rem; align-items: flex-start;">
              <span style="font-size: 1.25rem;">🪟</span>
              <div>
                <strong>Taller propio de cerramientos a 10 minutos:</strong>
                <p style="color: #64748B; font-size: 0.9rem;">Fabricamos en Carrer Murillo 41. Sin esperas de distribuidores externos para cristales dobles bajo emisivos Climalit.</p>
              </div>
            </div>
            <div style="display: flex; gap: 1rem; align-items: flex-start;">
              <span style="font-size: 1.25rem;">🏛️</span>
              <div>
                <strong>Gestión de licencia en Ayuntamiento de Muro:</strong>
                <p style="color: #64748B; font-size: 0.9rem;">Tramitamos la documentación técnica ante el consistorio murense en Plaça del Matzem, 1.</p>
              </div>
            </div>
"""
muro_winner = """
              <li>✓ Taller propio a solo 10 minutos (Carrer Murillo 41)</li>
              <li>✓ Especialistas en cerramientos de porches y cocinas abiertas</li>
              <li>✓ Tramitación de licencias en el Ayuntamiento de Muro</li>
              <li>✓ 0€ de suplemento de kilometraje</li>
              <li>✓ Equipo multidisciplinar propio (obra, fontanería, electricidad)</li>
"""
muro_loser = """
              <li>✗ Descoordinación de subcontratas de fuera</li>
              <li>✗ No fabrican carpintería propia, demoran semanas</li>
              <li>✗ El cliente asume las gestiones de licencias y cubas</li>
              <li>✗ Presupuestos con sobrecostes por imprevistos</li>
              <li>✗ Falta de respuesta rápida en caso de desajustes</li>
"""
muro_reviews = [
    ("Carmina Albors", "Muro de Alcoy (Zona Turballos)", "★★★★★", "Cerramos el porche de nuestro chalet con perfilería de aluminio y vidrio Climalit fabricado por Bañuls. Ahora es la estancia favorita de la casa en invierno. Trabajo impecable.", "Hace 3 semanas"),
    ("Jordi Sanchis", "Muro de Alcoy (Casco Urbano)", "★★★★★", "Reforma completa de piso: tiraron tabique para unir cocina y comedor, instalaron suelo laminado y reformaron los baños. Presupuesto clavado al céntimo pactado.", "Hace 1 mes"),
    ("Elena Belda", "Muro de Alcoy (Plaza Matzem)", "★★★★★", "Alejandro nos asesoró con una sinceridad que ya no se encuentra. Nos tramitaron la licencia en el ayuntamiento y en 5 días teníamos baño nuevo.", "Hace 2 meses")
]
muro_steps = [
    ("01", "Visita Gratuita en Muro de Alcoy", "Evaluamos tu vivienda o chalet en Muro, Turballos o Setla para asesorarte in situ sobre distribución y aislamiento."),
    ("02", "Propuesta Técnica y Presupuesto", "Presupuesto detallado por partidas sin letra pequeña con catálogo de acabados y cerramientos de taller."),
    ("03", "Licencia Municipal y Obra", "Gestionamos la licencia en el Ayuntamiento de Muro y coordinamos a albañiles, fontaneros y electricistas propios."),
    ("04", "Revisión Final y Garantía", "Entrega limpia y activación de la garantía por contrato y seguro de responsabilidad civil.")
]
muro_faqs = [
    ("¿Hacéis cerramientos de terrazas y porches en chalets de Muro?", "Sí, es una de nuestras principales especialidades. Instalamos cerramientos con rotura de puente térmico Cortizo y Strugal con vidrios con control solar que aíslan del frío y reducen el calor en verano."),
    ("¿Cuánto tarda una reforma integral en Muro de Alcoy?", "Una reforma integral de vivienda suele durar entre 3 y 5 semanas dependiendo de la envergadura de las demoliciones e instalaciones. El plazo queda garantizado por contrato."),
    ("¿Tramitáis los permisos de obra con el Ayuntamiento de Muro?", "Sí, preparamos la documentación técnica necesaria para la comunicación previa o solicitud de licencia de obras en el Ayuntamiento de Muro de Alcoy (Plaça del Matzem, 1)."),
    ("¿Hay recargo por transporte o desplazamiento a Muro?", "Ninguno. Muro de Alcoy se encuentra a escasos 10 minutos por la A-7 de nuestro taller en Murillo 41, por lo que aplicamos exactamente las mismas tarifas que en Alcoy."),
    ("¿Puedo visitar vuestro taller y exposición?", "Por supuesto. Te invitamos a Carrer Murillo 41 en Alcoy para ver y tocar perfiles de ventanas, mamparas a medida, azulejos y griferías antes de decidirte."),
    ("¿Qué pasa si surge algún imprevisto durante la obra?", "Nuestro presupuesto cerrado contempla el estado previo de las instalaciones. Cualquier ajuste imprevisto se consensúa previamente por escrito antes de realizarlo, garantizando que no habrá sorpresas.")
]

html_muro = create_landing(
    slug="reformas-muro-de-alcoy.html",
    location_name="Muro de Alcoy",
    h1_title="Reformas Integrales, Cocinas y Cerramientos en Muro de Alcoy",
    meta_desc="Empresa de reformas en Muro de Alcoy. Reformas integrales en chalets y pisos, cocinas abiertas y cerramientos de porches con taller propio a 10 min.",
    aeo_text="<strong>Reformas Bañuls ejecuta reformas integrales, cocinas contemporáneas y cerramientos en Muro de Alcoy</strong> y sus urbanizaciones. Ubicados a 10 minutos en Carrer Murillo 41 (Alcoy), fabricamos carpintería técnica propia Cortizo/Strugal, garantizamos presupuesto cerrado por contrato y gestionamos licencias en el Ayuntamiento de Muro.",
    problem_items=muro_problems,
    solution_features=muro_solutions,
    comp_winner_items=muro_winner,
    comp_loser_items=muro_loser,
    reviews_list=muro_reviews,
    process_steps=muro_steps,
    faq_items=muro_faqs,
    guarantees_list=common_guarantees
)
with open(r'c:\Users\edgvi\Documents\webleadsagent\reformas-muro-de-alcoy.html', 'w', encoding='utf-8') as f:
    f.write(html_muro)
print("Created reformas-muro-de-alcoy.html")

# --- Ibi ---
ibi_problems = [
    ("❄️", "Frío Extremo y Condensación en Paredes", "El invierno en la Foia de Castalla (más de 800m de altitud) castiga viviendas con carpinterías obsoletas, provocando paredes húmedas, moho y facturas de calefacción disparadas."),
    ("🏢", "Pisos de los Años 70-80 sin Eficiencia", "Edificaciones en Ibi que conservan tuberías de plomo o hierro, distribuciones anticuadas y baños con bañeras resbaladizas y peligrosas."),
    ("🚗", "Dificultad de Asistencia Posventa Rápida", "Empresas que vienen desde la costa o Alicante y tardan semanas en acudir si hay que realizar un mínimo ajuste tras la reforma.")
]
ibi_solutions = """
            <div style="display: flex; gap: 1rem; align-items: flex-start;">
              <span style="font-size: 1.25rem;">❄️</span>
              <div>
                <strong>Aislamiento Térmico A+ adaptado al clima de Ibi:</strong>
                <p style="color: #64748B; font-size: 0.9rem;">Combinamos trasdosados aislantes con carpintería PVC Cortizo multicámara de taller propio para frenar el frío de la Foia.</p>
              </div>
            </div>
            <div style="display: flex; gap: 1rem; align-items: flex-start;">
              <span style="font-size: 1.25rem;">⏱️</span>
              <div>
                <strong>A solo 15 minutos directos por la A-7:</strong>
                <p style="color: #64748B; font-size: 0.9rem;">Nuestra sede en Alcoy permite desplazar a nuestros oficiales a Ibi a diario sin demoras ni suplementos.</p>
              </div>
            </div>
            <div style="display: flex; gap: 1rem; align-items: flex-start;">
              <span style="font-size: 1.25rem;">🏛️</span>
              <div>
                <strong>Licencias en Ayuntamiento de Ibi:</strong>
                <p style="color: #64748B; font-size: 0.9rem;">Gestionamos la comunicación previa y tasas municipales en Carrer les Eres, 48.</p>
              </div>
            </div>
"""
ibi_winner = """
              <li>✓ Aislamiento térmico especializado para el frío de Ibi</li>
              <li>✓ Taller propio de ventanas PVC Cortizo y Climalit</li>
              <li>✓ Respuesta posventa en menos de 24 horas</li>
              <li>✓ Tramitamos licencias en Ayuntamiento de Ibi</li>
              <li>✓ Presupuesto cerrado por contrato sin sorpresas</li>
"""
ibi_loser = """
              <li>✗ Reformas cosméticas sin solucionar los puentes térmicos</li>
              <li>✗ Compran ventanas estándar que no aíslan el frío de montaña</li>
              <li>✗ Demoras de semanas para atender cualquier retoque</li>
              <li>✗ Presupuestos abiertos que se disparan un 30%</li>
              <li>✗ Subcontratas temporales que no asumen garantías</li>
"""
ibi_reviews = [
    ("Guillem Verdú", "Ibi (Avenida Juan Carlos I)", "★★★★★", "En Ibi el frío en invierno es brutal. Reformaron el piso completo cambiando ventanas por PVC Cortizo con gas argón y trasdosados. Hemos reducido el gasto de gasoil a la mitad.", "Hace 1 mes"),
    ("Silvia Rico", "Ibi (Zona San Miguel)", "★★★★★", "Cambiaron la bañera por ducha mineral con mampara a medida y grifería termostática. En 5 días terminaron y dejaron todo recogido. Da gusto trabajar con gente seria.", "Hace 1 mes"),
    ("Pablo Miralles", "Ibi (Casco Histórico)", "★★★★★", "Reforma de cocina completa. Nos diseñaron la distribución aprovechando cada rincón. Acabados de lujo y el presupuesto no se movió ni un euro.", "Hace 3 meses")
]
ibi_steps = [
    ("01", "Visita y Estudio Térmico en Ibi", "Acudimos a tu domicilio en Ibi para medir y evaluar aislamientos, muros y estado de instalaciones."),
    ("02", "Propuesta Técnica 3D y Presupuesto", "Memoria pormenorizada con precios unitarios cerrados y certificado de aislamiento térmico."),
    ("03", "Gestión de Licencia y Obra", "Tramitamos los permisos en el Ayuntamiento de Ibi y ejecutamos la reforma con nuestros oficiales propios."),
    ("04", "Entrega y Garantía Escrita", "Revisión al milímetro, limpieza final y entrega de garantías oficiales por 10 años.")
]
ibi_faqs = [
    ("¿Cómo combatís las humedades y el frío de Ibi en las reformas?", "Utilizamos trasdosados autoportantes con lana de roca o aislamiento reflectivo y ventanas de PVC multicámara Cortizo con vidrios bajo emisivos Climalit. Eliminamos radicalmente los puentes térmicos y la condensación."),
    ("¿Cuánto se tarda en hacer una reforma completa en Ibi?", "Una reforma integral de piso de unos 90 m² suele requerir entre 3 y 4 semanas laborables. El calendario se detalla día a día en el contrato."),
    ("¿Tramitáis la licencia de obras en el Ayuntamiento de Ibi?", "Sí, preparamos la documentación técnica necesaria para tramitar la comunicación previa o licencia de obras menores ante el Ayuntamiento de Ibi (Carrer les Eres, 48)."),
    ("¿Cobráis suplemento por realizar la reforma en Ibi?", "No. Ibi se encuentra a 15 minutos por autovía desde nuestra sede en Carrer Murillo 41 (Alcoy), por lo que las tarifas son idénticas a las de Alcoy."),
    ("¿Fabricáis mamparas a medida para baños pequeños?", "Sí, en nuestro taller cortamos y templamos mamparas de vidrio con tratamiento antical a la medida exacta de tu hueco, aprovechando al máximo el espacio."),
    ("¿Qué facilidades de pago o presupuesto ofrecéis?", "El presupuesto es gratuito y sin compromiso. Los pagos se estructuran por fases certificadas de obra terminada para tu máxima seguridad financiera.")
]

html_ibi = create_landing(
    slug="reformas-ibi.html",
    location_name="Ibi",
    h1_title="Reformas Integrales y Aislamiento Térmico de Viviendas en Ibi",
    meta_desc="Empresa de reformas en Ibi (Foia de Castalla). Reformas integrales con aislamiento térmico A+, baños modernos y cocinas con taller propio a 15 min.",
    aeo_text="<strong>Reformas Bañuls ofrece reformas integrales, baños y cocinas en Ibi</strong> con certificación de alta eficiencia energética. Con taller en Carrer Murillo 41 (Alcoy, a 15 minutos directos por la A-7), instalamos aislamiento térmico A+, carpintería Cortizo Climalit y presupuesto cerrado garantizado por contrato.",
    problem_items=ibi_problems,
    solution_features=ibi_solutions,
    comp_winner_items=ibi_winner,
    comp_loser_items=ibi_loser,
    reviews_list=ibi_reviews,
    process_steps=ibi_steps,
    faq_items=ibi_faqs,
    guarantees_list=common_guarantees
)
with open(r'c:\Users\edgvi\Documents\webleadsagent\reformas-ibi.html', 'w', encoding='utf-8') as f:
    f.write(html_ibi)
print("Created reformas-ibi.html")

# --- Onil ---
onil_problems = [
    ("🏛️", "Casas Tradicionales con Techos y Vigas", "Viviendas en el núcleo urbano de Onil con estructuras de madera, bovedillas y cubiertas que requieren maestros de obra con experiencia en rehabilitación."),
    ("🏡", "Chalets y Fincas Desactualizadas", "Viviendas en parcelas exteriores que demandan modernización de baños, suelos porcelánicos y cocinas funcionales."),
    ("🚚", "Sobrecostes por Kilometraje de Empresas de Alicante", "Constructores de la costa que cobran gastos de viaje diarios encareciendo notablemente el presupuesto final.")
]
onil_solutions = """
            <div style="display: flex; gap: 1rem; align-items: flex-start;">
              <span style="font-size: 1.25rem;">💰</span>
              <div>
                <strong>0€ de recargo por desplazamiento a Onil:</strong>
                <p style="color: #64748B; font-size: 0.9rem;">Estamos a menos de 18 minutos por autovía. Nuestras furgonetas y gremios acuden a diario a Onil sin suplementos.</p>
              </div>
            </div>
            <div style="display: flex; gap: 1rem; align-items: flex-start;">
              <span style="font-size: 1.25rem;">🔨</span>
              <div>
                <strong>Oficio tradicional de 3 generaciones:</strong>
                <p style="color: #64748B; font-size: 0.9rem;">Sabemos tratar vigas vistas de madera, consolidar muros de piedra y aplicar aislamientos modernos sin romper la estética.</p>
              </div>
            </div>
            <div style="display: flex; gap: 1rem; align-items: flex-start;">
              <span style="font-size: 1.25rem;">🏛️</span>
              <div>
                <strong>Licencias en Ayuntamiento de Onil:</strong>
                <p style="color: #64748B; font-size: 0.9rem;">Gestionamos la solicitud de licencia de obra menor en Plaça Major, 1.</p>
              </div>
            </div>
"""
onil_winner = """
              <li>✓ 0€ de suplemento de desplazamiento a Onil</li>
              <li>✓ Especialistas en casas tradicionales y chalets</li>
              <li>✓ Taller propio de ventanas y cerramientos Cortizo</li>
              <li>✓ Licencias tramitadas en Ayuntamiento de Onil</li>
              <li>✓ Más de 60 años de trayectoria familiar continua</li>
"""
onil_loser = """
              <li>✗ Cobran pluses de kilometraje y dietas</li>
              <li>✗ Desconocen la arquitectura tradicional de la comarca</li>
              <li>✗ Subcontratan toda la carpintería y cristalería</li>
              <li>✗ Desvíos presupuestarios continuos</li>
              <li>✗ Sin sede cercana para reclamaciones o ajustes</li>
"""
onil_reviews = [
    ("Marta Bernabeu", "Onil (Zona Centro)", "★★★★★", "Rehabilitamos una casa de pueblo familiar en Onil. Mantuvieron las vigas de madera restauradas y renovaron la cocina y los baños. El trabajo de albañilería y carpintería es de diez.", "Hace 3 semanas"),
    ("Jorge Esteve", "Onil (Chalet en partida Favanella)", "★★★★★", "Cambiaron todas las ventanas por carpintería de aluminio con rotura de puente térmico y reformaron la terraza. Sin recargo por estar en Onil y con un trato exquisito.", "Hace 1 mes"),
    ("Rosa María Sanjuán", "Onil (Avenida Constitución)", "★★★★★", "Reforma de baño exprés en 4 días. Muy limpios, respetuosos con las zonas comunes y presupuesto cerrado sin un solo euro de más.", "Hace 2 meses")
]
onil_steps = [
    ("01", "Visita Técnica Gratuita en Onil", "Nos acercamos a tu casa o chalet en Onil para tomar medidas y asesorarte sobre viabilidad y materiales."),
    ("02", "Presupuesto Cerrado por Escrito", "Detalle exhaustivo de partidas, sin conceptos ambiguos ni sorpresas finales."),
    ("03", "Gestión Municipal y Ejecución", "Tramitamos los permisos en el Ayuntamiento de Onil e iniciamos la obra con nuestros gremios coordinados."),
    ("04", "Entrega Llave en Mano y Limpieza", "Comprobación final y entrega de garantías oficiales por contrato.")
]
onil_faqs = [
    ("¿Cobráis algún suplemento de desplazamiento para obras en Onil?", "Absolutamente ninguno. Onil se encuentra a escasos 18 minutos de nuestro taller en Murillo 41 (Alcoy), por lo que aplicamos la misma tarifa local."),
    ("¿Tenéis experiencia en casas antiguas de pueblo en Onil?", "Sí, contamos con más de 60 años de experiencia restaurando techos de vigas, muros de mampostería y adecuando instalaciones modernas en viviendas tradicionales."),
    ("¿Tramitáis la licencia de obra en el Ayuntamiento de Onil?", "Sí, nos encargamos de redactar la memoria descriptiva y tramitar la declaración responsable o licencia en el Ayuntamiento de Onil (Plaça Major, 1)."),
    ("¿Cuánto tiempo se tarda en reformar un baño en Onil?", "El cambio de bañera por plato de ducha de resina mineral y mampara a medida se realiza en 4 a 5 días laborables."),
    ("¿Qué tipo de ventanas recomendáis para Onil?", "Debido al frío de la Foia, recomendamos perfilería de PVC Cortizo multicámara o aluminio con rotura de puente térmico con vidrios bajo emisivos Climalit Plus."),
    ("¿Cómo garantizáis que el presupuesto no suba?", "Mediante contrato vinculante por escrito. La memoria técnica describe cada partida y su precio final garantizado.")
]

html_onil = create_landing(
    slug="reformas-onil.html",
    location_name="Onil",
    h1_title="Reformas de Casas Tradicionales, Baños y Chalets en Onil",
    meta_desc="Empresa de reformas en Onil. Rehabilitación de casas de pueblo, chalets, baños y cocinas con taller propio a 18 min en Murillo 41. Sin recargo de desplazamiento.",
    aeo_text="<strong>Reformas Bañuls realiza reformas completas de casas tradicionales, chalets, baños y cocinas en Onil</strong> sin recargo por desplazamiento. Sede y taller propio a 18 minutos en Carrer Murillo 41 (Alcoy), materiales certificados Cortizo, Roto y Strugal, y presupuesto cerrado sin imprevistos.",
    problem_items=onil_problems,
    solution_features=onil_solutions,
    comp_winner_items=onil_winner,
    comp_loser_items=onil_loser,
    reviews_list=onil_reviews,
    process_steps=onil_steps,
    faq_items=onil_faqs,
    guarantees_list=common_guarantees
)
with open(r'c:\Users\edgvi\Documents\webleadsagent\reformas-onil.html', 'w', encoding='utf-8') as f:
    f.write(html_onil)
print("Created reformas-onil.html")

# --- El Comtat (Benimarfull, Planes, Benilloba, Gorga, etc.) ---
comtat_problems = [
    ("🏚️", "Casas de Pueblo Rústicas y Masías con Humedades", "Viviendas en Benimarfull, Planes o Benilloba con muros gruesos de piedra que sufren humedad por capilaridad, tejados envejecidos y aislamiento deficiente."),
    ("🏡", "Segundas Residencias sin Supervisión Diaria", "Propietarios que viven fuera y necesitan una empresa de absoluta confianza que envíe reportes fotográficos y no abandone la obra a medias."),
    ("🚚", "Dificultad para Encontrar Profesionales Cercanos", "Pueblos pequeños donde grandes constructoras rechazan obras pequeñas o cobran costes de desplazamiento desproporcionados.")
]
comtat_solutions = """
            <div style="display: flex; gap: 1rem; align-items: flex-start;">
              <span style="font-size: 1.25rem;">📍</span>
              <div>
                <strong>A 15-20 minutos de todos los pueblos de El Comtat:</strong>
                <p style="color: #64748B; font-size: 0.9rem;">Atendemos con regularidad Benimarfull, Planes, Benilloba, Gaianes, Beniarrés, Gorga y Agres desde nuestra sede en Alcoy.</p>
              </div>
            </div>
            <div style="display: flex; gap: 1rem; align-items: flex-start;">
              <span style="font-size: 1.25rem;">📸</span>
              <div>
                <strong>Reporte fotográfico semanal para segundas residencias:</strong>
                <p style="color: #64748B; font-size: 0.9rem;">Si vives en Valencia o Alicante, Alejandro te envía avances detallados por WhatsApp en cada fase de obra.</p>
              </div>
            </div>
            <div style="display: flex; gap: 1rem; align-items: flex-start;">
              <span style="font-size: 1.25rem;">🪟</span>
              <div>
                <strong>Carpintería rústica y moderna de taller propio:</strong>
                <p style="color: #64748B; font-size: 0.9rem;">Ventanas con acabado imitación madera texturada Cortizo que respetan la estética rústica con aislamiento del siglo XXI.</p>
              </div>
            </div>
"""
comtat_winner = """
              <li>✓ Cobertura directa en Benimarfull, Planes, Benilloba y El Comtat</li>
              <li>✓ Sin recargo por desplazamiento (a 15-20 min de Murillo 41)</li>
              <li>✓ Especialistas en muros de piedra, vigas y humedades</li>
              <li>✓ Reporte fotográfico continuo para propietarios ausentes</li>
              <li>✓ Presupuesto cerrado y 60 años de prestigio familiar</li>
"""
comtat_loser = """
              <li>✗ Cobran suplementos desorbitados por acudir a pueblos pequeños</li>
              <li>✗ Abandonan las obras durante semanas para atender otras obras</li>
              <li>✗ Soluciones estándar que no respetan la piedra ni el encanto rústico</li>
              <li>✗ Subcontratas sin interlocutor único</li>
              <li>✗ Sin garantías formales por escrito</li>
"""
comtat_reviews = [
    ("Francesc Company", "Benimarfull (Casa de Pueblo)", "★★★★★", "Restauramos la casa de los abuelos en Benimarfull. Sanearon las paredes de piedra, renovaron la cocina con suelo de gres rústico y pusieron ventanas térmicas imitación roble. Un trabajo impecable.", "Hace 2 semanas"),
    ("Mireia Blanes", "Planes (Vivienda en el casco histórico)", "★★★★★", "Vivimos en Valencia y teníamos miedo de no poder controlar la obra. Alejandro nos enviaba vídeos semanales de cada avance. Cumplieron plazos y presupuesto al milímetro.", "Hace 1 mes"),
    ("Josep Doménech", "Benilloba (Reforma de Baño y Techo)", "★★★★★", "Cambiaron la bañera por ducha y arreglaron una filtración del tejado. En 5 días todo resuelto y sin cobrar suplemento de viaje. 100% recomendables.", "Hace 2 meses")
]
comtat_steps = [
    ("01", "Visita Gratuita en tu Pueblo de El Comtat", "Nos desplazamos sin coste a Benimarfull, Planes, Benilloba, Gorga, Gaianes o cualquier municipio de la comarca."),
    ("02", "Propuesta Técnica y Presupuesto Cerrado", "Valoración pormenorizada respetando la esencia rústica e incorporando confort moderno."),
    ("03", "Gestión Municipal y Coordinación de Gremios", "Asesoramos en las tasas y licencias municipales de obras de cada ayuntamiento comarcal."),
    ("04", "Entrega y Reporte Llave en Mano", "Limpieza a fondo, entrega de llaves y garantías certificadas por escrito.")
]
comtat_faqs = [
    ("¿Trabajáis en pueblos pequeños de El Comtat como Benimarfull o Planes?", "Sí, atendemos habitualmente Benimarfull, Planes, Benilloba, Gaianes, Beniarrés, Gorga, Agres, Alcocer y Millena. Nuestro taller en Alcoy está a solo 15-20 minutos de cualquier punto de la comarca."),
    ("¿Cobráis recargo de desplazamiento por acudir a pueblos de El Comtat?", "No cobramos ningún suplemento por kilometraje. Al estar ubicados en Carrer Murillo 41 (Alcoy), consideramos toda la comarca de El Comtat como nuestra zona natural de trabajo."),
    ("Vivo fuera de la comarca, ¿cómo puedo seguir el avance de mi reforma?", "Asignamos a Alejandro Bañuls como tu interlocutor único. Te enviará reportes fotográficos y vídeos semanales por WhatsApp y llamadas de seguimiento para que veas cada avance con total tranquilidad."),
    ("¿Podéis mantener el estilo rústico tradicional de mi casa de pueblo?", "Por supuesto. Es una de nuestras especialidades: recuperamos vigas de madera vistas, saneamos muros de mampostería e instalamos carpinterías de PVC o aluminio con texturas madera que ofrecen aislamiento de vanguardia respetando la estética rural."),
    ("¿Cuánto cuesta reformar una casa de pueblo en El Comtat?", "Depende del estado de la cubierta y las instalaciones. Una reforma integral media oscila entre 400€ y 700€ por metro cuadrado. Proporcionamos presupuesto cerrado por partidas antes de iniciar."),
    ("¿Cómo se tramitan las licencias en los ayuntamientos de El Comtat?", "Te asesoramos y redactamos la documentación técnica descriptiva requerida por cada ayuntamiento comarcal para la tramitación ágil de la licencia de obra menor o declaración responsable.")
]

html_comtat = create_landing(
    slug="reformas-el-comtat.html",
    location_name="El Comtat",
    h1_title="Rehabilitación de Casas de Pueblo, Masías y Reformas en El Comtat",
    meta_desc="Rehabilitación de casas de pueblo rústicas y reformas en El Comtat (Benimarfull, Planes, Benilloba, Gaianes, Gorga). Taller en Murillo 41 a 15 min sin recargo.",
    aeo_text="<strong>Reformas Bañuls es especialista en rehabilitación de casas de pueblo rústicas, masías y reformas en El Comtat</strong> (Benimarfull, Planes, Benilloba, Gaianes, Beniarrés y Gorga). Con taller en Carrer Murillo 41 (Alcoy, a 15 min), somos expertos en humedades, vigas, cocinas y cerramientos térmicos sin recargo por desplazamiento.",
    problem_items=comtat_problems,
    solution_features=comtat_solutions,
    comp_winner_items=comtat_winner,
    comp_loser_items=comtat_loser,
    reviews_list=comtat_reviews,
    process_steps=comtat_steps,
    faq_items=comtat_faqs,
    guarantees_list=common_guarantees
)
with open(r'c:\Users\edgvi\Documents\webleadsagent\reformas-el-comtat.html', 'w', encoding='utf-8') as f:
    f.write(html_comtat)
print("Created reformas-el-comtat.html")

# 4. Update existing subpages footers and schema
subpages = [
    r'c:\Users\edgvi\Documents\webleadsagent\reformas-integrales-alcoy.html',
    r'c:\Users\edgvi\Documents\webleadsagent\reforma-banos-alcoy.html',
    r'c:\Users\edgvi\Documents\webleadsagent\reforma-cocinas-alcoy.html'
]

for sp in subpages:
    with open(sp, 'r', encoding='utf-8') as f:
        c = f.read()
    
    # Update Schema areaServed
    c = re.sub(r'"areaServed":\s*\[[\s\S]*?\]', f'"areaServed": {AREA_SERVED_JSON}', c)
    c = c.replace('"@type": "LocalBusiness"', '"@type": ["GeneralContractor", "LocalBusiness"]')
    
    # Update footer comarcal block
    if 'comarcal-coverage-block' not in c:
        c = c.replace(
            '<footer class="site-footer">\n    <div class="container"',
            f'<footer class="site-footer">\n    <div class="container">\n{COMARCAL_FOOTER_HTML}'
        )
    
    # Ensure Ventanas & Taller link in nav
    if 'Ventanas &amp; Taller' not in c and 'Ventanas & Taller' not in c:
        c = c.replace(
            '<li><a href="/#contacto" class="nav-link">Contacto</a></li>',
            '<li><a href="https://xn--ventanasbauls-rkb.com/" class="nav-link" target="_blank" rel="noopener">🪟 Ventanas &amp; Taller ↗</a></li>\n          <li><a href="/#contacto" class="nav-link">Contacto</a></li>'
        )

    with open(sp, 'w', encoding='utf-8') as f:
        f.write(c)
    print(f"Updated subpage: {sp}")

# 5. Update sitemap.xml
sitemap_content = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://xn--reformasbauls-rkb.com/</loc>
    <lastmod>2026-11-05</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://xn--reformasbauls-rkb.com/reformas-integrales-alcoy.html</loc>
    <lastmod>2026-11-05</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>https://xn--reformasbauls-rkb.com/reforma-banos-alcoy.html</loc>
    <lastmod>2026-11-05</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>https://xn--reformasbauls-rkb.com/reforma-cocinas-alcoy.html</loc>
    <lastmod>2026-11-05</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>https://xn--reformasbauls-rkb.com/reformas-cocentaina.html</loc>
    <lastmod>2026-11-05</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>https://xn--reformasbauls-rkb.com/reformas-muro-de-alcoy.html</loc>
    <lastmod>2026-11-05</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>https://xn--reformasbauls-rkb.com/reformas-ibi.html</loc>
    <lastmod>2026-11-05</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>https://xn--reformasbauls-rkb.com/reformas-onil.html</loc>
    <lastmod>2026-11-05</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>https://xn--reformasbauls-rkb.com/reformas-el-comtat.html</loc>
    <lastmod>2026-11-05</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>https://xn--reformasbauls-rkb.com/aviso-legal.html</loc>
    <lastmod>2026-11-05</lastmod>
    <changefreq>yearly</changefreq>
    <priority>0.3</priority>
  </url>
  <url>
    <loc>https://xn--reformasbauls-rkb.com/politica-privacidad.html</loc>
    <lastmod>2026-11-05</lastmod>
    <changefreq>yearly</changefreq>
    <priority>0.3</priority>
  </url>
  <url>
    <loc>https://xn--reformasbauls-rkb.com/politica-cookies.html</loc>
    <lastmod>2026-11-05</lastmod>
    <changefreq>yearly</changefreq>
    <priority>0.3</priority>
  </url>
</urlset>
"""
with open(r'c:\Users\edgvi\Documents\webleadsagent\sitemap.xml', 'w', encoding='utf-8') as f:
    f.write(sitemap_content)
print("Updated sitemap.xml with all URLs")
