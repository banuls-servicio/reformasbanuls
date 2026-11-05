# 🔗 Estrategia de Autoridad y Enlazado Cruzado: `ventanasbañuls.com` ➔ `reformasbañuls.com`
## Cómo transferir autoridad SEO, visibilidad local y leads sin riesgo de penalización

---

## 1. El Diagnóstico Estratégico

El usuario ha tomado una decisión de negocio altamente inteligente:
* **`ventanasbañuls.com`**: Se enfoca al 100% en captar clientes que buscan *ventanas de PVC, carpintería de aluminio con RPT, cerramientos, aislamiento contra el frío en Alcoy y subvenciones de eficiencia energética*.
* **`reformasbañuls.com`**: Se enfoca al 100% en captar clientes de alto ticket que buscan *reformas integrales, reformas de baños con mamparas a medida, cocinas contemporáneas e interiorismo llave en mano en Alcoy y comarca* (@proyectos.banuls).

Ambos dominios pertenecen a la misma empresa familiar (con más de 60 años de trayectoria física en Carrer Murillo 41, Alcoy). 

### ¿Es seguro enlazar entre ambos dominios?
**Sí, absolutamente**, siempre que no se utilicen esquemas artificiales de enlaces recíprocos en el footer con anclas exactas sobreoptimizadas. Google premia las arquitecturas de **"Ecosistema de Marca" (Brand Network)** cuando existe una relación temática real y aporta valor al usuario que navega.

---

## 2. Los 5 Puentes de Enlazado de Alta Autoridad

```
     [ CLIENTE BUSCA AISLAMIENTO / VENTANAS ]
                     ↓
             ventanasbañuls.com
                     │
    ┌────────────────┴────────────────────────┐
    │ 1. Barra de Ecosistema Superior         │ ➔ reformasbañuls.com (Tráfico Referencial)
    │ 2. Enlace Contextual en Casos Reales    │ ➔ reformasbañuls.com/reformas-integrales
    │ 3. Bloque "Reforma de Baño y Cocina"    │ ➔ reformasbañuls.com/reforma-banos
    │ 4. Checkbox en Formulario de Presupuesto│ ➔ Lead Cualificado de Alto Ticket
    └────────────────┬────────────────────────┘
                     │
                     ▼ (Retorno Natural)
             reformasbañuls.com
    (Enlaza a ventanasbañuls.com como taller propio
     de carpintería para cerramientos Cortizo / Strugal)
```

---

### Puente 1: La Barra de Red Corporativa (Header Network Switcher)
En la parte superior extrema (pre-header) de ambas webs, se coloca una franja discreta y elegante:
```html
<div class="network-bar">
  <span>Familia Bañuls Alcoy:</span>
  <a href="https://ventanasbañuls.com" class="active">Ventanas &amp; Aislamiento</a>
  <span class="sep">|</span>
  <a href="https://reformasbañuls.com">Reformas &amp; Interiorismo</a>
</div>
```
* **Impacto SEO**: Googlebot rastrea la relación corporativa legítima entre ambos dominios.
* **Impacto CRO**: Cualquier usuario que entra buscando ventanas y descubre que también hacen reformas integrales pasa de un ticket medio de 2.000€ a uno potencial de 25.000€.

---

### Puente 2: Enlazado Contextual Editorial (Anchor Text Natural)
En la web nueva de `ventanasbañuls.com`, dentro del contenido explicativo sobre cerramientos y cambios de vivienda:
* **Ubicación en página**: En secciones donde se hable de reformas de estancias o cerramientos integrales.
* **Ancla recomendada**: Variar entre marca y marca + servicio (NUNCA enlaces masivos de palabra clave exacta):
  - *"nuestro estudio especializado Reformas Bañuls"*
  - *"la división de interiorismo de Proyectos Bañuls"*
  - *"ver proyecto de reforma integral ejecutado por Reformas Bañuls"*
* **URL de destino específica**: Enlazar a páginas internas temáticas (`reformasbañuls.com/reforma-banos-alcoy.html` o `/reformas-integrales-alcoy.html`), no solo a la home.

---

### Puente 3: El Muro de Casos Reales Cruzados
Cuando en `ventanasbañuls.com` se muestre un proyecto donde se cambiaron las ventanas como parte de una reforma completa de piso:
* **Ficha de caso de éxito**:
  > *"Vivienda en Zona Ensanche (Alcoy): Instalación de carpintería Cortizo con vidrio acústico Climalit. Proyecto de reforma integral, redistribución de tabiques y cocina abierta ejecutado por nuestro equipo de **[Reformas Bañuls](https://reformasbañuls.com)**."*
* Esto transfiere PageRank de forma 100% natural y con métricas de comportamiento excepcionales (tiempo en página y clics reales de usuarios interesados).

---

### Puente 4: Pasarela de Leads en el Formulario de Presupuesto
En el formulario de contacto de `ventanasbañuls.com`, se incluye un campo inteligente:
```html
<label>
  <input type="checkbox" name="cross_lead" value="reforma">
  ¿Tu proyecto incluye también reforma de baño, cocina o vivienda completa? (Te asesorará nuestro equipo de Reformas Bañuls)
</label>
```
Si el usuario lo marca, el formulario notifica internamente al gestor de reformas, multiplicando la tasa de captación de leads de alto valor sin gastar un céntimo en publicidad.

---

### Puente 5: Enlazado Semántico en Schema.org (Google Knowledge Graph)
Configuración de la relación corporativa en los datos estructurados JSON-LD de ambos dominios:

**En `ventanasbañuls.com`:**
```json
{
  "@context": "https://schema.org",
  "@type": "HomeAndConstructionBusiness",
  "name": "Ventanas Bañuls",
  "sameAs": [
    "https://maps.app.goo.gl/9Ww7zbGbAvi6bTe36",
    "https://www.instagram.com/proyectos.banuls/"
  ],
  "parentOrganization": {
    "@type": "Organization",
    "name": "Grupo Bañuls Alcoy",
    "url": "https://reformasbañuls.com",
    "address": "Carrer Murillo, 41, 03802 Alcoi"
  }
}
```

**En `reformasbañuls.com`:**
```json
{
  "@context": "https://schema.org",
  "@type": "HomeAndConstructionBusiness",
  "name": "Reformas Bañuls",
  "parentOrganization": {
    "@type": "Organization",
    "name": "Grupo Bañuls Alcoy"
  },
  "subOrganization": {
    "@type": "LocalBusiness",
    "name": "Ventanas Bañuls",
    "url": "https://ventanasbañuls.com"
  }
}
```

---

## 3. Resumen de Beneficios
1. **Doble Posicionamiento en SERPs locales**: En búsquedas como *"reformas y ventanas alcoy"* podrás acaparar la posición #1 con una web y la #2 con la otra.
2. **Claridad de Conversión**: El usuario que solo quiere arreglar una ventana no se abruma con presupuestos de reformas completas, y el usuario que quiere reformar su casa no siente que está contratando a un simple montador de ventanas.
3. **Traspaso de Antigüedad y Autoridad**: El dominio veterano transfiere señales de confianza al nuevo dominio desde el primer día.
