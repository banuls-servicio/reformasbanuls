/**
 * Reformas Bañuls - Interactive Frontend Logic
 * Features: Dynamic Real Clients Before/After Slider, Project Tabs, Quick WhatsApp Quote
 * Zero Dependencies | Ultra Fast
 */

/* ==========================================================================
   REAL CLIENTS PROJECTS DATA (Easy to update and add new Before & After cases)
   ========================================================================== */
const realProjects = [
  {
    id: 'bano-santarosa',
    tabLabel: 'Baño · Santa Rosa',
    tag: 'Reforma de Baño · Santa Rosa (Alcoy)',
    title: 'Transformación Integral de Baño con Mampara a Medida',
    desc: 'Sustitución de sanitarios antiguos por plato de ducha mineral antideslizante, nueva ventana oscilobatiente, revestimiento porcelánico rectificado y fabricación de mampara de vidrio templado antical a medida exacta en nuestro taller.',
    beforeImg: 'assets/img/ba-bano-antes.jpg',
    afterImg: 'assets/img/ba-bano-despues.jpg',
    duration: '5 días',
    budget: 'Llave en mano',
    quote: '“Me he reformado el aseo!! He quedado súper contenta, cuánto tiempo buscando presupuestos y no había encontrado a nadie tan profesional como el tubito.”',
    author: '<a href="https://www.google.com/maps/contrib/113406489948041950500/reviews?hl=es" target="_blank" rel="noopener" style="color: inherit; text-decoration: underline;">Alicia Vilaplana</a> (Reseña 5★ en Google Maps)'
  },
  {
    id: 'cocina-ensanche',
    tabLabel: 'Cocina · Ensanche',
    tag: 'Cocina Contemporánea · Ensanche (Alcoy)',
    title: 'Cocina Vanguardista Abierta con Isla y Luz Natural',
    desc: 'Derribo de tabique para unir salón y cocina, instalación de isla de trabajo con encimera porcelánica ultra resistente, columnas integradas sin tiradores y cerramientos arquitectónicos para ganar luminosidad.',
    beforeImg: 'assets/img/ba-cocina-antes.jpg',
    afterImg: 'assets/img/ba-cocina-despues.jpg',
    duration: '12 días',
    budget: 'Reforma media',
    quote: '“Nos asesoraron en la distribución y ahora el espacio parece el doble de grande. La calidad de los acabados es increíble.”',
    author: 'Javier & Andrea (Zona Ensanche)'
  },
  {
    id: 'salon-centro',
    tabLabel: 'Salón · Centro Histórico',
    tag: 'Reforma Integral · Centro Histórico (Alcoy)',
    title: 'Rehabilitación de Salón y Cerramiento Panorámico',
    desc: 'Demolición de tabiquería para ganar espacio abierto, solera autonivelante con suelo laminado AC5 de alta densidad, iluminación integrada y grandes ventanales con rotura de puente térmico para maximizar la luz.',
    beforeImg: 'assets/img/ba-salon-antes.jpg',
    afterImg: 'assets/img/ba-salon-despues.jpg',
    duration: '3 semanas',
    budget: 'Reforma integral',
    quote: '“Sesenta años de experiencia familiar se notan en cada detalle de carpintería y remates. Cero sorpresas en el presupuesto.”',
    author: 'Vicent P. (Centro Histórico, Alcoy)'
  }
];

let activeProjectIndex = 0;
let isDraggingSlider = false;

document.addEventListener('DOMContentLoaded', () => {
  initRealClientsShowcase();
  initSliderDragEvents();
  initQuickQuoteForm();
});

/* ==========================================================================
   1. Real Clients Dynamic Project Switcher
   ========================================================================== */
function initRealClientsShowcase() {
  const tabsContainer = document.getElementById('project-tabs-container');
  if (!tabsContainer) return;

  // Render tab buttons
  tabsContainer.innerHTML = '';
  realProjects.forEach((proj, idx) => {
    const btn = document.createElement('button');
    btn.className = `project-tab-btn ${idx === activeProjectIndex ? 'active' : ''}`;
    btn.textContent = proj.tabLabel;
    btn.setAttribute('type', 'button');
    btn.addEventListener('click', () => switchProject(idx));
    tabsContainer.appendChild(btn);
  });

  renderProject(activeProjectIndex);
}

function switchProject(index) {
  if (index === activeProjectIndex) return;
  activeProjectIndex = index;

  // Update tab buttons
  const buttons = document.querySelectorAll('.project-tab-btn');
  buttons.forEach((btn, idx) => {
    btn.classList.toggle('active', idx === activeProjectIndex);
  });

  renderProject(activeProjectIndex);
}

