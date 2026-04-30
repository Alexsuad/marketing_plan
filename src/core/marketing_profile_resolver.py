# File: src/core/marketing_profile_resolver.py
# ──────────────────────────────────────────────────────────────────────
# Propósito: Resolver un perfil inicial de marketing según los datos del brief.
# Rol: Lógica central reutilizable para adaptar canales, tono y tácticas.
# ──────────────────────────────────────────────────────────────────────

# Palabras clave para clasificar el tipo de negocio.
# Se buscan en los campos: tipo_negocio, oferta_principal, cliente_objetivo.

PROFILE_KEYWORDS = {
    "ecommerce_transaccional": [
        "ecommerce", "tienda online", "tienda virtual", "shopify", "woocomerce",
        "ventas online", "venta online", "compra online", "tienda propia",
        "envíos", "envios", "envío a domicilio", "producto físico",
        "producto fisico", "ticket medio", "roas", "conversión", "carrito",
        "checkout", "pasarela de pago", "embudo de ventas", "funnel",
        "ventas web", "stock", "inventario", "pedidos", "calzado", "zapatillas",
        "ropa", "moda", "electrónica", "tecnología de consumo",
        "d2c", "direct to consumer", "direct-to-consumer",
        "producto artesanal", "hecho a mano", "exclusividad",
    ],
    "hibrido_producto_servicio": [
        "mantenimiento", "servicio técnico", "servicio tecnico", "reparación",
        "instalación", "instalacion", "soporte técnico", "soporte tecnico",
        "contrato anual", "abono", "mantenimiento preventivo", "post-venta",
        "garantía extendida", "venta y servicio", "venta y mantenimiento",
        "impresora 3d", "maquinaria + servicio", "equipo + soporte",
        "maquinaria", "equipo industrial",
    ],
    "b2b_consultivo": [
        "consultoría", "consultoria", "b2b", "pymes", "pyme", "empresas",
        "corporativo", "corporativa", "tecnología", "tecnologia",
        "informática", "informatica", "soporte tecnológico",
        "logística", "logistica", "legal", "jurídico", "juridico", "contable",
        "auditoría", "auditoria", "erp", "crm", "saas", "software",
        "cloud", "migración", "migracion", "infraestructura",
        "servicios profesionales", "asesoría", "asesoria",
        "outsourcing", "subcontratación", "subcontratacion",
    ],
    "b2c_local_servicios": [
        "estética", "estetica", "peluquería", "peluqueria", "belleza",
        "spa", "masaje", "manicura", "pedicura", "barbería", "barberia",
        "restaurante", "cafetería", "cafeteria", "hostelería", "bares",
        "comida", "fisioterapia", "fisio", "dentista", "dental", "óptica",
        "veterinaria", "gimnasio", "yoga", "bienestar",
        "lavandería", "taller", "cerrajería", "fontanería", "electricista",
        "personas", "familias", "vecinos", "tratamiento", "salud",
        "cuidado personal", "sesión", "sesion",
        "cita previa", "reserva", "servicio local", "local", "barrio",
        "zona urbana", "cercanía", "cercania",
    ],
    "educativo_formativo": [
        "academia", "formación", "formacion", "cursos", "curso",
        "talleres", "taller", "clases", "clase", "educación", "educacion",
        "colegio", "escuela", "instituto", "universidad",
        "capacitación", "capacitacion", "entrenamiento", "training",
        "coaching", "coach", "mentoría", "mentoria", "tutor",
        "idiomas", "inglés", "ingles", "refuerzo", "online", "e-learning",
    ],
    "b2c_producto_ecommerce": [
        "consumidor final", "venta directa", "tienda", "regalos", "ropa",
        "accesorios", "hogar", "cosmética", "cosmetica", "moda",
        "dropshipping", "marketplace", "amazon", "mercadolibre", "compra online",
    ],
    "b2b_producto_industrial": [
        "mayorista", "distribución", "distribucion", "distribuidor", "suministro",
        "fabricación", "fabricacion", "fábrica", "fabrica", "maquinaria",
        "componentes", "repuestos", "catálogo", "catalogo", "b2b", "industrial",
        "volumen", "pedidos grandes", "insumos", "materia prima", "equipamiento",
    ],
    "retail_fisico": [
        "tienda física", "tienda fisica", "comercio", "local comercial", "mostrador",
        "escaparate", "probador", "calle", "avenida", "centro comercial", "retail",
        "ferretería", "ferreteria", "supermercado", "almacén", "almacen",
        "tienda", "punto de venta", "pago en caja", "stock local", "venta",
        "productos", "artículos", "articulos", "local", "barrio",
        "zona urbana", "comercio local", "tienda de barrio",
    ],
}


