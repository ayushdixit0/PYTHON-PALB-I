# 🤖 ApexSupport AI - Intelligent NLP Customer Support & FAQ Chatbot

A high-performance conversational AI platform designed for customer service and FAQ resolution. Combines Natural Language Processing (**NLTK** tokenization, POS tagging, lemmatization, VADER sentiment analysis, TF-IDF) with Modern Dense Semantic Search (**Transformers / Sentence-Transformers**), **FastAPI** backend, and **SQLite** persistence with real-time audit interaction logging and analytics.

---

## 🌟 Key Features

1. **Context-Aware Multi-Turn Dialogue Engine**:
   - Stateful conversation tracking for slot-filling workflows (e.g. collecting Order ID $\rightarrow$ tracking carrier status, or checking 30-day return eligibility $\rightarrow$ reason collection $\rightarrow$ automatic return label generation).
   - Entity & parameter extraction using regex & NLTK (Order IDs like `ORD-9821`, email addresses, reason categories).

2. **Dual-Tier Hybrid Semantic & Lexical FAQ Retrieval**:
   - **Dense Retriever**: Precomputed sentence embeddings via `sentence-transformers/all-MiniLM-L6-v2` with Cosine Similarity.
   - **Sparse Lexical Retriever**: NLTK lemmatized TF-IDF vectorizer.
   - **Dynamic Hybrid Fusion**: Blended confidence score ($65\%$ dense $+ 35\%$ sparse + exact keyword boost) with automatic top-$k$ alternative suggestions.

3. **Sentiment & Frustration Detection**:
   - Real-time customer emotion scoring with **NLTK VADER**.
   - Automatic empathy prompts and human agent escalation ticket generation (`TICK-#####`) when frustration or unresolved complex issues are detected.

4. **Complete Single-Page Web Application**:
   - **Customer Chat UI**: Modern messaging interface with avatar badges, dynamic quick suggestion chips, live typing indicator, markdown formatting, speech-to-text voice input, text-to-speech audio playback, message copy, and thumbs up/down rating buttons.
   - **Admin & Analytics Portal**: Real-time KPI dashboard (Total Queries, Intent Accuracy, Avg Latency, Avg Sentiment, Tickets Queue), interaction logs explorer with intent filtering, CSV export, and live Knowledge Base (FAQ) CRUD manager.
   - **Interactive NLP Model Inspector (Playground)**: Real-time inspector for tokenization, lemmatization, sentiment polarity, classified intent, and semantic similarity rankings.

5. **SQLite Interaction & Audit Logging**:
   - Every single conversation, message, customer query, bot response, classified intent, confidence score, sentiment score, latency (ms), and rating is persisted and queryable.

---

## 🛠️ Technology Stack

- **Core Language**: Python 3.10+
- **NLP & AI**: NLTK (Tokenization, WordNet Lemmatizer, POS Tagger, VADER Sentiment), HuggingFace Transformers, Sentence-Transformers, Scikit-learn (TF-IDF, Cosine Similarity)
- **Web Framework & API**: FastAPI, Uvicorn, Jinja2, Pydantic, Python-Multipart
- **Database**: SQLite3
- **Frontend**: Responsive HTML5, CSS3 Glassmorphism theme (Dark / Light mode), FontAwesome 6, Marked.js Markdown parser, Web Speech API (STT & TTS)
- **Testing**: Pytest, FastAPI TestClient

---

## 🚀 Quick Start Guide

### 1. Setup Virtual Environment & Install Dependencies
```bash
# Create and activate virtual environment
python -m venv venv

# Windows
.\venv\Scripts\Activate.ps1
# Linux / macOS
# source venv/bin/activate

# Install requirements
pip install -r requirements.txt
```

### 2. Run the Application
```bash
python run.py
```

Open your browser and navigate to:
```
http://127.0.0.1:8000
```

---

## 🧪 Running Automated Tests

Execute the complete test suite:
```bash
pytest tests/ -v
```

---

## 📡 REST API Documentation

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/api/session/new` | Generates a new conversation session and welcome message |
| `POST` | `/api/chat` | Main contextual chat query endpoint |
| `GET` | `/api/session/{id}/history` | Retrieves chronologically ordered chat messages |
| `POST` | `/api/feedback` | Submits customer satisfaction rating (1-5 stars) and comments |
| `GET` | `/api/faqs` | Lists all knowledge base FAQs |
| `POST` | `/api/faqs` | Adds a new FAQ entry and re-indexes the vector space in real-time |
| `PUT` | `/api/faqs/{id}` | Updates existing FAQ entry |
| `DELETE` | `/api/faqs/{id}` | Deletes an FAQ entry |
| `GET` | `/api/tickets` | Lists escalated support tickets |
| `POST` | `/api/tickets` | Creates a support ticket |
| `GET` | `/api/analytics/summary` | Real-time KPI metrics and sentiment averages |
| `GET` | `/api/analytics/logs` | Searchable and filterable user interaction audit logs |
| `GET` | `/api/analytics/export` | Downloads interaction audit logs as CSV |
| `POST` | `/api/nlp/test` | NLP diagnostic playground endpoint |
| `GET` | `/health` | Server and model health check |

---

## 🗄️ Database Architecture (SQLite)

- **`conversations`**: Tracks unique sessions, timestamps, user identities, and status (`active`, `resolved`, `escalated`).
- **`messages`**: Records every message with sender (`user`, `bot`), text, intent, confidence, sentiment label, compound score, and latency (ms).
- **`faqs`**: Knowledge base articles with category, question, answer, keywords, hits counter, and active status.
- **`interaction_logs`**: Audit trail containing full query-response pairs, intent, confidence, sentiment, latency, and resolution status.
- **`feedback`**: User ratings (1-5 stars), message linkages, and comments.
- **`tickets`**: Support escalation tickets with ticket codes (`TICK-XXXXXX`), category, description, customer contact, and priority.
