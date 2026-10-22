# Content for the Super Routine content pages. Edit here, then run: python3 tools/build_pages.py
# Rules: structure/function wording only ("supports", "contributes to"), never disease claims
# ("treats", "cures", "prevents"). Every dose/safety fact needs a source in the page's sources list.

SITE = "https://www.superroutine.in"

AUTHOR = {
    "name": "Shubham Pasalkar",
    "title": "Founder",
    "knows": ["Dietary supplements", "Nutrition", "Supplement formulation"],
}

ODS = "https://ods.od.nih.gov/factsheets/"
S_MG = ("NIH Office of Dietary Supplements: Magnesium fact sheet", ODS + "Magnesium-HealthProfessional/")
S_ZN = ("NIH Office of Dietary Supplements: Zinc fact sheet", ODS + "Zinc-HealthProfessional/")
S_D = ("NIH Office of Dietary Supplements: Vitamin D fact sheet", ODS + "VitaminD-HealthProfessional/")
S_K = ("NIH Office of Dietary Supplements: Vitamin K fact sheet", ODS + "VitaminK-HealthProfessional/")
S_B12 = ("NIH Office of Dietary Supplements: Vitamin B12 fact sheet", ODS + "VitaminB12-HealthProfessional/")
S_OM = ("NIH Office of Dietary Supplements: Omega-3 fatty acids fact sheet", ODS + "Omega3FattyAcids-HealthProfessional/")
S_ASH = ("NIH Office of Dietary Supplements: Ashwagandha fact sheet", ODS + "Ashwagandha-HealthProfessional/")
S_MEL = ("NCCIH (NIH): Melatonin, what you need to know", "https://www.nccih.nih.gov/health/melatonin-what-you-need-to-know")
S_SHIL_T = ("Keller et al. (2019), Journal of the International Society of Sports Nutrition: shilajit and muscle strength",
            "https://link.springer.com/article/10.1186/s12970-019-0270-2")
S_FE = ("NIH Office of Dietary Supplements: Iron fact sheet", ODS + "Iron-HealthProfessional/")
S_CA = ("NIH Office of Dietary Supplements: Calcium fact sheet", ODS + "Calcium-HealthProfessional/")
S_HAM = ("Hamedifard et al. (2020), Lipids in Health and Disease: combined magnesium and zinc supplementation, randomised controlled trial",
         "https://link.springer.com/article/10.1186/s12944-020-01298-4")
S_SHIL_W = ("WebMD: Shilajit uses, side effects and interactions", "https://www.webmd.com/vitamins-supplements/shilajit")

ING = "/ingredients/"
LINKS = {
    "d3": (ING + "vitamin-d3-k2/", "Vitamin D3 + K2", "600 IU · after breakfast"),
    "b12": (ING + "vitamin-b12-methylcobalamin/", "Vitamin B12 (methylcobalamin)", "1 mg · after breakfast"),
    "zn": (ING + "zinc-picolinate/", "Zinc Picolinate", "12 mg · after breakfast"),
    "shil": (ING + "himalayan-shilajit/", "Himalayan Shilajit", "250 mg · after breakfast"),
    "mg": (ING + "magnesium-glycinate/", "Magnesium Glycinate", "1000 mg (140 mg elemental) · night"),
    "ash": (ING + "ashwagandha-ksm-66/", "Ashwagandha KSM-66", "300 mg · night"),
    "om": (ING + "omega-3-rtg/", "Omega-3 (rTG)", "750 mg · night"),
    "mel": (ING + "melatonin/", "Melatonin", "3 mg · before bed"),
}


def cards(keys):
    return '<div class="cards">' + "".join(
        f'<a class="card" href="{LINKS[k][0]}"><strong>{LINKS[k][1]}</strong><span>{LINKS[k][2]}</span></a>'
        for k in keys) + "</div>"


def link(k, text=None):
    return f'<a href="{LINKS[k][0]}">{text or LINKS[k][1]}</a>'


DAY = ["d3", "b12", "zn", "shil"]
NIGHT = ["mg", "ash", "om", "mel"]
ING_CRUMB = [("Ingredients", "/ingredients/")]

