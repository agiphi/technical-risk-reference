# Technical Risk Reference

A deterministic reference implementation for structured technical-risk assessment.

It demonstrates how evidence from a codebase and its infrastructure can be converted into explicit risk signals and repeatable classification.

**Important:** this is an independent reference implementation. It is not the source code or proprietary methodology of any commercial due-diligence system.

## Architecture

`Target Repository → Static Signals → Architecture Signals → Infrastructure Signals → Risk Classifier → Structured Report`

## Example signals

- oversized modules
- missing tests
- dependency concentration
- configuration exposure
- missing health checks
- infrastructure coupling

## Run

```bash
python -m src.main
```

## Design goals

- deterministic classification
- evidence before conclusions
- explicit scoring inputs
- machine-readable output
- easy extension with additional scanners

The system is a technical reference, not an investment decision engine.

## Architecture

```mermaid
flowchart LR
  A[Target Repository] --> B[Static Signals]
  B --> C[Architecture Signals]
  C --> D[Infrastructure Signals]
  D --> E[Deterministic Classifier]
  E --> F[Structured Report]
```