# Definición completa de cada perfil de marketing.
PROFILES = {
    "b2b_consultivo": {
        "marketing_profile": "b2b_consultivo",
        "profile_reason": (
            "El negocio ofrece servicios profesionales o técnicos complejos a empresas. "
            "El ciclo de venta es largo y se basa en autoridad y confianza."
        ),
        "recommended_channel_families": [
            {"name": "Venta Consultiva / Contacto Directo", "objective": "Generar confianza y cerrar ventas mediante asesoramiento.", "effort": "Alto", "risk": "Medio", "cost": "Bajo"},
            {"name": "Alianzas Profesionales y Referidos", "objective": "Captar clientes mediante el aval de terceros.", "effort": "Medio", "risk": "Bajo", "cost": "Bajo"}
        ],
        "secondary_channel_families": [
            {"name": "LinkedIn / Redes Profesionales", "utility": "Validar autoridad y marca personal/empresa.", "effort": "Medio", "risk": "Bajo", "cost": "Medio"},
            {"name": "Email Marketing B2B", "utility": "Mantener contacto con prospectos en ciclos largos.", "effort": "Bajo", "risk": "Bajo", "cost": "Bajo"}
        ],
        "avoid_channel_families": [
            {"name": "TikTok / Entretenimiento masivo", "reason": "Baja intención de compra profesional."},
            {"name": "Ads de producto masivo", "reason": "Dificultad de segmentar decisores sin alto desperdicio."}
        ],
        "tone_guidelines": ["Profesional", "Autoritario", "Educativo", "Cercano"],
        "terminology": {
            "accion_principal": "contratar",
            "cliente": "cliente/empresa",
            "oferta": "servicio consultivo"
        },
        "tactical_focus": ["Guiones de venta", "Listado de empresas diana", "Contenido educativo especializado"],
        "risk_notes": ["Ciclo de venta muy lento", "Dependencia de fundadores/expertos"]
    },
    "b2c_local_servicios": {
        "marketing_profile": "b2c_local_servicios",
        "profile_reason": (
            "Negocio de servicios personales en una zona geográfica específica. "
            "Ciclo de venta corto basado en visibilidad local y reseñas."
        ),
        "recommended_channel_families": [
            {"name": "Google Business Profile / Maps", "objective": "Captar intención de búsqueda local.", "effort": "Bajo", "risk": "Bajo", "cost": "Bajo"},
            {"name": "WhatsApp Business", "objective": "Facilitar reservas y atención rápida.", "effort": "Medio", "risk": "Bajo", "cost": "Bajo"}
        ],
        "secondary_channel_families": [
            {"name": "Instagram / Redes Visuales", "utility": "Mostrar resultados y ambiente.", "effort": "Medio", "risk": "Bajo", "cost": "Medio"},
            {"name": "Referidos Locales", "utility": "Boca a boca incentivado.", "effort": "Medio", "risk": "Bajo", "cost": "Bajo"}
        ],
        "avoid_channel_families": [
            {"name": "LinkedIn", "reason": "Público no busca servicios locales personales aquí."},
            {"name": "SEO Nacional", "reason": "Competencia irrelevante fuera de la zona de servicio."}
        ],
        "tone_guidelines": ["Cálido", "Visual", "Directo", "Transparente"],
        "terminology": {
            "accion_principal": "reservar",
            "cliente": "vecino/cliente",
            "oferta": "servicio"
        },
        "tactical_focus": ["Optimización de ficha Maps", "Gestión activa de reseñas", "Promociones de bienvenida"],
        "risk_notes": ["Dependencia crítica de la ubicación", "Impacto alto de reseñas negativas"]
    },
    "educativo_formativo": {
        "marketing_profile": "educativo_formativo",
        "profile_reason": "Venta de conocimiento y capacitación. Requiere demostrar resultados y autoridad docente.",
        "recommended_channel_families": [
            {"name": "Contenido Educativo / Lead Magnets", "objective": "Demostrar valor antes de la venta.", "effort": "Alto", "risk": "Bajo", "cost": "Bajo"},
            {"name": "Clases de Prueba / Webinars", "objective": "Reducir barrera de entrada.", "effort": "Alto", "risk": "Medio", "cost": "Medio"}
        ],
        "secondary_channel_families": [
            {"name": "Email Marketing", "utility": "Nutrir a interesados hasta el momento de compra.", "effort": "Medio", "risk": "Bajo", "cost": "Bajo"},
            {"name": "Testimonios de Alumnos", "utility": "Prueba social crítica.", "effort": "Bajo", "risk": "Bajo", "cost": "Bajo"}
        ],
        "avoid_channel_families": [
            {"name": "Ads directos a venta fría", "reason": "Baja conversión sin confianza previa."}
        ],
        "tone_guidelines": ["Inspirador", "Metódico", "Generoso", "Accesible"],
        "terminology": {
            "accion_principal": "inscribirse",
            "cliente": "alumno/estudiante",
            "oferta": "formación"
        },
        "tactical_focus": ["Creación de guías/muestras gratuitas", "Automatización de correos", "Recopilación de casos de éxito"],
        "risk_notes": ["Saturación de oferta gratuita", "Alta tasa de abandono si no hay seguimiento"]
    },
    "b2c_producto_ecommerce": {
        "marketing_profile": "b2c_producto_ecommerce",
        "profile_reason": "Venta directa de productos físicos al consumidor final mediante canales digitales.",
        "recommended_channel_families": [
            {"name": "Meta Ads (Instagram/FB)", "objective": "Generar deseo visual y compra por impulso.", "effort": "Medio", "risk": "Alto", "cost": "Alto"},
            {"name": "SEO de Producto / Shopping", "objective": "Captar búsquedas transaccionales directas.", "effort": "Alto", "risk": "Medio", "cost": "Medio"}
        ],
        "secondary_channel_families": [
            {"name": "Email Marketing / Recuperación de Carritos", "utility": "Maximizar el valor de vida del cliente (LTV).", "effort": "Medio", "risk": "Bajo", "cost": "Bajo"},
            {"name": "Marketing de Influencers", "utility": "Ganar alcance y validación social rápida.", "effort": "Medio", "risk": "Alto", "cost": "Alto"}
        ],
        "avoid_channel_families": [
            {"name": "Llamadas en frío", "reason": "Modelo ineficiente para productos de consumo masivo."},
            {"name": "Canales B2B puros", "reason": "El comprador final no está en modo 'profesional'."}
        ],
        "tone_guidelines": ["Directo", "Dinámico", "Aspiracional", "Confiable (seguridad de pago/envío)"],
        "terminology": {
            "accion_principal": "comprar",
            "cliente": "usuario/comprador",
            "oferta": "producto"
        },
        "tactical_focus": ["Optimización de fichas de producto", "Campañas de Retargeting", "Logística como ventaja competitiva"],
        "risk_notes": ["Márgenes ajustados por costes de envío/ads", "Alta dependencia de algoritmos publicitarios"]
    },
    "b2b_producto_industrial": {
        "marketing_profile": "b2b_producto_industrial",
        "profile_reason": "Suministro de productos, maquinaria o insumos a otras empresas o distribuidores.",
        "recommended_channel_families": [
            {"name": "SEO Técnico / Fichas Técnicas", "objective": "Ser encontrado por compradores técnicos y logísticos.", "effort": "Alto", "risk": "Bajo", "cost": "Medio"},
            {"name": "Ferias / Catálogos / Red Comercial", "objective": "Cerrar acuerdos de volumen y suministro recurrente.", "effort": "Alto", "risk": "Alto", "cost": "Alto"}
        ],
        "secondary_channel_families": [
            {"name": "LinkedIn (Cuenta Empresa)", "utility": "Noticias corporativas y presencia sectorial.", "effort": "Bajo", "risk": "Bajo", "cost": "Bajo"},
            {"name": "Muestras / Demos Industriales", "utility": "Validar calidad en el entorno del cliente.", "effort": "Medio", "risk": "Medio", "cost": "Medio"}
        ],
        "avoid_channel_families": [
            {"name": "Instagram / TikTok (Enfoque estilo de vida)", "reason": "Irrelevante para decisiones industriales de volumen."},
            {"name": "Banners de consumo masivo", "reason": "Desperdicio de impresión en perfiles no decisores."}
        ],
        "tone_guidelines": ["Técnico", "Fiable", "Eficiente", "Sólido"],
        "terminology": {
            "accion_principal": "homologar",
            "cliente": "departamento de compras",
            "oferta": "suministro industrial"
        },
        "tactical_focus": ["Digitalización de catálogos", "Optimización de procesos de pedido recurrente", "Estrategia de ferias"],
        "risk_notes": ["Ciclos de reposición largos", "Dependencia de pocos clientes grandes"]
    },
    "retail_fisico": {
        "marketing_profile": "retail_fisico",
        "profile_reason": "Venta de productos en establecimiento físico. El objetivo es atraer tráfico al local.",
        "recommended_channel_families": [
            {"name": "Google Business Profile / Maps", "objective": "Aparecer cuando el cliente busca 'tienda de X cerca'.", "effort": "Bajo", "risk": "Bajo", "cost": "Bajo"},
            {"name": "Publicidad Local (Folletería/Ads geo)", "objective": "Avisar de promociones y stock disponible.", "effort": "Medio", "risk": "Medio", "cost": "Medio"}
        ],
        "secondary_channel_families": [
            {"name": "Programas de Fidelización (Tarjeta/Puntos)", "utility": "Aumentar la recurrencia del cliente de barrio.", "effort": "Medio", "risk": "Bajo", "cost": "Bajo"},
            {"name": "Escaparatismo / Visual Merchandising", "utility": "Captar atención del tráfico peatonal.", "effort": "Medio", "risk": "Bajo", "cost": "Medio"}
        ],
        "avoid_channel_families": [
            {"name": "Venta telefónica nacional", "reason": "Incoherente con el modelo de cercanía física."},
            {"name": "Twitter", "reason": "Poco efectivo para generar tráfico a tienda de barrio."}
        ],
        "tone_guidelines": ["Amable", "Promocional", "Local", "Útil"],
        "terminology": {
            "accion_principal": "visitar",
            "cliente": "cliente local",
            "oferta": "producto de tienda"
        },
        "tactical_focus": ["Eventos en tienda", "Promociones exclusivas locales", "Cartelería exterior"],
        "risk_notes": ["Limitación geográfica estricta", "Altos costes fijos del local"]
    },
    "estrategia_general_prudente": {
        "marketing_profile": "estrategia_general_prudente",
        "profile_reason": (
            "Perfil híbrido o con información ambigua. Se recomienda un enfoque de validación "
            "multicanal moderado antes de escalar."
        ),
        "recommended_channel_families": [
            {"name": "Presencia Digital Mínima", "objective": "Validar qué canal genera más interés inicial.", "effort": "Bajo", "risk": "Bajo", "cost": "Bajo"},
            {"name": "Referidos y Boca a Boca", "objective": "Crecimiento seguro basado en calidad.", "effort": "Bajo", "risk": "Bajo", "cost": "Bajo"}
        ],
        "secondary_channel_families": [
            {"name": "Contacto Directo", "utility": "Aprender del cliente en tiempo real.", "effort": "Medio", "risk": "Bajo", "cost": "Bajo"}
        ],
        "avoid_channel_families": [
            {"name": "Inversión alta en canales automáticos", "reason": "Riesgo de pérdida sin perfil validado."}
        ],
        "tone_guidelines": ["Prudente", "Directo", "Adaptable"],
        "terminology": {
            "accion_principal": "conocer",
            "cliente": "prospecto",
            "oferta": "propuesta"
        },
        "tactical_focus": ["Pruebas A/B de mensaje", "Entrevistas a clientes"],
        "risk_notes": ["Lentitud en el escalado", "Necesidad de revisión manual constante"]
    },
    "ecommerce_transaccional": {
        "marketing_profile": "ecommerce_transaccional",
        "profile_reason": "Venta directa de productos físicos con alto volumen de transacciones y optimización de conversión web.",
        "recommended_channel_families": [
            {"name": "Performance Ads (Shopping/Social)", "objective": "Venta directa con retorno medible.", "effort": "Alto", "risk": "Alto", "cost": "Alto"},
            {"name": "Email de Recuperación / Retargeting", "objective": "Recuperar ventas perdidas y aumentar conversión.", "effort": "Medio", "risk": "Bajo", "cost": "Medio"}
        ],
        "secondary_channel_families": [
            {"name": "SEO de Producto / Categoría", "utility": "Captar tráfico orgánico recurrente.", "effort": "Alto", "risk": "Bajo", "cost": "Medio"},
            {"name": "Marketing de Afiliación", "utility": "Escalar ventas mediante terceros.", "effort": "Medio", "risk": "Bajo", "cost": "Variable"}
        ],
        "avoid_channel_families": [
            {"name": "Ferretería / Punto de venta físico", "reason": "Modelo 100% digital."},
            {"name": "Consultoría personalizada", "reason": "Dificulta el escalado transaccional."}
        ],
        "tone_guidelines": ["Directo", "Urgente (moderado)", "Visual", "Transaccional"],
        "terminology": {
            "accion_principal": "comprar ahora",
            "cliente": "usuario",
            "oferta": "producto ecommerce"
        },
        "tactical_focus": ["Embudo de conversión (Checkout)", "Publicidad basada en ROAS", "Logística y devoluciones"],
        "risk_notes": ["Dependencia de costes de publicidad", "Competencia feroz en precios"]
    },
    "hibrido_producto_servicio": {
        "marketing_profile": "hibrido_producto_servicio",
        "profile_reason": "Modelo que combina la venta de un activo físico con un contrato de servicio recurrente (mantenimiento o soporte).",
        "recommended_channel_families": [
            {"name": "Venta Técnica + Contrato de Servicio", "objective": "Cerrar la venta del equipo con recurrencia asegurada.", "effort": "Alto", "risk": "Medio", "cost": "Alto"},
            {"name": "Customer Success / Soporte Preventivo", "objective": "Fidelización y reducción de bajas de servicio.", "effort": "Medio", "risk": "Bajo", "cost": "Medio"}
        ],
        "secondary_channel_families": [
            {"name": "SEO Técnico e Instalación", "utility": "Atraer clientes que buscan la solución completa.", "effort": "Alto", "risk": "Bajo", "cost": "Medio"},
            {"name": "Webinars de Operación", "utility": "Educar en el uso del equipo y valor del soporte.", "effort": "Medio", "risk": "Bajo", "cost": "Bajo"}
        ],
        "avoid_channel_families": [
            {"name": "Venta impulsiva", "reason": "La decisión requiere evaluar el soporte a largo plazo."},
            {"name": "Modelos low-cost sin soporte", "reason": "Canibaliza el valor del servicio recurrente."}
        ],
        "tone_guidelines": ["Seguro", "Técnico", "Acompañante", "Profesional"],
        "terminology": {
            "accion_principal": "adquirir con soporte",
            "cliente": "socio/cliente",
            "oferta": "solución integral"
        },
        "tactical_focus": ["Garantía de disponibilidad", "Proceso de Onboarding", "Gestión de renovaciones de servicio"],
        "risk_notes": ["Complejidad operativa (logística + técnicos)", "Riesgo de incumplimiento de SLA"]
    },
}


