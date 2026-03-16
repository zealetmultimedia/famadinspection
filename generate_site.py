"""
FAMAD PLC — Multi-Page Roofing Inspection Website Generator
Generates all HTML pages for the inspection report site.
"""

import os

BASE = r"E:\CLIENT JOBS\FAMAD\FAMAD-INSPEECTION-WEBSITE"

# ─── Structure Data ────────────────────────────────────────────────────────────
STRUCTURES = [
    {"label": "A", "name": "Kinstar / Lontor Offices",
     "perimeter": "186.66", "area": "1,243.54", "roof": "1,189.7",
     "pictures": ["A-PICTURE1.JPG", "A-PICTURE2.JPG", "A-PICTURE3.JPG", "A-PICTURE4.JPG"],
     "measurements": ["A-MEASUREMENT1.jpg", "A-MEASUREMENT2.jpg"]},

    {"label": "B", "name": "FAMAD Central Store",
     "perimeter": "80.759", "area": "387.65", "roof": "373.6",
     "pictures": ["B-PICTURE1.JPG", "B-PICTURE2.JPG"],
     "measurements": ["B-MEASUREMENT1.jpg", "B-MEASUREMENT2.jpg"]},

    {"label": "C", "name": "GAC Motors",
     "perimeter": "49.036", "area": "145.51", "roof": "137.8",
     "pictures": ["C-PICTURE1.JPG", "C-PICTURE2.JPG"],
     "measurements": ["C-MEASUREMENT1.jpg", "C-MEASUREMENT2.jpg"]},

    {"label": "D", "name": "FAMAD Admin Office",
     "perimeter": "148.938", "area": "1,003.52", "roof": "898.4",
     "pictures": ["D-PICTURE1.JPG", "D-PICTURE2.JPG"],
     "measurements": ["D-MEASUREMENT1.jpg", "D-MEASUREMENT2.jpg"]},

    {"label": "E", "name": "FAMAD Factory",
     "perimeter": "464.581", "area": "12,963.32", "roof": "13,868.07",
     "featured": True,
     "estimation": "estimation-e.html",
     "pictures": ["E-PICTURE1.JPG", "E-PICTURE2.JPG", "E-PICTURE3.JPG", "E-PICTURE4.JPG", "E-PICTURE5.JPG"],
     "measurements": ["E-MEASUREMENT1.jpg", "E-MEASUREMENT2.jpg", "E-MEASUREMENT3.jpg",
                      "E-MEASUREMENT4.jpg", "E-MEASUREMENT5.jpg"]},

    {"label": "F", "name": "GAC Warehouse",
     "perimeter": "144.612", "area": "940.14", "roof": "960.4",
     "defects": ["F-DEFECT1.JPG","F-DEFECT2.JPG","F-DEFECT3.JPG","F-DEFECT4.JPG",
                 "F-DEFECT5.JPG","F-DEFECT6.JPG","F-DEFECT7.JPG"],
     "pictures": ["F-PICTURE1.JPG", "F-PICTURE2.JPG"],
     "measurements": ["F-MEASUREMENT1.jpg", "F-MEASUREMENT2.jpg", "F-MEASUREMENT3.jpg"]},

    {"label": "G", "name": "Kinlife",
     "perimeter": "187.957", "area": "1,155.43", "roof": "465.9",
     "defects": ["G-DEFECT1.JPG"],
     "pictures": ["G-PICTURE1.JPG", "G-PICTURE2.JPG"],
     "measurements": ["G-MEASUREMENT1.jpg", "G-MEASUREMENT2.jpg"]},

    {"label": "H", "name": "Elizabeth R / Gatimo",
     "perimeter": "298.993", "area": "3,656.86", "roof": "3,705.1",
     "pictures": ["H-PICTURE1.JPG", "H-PICTURE2.JPG"],
     "measurements": ["H-MEASUREMENT1.jpg", "H-MEASUREMENT2.jpg"]},

    {"label": "I", "name": "Generator Room",
     "perimeter": "78.32", "area": "294.94", "roof": "329.6",
     "pictures": ["I-PICTURE1.JPG", "I-PICTURE2.JPG"],
     "measurements": ["I-MEASUREMENT1.jpg", "I-MEASUREMENT2.jpg"]},

    {"label": "J", "name": "MTN-J",
     "perimeter": "131.731", "area": "936.4", "roof": "922.1",
     "pictures": ["J-PICTURE1.JPG", "J-PICTURE2.JPG"],
     "measurements": ["J-MEASUREMENT1.jpg", "J-MEASUREMENT2.jpg"]},

    {"label": "K", "name": "MTN-K",
     "perimeter": "185.736", "area": "1,877.01", "roof": "1,442.70",
     "pictures": ["K-PICTURE1.JPG", "K-PICTURE2.JPG"],
     "measurements": ["K-MEASUREMENT1.jpg", "K-MEASUREMENT2.jpg"]},

    {"label": "L", "name": "MTN-L",
     "perimeter": "107.559", "area": "644.21", "roof": "623.3",
     "pictures": ["L-PICTURE1.JPG", "L-PICTURE2.JPG"],
     "measurements": ["L-MEASUREMENT1.jpg", "L-MEASUREMENT2.jpg"]},

    {"label": "M", "name": "MTN-M",
     "perimeter": "78.129", "area": "316.48", "roof": "315.6",
     "pictures": ["M-PICTURE1.JPG", "M-PICTURE2.JPG"],
     "measurements": ["M-MEASUREMENT1.jpg", "M-MEASUREMENT2.jpg"]},

    {"label": "N", "name": "MTN-N",
     "perimeter": "130.413", "area": "978.2", "roof": "962.3",
     "pictures": ["N-PICTURE1.JPG", "N-PICTURE2.JPG"],
     "measurements": ["N-MEASUREMENT1.jpg", "N-MEASUREMENT2.jpg"]},

    {"label": "O", "name": "MTN-O",
     "perimeter": "178.559", "area": "1,447.27", "roof": "1,285.1",
     "pictures": ["O-PICTURE1.JPG", "O-PICTURE2.JPG"],
     "measurements": ["O-MEASUREMENT1.jpg", "O-MEASUREMENT2.jpg"]},

    {"label": "P", "name": "MTN-P",
     "perimeter": "154.479", "area": "971.1", "roof": "749.2",
     "pictures": ["P-PICTURE1.JPG", "P-PICTURE2.JPG"],
     "measurements": ["P-MEASUREMENT1.jpg", "P-MEASUREMENT2.jpg"]},

    {"label": "Q", "name": "MTN-Q",
     "perimeter": "73.251", "area": "282.61", "roof": "278.4",
     "pictures": ["Q-PICTURE1.JPG", "Q-PICTURE2.JPG"],
     "measurements": ["Q-MEASUREMENT1.jpg", "Q-MEASUREMENT2.jpg"]},

    {"label": "R", "name": "MTN-R",
     "perimeter": "53.242", "area": "176.66", "roof": "176.3",
     "pictures": ["R-PICTURE1.JPG", "R-PICTURE2.JPG"],
     "measurements": ["R-MEASUREMENT1.jpg", "R-MEASUREMENT2.jpg"]},

    {"label": "S", "name": "MTN-S",
     "perimeter": "63.027", "area": "248.32", "roof": "248.5",
     "pictures": ["S-PICTURE1.JPG", "S-PICTURE2.JPG"],
     "measurements": ["S-MEASUREMENT1.jpg", "S-MEASUREMENT2.jpg"]},

    {"label": "T", "name": "MTN-T",
     "perimeter": "54.613", "area": "179.53", "roof": "178.0",
     "pictures": ["T-PICTURE1.JPG", "T-PICTURE2.JPG"],
     "measurements": ["T-MEASUREMENT1.jpg", "T-MEASUREMENT2.jpg"]},
]

