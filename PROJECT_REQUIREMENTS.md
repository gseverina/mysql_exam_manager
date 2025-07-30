# MySQL Exam Manager - Requisitos del Proyecto

Este proyecto tiene como objetivo facilitar la evaluación de estudiantes en materias relacionadas con MySQL mediante un sistema basado en Git y Docker. El flujo de trabajo está diseñado para ser repetible y escalable en múltiples cursos y ciclos lectivos.

## 🎯 Objetivo Principal

Evaluar a estudiantes mediante exámenes prácticos de MySQL que se resuelven de forma local o remota, con herramientas automatizadas para la entrega, corrección y retroalimentación.

---

## 📦 Estructura del Proyecto

- `/templates/`: Plantillas reutilizables para distintos tipos de exámenes.
- `/exams/`: Exámenes creados a partir de templates, uno por estudiante.
- `/scripts/`: Scripts para crear exámenes, inicializar bases de datos, corregir y reportar.
- `docker-compose.yaml`: Entorno local de base de datos MySQL.
- `README.md`: Instrucciones generales de uso.

---

## 🚦 Flujo de Trabajo

### 1. Crear Templates de Examen

El docente puede crear templates con:

- Enunciado (`README.md`)
- Script de inicialización SQL (`schema.sql`)
- Casos de prueba (`tests.sql`, opcional)

### 2. Crear un Examen

Un script permite crear una nueva instancia de examen para un curso:

```bash
python3 scripts/new_exam.py \
  --exam-name "2025-midterm" \
  --template "basic-join" \
  --students-file students.csv
```

Esto genera una carpeta por estudiante bajo `/exams/`.

### 3. Entrega del Estudiante

Cada estudiante recibe una carpeta con:

- Enunciado
- Script para levantar su entorno (`docker-compose.yaml`)
- Carpeta para incluir sus respuestas (`solution.sql` o similar)

### 4. Corrección

El docente puede corregir las entregas con un script de grading:

```bash
python3 scripts/grade_exam.py --exam-name "2025-midterm"
```

Opcionalmente puede generar reportes o notificar a los alumnos.

---

## 🔧 Requisitos Técnicos

- Python 3.9+
- Docker y Docker Compose
- Git
- MySQL client (para pruebas locales o conexión a servidor remoto)

---

## 📌 Funcionalidades Futuras (Propuestas)

- Validación automática de respuestas con tests SQL
- Reportes individuales en PDF o HTML
- Sistema de feedback por alumno
- Soporte para entornos remotos (Render, Fly.io, AWS)
- Interfaz gráfica o CLI interactiva

---

## 🧪 Ejemplos de Templates

- `basic-join`: Consulta con `JOIN` simple
- `aggregation`: Agrupaciones y funciones de agregación

---

## 📁 Entorno del Alumno

Cada alumno podrá correr:

```bash
docker-compose up -d
```

Y ejecutar su SQL en la base `exam_db`.

---

## 👨‍🏫 Revisión del Docente

Scripts planeados:

- `list_templates.py`: Lista los templates disponibles
- `list_exams.py`: Lista exámenes ya generados
- `grade_exam.py`: Evalúa entregas
- `notify_results.py`: (futuro) Notifica resultados por email

---

## ✅ Estado Actual

- [x] Scripts para crear examen
- [x] Estructura de templates y examenes
- [x] Docker Compose básico
- [ ] Script de grading
- [ ] Mejora de documentación y CLI
- [ ] Ejemplos de templates y entregas