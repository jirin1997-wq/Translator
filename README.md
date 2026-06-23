# Škoda X Translator – webová verze

## Spuštění

```bash
# 1. Nainstaluj závislosti
pip install -r requirements.txt

# 2. Vytvoř soubor .env (ze vzoru .env.example)
cp .env.example .env
# a doplň klíče OPENAI_API_KEY a DEEPL_API_KEY

# 3. Spusť server
uvicorn app:app --reload

# Aplikace běží na http://localhost:8000
```

## Struktura

```
web/
├── app.py            # FastAPI backend
├── glossary.py       # Škoda terminologie
├── requirements.txt
├── .env              # API klíče (neverzovat!)
└── templates/
    └── index.html    # Webové rozhraní
```

## Podporované jazyky

Stejné jako původní aplikace – DeepL pro většinu EU jazyků + OpenAI pro
bosenštinu, chorvatštinu, makedonštinu a srbštinu. Pro všechny jazyky
se automaticky aplikuje Škoda Auto terminologie.
