## PASOS PARA LA CONSTRUCCION DE LA APP

# 🏋️‍♂️ GymManager - Sistema de Gestión de Gimnasio

Sistema integral desarrollado con **Django 5.1** y **PostgreSQL** para la administración de un gimnasio. Permite el control de socios, gestión de staff técnico y organización de clases dirigidas con asignación dinámica de descripciones.

## 🚀 Funcionalidades Principales

- **Gestión de Socios:** CRUD completo para miembros (Alta, Baja, Edición y Listado).
- **Control de Entrenadores:** Registro de staff especializado.
- **Sistema de Clases:** 
  - Selección de disciplinas (Yoga, CrossFit, Boxeo, etc.).
  - Asignación automática de descripciones predefinidas según la disciplina.
  - Control de cupos máximos y disponibilidad en tiempo real.
  - Relación Many-to-Many entre Socios y Clases.
- **Interfaz Administrativa:** Panel personalizado para gestión rápida de datos.

## 🛠️ Stack Tecnológico

- **Backend:** Python 3.10 & Django 5.1
- **Base de Datos:** PostgreSQL 14+ (Gestionada vía DBeaver)
- **Frontend:** Django Templates (HTML5, CSS)

## 🔧 Instalación y Configuración

### 1. Preparar el entorno (Ubuntu 22.04)
```bash
python3 -m venv venv
source venv/bin/activate
pip install django psycopg2-binary
