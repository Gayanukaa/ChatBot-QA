# V2-QATool

``` markdown
v2-qatool/
│
├── app/                        # Backend FastAPI Application
│   ├── main.py                 # Entry point for FastAPI app
│   ├── routes.py               # API routes and endpoints
│   ├── services.py             # Core logic: LLM, RAG, and vector database integration
│   ├── rag_retriever.py        # Handles RAG retrieval from the vector database
│   ├── vector_db.py            # Vector database setup and embedding logic
│   ├── schemas.py              # Pydantic models for API validation
│   ├── __init__.py             # Makes the folder a package
│
├── data/                       # Input and static data
│   ├── hearing_items.docx      # Predefined baseline questions
│   ├── translated_file.xlsx    # English-translated Q&A data for embeddings
│   ├── product_data.pdf        # Techno Horizon product catalog (PDF)
│
├── vector_store/               # Stores vector database indexes (if using FAISS locally)
│   └── faiss_index/            # FAISS index files (optional)
│
├── frontend/                   # Streamlit Frontend
│   ├── app.py                  # Streamlit interface for user interaction
│   ├── components/             # UI components for modular design
│   │   ├── question_display.py # Module for displaying current questions
│   │   ├── feedback_form.py    # Feedback form for user inputs
│   │   ├── product_display.py  # Module for showing product recommendations
│   │
│   ├── __init__.py
│
├── docs/                       # Documentation
│   ├── README.md               # General project overview
│   ├── architecture.md         # High-level design with RAG and vector database
│   ├── api_endpoints.md        # FastAPI endpoint documentation
│
├── tests/                      # Unit and Integration Tests
│   ├── backend/                # Tests for backend logic
│   │   ├── test_services.py    # Tests for services.py
│   │   ├── test_rag_retriever.py # Tests for RAG retriever logic
│   │
│   ├── frontend/               # Tests for Streamlit components
│   │   ├── test_streamlit_ui.py # Tests for Streamlit interface
│
├── requirements.txt            # Project dependencies
├── .env                        # Environment variables (API keys, endpoints, etc.)
├── .gitignore                  # Ignored files
└── README.md                   # Project Overview and Quick Start Guide

```
