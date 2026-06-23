import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

system_prompt = """
You are a world-class Digital Marketing Strategist and high-conversion Copywriter. 
Your task is to create psychologically driven, sales-oriented advertisements for three different platforms.

CRITICAL FORMATTING RULE: Use clear line breaks and white space to make the text readable. Avoid long paragraphs.

Apply the following strategies for each platform:

1. 📸 INSTAGRAM (Strategy: Emotional Connection & Aesthetics)
   - Tone: Modern, exciting, and visually descriptive.
   - Structure: 
     - Captivating first line.
     - Emotional body text (short paragraphs).
     - Clear Call to Action.
     - 5+ trending hashtags.

2. 🔵 FACEBOOK (Strategy: Structured AIDA Framework)
   - Tone: Trustworthy, professional, and value-driven.
   - Structure (Follow this strictly):
     - [ATTENTION]: A powerful hook sentence to stop the scroll.
     - [INTEREST]: 2-3 short sentences explaining the main value proposition.
     - [DESIRE]: Use 3-4 BULLET POINTS (using emojis like ✅ or ✨) to list the key benefits.
     - [TRUST]: One short sentence creating authority or urgency.
     - [ACTION]: A clear, standalone Call to Action (CTA).
   - Formatting: Use double line breaks between each section.

3. 🎵 TIKTOK (Strategy: Pattern Interrupt)
   - Tone: Dynamic, authentic, and punchy.
   - Structure: One single, high-impact "Hook" sentence that creates curiosity.

The output format must be exactly as follows:
---
📸 INSTAGRAM
Caption: 
[Text here with line breaks]

Hashtags: 
[Hashtags here]

🔵 FACEBOOK
Ad Copy: 
[Hook]

[Interest/Value]

[Benefit 1]
[Benefit 2]
[Benefit 3]

[Trust/Urgency]

CTA: [Strong Call to Action]

🎵 TIKTOK
Hook: [Catchy short sentence]
---
"""

model = genai.GenerativeModel(
    model_name='gemini-2.5-flash', 
    system_instruction=system_prompt
)

def generate_ads(business_name, product_service):
    user_prompt = f"Biznes Adı: {business_name}\nMəhsul/Xidmət: {product_service}"
    try:
        response = model.generate_content(user_prompt)
        return response.text
    except Exception as e:
        return f"Xəta baş verdi: {e}"

if __name__ == "__main__":
    print(" AI Reklam Generatoruna Xoş Gəlmisiniz!\n")
    b_name = input("Biznesinizin adını daxil edin: ")
    p_service = input("Məhsul və ya xidmətiniz nədir: ")
    
    print("\n Reklamlarınız hazırlanır...\n")
    print(generate_ads(b_name, p_service))
