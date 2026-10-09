from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class Source:
    source_id: str
    text: str
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class RequestResult:
    source_id: str
    category: str
    summary: str
    available: list[str]
    missing: list[str]
    status: str
    next_step: str
    draft: str | None
    policy_conflict: bool = False
    evidence: tuple[str, ...] = ()


@dataclass(frozen=True)
class Requirement:
    name: str
    kind: str
    value: Any
    source_id: str = "B00"


@dataclass(frozen=True)
class Proposal:
    name: str
    sessions: int
    minutes_per_session: int
    participants: int
    materials: bool
    final_price: float | None
    quoted_price: float
    taxes_included: bool
    recording_days: int | None
    dates_confirmed: bool = False
    source_id: str = ""


@dataclass(frozen=True)
class ProposalResult:
    proposal: Proposal
    covered: list[str]
    missing_or_unconfirmed: list[str]
    non_comparable: list[str]
    questions: list[str]
    evidence: tuple[str, ...]


@dataclass(frozen=True)
class ComparisonResult:
    requirements: list[Requirement]
    proposals: list[ProposalResult]
    provisional_conclusion: str
    actions_blocked: list[str]
