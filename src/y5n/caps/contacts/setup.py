from __future__ import annotations

from y5n.sdk import ports, store

from .services import ContactService, Namespaces


async def main():

    namespaces = Namespaces()
    db = store.get("contacts")

    for spec in ContactService.index_specs():
        await db.ensure_indexes(namespace=namespaces.contact_namespace(), specs=[spec])

    contacts = ContactService(
        on_get=db.get,
        on_replace=db.replace,
        on_get_many=db.get_many,
        on_scan=db.scan,
        on_delete=db.delete,
        on_query_index=db.query_index,
        on_next_id=db.next_id,
    )

    ports.publish("contacts.contact.service", contacts)
    ports.publish("contacts.namespaces", namespaces)
