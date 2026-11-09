"""Ham HTTP istek metnini bölümlerine ayırır (method, uri, headers, body)."""
from __future__ import annotations

import re
from dataclasses import dataclass, field

_SPLIT_HEAD_BODY = re.compile(r"\r?\n\r?\n", re.MULTILINE)


@dataclass
class ParsedRequest:
    method: str
    uri: str
    version: str
    headers: dict[str, str] = field(default_factory=dict)
    body: str = ""

    @property
    def path(self) -> str:
        return self.uri.split("?", 1)[0]

    @property
    def query(self) -> str:
        return self.uri.split("?", 1)[1] if "?" in self.uri else ""

    def payload(self) -> str:
        """Header'lar hariç saldırı yüzeyi: URI + body."""
        return self.uri if not self.body else f"{self.uri}\n{self.body}"

    def attack_surface(self) -> str:
        """URI + body + kalıp dışı header değerleri.

        DS-Augmented sürümlerinde payload'lar Cookie/Referer gibi header'lara da enjekte edilmiştir.
        Tarayıcının standart gönderdiği ve saldırı yüzeyi olmayan header'lar (User-Agent, Accept*,
        Sec-*, Host vb.) dışarıda bırakılır; böylece ortak tarayıcı header'ları benzerliği şişirmez.
        """
        extra = [f"{k}: {v}" for k, v in self.headers.items() if k not in BOILERPLATE_HEADERS and not k.startswith("sec-")]
        parts = [f"{self.method} {self.uri}"] + extra + ([self.body] if self.body else [])
        return "\n".join(parts)


BOILERPLATE_HEADERS = {
    "host", "user-agent", "accept", "accept-language", "accept-encoding", "connection",
    "upgrade-insecure-requests", "priority", "te", "cache-control", "pragma", "dnt",
    "content-length", "origin",
}


def parse(raw: str) -> ParsedRequest:
    parts = _SPLIT_HEAD_BODY.split(raw, maxsplit=1)
    head = parts[0]
    body = parts[1].strip("\r\n") if len(parts) > 1 else ""
    lines = head.splitlines()
    first = lines[0] if lines else ""
    tokens = first.split(" ")
    if len(tokens) >= 3:
        method, uri, version = tokens[0], " ".join(tokens[1:-1]), tokens[-1]
    elif len(tokens) == 2:
        method, uri, version = tokens[0], tokens[1], ""
    else:
        method, uri, version = first, "", ""
    headers: dict[str, str] = {}
    for line in lines[1:]:
        if ":" in line:
            k, v = line.split(":", 1)
            headers[k.strip().lower()] = v.strip()
    return ParsedRequest(method, uri, version, headers, body)
