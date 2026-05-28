# Pine_Script_v6_doc

Herramienta basada en Python para extraer y procesar la documentación de Pine Script V6 de TradingView, construida con el framework **Crawl4Ai**. Esta herramienta extrae, limpia y organiza la documentación, facilitando su referencia y análisis. Crawl4Ai proporciona el framework principal para web crawling, extracción de datos y procesamiento asíncrono.

## ✨ Características

### Extracción
- Extrae automáticamente la documentación del sitio web de Pine Script V6 de TradingView usando Crawl4Ai
- Maneja eficientemente la navegación a través de las páginas de documentación
- Soporta procesamiento por lotes con limitación de velocidad
- Mantiene un esquema de extracción estructurado para resultados consistentes
- Guarda URLs individuales y archivos de documentación combinados

### Procesamiento de Contenido
- Limpia y formatea el contenido de la documentación
- Preserva bloques de código Pine Script con resaltado de sintaxis apropiado
- Extrae y formatea la documentación de funciones
- Elimina elementos de navegación innecesarios (links de footer, secciones "On this page")
- Procesa el contenido en formato markdown limpio y legible
- Incluye extracción de Apps Script enfocada en el rectángulo verde de contenido principal, excluyendo la sección “En esta página”

### Organización de Salida
- Crea archivos separados para URLs y contenido
- Genera archivos de documentación combinados para fácil referencia
- Mantiene el orden original de secciones de la documentación de TradingView
- Rastrea estadísticas de extracción y timestamps

## 📊 Cobertura de Documentación

| Fuente | Items | Secciones | Tamaño |
|--------|-------|-----------|--------|
| Manual de Referencia | 941 | 7 | 0.7 MB |
| Manual de Usuario | 71 | 11 | 2.7 MB |

### Secciones de Referencia
Annotations (10), Constants (239), Functions (475), Keywords (15), Operators (21), Types (20), Variables (161)

### Secciones del Manual de Usuario
Welcome, Primer, Language, Visuals, Concepts, Writing, FAQ, Error Messages, Release Notes, Migration Guides, Where Can I Get More Information

## 🛠️ Instalación

### Requisitos
- Python 3.10-3.12 recomendado para la extracción completa. Python 3.14 puede resolver dependencias, pero en Windows puede forzar builds nativos de paquetes como `lxml` vía Crawl4AI.

### 1. Clonar el repositorio:
```bash
git clone https://github.com/faustoevillegas86/Pine_Script_v6_doc.git
cd Pine_Script_v6_doc
```

### 2. Instalar dependencias:
```bash
python setup.py
```

O manualmente:
```bash
pip install -r requirements.txt
python -m playwright install chromium
```

## 🚀 Uso

### Ejecutar Extracción Completa
```bash
python src/run_all.py
```

### Ejecutar Individualmente
```bash
python src/extract_urls.py     # Extraer solo URLs
python src/extract_content.py  # Extraer solo contenido
python src/extract_apps_script_urls.py     # URLs Apps Script (ES-419)
python src/extract_apps_script_content.py  # Contenido Apps Script (ES-419)
```

## 📁 Estructura del Proyecto

```
Pine_Script_v6_doc/
├── README.md
├── requirements.txt
├── setup.py                  # Instala todas las dependencias
├── src/
│   ├── run_all.py            # Ejecuta extracción completa
│   ├── extract_urls.py       # Extracción de URLs
│   └── extract_content.py    # Extracción de contenido
│   ├── extract_apps_script_urls.py     # URLs Apps Script (ES-419)
│   └── extract_apps_script_content.py  # Contenido Apps Script (ES-419)
└── output/
    ├── reference_urls.md     # 941 URLs de Referencia
    ├── reference_content.md  # Documentación de referencia completa
    ├── docs_urls.md          # 71 URLs de Docs
    └── docs_content.md       # Manual de usuario completo
    ├── apps_script_urls.md   # URLs de Apps Script (ES-419)
    └── apps_script_content.md # Contenido Apps Script (ES-419)
```

## 📝 Archivos de Salida

| Archivo | Descripción |
|---------|-------------|
| `reference_urls.md` | URLs de los 941 items de referencia |
| `reference_content.md` | Referencia API completa (funciones, tipos, constantes, etc.) |
| `docs_urls.md` | URLs de las 71 páginas de documentación |
| `docs_content.md` | Manual de usuario completo con tutoriales y guías |
| `apps_script_urls.md` | URLs de secciones/subsecciones Apps Script (ES-419) |
| `apps_script_content.md` | Contenido Apps Script (ES-419) sin barra lateral |

## 🔧 Dependencias

| Paquete | Propósito |
|---------|-----------|
| crawl4ai | Framework de web scraping |
| beautifulsoup4 | Parsing de HTML |
| playwright | Automatización de navegador |
| requests | Peticiones HTTP |
| aiofiles | Operaciones de archivo asíncronas |

---

**Fuente**: Documentación de Pine Script V6 de TradingView  
**Framework**: [Crawl4Ai](https://github.com/unclecode/crawl4ai)  
**Última Actualización**: Febrero 2026
