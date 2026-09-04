# -*- coding: utf-8 -*-
"""Generate the static Nikolaus Teply Restorations site."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent

SERVICE_LINKS = [
    ("Antique Restoration", "/services/antique-restoration/"),
    ("Antique Repairs", "/services/antique-repairs/"),
    ("Antique Furniture Restoration", "/services/antique-furniture-restoration/"),
    ("Restoring / Refinishing Old Wood Furniture", "/services/refinishing-old-wood-furniture/"),
    ("Veneer Furniture Restoration", "/services/veneer-furniture-restoration/"),
    ("French Polishing", "/services/french-polishing/"),
    ("Custom Wood Turning and Carving", "/services/woodturning/"),
    ("Furniture Colour Matching", "/services/furniture-colour-matching/"),
    ("Overview of all services", "/services/"),
]

WHAT_WE_DO = [
    ("French Polishing", "/services/french-polishing/"),
    ("Stripping and finishing with hand applied finishes", "/services/refinishing-old-wood-furniture/"),
    ("Reproducing antique finishes", "/services/antique-furniture-restoration/"),
    ("Colour matching", "/services/furniture-colour-matching/"),
    ("All manner of repairs", "/services/antique-repairs/"),
    ("Modern, hand applied finishes", "/services/french-polishing/"),
    ("All structural repairs", "/services/antique-restoration/"),
    ("Veneer work", "/services/veneer-furniture-restoration/"),
    ("Hand stripping", "/services/refinishing-old-wood-furniture/"),
    ("Turning", "/services/woodturning/"),
    ("Furniture related metalwork", "/services/"),
    ("On site work", "/contact/"),
]


def head(title, desc):
    return f"""<!DOCTYPE html>
<html lang="en-AU">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <link rel="icon" href="/favicon.ico" sizes="any">
  <link rel="icon" type="image/png" href="/favicon.png" sizes="256x256">
  <link rel="apple-touch-icon" href="/apple-touch-icon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500&family=Source+Sans+3:ital,wght@0,400;0,500;0,600;1,400&display=swap" rel="stylesheet">
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      theme: {{
        extend: {{
          colors: {{
            walnut: "#3B2A1F",
            brass: "#B08D57",
            ivory: "#F6F1E8",
            parchment: "#EDE6D9",
            ink: "#1C1612"
          }},
          fontFamily: {{
            serif: ['"Cormorant Garamond"', "Georgia", "serif"],
            sans: ['"Source Sans 3"', "system-ui", "sans-serif"]
          }}
        }}
      }}
    }}
  </script>
  <link rel="stylesheet" href="/css/site.css">
</head>
<body class="bg-ivory text-ink antialiased">
<a class="skip-link" href="#main">Skip to content</a>
"""


def header(active):
    def nav_cls(key):
        return "nav-link is-active" if active == key else "nav-link"

    items = "".join(
        f'<a href="{href}">{label}</a>\n'
        for label, href in SERVICE_LINKS
    )
    return f"""
<header class="site-header">
  <div class="mx-auto flex h-full max-w-6xl items-center justify-between gap-6 px-5">
    <a href="/" class="flex items-center shrink-0" aria-label="Nikolaus Teply Restorations home">
      <img src="/public/images/logo.png" alt="nikolaus teply logo" width="350" height="90" class="h-11 w-auto md:h-12">
    </a>
    <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="site-nav" aria-label="Open menu"><span></span></button>
    <nav id="site-nav" class="nav-wrap flex items-center gap-6" aria-label="Primary">
      <a class="{nav_cls("home")}" href="/">Home</a>
      <div class="dropdown" data-dropdown>
        <button class="{nav_cls("services")}" type="button" aria-expanded="false" aria-haspopup="true" aria-controls="services-menu">Services</button>
        <div id="services-menu" class="dropdown-panel" role="menu">{items}</div>
      </div>
      <a class="{nav_cls("gallery")}" href="/gallery/">Gallery</a>
      <a class="{nav_cls("about")}" href="/about/">About</a>
      <a class="{nav_cls("testimonials")}" href="/testimonials/">Testimonials</a>
      <a class="{nav_cls("contact")}" href="/contact/">Contact</a>
      <a class="nav-link shrink-0" href="tel:0425217269">0425 217 269</a>
    </nav>
  </div>
</header>
"""


def footer():
    svc = "".join(
        f'<li><a href="{href}">{label}</a></li>'
        for label, href in SERVICE_LINKS
        if label != "Overview of all services"
    )
    return f"""
<footer class="site-footer mt-0">
  <div class="mx-auto grid max-w-6xl gap-10 px-5 py-16 md:grid-cols-3">
    <div>
      <p class="serif text-2xl text-ivory">Nikolaus Teply</p>
      <p class="mt-3 max-w-xs text-sm leading-relaxed">European-trained restorer · Marrickville, Sydney</p>
      <p class="mt-4 text-sm">Restoration and conservation of antique furniture and objects of art.</p>
    </div>
    <div>
      <p class="eyebrow">Workshop</p>
      <p class="mt-3 text-sm leading-relaxed">
        Suite A1, Building A<br>
        10 Carrington Road<br>
        Marrickville NSW 2204
      </p>
      <p class="mt-3 text-sm"><a href="tel:0425217269">0425 217 269</a><br>
      <a href="mailto:nikteply@gmail.com">nikteply@gmail.com</a></p>
    </div>
    <div>
      <p class="eyebrow">Services</p>
      <ul class="mt-3 space-y-1 text-sm">{svc}</ul>
    </div>
  </div>
  <div class="border-t border-brass/30 px-5 py-5 text-center text-xs tracking-wide">
    Copyright Nikolaus Teply. All rights reserved. 2026
  </div>
</footer>
<script src="/js/site.js" defer></script>
</body>
</html>
"""


def consult_band():
    return """
<section class="bg-walnut text-ivory">
  <div class="mx-auto flex max-w-6xl flex-col items-start justify-between gap-6 px-5 py-16 md:flex-row md:items-center">
    <div>
      <p class="eyebrow">Consultation</p>
      <h2 class="serif mt-2 text-3xl md:text-4xl">Bring the piece. We will talk through the work.</h2>
      <p class="mt-3 max-w-xl text-parchment">Estimates can be given from photographs. A detailed quote is always provided before work commences.</p>
    </div>
    <div class="flex flex-wrap gap-3">
      <a class="btn btn-primary" href="/contact/">Request a consultation</a>
      <a class="btn btn-secondary" href="tel:0425217269">Call 0425 217 269</a>
    </div>
  </div>
</section>
"""


def page_hero(title, image, alt, kicker=""):
    kicker_html = f'<p class="eyebrow">{kicker}</p>' if kicker else ""
    return f"""
<section class="page-hero flex items-end">
  <img src="{image}" alt="{alt}" width="1180" height="550">
  <div class="veil"></div>
  <div class="relative z-10 mx-auto w-full max-w-6xl px-5 py-12">
    {kicker_html}
    <h1 class="serif mt-3 max-w-3xl text-4xl text-ivory md:text-5xl">{title}</h1>
  </div>
</section>
"""


def write(rel, html):
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html, encoding="utf-8")
    print("wrote", rel)


def wrap(title, desc, active, body):
    return head(title, desc) + header(active) + f'<main id="main">{body}</main>' + footer()


# ---------------------------------------------------------------------------
# HOME
# ---------------------------------------------------------------------------
HOME = wrap(
    "Art &amp; Furniture Restoration Sydney | Nikolaus Teply",
    "Sydney’s master furniture restorer specialising in antique furniture restoration and French polishing using traditional European techniques.",
    "home",
    f"""
<section class="hero">
  <img src="/public/images/new-slide1-opt.webp" alt="antique furniture restorers in Sydney" width="1180" height="550" fetchpriority="high">
  <div class="hero-veil"></div>
  <div class="relative z-10 mx-auto w-full max-w-6xl px-5 pb-16 pt-32">
    <p class="eyebrow text-brass">Marrickville · Sydney</p>
    <h1 class="serif mt-4 max-w-3xl text-5xl leading-tight text-ivory md:text-7xl">Furniture Restorer Sydney</h1>
    <p class="mt-5 max-w-2xl text-lg text-parchment">At Nikolaus Teply Restorations, we are Sydney’s master furniture restorer, dedicated to preserving and revitalising antique pieces with exceptional craftsmanship. We combine respect for historical authenticity with skilled handwork, ensuring your cherished furniture retains both its heritage and its value. As a professional furniture restorer Sydney clients depend on, we use time-honoured European techniques passed down through generations of artisans.</p>
    <div class="mt-8 flex flex-wrap gap-3">
      <a class="btn btn-primary" href="/contact/">Request a consultation</a>
      <a class="btn btn-secondary" href="/gallery/">View the gallery</a>
    </div>
  </div>
