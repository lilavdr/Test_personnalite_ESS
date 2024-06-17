#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 14:21:49 2024

@author: lilavendrely
"""
import streamlit as st
import matplotlib.pyplot as plt

# Définir le questionnaire de personnalité ESS
questionnaire = [
    {
        "question": "Ton point fort en cours :",
        "options": ["Les maths", "SES", "Activités manuelles et artistiques", "Sciences de la vie et de la terre", "Sport"]
    },
    {
        "question": "Un repas entre ami·e·s est organisé…",
        "options": ["C’est toi qui cuisine!! et attention à la première personne qui ose critiquer",
                    "… organisé de A à Z par toi évidemment, control freak va",
                    "Tu fais l’animation en racontant tes anecdotes improbables toute la soirée",
                    "Tu es ravi·e de pouvoir ramener tous tes jeux de société et partager tes nouveaux sons",
                    "C’est l’occasion d’avoir des super discussions deep dans la cuisine en petit comité"]
    },
    {
        "question": "Le duo de qualités qui te correspond :",
        "options": ["Créativité et originalité", "Ecoute et sens du dialogue", "Rigueur et organisation",
                    "Capacité de synthèse et de rédaction", "Aisance à l’oral et capacité de persuasion"]
    },
    {
        "question": "Ton activité de rêve à Bordeaux :",
        "options": ["Dépenser tout ton argent en testant l’ensemble des ateliers de peinture sur céramique",
                    "Concert à la Rock School ou soirée à l'entrepôt, ça dépend de l’envie du jour",
                    "Combo dominical du seigneur (brocante à Saint Mich puis marché des Capu)",
                    "Verre au soleil (ouioui il y en a des fois) à Victoire",
                    "Manif et rassemblements politiques, tu connais les slogans sur Macron mieux que tes cours"]
    },
    {
        "question": "Ton film préféré :",
        "options": ["Simone", "Le Loup de Wall Street", "Intouchable", "Mamma Mia", "Ratatouille"]
    },
    {
        "question": "Ta chaussure phare de 2024 :",
        "options": ["tes Birk", "Des runnings flambantes neuves (NIKE ZOOMX STREAKFLY pour préciser)",
                    "Une paire trouvée en brocante", "Spezial, Gazelle, Samba, la trend ne t’a pas échappée", "Mocassins"]
    },
    {
        "question": "Ton animal totem :",
        "options": ["Requin", "Araignée", "Chien", "Abeille", "Chat noir"]
    },
    {
        "question": "Ton arrêt de tram préféré :",
        "options": ["Montaigne Montesquieu", "Hôtel de ville", "CHU Pellegrin", "CAPC musée d’art contemporain", "Jardin botanique"]
    },
    {
        "question": "À quelle émission pourrais-tu participer ?",
        "options": ["Koh Lanta", "Top chef", "Qui veut gagner des millions", "La Star Academy", "Nus et culottés"]
    },
    {
        "question": "Ton application préférée :",
        "options": ["X (Twitter)", "Strava", "Tik Tok", "Duolingo", "Betclic"]
    }
]

# Mapping des réponses aux catégories
categories = {
    1: "Finance éthique + management ESS",
    2: "Artisanat",
    3: "Collectivité",
    4: "Asso réinsertion sociale par le sport",
    5: "Education",
    6: "Arts, événementiel, fête, Tiers Lieu",
    7: "Alimentation durable",
    8: "Médico-social",
    9: "Association militante"
}

st.set_page_config(page_title="Questionnaire de Personnalité ESS", layout="centered")
st.title("Questionnaire de Personnalité ESS")

if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
if 'answers' not in st.session_state:
    st.session_state.answers = []
if 'points' not in st.session_state:
    st.session_state.points = {i: 0 for i in range(1, 10)}

def process_answer(answer, question_index):
    mapping = [
        ["Les maths", 1], ["SES", 3], ["Activités manuelles et artistiques", 2], ["Sciences de la vie et de la terre", 8], ["Sport", 4],
        ["C’est toi qui cuisine!! et attention à la première personne qui ose critiquer", 2], ["… organisé de A à Z par toi évidemment, control freak va", 1],
        ["Tu fais l’animation en racontant tes anecdotes improbables toute la soirée", 5], ["Tu es ravi·e de pouvoir ramener tous tes jeux de société et partager tes nouveaux sons", 6],
        ["C’est l’occasion d’avoir des super discussions deep dans la cuisine en petit comité", 4], ["Créativité et originalité", 2], ["Ecoute et sens du dialogue", 8],
        ["Rigueur et organisation", 1], ["Capacité de synthèse et de rédaction", 3], ["Aisance à l’oral et capacité de persuasion", 3], ["Dépenser tout ton argent en testant l’ensemble des ateliers de peinture sur céramique", 2],
        ["Concert à la Rock School ou soirée à l'entrepôt, ça dépend de l’envie du jour", 6], ["Combo dominical du seigneur (brocante à Saint Mich puis marché des Capu)", 3],
        ["Verre au soleil (ouioui il y en a des fois) à Victoire", 1], ["Manif et rassemblements politiques, tu connais les slogans sur Macron mieux que tes cours", 9], ["Simone", 3],
        ["Le Loup de Wall Street", 1], ["Intouchable", 8], ["Mamma Mia", 2], ["Ratatouille", 5], ["tes Birk", 6], ["Des runnings flambantes neuves (NIKE ZOOMX STREAKFLY pour préciser)", 4],
        ["Une paire trouvée en brocante", 2], ["Spezial, Gazelle, Samba, la trend ne t’a pas échappée", 3], ["Mocassins", 1], ["Requin", 1], ["Araignée", 2], ["Chien", 4], ["Abeille", 3], ["Chat noir", 9],
        ["Montaigne Montesquieu", 5], ["Hôtel de ville", 1], ["CHU Pellegrin", 8], ["CAPC musée d’art contemporain", 2], ["Jardin botanique", 4], ["Koh Lanta", 2], ["Top chef", 7],
        ["Qui veut gagner des millions", 1], ["La Star Academy", 5], ["Nus et culottés", 9], ["X (Twitter)", 9], ["Strava", 4], ["Tik Tok", 6], ["Duolingo", 5], ["Betclic", 1]
    ]
    
    answer_map = mapping[question_index * len(questionnaire[0]['options']): (question_index + 1) * len(questionnaire[0]['options'])]
    
    for map_answer, category in answer_map:
        if answer == map_answer:
            st.session_state.points[category] += 1

def show_question():
    question_index = st.session_state.current_question
    question = questionnaire[question_index]
    st.radio(question['question'], question['options'], key=f"q{question_index}", on_change=next_question)

def next_question():
    question_index = st.session_state.current_question
    answer = st.session_state.get(f"q{question_index}")
    st.session_state.answers.append(answer)
    process_answer(answer, question_index)
    if question_index + 1 < len(questionnaire):
        st.session_state.current_question += 1

def previous_question():
    if st.session_state.current_question > 0:
        st.session_state.current_question -= 1
        st.session_state.answers.pop()

def show_results():
    total_points = sum(st.session_state.points.values())
    if total_points > 0:
        percentages = {categories[k]: (v / total_points) * 100 for k, v in st.session_state.points.items() if v > 0}
        
        # Graphique en secteurs
        fig, ax = plt.subplots()
        labels = list(percentages.keys())
        sizes = list(percentages.values())
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired(range(len(labels))))
        ax.axis('equal')
        plt.title("Résultats du questionnaire de personnalité ESS")

        st.pyplot(fig)
    else:
        st.warning("Veuillez répondre à toutes les questions.")

if st.session_state.current_question < len(questionnaire):
    show_question()
    if st.session_state.current_question > 0:
        st.button("Précédent", on_click=previous_question)
else:
    show_results()
    st.button("Recommencer", on_click=lambda: [st.session_state.update({'current_question': 0, 'answers': [], 'points': {i: 0 for i in range(1, 10)}})])


