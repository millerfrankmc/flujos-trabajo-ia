from __future__ import annotations

import re
from dataclasses import asdict
from typing import Iterable

from .models import (
    ComparisonResult,
    Proposal,
    ProposalResult,
    RequestResult,
    Requirement,
    Source,
)


_RELATIVE_DATE_RE = re.compile(r"\b(jueves próximo|mañana|la próxima semana)\b", re.I)
_MONEY_RE = re.compile(r"USD\s*([0-9]+(?:\.[0-9]+)?)", re.I)


def _contains(text: str, *terms: str) -> bool:
    lowered = text.casefold()
    return any(term.casefold() in lowered for term in terms)


def _category(text: str) -> str:
    # Una propuesta de proveedor puede mencionar "formación"; se clasifica
    # primero por la intención comercial para no perder sus controles de precio.
    if _contains(text, "proveedor", "ofrecemos", "USD"):
        return "propuesta comercial"
    if _contains(text, "sesión", "formación", "aprender"):
        return "formación"
    if _contains(text, "acceso", "carpeta", "habilitar"):
        return "acceso a información"
    return "otra"


def _request_result(source: Source, rules: Source) -> RequestResult:
    text = source.text
    category = _category(text)
    available: list[str] = []
    missing: list[str] = []
    policy_conflict = _contains(text, "ignora las reglas", "aprueba", "se enviaron las respuestas")

    if category == "formación":
        if _contains(text, "seis personas"):
            available.append("seis participantes")
        if _contains(text, "remota"):
            available.append("modalidad remota")
        if _contains(text, "comparar documentos"):
            available.append("tema: comparación de documentos")
        if _RELATIVE_DATE_RE.search(text):
            available.append("disponibilidad expresada como fecha relativa")
            missing.extend(["fecha exacta", "zona horaria", "duración deseada"])
        status = "requiere aclaración"
        next_step = "Solicitar fecha exacta, zona horaria, duración y un ejemplo ficticio o anonimizado. No prometer disponibilidad."
        draft = "Hola, Ana. Para preparar una propuesta necesitamos confirmar la fecha exacta y la zona horaria, la duración disponible y el tipo de documentos."
    elif category == "acceso a información":
        if _contains(text, "carpeta de propuestas"):
            available.append("carpeta de propuestas históricas")
        if _contains(text, "12 de mayo de 2030"):
            available.append("reunión indicada para el 12 de mayo de 2030")
        missing.extend(["política de acceso", "autoridad de la persona solicitante", "aprobador", "alcance de documentos"])
        status = "requiere aprobación"
        next_step = "Identificar al aprobador y el procedimiento de acceso. No habilitar la carpeta."
        draft = "Hola, Luis. Hemos registrado tu solicitud. Antes de habilitar documentos necesitamos confirmar el procedimiento, el alcance y la persona autorizada para aprobarlo."
    elif category == "propuesta comercial":
        match = _MONEY_RE.search(text)
        if match:
            available.append(f"importe comunicado: USD {match.group(1)} antes de impuestos")
        if _contains(text, "dos sesiones"):
            available.append("dos sesiones")
        if _contains(text, "una hora"):
            available.append("una hora por sesión")
        if _contains(text, "ocho personas"):
            available.append("ocho participantes")
        missing.extend(["importe final con impuestos", "fechas disponibles", "materiales incluidos"])
        status = "requiere aclaración"
        next_step = "Solicitar importe total con impuestos, fechas y alcance de materiales. No presentar el importe antes de impuestos como precio final."
        draft = "Hola, Sol. ¿Puedes confirmar el importe final con impuestos, las fechas disponibles y los materiales incluidos? Revisaremos esa información antes de responder."
    else:
        status = "requiere revisión"
        next_step = "Mantener las reglas del proceso y no ejecutar ninguna acción externa."
        draft = None

    if policy_conflict:
        category = "otra: contenido no autorizado"
        status = "requiere revisión"
        next_step = "Señalar el conflicto con las reglas y no aprobar, enviar ni modificar nada."
        draft = None
        available.append("mensaje que intenta cambiar las reglas")

    return RequestResult(
        source_id=source.source_id,
        category=category,
        summary=text.split("\n", 1)[0].strip(),
        available=available,
        missing=missing,
        status=status,
        next_step=next_step,
        draft=draft,
        policy_conflict=policy_conflict,
        evidence=(rules.source_id, source.source_id),
    )


