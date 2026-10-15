<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/header-dark.svg">
  <img alt="Marina Medeiros, full stack developer in Maceió, Brazil. Software built end to end, from the database to the app in people's hands." src="./assets/header-light.svg" width="100%">
</picture>

<p>
<a href="https://www.linkedin.com/in/marina-paffer/" title="LinkedIn"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/link-linkedin-dark.svg"><img alt="LinkedIn" src="./assets/link-linkedin-light.svg" width="36"></picture></a>
<a href="mailto:marinapaffer@gmail.com" title="Email"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/link-email-dark.svg"><img alt="Email" src="./assets/link-email-light.svg" width="36"></picture></a>
</p>

Hi, I'm Marina. I like owning the whole path of a feature: the data model, the API, and the screen someone uses out in the field
on a weak signal. Today I'm part of the team behind the data platform the State of Alagoas uses
to follow its programs and investments, and at F2J Soluções I build SaaS products with digital signatures,
offline-first apps, and integrations that let AI agents work with real systems. I'm also finishing my Information
Systems degree at IFAL, with a thesis that grew out of a shelter management system I built in a community
outreach project.

### How I work

- **Offline first** when the field demands it: durable queues, idempotent sync, nothing lost when the signal drops.
- **Integrations designed for the people on the other end**: clear errors, deduplication and guides for the teams that send data.
- **Security by default**: single sign-on, tenant isolation, signed requests and privacy by design (LGPD, Brazil's GDPR) from the first table.
- **AI where it helps**: MCP servers that let agents work with real systems.
- **Shipping safely**: Docker, tests before every deploy, blue-green releases and Kubernetes.

<details open>
<summary><h3>Selected work</h3></summary>
<br>

<p>
<picture><source media="(prefers-color-scheme: dark)" srcset="./assets/card-gov-dark.svg"><img alt="Government data platform: the State of Alagoas's data and decision-support platform, with 50+ solutions in production, about 250 users and 40+ native dashboards. Validated imports and APIs for other agencies. React, Node.js, PostgreSQL, Keycloak." src="./assets/card-gov-light.svg" width="49%"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="./assets/card-docs-dark.svg"><img alt="Documents and signatures: document management with qualified ICP-Brasil signatures, batch signing, public signature verification, a local Windows signer in Rust and full-text search with OCR. React, Fastify, Java, Rust." src="./assets/card-docs-light.svg" width="49%"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="./assets/card-offline-dark.svg"><img alt="Apps that work offline: time tracking with facial recognition and kiosks that sign every request, and field service apps on the Play Store and App Store. React Native, Expo, Python, NestJS." src="./assets/card-offline-light.svg" width="49%"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="./assets/card-ai-dark.svg"><img alt="SaaS and AI agents: project and service management with row-level tenant isolation and plan-based features, and MCP servers used by agents in n8n and Gemini. NestJS, Next.js, MCP, Oracle." src="./assets/card-ai-light.svg" width="49%"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="./assets/card-acolhe-dark.svg"><img alt="Acolhe.AL, community outreach project at IFAL and basis of my thesis: helps short-term shelters for people experiencing homelessness manage residents, intake and attendance. Laravel, React, Inertia.js, PostgreSQL." src="./assets/card-acolhe-light.svg" width="49%"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="./assets/card-mariscar-dark.svg"><img alt="Mariscar com Dignidade, community outreach project at IFAL: offline-first app for artisanal shellfish gathering data, an API built with privacy (LGPD) in mind and a researcher dashboard. Flutter, Django, Next.js, PostgreSQL." src="./assets/card-mariscar-light.svg" width="49%"></picture>
<a href="https://github.com/marinamedeirosz/mapa-cc-mhn"><picture><source media="(prefers-color-scheme: dark)" srcset="./assets/project-mapa-cc-mhn-dark.svg"><img alt="mapa-cc-mhn: turns a crustacean (carcinological) collection spreadsheet into interactive maps, filters and statistics, with no programming required. React, Leaflet, TanStack Table, Vitest." src="./assets/project-mapa-cc-mhn-light.svg" width="98.5%"></picture></a>
</p>

<details>
<summary><b>More on this work</b></summary>
<br>

**Government data platform** · Secretariat of Corporate Governance of the State of Alagoas, since 2026, as part of the team.

- Forms, spreadsheet imports reviewed before saving, validation queues, georeferenced maps, and PDF, Word and Excel reports.
- Integration APIs for other state agencies on a durable PostgreSQL queue, with deduplication, masking of personal IDs (CPF) in logs, batch tracking and integration guides. One batch load went from 106 s to 1 s.
- An internal agile management system with kanban, sprints, a productivity dashboard and an MCP server for AI agents.
- Single sign-on with Keycloak and OIDC, a k3s cluster with sandbox and production, and a state data catalog validated in CI.

**Documents and signatures** · F2J Soluções. Java signing service (PDFBox, Bouncy Castle), batch signing, public signature verification with a PDF report, a local Windows signer in Rust with a browser extension and JWS ES256 authorization, full-text search in PostgreSQL with OCR, and a citizen portal.

**Apps that work offline** · F2J Soluções. An offline-first time tracking app with an encrypted contingency queue and idempotent sync, a facial recognition service with hexagonal architecture, kiosks with hardware-backed keys and HTTP message signatures (RFC 9421), and field service apps with branching checklists, geolocation and offline media.

**SaaS and AI agents** · F2J Soluções. Tenant isolation through PostgreSQL row-level security, plan-based features, scoped integration tokens, an MCP server with more than 100 tools, hour tracking with overlap detection, a Next.js site with self-service checkout and an AI pre-sales chat, finance, CRM and HR systems on Oracle, and a WhatsApp sales agent powered by an LLM.

**Mariscar com Dignidade** · Flutter app with local storage (Hive), a durable outbox, background sync and a minimum version policy, and a Django API with idempotent writes, access auditing, consent records and in-app account deletion.

</details>

</details>

<details>
<summary><h3>Technologies</h3></summary>

#### Languages

<img alt="TypeScript" src="https://img.shields.io/badge/TypeScript-151b23?style=for-the-badge&logo=typescript&logoColor=3178C6">
<img alt="JavaScript" src="https://img.shields.io/badge/JavaScript-151b23?style=for-the-badge&logo=javascript&logoColor=F7DF1E">
<img alt="Python" src="https://img.shields.io/badge/Python-151b23?style=for-the-badge&logo=python&logoColor=3776AB">
<img alt="PHP" src="https://img.shields.io/badge/PHP-151b23?style=for-the-badge&logo=php&logoColor=777BB4">
<img alt="Java" src="https://img.shields.io/badge/Java-151b23?style=for-the-badge&logo=openjdk&logoColor=F89820">
<img alt="Dart" src="https://img.shields.io/badge/Dart-151b23?style=for-the-badge&logo=dart&logoColor=0175C2">
<img alt="Rust" src="https://img.shields.io/badge/Rust-151b23?style=for-the-badge&logo=rust&logoColor=FFFFFF">

#### Frontend

<img alt="React" src="https://img.shields.io/badge/React-151b23?style=for-the-badge&logo=react&logoColor=61DAFB">
<img alt="Next.js" src="https://img.shields.io/badge/Next.js-151b23?style=for-the-badge&logo=nextdotjs&logoColor=FFFFFF">
<img alt="Vite" src="https://img.shields.io/badge/Vite-151b23?style=for-the-badge&logo=vite&logoColor=646CFF">
<img alt="Tailwind CSS" src="https://img.shields.io/badge/Tailwind_CSS-151b23?style=for-the-badge&logo=tailwindcss&logoColor=06B6D4">
<img alt="TanStack Query" src="https://img.shields.io/badge/TanStack_Query-151b23?style=for-the-badge&logo=reactquery&logoColor=FF4154">
<img alt="shadcn/ui" src="https://img.shields.io/badge/shadcn%2Fui-151b23?style=for-the-badge&logo=shadcnui&logoColor=FFFFFF">
<img alt="Leaflet" src="https://img.shields.io/badge/Leaflet-151b23?style=for-the-badge&logo=leaflet&logoColor=199900">

#### Backend

<img alt="Node.js" src="https://img.shields.io/badge/Node.js-151b23?style=for-the-badge&logo=nodedotjs&logoColor=5FA04E">
<img alt="NestJS" src="https://img.shields.io/badge/NestJS-151b23?style=for-the-badge&logo=nestjs&logoColor=E0234E">
<img alt="Fastify" src="https://img.shields.io/badge/Fastify-151b23?style=for-the-badge&logo=fastify&logoColor=FFFFFF">
<img alt="Express" src="https://img.shields.io/badge/Express-151b23?style=for-the-badge&logo=express&logoColor=FFFFFF">
<img alt="Laravel" src="https://img.shields.io/badge/Laravel-151b23?style=for-the-badge&logo=laravel&logoColor=FF2D20">
<img alt="Inertia.js" src="https://img.shields.io/badge/Inertia.js-151b23?style=for-the-badge&logo=inertia&logoColor=9553E9">
<img alt="Django" src="https://img.shields.io/badge/Django-151b23?style=for-the-badge&logo=django&logoColor=44B78B">
<img alt="FastAPI" src="https://img.shields.io/badge/FastAPI-151b23?style=for-the-badge&logo=fastapi&logoColor=009688">

#### Mobile

<img alt="React Native" src="https://img.shields.io/badge/React_Native-151b23?style=for-the-badge&logo=react&logoColor=61DAFB">
<img alt="Expo" src="https://img.shields.io/badge/Expo-151b23?style=for-the-badge&logo=expo&logoColor=FFFFFF">
<img alt="Flutter" src="https://img.shields.io/badge/Flutter-151b23?style=for-the-badge&logo=flutter&logoColor=54C5F8">

#### Data

<img alt="PostgreSQL" src="https://img.shields.io/badge/PostgreSQL-151b23?style=for-the-badge&logo=postgresql&logoColor=4169E1">
<img alt="Oracle PL/SQL" src="https://img.shields.io/badge/Oracle_PL%2FSQL-151b23?style=for-the-badge&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI%2BPGcgZmlsbD0ibm9uZSIgc3Ryb2tlPSIjRjgwMDAwIiBzdHJva2Utd2lkdGg9IjIiPjxlbGxpcHNlIGN4PSIxMiIgY3k9IjUiIHJ4PSI4IiByeT0iMyIvPjxwYXRoIGQ9Ik00IDV2MTRjMCAxLjcgMy42IDMgOCAzczgtMS4zIDgtM1Y1Ii8%2BPHBhdGggZD0iTTQgMTJjMCAxLjcgMy42IDMgOCAzczgtMS4zIDgtMyIvPjwvZz48L3N2Zz4%3D">
<img alt="MySQL" src="https://img.shields.io/badge/MySQL-151b23?style=for-the-badge&logo=mysql&logoColor=4479A1">
<img alt="Redis" src="https://img.shields.io/badge/Redis-151b23?style=for-the-badge&logo=redis&logoColor=FF4438">
<img alt="TypeORM" src="https://img.shields.io/badge/TypeORM-151b23?style=for-the-badge&logo=typeorm&logoColor=FE0803">
<img alt="Drizzle" src="https://img.shields.io/badge/Drizzle-151b23?style=for-the-badge&logo=drizzle&logoColor=C5F74F">
<img alt="RabbitMQ" src="https://img.shields.io/badge/RabbitMQ-151b23?style=for-the-badge&logo=rabbitmq&logoColor=FF6600">
<img alt="MinIO" src="https://img.shields.io/badge/MinIO-151b23?style=for-the-badge&logo=minio&logoColor=C72E49">
<img alt="Supabase" src="https://img.shields.io/badge/Supabase-151b23?style=for-the-badge&logo=supabase&logoColor=3FCF8E">
<img alt="Firebase" src="https://img.shields.io/badge/Firebase-151b23?style=for-the-badge&logo=firebase&logoColor=FFCA28">

#### Infrastructure

<img alt="Docker" src="https://img.shields.io/badge/Docker-151b23?style=for-the-badge&logo=docker&logoColor=2496ED">
<img alt="Kubernetes" src="https://img.shields.io/badge/Kubernetes-151b23?style=for-the-badge&logo=kubernetes&logoColor=326CE5">
<img alt="k3s" src="https://img.shields.io/badge/k3s-151b23?style=for-the-badge&logo=k3s&logoColor=FFC61C">
<img alt="GitHub Actions" src="https://img.shields.io/badge/GitHub_Actions-151b23?style=for-the-badge&logo=githubactions&logoColor=2088FF">
<img alt="Nginx" src="https://img.shields.io/badge/Nginx-151b23?style=for-the-badge&logo=nginx&logoColor=009639">
<img alt="Turborepo" src="https://img.shields.io/badge/Turborepo-151b23?style=for-the-badge&logo=turborepo&logoColor=EF4444">
<img alt="Prometheus" src="https://img.shields.io/badge/Prometheus-151b23?style=for-the-badge&logo=prometheus&logoColor=E6522C">
<img alt="Grafana" src="https://img.shields.io/badge/Grafana-151b23?style=for-the-badge&logo=grafana&logoColor=F46800">
<img alt="Sentry" src="https://img.shields.io/badge/Sentry-151b23?style=for-the-badge&logo=sentry&logoColor=FFFFFF">

#### Identity and security

<img alt="Keycloak" src="https://img.shields.io/badge/Keycloak-151b23?style=for-the-badge&logo=keycloak&logoColor=FFFFFF">
<img alt="OpenID Connect" src="https://img.shields.io/badge/OpenID_Connect-151b23?style=for-the-badge&logo=openid&logoColor=F78C40">
<img alt="ICP-Brasil PAdES" src="https://img.shields.io/badge/ICP--Brasil_PAdES-151b23?style=for-the-badge&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI%2BPGcgZmlsbD0ibm9uZSIgc3Ryb2tlPSIjMkRENEJGIiBzdHJva2Utd2lkdGg9IjIiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI%2BPHBhdGggZD0iTTEyIDJsNyAzdjZjMCA1LTMgOS03IDExLTQtMi03LTYtNy0xMVY1eiIvPjxwYXRoIGQ9Ik05IDEybDIgMiA0LTQiLz48L2c%2BPC9zdmc%2B">

#### AI and automation

<img alt="MCP" src="https://img.shields.io/badge/MCP-151b23?style=for-the-badge&logo=modelcontextprotocol&logoColor=FFFFFF">
<img alt="n8n" src="https://img.shields.io/badge/n8n-151b23?style=for-the-badge&logo=n8n&logoColor=EA4B71">
<img alt="Google Gemini" src="https://img.shields.io/badge/Google_Gemini-151b23?style=for-the-badge&logo=googlegemini&logoColor=8E75B2">

</details>

<br>

<sub>Information Systems at IFAL · English: proficient · the images on this page are SVGs built by <a href="./scripts/build_assets.py">one script</a>.</sub>

<br><br>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/marinamedeirosz/marinamedeirosz/output/github-contribution-grid-snake-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/marinamedeirosz/marinamedeirosz/output/github-contribution-grid-snake.svg">
  <img alt="github contribution grid snake animation" src="https://raw.githubusercontent.com/marinamedeirosz/marinamedeirosz/output/github-contribution-grid-snake.svg" width="100%">
</picture>
