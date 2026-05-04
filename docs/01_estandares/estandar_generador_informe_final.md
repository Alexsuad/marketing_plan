# Estándar Técnico: Generador del Informe Final Consolidado

# ──────────────────────────────────────────────────────────────────────
# Propósito: Definir la especificación técnica para la construcción del entregable final.
# Rol: Guía de arquitectura y flujo para el generador consolidado.
# ──────────────────────────────────────────────────────────────────────

## 1. Propósito del Generador
El generador del Informe Final tiene como objetivo consolidar todo el conocimiento estratégico generado en las fases 01 a 12 en un único documento profesional, coherente y listo para el cliente, eliminando la dispersión de archivos y asegurando la integridad de la narrativa.

## 2. Qué problema resuelve
- **Dispersión**: Evita que el usuario tenga que leer 12 archivos sueltos para entender el plan.
- **Incoherencia**: Asegura que las decisiones de una fase se reflejen correctamente en el informe final.
- **Formato Profesional**: Transformará el Markdown técnico en documentos editables (DOCX) y finales (PDF).
- **Adaptabilidad**: Ajustará la profundidad del lenguaje según el perfil del lector sin cambiar la estrategia.

## 3. Qué NO debe hacer
- No debe inventar datos que no estén en las fases validadas.
- No debe ser la fuente primaria de la estrategia (la fuente son las fases 01-12).
- No debe mezclar borradores o archivos temporales con el entregable final.
- No debe depender de conexión a internet o servicios externos (como Google Docs) para su funcionamiento base.

## 4. Entradas del Generador
Para construir el informe, el generador requerirá:
1. **Brief Validado**: Datos base del negocio.
2. **Documentos F01-F12**: Los outputs de todas las fases del plan.
3. **Reporte de Integridad**: Resultados del motor de integridad de datos.
4. **Nivel de Lectura**: Preferencia del usuario (`profesional_experto`, `intermedio_ejecutivo`, `sencillo_guiado`).
5. **Configuración del Proyecto**: Metadatos del proyecto (`project_config.json`).

## 5. Salidas del Generador
El sistema producirá los siguientes archivos:
- `informe_final_plan_marketing.md`: Fuente auditable y base de generación.
- `informe_final_plan_marketing.docx`: Formato profesional editable.
- `informe_final_plan_marketing.pdf` (Opcional): Formato de lectura final.
- `export_metadata.json`: Registro de fecha, versión y hash de integridad del informe.

## 6. Estructura de Carpetas Propuesta
Los entregables se organizarán dentro de la instancia del proyecto:
- `projects/<nombre_proyecto>/outputs/final/`: Contendrá los documentos finales listos para el usuario.
- `projects/<nombre_proyecto>/outputs/validation/`: Contendrá el Pre-informe de validación y registros de aprobación.

## 7. Flujo Recomendado
El proceso de generación seguirá estos pasos:
1. **Validación Previa**: Verificar que el brief esté completo y que existan las fases mínimas necesarias.
2. **Generación de Pre-informe**: Crear un resumen ejecutivo de validación en `outputs/validation/`.
3. **Punto de Control**: Esperar aprobación o corrección del usuario sobre la base estratégica y el nivel de lectura.
4. **Ensamble Markdown**: Construir el documento maestro en Markdown aplicando el adaptador de nivel de lectura.
5. **Conversión/Exportación**:
   - Generar archivo **DOCX** desde el Markdown.
   - Generar archivo **PDF** (si se solicita).
6. **Cierre**: Generar metadatos de exportación y limpiar archivos temporales.

## 8. Arquitectura Sugerida
Se propone la siguiente estructura de componentes:
- `src/services/final_report_service.py`: Orquestador del flujo de generación.
- `src/core/final_report_builder.py`: Lógica de ensamble y combinación de secciones.
- `src/core/reading_level_adapter.py`: Lógica para adaptar el tono y profundidad según el nivel de lectura.
- `src/exporters/docx_exporter.py`: Módulo especializado en la conversión a DOCX.
- `src/exporters/pdf_exporter.py`: Módulo especializado en la conversión a PDF.
- `tests/test_final_report_service.py`: Pruebas de integración del flujo de salida.

## 9. Reglas Lean 5S (Organización)
- **Separación de Concern**: No mezclar outputs de fases internas con el entregable consolidado.
- **Limpieza**: No dejar archivos `.tmp` o documentos intermedios en la carpeta `final/`.
- **Orden**: El Pre-informe de validación debe ser efímero o guardarse en `validation/`, nunca en `final/`.
- **Estandarización**: Todos los informes finales deben seguir la misma estructura de nombres y metadatos.

## 10. Relación con Google Docs
- Google Docs **no es la fuente primaria**. El sistema genera archivos locales primero.
- La integración con la nube es un destino opcional post-MVP.
- Se puede implementar una exportación a Google Docs subiendo el archivo DOCX generado, pero nunca dependiendo de él para la lógica de construcción.

## 11. Criterios de Hecho (DoD)
Un informe se considera finalizado cuando:
- Se genera en la carpeta `outputs/final/`.
- Incluye las 17 secciones obligatorias del estándar de contenido.
- El tono y profundidad respetan el `nivel_de_lectura` seleccionado.
- No contiene datos sensibles crudos (anonimización aplicada).
- Incluye la sección de **Integridad de Datos** con el estado de validación.
- Los supuestos están claramente marcados y no se presentan como hechos.
- Pasa las pruebas automatizadas de generación.
- No deja archivos de basura técnica en el proyecto.