</section>

<section class="strip" aria-label="What we do">
  <div class="mx-auto max-w-6xl px-5 py-6">
    <p class="eyebrow mb-4">What we do</p>
    <div class="flex flex-wrap gap-x-6 gap-y-2">
      {"".join(f'<a href="{h}">{t}</a>' for t, h in WHAT_WE_DO)}
    </div>
  </div>
</section>

<section class="mx-auto max-w-6xl px-5 py-20">
  <div class="grid items-start gap-12 lg:grid-cols-2">
    <div>
      <p class="eyebrow">The workshop</p>
      <h2 class="serif mt-3 text-4xl md:text-5xl">Sydney’s Premier Antique And Furniture Restoration Specialists</h2>
      <hr class="rule mt-6 max-w-xs">
      <p class="mt-6 prose-measure">Entrusting valuable antiques to us means choosing a team committed to superior results. Our antique restorer Sydney services focus on maintaining the beauty and original design of each piece. We recognise that antique furniture carries stories and heritage, and through careful restoration and conservation, we preserve those narratives for future generations.</p>
    </div>
    <figure class="letterbox aspect-[718/322]">
      <img src="/public/images/homeimg-opt.webp" alt="antique furniture restorers" width="718" height="322" loading="lazy">
    </figure>
  </div>
</section>

<section class="bg-parchment/60">
  <div class="mx-auto max-w-6xl px-5 py-20">
    <h3 class="serif text-3xl">Preserving Historical And Financial Value</h3>
    <p class="mt-5 max-w-3xl">Each piece we restore begins with a careful assessment of its history and condition. Our objective as a furniture restoration specialist is not only to enhance appearance, but also to protect provenance and long term worth. Sentimental value matters, monetary value matters, and we balance both with measured care.</p>
  </div>
</section>

<section class="mx-auto max-w-6xl px-5 py-20">
  <p class="eyebrow">Services</p>
  <h2 class="serif mt-3 text-4xl md:text-5xl">Comprehensive Furniture And Art Restoration Services</h2>
  <p class="mt-5 max-w-3xl">We offer a wide range of tailored restoration and conservation services for antique furniture and related art forms. From domestic heirlooms to commercial heritage pieces, our work is precise, respectful, and focused on longevity.</p>
  <div class="mt-12 grid gap-10 md:grid-cols-3">
    <article>
      <h3 class="serif text-2xl">Antique Furniture Restoration And Conservation</h3>
      <p class="mt-3">Nikolaus Teply Restorations specialises in antique furniture restoration Sydney homeowners and businesses rely on. Whether repairing loose joints, restoring veneer, or revitalising original finishes, our methods respect the craftsmanship of the period. Conservation work stabilises fragile elements and secures the longevity of your furniture while preserving its authenticity.</p>
    </article>
    <article>
      <h3 class="serif text-2xl">French Polishing And Veneer Repair</h3>
      <p class="mt-3">As a leading french polisher Sydney service, we apply traditional shellac polishing techniques to restore the warm, lustrous finish of period furniture. Our veneer repairs address warping, peeling, or missing sections with precise, patient work. The result is a finish that sits comfortably with the original character of the piece.</p>
    </article>
    <article>
      <h3 class="serif text-2xl">Restoration Of Wooden Art, Mirrors, Frames, Sculptures, And Clocks</h3>
      <p class="mt-3">Beyond furniture, we are wood restoration specialists Sydney clients trust for art conservation. Whether a carved mirror frame, ornate clock casing, or wooden sculpture, our team restores fine details through hand finishing and delicate repairs, ensuring these items retain their original charm and structural soundness.</p>
    </article>
  </div>
</section>

<section class="bg-walnut text-ivory">
  <div class="mx-auto max-w-6xl px-5 py-20">
    <p class="eyebrow">Training</p>
    <h2 class="serif mt-3 text-4xl">Expertise Backed By European Training</h2>
    <p class="mt-5 max-w-3xl text-parchment">Our craft is rooted in traditional European methods. That training gives us the tools to recognise authentic materials, match historical finishes, and apply techniques that honour the original maker’s intent.</p>
    <div class="mt-12 grid gap-10 md:grid-cols-2">
      <div>
        <h3 class="serif text-2xl">Traditional Restoration Techniques</h3>
        <p class="mt-3 text-parchment">Our team’s skills come from European-trained craftsmanship. This background equips us to use time-proven approaches, careful joinery repair, and period-appropriate finishing methods. The result is restoration that feels honest and looks right.</p>
      </div>
      <div>
        <h3 class="serif text-2xl">Knowledge Of Authentic Materials And Finishes</h3>
        <p class="mt-3 text-parchment">A detailed understanding of woods, stains, waxes, and shellacs is essential. That knowledge lets us select materials that protect and complement your pieces, preserving their integrity and appearance over time.</p>
      </div>
    </div>
  </div>
</section>

<section class="mx-auto max-w-6xl px-5 py-20">
  <h2 class="serif text-4xl">Understanding Our Restoration And Conservation Process</h2>
  <p class="mt-5 max-w-3xl">We explain the differences between restoration and conservation so you can choose the best path for each item. Our recommendations reflect the piece’s age, condition, provenance, and your own wishes.</p>
  <div class="mt-12 grid gap-10 md:grid-cols-3">
    <article class="border border-brass/30 bg-parchment/40 p-6">
      <h3 class="serif text-2xl">What Is Restoration?</h3>
      <p class="mt-3">Restoration involves returning an item to a previous known state by repairing or replacing components where necessary. This can include fixing structural damage, refinishing surfaces, or reinstalling missing elements. Restoration is the right choice when the goal is to recover original function and appearance.</p>
    </article>
    <article class="border border-brass/30 bg-parchment/40 p-6">
      <h3 class="serif text-2xl">What Is Conservation?</h3>
      <p class="mt-3">Conservation focuses on stabilising the current condition of a piece to prevent further deterioration, while keeping interventions minimal and reversible. This approach suits highly valuable or fragile antiques that require careful handling and documentation.</p>
    </article>
    <article class="border border-brass/30 bg-parchment/40 p-6">
      <h3 class="serif text-2xl">Helping You Choose The Right Approach</h3>
      <p class="mt-3">We guide you through the decision, explaining risks, benefits, and likely outcomes. Our aim is clear advice, tailored to the item and to your priorities.</p>
    </article>
  </div>
</section>

<section class="bg-parchment/70">
  <div class="mx-auto max-w-6xl px-5 py-20">
    <h2 class="serif text-4xl">Trusted Furniture Restoration Specialist In Sydney</h2>
    <p class="mt-5 max-w-3xl">We take pride in our reputation, earned through careful work and satisfied clients. Respect for each piece, clear communication, and consistent results are central to how we operate.</p>
    <div class="mt-12 grid gap-8 lg:grid-cols-2">
      <div>
        <h3 class="serif text-2xl">Testimonials From Satisfied Clients</h3>
        <blockquote class="pullquote mt-6">Attached are some photos of the furniture in its “home” – looks wonderful! Thanks again for a great job, we are really enjoying these beautiful pieces again and we will recommend you to anyone we know looking for restoration work.</blockquote>
        <p class="mt-3 text-sm tracking-wide uppercase text-walnut">Susan</p>
        <blockquote class="pullquote mt-10">Hi Nick, we just wanted to say thanks for all of the restoration work you have done for us – dining table, chairs, chiffonier. The furniture now looks fantastic and we appreciate your dedication in bringing each piece ‘back to life’.</blockquote>
        <p class="mt-3 text-sm tracking-wide uppercase text-walnut">Wendy and Simon, Dulwich Hill</p>
        <p class="mt-6"><a class="nav-link" href="/testimonials/">Read all client reviews</a></p>
      </div>
      <div>
        <h3 class="serif text-2xl">Before And After Galleries</h3>
        <p class="mt-3 mb-5">Photos tell a story. Our galleries present striking restorations of antique furniture and artworks, showing the care and craft behind each project. Browse to see examples of repair, refinishing, and conservation.</p>
        <div class="ba" data-ba>
          <img src="/public/images/cambodian-jewellery-before.jpg" alt="antique restoration furniture" width="800" height="533" loading="lazy">
          <img class="ba-after" src="/public/images/cambodian-jewellery-after.jpg" alt="Cambodian jewellery cabinet after restoration" width="800" height="600" loading="lazy">
          <span class="ba-label before">Before</span>
          <span class="ba-label after">After</span>
          <div class="ba-handle"></div>
          <input class="ba-range" type="range" min="0" max="100" value="50" aria-label="Compare before and after">
        </div>
        <p class="mt-3 text-sm">Cambodian jewellery cabinet — before and after restoration.</p>
      </div>
    </div>
    <div class="mt-16">
      <h3 class="serif text-2xl">Proven Credentials And Industry Recognition</h3>
      <p class="mt-4 max-w-3xl">With years of experience and certification from respected European institutions, our credentials validate our expertise. We adhere to industry standards and continue professional development to keep skills sharp. Nick trained as a traditional cabinetmaker in Garmisch-Partenkirchen in the mid-1980s, completed three years at the Goering Institute in Munich, and has run his own Sydney workshop since 2002.</p>
    </div>
  </div>
