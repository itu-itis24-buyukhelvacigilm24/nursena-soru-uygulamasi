import streamlit as st
import json
import os

# JSON dosyasını oku
json_file = r"combined_questions.json"

if not os.path.exists(json_file):
    st.error(f"Dosya bulunamadı: {json_file}")
else:
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    questions = data.get('matched_questions', [])
    
    kelime = st.text_input(label="ı asked what you want ? i said painting she said aşkım sıralamalı sorular")
    questions = [q for q in questions if kelime in q["text"]]
    
    st.title("askim ramazan bayramin mubarek olsun bayram sekerisin keske senanur diye seker olsa ece cok kotu öle iste askim")
    st.write(f"Toplam {len(questions)} soru yüklendi.(nursena için senanur deil)")

    if questions:
        question_numbers = [f"Soru {q['number']} (Test {q['test_info']['test_number']})" for q in questions]
        selected_question = st.selectbox("Bir soru seçin:", question_numbers)
        selected_index = question_numbers.index(selected_question)

        question = questions[selected_index]
        st.subheader(f"Soru {question['number']} (Test {question['test_info']['test_number']})")
        st.write("**Paragraf:**")
        st.write(question['paragraph'])
        st.write("**Soru:**")
        st.write(question['text'])
        st.write("**Seçenekler:**")
        for option in question['options']:
            st.write(f"{option['option']}: {option['text']}")

        if st.checkbox("Doğru cevabı göster"):
            st.write(f"**Doğru Cevap:** {question['correct_answer']}")
    else:
        st.warning("Eşleşen soru bulunamadı.")