FACILITY_IMAGES = [
    ("FAMAD-FACILITY-ANGLE1.JPG", "Aerial View — Angle 1"),
    ("FAMAD-FACILITY-ANGLE2.JPG", "Aerial View — Angle 2"),
    ("FAMAD-FACILITY-ANGLE3.JPG", "Aerial View — Angle 3"),
    ("FAMAD-FACILITY.jpg",        "Full Site Overview"),
    ("FAMAD-ADMIN_BLOCK.jpg",     "Administration Block"),
    ("ADMIN AND FAMAD FACTORY.jpg", "Admin Block &amp; Factory"),
    ("FAMAD-FACILITY-PERIMETER-MEASUREMENT.jpg", "Perimeter Measurement"),
    ("KINSTAR-BLOCK.jpg",         "Kinstar Block"),
    ("KINLIFE_WORKSHOP.jpg",      "Kinlife Workshop"),
    ("ELIZABETH R.jpg",           "Elizabeth R / Gatimo"),
    ("MTN-YARD.jpg",              "MTN Yard"),
    ("POWER- YARD.jpg",           "Power Yard"),
]

# ─── Helpers ──────────────────────────────────────────────────────────────────

def struct_filename(label):
    return f"structure-{label.lower()}.html"

def nav(active=""):
    pages = [
        ("index.html",       "Home"),
        ("overview.html",    "Overview"),
        ("environment.html", "Environment"),
        ("calculations.html","Roof Areas"),
        ("structures.html",  "Structures"),
        ("defects.html",     "Defects"),
        ("maintenance.html", "Maintenance"),
    ]
    items = ""
    for href, label in pages:
        cls = ' class="active"' if label == active else ""
        items += f'<li><a href="{href}"{cls}>{label}</a></li>\n        '
    return f"""<nav class="navbar" id="navbar">
  <div class="nav-inner">
    <a href="index.html" class="nav-brand">
      <span class="brand-tag">FAMAD PLC</span>
      <span class="brand-sub">Roofing Inspection Report</span>
    </a>
    <button class="nav-toggle" id="navToggle" aria-label="Toggle menu">
      <span></span><span></span><span></span>
    </button>
    <ul class="nav-links" id="navLinks">
        {items}</ul>
  </div>
</nav>"""

def footer():
    return """<footer class="footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <span class="brand-tag">FAMAD PLC</span>
        <p>Technical Evaluation of Roofing Systems and Structural Integrity</p>
        <p class="footer-addr">Kilometer 15, Ikorodu Road, Ojota, Lagos, Nigeria</p>
      </div>
      <div class="footer-info">
        <h4>Report Summary</h4>
        <ul>
          <li>Total Land Area: 56,819.28 m&sup2;</li>
          <li>Site Perimeter: 967.12 m</li>
          <li>Structures Inspected: 20</li>
          <li>Factory Roof Area: 13,868.07 m&sup2;</li>
          <li>Year Established: 1960</li>
        </ul>
      </div>
      <div class="footer-info">
        <h4>Inspection Scope</h4>
        <ul>
          <li>Aerial Photogrammetry</li>
          <li>Structural Dimensional Survey</li>
          <li>Atmospheric Corrosion Analysis</li>
          <li>Roof Coverage Quantification</li>
          <li>Environmental Stressor Assessment</li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <p>FAMAD PLC Industrial Facility &mdash; Confidential Technical Report</p>
      <div class="footer-presenter">
        <span>Presented by</span>
        <a href="maintenance.html" class="zealet-credit">
          <img src="assets/img/zealet-logo.svg" alt="Zealet" class="zealet-logo-sm" />
          <span>Zealet Creative Division</span>
        </a>
      </div>
    </div>
  </div>
</footer>"""

def lightbox():
    return """<div class="lightbox" id="lightbox">
  <button class="lb-close" id="lbClose">&times;</button>
  <button class="lb-prev" id="lbPrev">&#8249;</button>
  <button class="lb-next" id="lbNext">&#8250;</button>
  <div class="lb-img-wrap"><img id="lbImg" src="" alt="Enlarged view" /></div>
</div>"""