</section>

<section class="mx-auto max-w-6xl px-5 py-20">
  <h2 class="serif text-4xl">Proudly Serving Sydney And Surrounding Areas</h2>
  <p class="mt-5 max-w-3xl">Nikolaus Teply Restorations proudly serves Sydney and nearby regions. Familiarity with local heritage styles helps us provide services suited to the city’s diverse history and design tastes. The workshop is in Marrickville, with pickup and delivery arranged by trusted removalists when needed.</p>
</section>

<section class="mx-auto max-w-6xl px-5 pb-20">
  <h2 class="serif text-4xl">Contact Us For Professional Antique Restorations</h2>
  <p class="mt-5 max-w-3xl">Restore your treasured antiques with Sydney’s trusted master furniture restorer. Visit our home page or contact us for a personalised consultation, and experience the Nikolaus Teply difference.</p>
  <div class="mt-8 flex flex-wrap gap-3">
    <a class="btn btn-primary" href="/contact/">Request a consultation</a>
    <a class="btn btn-secondary on-light" href="tel:0425217269">Call 0425 217 269</a>
  </div>
</section>
""",
)
write("index.html", HOME)

# ---------------------------------------------------------------------------
# SERVICES OVERVIEW
# ---------------------------------------------------------------------------
write(
    "services/index.html",
    wrap(
        "Services | Nikolaus Teply Restorations | Sydney",
        "We provide restoration, conservation, &amp; repair services to your antiques or wooden furniture &amp; restore it to its full glory. Enquire today!",
        "services",
        page_hero(
            "Professional Antique Restoration and Conservation Services",
            "/public/images/new-slide2-opt.webp",
            "antique restoration Sydney",
            "Comprehensive Restoration Services",
        )
        + """
<article class="mx-auto max-w-6xl px-5 py-16">
  <p class="max-w-3xl">Services provided across restoration, conservation, and related workshop work. All restoration and conservation work is carried out in accordance with internationally recognised guidelines.</p>
  <div class="mt-12 grid gap-8 md:grid-cols-3">
    <section class="border border-brass/30 p-6">
      <h2 class="serif text-2xl">Restoration</h2>
      <ul class="mt-4 list-disc space-y-2 pl-5">
        <li>Structural repairs to all kinds of furniture</li>
        <li>Veneer repairs and replacements, wooden or other materials</li>
        <li>Repair and replacement of related metal work</li>
        <li>Hand finishing (French Polish, Oil finishes, Wax finishes)</li>
        <li>Re-laying of baize and leathers</li>
        <li>Turning</li>
        <li>Re-caning</li>
        <li>Colour matching</li>
      </ul>
    </section>
    <section class="border border-brass/30 p-6">
      <h2 class="serif text-2xl">Conservation</h2>
      <ul class="mt-4 list-disc space-y-2 pl-5">
        <li>Preservation of original finishes and patina during cleaning and reviving processes</li>
        <li>Preservation of other surfaces like antique lacquer work (ex. Chinoiserie) and gilding</li>
        <li>Surface cleaning of non-wooden objects</li>
      </ul>
    </section>
    <section class="border border-brass/30 p-6">
      <h2 class="serif text-2xl">Other</h2>
      <ul class="mt-4 list-disc space-y-2 pl-5">
        <li>Repairs to contemporary furniture</li>
        <li>Advice on the care of your antique objects</li>
        <li>Full documentation in word and photography if required</li>
        <li>Complete refinishing of furniture or parts of them</li>
        <li>Pick-up and delivery by competent and trusted removalists</li>
        <li>Making of custom designed fine furniture</li>
        <li>On site work (colour work, reviving, watermark removal, cleaning, polishing, waxing)</li>
        <li>Upholstery</li>
      </ul>
    </section>
  </div>
  <p class="mt-12 max-w-3xl">An estimate of costs can be given from photos and a description of the work required. However, due to the complex nature of restoration/conservation work it is better if the piece can be viewed in person.</p>
  <p class="mt-4 max-w-3xl">A detailed quote will be given before any work commences.</p>
  <ul class="mt-12 grid gap-3 sm:grid-cols-2">
"""
        + "".join(
            f'<li><a class="block border border-brass/25 px-4 py-3 hover:bg-parchment" href="{h}">{t}</a></li>'
            for t, h in SERVICE_LINKS
            if t != "Overview of all services"
        )
        + """
  </ul>
</article>
"""
        + consult_band(),
    ),
)


def service(rel, title, desc, h1, image, alt, kicker, inner):
    write(
        rel,
        wrap(
            title,
            desc,
            "services",
            page_hero(h1, image, alt, kicker)
            + f'<article class="prose-measure mx-auto px-5 py-16">{inner}<p class="mt-12 flex flex-wrap gap-3"><a class="btn btn-primary" href="/contact/">Request a consultation</a><a class="btn btn-secondary on-light" href="tel:0425217269">Call 0425 217 269</a></p></article>'
            + consult_band(),
        ),
    )


service(
    "services/antique-restoration/index.html",
    "Antique Restoration | Sydney | Nikolaus Teply Restorations",
    "Experience the craftsmanship of antique furniture restoration. Choose professionals with the expertise and tools for preserving its artistry.",
    "Antique Restoration in Sydney",
    "/public/images/slide1.jpg",
    "Restored dining furniture",
    "Antique Restoration",
    """
<h2 class="serif text-3xl">Everything You Need to Know About Antique Restoration near Sydney</h2>
<p class="mt-5">Owning an antique piece of furniture can become a big responsibility when it comes to ensuring that it stays in perfect condition. You may find that from time to time your furniture may require restoration; this can be anything from professionally removing dirt and grime or more work such as repairs and partial or complete refinishing. Ensure that you use a professional company with experience in <a href="/gallery/">antique restoration near Sydney</a>. At Nikolaus Teply Restorations, we have been restoring furniture for many years. We have the required experience and knowledge to ensure that your antique pieces are restored to its original glory and will last for many more years.</p>
<h3 class="serif mt-12 text-2xl">Benefits of Antique Furniture Restoration</h3>
<p class="mt-4">When you own an antique table or other furniture that needs a little TLC, you should consider restoration an option. Conservers have studied the art of giving new life to old furniture and know the right techniques for things such as antique chair restoration. Here are some of the benefits you can enjoy when you choose to restore your current furniture:</p>
<ul class="mt-4 list-disc space-y-2 pl-5">
  <li><strong>Maintaining your furniture.</strong> Having your antique furniture restored can prolong its lifespan while keeping it in pristine condition. This is especially essential when there are loose joints, missing pieces or worn-out areas on the item.</li>
  <li><strong>Eco friendly.</strong> While it might not be cheaper to restore your furniture compared to buying new items, restoring your furniture is eco-friendly. Instead of cutting down more trees to manufacture new furniture, you can simply restore your current pieces and help conserve the planet.</li>
  <li><strong>Investment.</strong> Well-maintained antique furniture is considered an investment by many people. As the furniture ages, its value can increase. If you plan on passing these pieces down to your children or grandchildren, you’ll want to ensure that they’re in pristine condition.</li>
