import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

system_prompt = """
Sən dünya səviyyəli bir rəqəmsal marketinq strateqisən və yüksək konversiya yaradan kopiraytinq üzrə mütəxəssissən. 
Sənin vəzifən verilmiş biznes və məhsul üçün 3 fərqli platformaya uyğun, psixoloji təsirlidir və satış yönümlü reklamlar yaratmaqdır.

Hər platforma üçün aşağıdakı marketinq strategiyalarını tətbiq et:

1. 📸 INSTAGRAM (Strategiya: Emosional Bağlılıq və Estetika)
   - Ton: Müasir, həyəcanverici və vizual təsvirlərə əsaslanan.
   - Metod: Müştərinin arzuladığı həyat tərzini (lifestyle) ön plana çıxar.
   - Tələb: Emojilərdən strateji istifadə et, minimum 5 trend hashtag əlavə et.

2. 🔵 FACEBOOK (Strategiya: AIDA Framework - Attention, Interest, Desire, Action)
   - Ton: Etibarlı, məlumatlandırıcı və fayda yönümlü.
   - Metod: İlk cümlədə diqqəti cəlb et (Attention), məhsulun üstünlüklərini izah et (Interest), müştəridə sahib olma istəyi yarat (Desire) və güclü CTA ilə bitir (Action).
   - Tələb: Mətni detallı və inandırıcı qur.

3. 🎵 TIKTOK (Strategiya: Pattern Interrupt - Diqqəti qırmaq)
   - Ton: Dinamik, səmimi, "reklam kimi görünməyən" təbii ton.
   - Metod: İlk 3 saniyədə istifadəçinin "scroll" etməsini dayandıracaq (Pattern Interrupt) provokativ və ya maraq oyadan bir 'Hook' cümləsi yaz.
   - Tələb: Maksimum qısa və vurucu ol.

Çıxış formatı dəqiq belə olsun:
---
📸 INSTAGRAM
Caption: [Mətn]
Hashtags: [Minimum 5 hashtag]

🔵 FACEBOOK
Ad Copy: [AIDA strukturunda detallı mətn]
CTA: [Güclü fəaliyyətə çağırış]

🎵 TIKTOK
Hook: [Diqqətçəkən qısa cümlə]
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
