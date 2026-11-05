# 🪟 Ventanas Bañuls | Sistema Web Leads & Re-Engineering Agent

Este repositorio contiene dos soluciones completas integradas:
1. **La nueva web de alta conversión y estrategia SEO/GEO/AEO para Ventanas Bañuls** (`ventanasbañuls.com`), lista para producción con los recursos reales de la empresa (60 años de trayectoria, Carrer Murillo 41, fotos reales de taller, Instagram `@proyectos.banuls` y Canva).
2. **El Agente Reutilizable `web-leads-architect`**: Un agente y CLI automatizado para auditar y reconstruir la web de cualquier cliente local pasando únicamente sus enlaces (Google Maps, Instagram, web antigua, Canva o fotos).

---

## 📁 Estructura del Proyecto

```
webleadsagent/
├── agent/                         # Definición del Agente Reutilizable
│   └── AGENT_INSTRUCTIONS.md      # Protocolo de ejecución y system prompt
├── cli/                           # CLI automatizado para nuevos clientes
│   └── web_leads_agent.py         # Script de extracción y auditoría
├── strategy/                      # Estrategia Completa para Ventanas Bañuls
│   ├── KEYWORD_RESEARCH_ALCOY.md  # Matriz de keywords, intención, volumen y KD
│   ├── SEO_AEO_GEO_STRATEGY.md    # Plan de dominación Local Maps, AEO y Search Console
│   └── ARCHITECTURE_SITEMAP.md    # Estructura en silos y enlazado interno
├── assets/                        # Recursos de marca optimizados
│   └── img/                       # Logotipos SVG, fotos reales de obras y antes/después
├── css/
│   └── style.css                  # Sistema de diseño arquitectónico (sin dependencias)
├── js/
│   └── main.js                    # Slider antes/después, calculadora climática y WhatsApp
├── index.html                     # Master Landing Page (Secuencia de 14 secciones)
├── ventanas-pvc-alcoy.html        # Silo específico: Ventanas de PVC
├── ventanas-aluminio-rpt.html     # Silo específico: Ventanas de Aluminio RPT
├── reformas-alcoy.html            # Silo específico: Reformas Baños y Cocinas (@proyectos.banuls)
├── subvenciones-ventanas.html     # Silo específico: Deducción IRPF hasta el 40%
├── sitemap.xml                    # Sitemap XML listo para Search Console
└── robots.txt                     # Configuración de rastreo
```

---

## 🚀 Despliegue en el Dominio Propio (`ventanasbañuls.com`)

1. **Subir archivos**: Sube el contenido a tu hosting o servidor web (Apache, Nginx, Vercel, Netlify o cPanel).
2. **Google Search Console**:
   - Accede a la propiedad de `ventanasbañuls.com`.
   - Envía el sitemap: `https://xn--ventanasbauls-rkb.com/sitemap.xml`.
   - Solicita la indexación de las 5 páginas creadas.
3. **Google Maps / Business Profile**:
   - Vincula la URL canónica a la ficha de Carrer Murillo 41.

---

## 🤖 Cómo Usar el Agente con Nuevos Clientes

El agente `web-leads-architect` está registrado en el entorno. Puedes ejecutarlo en cualquier momento pasando un prompt como este:

```text
Actúa como web-leads-architect con los siguientes recursos:
- Google Maps: [Enlace]
- Instagram: [Enlace]
- Web actual / Canva: [Enlace]
- Dominio: [Dominio]
```

O bien mediante la herramienta CLI:
```bash
python cli/web_leads_agent.py --name "Nombre Cliente" --maps "URL" --site "URL" --instagram "URL"
```