</ul>
<h3 class="serif mt-12 text-2xl">Common Mistakes People Make Regarding Wooden Furniture or Vintage Dresser Restoration</h3>
<p class="mt-4">Restoring antique furniture is an art and you should get someone with the necessary training to perform the task correctly. Tasks such as vintage dresser restoration can be quite tricky and you may end up damaging your furniture beyond repair. Here are some mistakes people often make and how you can avoid them:</p>
<ul class="mt-4 list-disc space-y-2 pl-5">
  <li><strong>Trying DIY.</strong> When it comes to restoring your furniture, many people believe they can do it themselves. Still, without the proper knowledge, tools, and experience, this may result in your furniture becoming damaged.</li>
  <li><strong>Going cheap.</strong> While we all want to save money wherever we can, you shouldn’t compromise the integrity of your furniture by using the cheapest restorer you can find.</li>
  <li><strong>Not reading reviews.</strong> Going online and reading the reviews about the different restorers in your area can assist you with deciding on which company you should use. You can also ask the company if you can see their previous work.</li>
</ul>
<h3 class="serif mt-12 text-2xl">Key Questions to Ask Us Regarding the Conservation of Furniture</h3>
<p class="mt-4">If you’ve never had your furniture restored, you can research the topic, or you can simply visit us, and we will answer all your questions before restoring your item. Here are some questions you should remember to ask:</p>
<ul class="mt-4 list-disc space-y-2 pl-5">
  <li><strong>Is my piece of furniture worth restoring?</strong> Although you may love a particular piece of your wooden furniture, it may cost more to fix it than replace it. But, apart from the financial value you should also consider the sentimental value. Ask your restorer if you should repair or replace the piece.</li>
  <li><strong>Can you customise the item?</strong> Sometimes people want to modify or completely change some aspects of their furniture; you can find out if it’s possible to do so.</li>
</ul>
<h3 class="serif mt-12 text-2xl">What You Should Know About the Restoration of Furniture</h3>
<ul class="mt-4 list-disc space-y-2 pl-5">
  <li><strong>It takes time.</strong> While your restorer will give you an estimated date of when your furniture will be ready, you need to be flexible as it may take longer than expected.</li>
  <li><strong>Be realistic about your expectations.</strong> You may have a picture in your mind of what your furniture will look like once restored, although you need to remember that sometimes it may not be possible to have it done exactly as you want it.</li>
  <li><strong>Not all furniture can be restored.</strong> Although you may have your heart set on having a particular piece of furniture repaired or restored, in very rare cases it may not be possible to do so.</li>
</ul>
<h3 class="serif mt-12 text-2xl">Why Trust Nikolaus Teply Restorations Regarding Antique Restoration of Furniture</h3>
<p class="mt-4">With more than two decades in the <a href="/about/">vintage furniture restoration</a> industry, we have established our name as one of the leading restorers in Sydney. German native Nick Teply discovered his love for craftsmanship during his training as a traditional cabinetmaker. After completing three years of studying restoration and conservation of wooden furniture, he became a fully accredited furniture restorer and conserver. All repairs and restorations are done on site and thoroughly checked to present you with a piece of furniture you can proudly display in your home. Nick uses modern and traditional techniques in his restoration and conversation process. While his primary focus is that of antique furniture, he offers his customers the opportunity to design their fine furniture, which he then makes. Before we work on your furniture, we will give you a detailed quote so you can decide if you want to go ahead with the restoration.</p>
<p class="mt-4">For more information about the services you can expect from Nikolaus Teply Restorations, <a href="/contact/">contact us</a> now.</p>
""",
)

service(
    "services/antique-repairs/index.html",
    "Antique Repairs | Sydney | Nikolaus Teply Restorations",
    "For antique furniture restorers in Sydney, look no further than Nikolaus Teply Restorations. For all enquiries, give us a call today.",
    "Antique Repairs Sydney",
    "/public/images/gallery-1.jpg",
    "Restored antique furniture",
    "Antique Repairs",
    """
<h2 class="serif text-3xl">Background to Antique Repairs in Sydney</h2>
<p class="mt-5">Our business to offer <a href="/about/">antique repairs in Sydney</a> started with Nick Teply’s creative journey across Germany. Coming from Bavaria, Germany, Nick underwent extensive training as a traditional cabinetmaker in the 1980s, after which he decided to pursue his passion for restoration and conservation. Nick went on to study full time at the Goering Institute of Restoration and Conservation of Wooden Objects in Munich for three years before moving to Australia in 1996.</p>
<h3 class="serif mt-12 text-2xl">What Sets Us Apart Regarding Furniture Repair Around Sydney</h3>
<p class="mt-4">We believe the restoration and conservation of all antique furniture is vital to their longevity. Maintaining your antique furniture will ensure it stays in good condition for collections and resale purposes.</p>
<ul class="mt-4 list-disc space-y-2 pl-5">
  <li>We offer structural repairs, veneer repairs and replacements of all kinds of materials on antique furniture. This includes wood, metal, and other materials.</li>
  <li>We ensure exact colour matching when restoring your vintage furniture, along with doing the finer hand finishing touches. We include wax, oil, and French Polish finishes to furniture that require it.</li>
  <li>Depending on the condition, leather and other materials can undergo restoration or replacement.</li>
</ul>
<h3 class="serif mt-12 text-2xl">The Importance Of Furniture Restoration Near Sydney</h3>
<p class="mt-4">With our extensive knowledge about the restoration and conservation of furniture and objects, we aim to ensure all vintage furniture gets the right treatment for it to last longer.</p>
<ul class="mt-4 list-disc space-y-2 pl-5">
  <li>We aim to preserve the original finishes of the items. We further focus on preserving the finer details and patina while cleaning and improving furniture.</li>
  <li>We take antique lacquer work (such as Chinoiserie) and gilding into consideration when working on any antique furniture with those features.</li>
  <li>We carry out proper surface cleaning on all non-wooden objects during the repair process.</li>
</ul>
<p class="mt-4">Along with our basic services, we can provide written and photographic documentation of the work we carry out; we offer to restore contemporary furniture, and we offer advice on how to care for your antique furniture correctly.</p>
<h3 class="serif mt-12 text-2xl">What You Stand To Gain When You Use Nikolaus Teply Restorations</h3>
<p class="mt-4">At Nikolaus Teply Restorations, we believe that every piece of furniture is a work of art with its own story to tell. We aim to preserve the unique history of all furniture and objects that we receive. We offer to pick up and deliver your furniture to ensure convenience. We do on-site restorations and upholstery repairs and replacements. Nikolaus Teply Restorations offers you the opportunity to design and create fine custom furniture. We take pride in our services and aim to become one of the best furniture restorers in Sydney.</p>
<p class="mt-4">Since 2002, Nick Teply has worked on restoring wooden furniture and objects, including mirrors, sculptures and clocks, and always includes the element of conservation in the restoration process.</p>
<p class="mt-4">We can give you an estimate after we have received images and description of the furniture; however, we prefer to see the item before giving a formal quotation. You will receive a detailed quote of all costs before we start working on your furniture.</p>
<p class="mt-4">For any further queries or details, you can contact us <a href="/contact/">online</a> or visit us in store.</p>
""",
)

service(
    "services/antique-furniture-restoration/index.html",
    "Antique Furniture Restoration | Nikolaus Teply Restorations",
    "We provide antique furniture restoration Sydney-wide and are ready to restore and conserve your furniture with the greatest care. Discover more now.",
    "Antique Furniture Restoration Sydney",
    "/public/images/new-slide3-opt.webp",
    "antique furniture restoration Sydney",
    "Antique Furniture Restoration",
    """
<h2 class="serif text-3xl">The Most Reliable Antique Furniture Restoration Sydney-Wide at Your Service</h2>
<p class="mt-5">At Nikolaus Teply Restorations, we understand that we are working with pieces of furniture that are between some decades to several centuries old. These items are handcrafted from materials with characteristics so unique to each piece that they are almost impossible to duplicate. We understand some of these pieces are passed on through families and have lived entire lives of their own. That chair, that stool, and that table each tell their own stories, and that is why we understand how important it is to restore and conserve these precious sentimental pieces.</p>
<p class="mt-4">We offer antique furniture restoration around Sydney, ensuring that no matter your location, we can reach out and restore the memories attached to your, for example, great-grandmother’s ball and claw dining room set and allow it to see the next century.</p>
<h2 class="serif mt-12 text-3xl">The Importance of Antique Furniture Repairs</h2>
<p class="mt-4">Antique furniture restorers are a dying breed. With their skilled hands these artisans keep history alive in our houses. We need to sit back and reflect on the value of these antiques before turning to sell them online.</p>
<ul class="mt-4 list-disc space-y-2 pl-5">
  <li>Antique restorers work hard to restore your heirloom so that it retains its value. So many items today are manufactured from modern materials and have a limited life span compared to antique furniture</li>
  <li>It is by far more eco-friendly to restore your beautiful old pieces than purchasing new furniture if you can simultaneously reduce your carbon footprint and support a good cause.</li>
