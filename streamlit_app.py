import pandas as pd
import numpy as np
import re
import time
import os

import pickle
import streamlit as st


@st.cache
def get_search_term_mapping():
    with open('who_search_terms_mapping.pkl', 'rb') as handle:
        out_search_space = pickle.load(handle)
        return out_search_space

st.title('Specialist Doctor Search')
search_space = get_search_term_mapping()
#search_terms = []
search_term = st.selectbox(
    "Select search terms", list(search_space.keys())
)

addln_suggestions = []
#for term in search_terms:
addln_suggestions.extend(search_space[search_term])

# only unique terms
addln_suggestions = list(set(addln_suggestions))
addln_suggestions = [term for term in addln_suggestions if term != search_term]

addln_search_terms = []
if len(addln_suggestions) > 0:
    addln_search_terms = st.multiselect(
        "Optionally add related terms", addln_suggestions, []
    )

st.write(f'User selected search terms: {search_term}')
if len(addln_search_terms) > 0:
    st.write(f'User selected additional related terms: {addln_search_terms}')

