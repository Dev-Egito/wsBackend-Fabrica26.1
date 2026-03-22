# 🎬 CineScope — wsBackend-Fabrica26.1

Projeto de faculdade desenvolvido com Django. Permite buscar filmes via API do OMDB e registrar críticas com nota e comentário.

---

## 🚀 Funcionalidades

- Busca de filmes pelo título via [OMDB API](http://www.omdbapi.com/)
- Exibição de poster, ano, gênero e sinopse
- Criação e atualização de críticas por usuário
- Listagem de críticas por filme

---

## 🛠️ Tecnologias

- Python 3.14
- Django 6.0.3
- SQLite
- Docker + Colima (Mac Intel)
- OMDB API

---

## ⚙️ Como rodar localmente

**1. Clone o repositório**
```bash
git clone https://github.com/seu-usuario/wsBackend-Fabrica26.1.git
cd wsBackend-Fabrica26.1
```

**2. Crie e ative a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

**3. Instale as dependências**
```bash
pip install -r requirements.txt
```

**4. Rode as migrations**
```bash
python manage.py migrate
```

**5. Crie um superusuário (necessário para críticas)**
```bash
python manage.py createsuperuser
```

**6. Suba o servidor**
```bash
python manage.py runserver
```

Acesse em `http://localhost:8000/filmes/`

---

## 🐳 Como rodar com Docker

> **Mac com Intel + macOS Ventura:** use o Colima no lugar do Docker Desktop.
> ```bash
> brew install colima docker
> colima start
> ```

**Build da imagem**
```bash
docker build -t cinescope .
```

**Rodar o container**
```bash
docker run -p 8000:8000 cinescope
```

Para persistir o banco de dados entre execuções:
```bash
docker run -p 8000:8000 -v $(pwd)/db.sqlite3:/app/db.sqlite3 cinescope
```

Acesse em `http://localhost:8000/filmes/`

---

## 📁 Estrutura do projeto

```
wsBackend-Fabrica26.1/
├── core/               # Configurações do Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── filmes/             # App principal
│   ├── migrations/
│   ├── templates/
│   │   └── filmes/
│   │       ├── buscar.html
│   │       └── criar_critica.html
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── Dockerfile
├── manage.py
└── requirements.txt
```

---

## 🗄️ Models

**Filme**
| Campo | Tipo | Descrição |
|---|---|---|
| titulo | CharField | Título do filme |
| imdb_id | CharField | ID único do OMDB |

**Critica**
| Campo | Tipo | Descrição |
|---|---|---|
| usuario | ForeignKey | Usuário que avaliou |
| filme | ForeignKey | Filme avaliado |
| comentarios | TextField | Texto da crítica |
| nota | IntegerField | Nota de 1 a 5 |
| criado_em | DateTimeField | Data de criação |

> Um usuário só pode ter uma crítica por filme. Caso avalie novamente, a crítica é atualizada (`update_or_create`).

---

## 🔗 Rotas

| Método | URL | Descrição |
|---|---|---|
| GET | `/filmes/` | Busca filme por título |
| GET/POST | `/filmes/criar_critica/<id>/` | Cria ou atualiza crítica |

---

## ⚠️ Observações

- O projeto usa `User.objects.first()` como usuário fixo. A autenticação real com `request.user` será implementada futuramente.
- A API key do OMDB está no código por ser um projeto acadêmico. Em produção, mover para variável de ambiente.