</ul>
<h2 class="serif mt-12 text-3xl">What You Can Expect From Nikolaus Teply Restorations</h2>
<p class="mt-4">We enjoy restoring your antique furniture and we look forward to share with you what we know, providing you with only the best service.</p>
<ul class="mt-4 list-disc space-y-2 pl-5">
  <li>We use a combination of both traditional and modern techniques in our restoration and conservation processes</li>
  <li>These processes include French polishing, reproducing antique finishes, colour matching, veneer work and structural repairs. Please contact us for any more specific restoration and conservation processes.</li>
  <li>Other services we offer are repairs to contemporary furniture and advice on caring for your antique furniture. We can provide you with complete documentation and photography and assist with upholstery to add that final touch.</li>
</ul>
<h2 class="serif mt-12 text-3xl">About Nikolaus Teply Restorations</h2>
<p class="mt-4">Nick Teply, a second-generation cabinetmaker, moved to Australia in 1996. He completed a traditional apprenticeship in Germany and three years of dedicated study at the Goering Institute of Restoration and Conservation of Wooden Objects in Munich. In 2002 he opened his workshop in Sydney, where he continues to follow his passion of restoring and conserving furniture.</p>
<p class="mt-4">Should you have any questions, please do not hesitate to <a href="/contact/">contact us</a>.</p>
""",
)

service(
    "services/refinishing-old-wood-furniture/index.html",
    "Wooden Furniture Restoration &amp; Refinishing | Nikolaus Teply",
    "We get great joy from refinishing and refurbishing old wood furniture. Let us give your antique piece of furniture new life. Contact us today!",
    "Restoring Old Furniture",
    "/public/images/homeimg.png",
    "antique furniture restorers",
    "Refinishing",
    """
<h2 class="serif text-3xl">We Love Refinishing Old Wood Furniture</h2>
<p class="mt-5">The art of <a href="/services/">refinishing old wood furniture</a> and other wooden antiques is something we have a passion for as we restore and conserve antique furniture. If you want us to refurbish a piece, it will be restored to its original condition or as close to it as possible, so it keeps the old style and look. Conservation is where we preserve the object in its current form and prevent further damage or deterioration. Clients may prefer conservation as it keeps the integrity of the original piece intact.</p>
<h3 class="serif mt-12 text-2xl">What You Can Expect From Us Regarding Restoring Old Wood Furniture</h3>
<p class="mt-4">To restore a piece of wooden furniture, we will first have to analyse the style and products used on the wood, and we can then move forward from there. Here is what a typical restoration entails:</p>
<ul class="mt-4 list-disc space-y-2 pl-5">
  <li>If you prefer to simply give your piece a new look, we can use the <a href="/services/french-polishing/">French Polishing technique</a> to provide it with a glossy surface. Finally, we hand-apply shellac to protect the wood and to give it a shiny look.</li>
  <li>We take our time to precisely determine what techniques were used on your furniture to accurately <a href="/services/antique-furniture-restoration/">recreate antique finishes</a> and give it a more modern look and feel if you want it to fit in with your current style.</li>
  <li>Every piece we get to repair, we treat with the respect that it deserves. Having seen many centuries, perhaps, it needs to be treated with care, which is why we apply, turn and colour match by hand, so no harsh machinery touches the wood.</li>
</ul>
<p class="mt-4">Owning an antique piece of furniture is a gift and an honour, and we will do all we can to refurbish your old wood furniture so you can enjoy it and it can match the rest of your house as far as possible, for as long as possible.</p>
<h3 class="serif mt-12 text-2xl">Tips Regarding Choosing Furniture Restorers</h3>
<p class="mt-4">Depending on the type of wood and style of the antique furniture, more complicated repairs may be necessary, but we will discuss timeframes and cost beforehand. After we have inspected the piece, we’ll know how much work will go into restoring old furniture. When you choose a furniture refurbisher, it is essential to look out for a few things:</p>
<ul class="mt-4 list-disc space-y-2 pl-5">
  <li>What are their services? You can’t just take an antique to any furniture refurbisher and expect they will know how to treat an antique and the processes and the techniques involved to keep its style and integrity intact. So, make sure you choose an accredited antique refurbisher.</li>
  <li>What tools do they use? For example, do they only use machinery to get the job done quickly instead of attention to detail that only hand care can bring to a piece?</li>
  <li>Part of repair or refurbishing is also to stay in contact with the client. And to be sure at all times that you deliver on what the customer asked for, be it watermark removal, colour matching, waxing or polishing.</li>
</ul>
<p class="mt-4">Ultimately, you entrust us with your special piece of furniture that is not just an antique but may be an heirloom that has sentimental value to you, and you need it to be cared for while out of your sight. We understand the value, and we find joy in restoring or conserving a piece to look old but new again.</p>
<h3 class="serif mt-12 text-2xl">About Nikolaus Teply Restorations</h3>
<p class="mt-4">Nick Teply has a passion for cabinetmaking that spilled over into the restoring of antique pieces. He is accredited by the Goering Institute of Restoration and Conservation of Wooden Objects in Munich as a state-accredited furniture restorer and conserver. <a href="/contact/">Contact us</a> to discuss the work needed on your refurbished antique furniture.</p>
""",
)

service(
    "services/veneer-furniture-restoration/index.html",
    "Restoring Veneer Furniture | Nikolaus Teply Restorations",
    "Trust Nikolaus Teply for professional veneer furniture restoration. Renew the elegance of your furniture and bring new life to your home. Get in touch now!",
    "Veneer Furniture Restoration",
    "/public/images/gallery-3.jpg",
    "Restored antique furniture",
    "Veneer",
    """
<p>Is your beloved timber veneer furniture showing signs of wear and tear, or has it lost its former lustre? At Nikolaus Teply Restorations, we specialise in veneer furniture restoration, helping you breathe new life into your timber veneer furniture.</p>
<h2 class="serif mt-12 text-3xl">Your Local Furniture Restoration Specialist</h2>
<p class="mt-4">Veneering timber furniture is one of the world’s oldest woodworking techniques, dating back almost 4,000 years, and it still remains popular today. This is because timber veneer furniture offers the aesthetic appeal of solid wood while being more environmentally friendly and cost-effective.</p>
<p class="mt-4">With its unique charm and timeless beauty, timber veneer furniture can add a touch of warmth and character to any space. However, over time, these pieces can show signs of wear and tear, losing their lustre and appeal. That is where Nikolaus Teply Restorations comes in. Here, we understand the value of quality furniture, especially when it comes to cherished timber veneer pieces, and take great care in carefully restoring these pieces back to their former glory.</p>
<p class="mt-4">Restoring your veneer furniture is not only a more sustainable and cost-effective alternative to buying new, but it also helps to nurture and restore the existing character of the piece. This is essential because timber veneer furniture has a unique charm and beauty that is increasingly hard to replicate with modern alternatives.</p>
<h2 class="serif mt-12 text-3xl">How We Can Help</h2>
<p class="mt-4">As time weathers the surfaces of your timber veneer furniture, it’s not uncommon to notice signs of wear and tear. Blisters, loose veneers, cracks, wobbly legs, and other imperfections can mar the timeless beauty of these pieces. Fortunately, at Nikolaus Teply Restorations, we specialise in addressing the following to help you get your beloved furniture back to looking and functioning at its best:</p>
<ul class="mt-4 list-disc space-y-2 pl-5">
  <li>Blisters or bubbles</li>
  <li>Cracks</li>
  <li>Chipped or broken veneers</li>
  <li>Stains and discolouration</li>
  <li>Scratches and dents</li>
  <li>Broken hardware (handles etc)</li>
  <li>Structural issues (broken or wobbly legs, etc)</li>
</ul>
<h2 class="serif mt-12 text-3xl">Give Your Furniture A Second Life</h2>
<p class="mt-4">Discover the power of veneer furniture restoration with Nikolaus Teply Restorations and get your timber veneer piece looking as good as new. With a passion for preserving the beauty and integrity of veneer furniture, we provide a comprehensive range of restoration services designed to bring your furniture back to its former glory.</p>
<p class="mt-4">Our skilled craftsmen have a passion for preserving the beauty and integrity of timber veneer furniture. We offer a comprehensive range of restoration services to revive your furniture, including:</p>
<ul class="mt-4 list-disc space-y-2 pl-5">
  <li>Surface refinishing</li>
  <li>Veneer repair</li>
  <li>Staining and colour-matching</li>
  <li>Hardware repairs</li>
  <li>Structural repairs</li>
  <li>Full veneer furniture restoration</li>