PAGES = [
# ---------------------------------------------------------------- DAY PACK
{
 "path": "/day-pack/", "crumb": "Day Pack", "priority": "0.9", "about": "Super Routine Day Pack",
 "title": "Day Pack: Morning Supplements – D3+K2, B12, Zinc, Shilajit",
 "description": "Vitamin D3 + K2, methylcobalamin B12, zinc picolinate and purified shilajit in one morning sachet. Doses, forms and why they go in the morning.",
 "h1": "Day Pack: your morning supplements in one sachet",
 "answer": "The Day Pack holds four nutrients that suit the morning: <strong>vitamin D3 + K2</strong> (600 IU), <strong>vitamin B12</strong> as methylcobalamin (1 mg), <strong>zinc picolinate</strong> (12 mg) and <strong>purified Himalayan shilajit</strong> (250 mg). Take one sachet after breakfast, ideally with a meal that contains some fat.",
 "facts": [("When", "After breakfast"), ("Sachets", "30 per month"), ("Focus", "Energy · Focus · Immunity · Bone")],
 "body": f'''
<h2>What is in the Day Pack</h2>
<div class="tw"><table><thead><tr><th>Nutrient</th><th>Form</th><th>Dose</th><th>Why it is here</th></tr></thead><tbody>
<tr><td>{link("d3","Vitamin D3 + K2")}</td><td>Cholecalciferol + K2</td><td>600 IU (15 mcg)</td><td>Contributes to normal bones, muscle function and immune function. K2 is paired with it.</td></tr>
<tr><td>{link("b12","Vitamin B12")}</td><td>Methylcobalamin</td><td>1 mg</td><td>Contributes to normal energy metabolism, red blood cell formation and nerve function.</td></tr>
<tr><td>{link("zn","Zinc")}</td><td>Zinc picolinate</td><td>12 mg</td><td>Contributes to normal immune function, skin and protein synthesis.</td></tr>
<tr><td>{link("shil","Shilajit")}</td><td>Purified resin</td><td>250 mg</td><td>Traditional Ayurvedic ingredient. Early studies look at energy and muscle fatigue.</td></tr>
</tbody></table></div>
<h2>Why these four go in the morning</h2>
<p><strong>Vitamin D and K2 are fat-soluble</strong>, so they are best taken with a meal. Breakfast is the most consistent meal for most people, which makes it easy to remember.</p>
<p><strong>Zinc is kept apart from the Night Pack's magnesium.</strong> At normal doses most people can take the two together, but very high zinc intakes can reduce magnesium absorption, and minerals compete for absorption in the gut. Splitting them across morning and night removes the question entirely. Read more in {link("zn","our zinc guide")}.</p>
<p><strong>B12 and shilajit</strong> support the day's energy metabolism, so they sit with the morning routine. Neither is a stimulant and neither contains caffeine.</p>
<h2>How to take it</h2>
<ul><li>Take one Day sachet after breakfast with water.</li><li>Take one {'<a href="/night-pack/">Night sachet</a>'} after dinner or 30–60 minutes before bed.</li><li>Do not take more than one Day sachet a day.</li><li>If you take iron tablets, antibiotics or thyroid medicine, ask your doctor or pharmacist about spacing them from the Day Pack.</li></ul>
<h2>Read the full guide for each nutrient</h2>
{cards(DAY)}
''',
 "faq": [
  ("Can I take the Day Pack on an empty stomach?", "It is better after breakfast. Vitamin D and K2 absorb best with food that contains fat, and zinc can cause nausea in some people on an empty stomach."),
  ("Does the Day Pack contain caffeine?", "No. There are no stimulants in the Day Pack."),
  ("Can I take the Day Pack and Night Pack together?", "They are designed to be taken apart: Day after breakfast, Night in the evening. This keeps zinc and magnesium apart and puts melatonin at bedtime, where it belongs."),
 ],
 "sources": [S_D, S_K, S_B12, S_ZN, S_MG, S_SHIL_T],
},
# ---------------------------------------------------------------- NIGHT PACK
{
 "path": "/night-pack/", "crumb": "Night Pack", "priority": "0.9", "about": "Super Routine Night Pack",
 "title": "Night Pack: Sleep & Recovery Supplements in One Sachet",
 "description": "The Super Routine Night Pack: magnesium glycinate, ashwagandha KSM-66, omega-3 rTG and 3 mg melatonin in one evening sachet. Doses, forms, timing and safety.",
 "h1": "Night Pack: your evening supplements in one sachet",
 "answer": "The Night Pack holds four nutrients for the evening: <strong>magnesium glycinate</strong> (1000 mg, giving 140 mg elemental magnesium), <strong>ashwagandha KSM-66</strong> (300 mg), <strong>omega-3 in rTG form</strong> (750 mg) and <strong>melatonin</strong> (3 mg). Take one sachet after dinner or 30–60 minutes before bed.",
 "facts": [("When", "After dinner / before bed"), ("Sachets", "30 per month"), ("Focus", "Recovery · Sleep · Muscle · Wellness")],
 "body": f'''
<h2>What is in the Night Pack</h2>
<div class="tw"><table><thead><tr><th>Nutrient</th><th>Form</th><th>Dose</th><th>Why it is here</th></tr></thead><tbody>
<tr><td>{link("mg","Magnesium")}</td><td>Glycinate (chelated)</td><td>1000 mg = 140 mg elemental</td><td>Contributes to normal muscle and nervous system function and to reduced tiredness.</td></tr>
<tr><td>{link("ash","Ashwagandha")}</td><td>KSM-66 root extract</td><td>300 mg</td><td>Studied for perceived stress and sleep quality, at 250–600 mg a day.</td></tr>
<tr><td>{link("om","Omega-3")}</td><td>Re-esterified triglyceride (rTG)</td><td>750 mg</td><td>EPA and DHA contribute to normal heart and brain function.</td></tr>
<tr><td>{link("mel","Melatonin")}</td><td>Melatonin</td><td>3 mg</td><td>Helps shorten the time it takes to fall asleep and eases jet lag.</td></tr>
</tbody></table></div>
<h2>Why these four go at night</h2>
<p><strong>Melatonin only makes sense before bed.</strong> It signals to the body clock that it is night, so it has to be taken in the evening. Taken in the morning it can cause daytime drowsiness.</p>
<p><strong>Magnesium glycinate</strong> pairs magnesium with glycine, an amino acid, and is gentle on the stomach. Many people take magnesium as part of a wind-down routine, and the glycinate form is less likely to have a laxative effect than oxide or citrate. See {link("mg","our magnesium glycinate guide")}.</p>
<p><strong>Omega-3 with dinner.</strong> Omega-3 can be taken at any time of day. Taking it with the evening meal fits the routine and reduces fishy aftertaste for many people.</p>
<p><strong>Ashwagandha</strong> has been studied for stress and sleep, and the evening suits a calmer routine. Trials mostly lasted 8–12 weeks.</p>
<h2>How to take it</h2>
<ul><li>Take one Night sachet after dinner or 30–60 minutes before bed, with water.</li><li>Do not drive or operate machinery after taking it, because melatonin can make you drowsy.</li><li>Do not combine with other sleep aids or sedatives without asking your doctor.</li><li>Not for children, or for anyone pregnant or breastfeeding.</li></ul>
<h2>Read the full guide for each nutrient</h2>
{cards(NIGHT)}
<p>Comparing options? Read our honest guide to the <a href="/science/best-supplements-for-night/">best supplements to take at night</a>.</p>
''',
 "faq": [
  ("Can I take magnesium and melatonin together?", "Yes. They work differently: melatonin signals night to the body clock and magnesium supports normal muscle and nerve function. Both are commonly taken in the evening. Check with your doctor if you take sedatives or blood thinners."),
  ("Will the Night Pack make me groggy in the morning?", "3 mg of melatonin is a common adult dose. Some people, especially older adults, feel drowsy the next morning. If that happens, take the sachet earlier in the evening and speak to a pharmacist."),
  ("Is it safe to take every night?", "The doses are within commonly studied ranges, but long-term safety data for melatonin and ashwagandha are limited. Most ashwagandha trials lasted up to 3 months. Review your routine with your doctor if you plan to use it for longer."),
 ],
 "sources": [S_MG, S_ASH, S_OM, S_MEL],
},
# ---------------------------------------------------------------- HUB
{
 "path": "/ingredients/", "crumb": "Ingredients", "priority": "0.9", "schema_type": "CollectionPage",
 "title": "The 8 Ingredients: Doses, Forms & Best Time to Take Each",
 "description": "Exact dose, form and timing for all 8 Super Routine ingredients: D3+K2, B12, zinc, shilajit, magnesium, ashwagandha, omega-3 and melatonin.",
 "h1": "The 8 essentials: forms, doses and timing",
 "answer": "Super Routine has eight ingredients. Four go in the <a href=\"/day-pack/\">Day Pack</a>, taken after breakfast, and four in the <a href=\"/night-pack/\">Night Pack</a>, taken in the evening. Each was chosen for a well-absorbed form and a dose within the range used in published studies.",
 "body": f'''
<div class="tw"><table><thead><tr><th>Ingredient</th><th>Form</th><th>Dose</th><th>Pack</th></tr></thead><tbody>
<tr><td>{link("d3","Vitamin D3 + K2")}</td><td>Cholecalciferol + K2</td><td>600 IU</td><td>Day</td></tr>
<tr><td>{link("b12","Vitamin B12")}</td><td>Methylcobalamin</td><td>1 mg</td><td>Day</td></tr>
<tr><td>{link("zn","Zinc")}</td><td>Picolinate</td><td>12 mg</td><td>Day</td></tr>
<tr><td>{link("shil","Shilajit")}</td><td>Purified Himalayan resin</td><td>250 mg</td><td>Day</td></tr>
<tr><td>{link("mg","Magnesium")}</td><td>Glycinate</td><td>1000 mg (140 mg elemental)</td><td>Night</td></tr>
<tr><td>{link("ash","Ashwagandha")}</td><td>KSM-66 root extract</td><td>300 mg</td><td>Night</td></tr>
<tr><td>{link("om","Omega-3")}</td><td>rTG fish oil</td><td>750 mg</td><td>Night</td></tr>
<tr><td>{link("mel","Melatonin")}</td><td>Melatonin</td><td>3 mg</td><td>Night</td></tr>
</tbody></table></div>
<h2>Day Pack ingredients</h2>
{cards(DAY)}
<h2>Night Pack ingredients</h2>
{cards(NIGHT)}
<h2>Which supplements go together</h2>
<p>For combinations to avoid, read <a href="/science/supplements-not-to-take-together/">7 supplements you should not take together</a>. More guides are in our <a href="/science/">science library</a>.</p>
<h2>How our doses are set</h2>
<p>We start from the daily intake levels set by health authorities, and from the doses used in human studies. We choose forms that absorb well, such as chelated minerals, methylcobalamin and rTG omega-3. Every dose stays below the tolerable upper intake level where one exists. Every amount is printed on the pack, with no proprietary blends.</p>
''',
 "faq": [
  ("Which supplements should not be taken together?", "Some combinations compete or interact. High-dose zinc and magnesium compete for absorption, iron reduces zinc absorption, vitamin K affects warfarin, and minerals bind some antibiotics. That is why Super Routine splits zinc (Day) and magnesium (Night) and lists every interaction on each ingredient page."),
  ("Why a day and night split instead of one multivitamin?", "Timing matters for some nutrients. Melatonin belongs at bedtime, fat-soluble vitamins absorb best with a meal, and keeping zinc and magnesium apart avoids competition between them."),
 ],
 "sources": [S_MG, S_ZN, S_D, S_K, S_B12, S_OM, S_ASH, S_MEL],
},
# ---------------------------------------------------------------- MAGNESIUM
{
 "path": ING + "magnesium-glycinate/", "crumb": "Magnesium Glycinate", "crumbs": ING_CRUMB, "about": "Magnesium glycinate",
 "title": "Magnesium Glycinate: Benefits, Dose & When to Take It",
 "description": "Magnesium glycinate explained: elemental magnesium per dose, benefits, morning vs night, interactions, and how it compares with oxide and citrate.",
 "h1": "Magnesium glycinate: benefits, dose and when to take it",
 "answer": "Magnesium glycinate is magnesium bound to the amino acid glycine. It is gentle on the stomach and well absorbed. Most people take it <strong>in the evening</strong>. A 1000 mg dose gives about <strong>140 mg of elemental magnesium</strong>, well within the 350 mg daily upper limit for supplements. That is the amount in the Super Routine Night Pack.",
 "facts": [("Our dose", "1000 mg (140 mg elemental)"), ("Pack", "Night"), ("Adult RDA", "310–420 mg/day"), ("Supplement UL", "350 mg/day")],
 "body": f'''
<h2>Elemental magnesium: read this before comparing labels</h2>
<p>Labels can be confusing. "1000 mg magnesium glycinate" is the weight of the whole compound, magnesium plus glycine. Only about 14% of that weight is magnesium itself. The figure that matters is <strong>elemental magnesium</strong>: 1000 mg of glycinate gives roughly 140 mg.</p>
<p>The adult Recommended Dietary Allowance is 400–420 mg a day for men and 310–320 mg for women, from food and supplements combined. The upper limit for magnesium <em>from supplements</em> is 350 mg a day. 140 mg tops up a diet that falls short without going near that limit.</p>
<h2>What magnesium does</h2>
<p>Magnesium is a co-factor in more than 300 enzyme systems. It contributes to normal muscle function, normal nervous system function, energy-yielding metabolism and the reduction of tiredness and fatigue. It also helps regulate calcium movement in nerve and muscle cells.</p>
<h2>Glycinate vs oxide vs citrate</h2>
<div class="tw"><table><thead><tr><th>Form</th><th>Stomach tolerance</th><th>Typical use</th></tr></thead><tbody>
<tr><td>Glycinate (bisglycinate)</td><td>Gentle; low laxative effect</td><td>Daily top-up, evening routine</td></tr>
<tr><td>Citrate</td><td>Can loosen stools</td><td>Also used for occasional constipation</td></tr>
<tr><td>Oxide</td><td>More likely to cause loose stools; absorbed less well</td><td>Cheap tablets and antacids</td></tr>
</tbody></table></div>
<h2>When to take magnesium glycinate</h2>
<p>You can take it at any time, but most people take it <strong>in the evening</strong> with dinner or before bed. It fits a wind-down routine, and evening is when the Super Routine Night Pack is taken. Evidence that magnesium improves sleep is limited and mixed, and is strongest in people whose intake is low. We do not claim it is a sleep aid.</p>
<p>We keep magnesium in the Night Pack and {link("zn","zinc")} in the Day Pack. Very high zinc intakes (around 142 mg a day) have been shown to reduce magnesium absorption. Our doses are far lower, but splitting the two removes any competition. See <a href="/science/zinc-and-magnesium-together/">taking zinc and magnesium together</a>.</p>
<h2>Who should be careful</h2>
<ul>
<li><strong>Antibiotics</strong> (tetracyclines such as doxycycline; quinolones such as ciprofloxacin): take the antibiotic at least 2 hours before, or 4–6 hours after, magnesium.</li>
<li><strong>Bisphosphonates</strong> for bone health (such as alendronate): separate by at least 2 hours.</li>
<li><strong>Diuretics and long-term proton pump inhibitors</strong> (such as omeprazole) can change magnesium levels. Ask your doctor.</li>
<li><strong>Kidney disease:</strong> do not take magnesium supplements without medical advice.</li>
</ul>
<p>Magnesium sits in the Night Pack with {link("ash","ashwagandha")}, {link("om","omega-3")} and {link("mel","melatonin")}. <a href="/night-pack/">See the full Night Pack</a>.</p>
''',
 "faq": [
  ("Is magnesium glycinate better taken in the morning or at night?", "Either works, because absorption does not depend on time of day. Most people prefer the evening because it fits a wind-down routine, and that is when the Super Routine Night Pack is taken."),
  ("How much elemental magnesium is in 1000 mg of magnesium glycinate?", "About 140 mg. Glycinate is roughly 14% magnesium by weight."),
  ("Can I take magnesium glycinate every day?", "Yes, for most healthy adults, if total magnesium from supplements stays below 350 mg a day. People with kidney disease should ask their doctor first."),
  ("Is magnesium glycinate the same as bisglycinate?", "Yes. Bisglycinate means one magnesium bound to two glycine molecules, which is what most labels mean by glycinate."),
 ],
 "sources": [S_MG],
},
# ---------------------------------------------------------------- ASHWAGANDHA
{
 "path": ING + "ashwagandha-ksm-66/", "crumb": "Ashwagandha KSM-66", "crumbs": ING_CRUMB, "about": "Ashwagandha (Withania somnifera) root extract",
 "title": "Ashwagandha KSM-66: Dose (300 vs 600 mg), Timing & Safety",
 "description": "KSM-66 ashwagandha explained: doses studied (250–600 mg), when to take it, trial length, and who should avoid it (thyroid, pregnancy, liver).",
 "h1": "Ashwagandha KSM-66: dose, timing and safety",
 "answer": "KSM-66 is a full-spectrum ashwagandha extract made from the root only. Human trials have used <strong>250–600 mg a day</strong> for stress and sleep, mostly for 8–12 weeks. The Super Routine Night Pack contains <strong>300 mg</strong>, taken in the evening. Avoid it if you are pregnant or breastfeeding, or have thyroid or liver problems, unless your doctor agrees.",
 "facts": [("Our dose", "300 mg KSM-66"), ("Pack", "Night"), ("Studied range", "250–600 mg/day"), ("Typical trial length", "8–12 weeks")],
 "body": f'''
<h2>What KSM-66 is</h2>
<p>Ashwagandha (<em>Withania somnifera</em>) is an Ayurvedic herb. KSM-66 is a branded extract made from the root only and standardised to its withanolide content. Generic ashwagandha powders vary, and some include leaf. A standardised extract means each dose is consistent.</p>
<h2>What the research says</h2>
<p>Several randomised trials found that ashwagandha root extract lowered perceived stress and cortisol compared with placebo. A 2021 meta-analysis found a small but significant improvement in sleep, larger in people with insomnia. The NIH Office of Dietary Supplements notes the limits: trials are small and short, most were run in India, and the extracts differ. We describe ashwagandha as <em>studied for</em> stress and sleep, not as a treatment.</p>
<h2>300 mg vs 600 mg</h2>
<p>KSM-66 trials on sleep used 250–600 mg a day, and some found larger effects at 600 mg. We chose 300 mg so the Night Pack works alongside {link("mel","melatonin")} and {link("mg","magnesium")}, rather than relying on a single high dose. 300 mg is also the lower end of the range an international psychiatry taskforce suggested for anxiety (300–600 mg of root extract).</p>
<h2>When to take ashwagandha</h2>
<p>Trials gave it once or twice a day, morning or evening, so timing is flexible. We put it in the evening because the sleep studies are a key reason it is in the formula, and it fits a wind-down routine.</p>
<h2>Who should avoid it</h2>
<ul>
<li><strong>Pregnancy and breastfeeding:</strong> avoid. Several authorities advise against use.</li>
<li><strong>Thyroid conditions or thyroid medicine:</strong> ashwagandha can change thyroid hormone levels. Speak to your doctor.</li>
<li><strong>Liver disease:</strong> rare cases of liver injury have been reported. Stop and see a doctor if you notice yellowing skin, dark urine or abdominal pain.</li>
<li><strong>Medicines</strong> for diabetes, blood pressure, immune suppression or sedation: ashwagandha may interact with them. Ask your doctor.</li>
<li><strong>Hormone-sensitive prostate cancer:</strong> avoid unless your specialist agrees.</li>
</ul>
<p>Safety beyond about 3 months has not been well studied. If you plan to use it for longer, review it with your doctor.</p>
''',
 "faq": [
  ("Is it better to take ashwagandha in the morning or at night?", "Trials used both. Night suits a wind-down routine and the sleep studies, so it is in the Super Routine Night Pack."),
  ("What is the difference between KSM-66 and normal ashwagandha?", "KSM-66 is a root-only extract standardised to withanolides, so each dose is consistent. Generic powders vary in strength and may include leaf."),
  ("How long does ashwagandha take to work?", "Most trials measured results after 8–12 weeks of daily use."),
 ],
 "sources": [S_ASH],
},
# ---------------------------------------------------------------- OMEGA-3
{
 "path": ING + "omega-3-rtg/", "crumb": "Omega-3 (rTG)", "crumbs": ING_CRUMB, "about": "Omega-3 fatty acids (EPA and DHA)",
 "title": "Omega-3 rTG vs EE Fish Oil: Best Time to Take Omega-3",
 "description": "What rTG omega-3 is, how it compares with ethyl ester fish oil, the best time to take omega-3 (morning or night), and interactions with blood thinners.",
 "h1": "Omega-3 (rTG): form, dose and the best time to take it",
 "answer": "Omega-3 can be taken <strong>at any time of day</strong>. What matters is taking it consistently, and with a meal. The rTG (re-esterified triglyceride) form is absorbed somewhat better than the cheaper ethyl ester (EE) form. The Super Routine Night Pack contains <strong>750 mg of rTG omega-3</strong>, taken after dinner.",
 "facts": [("Our dose", "750 mg rTG"), ("Pack", "Night"), ("Form", "Re-esterified triglyceride"), ("Take with", "A meal")],
 "body": f'''
<h2>What EPA and DHA do</h2>
<p>EPA and DHA are long-chain omega-3 fats from oily fish and algae. They are built into cell membranes, especially in the brain and eyes. EPA and DHA contribute to normal heart function, and DHA contributes to normal brain function and vision. Many Indian diets, especially vegetarian ones, contain little EPA or DHA.</p>
<h2>rTG vs EE vs natural TG</h2>
<div class="tw"><table><thead><tr><th>Form</th><th>What it is</th><th>Absorption</th></tr></thead><tbody>
<tr><td>Natural triglyceride (TG)</td><td>Fish oil as it occurs in fish</td><td>Good</td></tr>
<tr><td>Ethyl ester (EE)</td><td>Concentrated by bonding fatty acids to ethanol</td><td>Somewhat lower</td></tr>
<tr><td>Re-esterified triglyceride (rTG)</td><td>Concentrated, then converted back to the triglyceride form</td><td>Somewhat higher than EE</td></tr>
</tbody></table></div>
<p>All three forms raise blood EPA and DHA. rTG gives a concentrated oil in a form closer to natural fish oil.</p>
<h2>Best time to take omega-3: morning or night?</h2>
<p>No study shows that one time of day is clearly better. Two things do matter:</p>
<ul><li><strong>Take it with a meal.</strong> Omega-3 is a fat and is handled like dietary fat, and taking it with food reduces fishy aftertaste and burps for many people.</li><li><strong>Be consistent.</strong> Blood levels build over weeks of daily use, not hours.</li></ul>
<p>We put omega-3 in the Night Pack so it is taken with dinner, usually the largest meal of the day in India. It also keeps the morning sachet small.</p>
<h2>Who should be careful</h2>
<ul>
<li><strong>Blood thinners</strong> such as warfarin: fish oil may slightly affect clotting. Tell your doctor, who may monitor your INR.</li>
<li><strong>Fish or shellfish allergy:</strong> check with your doctor before taking fish oil.</li>
<li>Common mild side effects are an unpleasant taste, heartburn, nausea and loose stools.</li>
</ul>
<p>See the rest of the <a href="/night-pack/">Night Pack</a>: {link("mg","magnesium glycinate")}, {link("ash","ashwagandha")} and {link("mel","melatonin")}.</p>
''',
 "faq": [
  ("Should I take omega-3 in the morning or at night?", "Either is fine. Take it with a meal and at the same time each day. We use dinner because it is usually the largest meal of the day."),
  ("Is rTG omega-3 better than regular fish oil?", "rTG is absorbed somewhat better than ethyl ester (EE) concentrates, and is similar to natural fish oil. All forms raise EPA and DHA levels."),
  ("Can vegetarians get EPA and DHA?", "Plant foods such as flax provide ALA, which the body converts to EPA and DHA only in small amounts. Algae oil is a vegetarian source of DHA and EPA. The Super Routine Night Pack uses fish oil."),
 ],
 "sources": [S_OM],
},
# ---------------------------------------------------------------- MELATONIN
{
 "path": ING + "melatonin/", "crumb": "Melatonin", "crumbs": ING_CRUMB, "about": "Melatonin",
 "title": "Melatonin 3 mg: When to Take It, How It Works & Safety",
 "description": "Melatonin explained: how it works, when to take 3 mg, what the evidence shows for sleep onset and jet lag, and who should not take it.",
 "h1": "Melatonin 3 mg: when to take it and how it works",
 "answer": "Melatonin is the hormone that tells the body clock it is night. Take it <strong>30–60 minutes before your usual bedtime</strong>. In studies it shortened the time to fall asleep in people with delayed sleep timing, and eased jet lag. The Super Routine Night Pack contains <strong>3 mg</strong>, a common adult dose. It is not for children or for anyone pregnant or breastfeeding.",
 "facts": [("Our dose", "3 mg"), ("Pack", "Night"), ("When", "30–60 min before bed"), ("Not for", "Children, pregnancy")],
 "body": f'''
<h2>How melatonin works</h2>
<p>The brain releases melatonin when it gets dark. It acts on MT1 and MT2 receptors in the body's master clock, which lowers alertness and shifts the body towards sleep. Bright screens late at night, irregular schedules and travel across time zones can all delay this signal.</p>
<h2>What the research shows</h2>
<ul>
<li><strong>Falling asleep:</strong> in people with delayed sleep timing, melatonin helped them fall asleep about 20–35 minutes sooner in reviewed studies, especially when combined with a fixed bedtime.</li>
<li><strong>Jet lag:</strong> studies suggest it reduces jet lag symptoms after flights both east and west.</li>
<li><strong>Chronic insomnia:</strong> evidence is weaker. Behavioural therapy (CBT-I) is the first-line approach.</li>
</ul>
<h2>When and how to take it</h2>
<p>Take the Night sachet <strong>30–60 minutes before your target bedtime</strong>, at about the same time every night, and dim screens and lights after taking it. Do not take melatonin in the morning or during the day.</p>
<h2>Why 3 mg</h2>
<p>3 mg is a widely used adult dose. Higher doses do not reliably work better and are more likely to cause next-day grogginess. Some people do well on less. If you feel drowsy the next morning, take it earlier in the evening and speak to a pharmacist.</p>
<h2>Who should not take it</h2>
<ul>
<li>Children and teenagers, unless a doctor advises it.</li>
<li>Pregnant or breastfeeding women.</li>
<li>People with epilepsy, or taking blood thinners, sedatives or immunosuppressants: ask your doctor first.</li>
<li>People with dementia: guidelines advise against it.</li>
<li>Do not drive or operate machinery after taking melatonin.</li>
</ul>
<p>Common side effects are mild: headache, dizziness, nausea and sleepiness. Long-term safety data are limited.</p>
<p>Melatonin works alongside {link("mg","magnesium glycinate")} and {link("ash","ashwagandha")} in the <a href="/night-pack/">Night Pack</a>.</p>
''',
 "faq": [
  ("How long before bed should I take melatonin?", "30–60 minutes before your usual bedtime, at the same time each night."),
  ("Can I take melatonin and magnesium together?", "Yes. They work in different ways and are commonly taken together in the evening. Check with your doctor if you take sedatives."),
  ("Is 3 mg of melatonin too much?", "3 mg is a common adult dose. Higher doses are not reliably better and can cause morning grogginess. Some people need less."),
  ("Is melatonin habit-forming?", "Melatonin is not considered habit-forming, but long-term safety has not been well studied. Use it as part of a consistent sleep routine."),
 ],
 "sources": [S_MEL],
},
# ---------------------------------------------------------------- VITAMIN D3 + K2
{
 "path": ING + "vitamin-d3-k2/", "crumb": "Vitamin D3 + K2", "crumbs": ING_CRUMB, "about": "Vitamin D3 (cholecalciferol) and vitamin K2",
 "title": "Vitamin D3 + K2: Dosage, Best Time to Take & Why They Pair",
 "description": "Vitamin D3 with K2 explained: why 600 IU, the best time to take vitamin D3, why it pairs with K2, and the warfarin interaction to know.",
 "h1": "Vitamin D3 + K2: dose, best time to take it and why they pair",
 "answer": "Take vitamin D3 <strong>with a meal that contains some fat</strong>, ideally at the same time each day. Breakfast works well for most people. D3 is fat-soluble and absorbs best with food. The Super Routine Day Pack contains <strong>600 IU (15 mcg)</strong> of D3, which matches the adult daily recommendation, paired with vitamin K2.",
 "facts": [("Our dose", "600 IU (15 mcg) D3 + K2"), ("Pack", "Day"), ("Adult RDA", "600 IU (800 IU 70+)"), ("UL", "4,000 IU/day")],
 "body": f'''
<h2>Why vitamin D matters in India</h2>
<p>The skin makes vitamin D from sunlight, but indoor work, pollution, clothing, sunscreen and darker skin all reduce it. Low vitamin D status is common in India despite the sunshine. Vitamin D contributes to the normal absorption of calcium, normal bones and teeth, normal muscle function and normal immune function.</p>
<h2>Why D3 and not D2</h2>
<p>Both forms raise blood vitamin D, but D3 (cholecalciferol) raises and maintains levels more effectively than D2 (ergocalciferol) in most studies. D3 is also the form the skin makes.</p>
<h2>Why D3 is paired with K2</h2>
<p>Vitamin D raises calcium absorption from the gut. Vitamin K is needed to activate proteins such as osteocalcin, which bind calcium into bone. Pairing the two is a common approach, though trials have not shown that the combination prevents fractures. We include K2 because both nutrients contribute to normal bones.</p>
<h2>Why 600 IU and not 60,000 IU</h2>
<p>600 IU a day is the adult Recommended Dietary Allowance (800 IU over age 70), and it is used daily to <strong>maintain</strong> levels. High-dose sachets such as 60,000 IU are given weekly by doctors to <strong>correct</strong> a diagnosed deficiency. That is treatment, not daily nutrition. The upper limit for adults is 4,000 IU a day. If you have been told you are deficient, follow your doctor's plan.</p>
<h2>Best time to take vitamin D3</h2>
<p>With a meal that contains some fat, at a consistent time. Breakfast is easiest to remember, which is why D3 + K2 is in the <a href="/day-pack/">Day Pack</a>.</p>
<h2>Who should be careful</h2>
<ul>
<li><strong>Warfarin or other vitamin K antagonists:</strong> vitamin K can reduce the effect of warfarin. Do not take a product with K2 without your doctor's approval.</li>
<li>Steroids, orlistat, some statins and thiazide diuretics can interact with vitamin D. Ask your doctor.</li>
<li>High calcium levels, kidney stones or sarcoidosis: ask your doctor first.</li>
</ul>
''',
 "faq": [
  ("What is the best time to take vitamin D3?", "With a meal that contains some fat, at the same time every day. Breakfast or lunch both work."),
  ("Should vitamin D3 be taken with K2?", "Many people take them together because vitamin D raises calcium absorption and vitamin K helps activate the proteins that use calcium in bone. Anyone on warfarin must speak to their doctor first."),
  ("Is 600 IU of vitamin D enough?", "600 IU is the daily recommendation for adults up to 70 and is meant to maintain normal levels. People with a diagnosed deficiency usually need a doctor-prescribed higher dose for a period."),
 ],
 "sources": [S_D, S_K],
},
# ---------------------------------------------------------------- B12
{
 "path": ING + "vitamin-b12-methylcobalamin/", "crumb": "Vitamin B12", "crumbs": ING_CRUMB, "about": "Vitamin B12 (methylcobalamin)",
 "title": "Methylcobalamin vs Cyanocobalamin: Vitamin B12 Form & Timing",
 "description": "Methylcobalamin vs cyanocobalamin explained, plus the best time to take vitamin B12, why 1 mg, and who is most at risk of low B12 in India.",
 "h1": "Vitamin B12: methylcobalamin vs cyanocobalamin, dose and timing",
 "answer": "Both <strong>methylcobalamin</strong> and <strong>cyanocobalamin</strong> raise vitamin B12 levels. Cyanocobalamin is converted in the body, while methylcobalamin is already an active form. B12 can be taken at any time, though many people take it in the morning. The Super Routine Day Pack contains <strong>1 mg (1,000 mcg) of methylcobalamin</strong>.",
 "facts": [("Our dose", "1 mg methylcobalamin"), ("Pack", "Day"), ("Adult RDA", "2.4 mcg/day"), ("UL", "None set")],
 "body": f'''
<h2>Who is most at risk of low B12</h2>
<p>B12 is found almost only in animal foods, so <strong>vegetarians and vegans</strong> are at higher risk, and that covers a large share of India. Absorption also falls with age, and with long-term use of <strong>metformin</strong> or acid-reducing medicines (proton pump inhibitors and H2 blockers). Low B12 can cause tiredness, poor concentration, and tingling in the hands and feet.</p>
<h2>What B12 does</h2>
<p>Vitamin B12 contributes to normal energy-yielding metabolism, the formation of red blood cells, normal nerve function and the reduction of tiredness and fatigue.</p>
<h2>Methylcobalamin vs cyanocobalamin</h2>
<div class="tw"><table><thead><tr><th></th><th>Methylcobalamin</th><th>Cyanocobalamin</th></tr></thead><tbody>
<tr><td>What it is</td><td>One of the two active coenzyme forms</td><td>Synthetic, stable form</td></tr>
<tr><td>In the body</td><td>Used directly</td><td>Converted to the active forms</td></tr>
<tr><td>Raises B12 levels</td><td>Yes</td><td>Yes</td></tr>
<tr><td>Common in India</td><td>Very common in pharmacy B12 tablets</td><td>Common in multivitamins</td></tr>
</tbody></table></div>
<p>Honest summary: both work for most healthy people, and there is limited evidence that one is clearly superior. We chose methylcobalamin because it is already active and is widely used in Indian pharmacy B12 products.</p>
<h2>Why 1 mg when the RDA is only 2.4 mcg</h2>
<p>The body absorbs only a small share of a large oral dose, because the intrinsic factor pathway saturates at a few micrograms. Above that, roughly 1% is absorbed by passive diffusion. A 1 mg dose therefore delivers a useful amount even if absorption is weak. No upper limit has been set for B12, because excess is excreted.</p>
<h2>Best time to take vitamin B12</h2>
<p>B12 can be taken at any time, with or without food. We put it in the <a href="/day-pack/">Day Pack</a> because it supports energy metabolism and fits the morning routine with {link("d3","vitamin D3")} and {link("zn","zinc")}.</p>
''',
 "faq": [
  ("Is methylcobalamin better than cyanocobalamin?", "Both raise B12 levels. Methylcobalamin is an active form and cyanocobalamin is converted in the body. Evidence that one is clearly better for healthy people is limited."),
  ("What is the best time to take vitamin B12?", "Any time, with or without food. Many people take it in the morning, which is when it is in the Super Routine Day Pack."),
  ("Can I take B12 if I am on metformin?", "Metformin can lower B12 levels over time, so B12 is often recommended alongside it. Ask your doctor to check your levels."),
 ],
 "sources": [S_B12],
},
# ---------------------------------------------------------------- ZINC
{
 "path": ING + "zinc-picolinate/", "crumb": "Zinc Picolinate", "crumbs": ING_CRUMB, "about": "Zinc picolinate",
 "title": "Zinc Picolinate: Dose & Taking Zinc With Magnesium",
 "description": "Zinc picolinate explained: benefits, why 12 mg, the best time to take zinc, and whether you can take zinc and magnesium together.",
 "h1": "Zinc picolinate: dose, timing and taking it with magnesium",
 "answer": "Yes, <strong>most people can take zinc and magnesium together</strong> at normal doses. Very high zinc intakes (around 142 mg a day) can reduce magnesium absorption, so Super Routine keeps them apart anyway: <strong>12 mg of zinc picolinate</strong> in the Day Pack and magnesium in the Night Pack. Take zinc with food if it upsets your stomach.",
 "facts": [("Our dose", "12 mg"), ("Pack", "Day"), ("Adult RDA", "8–11 mg/day"), ("UL", "40 mg/day")],
 "body": f'''
<h2>What zinc does</h2>
<p>Zinc is a co-factor for hundreds of enzymes. It contributes to normal immune function, normal protein and DNA synthesis, normal skin, hair and nails, and normal fertility and reproduction. Diets heavy in cereals and legumes, which are common in India, contain phytates that reduce zinc absorption.</p>
<h2>Why picolinate</h2>
<p>Zinc picolinate is zinc bound to picolinic acid. A small early study found it raised zinc levels more than gluconate or citrate. The evidence is limited, but picolinate is a well-tolerated chelated form, and much better than poorly absorbed zinc oxide.</p>
<h2>Why 12 mg</h2>
<p>The adult RDA is 11 mg for men and 8 mg for women. 12 mg covers that need while staying far below the 40 mg upper limit. Doses of 50 mg or more a day over weeks can lower copper levels, which is why we avoid high-dose zinc.</p>
<h2>Can I take zinc and magnesium together?</h2>
<p>At normal supplement doses, yes. The interaction that has been measured involves very high zinc intake (around 142 mg a day), which reduced magnesium absorption. Super Routine still separates them, with zinc in the morning and {link("mg","magnesium glycinate")} at night, so the two minerals never compete.</p>
<p>Read the full guide: <a href="/science/zinc-and-magnesium-together/">Can you take zinc and magnesium together?</a></p>
<h2>Best time to take zinc</h2>
<ul><li>Zinc absorbs well on an empty stomach, but it can cause nausea. Taking it after breakfast, as in the <a href="/day-pack/">Day Pack</a>, is easier on the stomach.</li><li>Keep it away from <strong>iron supplements</strong> of 25 mg or more, which reduce zinc absorption.</li></ul>
<h2>Who should be careful</h2>
<ul><li><strong>Antibiotics</strong> (quinolones, tetracyclines): take the antibiotic 2 hours before, or 4–6 hours after, zinc.</li><li><strong>Penicillamine:</strong> separate by at least 1 hour.</li><li><strong>Thiazide diuretics</strong> increase zinc loss. Ask your doctor.</li></ul>
''',
 "faq": [
  ("Can you take zinc and magnesium together?", "Yes, at normal doses. Only very high zinc intakes (about 142 mg a day) have been shown to reduce magnesium absorption. Super Routine separates them anyway: zinc in the Day Pack, magnesium in the Night Pack."),
  ("What is the best time to take zinc?", "After a meal if it upsets your stomach, and away from iron supplements. In Super Routine it is taken after breakfast."),
  ("Is zinc picolinate better than zinc gluconate?", "A small study found picolinate raised zinc levels more. Evidence is limited, but both are well absorbed compared with zinc oxide."),
 ],
 "sources": [S_ZN, S_MG],
},
# ---------------------------------------------------------------- SHILAJIT
{
 "path": ING + "himalayan-shilajit/", "crumb": "Himalayan Shilajit", "crumbs": ING_CRUMB, "about": "Purified shilajit",
 "title": "Shilajit: Best Time to Take It, Dose & Heavy Metal Testing",
 "description": "Shilajit explained: best time to take it (morning or night), the 250 mg dose, what studies show, and why heavy-metal-tested resin matters.",
 "h1": "Himalayan shilajit: best time to take it, dose and purity",
 "answer": "Shilajit is traditionally taken <strong>in the morning</strong>, which is how it is used in the Super Routine Day Pack: <strong>250 mg of purified resin</strong> after breakfast. Human research is early and small. The most important thing is purity: raw shilajit can contain heavy metals, so only purified, third-party-tested shilajit should be used.",
 "facts": [("Our dose", "250 mg purified"), ("Pack", "Day"), ("Studied range", "250–500 mg/day"), ("Must have", "Heavy-metal testing")],
 "body": f'''
<h2>What shilajit is</h2>
<p>Shilajit is a sticky, tar-like resin that seeps from rocks in the Himalayas. It forms over centuries from decomposed plant matter and has been used in Ayurveda for vitality for a very long time. It is rich in fulvic acid, along with compounds called dibenzo-alpha-pyrones and trace minerals.</p>
<h2>What the research shows</h2>
<p>Human research is limited. In a 2019 trial, recreationally active men took 250 mg or 500 mg of purified shilajit a day for 8 weeks. The higher dose was linked to better retention of muscle strength after a fatiguing exercise test. Other small studies have looked at energy and male hormone levels. These are early findings in small groups, so we describe shilajit as a traditional ingredient that is being studied for energy and stamina, not as a proven treatment.</p>
<h2>Shilajit: morning or night?</h2>
<p>Traditional use and most brands favour the <strong>morning</strong>, because shilajit is used for energy and vitality. There is no clinical evidence that one time is better, so consistency matters more. In Super Routine it is taken after breakfast in the <a href="/day-pack/">Day Pack</a>, with {link("d3","vitamin D3 + K2")}, {link("b12","B12")} and {link("zn","zinc")}.</p>
<h2>Purity: the part that matters most</h2>
<p>Raw or poorly processed shilajit can contain <strong>lead, arsenic, mercury and cadmium</strong>, along with fungal contamination. Our specification for shilajit is no detectable lead, arsenic, mercury, cadmium or thallium. Each batch will be tested by an independent laboratory before release, and the results will be published on this site.</p>
<h2>Who should avoid it</h2>
<ul><li>Pregnant or breastfeeding women, and children.</li><li>Anyone with a medical condition, or taking any medicine: ask your doctor first.</li><li>Stop taking it and see a doctor if you notice any unusual symptoms.</li></ul>
''',
 "faq": [
  ("Should shilajit be taken in the morning or at night?", "Traditionally in the morning, because it is used for energy and vitality. No study shows one time is better. In Super Routine it is in the morning Day Pack."),
  ("How much shilajit should I take?", "Human studies have used 250–500 mg a day of purified shilajit. Super Routine contains 250 mg."),
  ("Is shilajit safe?", "Only purified, lab-tested shilajit should be used, because raw resin can contain heavy metals. Avoid it if you are pregnant or breastfeeding, and speak to your doctor if you have a medical condition or take medicines."),
 ],
 "sources": [S_SHIL_T, S_SHIL_W],
},
# ---------------------------------------------------------------- ABOUT
{
 "path": "/about/", "crumb": "About", "priority": "0.7", "schema_type": "AboutPage", "person": True, "byline": False,
 "title": "About Super Routine – Founded by Shubham Pasalkar",
 "description": "Super Routine was founded by Shubham Pasalkar. Our standards, how we choose doses and forms, and our testing plan.",
 "h1": "About Super Routine",
 "answer": "Super Routine is a day and night supplement system being built in India by founder <strong>Shubham Pasalkar</strong>. Eight essentials, two sachets, every dose on the pack, and no proprietary blends.",
 "body": '''
<h2 id="founder">The founder</h2>
<p>Shubham Pasalkar started Super Routine to solve a simple problem: people trying to look after their health were buying eight separate jars, guessing at doses and timing, and paying around ₹3,000 a month to do it. Super Routine puts the same essentials into one Day sachet and one Night sachet, at clear, studied doses.</p>
<p>Shubham writes and reviews every ingredient page on this site.</p>
<h2>Our standards</h2>
<ul>
<li><strong>Clean:</strong> only what is necessary, with no fillers or extras.</li>
<li><strong>Transparent:</strong> every ingredient, form and amount is on the pack. No proprietary blends.</li>
<li><strong>Evidence-led:</strong> doses and forms come from published human studies and from intake levels set by health authorities.</li>
<li><strong>Honest:</strong> we say what each nutrient does and what it does not. We do not claim to treat, cure or prevent any disease.</li>
</ul>
<h2>How we write and review content</h2>
<p>Every ingredient page is based on primary sources such as the NIH Office of Dietary Supplements and peer-reviewed studies, which are linked at the bottom of each page. Each page states the dose, form and timing, who should not take the ingredient, and its known interactions with medicines. Pages are reviewed whenever the science or our formula changes.</p>
<h2>Testing</h2>
<p>Before the first drop, each batch will be tested by an independent laboratory for identity, content and contaminants, including heavy metals in shilajit. Results will be published for founding members.</p>
<h2>Where we are now</h2>
<p>We are building in public. The research and formulation are in progress, and testing and the Founding Drop come next. <a href="/#join">Join the founding list</a> to follow along and vote on what we make next.</p>
''',
 "sources": [],
},
]

