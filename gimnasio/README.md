# 🏋️‍♂️ GymManager - Sistema de Gestión de Gimnasio

Sistema profesional desarrollado con **Django 5.1** y **PostgreSQL** para la administración integral de un centro deportivo. Incluye automatización de procesos y gestión de aforo en tiempo real.

## 🚀 Funcionalidades Principales

- **Gestión de Socios:** CRUD completo (Alta, Baja, Edición y Listado) con indicadores de estado (Activo/Inactivo).
- **Control de Entrenadores:** Registro de staff técnico vinculado a disciplinas específicas.
- **Sistema de Clases Inteligente:** 
  - **Automatización:** El modelo asigna descripciones predefinidas automáticamente según la disciplina elegida (Yoga, CrossFit, etc.) mediante la sobrescritura del método `save()`.
  - **Gestión de Aforo:** Cálculo dinámico de plazas disponibles mediante el método `cupo_disponible`.
  - **Inscripciones:** Relación `ManyToManyField` entre Socios y Clases con tabla intermedia visible en **DBeaver**.
- **Seguridad:** Protección de credenciales mediante variables de entorno.

## 🛠️ Stack Tecnológico

- **Backend:** Python 3.10 & Django 5.1
- **Base de Datos:** PostgreSQL 14+ (Administrada con [DBeaver](https://dbeaver.io))
- **Configuración:** [Python-Decouple](https://pypi.org) para gestión de `.env`

## 🔧 Instalación y Configuración

### 1. Preparar el entorno (Ubuntu 22.04)
```bash
python3 -m venv venv
source venv/bin/activate
pip install django psycopg2-binary python-decouple