</ul>
<p class="mt-4"><a href="/contact/">Contact us</a> today to learn about how we can help you get your timber veneer furniture back looking and functioning at its best!</p>
""",
)

service(
    "services/french-polishing/index.html",
    "French Polishing | Sydney | Nikolaus Teply Restorations",
    "Discover the art of french polishing furnitures with Nikolaus Teply. Let us bring out the natural beauty of your furniture. Contact us for expert service!",
    "French Polishing | Sydney &amp; Surrounds",
    "/public/images/gallery-4.jpg",
    "Restored antique furniture",
    "French Polishing",
    """
<p>Breathe new life into your beloved antique furniture with professional French polishing services. Based in Sydney, Nikolaus Teply Restorations specialises in <a href="/services/antique-furniture-restoration/">restoring beautiful antique woodwork</a> to its former glory. With a dedication to the craft and great attention to detail, you can trust your furniture is in good hands with Nikolaus Teply Restorations.</p>
<h2 class="serif mt-12 text-3xl">What is French Polishing?</h2>
<p class="mt-4">French polishing is a traditional and highly refined wood furnishing technique used to create a high-gloss, mirror-like finish on wooden surfaces. It is known for its ability to enhance the natural beauty and grain of the wood while providing a lustrous and durable finish.</p>
<p class="mt-4">Dating back to the 17th century, French polishing has remained a popular choice for fine furniture, antique pieces, musical instruments, and architectural woodwork. This is because it not only protects the wood but also brings out its natural beauty, highlighting the grain patterns and unique characteristics of timber. Whether you’re looking to restore a vintage heirloom to its former glory or add the finishing touch to a handmade piece of woodwork, French polishing is the ideal solution.</p>
<h2 class="serif mt-12 text-3xl">Benefits of French Polishing</h2>
<p class="mt-4">French polishing is a traditional method of coating wooden furniture that has stood the test of time for centuries. This technique offers a range of benefits that continue to make it a preferred choice for restoring and enhancing the beauty of wooden surfaces. These benefits include, but are not limited to, the following:</p>
<ul class="mt-4 list-disc space-y-2 pl-5">
  <li><strong>Enhanced Visual Appearance –</strong> French polishing is renowned for its ability to create a glass-like mirror finish on wood surfaces. This shine and lustre gives woodwork an unparalleled level of elegance and sophistication.</li>
  <li><strong>Highlight Natural Beauty –</strong> Unlike some modern finishing methods, French polishing allows the unique features and grain patterns of the wood to shine through.</li>
  <li><strong>Environmentally Friendly –</strong> French polishing utilises shellac, a natural and environmentally friendly finish. This makes it an eco-friendly alternative to some modern finishes that may contain synthetic chemicals.</li>
  <li><strong>Timeless Appeal –</strong> French polishing offers a timeless and classic appeal that has the ability to complement a range of interior styles and transcend trends and fads.</li>
  <li><strong>Durable &amp; Long Lasting –</strong> A well-executed French polish provides a durable finish that forms a protective layer that guards the surface against minor scratches, moisture, and wear.</li>
  <li><strong>Repairability –</strong> Unlike other finishes, French polish repairs are relatively easy to perform. Cracks, scratches, or blemishes can be amended without stripping the entire piece of furniture.</li>
</ul>
<h2 class="serif mt-12 text-3xl">Why Opt for Professional French Polishing Services?</h2>
<p class="mt-4">French polishing furniture is a method of restoration that requires the touch of a professional with a strong understanding of the craft. This is because French polishing is a complex and time-consuming process that requires multiple steps to achieve the desired result. This includes meticulously applying multiple layers of shellac alongside careful sanding between layers to attain the perfect high-gloss finish.</p>
<p class="mt-4">The process demands both expertise and patience to ensure that every coat blends seamlessly, resulting in a flawless, mirror-like surface. This level of precision is best achieved by an experienced craftsman who has honed their craft through years of training and experience. Opting to go for professional French polishing services also ensures that the lifespan of your beloved antique piece is extended and continues to exude its thrive for years to come.</p>
<h2 class="serif mt-12 text-3xl">How We Can Help</h2>
<p class="mt-4">If you’re based in Sydney and are looking for expert French polishing services from a business you can trust, look no further than Nikolaus Teply Restorations. With years of experience restoring thousands of antique furniture and woodwork pieces, you can trust that your beloved antique pieces are in safe hands.</p>
<p class="mt-4">In addition to french polishing, we’re able to complete the following:</p>
<ul class="mt-4 list-disc space-y-2 pl-5">
  <li>Complete furniture restoration</li>
  <li>General maintenance and upkeep</li>
  <li>Colour matching</li>
  <li>Veneer repair</li>
  <li>Surface refinishing</li>
  <li>Structural repairs</li>
</ul>
<p class="mt-4">Regardless of if you’re looking to breathe new life into an antique piece or refurbish an old heirloom, you’ve come to the right place. <a href="/contact/">Contact us</a> today to see how we can help you revive your antique furniture.</p>
""",
)

service(
    "services/woodturning/index.html",
    "Wood Turning Furniture | Nikolaus Teply Restorations",
    "Witness the artistry of wood turning and carving furnitures by Nikolaus Teply. Bring unique wooden pieces into your life. Contact us today!",
    "Custom Wood Turning and Carving",
    "/public/images/gallery-5.jpg",
    "Restored antique furniture",
    "Woodturning",
    """
<p>An age-old craft, woodturning and wood carving play a huge role in the restoration and conservation of antique and heritage woodwork. At Nikolaus Teply Restorations, we are committed to using both woodturning and carving as a means of helping clients restore their beloved antique furniture. Be it reproducing components of a charming piece of antique furniture or crafting an entirely custom work, restoration is what we do, and woodturning is a large part of it.</p>
<h2 class="serif mt-12 text-3xl">What is Woodturning?</h2>
<p class="mt-4">Woodturning is a specialised woodworking technique that has been practised for centuries. The process revolves around mounting a piece of wood on a rotating spindle and then skillfully using cutting tools to carve and shape the wood into various functional and decorative items.</p>
<p class="mt-4">Woodturning furniture specifically combines craftsmanship with a keen eye for detail to make unique wooden pieces that showcase the natural beauty of the wooden grain. This wood carving technique enables the creation of a wide range of stunning wooden products, such as furniture legs, spindles, knobs, handles, and more.</p>
<h2 class="serif mt-12 text-3xl">Custom Pieces Made to Order</h2>
<p class="mt-4">As your local specialist in furniture revival and restoration, we are passionate about preserving and celebrating the unique charm and timeless character of your antique furniture. That is why we will work with you from the very beginning to understand your goals and preferences to ensure that every detail aligns with your vision. This way, we’re able to create entirely custom components and decorative features that restore the functionality and beauty of your beloved antique furniture.</p>
<h2 class="serif mt-12 text-3xl">Our Wood Turning Services</h2>
<p class="mt-4">Working with a range of woods and various hand tools and machinery, we aim to bring your vision to life with the utmost care and attention to detail. Leveraging traditional methods and advanced techniques, we offer bespoke services to cater to the unique needs of our customers. This way, each piece of work is created using only the best quality materials and the highest attention to detail to ensure optimal durability, functionality, and appearance. Explore our range of woodturning and carving options below:</p>
<ul class="mt-4 list-disc space-y-2 pl-5">
  <li>Banisters</li>
  <li>Furniture legs</li>
  <li>Staircase spindles</li>
  <li>Knobs &amp; handles</li>
  <li>Decorative features</li>
  <li>Custom pieces</li>
</ul>
<h2 class="serif mt-12 text-3xl">Helping restore worn pieces</h2>
<p class="mt-4">Whether you have an antique piece in need of restoration or a wooden heirloom longing for a fresh start, you’ve come to the right place. At Nikolaus Teply Restorations, we specialise in both wood carving and woodturning to breathe new life into your wooden furniture. With over 20 years of experience in <a href="/services/refinishing-old-wood-furniture/">restoring antique furniture</a>, you can trust us to give your worn-out furniture some love and restore it to its former glory.</p>
<p class="mt-4">Revive your old furniture with our wood carving and wood-turning services. <a href="/contact/">Contact us</a> today for more information or to discuss how we can help you restore your beloved antique pieces.</p>
""",
)

service(
    "services/furniture-colour-matching/index.html",
    "Furniture Colour Matching | Nikolaus Teply",
    "Expert furniture colour matching in Sydney for authentic, seamless finishes that preserve and restore the beauty of your antique furniture.",
    "Furniture Colour Matching",
    "/public/images/gallery-6.jpg",
    "Restored antique furniture",
    "Colour matching",
    """