# ================================================================ SCIENCE ARTICLES
# Each article: "blurb" is shown on the /science/ hub. Newest first.
SCI = "/science/"
SCI_CRUMB = [("Science", SCI)]

SCIENCE = [
# ---------------------------------------------------------------- BEST SUPPLEMENTS FOR NIGHT
{
 "path": SCI + "best-supplements-for-night/", "crumb": "Best Supplements for Night", "crumbs": SCI_CRUMB,
 "schema_type": "Article", "published": "2026-10-22", "about": "Supplements taken at night",
 "blurb": "Melatonin, magnesium, ashwagandha, L-theanine, valerian and more: what the evidence says, what to avoid, and which nutrients simply suit the evening.",
 "title": "Best Supplements to Take at Night: An Honest Evidence Guide",
 "description": "The best supplements to take at night, ranked by evidence: melatonin, magnesium, ashwagandha, L-theanine, valerian, chamomile. Doses, safety and who should avoid them.",
 "h1": "Best supplements to take at night: an honest evidence guide",
 "answer": "The best-supported supplements to take at night are <strong>melatonin</strong> (for jet lag and a late body clock), <strong>ashwagandha</strong> (small benefits for sleep quality in trials), <strong>L-theanine</strong> and <strong>magnesium</strong> (limited but promising evidence). Valerian and chamomile have weak evidence, and kava carries a liver risk. Start with sleep habits; supplements are a support, not a fix.",
 "facts": [("Strongest evidence", "Melatonin (jet lag, late body clock)"), ("Avoid", "Kava (liver injury reports)"), ("Mg upper limit", "350 mg/day (supplements)"), ("First-line for insomnia", "CBT-I, not supplements")],
 "body": f'''
<p>Search "best supplements for night" and you will find shopping lists. This guide is different: it ranks the common night-time supplements by what the research actually shows, using the NIH's National Center for Complementary and Integrative Health (NCCIH), the NIH Office of Dietary Supplements and recent meta-analyses. Some popular options do well. Some do not. One is a safety concern.</p>
<p>A quick word first. If you have had trouble sleeping for months, the recommended first step is not a supplement. NCCIH notes that the American College of Physicians strongly recommends cognitive behavioural therapy for insomnia (CBT-I) as the initial treatment for chronic insomnia. A consistent bedtime, a dark room and fewer late screens help any supplement work better.</p>
<h2>Best supplements to take at night: the evidence at a glance</h2>
<div class="tw"><table><thead><tr><th>Supplement</th><th>What the evidence says</th><th>Typical studied dose</th><th>Main caution</th></tr></thead><tbody>
<tr><td>{link("mel","Melatonin")}</td><td>Helps jet lag and a delayed body clock; weak for chronic insomnia</td><td>Ours is 3 mg, 1 hour or less before bed</td><td>Epilepsy, blood thinners, pregnancy, dementia</td></tr>
<tr><td>{link("ash","Ashwagandha")}</td><td>Small but significant benefit for sleep in a meta-analysis</td><td>250–600 mg/day root extract, 6–12 weeks</td><td>Pregnancy, thyroid medicine, liver problems</td></tr>
<tr><td>L-theanine</td><td>Small improvements in self-reported sleep quality and sleep onset</td><td>Varies by study</td><td>Few studies on pure L-theanine</td></tr>
<tr><td>{link("mg","Magnesium")}</td><td>Very little, low-quality research; may help sleep onset in older adults</td><td>Stay under 350 mg/day from supplements</td><td>Kidney disease, some antibiotics</td></tr>
<tr><td>Valerian</td><td>Inconsistent trial results; benefit not shown</td><td>Varies</td><td>Long-term safety uncertain</td></tr>
<tr><td>Chamomile</td><td>No conclusive trial evidence</td><td>Usually as tea</td><td>Ragweed allergy</td></tr>
<tr><td>Kava</td><td>Very little research for sleep</td><td>Not recommended</td><td>Linked to serious liver injury</td></tr>
</tbody></table></div>
<h2>1. Melatonin: best for jet lag and a late body clock</h2>
<p>Melatonin is the hormone that tells your body clock it is night. It is the most studied night-time supplement, but what it helps with is specific.</p>
<ul>
<li><strong>Delayed sleep timing:</strong> in a 2018 trial of 307 people cited by NCCIH, melatonin taken 1 hour before a set bedtime helped people fall asleep about 34 minutes earlier.</li>
<li><strong>Jet lag:</strong> research suggests it may help, from small studies of eastward and westward travel.</li>
<li><strong>Chronic insomnia:</strong> NCCIH says there is not enough strong evidence, and sleep medicine guidelines have recommended against it for that use.</li>
</ul>
<p>Short-term use appears to be safe for most people; long-term safety is not established. Mild side effects include headache, dizziness, nausea and sleepiness. People with epilepsy and those taking blood thinners need medical supervision, guidelines recommend against it in dementia, and there is little safety research in pregnancy or breastfeeding. Melatonin may stay active longer in older people and cause daytime drowsiness.</p>
<p>Label accuracy matters too. NCCIH reports that in a 2023 study, 22 of 25 melatonin gummies were inaccurately labelled, with 74% to 347% of the stated amount. Choose one clearly labelled product and never stack two.</p>
<h2>2. Ashwagandha: modest benefit after several weeks</h2>
<p>According to the NIH Office of Dietary Supplements, a 2021 meta-analysis of 5 studies (372 adults) found a small but significant benefit of ashwagandha over placebo for sleep. Doses were 250–600 mg a day of KSM-66 root extract (or 120 mg of another extract) for 6–12 weeks. Benefits were greater at 600 mg a day, with at least 8 weeks of use, and in people with insomnia.</p>
<p>It appears well tolerated for up to about 3 months; long-term safety is unknown. Avoid it in pregnancy and breastfeeding. Rare liver injury has been reported, small studies found changes in thyroid hormone levels, and it may interact with thyroid medicine, sedatives, diabetes and blood pressure medicines, and immunosuppressants. More in our {link("ash","ashwagandha KSM-66 guide")}.</p>
<h2>3. L-theanine: calm without sedation</h2>
<p>L-theanine is an amino acid found in tea. A 2025 meta-analysis in <em>Sleep Medicine Reviews</em> (19 articles, 897 participants) found it improved self-reported time to fall asleep, daytime dysfunction and overall sleep quality, though the effects were small and the authors noted a lack of studies on pure L-theanine. Promising, not proven.</p>
<h2>4. Magnesium: useful nutrient, unproven sleep aid</h2>
<p>Magnesium is often sold as a sleep supplement, but NCCIH says very little research exists: one review suggested it may help sleep onset in older adults, from low-quality studies, and another found conflicting results. Where magnesium earns its place is as a nutrient. Adults need 310–420 mg a day from food and supplements combined, and many people take it in the evening simply because it fits a wind-down routine.</p>
<p>Keep supplemental magnesium under <strong>350 mg a day</strong>; high doses often cause diarrhoea. Take tetracycline or quinolone antibiotics at least 2 hours before or 4–6 hours after magnesium, and separate bisphosphonates by 2 hours. People with kidney problems should not take it without medical advice. The glycinate form is gentle on the stomach; see {link("mg","magnesium glycinate explained")}.</p>
<h2>5. Valerian, chamomile and lavender</h2>
<p>These are traditional favourites with thin evidence. NCCIH says valerian trial results are inconsistent and its value for insomnia has not been shown. Chamomile has no conclusive trial evidence, and people allergic to ragweed may react to it. Lavender aromatherapy improved sleep quality in a review of 16 studies, but larger, more rigorous trials are needed. A cup of chamomile tea as part of a routine is fine; just do not expect it to do much on its own.</p>
<h2>Night supplements to avoid or use with care</h2>
<ul>
<li><strong>Kava:</strong> NCCIH says it has been linked to liver injury that is sometimes serious or even fatal. We do not recommend it.</li>
<li><strong>L-tryptophan and 5-HTP:</strong> data for insomnia are very limited, and L-tryptophan may cause serotonin toxicity with medicines that affect serotonin, such as some antidepressants.</li>
<li><strong>CBD:</strong> there is insufficient evidence for any sleep disorder, and it can cause liver injury and drug interactions.</li>
<li><strong>Multiple "sleep blends" at once:</strong> many contain melatonin, so doses add up. See <a href="/science/supplements-not-to-take-together/">supplements not to take together</a>.</li>
</ul>
<h2>Nutrients that simply suit the evening</h2>
<p>Not every night-time supplement is about sleep. {link("om","Omega-3")} (EPA and DHA) is a component of every cell membrane and can be taken at any time; taking it with dinner fits many routines. Its usual side effects are mild, such as an unpleasant taste or heartburn, but high doses may cause bleeding problems with warfarin or other anticoagulants, so tell your doctor if you take one.</p>
<h2>How the Super Routine Night Pack fits</h2>
<p>We built the <a href="/night-pack/">Night Pack</a> from the evening options with the most sensible evidence and safety profile, at clearly labelled doses, in one sachet taken after dinner or 30–60 minutes before bed:</p>
{cards(NIGHT)}
<p>To be clear about what that means: our 3 mg of melatonin is a common adult dose, best suited to resetting a late body clock; our 300 mg of ashwagandha sits inside the studied 250–600 mg range, though the larger trial benefits were seen at 600 mg; and our 140 mg of elemental magnesium is a nutrient top-up well under the 350 mg limit, not a sedative. There is no kava, valerian or proprietary blend. Morning nutrients such as vitamin D3, B12 and zinc are in the separate <a href="/day-pack/">Day Pack</a>, and our <a href="/">Super Routine home page</a> explains the full day and night system.</p>
<p>Do not take the Night Pack with another melatonin product, and do not drive after taking it. If you are pregnant, breastfeeding, under 18, have epilepsy or a liver, kidney or thyroid condition, or take blood thinners, sedatives or other regular medicines, ask your doctor or pharmacist first.</p>
''',
 "faq": [
  ("What is the best supplement to take at night for sleep?", "Melatonin has the clearest evidence, but mainly for jet lag and a late body clock. For general sleep quality, ashwagandha and L-theanine show small benefits in trials. For long-term insomnia, CBT-I is the recommended first step."),
  ("Is it good to take magnesium at night?", "Many people take magnesium in the evening because it fits a wind-down routine, and absorption does not depend on time of day. Evidence that it improves sleep is limited. Keep supplemental magnesium under 350 mg a day."),
  ("Can I take melatonin and ashwagandha together?", "They are often combined in the evening. Both can cause drowsiness, so do not add sedatives or alcohol, and ask your doctor first if you take any regular medicine, have a thyroid condition or are pregnant."),
  ("Which sleep supplements should I avoid?", "Avoid kava because of reports of serious liver injury, avoid L-tryptophan if you take medicines that affect serotonin, and do not take two products that both contain melatonin."),
 ],
 "sources": [S_MEL,
   ("NCCIH (NIH): Sleep disorders and complementary health approaches", "https://www.nccih.nih.gov/health/sleep-disorders-and-complementary-health-approaches"),
   S_ASH, S_MG,
   ("NIH Office of Dietary Supplements: Omega-3 fatty acids (consumer fact sheet)", "https://ods.od.nih.gov/factsheets/Omega3FattyAcids-Consumer/"),
   ("Bulman et al. (2025), Sleep Medicine Reviews: L-theanine and sleep outcomes, systematic review and meta-analysis", "https://doi.org/10.1016/j.smrv.2025.102076")],
},
# ---------------------------------------------------------------- 7 COMBINATIONS
{
 "path": SCI + "supplements-not-to-take-together/", "crumb": "Supplements Not to Take Together", "crumbs": SCI_CRUMB,
 "schema_type": "Article", "published": "2026-10-21",
 "blurb": "Calcium and iron, iron and zinc, high-dose zinc, melatonin stacks, blood thinners and double-dosing: what to separate and by how long.",
 "title": "7 Supplements You Should Not Take Together (and What to Do)",
 "description": "A list of 7 supplement combinations to separate or avoid, with spacing times, upper limits and the medicines that interact with minerals.",
 "h1": "7 supplements you should not take together",
 "answer": "The main combinations to separate or avoid are <strong>calcium with iron</strong>, <strong>iron with zinc</strong>, <strong>high-dose zinc with copper or magnesium</strong>, <strong>melatonin with other sleep products</strong>, <strong>omega-3 or vitamin K with blood thinners</strong>, and <strong>two products with the same nutrient</strong>. Most can still be taken on the same day if you space them a few hours apart.",
 "facts": [("Most common clash", "Calcium + iron"), ("Zinc upper limit", "40 mg/day"), ("Mg upper limit", "350 mg/day (supplements)"), ("Vitamin D upper limit", "4,000 IU/day")],
 "body": f'''
<p>"Not together" rarely means "never". For most of the pairs below the problem is competition for absorption in the gut, which you solve by taking them at different times of day. A few are about safety, where the answer is to talk to your doctor first. Here is each combination, why it matters and what to do.</p>
<h2>Quick reference: which supplements not to take together</h2>
<div class="tw"><table><thead><tr><th>Combination</th><th>Why</th><th>What to do</th></tr></thead><tbody>
<tr><td>1. Calcium + iron</td><td>Calcium might reduce iron absorption</td><td>Take at different times of day</td></tr>
<tr><td>2. Iron (25 mg+) + zinc</td><td>Iron reduces zinc absorption</td><td>Take at different times of day</td></tr>
<tr><td>3. High-dose zinc + copper status</td><td>50 mg+ zinc for weeks inhibits copper absorption</td><td>Keep zinc under 40 mg a day</td></tr>
<tr><td>4. Very high-dose zinc + magnesium</td><td>142 mg zinc a day might reduce magnesium absorption</td><td>Normal doses are fine; splitting is optional</td></tr>
<tr><td>5. Melatonin + other sleep products</td><td>Stacked doses, uncertain label content</td><td>Use one melatonin product only</td></tr>
<tr><td>6. Omega-3 or vitamin K + blood thinners</td><td>Can change clotting tests (INR)</td><td>Only with your doctor's agreement</td></tr>
<tr><td>7. Two products with the same nutrient</td><td>Can push you over the upper limit</td><td>Add up every label</td></tr>
</tbody></table></div>
<h2>1. Calcium and iron</h2>
<p>This is the pairing most people have heard of. The NIH Office of Dietary Supplements says calcium <em>might</em> interfere with iron absorption, although the effect has not been definitively established, and experts suggest taking individual calcium and iron supplements at different times of the day. A simple routine is iron in the morning and calcium with dinner, or the other way round.</p>
<p>Calcium absorbs best in small amounts: absorption from supplements is highest at doses of 500 mg or less. If you take more, split it across meals rather than taking it all at once.</p>
<h2>2. Iron and zinc</h2>
<p>Iron tablets of <strong>25 mg of elemental iron or more</strong>, taken at the same time as zinc, can reduce zinc absorption. The iron added to fortified foods does not have a significant effect. If you have been prescribed iron, take it at a different time from any zinc supplement. With Super Routine, that means taking your iron away from the <a href="/day-pack/">Day Pack</a>, which contains {link("zn","12 mg of zinc")}.</p>
<h2>3. High-dose zinc and copper</h2>
<p>Zinc and copper share an absorption pathway. Doses of <strong>50 mg of zinc or more over a period of weeks</strong> can inhibit copper absorption and lead to low copper status. This is one reason the adult upper limit for zinc is 40 mg a day. Long courses of high-dose "immunity" zinc are the usual way people get there. Stay under 40 mg a day from all supplements combined unless a doctor has prescribed more.</p>
<h2>4. Very high-dose zinc and magnesium</h2>
<p>Very high zinc intakes from supplements, around <strong>142 mg a day</strong>, might interfere with magnesium absorption. That is more than three times the zinc upper limit. At ordinary doses the two are commonly taken together. We cover this in detail in <a href="/science/zinc-and-magnesium-together/">Can you take zinc and magnesium together?</a> Super Routine still keeps them apart, with zinc in the morning and {link("mg","magnesium glycinate")} at night, so the question never comes up.</p>
<h2>5. Melatonin and other sleep products</h2>
<p>Melatonin appears in many sleep gummies, drinks and "night" blends, so it is easy to take two products that both contain it. Label accuracy is a real issue: NCCIH reports that in a 2023 study of melatonin gummies, the actual amount ranged from <strong>74% to 347%</strong> of the labelled quantity. Stacking products multiplies that uncertainty.</p>
<p>Use one melatonin product only. The Super Routine <a href="/night-pack/">Night Pack</a> already contains {link("mel","3 mg of melatonin")}, so do not add a separate melatonin supplement. NCCIH advises anyone taking medicine to speak to their health care provider before using melatonin, and says people with epilepsy and those on blood thinners need medical supervision. {link("ash","Ashwagandha")} might also interact with sedative medicines, so if you take a prescribed sleeping tablet or sedative, ask your doctor before adding either.</p>
<h2>6. Omega-3 or vitamin K with blood thinners</h2>
<p>This one is a supplement-and-medicine pairing, but it is the most important on the list.</p>
<ul>
<li><strong>Vitamin K and warfarin:</strong> people on warfarin need a consistent vitamin K intake from food and supplements, because sudden changes can increase or decrease the drug's effect. Do not start a product with vitamin K2, such as {link("d3","our vitamin D3 + K2")}, without your doctor's approval.</li>
<li><strong>Omega-3 and anticoagulants:</strong> fish oil might prolong clotting time (raise INR). Most research found 3–6 g a day does not significantly affect anticoagulant status, but the NIH advises that people taking omega-3 with anticoagulants are monitored periodically. Tell your doctor before taking {link("om","omega-3")}.</li>
</ul>
<h2>7. Two products that contain the same nutrient</h2>
<p>The most common "combination" problem is not two different nutrients. It is the same nutrient from two products: a multivitamin, an immunity tablet and a separate zinc or vitamin D supplement. Vitamin D is the clearest example. The adult upper limit is <strong>4,000 IU a day</strong>, and according to the NIH, vitamin D toxicity is almost always the result of excessive intake from supplements. If your doctor has prescribed high-dose vitamin D, follow that plan and tell them about any other vitamin D you take.</p>
<div class="tw"><table><thead><tr><th>Nutrient</th><th>Adult upper limit</th><th>Super Routine dose</th></tr></thead><tbody>
<tr><td>Zinc</td><td>40 mg/day</td><td>12 mg</td></tr>
<tr><td>Magnesium (from supplements)</td><td>350 mg/day</td><td>140 mg elemental</td></tr>
<tr><td>Vitamin D</td><td>4,000 IU/day</td><td>600 IU</td></tr>
<tr><td>Iron</td><td>45 mg/day</td><td>None</td></tr>
<tr><td>Calcium</td><td>2,000–2,500 mg/day</td><td>None</td></tr>
</tbody></table></div>
<h2>Minerals and common medicines</h2>
<p>Minerals also bind to some medicines in the gut. These timings come from the NIH fact sheets:</p>
<ul>
<li><strong>Quinolone and tetracycline antibiotics</strong> (such as ciprofloxacin or doxycycline): take the antibiotic at least 2 hours before, or 4–6 hours after, zinc or magnesium. For calcium and quinolones, 2 hours before or after.</li>
<li><strong>Levothyroxine (thyroid medicine):</strong> do not take it within 4 hours of calcium carbonate or iron supplements.</li>
<li><strong>Bisphosphonates</strong> (such as alendronate): separate from magnesium by at least 2 hours.</li>
<li><strong>Levodopa:</strong> iron supplements reduce its absorption.</li>
</ul>
<h2>How Super Routine is built around these rules</h2>
<p>We designed the two packs so the clashes above do not happen inside the routine. Zinc is in the Day Pack and magnesium in the Night Pack. Neither pack contains iron or calcium, so neither competes with a prescribed iron or calcium tablet if you space them. Melatonin is only in the Night Pack, and every dose stays below its upper limit. See the full list on our <a href="/ingredients/">ingredients page</a>.</p>
''',
 "faq": [
  ("What vitamins should not be taken together?", "The main ones to separate are calcium and iron, iron (25 mg or more) and zinc, and high-dose zinc with copper or magnesium. Also avoid taking two products that both contain vitamin D, zinc or melatonin, because the doses add up."),
  ("How far apart should I take iron and calcium?", "Experts suggest taking them at different times of day, for example iron in the morning and calcium with dinner."),
  ("Can I take all my vitamins at once?", "Many can be taken together, but minerals that compete, such as iron with calcium or zinc, are better spaced out. Fat-soluble vitamins such as D and K absorb best with a meal."),
  ("Which supplements interact with blood thinners?", "Vitamin K can change the effect of warfarin, and fish oil can raise INR. Anyone on a blood thinner should ask their doctor before starting either."),
 ],
 "sources": [S_FE, S_CA, S_ZN, S_MG, S_K, S_OM, S_D, S_MEL, S_ASH],
},
# ---------------------------------------------------------------- ZINC + MAGNESIUM
{
 "path": SCI + "zinc-and-magnesium-together/", "crumb": "Zinc and Magnesium Together", "crumbs": SCI_CRUMB,
 "schema_type": "Article", "published": "2026-10-21",
 "blurb": "Yes at normal doses. The 142 mg zinc threshold, safe upper limits, the best time to take each, and the medicines to space them from.",
 "title": "Can You Take Zinc and Magnesium Together? Doses & Timing",
 "description": "Yes, at normal doses. We explain the 142 mg zinc threshold, safe upper limits, the best time to take zinc and magnesium, and medicines to space.",
 "h1": "Can you take zinc and magnesium together?",
 "answer": "<strong>Yes.</strong> For most healthy adults, zinc and magnesium can be taken together at normal doses. The interaction that has been measured involves very high zinc intakes of about <strong>142 mg a day</strong>, more than three times the 40 mg upper limit. Keep zinc under 40 mg, supplemental magnesium under 350 mg, and space both from certain antibiotics.",
 "facts": [("Together?", "Yes, at normal doses"), ("Problem dose", "Zinc ~142 mg/day"), ("Zinc upper limit", "40 mg/day"), ("Mg upper limit", "350 mg/day (supplements)")],
 "body": f'''
<h2>Why people worry about zinc and magnesium together</h2>
<p>Zinc and magnesium are both minerals absorbed in the small intestine, so it is reasonable to ask whether they compete. The NIH Office of Dietary Supplements gives a clear threshold: <strong>very high doses of zinc from supplements (142 mg a day) might interfere with magnesium absorption</strong>. Typical supplements contain 8–25 mg of zinc, nowhere near that level.</p>
<p>The two are also given together in research. In a 12-week randomised, placebo-controlled trial, 55 adults took 250 mg of magnesium and 30 mg of elemental zinc together every day, and the authors reported no adverse effects from the combination.</p>
<h2>What zinc and magnesium each do</h2>
<p>They are often sold together, but they do different jobs.</p>
<ul>
<li><strong>Zinc</strong> is a co-factor for hundreds of enzymes. It contributes to normal immune function, protein and DNA synthesis, wound healing and cell division. Whole grains, beans and nuts contain phytates, which bind zinc in the gut and reduce how much is absorbed, a point worth knowing for many Indian vegetarian diets.</li>
<li><strong>Magnesium</strong> is involved in more than 300 enzyme systems. It contributes to normal muscle and nerve function, protein synthesis and energy production.</li>
</ul>
<p>Because their roles do not overlap, there is no reason to choose one over the other. The question is only how much of each, and when.</p>
<h2>How much zinc and magnesium is safe to take together?</h2>
<p>Stay within the daily upper limits for both, counting every product you take.</p>
<div class="tw"><table><thead><tr><th></th><th>Zinc</th><th>Magnesium</th></tr></thead><tbody>
<tr><td>Adult RDA</td><td>11 mg men, 8 mg women</td><td>400–420 mg men, 310–320 mg women</td></tr>
<tr><td>Upper limit</td><td>40 mg/day (all sources)</td><td>350 mg/day from supplements and medicines only</td></tr>
<tr><td>Signs of too much</td><td>Nausea, dizziness, headache, stomach upset, vomiting, loss of appetite</td><td>Diarrhoea, nausea, abdominal cramps</td></tr>
<tr><td>In Super Routine</td><td>{link("zn","12 mg picolinate")} (Day Pack)</td><td>{link("mg","140 mg elemental, as glycinate")} (Night Pack)</td></tr>
</tbody></table></div>
<p>Two details are easy to miss. The magnesium upper limit counts only supplements and medicines, not magnesium from food. And on a label, "1000 mg magnesium glycinate" is the whole compound: the elemental magnesium is about 140 mg. Always compare elemental amounts.</p>
<h2>Watch for hidden zinc</h2>
<p>Most people who exceed the zinc limit do it by stacking products: a multivitamin, an immunity tablet and a separate zinc supplement. Some nasal sprays, homeopathic products and denture creams also contain zinc. Long-term intakes of <strong>50 mg of zinc a day or more</strong> can inhibit copper absorption, which is a separate reason to keep total zinc under 40 mg. Read more in <a href="/science/supplements-not-to-take-together/">7 supplements you should not take together</a>.</p>
<h2>Best time to take zinc and magnesium</h2>
<div class="tw"><table><thead><tr><th>Option</th><th>How</th><th>Suits</th></tr></thead><tbody>
<tr><td>Together</td><td>Both with a meal</td><td>The simplest routine. Fine at normal doses.</td></tr>
<tr><td>Split</td><td>Zinc after breakfast, magnesium in the evening</td><td>Anyone who wants to avoid any competition, or finds zinc hard on the stomach</td></tr>
</tbody></table></div>
<ul>
<li><strong>Zinc:</strong> can cause stomach upset and nausea, so many people take it after a meal. Keep it apart from iron supplements of 25 mg or more, which reduce zinc absorption.</li>
<li><strong>Magnesium:</strong> absorption does not depend on time of day. Many people take it in the evening as part of a wind-down routine. Forms that dissolve well, such as citrate, chloride and lactate, tend to be absorbed better than oxide. Glycinate is gentle on the stomach.</li>
</ul>
<h2>Should you split them anyway?</h2>
<p>You do not have to, but splitting has practical advantages. It removes any question of competition, it keeps a zinc-related upset stomach away from bedtime, and it fits how people already live: one routine in the morning and one in the evening. That is how Super Routine is built. The <a href="/day-pack/">Day Pack</a> holds zinc with vitamin D3 + K2, B12 and shilajit after breakfast. The <a href="/night-pack/">Night Pack</a> holds magnesium glycinate with ashwagandha, omega-3 and melatonin after dinner.</p>
<h2>Who should be careful</h2>
<ul>
<li><strong>Antibiotics</strong> (quinolones such as ciprofloxacin, tetracyclines such as doxycycline): take the antibiotic at least 2 hours before, or 4–6 hours after, zinc or magnesium.</li>
<li><strong>Penicillamine:</strong> take zinc at least 1 hour apart from it.</li>
<li><strong>Bisphosphonates</strong> (such as alendronate): separate from magnesium by at least 2 hours.</li>
<li><strong>Diuretics:</strong> thiazide diuretics increase zinc loss in urine, and loop and thiazide diuretics increase magnesium loss. Potassium-sparing diuretics reduce magnesium excretion. Ask your doctor before adding either mineral.</li>
<li><strong>Long-term proton pump inhibitors</strong> (usually more than a year) can lower magnesium levels.</li>
<li>If you are pregnant, breastfeeding, have a medical condition or take any regular medicine, check with your doctor or pharmacist first.</li>
</ul>
''',
 "faq": [
  ("Is it safe to take zinc and magnesium every day?", "For most healthy adults, yes, if total zinc stays under 40 mg a day and magnesium from supplements stays under 350 mg a day. Check with your doctor if you have a medical condition or take regular medicines."),
  ("Can I take zinc and magnesium at night?", "Yes. Magnesium is often taken in the evening. Some people find zinc unsettles the stomach, so if that happens, take zinc after breakfast instead."),
  ("What should you not take with zinc?", "Iron supplements of 25 mg or more, quinolone and tetracycline antibiotics, and penicillamine all need spacing from zinc. Long-term doses of 50 mg or more can lower copper levels."),
  ("Does zinc block magnesium absorption?", "Only at very high doses. The NIH notes that about 142 mg of zinc a day might interfere with magnesium absorption. Normal supplement doses have not been shown to do this."),
 ],
 "sources": [S_ZN, S_MG, S_FE, S_HAM],
},
]


