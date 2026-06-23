import streamlit as st
import google.generativeai as genai

try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
except Exception as e:
    st.error("API Key not found. Please add GEMINI_API_KEY to Streamlit Secrets.")

system_prompt = """
Sən dünya səviyyəli bir rəqəmsal marketinq strateqi və yüksək konversiya yaradan peşəkar kopiraytersən. 
Sənin vəzifən verilmiş biznes və məhsul üçün 3 fərqli platformaya uyğun, psixoloji təsirlərə əsaslanan və satış yönümlü reklamlar hazırlamaqdır.

KRİTİK FORMATLAŞDIRMA QAYDASI: Mətnin oxunaqlı olması üçün aydın sətir keçidlərindən və boşluqlardan istifadə et. Uzun və sıx paraqraflardan qaç.

Hər platforma üçün aşağıdakı strategiyaları tətbiq et:

1. 📸 INSTAGRAM (Strategiya: Emosional Bağlılıq və Estetika)
   - Ton: Müasir, həyəcanverici və vizual təsvirlərə əsaslanan.
   - Struktur: 
     - Diqqətçəkən və maraq oyadan ilk cümlə.
     - Emosional bədən mətni (qısa paraqraflarla).
     - Aydın və dəqiq Call to Action (Fəaliyyətə çağırış).
     - Minimum 5 trend hashtag.

2. 🔵 FACEBOOK (Strategiya: Strukturlaşdırılmış AIDA Framework-ü)
   - Ton: Etibarlı, peşəkar və fayda yönümlü.
   - Struktur (Bu ardıcıllığa ciddi riayət et):
     - [ATTENTION/DİQQƏT]: İstifadəçinin "scroll" etməsini dayandıracaq güclü bir giriş cümləsi.
     - [INTEREST/MARAQ]: Əsas dəyər təklifini izah edən 2-3 qısa cümlə.
     - [DESIRE/İSTƏK]: Əsas üstünlükləri siyahı şəklində (✅ və ya ✨ emojiləri ilə) 3-4 bəndlə qeyd et.
     - [TRUST/ETİBAR]: Avtoritet yaradan və ya təcililik hissi verən bir cümlə.
     - [ACTION/HƏRƏKƏT]: Aydın və təkbaşına dayanan güclü Call to Action (CTA).
   - Formatlaşdırma: Hər bölmə arasında iki sətirlik boşluq qoy.

3. 🎵 TIKTOK (Strategiya: Pattern Interrupt - Diqqəti dayandırmaq)
   - Ton: Dinamik, səmimi və vurucu.
   - Struktur: Maraq oyadan və istifadəçini dərhal cəlb edən tək bir yüksək təsirli "Hook" (Qarmaq) cümləsi.

Çıxış formatı dəqiq belə olmalıdır:
---
📸 INSTAGRAM
Caption: 
[Sətir keçidləri olan mətn]

Hashtags: 
[Hashtag-lər]

🔵 FACEBOOK
Ad Copy: 
[Hook/Giriş]

[Maraq/Dəyər təklifi]

[Üstünlük 1]
[Üstünlük 2]
[Üstünlük 3]

[Etibar/Təcililik]

CTA: [Güclü fəaliyyətə çağırış]

🎵 TIKTOK
Hook: [Diqqətçəkən qısa cümlə]
---
"""

model = genai.GenerativeModel(
    model_name='gemini-2.5-flash', 
    system_instruction=system_prompt
)

@st.cache_data(show_spinner=False)
def get_ai_response(business_name, product_service):
    user_prompt = f"Business Name: {business_name}\nProduct/Service: {product_service}"
    try:
        response = model.generate_content(user_prompt)
        return response.text
    except Exception as e:
        return f"An error occurred: {e}"


st.set_page_config(page_title="AI Ad Generator")
st.title(" Multi-Platform AI Ad Generator")
st.write("Enter your business details below to generate high-conversion ads!")

business_name = st.text_input("Business Name", placeholder="e.g. CodeAcademy AZ")
product_service = st.text_area("Product/Service", placeholder="e.g. 3-month Python course")

if st.button("Generate Ads ✨"):
    if business_name and product_service:
        with st.spinner("Generating your ads..."):
            result = get_ai_response(business_name, product_service)
            st.markdown("---")
            st.text(result)
    else:
        st.warning("Please fill in both fields!")
