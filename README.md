# Yakoon Contacts

**Status: Early development**

The first business application built on Yakoon: customer relationship
management.

Contacts is the reference for what an application on Yakoon looks like. It
gives a team a shared, searchable customer directory with which they can
work and against which the platform's runtime, store and application model
are validated in real use.

## What Contacts does

A contact is a person or company with the usual profile — name, company,
email, phone, address, notes. Contacts are created, changed, found and
removed through simple commands:

| Command | Purpose |
|---------|---------|
| `contact/add` | Create a contact |
| `contact/list` | List all contacts |
| `contact/find` | Search contacts by any profile field |
| `contact/show` | Show one contact in detail |
| `contact/edit` | Change a contact |
| `contact/delete` | Remove a contact |

Search is not limited to names: any field (company, email, city, …) can be
queried, so a directory stays navigable as it grows.

## Why it exists

Yakoon's own growth is driven by building real software on it. Contacts is
that build project — a small, complete application that exercises the
platform surface end to end: capabilities, runtime services, persistence
and identity. It doubles as the pattern future applications follow.

## Where it goes next

Contacts is deliberately small today. The direction is a full CRM —
accounts, addresses, interaction history and follow-ups — built on the same
command model.

## Technical reference

The application runs as a Yakoon capability tree mounted under `/opt/contacts`
inside a Yakoon environment. Each command is a thin entry point (`.yak/yak.yml`
under `structure/`) into the `y5n-caps-contacts` package.

Persistence goes through Yakoon's stores: an event store for the documents
plus a sequencer for generated ids, defined by the app's `contacts` store
profile. The repository ships PostgreSQL provisioning scripts that create a
dedicated `yakoon_contacts` database with the required store tables.

## Links

- Developer setup: [yakoon-runtime/developer](https://github.com/yakoon-runtime/developer)
- Runtime: [yakoon-runtime/runtime](https://github.com/yakoon-runtime/runtime)