# Multi-Platform AI Generator

An AI-powered tool designed to generate high-conversion marketing copy for **Instagram, Facebook, and TikTok**. This project demonstrates advanced Prompt Engineering techniques to ensure platform-specific tone and psychological triggers.

## Prompt Engineering Approach

Instead of simple instructions, this project implements professional marketing frameworks to maximize AI output quality:

### 1. Instagram: Emotional Lifestyle Approach
The prompt instructs the AI to focus on the **emotional benefit** and "lifestyle" rather than just features. This aligns with Instagram's visually-driven, aspirational user behavior.

### 2. Facebook: AIDA Framework
For Facebook, I implemented the **AIDA (Attention, Interest, Desire, Action)** framework:
- **Attention**: Captures the user immediately.
- **Interest**: Builds engagement through benefits.
- **Desire**: Creates an emotional need for the product.
- **Action**: Drives the user toward a specific goal with a strong CTA.

### 3. TikTok: Pattern Interrupt
TikTok users scroll rapidly. The prompt uses the **Pattern Interrupt** technique to generate "Hooks" that break the user's scrolling habit within the first 3 seconds.

## Texnologiyalar
- **Dil:** Python
- **AI Model:** Google Gemini 2.5 Flash
- **Kitabxanalar:** `google-generativeai`, `python-dotenv`

## Installation & Setup
1. **Clone the repository**: `git clone https://github.com/sizin-adiniz/ai-ad-generator.git`
2. **Install dependencies**: `pip install -r requirements.txt`
3. **Set up API Key**: Create a `.env` file in the root directory and add your `GEMINI_API_KEY`
4. **Run the application**: `python main.py`

## 1) Case Study
- Input:
  - Business Name: `CodeAcademy AZ`
  - Product/Service: `Sıfırdan Python proqramlaşdırma kursu (3 aylıq intensiv)`
- AI Generated Results:
```Text
📸 INSTAGRAM
Caption: Gələcəyin səni çağırır! 🚀 Heç bir proqramlaşdırma biliyin olmadan, cəmi 3 ayda yüksək maaşlı IT karyerasına başlamaq istəyirsən? CodeAcademy AZ-ın intensiv Python kursu ilə arzularını reallığa çevir. ✨ Sıfırdan başla, real layihələr üzərində işlə, texnologiya dünyasının tələb etdiyi mütəxəssis ol! Bu fürsəti qaçırma, həyatını dəyişməyə indi başla! 💻💡
Hashtags: #PythonDərsləri #CodeAcademyAZ #Proqramlaşdırma #TechKaryera #GələcəyinProqramçısı #KaryeraDəyişikliyi #ITAzərbaycan
🔵 FACEBOOK
Ad Copy: Texnologiya dünyası durmadan inkişaf edir və yüksək ixtisaslı proqramçılara ehtiyac günü-gündən artır. Siz də bu inqilabın bir hissəsi olmaq, gələcəyin peşəsini öyrənərək stabil və gəlirli bir karyeraya sahib olmaq istəyirsiniz?
CodeAcademy AZ sizin üçün ən mükəmməl fürsəti təqdim edir: Sıfırdan Python Proqramlaşdırma kursu! Cəmi 3 aylıq bu intensiv proqramda siz Python-un əsaslarından başlayaraq, data analizi, veb inkişafı və avtomatlaşdırma kimi sahələrdə tətbiqlər yaratmağı öyrənəcəksiniz. Təcrübəli mentorlarımızın rəhbərliyi altında real layihələr üzərində işləyəcək, biliklərinizi praktiki olaraq tətbiq edəcəksiniz.
Təsəvvür edin, 3 aydan sonra siz artıq yalnız kod oxuyan deyil, eyni zamanda kod yaza bilən, problemləri alqoritmik düşüncə ilə həll edən bir mütəxəssis olacaqsınız. Öz ideyalarınızı reallaşdırmaq, rəqəmsal dünyada dəyər yaratmaq və maliyyə azadlığına qovuşmaq artıq xəyal deyil, reallıqdır.
Gələcək karyeranızı bu gün formalaşdırın! Yerlər məhduddur, bu unikal fürsəti qaçırmayın.
CTA: İndi Qeydiyyatdan Keç!
🎵 TIKTOK
Hook: Həyatını 3 aya dəyişmək istəyirsən? 🚀
```