function renderProject(index) {
  const proj = realProjects[index];
  if (!proj) return;

  // Elements
  const tagEl = document.getElementById('proj-meta-tag');
  const titleEl = document.getElementById('proj-title');
  const descEl = document.getElementById('proj-desc');
  const durationEl = document.getElementById('proj-duration');
  const budgetEl = document.getElementById('proj-budget');
  const quoteEl = document.getElementById('proj-quote');
  const authorEl = document.getElementById('proj-author');
  
  const beforeImgEl = document.getElementById('ba-img-before');
  const afterImgEl = document.getElementById('ba-img-after');
  const sliderAfterWrap = document.querySelector('.ba-image-after');
  const sliderHandle = document.querySelector('.ba-slider-handle');

  if (tagEl) tagEl.textContent = proj.tag;
  if (titleEl) titleEl.textContent = proj.title;
  if (descEl) descEl.textContent = proj.desc;
  if (durationEl) durationEl.textContent = proj.duration;
  if (budgetEl) budgetEl.textContent = proj.budget;
  if (quoteEl) quoteEl.innerHTML = proj.quote;
  if (authorEl) authorEl.innerHTML = proj.author;

  // Images with fade
  if (beforeImgEl && afterImgEl) {
    beforeImgEl.style.opacity = '0.3';
    afterImgEl.style.opacity = '0.3';

    setTimeout(() => {
      beforeImgEl.src = proj.beforeImg;
      afterImgEl.src = proj.afterImg;
      beforeImgEl.alt = `Antes: ${proj.title}`;
      afterImgEl.alt = `Después: ${proj.title}`;
      beforeImgEl.style.opacity = '1';
      afterImgEl.style.opacity = '1';
    }, 150);
  }

  // Reset handle position to 50%
  if (sliderAfterWrap && sliderHandle) {
    sliderAfterWrap.style.width = '50%';
    sliderHandle.style.left = '50%';
  }
}

/* ==========================================================================
   2. Draggable Split Slider Logic (Mouse & Touch)
   ========================================================================== */
function initSliderDragEvents() {
  const container = document.querySelector('.ba-slider-container');
  if (!container) return;

  const afterImage = container.querySelector('.ba-image-after');
  const handle = container.querySelector('.ba-slider-handle');

  function updateSliderPosition(xPos) {
    const rect = container.getBoundingClientRect();
    let pos = ((xPos - rect.left) / rect.width) * 100;
    if (pos < 5) pos = 5;
    if (pos > 95) pos = 95;

    afterImage.style.width = `${pos}%`;
    handle.style.left = `${pos}%`;
  }

  handle.addEventListener('mousedown', (e) => {
    isDraggingSlider = true;
    e.preventDefault();
  });

  window.addEventListener('mouseup', () => {
    isDraggingSlider = false;
  });

  window.addEventListener('mousemove', (e) => {
    if (!isDraggingSlider) return;
    updateSliderPosition(e.clientX);
  });

  handle.addEventListener('touchstart', () => {
    isDraggingSlider = true;
  }, { passive: true });

  window.addEventListener('touchend', () => {
    isDraggingSlider = false;
  });

  window.addEventListener('touchmove', (e) => {
    if (!isDraggingSlider || !e.touches[0]) return;
    updateSliderPosition(e.touches[0].clientX);
  }, { passive: true });

  container.addEventListener('click', (e) => {
    updateSliderPosition(e.clientX);
  });
}

/* ==========================================================================
   3. Quick Quote Form -> WhatsApp Automation
   ========================================================================== */
function initQuickQuoteForm() {
  const form = document.getElementById('quick-quote-form');
  if (!form) return;

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const nombre = document.getElementById('quote-name')?.value || 'Cliente';
    const servicio = document.getElementById('quote-service')?.value || 'Reforma Integral';
    const poblacion = document.getElementById('quote-location')?.value || 'Alcoy';
    const notas = document.getElementById('quote-notes')?.value || '';

    const textMsg = `Hola Reformas Bañuls! Mi nombre es ${nombre}. Estoy interesado en un presupuesto para ${servicio} en ${poblacion}. Detalle de la reforma: ${notas}`;
    const waUrl = `https://wa.me/34601281313?text=${encodeURIComponent(textMsg)}`;
    
    window.open(waUrl, '_blank');
  });
}
