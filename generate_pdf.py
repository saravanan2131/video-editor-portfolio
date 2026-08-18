from fpdf import FPDF

class PortfolioPDF(FPDF):
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=20)

    def header(self):
        if self.page_no() > 1:
            self.set_font("Helvetica", "B", 8)
            self.set_text_color(150, 150, 170)
            self.cell(0, 8, "S. Saravana Perumal  |  Video Editor Portfolio", align="L")
            self.set_text_color(124, 58, 237)
            self.cell(0, 8, f"Page {self.page_no()}", align="R", new_x="LMARGIN", new_y="NEXT")
            self.set_draw_color(40, 40, 60)
            self.line(20, 18, 190, 18)
            self.ln(4)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "", 7)
        self.set_text_color(100, 100, 120)
        self.cell(0, 10, "starkindustries2131@gmail.com  |  +91 93443 90658  |  Tirunelveli, Tamil Nadu", align="C")

    def section_title(self, title):
        self.set_font("Helvetica", "B", 14)
        self.set_text_color(124, 58, 237)
        self.cell(0, 10, title, new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(124, 58, 237)
        self.line(20, self.get_y(), 80, self.get_y())
        self.ln(4)

    def subsection(self, title):
        self.set_font("Helvetica", "B", 11)
        self.set_text_color(230, 230, 240)
        self.cell(0, 8, title, new_x="LMARGIN", new_y="NEXT")
        self.ln(1)

    def body_text(self, text):
        self.set_font("Helvetica", "", 9)
        self.set_text_color(160, 160, 180)
        self.multi_cell(0, 5, text)
        self.ln(2)

    def bullet(self, text, bold_prefix=""):
        self.set_font("Helvetica", "", 9)
        self.set_text_color(160, 160, 180)
        x = self.get_x()
        self.cell(8, 5, "-")
        if bold_prefix:
            self.set_font("Helvetica", "B", 9)
            self.set_text_color(200, 200, 220)
            self.cell(self.get_string_width(bold_prefix) + 2, 5, bold_prefix)
            self.set_font("Helvetica", "", 9)
            self.set_text_color(160, 160, 180)
            self.multi_cell(0, 5, text)
        else:
            self.multi_cell(0, 5, text)
        self.ln(1)

    def skill_row(self, skills_list):
        col_w = 42
        cols = 4
        self.set_font("Helvetica", "", 8)
        for i, skill in enumerate(skills_list):
            self.set_fill_color(25, 25, 40)
            self.set_text_color(200, 200, 220)
            self.cell(col_w, 7, "  " + skill, border=0, fill=True)
            if (i + 1) % cols == 0:
                self.ln()
        if len(skills_list) % cols != 0:
            self.ln()
        self.ln(2)

    def project_card(self, title, ptype, desc, tags):
        self.set_fill_color(20, 20, 35)
        self.set_draw_color(40, 40, 60)
        y_start = self.get_y()
        self.rect(20, y_start, 170, 38, style="DF")
        self.set_xy(24, y_start + 3)
        self.set_font("Helvetica", "B", 10)
        self.set_text_color(230, 230, 240)
        self.cell(0, 6, title)
        self.set_xy(24, y_start + 10)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(124, 58, 237)
        self.cell(0, 5, ptype)
        self.set_xy(24, y_start + 17)
        self.set_font("Helvetica", "", 8)
        self.set_text_color(140, 140, 160)
        self.multi_cell(158, 4, desc)
        self.set_xy(24, y_start + 30)
        self.set_font("Helvetica", "", 7)
        self.set_text_color(168, 85, 247)
        self.cell(0, 5, "Tags: " + "  |  ".join(tags))
        self.set_y(y_start + 42)


pdf = PortfolioPDF()
pdf.set_margins(20, 20, 20)

# ===== COVER PAGE =====
pdf.add_page()
pdf.set_fill_color(10, 10, 15)
pdf.rect(0, 0, 210, 297, style="F")

# Accent bar
pdf.set_fill_color(124, 58, 237)
pdf.rect(0, 0, 210, 4, style="F")

# Name
pdf.set_y(60)
pdf.set_font("Helvetica", "B", 36)
pdf.set_text_color(230, 230, 240)
pdf.cell(0, 16, "S. Saravana Perumal", align="C", new_x="LMARGIN", new_y="NEXT")

# Title
pdf.set_font("Helvetica", "", 16)
pdf.set_text_color(124, 58, 237)
pdf.cell(0, 12, "Video Editor  |  Creative Content Creator", align="C", new_x="LMARGIN", new_y="NEXT")

# Divider
pdf.ln(8)
pdf.set_draw_color(124, 58, 237)
pdf.line(70, pdf.get_y(), 140, pdf.get_y())
pdf.ln(12)

# Tagline
pdf.set_font("Helvetica", "", 11)
pdf.set_text_color(160, 160, 180)
pdf.multi_cell(0, 7, "Crafting compelling short-form videos, social media content,\nand creative edits that capture attention and tell stories.", align="C")

pdf.ln(12)

# Info badges
pdf.set_font("Helvetica", "", 9)
pdf.set_text_color(180, 180, 200)
info_lines = [
    "Tirunelveli, Tamil Nadu, India",
    "starkindustries2131@gmail.com",
    "+91 93443 90658",
    "github.com/saravanan2131"
]
for line in info_lines:
    pdf.cell(0, 7, line, align="C", new_x="LMARGIN", new_y="NEXT")

pdf.ln(16)

# Bottom bar
pdf.set_fill_color(20, 20, 35)
pdf.rect(30, 200, 150, 40, style="F")
pdf.set_draw_color(40, 40, 60)
pdf.rect(30, 200, 150, 40, style="D")

pdf.set_y(204)
pdf.set_font("Helvetica", "B", 10)
pdf.set_text_color(230, 230, 240)
pdf.cell(0, 7, "Seeking: Video Editor / Junior Video Editor / Social Media Video Editor", align="C", new_x="LMARGIN", new_y="NEXT")
pdf.set_font("Helvetica", "", 9)
pdf.set_text_color(124, 58, 237)
pdf.cell(0, 7, "B.Sc Computer Science  |  Manonmaniam Sundaranar University", align="C", new_x="LMARGIN", new_y="NEXT")
pdf.set_font("Helvetica", "", 8)
pdf.set_text_color(140, 140, 160)
pdf.cell(0, 7, "2023 - 2026  |  Open to Remote & On-site Roles", align="C", new_x="LMARGIN", new_y="NEXT")


# ===== PAGE 2: ABOUT =====
pdf.add_page()
pdf.section_title("ABOUT ME")
pdf.body_text(
    "I am S. Saravana Perumal from Tirunelveli, Tamil Nadu - a passionate and fast-learning "
    "video editor with a strong foundation in computer science. I combine technical knowledge "
    "with creative storytelling to produce engaging video content."
)
pdf.body_text(
    "Currently pursuing my B.Sc in Computer Science at Manonmaniam Sundaranar University College, "
    "Govindaperi (2023-2026), I am seeking an opportunity as a Video Editor / Junior Video Editor / "
    "Social Media Video Editor to grow professionally and contribute to creative teams."
)

pdf.ln(2)
pdf.subsection("Key Attributes")
pdf.bullet("B.Sc Computer Science student with strong problem-solving skills")
pdf.bullet("Fast learner with a genuine passion for video editing and digital content")
pdf.bullet("Detail-oriented approach to transitions, timing, and visual storytelling")
pdf.bullet("Technical background that complements creative workflow efficiency")
pdf.bullet("Available for Remote, On-site, and Hybrid roles")


# ===== SKILLS =====
pdf.ln(4)
pdf.section_title("VIDEO EDITING SKILLS")
pdf.skill_row(["Short-Form Editing", "Instagram Reels", "YouTube Shorts", "Social Media Content"])
pdf.skill_row(["Transitions", "Text Overlays", "Colour Correction", "Audio / Music Sync"])
pdf.skill_row(["Storytelling", "Pacing & Timing", "Beat Matching", "Aspect Ratios"])
pdf.skill_row(["Precision Cutting", "Fast Turnaround", "Narrative Flow", "Visual Effects"])


# ===== SOFTWARE =====
pdf.ln(4)
pdf.section_title("SOFTWARE")
pdf.body_text("Tools I am actively building proficiency in:")
pdf.bullet("Video Editing Software", "Proficiency: Learning")
pdf.bullet("Adobe Premiere Pro", "Proficiency: Building")
pdf.bullet("DaVinci Resolve", "Proficiency: Building")
pdf.bullet("CapCut (Mobile & Desktop)", "Proficiency: Building")
pdf.set_font("Helvetica", "I", 8)
pdf.set_text_color(120, 120, 140)
pdf.ln(2)
pdf.cell(0, 5, "* Software expertise is actively developing. This section will be updated as proficiency grows.", new_x="LMARGIN", new_y="NEXT")


# ===== PAGE 3: PROJECTS =====
pdf.add_page()
pdf.section_title("FEATURED PROJECTS")
pdf.body_text("Sample project concepts demonstrating editing approach and creative thinking:")

pdf.project_card(
    "Trending Reel Edit",
    "Instagram Reel  |  9:16 Vertical",
    "A fast-paced Instagram Reel with beat-synced transitions, text overlays, and trending audio for maximum engagement and scroll-stopping impact.",
    ["Transitions", "Audio Sync", "Text Overlay", "Reels"]
)
pdf.project_card(
    "YouTube Shorts Compilation",
    "YouTube Short  |  9:16 Vertical",
    "Edited a series of YouTube Shorts with clean cuts, engaging pacing, and consistent branding across multiple short-form videos.",
    ["Pacing", "Clean Cuts", "Branding", "Shorts"]
)
pdf.project_card(
    "Cinematic Mood Piece",
    "Short Film Edit  |  16:9 Widescreen",
    "A colour-graded short-form cinematic edit with ambient sound design, slow-motion sequences, and narrative-driven pacing.",
    ["Colour Grade", "Sound Design", "Storytelling", "Cinematic"]
)
pdf.project_card(
    "Product Showcase Edit",
    "Social Media  |  1:1 Square",
    "Eye-catching product highlight video with dynamic transitions, zoom effects, and call-to-action text for social media campaigns.",
    ["Zoom Effects", "CTA Text", "Dynamic Cuts", "Product"]
)


# ===== PROCESS =====
pdf.ln(6)
pdf.section_title("MY CREATIVE PROCESS")

process_steps = [
    ("01  Understand the Brief", "Grasp project goals, target audience, platform requirements, and creative direction."),
    ("02  Collect & Organise Assets", "Gather raw footage, audio files, graphics, and reference materials. Organise for efficiency."),
    ("03  Rough Cut", "Assemble the initial timeline - place clips, establish flow, build the story structure."),
    ("04  Transitions & Effects", "Add smooth transitions, motion effects, text overlays, and visual elements."),
    ("05  Audio & Colour", "Synchronise music and sound, apply colour correction, ensure visual consistency."),
    ("06  Final Review", "Watch the complete edit multiple times. Check timing, errors, and overall impact."),
    ("07  Export & Deliver", "Render in correct format, resolution, and specs for the target platform."),
]

for title, desc in process_steps:
    pdf.set_font("Helvetica", "B", 9)
    pdf.set_text_color(124, 58, 237)
    pdf.cell(0, 6, title, new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", "", 8)
    pdf.set_text_color(150, 150, 170)
    pdf.multi_cell(0, 4.5, desc)
    pdf.ln(2)


# ===== PAGE 4: TECH + CONTACT =====
pdf.add_page()
pdf.section_title("TECHNICAL BACKGROUND")
pdf.body_text(
    "My computer science foundation gives me an edge in understanding digital media at a deeper "
    "level - from file formats and compression to rendering pipelines and platform algorithms."
)

tech_skills = [
    "Computer Science Fundamentals", "Python Programming",
    "HTML / CSS / Web Basics", "Problem Solving",
    "File Management & Organisation", "Troubleshooting & Debugging",
    "Data Handling & Analysis", "AI Tool Awareness",
    "Cloud Services / Git", "Mobile Technology"
]
pdf.skill_row(tech_skills[:4])
pdf.skill_row(tech_skills[4:8])
pdf.skill_row(tech_skills[8:])

pdf.ln(8)
pdf.section_title("CONTACT")

contact_items = [
    ("Email", "starkindustries2131@gmail.com"),
    ("Phone", "+91 93443 90658"),
    ("Location", "Tirunelveli, Tamil Nadu, India"),
    ("GitHub", "github.com/saravanan2131"),
]

for label, value in contact_items:
    pdf.set_fill_color(20, 20, 35)
    pdf.set_draw_color(40, 40, 60)
    y = pdf.get_y()
    pdf.rect(20, y, 170, 10, style="DF")
    pdf.set_xy(24, y + 2)
    pdf.set_font("Helvetica", "B", 9)
    pdf.set_text_color(124, 58, 237)
    pdf.cell(30, 6, label)
    pdf.set_font("Helvetica", "", 9)
    pdf.set_text_color(200, 200, 220)
    pdf.cell(0, 6, value)
    pdf.set_y(y + 12)

pdf.ln(10)

# Availability box
pdf.set_fill_color(25, 15, 50)
pdf.set_draw_color(124, 58, 237)
y = pdf.get_y()
pdf.rect(20, y, 170, 30, style="DF")
pdf.set_xy(20, y + 4)
pdf.set_font("Helvetica", "B", 11)
pdf.set_text_color(230, 230, 240)
pdf.cell(170, 8, "Open to Opportunities", align="C", new_x="LMARGIN", new_y="NEXT")
pdf.set_x(20)
pdf.set_font("Helvetica", "", 9)
pdf.set_text_color(168, 85, 247)
pdf.cell(170, 7, "Video Editor  |  Junior Video Editor  |  Social Media Video Editor", align="C", new_x="LMARGIN", new_y="NEXT")
pdf.set_x(20)
pdf.set_font("Helvetica", "", 8)
pdf.set_text_color(140, 140, 160)
pdf.cell(170, 7, "Remote, On-site, Hybrid  |  Available Immediately", align="C", new_x="LMARGIN", new_y="NEXT")


# Save
pdf.output("/data/data/com.termux/files/home/portfolio/S_Saravana_Perumal_Video_Editor_Portfolio.pdf")
print("PDF created successfully!")
