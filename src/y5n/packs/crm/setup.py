from __future__ import annotations

from y5n.sdk import ports
from y5n.sdk.store_client import StoreClient

from .services import ContactService, Namespaces


async def main():

    namespaces = Namespaces()
    store = StoreClient()

    for spec in ContactService.index_specs():
        await store.ensure_indexes(
            namespace=namespaces.contact_namespace(), specs=[spec]
        )

    contacts = ContactService(
        on_get=store.get,
        on_replace=store.replace,
        on_get_many=store.get_many,
        on_scan=store.scan,
        on_delete=store.delete,
        on_query_index=store.query_index,
        on_next_id=store.next_id,
    )

    ports.publish("crm.contact.service", contacts)
    ports.publish("crm.namespaces", namespaces)
