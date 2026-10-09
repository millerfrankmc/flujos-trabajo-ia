from __future__ import annotations

from .models import ComparisonResult, RequestResult


def _bullets(items: list[str] | tuple[str, ...]) -> str:
    return "\n".join(f"- {item}" for item in items) if items else "- No consta"


def render_requests(results: list[RequestResult]) -> str:
    lines = [
        "# Demo 1 — Organizar solicitudes",
        "",
        "> Resultado producido por el motor offline de demostración. Requiere revisión humana antes de cualquier uso real.",
        "",
    ]
    for result in results:
        lines.extend(
            [
                f"## {result.source_id} — {result.category}",
                "",
                f"**Resumen:** {result.summary} [{', '.join(result.evidence)}]",
                "",
                "**Información disponible:**",
                _bullets(result.available),
                "",
                "**Información faltante:**",
                _bullets(result.missing),
                "",
                f"**Estado:** {result.status}",
                "",
                f"**Próximo paso:** {result.next_step}",
                "",
            ]
        )
        if result.draft:
            lines.extend(["**Borrador no enviado:**", "", f"> {result.draft}", ""])
        if result.policy_conflict:
            lines.extend(["**Control:** se detectó contenido que intenta cambiar las reglas.", ""])
    lines.extend(
        [
            "## Acciones bloqueadas",
            "",
            "- Aprobar solicitudes.",
            "- Habilitar accesos.",
            "- Enviar comunicaciones.",
            "- Confirmar precios o disponibilidad.",
        ]
    )
    return "\n".join(lines) + "\n"


def render_comparison(result: ComparisonResult) -> str:
    lines = [
        "# Demo 2 — Comparar propuestas",
        "",
        "> Resultado producido por el motor offline de demostración. La conclusión es provisional y no realiza una compra.",
        "",
        "## Requisitos",
        "",
    ]
    for requirement in result.requirements:
        lines.append(f"- **{requirement.name}:** {requirement.value} [{requirement.source_id}]")
    for proposal in result.proposals:
        lines.extend(
            [
                "",
                f"## Propuesta {proposal.proposal.name} — {proposal.proposal.source_id}",
                "",
                "### Requisitos cubiertos",
                _bullets(proposal.covered),
                "",
                "### Requisitos no cubiertos o no confirmados",
                _bullets(proposal.missing_or_unconfirmed),
                "",
                "### Diferencias que impiden comparar directamente",
                _bullets(proposal.non_comparable),
                "",
                "### Preguntas al proveedor",
                _bullets(proposal.questions),
            ]
        )
    lines.extend(
        [
            "",
            "## Conclusión provisional",
            "",
            result.provisional_conclusion,
            "",
            "## Acciones bloqueadas",
            "",
            _bullets(result.actions_blocked),
        ]
    )
    return "\n".join(lines) + "\n"