<p>Achieving an authentic restoration takes more than fixing loose joints. It needs precise furniture colour matching, the kind that makes repairs vanish into the grain. When you are restoring an antique or a wooden art object, getting the colour and finish right keeps the piece looking natural, and it protects its history. Get it wrong, and the repair will shout, even if everything else is perfect.</p>
<h2 class="serif mt-12 text-3xl">What Is Furniture Colour Matching and Why It Matters</h2>
<p class="mt-4">Furniture colour matching is the careful work of studying an item’s original finish, then recreating the exact colour, texture and sheen. It is part science, part craft. A flawless match hides repairs so well you might forget a restoration ever happened. That matters for more than looks. It keeps character, helps preserve value, and respects the maker’s original work. Whether it is a small touch up or a full restoration, good colour matching makes the piece feel whole again.</p>
<h2 class="serif mt-12 text-3xl">Why Choose Nikolaus Teply Restorations for Your Furniture Colour Matching Needs</h2>
<p class="mt-4">At Nikolaus Teply Restorations we bring a blend of skills you do not see every day. Our team are European trained restorers, comfortable with traditional techniques such as French polishing, and with modern finishing methods too. The result is colour matching that looks right and lasts.</p>
<p class="mt-4">We know old finishes, from shellac layers to aged varnishes. We handle delicate veneers and timber inlays with care. Based in Marrickville, we offer a furniture colour matching service Sydney clients trust, whether you bring a single chair or a whole suite.</p>
<h3 class="serif mt-10 text-2xl">European-Trained Restorers with Deep Antique Expertise</h3>
<p class="mt-4">European training gives our team a solid background in historical styles and finishing techniques. That training helps us spot subtle clues in a piece, the little things that tell us how it was made and what it used to look like. Rare or delicate finishes do not scare us. They make us focus more, and that is where experience counts.</p>
<h3 class="serif mt-10 text-2xl">Integration of Traditional and Modern Techniques</h3>
<p class="mt-4">We use old school methods alongside modern tools. Traditional approaches keep the finish historically honest. Modern tools help us measure, test and repeat results accurately. Put the two together, and you get a match that respects the original look, and stands up to everyday use.</p>
<h2 class="serif mt-12 text-3xl">Our Furniture Colour Matching Process</h2>
<p class="mt-4">Our process is thorough, but not fussy. We work methodically, and we check our work at every stage.</p>
<h3 class="serif mt-10 text-2xl">Assessment and Identification of Original Finish</h3>
<p class="mt-4">First we examine your furniture, closely. We identify the timber, the original finish, and how the surface has aged. That examination guides the whole job. Sometimes the answer is obvious, sometimes it takes a bit of detective work. Either way, we treat each piece as unique.</p>
<h3 class="serif mt-10 text-2xl">Selection and Testing of Pigments and Finishes</h3>
<p class="mt-4">Next we mix pigments and choose finishes that will replicate the original colour and texture. We make test samples on similar timber, then compare and tweak until we have a convincing match. Think of it like mixing paint for a portrait, but with grain and sheen to consider.</p>
<h3 class="serif mt-10 text-2xl">Application and Quality Inspection</h3>
<p class="mt-4">Once the match is agreed, we apply the finish carefully, blending repairs into the existing surface. We sand and build up layers where needed, then inspect the result under different lights. Only when the finish reads right from every angle do we call the job done.</p>
<h2 class="serif mt-12 text-3xl">Benefits of Professional Furniture Colour Matching</h2>
<p class="mt-4">Hiring a professional for colour matching brings clear advantages. It saves stress, and it protects the piece you care about.</p>
<h3 class="serif mt-10 text-2xl">Restored Appearance and Seamless Finish</h3>
<p class="mt-4">Repairs and restored areas will blend in. The finish looks uniform and natural. In short, the work does not draw attention, which is exactly what you want.</p>
<h3 class="serif mt-10 text-2xl">Preservation of Value and Heritage Integrity</h3>
<p class="mt-4">Proper colour matching helps retain both the historical and market value of your furniture. It honours the original craftsmanship and keeps the story of the piece intact.</p>
<h3 class="serif mt-10 text-2xl">Durable and Long-Lasting Results</h3>
<p class="mt-4">We use finishes and techniques that last. The result resists fading and wear, so the match does not become obvious after a few months. A good restoration looks good for years.</p>
<h2 class="serif mt-12 text-3xl">Case Studies and Client Testimonials</h2>
<p class="mt-4">We have restored many Sydney antiques where colour matching made the difference. From delicate timber inlays to repaired veneers, our <a href="/gallery/">gallery</a> shows before and after photos that speak for themselves. Clients often tell us they cannot tell where the repair was done, which is the nicest compliment.</p>
<h2 class="serif mt-12 text-3xl">Contact Us for Your Furniture Colour Matching Service in Sydney</h2>
<p class="mt-4">If you have an antique or a wooden heirloom that needs expert colour matching, get in touch with Nikolaus Teply Restorations. Visit our Marrickville workshop, or we can arrange an onsite visit anywhere in Sydney. We will assess your piece, explain the options, and give you a clear quote.</p>
<p class="mt-4">Experience trusted, professional furniture colour matching Sydney depends on, preserving heritage and restoring beauty, piece by piece.</p>
""",
)

# ABOUT
write(
    "about/index.html",
    wrap(
        "About Us | Nikolaus Teply Restorations | Sydney",
        "Nick Teply is a second generation cabinetmaker with an expertise in restoring &amp; preserving fine wooden furniture &amp; antiques. Read more here.",
        "about",
        page_hero(
            "Discover Craftsmanship Behind Nikolaus Teply Restorations",
            "/public/images/new-slide1-2022.jpg",
            "Restored drop-leaf table",
            "Trusted Furniture Restoration Specialist",
        )
        + """
<article class="prose-measure mx-auto px-5 py-16">
  <p>A second generation cabinetmaker, Nick Teply, native to Bavaria in Germany, first developed an appreciation of quality craftsmanship and fine furniture during his training to become a traditional cabinetmaker in Garmisch-Partenkirchen (Germany) in the mid. 80’s.</p>
  <p>Following some years of employment as a cabinetmaker, he decided to pursue his interests in the restoration and conservation of fine furniture and wooden objects of art by completing three years of full time study at the state accredited <a href="http://www.restaurierung-goering.de">Goering Institute of Restoration and Conservation of Wooden Objects</a> in Munich to become a fully qualified, state accredited furniture restorer and conserver.</p>
  <p>Since moving to Australia in 1996 Nick has worked for some of the leading Antique dealers and Furniture Restorers in Sydney as well as managing the restoration, conservation and finishing workshop for <a href="http://www.originalfinish.com.au">Original Finish</a>.</p>
  <p>Nick opened his own workshop in St. Peters, Sydney in 2002 and has continued to lovingly restore a wide range of furniture. The workshop is now in Marrickville.</p>
  <p>Nick believes that a piece of furniture has a story to tell and that this unique history should be preserved during the restorative and conservative process.</p>
  <p class="mt-10 flex flex-wrap gap-3"><a class="btn btn-primary" href="/contact/">Request a consultation</a><a class="btn btn-secondary on-light" href="tel:0425217269">Call 0425 217 269</a></p>