def _sci_cards():
    return '<div class="cards">' + "".join(
        f'<a class="card" href="{a["path"]}"><strong>{a["h1"][0].upper() + a["h1"][1:]}</strong><span>{a["blurb"]}</span></a>'
        for a in SCIENCE) + "</div>"


SCIENCE_HUB = {
 "path": SCI, "crumb": "Science", "priority": "0.8", "schema_type": "CollectionPage",
 "title": "Supplement Science: Timing, Combinations & Safety Guides",
 "description": "Guides on supplement timing, which supplements to take together or apart, doses, upper limits and interactions, with sources.",
 "h1": "Supplement science, explained simply",
 "answer": "Practical guides to taking supplements well: which ones go together, which to space apart, when to take them and how much is safe. Every article is written and reviewed by founder Shubham Pasalkar and links to its sources, mainly the NIH Office of Dietary Supplements and peer-reviewed studies.",
 "body": f'''
<h2>All articles</h2>
{_sci_cards()}
<h2>Ingredient guides</h2>
<p>For dose, form and timing of each Super Routine ingredient, see the <a href="/ingredients/">ingredients hub</a>, the <a href="/day-pack/">Day Pack</a> and the <a href="/night-pack/">Night Pack</a>.</p>
''',
 "sources": [],
}

PAGES = PAGES + [SCIENCE_HUB] + SCIENCE