def html_head(title, desc=""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title} &mdash; FAMAD PLC Roofing Inspection</title>
  <meta name="description" content="{desc}" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Montserrat:wght@700;800;900&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="assets/css/style.css" />
</head>
<body>"""

def html_foot():
    return f"""  {lightbox()}
  <script src="assets/js/main.js"></script>
</body>
</html>"""

def breadcrumb(crumbs):
    """crumbs = [('Home', 'index.html'), ('Structures', 'structures.html'), ('Structure A', None)]"""
    parts = []
    for label, href in crumbs:
        if href:
            parts.append(f'<a href="{href}">{label}</a>')
        else:
            parts.append(f'<span>{label}</span>')
    return '<nav class="breadcrumb">' + ' <span class="bc-sep">/</span> '.join(parts) + '</nav>'

# ─── Page: index.html ─────────────────────────────────────────────────────────

def gen_index():
    return f"""{html_head("FAMAD PLC Roofing Inspection", "Technical evaluation of roofing systems and structural integrity for the FAMAD PLC industrial facility, Ojota, Lagos.")}
{nav("Home")}

<header class="hero" id="hero">
  <div class="hero-bg">
    <img src="PICTURE FOLDER/FAMAD-FACILITY/FAMAD-FACILITY-ANGLE1.JPG" alt="FAMAD PLC Aerial View" class="hero-img" />
    <div class="hero-overlay"></div>
  </div>
  <div class="hero-content">
    <div class="hero-badge">Technical Evaluation Report</div>
    <h1 class="hero-title">Roofing Systems &amp;<br/>Structural Integrity</h1>
    <p class="hero-sub">FAMAD PLC Industrial Facility &mdash; Kilometer 15, Ikorodu Road, Ojota, Lagos</p>
    <div class="hero-stats">
      <div class="hstat"><span class="hstat-num">56,819</span><span class="hstat-lbl">m&sup2; Land Area</span></div>
      <div class="hstat-div"></div>
      <div class="hstat"><span class="hstat-num">20</span><span class="hstat-lbl">Structures Inspected</span></div>
      <div class="hstat-div"></div>
      <div class="hstat"><span class="hstat-num">13,868</span><span class="hstat-lbl">m&sup2; Factory Roof</span></div>
      <div class="hstat-div"></div>
      <div class="hstat"><span class="hstat-num">1960</span><span class="hstat-lbl">Year Established</span></div>
    </div>
    <a href="overview.html" class="hero-cta">View Full Report</a>
  </div>
  <div class="scroll-indicator"><div class="scroll-dot"></div></div>
</header>

<section class="section landing-cards-section">
  <div class="container">
    <div class="section-label">Report Sections</div>
    <h2 class="section-title">Technical Evaluation Breakdown</h2>
    <p class="section-intro">A comprehensive multi-section assessment covering facility history, environmental stressors, structural dimensions, and photographic evidence for all 20 inspected buildings.</p>
    <div class="landing-cards">
      <a href="overview.html" class="lcard">
        <div class="lcard-icon">
          <img src="PICTURE FOLDER/FAMAD-FACILITY/FAMAD-FACILITY.jpg" alt="" />
        </div>
        <div class="lcard-body">
          <span class="lcard-num">01</span>
          <h3>Facility Overview</h3>
          <p>Site history, property attributes, land area, perimeter, and strategic positioning of the FAMAD PLC complex.</p>
          <span class="lcard-arrow">View Section &rarr;</span>
        </div>
      </a>
      <a href="environment.html" class="lcard">
        <div class="lcard-icon">
          <img src="PICTURE FOLDER/FAMAD-FACILITY/FAMAD-FACILITY-ANGLE2.JPG" alt="" />
        </div>
        <div class="lcard-body">
          <span class="lcard-num">02</span>
          <h3>Environmental Analysis</h3>
          <p>Atmospheric corrosion assessment, pollution stressors from the Olusosun landfill, and elevation profiling.</p>
          <span class="lcard-arrow">View Section &rarr;</span>
        </div>
      </a>
      <a href="calculations.html" class="lcard">
        <div class="lcard-icon">
          <img src="PICTURE FOLDER/E/E-MEASUREMENT1.jpg" alt="" />
        </div>
        <div class="lcard-body">
          <span class="lcard-num">03</span>
          <h3>Roof Area Calculations</h3>
          <p>Full dimensional breakdown of all 20 structures, factory roof segment calculations, and total coverage data.</p>
          <span class="lcard-arrow">View Section &rarr;</span>
        </div>
      </a>
      <a href="structures.html" class="lcard">
        <div class="lcard-icon">
          <img src="PICTURE FOLDER/FAMAD-FACILITY/FAMAD-FACILITY-LABELLED.jpg" alt="" />
        </div>
        <div class="lcard-body">
          <span class="lcard-num">04</span>
          <h3>Structure Reports</h3>
          <p>Individual photographic and dimensional records for all 20 structures (A&ndash;T) with measurement documentation.</p>
          <span class="lcard-arrow">View Structures &rarr;</span>
        </div>
      </a>
    </div>
  </div>
</section>

{footer()}
{html_foot()}"""

# ─── Page: overview.html ──────────────────────────────────────────────────────

def gen_overview():
    facility_gallery = ""
    for fname, caption in FACILITY_IMAGES:
        facility_gallery += f"""      <div class="gal-item lightbox-trigger">
        <img src="PICTURE FOLDER/FAMAD-FACILITY/{fname}" alt="{caption}" />
        <span class="gal-caption">{caption}</span>
      </div>
"""
    return f"""{html_head("Facility Overview", "General overview of the FAMAD PLC industrial facility, Ojota, Lagos.")}
{nav("Overview")}

