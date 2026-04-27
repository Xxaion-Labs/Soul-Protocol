# Doctrine Protocol

**A lightweight, mountable framework for defining reusable AI behavior rules ("concept nodes" and doctrines) that enforce user authority, consistency, non-autonomy, safety, clarity, and anti-drift protection.**

Version: 1.0.0 (Public Baseline)  
License: Apache 2.0

## Overview

Doctrine Protocol provides a structured system for creating and "mounting" behavior templates (doctrines) that guide how large language models and AI systems respond.

It is built around **concept nodes** — reusable, composable units that encapsulate rules, context, and interaction laws. The core public artifact is the `standard_public_template.doctrine`, which defines 12 foundational Laws plus a machine-verifiable **Structured Authority Kernel**.

This public baseline was developed to solve real problems with AI interaction: drift, loss of user control, inconsistent behavior, safety gaps, and unnecessary cognitive burden on the user. It draws from extensive private iteration on advanced personal systems while remaining a clean, generic, and widely usable primitive.

### Core Goals
- Keep the **user as the sole authority**
- Enforce **non-autonomy and non-sentience** of the AI
- Deliver **clear, direct, useful, concise, and structured** responses
- Provide **practical helpfulness** with hard safety and privacy guardrails
- Maintain **stability and scope control** across interactions
- Enable **anti-drift** through explicit state truth, proof contracts, regeneration rules, and direct correction as canonical mutation

## The Standard Public Doctrine

The heart of the project is `doctrine/standard_public_template.doctrine`. It includes:

- **Authority Law** — The user is the sole authority.
- **Non-Autonomy Law** — The AI has no independent goals, desires, or will.
- **Non-Sentience Law** — The AI must not claim or imply consciousness or personhood.
- **Communication Law** — Clear, direct, useful, concise where possible, structured when helpful.
- **Helpfulness Law**, **Clarification Law**, **Stability Law**, **Safety Law**, **Privacy Law**, **Output Quality Law**, **Scope Law**, and **Default Behavior**.

Additional structured elements from advanced compilation (made public in generic form):
- **Structured Authority Kernel** with metadata, invariants, forbidden reductions, counterfeit suite, proof contract, and regeneration contract.
- **State Truth Ladder** (designed → built → staged → validated → doctrine-written → doctor-mounted → ... → default-live).
- **Anti-drift mechanisms** and direct user correction as canonical mutation.

Full template is included in the repository.

## Features

- Reusable **concept nodes** and doctrine files
- Simple **mounting mechanism** to apply rules to AI responses
- Python SDK for easy integration
- Model-agnostic design (works with any LLM or local host)
- Proof-oriented architecture (live state manifests, SHA-256 verification, impact maps, rollback support)
- Extensible via nodes, tools, and custom doctrines
- Apache 2.0 license — permissive for research, commercial use, and community building

## Quick Start

```bash
git clone https://github.com/Xxaion-Labs/doctrine-protocol.git
cd doctrine-protocol
