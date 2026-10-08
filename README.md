# Cyber-Physical Systems Engineering Master's Repository

Central academic repository tracking coursework, laboratory projects (TPs), simulations, professional modules, and research contributions for the **Master of Science in Cyber-Physical Systems Engineering (CPSE)** at **Arts et Métiers (Campus of Aix-en-Provence)**.

---

## 📌 Program Overview

* **Degree:** Master of Science in Industrial Engineering — Specialization: Cyber-Physical Systems Engineering (CPSE)
* **Institution:** Arts et Métiers Institute of Technology, Campus of Aix-en-Provence
* **Laboratory:** LISPEN (Laboratoire d'Ingénierie des Systèmes Physiques et Numériques)
* **Program Coordinator:** Prof. Esma YAHIA (`Esma.Yahia@ensam.eu`)

---

## 🗂️ Repository Architecture

Every module is structured into its own self-contained directory containing lecture notes, problem sets, practical sessions (TPs), simulation code, and deliverables.

```text
arts-et-metiers-cpse/
│
├── README.md                   # Repository overview and master schedule
├── .gitignore                  # Exclusion rules for build artifacts, virtualenvs, etc.
│
├── modules/
│   ├── professional/           # MPi: Professional Modules (12h each)
│   │   ├── mp1-research-methodology/
│   │   ├── mp2-ai-and-data-analytics/
│   │   ├── mp3-industry-4.0/
│   │   └── mp4-digital-factory-supply-chain/
│   │
│   ├── scientific/             # MSi: Scientific Modules (24h each)
│   │   ├── ms1-digital-mockup-cps/
│   │   ├── ms2-reverse-engineering-prototyping/
│   │   ├── ms3-continuity-cps-heterogeneous/
│   │   ├── ms4-supervision-cps/
│   │   ├── ms5-advanced-robotics/
│   │   └── ms6-mechatronics-control-fault-detection/
│   │
│   └── language/               # MLi: Language Module (24h)
│       └── ml1-advanced-technical-english/
│
├── capestone-project/           # PJR: Long Research Project (128h)
├── master-thesis-internship/   # Semester 2: Research Internship & Master Thesis
│
└── shared/                     # Reusable scripts, report templates, assets
    ├── scripts/
    └── templates/

---

## 📚 Curriculum Breakdown

### 🔬 Scientific Modules (MSi — 24h / 3 ECTS each)

| Module Code | Module Name | Lead Instructor(s) | Key Topics & Tools |
| --- | --- | --- | --- |
| MS1 | Digital Mock-Up for CPS Modeling & Advanced Engineering | P. Véron | Configured DMU, CAD rules, 3DEXPERIENCE Platform |
| MS2 | Reverse Engineering & Digital Prototyping of CPS | JP. Pernot, A. Polette | 3D Scanning, FDM Slicing algorithms, 3D Printing |
| MS3 | Continuity for CPS Engineering in Heterogeneous Context | L. Roucoules, E. Yahia, Q. Brilhault, M. Kleiner | Interoperability, MBSE, Model Transformation, MBOM |
| MS4 | Supervision of CPS during Engineering & Exploitation | E. Yahia, K. Amzil | IIoT architectures, real-time monitoring, sensors, dashboards |
| MS5 | Advanced Robotics | A. Olabi, R. Béarée, Q. Brilhault | Robotic cell dynamics, trajectory generation, path planning |
| MS6 | Mechatronics, Advanced Control, Identification & Fault-Detection | G. Moraru, A. Polette | Non-linear systems, state estimation, AI-driven fault detection |

### 💼 Professional & Language Modules (MPi / MLi — 12h-24h / 2 ECTS each)

| Module Code | Module Name | Lead Instructor(s) | Core Focus |
| --- | --- | --- | --- |
| MP1 | Research Methodology | JP. Pernot, L. Roucoules, C. Wahnoun | Literature review, scientific state-of-the-art, IP & ethics |
| MP2 | Artificial Intelligence & Data Analytics | A. Polette | Machine Learning fundamentals, Neural Networks in Python |
| MP3 | Industry 4.0: Concept, Survey & Future Trends | L. Roucoules, E. Yahia, K. Amzil, C. White | Industry 4.0 pillars, flipped classroom presentations |
| MP4 | Digital Factory & Supply Chain | F. Rosin | SCM (MTO/ATO strategies), serious games, flow modeling |
| ML1 | Advanced Technical English | C. White | Scientific paper writing, debate, interview practice |

### 🧪 Long Research Project & Internship

* **Long Research Project (PJR) — 128h / 2 ECTS:** State-of-the-art investigation, multidisciplinary modeling, and scientific validation conducted between October and January.
* **Research Internship / Master Thesis (Semester 2) — 30 ECTS:** Full-time research project (February to September) in an academic laboratory (LISPEN) or industrial partner, concluding with a written master's thesis and oral defense.

### 🏆 Featured Challenge: I-NOVGAMES Hackathon (MS4 Project)

As part of the practical application for **MS4: Supervision of CPS during Engineering & Exploitation**, we are competing in the **I-NOVGAMES Hackathon (NOVGAMES #4)**. 

Organized by the **Campus of Excellence Industry of the Future Sud** via **I-NOVMICRO** in collaboration with **STMicroelectronics** and **EYCO**, this regional engineering challenge brings together teams across Provence-Alpes-Côte d'Azur to design and prototype smart, connected solutions.

* **Theme:** Preparation for the 2030 Winter Olympic Games & the role of innovation (*Préparation des JOP 2030 et place de l'innovation*).
* **Core Stack:** STMicroelectronics hardware platforms (STM32 microcontrollers, sensor nodes, and wireless connectivity), IIoT data acquisition pipelines, and real-time supervision dashboards.
* **Milestones:**
  * 🚀 **Launch & Design Thinking:** October 23 (Ideation, functional design, pitch)
  * 🛠️ **Development & Prototyping:** October – January (Sensors integration, dashboard development, HIL testing)
  * 🏁 **Final Defense & Demonstration:** January 29


### 🛠️ Environment Setup & Tools

* **OS:** Ubuntu 24.04 LTS / Linux
* **Languages:** Python 3.12+, C/C++
* **CAD & PLM:** Dassault Systèmes 3DEXPERIENCE Platform
* **Simulation & Modeling:** MATLAB / Simulink, Modelica, Python ML Ecosystem (PyTorch/Scikit-Learn)
* **IIoT & Embedded Systems:** ROS 2, FreeRTOS, STMicroelectronics boards