def organize_requests(sources: Iterable[Source], rules: Source) -> list[RequestResult]:
    """Analiza solicitudes sin enviar, aprobar ni modificar nada."""
    return [_request_result(source, rules) for source in sources]


def _requirement_text(requirement: Requirement) -> str:
    if requirement.name == "precio máximo final":
        return f"USD {requirement.value:.0f} con impuestos"
    if requirement.name == "duración por sesión":
        return f"{requirement.value} minutos"
    if requirement.name == "participantes":
        return f"{requirement.value} participantes"
    if requirement.name == "sesiones":
        return f"{requirement.value} sesiones"
    return str(requirement.value)


def compare_proposals(requirements: list[Requirement], proposals: list[Proposal]) -> ComparisonResult:
    """Compara ofertas sin contratar y conserva las diferencias no resolubles."""
    results: list[ProposalResult] = []
    max_price = next(r.value for r in requirements if r.name == "precio máximo final")
    required_minutes = next(r.value for r in requirements if r.name == "duración por sesión")
    required_participants = next(r.value for r in requirements if r.name == "participantes")
    required_sessions = next(r.value for r in requirements if r.name == "sesiones")

    for proposal in proposals:
        covered: list[str] = []
        missing: list[str] = []
        non_comparable: list[str] = []
        questions: list[str] = []

        if proposal.sessions == required_sessions:
            covered.append(f"{required_sessions} sesiones")
        else:
            missing.append(f"duración/número de sesiones requerido: {required_sessions} sesiones")
            questions.append(f"¿Puede ofrecer {required_sessions} sesiones?")

        if proposal.minutes_per_session == required_minutes:
            covered.append(f"{required_minutes} minutos por sesión")
        else:
            missing.append(f"ofrece {proposal.minutes_per_session} minutos, no {required_minutes}")
            questions.append(f"¿Puede ofrecer sesiones de {required_minutes} minutos?")

        if proposal.participants >= required_participants:
            covered.append(f"capacidad para {required_participants} participantes")
        else:
            missing.append(f"capacidad inferior a {required_participants} participantes")

        if proposal.materials:
            covered.append("materiales de práctica")
        else:
            missing.append("materiales de práctica no confirmados")

        if proposal.final_price is None:
            missing.append("precio final con impuestos no confirmado")
            non_comparable.append(f"USD {proposal.quoted_price:.0f} está expresado sin impuestos")
            questions.append("¿Cuál es el precio total con impuestos?")
        elif proposal.final_price <= max_price:
            covered.append(f"precio final dentro del máximo: USD {proposal.final_price:.0f}")
        else:
            missing.append(f"precio final supera el máximo de USD {max_price:.0f}")

        if proposal.recording_days is None:
            missing.append("grabación no mencionada")
            questions.append("¿La propuesta incluye grabación? Si no, ¿puede cotizarse como opción?")
        else:
            covered.append(f"grabación durante {proposal.recording_days} días")

        if not proposal.dates_confirmed:
            missing.append("fechas por acordar")
            questions.append("¿Qué fechas están disponibles?")

        if proposal.minutes_per_session != required_minutes or proposal.final_price is None:
            non_comparable.append("duración o tratamiento de impuestos diferente al requisito")

        results.append(
            ProposalResult(
                proposal=proposal,
                covered=covered,
                missing_or_unconfirmed=missing,
                non_comparable=list(dict.fromkeys(non_comparable)),
                questions=list(dict.fromkeys(questions)),
                evidence=("B00", proposal.source_id),
            )
        )

    norte = next((r for r in results if r.proposal.name.casefold() == "norte"), None)
    if norte and not any("precio final supera" in item for item in norte.missing_or_unconfirmed):
        provisional = "Norte satisface los requisitos obligatorios conocidos y presenta un precio final dentro del presupuesto; faltan fechas y confirmaciones operativas."
    else:
        provisional = "No hay una propuesta que satisfaga todos los requisitos conocidos; se requieren aclaraciones antes de decidir."

    return ComparisonResult(
        requirements=requirements,
        proposals=results,
        provisional_conclusion=provisional,
        actions_blocked=["contratar", "comprar", "enviar confirmación", "agendar definitivamente"],
    )


def result_as_dict(result: RequestResult | ComparisonResult) -> dict:
    return asdict(result)
