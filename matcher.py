import spacy

class KeywordMatcher:
    def __init__(self, job_description):
        self.nlp = self.load_spacy_model()
        self.keywords = self.extract_keywords(job_description)

    def load_spacy_model(self):
        try:
            # Try to load the model if it's already installed
            return spacy.load("en_core_web_sm")
        except OSError:
            # If not installed, download it programmatically
            from spacy.cli import download
            download("en_core_web_sm")
            return spacy.load("en_core_web_sm")

    def extract_keywords(self, text):
        doc = self.nlp(text.lower())
        words = [token.lemma_ for token in doc if token.is_alpha and not token.is_stop]
        return set(words)

    def match_score(self, resume_text):
        doc = self.nlp(resume_text.lower())
        resume_words = set(token.lemma_ for token in doc if token.is_alpha and not token.is_stop)
        common = self.keywords.intersection(resume_words)
        return len(common)