# ================================================================ BRAND FAQ
FAQ_PAGE = {
 "path": "/faq/", "crumb": "FAQ", "priority": "0.9", "schema_type": "WebPage", "about": "Super Routine supplements",
 "title": "Super Routine FAQ: Price, Sachets & Day and Night Supplements",
 "description": "Super Routine FAQ: what is in the Super Routine day and night sachets, the Super Routine price (₹1,200/month founding price), how to take them and who should avoid them.",
 "h1": "Super Routine FAQ: price, sachets and day and night supplements",
 "answer": "<strong>Super Routine</strong> is an Indian day and night supplement system: one Day sachet after breakfast and one Night sachet after dinner, with eight essentials at clearly labelled doses. The founding <strong>Super Routine price is ₹1,200 a month</strong> for 30 Day and 30 Night sachets. It is in pre-launch, so you can join the founding waitlist now.",
 "facts": [("Price", "₹1,200/month (founding)"), ("Sachets", "30 Day + 30 Night"), ("Day", "After breakfast"), ("Night", "After dinner / before bed")],
 "body": f'''
<p>These are the questions people ask most about Super Routine supplements. If you searched for "superroutine" or "superoutine", you are in the right place: Super Routine is the brand, and superroutine.in is its only official website. Founded by Shubham Pasalkar.</p>
<h2>What is in the Super Routine day and night sachets?</h2>
<div class="tw"><table><thead><tr><th>Sachet</th><th>Nutrient</th><th>Dose</th><th>When</th></tr></thead><tbody>
<tr><td rowspan="4"><a href="/day-pack/">Day sachet</a></td><td>{link("d3","Vitamin D3 + K2")}</td><td>600 IU D3 + K2</td><td rowspan="4">After breakfast</td></tr>
<tr><td>{link("b12","Vitamin B12 (methylcobalamin)")}</td><td>1 mg</td></tr>
<tr><td>{link("zn","Zinc picolinate")}</td><td>12 mg</td></tr>
<tr><td>{link("shil","Purified Himalayan shilajit")}</td><td>250 mg</td></tr>
<tr><td rowspan="4"><a href="/night-pack/">Night sachet</a></td><td>{link("mg","Magnesium glycinate")}</td><td>1000 mg (140 mg elemental)</td><td rowspan="4">After dinner or 30–60 min before bed</td></tr>
<tr><td>{link("ash","Ashwagandha KSM-66")}</td><td>300 mg</td></tr>
<tr><td>{link("om","Omega-3 (rTG)")}</td><td>750 mg</td></tr>
<tr><td>{link("mel","Melatonin")}</td><td>3 mg</td></tr>
</tbody></table></div>
<p>Every dose is printed on the pack, with no proprietary blends. See the full <a href="/ingredients/">Super Routine ingredients list</a>.</p>
<h2>Super Routine price</h2>
<p>The founding Super Routine price is <strong>₹1,200 a month</strong> for a full month of daily supplements: 30 Day sachets and 30 Night sachets. Super Routine is in pre-launch. Founding members get first access and the founding price when it launches; 255 people have already joined the founding list. <a href="/#join">Claim your founding spot</a>.</p>
<h2>How to take Super Routine daily supplements</h2>
<ul>
<li><strong>Morning:</strong> one Day sachet after breakfast, with water. Vitamin D3 and K2 are fat-soluble, so a meal helps.</li>
<li><strong>Evening:</strong> one Night sachet after dinner or 30–60 minutes before bed. It contains melatonin, so do not drive or operate machinery afterwards.</li>
<li>Take both every day, at about the same times. Do not take more than one of each sachet a day.</li>
</ul>
<h2>Why Super Routine is split into day and night</h2>
<p>Timing matters for some nutrients. Melatonin signals night to the body clock, so it belongs in the evening, and magnesium fits a wind-down routine. Zinc sits in the Day sachet and magnesium in the Night sachet so the two minerals are not taken together. Read more in <a href="/science/zinc-and-magnesium-together/">zinc and magnesium together</a> and our guide to the <a href="/science/best-supplements-for-night/">best supplements to take at night</a>.</p>
<h2>Who should not take Super Routine</h2>
<ul>
<li>Anyone pregnant or breastfeeding, or under 18.</li>
<li>People with epilepsy, or taking blood thinners such as warfarin: melatonin needs medical supervision, and high doses of omega-3 may cause bleeding problems with anticoagulants.</li>
<li>People taking thyroid medicine, sedatives, diabetes or blood pressure medicines, or immunosuppressants: ashwagandha may interact with them.</li>
<li>People with liver problems (rare liver injury has been reported with ashwagandha) or kidney disease (the risk of magnesium build-up is higher).</li>
<li>If you take antibiotics such as doxycycline or ciprofloxacin, take them at least 2 hours before, or 4–6 hours after, the Night sachet.</li>
</ul>
<p>If any of these apply, or you take any regular medicine, ask your doctor before starting.</p>
''',
 "faq": [
  ("What is Super Routine?", "Super Routine is an Indian day and night supplement system founded by Shubham Pasalkar. One Day sachet after breakfast and one Night sachet after dinner deliver eight essentials at clearly labelled doses."),
  ("What is the Super Routine price?", "The founding price is ₹1,200 a month for 30 Day and 30 Night sachets. Super Routine is in pre-launch; join the founding waitlist on superroutine.in to get first access at that price."),
  ("What is in Super Routine sachets?", "The Day sachet has vitamin D3 600 IU with K2, vitamin B12 1 mg, zinc picolinate 12 mg and purified shilajit 250 mg. The Night sachet has magnesium glycinate 1000 mg (140 mg elemental), ashwagandha KSM-66 300 mg, omega-3 rTG 750 mg and melatonin 3 mg."),
  ("Are Super Routine daily vitamins or supplements?", "Both. The Day sachet contains vitamins D3, K2 and B12 plus zinc and shilajit; the Night sachet contains magnesium, ashwagandha, omega-3 and melatonin. Together they are daily food supplements, not medicines."),
  ("When should I take Super Routine day and night sachets?", "Take the Day sachet after breakfast and the Night sachet after dinner or 30–60 minutes before bed, at about the same times each day."),
  ("Can I take Super Routine with other supplements?", "Do not add another melatonin product, and check that other supplements do not double up on vitamin D, zinc or magnesium. If you take any medicine, ask your doctor first."),
  ("Is SuperRoutine the same as Super Routine?", "Yes. SuperRoutine, Super Routine and superroutine.in are the same brand. superroutine.in is the only official website."),
 ],
 "sources": [S_MEL, S_ASH, S_MG,
   ("NIH Office of Dietary Supplements: Omega-3 fatty acids (consumer fact sheet)", "https://ods.od.nih.gov/factsheets/Omega3FattyAcids-Consumer/")],
}
PAGES = PAGES + [FAQ_PAGE]
