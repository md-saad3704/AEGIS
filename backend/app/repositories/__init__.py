"""
Repository layer for AEGIS domain persistence.

Repositories provide a boundary between application services and the
SQLAlchemy models. This keeps database-specific operations out of the
simulation, ETA, traffic, signal, and corridor services.
"""