<div class="page-hero page-hero--overview">
  <img src="PICTURE FOLDER/FAMAD-FACILITY/FAMAD-FACILITY-ANGLE3.JPG" alt="FAMAD Facility" class="page-hero-img" />
  <div class="page-hero-overlay"></div>
  <div class="page-hero-content container">
    {breadcrumb([("Home", "index.html"), ("Facility Overview", None)])}
    <h1 class="page-hero-title">Facility Overview</h1>
    <p class="page-hero-sub">Industrial Heritage &amp; Strategic Positioning of the FAMAD Complex</p>
  </div>
</div>

<section class="section">
  <div class="container">
    <div class="section-label">Section 01</div>
    <h2 class="section-title">Industrial Heritage &amp; Strategic Positioning</h2>
    <div class="two-col">
      <div class="prose">
        <p>The industrial evolution of Nigeria is intrinsically linked to the development of the Ikorodu Road corridor in Lagos, a primary artery that has facilitated the movement of goods and labor for over six decades. FAMAD PLC, formerly operating under the globally recognized Bata brand, established its footprint at Kilometer 15, Ikorodu Road, Ojota, in 1960.</p>
        <p>The FAMAD facility remains a cornerstone of this heritage, producing a diverse range of footwear, including industrial work boots, school shoes, and sneakers tailored for the Nigerian environment.</p>
        <p>The site at Kilometer 15 is a substantial industrial holding, with a total fenced land area of 56,819.28 square meters. A detailed analysis of the aerial imagery reveals a complex arrangement of high-bay warehouses and specialized utility zones.</p>
        <p>The facility's location is strategically vital, situated between the high-traffic Ikorodu Road to the East and a dense residential/commercial mix to the West. This proximity to critical infrastructure like the Lagos Metropolitan Area Transport Authority (LAMATA) Quality Bus Corridors (QBC) project introduces unique environmental stressors that directly impact the longevity of the facility's roofing systems.</p>
        <p>Industrial operations of this scale require robust roofing infrastructure to protect sensitive raw materials, such as leather and adhesives, as well as high-precision manufacturing equipment. The roofing system at FAMAD PLC is not merely a weather barrier but a critical component of the climate control and safety architecture of the plant.</p>
      </div>
      <div>
        <div class="prop-table-wrap">
          <table class="prop-table">
            <tbody>
              <tr><th>Facility Name</th><td>FAMAD PLC <span class="tag">Formerly Bata Nigeria</span></td></tr>
              <tr><th>Primary Address</th><td>Km 15, Ikorodu Road, Ojota, Lagos</td></tr>
              <tr><th>Year Established</th><td>1960</td></tr>
              <tr><th>Total Land Area</th><td>56,819.28 m&sup2;</td></tr>
              <tr><th>Total Site Perimeter</th><td>967.12 m</td></tr>
              <tr><th>Elevation (Min)</th><td>19.9 m</td></tr>
              <tr><th>Elevation (Median)</th><td>22.23 m</td></tr>
              <tr><th>Elevation (Max)</th><td>24.55 m</td></tr>
              <tr><th>Primary Production</th><td>Industrial, School &amp; Casual Footwear</td></tr>
              <tr><th>Surrounding Infrastructure</th><td>Ikorodu Road, LAMATA BRT Corridor, Olusosun Landfill</td></tr>
              <tr><th>Structures Inspected</th><td>20 (Labels A &ndash; T)</td></tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- SITE PLAN MAPS -->
<section class="section">
  <div class="container">
    <div class="section-label">Site Reference Maps</div>
    <h2 class="section-title">Facility Site Plans</h2>
    <p class="section-intro">The two maps below identify all structures on the FAMAD PLC site, labelled A through T. The annotated aerial photograph and CAD line drawing together provide the primary spatial reference for this inspection.</p>
    <div class="sitemap-grid">
      <div class="sitemap-card lightbox-trigger">
        <div class="sitemap-badge">Annotated Site Plan</div>
        <img src="PICTURE FOLDER/FAMAD-FACILITY/FAMAD-FACILITY-LABELLED.jpg" alt="Labelled Site Plan — Structures A to T" />
        <div class="sitemap-caption">
          <strong>Labelled Aerial Plan</strong>
          <span>All structures identified by label A &ndash; T</span>
        </div>
      </div>
      <div class="sitemap-card lightbox-trigger">
        <div class="sitemap-badge">CAD Line Drawing</div>
        <img src="PICTURE FOLDER/FAMAD-FACILITY/FAMAD-FACILITY-CAD.jpg" alt="CAD Site Drawing — Structures A to T" />
        <div class="sitemap-caption">
          <strong>CAD Site Drawing</strong>
          <span>Architectural line drawing with all structure labels</span>
        </div>
      </div>
    </div>
{sitemap_legend()}  </div>
</section>

<!-- LOCATION MAP -->
<section class="section section-alt">
  <div class="container">
    <div class="section-label">Location</div>
    <h2 class="section-title">Facility Location</h2>
    <p class="section-intro">FAMAD PLC is situated at Kilometre 15, Ikorodu Road, Ojota, Lagos — a key position along one of Lagos State's primary industrial corridors.</p>
    <div class="map-wrap">
      <iframe
        src="https://maps.google.com/maps?q=FAMAD+PLC+Km+15+Ikorodu+Road+Ojota+Lagos+Nigeria&output=embed&z=17"
        width="100%" height="420" style="border:0; border-radius:10px;"
        allowfullscreen loading="lazy" referrerpolicy="no-referrer-when-downgrade"
        title="FAMAD PLC Location — Km 15 Ikorodu Road, Ojota, Lagos">
      </iframe>
      <div class="map-footer">
        <div class="map-address">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
          Km 15, Ikorodu Road, Ojota, Lagos, Nigeria
        </div>
        <a href="https://maps.app.goo.gl/LvbjffZGzi4rJDxD7" target="_blank" rel="noopener" class="map-link">
          Open in Google Maps &rarr;
        </a>
      </div>
    </div>
  </div>
