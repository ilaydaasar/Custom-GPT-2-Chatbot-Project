# src/textcleaner.py
import re

def fix_spacing_issues(text):
    """Kelime birleşme sorunlarını düzelt"""
    fixes = {
        'likeyou': 'like you',
        'likeus': 'like us',
        'withyou': 'with you',
        'foryou': 'for you',
        'toyou': 'to you',
        'aboutyou': 'about you',
        'ofyou': 'of you',
        'inyou': 'in you',
        'onyou': 'on you',
        'atyou': 'at you',
        'areyou': 'are you',
        'isyou': 'is you',
        'wasyou': 'was you',
        'wereyou': 'were you',
        'haveyou': 'have you',
        'hasyou': 'has you',
        'hadyou': 'had you',
        'willyou': 'will you',
        'wouldyou': 'would you',
        'couldyou': 'could you',
        'shouldyou': 'should you',
        'canyou': 'can you',
        'didyou': 'did you',
        'doesyou': 'does you',
        'doyou': 'do you',
        'iam': 'I am',
        'iwill': 'I will',
        'iwould': 'I would',
        'ican': 'I can',
        'ihave': 'I have',
        'iwas': 'I was',
        'whatis': 'what is',
        'whois': 'who is',
        'whereis': 'where is',
        'whenis': 'when is',
        'whyis': 'why is',
        'howis': 'how is',
        'whatare': 'what are',
        'whoare': 'who are',
        'whereare': 'where are',
        'whenare': 'when are',
        'whyare': 'why are',
        'howare': 'how are'
    }
    
    for wrong, correct in fixes.items():
        text = re.sub(r'\b' + wrong + r'\b', correct, text, flags=re.IGNORECASE)
    
    return text

def extract_clean_response(full_text, prompt):
    """Temiz yanıt çıkar"""
    if "Assistant:" in full_text:
        response = full_text.split("Assistant:")[-1].strip()
    else:
        response = full_text.replace(prompt, "").strip()
    
    sentences = re.split(r'[.!?]', response)
    for sentence in sentences:
        sentence = sentence.strip()
        words = sentence.split()
        if 2 <= len(words) <= 20:
            if not sentence.endswith(('.', '!', '?')):
                sentence += '.'
            sentence = fix_spacing_issues(sentence)
            return sentence
    
    return fix_spacing_issues(response.split('.')[0] + '.')