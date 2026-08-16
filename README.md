# Yakoon Contacts

*A customer relationship management bundle for Yakoon.*

Contacts provides customer-facing nodes and workflows within the Yakoon
runtime tree. It is designed to be mounted into a workspace under
`/opt/contacts`.

## Structure

```
src/
├── .yak/              — Bundle metadata
└── customer/          — Customer node
    ├── .yak/
    │   └── yak.yml
    └── .yak/run/      — Customer commands
```

## Mounting

Add to `workspace.yml`:

```yaml
workspace:
  /opt/contacts: repos/yakoon-contacts/src
```

## Built on Yakoon

Contacts is implemented as a Yakoon bundle. It extends the node tree
with domain-specific nodes and commands, following the same
patterns — nodes, flows, ports, projections — as every other
Yakoon space.