</section>

<!-- FACILITY VIDEO -->
<section class="section">
  <div class="container">
    <div class="section-label">Facility Flythrough</div>
    <h2 class="section-title">Aerial Video Tour</h2>
    <p class="section-intro">A drone flythrough of the FAMAD PLC complex, providing a full aerial perspective of the site layout, roof conditions, and surrounding environment.</p>
    <div class="video-wrap">
      <div class="video-responsive">
        <iframe
          src="https://www.youtube.com/embed/qCAAfWlVrx4?rel=0&amp;modestbranding=1"
          title="FAMAD PLC Facility Aerial Flythrough"
          frameborder="0"
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
          allowfullscreen
          loading="lazy">
        </iframe>
      </div>
      <div class="video-footer">
        <div class="video-label">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M23.5 6.2a3 3 0 0 0-2.1-2.1C19.5 3.6 12 3.6 12 3.6s-7.5 0-9.4.5A3 3 0 0 0 .5 6.2C0 8.1 0 12 0 12s0 3.9.5 5.8a3 3 0 0 0 2.1 2.1c1.9.5 9.4.5 9.4.5s7.5 0 9.4-.5a3 3 0 0 0 2.1-2.1C24 15.9 24 12 24 12s0-3.9-.5-5.8z"/><polygon points="9.75 15.02 15.5 12 9.75 8.98 9.75 15.02" fill="white"/></svg>
          FAMAD PLC &mdash; Facility Aerial Flythrough
        </div>
        <a href="https://youtu.be/qCAAfWlVrx4" target="_blank" rel="noopener" class="map-link">
          Watch on YouTube &rarr;
        </a>
      </div>
    </div>
  </div>
</section>

<!-- GENERAL FACILITY PHOTOGRAPHY -->
<section class="section section-alt">
  <div class="container">
    <div class="section-label">Site Photography</div>
    <h2 class="section-title">General Facility Photographs</h2>
    <p class="section-intro">Aerial and ground-level imagery documenting the full FAMAD PLC site and its key zones.</p>
    <div class="photo-gallery">
{facility_gallery}    </div>
  </div>
</section>

{footer()}
{html_foot()}"""

# ─── Page: environment.html ───────────────────────────────────────────────────

def gen_environment():
    return f"""{html_head("Environmental Analysis", "Atmospheric corrosion and environmental stressor analysis for the FAMAD PLC facility.")}
{nav("Environment")}

<div class="page-hero page-hero--env">
  <img src="PICTURE FOLDER/FAMAD-FACILITY/FAMAD-FACILITY-ANGLE2.JPG" alt="FAMAD Facility Environment" class="page-hero-img" />
  <div class="page-hero-overlay"></div>
  <div class="page-hero-content container">
    {breadcrumb([("Home", "index.html"), ("Environmental Analysis", None)])}
    <h1 class="page-hero-title">Environmental Analysis</h1>
    <p class="page-hero-sub">Atmospheric Corrosion &amp; Environmental Stressor Assessment</p>
  </div>
</div>