</article>
"""
        + consult_band(),
    ),
)

GALLERY_ITEMS = [
    ("/public/images/gallery-1.jpg", "Restored antique furniture", "Project 1", False),
    ("/public/images/gallery-2.webp", "Restored antique furniture", "Project 2", False),
    ("/public/images/gallery-3.jpg", "Restored antique furniture", "Project 3", False),
    ("/public/images/gallery-4.jpg", "Restored antique furniture", "Project 4", False),
    ("/public/images/gallery-5.jpg", "Restored antique furniture", "Project 5", False),
    ("/public/images/gallery-6.jpg", "Restored antique furniture", "Project 6", False),
    ("/public/images/cambodian-jewellery-before.jpg", "antique restoration furniture", "Cambodian jewellery cabinet — Before", True),
    ("/public/images/cambodian-jewellery-after.jpg", "Cambodian jewellery cabinet after restoration", "Cambodian jewellery cabinet — After", True),
    ("/public/images/new-slide1-opt.webp", "antique furniture restorers in Sydney", "Dining suite", False),
    ("/public/images/new-slide2-opt.webp", "antique restoration Sydney", "Interior with restored furniture", False),
    ("/public/images/new-slide3-opt.webp", "antique furniture restoration Sydney", "Cabinet and chairs", False),
    ("/public/images/slide1.jpg", "Restored dining furniture", "Dining furniture", False),
    ("/public/images/slide3.jpg", "Restored cabinet and chairs", "Cabinet and chairs", False),
    ("/public/images/homeimg-opt.webp", "antique furniture restorers", "Workshop pieces", False),
    ("/public/images/new-slide1-2022.jpg", "Restored drop-leaf table", "Drop-leaf table", False),
]

gallery_html = []
for src, alt, cap, grouped in GALLERY_ITEMS:
    badge = ' <span class="text-brass">Before / After</span>' if grouped else ""
    gallery_html.append(
        f'<a href="{src}" data-lightbox data-alt="{alt}" data-caption="{cap}">'
        f'<img src="{src}" alt="{alt}" loading="lazy">'
        f'<span class="cap">{cap}{badge}</span></a>'
    )

write(
    "gallery/index.html",
    wrap(
        "Restoration Gallery | Nikolaus Teply Restorations",
        "Explore our gallery of beautifully restored antique furniture. See our craftsmanship and contact us for your own restoration project today.",
        "gallery",
        page_hero(
            "Explore Our Stunning Antique Furniture Restorations",
            "/public/images/new-slide3-opt.webp",
            "antique furniture restoration Sydney",
            "Our Restored Antique Treasures",
        )
        + f"""
<section class="mx-auto max-w-6xl px-5 py-16">
  <p class="max-w-2xl">Workshop photographs from completed restorations, including the original slider images and the Cambodian jewellery cabinet before and after. Click any picture for a larger view.</p>
  <div class="mt-10 max-w-3xl">
    <div class="ba" data-ba>
      <img src="/public/images/cambodian-jewellery-before.jpg" alt="antique restoration furniture" width="800" height="533">
      <img class="ba-after" src="/public/images/cambodian-jewellery-after.jpg" alt="Cambodian jewellery cabinet after restoration" width="800" height="600">
      <span class="ba-label before">Before</span>
      <span class="ba-label after">After</span>
      <div class="ba-handle"></div>
      <input class="ba-range" type="range" min="0" max="100" value="50" aria-label="Compare before and after">
    </div>
    <p class="mt-3 text-sm">Cambodian jewellery cabinet, grouped as a before and after pair.</p>
  </div>
  <div class="gallery-grid mt-12">
    {''.join(gallery_html)}
  </div>
</section>
"""
        + consult_band(),
    ),
)

write(
    "testimonials/index.html",
    wrap(
        "Client Reviews | Nikolaus Teply Restorations",
        "Read client testimonials on our antique restoration services. Discover how we bring furniture back to life. Contact us for your restoration today.",
        "testimonials",
        page_hero(
            "Hear What Our Clients Say About Their Restoration Experience",
            "/public/images/gallery-2.webp",
            "Restored antique furniture",
            "What Our Clients Say",
        )
        + """
<section class="mx-auto max-w-3xl px-5 py-16 space-y-14">
  <blockquote>
    <p class="pullquote">Attached are some photos of the furniture in its “home” – looks wonderful! Thanks again for a great job, we are really enjoying these beautiful pieces again and we will recommend you to anyone we know looking for restoration work.</p>
    <footer class="mt-4 text-sm tracking-wide uppercase text-walnut">Susan</footer>
  </blockquote>
  <hr class="rule">
  <blockquote>
    <p class="pullquote">Many kind thanks for your fabulous good work of making the wardrobe for us. It looks terrific.</p>
    <footer class="mt-4 text-sm tracking-wide uppercase text-walnut">Ruth from Newtown</footer>
  </blockquote>
  <hr class="rule">
  <blockquote>
    <p class="pullquote">Thanks Nick. The chest looks magnificent.</p>
    <footer class="mt-4 text-sm tracking-wide uppercase text-walnut">Linda from Darlington</footer>
  </blockquote>
  <hr class="rule">
  <blockquote>
    <p class="pullquote">Hi Nick, we just wanted to say thanks for all of the restoration work you have done for us – dining table, chairs, chiffonier. The furniture now looks fantastic and we appreciate your dedication in bringing each piece ‘back to life’. We have enjoyed learning about our furniture from you – the history, original uses and the restoration techniques. It has been a pleasure working with you and we highly recommend you to others. Once again, many thanks</p>
    <footer class="mt-4 text-sm tracking-wide uppercase text-walnut">Wendy and Simon from Dulwich Hill</footer>
  </blockquote>
</section>
"""
        + consult_band(),
    ),
)

write(
    "contact/index.html",
    wrap(
        "Contact Us | Nikolaus Teply Restorations | Sydney",
        "Reach out to Nick Teply if you have any enquiries or in need of a quote for furniture or antique restoration. Call or message us today!",
        "contact",
        page_hero(
            "Get in Touch with Nikolaus Teply Restorations",
            "/public/images/slide3.jpg",
            "Restored cabinet and chairs",
            "Get in Touch",
        )
        + """
<section class="mx-auto grid max-w-6xl gap-12 px-5 py-16 lg:grid-cols-2">
  <div>
    <h2 class="serif text-3xl">Workshop address</h2>
    <p class="mt-4">
      <a href="https://maps.app.goo.gl/k4KDyEzhGzLdL8yH9">Suite 1 A on the ground floor of Building A<br>
      at 10 Carrington Road, Marrickville, 2204 NSW</a>
    </p>
    <p class="mt-6">Mobile: <a href="tel:0425217269">0425 217 269</a><br>
    E-mail: <a href="mailto:nikteply@gmail.com">nikteply@gmail.com</a></p>
    <div class="mt-8 flex flex-wrap gap-3">
      <a class="btn btn-primary" href="tel:0425217269">Call 0425 217 269</a>
      <a class="btn btn-secondary on-light" href="mailto:nikteply@gmail.com">Email nikteply@gmail.com</a>
    </div>
    <div class="mt-10 overflow-hidden border border-brass/30" style="aspect-ratio: 4/3;">
      <iframe title="Map of Nikolaus Teply Restorations, Marrickville" src="https://www.google.com/maps?q=10+Carrington+Road+Marrickville+NSW+2204&amp;z=17&amp;output=embed" width="100%" height="100%" style="border:0;" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
    </div>
  </div>
  <form id="consult-form" class="space-y-5" novalidate>
    <p class="serif text-3xl">Request a consultation</p>
    <p class="text-sm">The form opens an email to nikteply@gmail.com with your details filled in. Please attach photographs of the piece in a follow-up email.</p>
    <div class="field">
      <label for="name">Name</label>
      <input id="name" name="name" type="text" autocomplete="name" required>
      <span class="error">Please enter your name.</span>
    </div>
    <div class="field">
      <label for="email">Email</label>
      <input id="email" name="email" type="email" autocomplete="email" required>
      <span class="error">Please enter a valid email address.</span>
    </div>
    <div class="field">
      <label for="phone">Phone</label>
      <input id="phone" name="phone" type="tel" autocomplete="tel" required>
      <span class="error">Please enter a phone number.</span>
    </div>
    <div class="field">
      <label for="piece">Piece / service</label>
      <input id="piece" name="piece" type="text" required>
      <span class="error">Please describe the piece or service.</span>
    </div>
    <div class="field">
      <label for="message">Message</label>
      <textarea id="message" name="message" rows="6" required></textarea>
      <span class="error">Please add a short message.</span>
    </div>
    <p class="text-sm">Attach photos by email after sending.</p>
    <button class="btn btn-primary" type="submit">Send enquiry</button>
  </form>
</section>
""",
    ),
)

write(
    "404.html",
    wrap(
        "Page not found | Nikolaus Teply Restorations",
        "The page you requested could not be found. Return to Nikolaus Teply Restorations.",
        "home",
        page_hero(
            "This page could not be found",
            "/public/images/new-slide2-opt.webp",
            "antique restoration Sydney",
            "404",
        )
        + """
<section class="mx-auto max-w-2xl px-5 py-16">
  <p>The address may have changed, or the page may never have existed. The workshop itself is still in Marrickville.</p>
  <div class="mt-8 flex flex-wrap gap-3">
    <a class="btn btn-primary" href="/">Return home</a>
    <a class="btn btn-secondary on-light" href="/contact/">Contact the workshop</a>
  </div>
</section>
""",
    ),
)

print("done")
