### Website Ohridski prolog po delu Vladike Nikolaja Velimirovica:
- FE: React
- BE: FastAPI, SQLite
- cheap domain and hosting
- deploy all apps on one server
- use subdomains or nginx routing
- monorepo
- content:
    - predgovor Arhimandrita Justina Popovica
    - za svaki dan u godini: zitije svetaca, rasudjivanje, sozercanje, beseda
    - pogovor i blagodarnost od oca Nikolaja

### Run on development enviroment:
#### Client app
- template created with `npx create-next-app`
- `cd app`
- `npm i`
- `npm run dev`

#### API
- `cd api`
- `source venv/bin/activate`
- `pip install -r requirements.txt`
- `uvicorn main:app --reload`