<section class="section">
  <div class="container">
    <div class="section-label">Section 02</div>
    <h2 class="section-title">Atmospheric Corrosion &amp; Environmental Stressors</h2>
    <div class="two-col">
      <div class="prose">
        <p>The geographical location of the FAMAD PLC factory in Ojota places it within one of the most chemically aggressive environments in the Lagos metropolis. The primary driver of this hostility is the facility's proximity to the <strong>Olusosun landfill</strong>, a sprawling waste disposal site covering between 42 and 100 acres.</p>
        <p>Since its inception in 1989, the landfill has become a major source of atmospheric pollutants, including <strong>sulfur dioxide (SO&#x2082;)</strong>, <strong>nitrogen oxides (NO&#x2093;)</strong>, and <strong>hydrogen sulfide (H&#x2082;S)</strong>, resulting from the decomposition of organic waste and the frequent burning of electronic waste.</p>
        <p>The interaction between these pollutants and the high relative humidity of Lagos &mdash; often exceeding <strong>80% year-round</strong> &mdash; creates a corrosive aerosol that settles on the expansive roof surfaces of the FAMAD plant, dramatically accelerating material degradation and reducing the serviceable life of roofing sheets.</p>
        <p>Additionally, the heavy vehicle traffic on Ikorodu Road and the adjacent LAMATA BRT corridor contributes nitrogen oxide emissions that further compound the corrosive environment at roof level. Given the elevated position of the structures, wind-borne pollutants from the landfill are deposited directly onto roofing surfaces, initiating oxidation cycles that are accelerated by seasonal rainfall.</p>
        <p>By utilizing advanced aerial diagnostics and adhering to the confirmed 93m structural reference, the facility can mitigate the aggressive environmental risks posed by its proximity to the Olusosun landfill and Ikorodu Road. This data-driven approach ensures that the FAMAD facility remains protected under a roof as durable as the footwear it produces.</p>
      </div>
      <div class="env-cards">
        <div class="env-card">
          <div class="env-icon">SO<sub>2</sub></div>
          <div class="env-text">
            <strong>Sulfur Dioxide</strong>
            <p>Released from landfill organic decomposition and e-waste burning. Reacts with moisture to form sulfuric acid, which corrodes metallic roofing.</p>
          </div>
        </div>
        <div class="env-card">
          <div class="env-icon">NO<sub>x</sub></div>
          <div class="env-text">
            <strong>Nitrogen Oxides</strong>
            <p>Byproduct of heavy vehicle traffic on the Ikorodu Road BRT corridor. Forms nitric acid in moist conditions, contributing to surface pitting.</p>
          </div>
        </div>
        <div class="env-card">
          <div class="env-icon">H<sub>2</sub>S</div>
          <div class="env-text">
            <strong>Hydrogen Sulfide</strong>
            <p>Emitted from landfill anaerobic zones. Highly corrosive to galvanized and aluminum roofing; promotes rapid oxidation even at low concentrations.</p>
          </div>
        </div>
        <div class="env-card">
          <div class="env-icon">80%</div>
          <div class="env-text">
            <strong>Relative Humidity</strong>
            <p>Year-round high humidity in Lagos amplifies corrosive aerosol formation and sustains electrochemical corrosion processes on roof surfaces.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="section-label">Elevation Data</div>
    <h2 class="section-title">Site Elevation Profile</h2>
    <p class="section-intro">Elevation measurements confirm the high-profile exposure of roof surfaces to prevailing wind-borne pollutants and corrosive aerosols from the surrounding environment.</p>
    <div class="elevation-banner">
      <div class="elevation-stats">
        <div class="elev-item">
          <div class="elev-bar" style="height:60%"></div>
          <span class="elev-val">19.9 m</span>
          <span class="elev-lbl">Minimum</span>
        </div>
        <div class="elev-item">
          <div class="elev-bar" style="height:78%"></div>
          <span class="elev-val">22.23 m</span>
          <span class="elev-lbl">Median</span>
        </div>
        <div class="elev-item">
          <div class="elev-bar" style="height:100%"></div>
          <span class="elev-val">24.55 m</span>
          <span class="elev-lbl">Maximum</span>
        </div>
      </div>
      <p class="elev-note">All values in meters above ground level. Source: aerial photogrammetric survey.</p>
    </div>
  </div>
</section>

{footer()}
{html_foot()}"""

# ─── Page: calculations.html ──────────────────────────────────────────────────

def gen_calculations():
    rows = ""
    for s in STRUCTURES:
        cls = "row-highlight" if s.get("featured") else ""
        cls_attr = f' class="{cls}"' if cls else ""
        href = struct_filename(s['label'])
        rows += f"""            <tr{cls_attr} data-href="{href}">
              <td class="label-cell">{s['label']}</td>
              <td>{s['name']}</td>
              <td>{s['perimeter']}</td>
              <td>{s['area']}</td>
              <td>{s['roof']}</td>
            </tr>
"""
    return f"""{html_head("Roof Area Calculations", "Detailed roof area calculations and dimensional data for all structures at the FAMAD PLC facility.")}
{nav("Roof Areas")}

<div class="page-hero page-hero--calc">
  <img src="PICTURE FOLDER/E/E-MEASUREMENT1.jpg" alt="Roof Measurements" class="page-hero-img" />
  <div class="page-hero-overlay"></div>
  <div class="page-hero-content container">
    {breadcrumb([("Home", "index.html"), ("Roof Area Calculations", None)])}
    <h1 class="page-hero-title">Roof Area Calculations</h1>
    <p class="page-hero-sub">Dimensional Quantification of All 20 Structures</p>
  </div>
</div>

<section class="section">
  <div class="container">
    <div class="section-label">Section 03</div>
    <h2 class="section-title">FAMAD Factory &mdash; Main Roof (Structure E)</h2>
    <p class="section-intro">The primary factory building (Structure E) represents the largest roofing area on site. Calculations are based on aerial photogrammetry with the confirmed 93 m structural reference length.</p>

    <div class="calc-grid">
      <div class="calc-card primary-calc">
        <h3>Main Slab Specification</h3>
        <div class="calc-spec"><span class="spec-badge">Roof Pitch: 18&deg;</span></div>
        <div class="calc-breakdown">
          <div class="calc-row"><span>Slab Width</span><span>8.83 m</span></div>
          <div class="calc-row"><span>Slab Length</span><span>93 m</span></div>
          <div class="calc-row"><span>Area per Slab (8.83 &times; 93)</span><span>821.19 m&sup2;</span></div>
          <div class="calc-row"><span>Number of Segments</span><span>13</span></div>
          <div class="calc-row highlight"><span>Total Slab Area</span><span>10,675.47 m&sup2;</span></div>
        </div>
        <div class="calc-breakdown mt">
          <h4>Additional Segments</h4>
          <div class="calc-row"><span>Front Segment (10.52 &times; 93 m)</span><span>978.36 m&sup2;</span></div>
          <div class="calc-row"><span>Back Segment (7.68 &times; 93 m)</span><span>714.24 m&sup2;</span></div>
          <div class="calc-row"><span>Roof Flaps (15 &times; 100 m&sup2;)</span><span>1,500 m&sup2;</span></div>
          <div class="calc-row grand-total"><span>Total Factory Roof Area</span><span>13,868.07 m&sup2;</span></div>
        </div>
      </div>
      <div class="calc-img-wrap">
        <img src="PICTURE FOLDER/E/E-MEASUREMENT1.jpg" alt="Factory Roof Measurement 1" class="lightbox-trigger" />
        <img src="PICTURE FOLDER/E/E-MEASUREMENT2.jpg" alt="Factory Roof Measurement 2" class="lightbox-trigger" />
        <img src="PICTURE FOLDER/E/E-MEASUREMENT3.jpg" alt="Factory Roof Measurement 3" class="lightbox-trigger" />
      </div>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="section-label">Complete Site Data</div>
    <h2 class="section-title">All Structures &mdash; Area Summary</h2>
    <p class="section-intro">Consolidated dimensional data for all 20 structures across the FAMAD PLC facility. Click any structure label to view its detailed report.</p>
    <div class="table-wrap">
      <table class="site-table">
        <thead>
          <tr>
            <th>Label</th>
            <th>Structure</th>
            <th>Perimeter (m)</th>
            <th>Total Area (m&sup2;)</th>
            <th>Roof Coverage (m&sup2;)</th>
          </tr>
        </thead>
        <tbody>
{rows}        </tbody>
      </table>
    </div>
  </div>
</section>

{footer()}
{html_foot()}"""

# ─── Page: structures.html ────────────────────────────────────────────────────

def sitemap_legend():
    """Renders a compact A-T legend table for site plan sections."""
    items = ""
    for s in STRUCTURES:
        href = struct_filename(s['label'])
        items += f'      <a href="{href}" class="legend-item"><span class="legend-label">{s["label"]}</span><span class="legend-name">{s["name"]}</span></a>\n'
    return f"""    <div class="sitemap-legend">
      <div class="legend-heading">Structure Labels</div>
{items}    </div>"""

def gen_structures():
    cards = ""
    for s in STRUCTURES:
        pic = s["pictures"][0] if s["pictures"] else ""
        featured_cls = " featured" if s.get("featured") else ""
        featured_badge = ' <span class="featured-badge">Primary</span>' if s.get("featured") else ""
        cards += f"""      <a href="{struct_filename(s['label'])}" class="struct-index-card{featured_cls}">
        <div class="sic-img">
          <img src="PICTURE FOLDER/{s['label']}/{pic}" alt="Structure {s['label']}" />
          <span class="sic-label">{s['label']}</span>
        </div>
        <div class="sic-body">
          <h3>{s['name']}{featured_badge}</h3>
          <div class="sic-stats">
            <span><strong>{s['roof']}</strong> m&sup2; Roof</span>
            <span>{s['area']} m&sup2; Total</span>
          </div>
          <span class="sic-link">View Report &rarr;</span>
        </div>
      </a>
"""
    return f"""{html_head("Structure Reports", "Individual photographic and dimensional reports for all 20 structures at the FAMAD PLC facility.")}
{nav("Structures")}

<div class="page-hero page-hero--struct">
  <img src="PICTURE FOLDER/FAMAD-FACILITY/FAMAD-FACILITY-ANGLE1.JPG" alt="FAMAD Facility Aerial" class="page-hero-img" />
  <div class="page-hero-overlay"></div>
  <div class="page-hero-content container">
    {breadcrumb([("Home", "index.html"), ("Structure Reports", None)])}
    <h1 class="page-hero-title">Structure Reports</h1>
    <p class="page-hero-sub">Photographic &amp; Dimensional Records for All 20 Inspected Structures (A &ndash; T)</p>
  </div>
</div>

<!-- SITE PLAN MAPS -->
<section class="section section-alt">
  <div class="container">
    <div class="section-label">Site Reference Maps</div>
    <h2 class="section-title">Facility Site Plans &mdash; Structures A &ndash; T</h2>
    <p class="section-intro">All 20 inspected structures are labelled A through T on the site plans below. Use these maps as a reference when navigating individual structure reports.</p>
    <div class="sitemap-grid">
      <div class="sitemap-card lightbox-trigger">
        <div class="sitemap-badge">Annotated Site Plan</div>
        <img src="PICTURE FOLDER/FAMAD-FACILITY/FAMAD-FACILITY-LABELLED.jpg" alt="Labelled Site Plan — Structures A to T" />
        <div class="sitemap-caption">
          <strong>Labelled Aerial Plan</strong>
          <span>All structures identified by label A &ndash; T</span>
        </div>
      </div>
      <div class="sitemap-card lightbox-trigger">
        <div class="sitemap-badge">CAD Line Drawing</div>
        <img src="PICTURE FOLDER/FAMAD-FACILITY/FAMAD-FACILITY-CAD.jpg" alt="CAD Site Drawing — Structures A to T" />
        <div class="sitemap-caption">
          <strong>CAD Site Drawing</strong>
          <span>Architectural line drawing with all structure labels</span>
        </div>
      </div>
    </div>
{sitemap_legend()}  </div>
</section>

<!-- STRUCTURE CARDS GRID -->
<section class="section">
  <div class="container">
    <div class="section-label">Section 04</div>
    <h2 class="section-title">All Structures (A &ndash; T)</h2>
    <p class="section-intro">Select any structure to view its complete inspection record, including facility photographs and annotated measurement documentation.</p>
    <div class="struct-index-grid">
{cards}    </div>
  </div>
</section>

{footer()}
{html_foot()}"""

# ─── Individual Structure Pages ───────────────────────────────────────────────

def gen_structure(s, prev_s, next_s):
    label = s["label"]
    name  = s["name"]

    # ── Facility photos section ──
    pics_html = ""
    for i, pic in enumerate(s["pictures"]):
        active = " active" if i == 0 else ""
        pics_html += f'          <img src="PICTURE FOLDER/{label}/{pic}" alt="{name} — Photo {i+1}" class="facility-slide{active} lightbox-trigger" />\n'

    pic_thumbs = ""
    for i, pic in enumerate(s["pictures"]):
        active = " active" if i == 0 else ""
        pic_thumbs += f'          <img src="PICTURE FOLDER/{label}/{pic}" alt="" class="thumb{active}" />\n'

    # ── Measurement photos section ──
    meas_html = ""
    for i, meas in enumerate(s["measurements"]):
        meas_html += f"""        <div class="meas-card lightbox-trigger">
          <img src="PICTURE FOLDER/{label}/{meas}" alt="{name} — Measurement {i+1}" />
          <span class="meas-label">Measurement {i+1}</span>
        </div>
"""

    # ── Estimation banner (Structure E only) ──
    if s.get("estimation"):
        estimation_banner = f"""
    <div style="margin-top:22px; padding:18px 22px; background:rgba(249,115,22,0.07); border-left:4px solid var(--orange); border-radius:0 10px 10px 0; display:flex; align-items:center; justify-content:space-between; gap:16px; flex-wrap:wrap;">
      <div>
        <strong style="color:var(--navy); font-size:0.95rem;">Roof Material Estimation Available</strong>
        <p style="margin:4px 0 0; font-size:0.85rem; color:var(--slate);">Detailed quantity take-off for all ancillary roof materials (excludes roof sheets) &mdash; purlins, ridge capping, gutters, flashings, fasteners, and insulation.</p>
      </div>
      <a href="{s['estimation']}" style="flex-shrink:0; display:inline-block; background:var(--orange); color:#fff; font-size:0.85rem; font-weight:700; padding:10px 20px; border-radius:8px; text-decoration:none; white-space:nowrap;">View Estimation &rarr;</a>
    </div>"""
    else:
        estimation_banner = ""

    # ── Defects callout section ──
    if s.get("defects"):
        n = len(s["defects"])
        defects_section = f"""
<!-- DEFECTS CALLOUT -->
<section class="section section-alt">
  <div class="container">
    <div class="section-label">Condition Assessment</div>
    <h2 class="section-title">Recorded Defects</h2>
    <p class="section-intro">{n} defect{"s" if n != 1 else ""} recorded for Structure {label} — {name}. View the full defects register for detailed photographic documentation.</p>
    <div class="defect-callout">
      <div class="dc-count"><span class="dc-num">{n}</span><span class="dc-lbl">Defect{"s" if n != 1 else ""} Recorded</span></div>
      <div class="dc-thumbs">
{"".join(f'        <img src="PICTURE FOLDER/DEFECTS/{d}" alt="Defect {i+1}" class="dc-thumb" />' + chr(10) for i, d in enumerate(s["defects"][:4]))}      </div>
      <a href="defects.html#{label.lower()}" class="dc-link">View All Defects for Structure {label} &rarr;</a>
    </div>
  </div>
</section>
"""
    else:
        defects_section = ""

    # ── Prev / Next ──
    prev_btn = ""
    if prev_s:
        prev_btn = f'<a href="{struct_filename(prev_s["label"])}" class="struct-nav-btn prev">&larr; {prev_s["label"]}: {prev_s["name"]}</a>'
    next_btn = ""
    if next_s:
        next_btn = f'<a href="{struct_filename(next_s["label"])}" class="struct-nav-btn next">{next_s["label"]}: {next_s["name"]} &rarr;</a>'

    featured_badge = ' <span class="featured-badge">Primary Structure</span>' if s.get("featured") else ""

    hero_img = s["pictures"][0] if s["pictures"] else (s["measurements"][0] if s["measurements"] else "")

    return f"""{html_head(f"Structure {label} — {name}", f"Inspection report for Structure {label}: {name} at the FAMAD PLC facility.")}
{nav("Structures")}

<div class="page-hero page-hero--structure">
  <img src="PICTURE FOLDER/{label}/{hero_img}" alt="Structure {label} — {name}" class="page-hero-img" />
  <div class="page-hero-overlay"></div>
  <div class="page-hero-content container">
    {breadcrumb([("Home", "index.html"), ("Structures", "structures.html"), (f"{label}: {name}", None)])}
    <h1 class="page-hero-title">
      <span class="hero-label-badge">{label}</span>
      {name}{featured_badge}
    </h1>
    <div class="page-hero-stats">
      <div class="ph-stat"><span class="ph-val">{s['perimeter']} m</span><span class="ph-lbl">Perimeter</span></div>
      <div class="ph-stat"><span class="ph-val">{s['area']} m&sup2;</span><span class="ph-lbl">Total Area</span></div>
      <div class="ph-stat"><span class="ph-val">{s['roof']} m&sup2;</span><span class="ph-lbl">Roof Coverage</span></div>
    </div>
  </div>
</div>

<!-- MEASUREMENTS -->
<section class="section">
  <div class="container">
    <div class="section-label">Area &amp; Dimensions</div>
    <h2 class="section-title">Measurement Documentation</h2>
    <p class="section-intro">Annotated aerial measurement screenshots confirming the dimensional data for Structure {label}.</p>
    <div class="meas-summary">
      <div class="meas-stat"><span class="ms-val">{s['perimeter']} m</span><span class="ms-lbl">Perimeter</span></div>
      <div class="meas-stat"><span class="ms-val">{s['area']} m&sup2;</span><span class="ms-lbl">Total Floor Area</span></div>
      <div class="meas-stat ms-highlight"><span class="ms-val">{s['roof']} m&sup2;</span><span class="ms-lbl">Roof Coverage Area</span></div>
    </div>
    <div class="meas-grid">
{meas_html}    </div>{estimation_banner}
  </div>
</section>
{defects_section}
<!-- FACILITY PHOTOS -->
<section class="section section-alt">
  <div class="container">
    <div class="section-label">Facility Description</div>
    <h2 class="section-title">Facility Photographs</h2>
    <p class="section-intro">On-site and aerial photographic documentation of Structure {label} — {name}.</p>
    <div class="facility-gallery">
      <div class="fg-main">
{pics_html}      </div>
      <div class="fg-thumbs">
{pic_thumbs}      </div>
    </div>
  </div>
</section>

<!-- PREV / NEXT -->
<div class="struct-nav-bar">
  <div class="container">
    {prev_btn}
    <a href="structures.html" class="struct-nav-all">All Structures</a>
    {next_btn}
  </div>
</div>

{footer()}
{html_foot()}"""

# ─── Generate All Files ───────────────────────────────────────────────────────

def write(filename, content):
    path = os.path.join(BASE, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  OK  {filename}")

if __name__ == "__main__":
    print("Generating FAMAD PLC site pages...")

    write("index.html",        gen_index())
    write("overview.html",     gen_overview())
    write("environment.html",  gen_environment())
    write("calculations.html", gen_calculations())
    write("structures.html",   gen_structures())

    for i, s in enumerate(STRUCTURES):
        prev_s = STRUCTURES[i - 1] if i > 0 else None
        next_s = STRUCTURES[i + 1] if i < len(STRUCTURES) - 1 else None
        write(struct_filename(s["label"]), gen_structure(s, prev_s, next_s))

    print(f"\nDone — {5 + len(STRUCTURES)} pages generated.")