def resolve_marketing_profile(brief_data: dict) -> dict:
    """
    Clasifica el tipo de negocio según los datos del brief y devuelve
    un perfil de marketing con canales, tono y tácticas recomendadas.

    Parámetros:
        brief_data (dict): Diccionario con los campos del brief:
            - tipo_negocio
            - oferta_principal
            - cliente_objetivo
            - problema_que_resuelve (opcional para clasificación)

    Retorna:
        dict: Perfil de marketing completo.
    """
    # Campos que analizamos para detectar el perfil.
    text_to_analyze = " ".join([
        brief_data.get("tipo_negocio", ""),
        brief_data.get("oferta_principal", ""),
        brief_data.get("cliente_objetivo", ""),
        brief_data.get("problema_que_resuelve", ""),
    ]).lower()

    # Contar coincidencias con cada perfil.
    scores = {}
    for profile_name, keywords in PROFILE_KEYWORDS.items():
        # Usamos set() para evitar que palabras duplicadas en la lista de keywords puntúen doble
        score = sum(1 for kw in set(keywords) if kw in text_to_analyze)
        scores[profile_name] = score

    # Umbral mínimo: se necesitan al menos 2 matches para clasificar.
    # Con 0 o 1 coincidencia, se usa el perfil fallback (estrategia_general_prudente).
    MIN_MATCHES = 2

    # Si todos los scores son 0, evitar error de max()
    if not any(scores.values()):
        return PROFILES["estrategia_general_prudente"]

    best_profile = max(scores, key=scores.get)
    best_score = scores[best_profile]

    # Si el mejor score no alcanza el umbral mínimo, usar fallback.
    if best_score < MIN_MATCHES:
        return PROFILES["estrategia_general_prudente"]

    # Verificar empates: si hay más de un perfil con el mejor score,
    # se prefiere el primero definido en PROFILE_KEYWORDS (orden de prioridad).
    top_profiles = [p for p, s in scores.items() if s == best_score]
    return PROFILES[top_profiles[0]]
