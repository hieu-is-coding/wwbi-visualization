# 📊 Data Visualization - Bureaucracy, Budgets, and the Gender Gap: A Global and Local Perspective

## Dataset: Worldwide Bureaucracy Indicators

### 📝 Dataset Description

The **Worldwide Bureaucracy Indicators (WWBI)** is a rich, cross-national dataset developed by the **World Bank’s Bureaucracy Lab** to fill a longstanding gap in public sector employment and wage data. Unlike perception-based governance measures, the WWBI is grounded in **administrative records and household surveys**, making it one of the most robust and comprehensive datasets of its kind.

The WWBI enables systematic comparisons **within the public sector** and **between public and private sectors**, offering insights into workforce demographics, wage structures, and the fiscal implications of government employment. It supports research on the personnel dimensions of **state capability**, **gender equity**, and the **public sector’s footprint** in national labor markets.

- **Provenance**: World Bank Open Data ([TidyTuesday adaptation – April 30, 2024](https://github.com/rfordatascience/tidytuesday/tree/main/data/2024/2024-04-30))
- **Dimensions**:
  - **Temporal**: 2000–2020
  - **Geographical**: 202 countries
  - **Indicators**: 192
  - **Variable Types**: 
    - **Numerical** – e.g., wage bill as % of GDP, share of female employees
    - **Categorical** – e.g., region, income group, occupation, sector

---

### 💡 Reason for Choosing the Dataset

We chose this dataset because it:
- Provides rich, policy-relevant information on **government workforce composition**.
- Offers a unique lens to explore **gender equity**, **economic priorities**, and **regional disparities**.
- Enables both **global comparison** and **country-specific analysis**, making it ideal for storytelling through visualization.
- Aligns with our interest in public policy, gender studies, and labor economics.

---

## Research Questions

### ❓ **Question 1**
**How has the proportion of GDP allocated to public wages changed over time across different world regions and income groups (2000–2020)?**

#### 🔧 Variables Involved
- `year`
- `indicator_code` = `BI.WAG.TOTL.GD.ZS` (Wage bill as a percentage of GDP)
- `value`
- `country_code`
- `income_group`
- `region`

#### 📊 Plan for Analysis
- Filter dataset for the selected indicator.
- Group by `region`, `income_group`, and `year`.
- Use **line charts** with **facets by region** and **colors by income group**.
- Apply a **log or fixed scale** to emphasize differences.
- Highlight trends, outliers, and policy implications.

---

###  **Question 2**
**How has the gap in female representation between high-level (managers, professionals, technicians) and low-level (clerks, elementary workers) occupations evolved over time (2010–2016) in Vietnam, and how does it differ between the public and private sectors?**

#### 🔧 Variables Involved
- `year`
- `country_code` = Vietnam
- `indicator_code`:  
  - Public sector:
    - `BI.PWK.PUBS.SN.FE.ZS` (Managers)
    - `BI.PWK.PUBS.PN.FE.ZS` (Professionals)
    - `BI.PWK.PUBS.TN.FE.ZS` (Technicians)
    - `BI.PWK.PUBS.CK.FE.ZS` (Clerks)
    - `BI.PWK.PUBS.EO.FE.ZS` (Elementary workers)  
  - Private sector:  
    - `BI.PWK.PRVS.SN.FE.ZS`, `...` (same structure)

- `value`

#### 📊 Plan for Analysis
- Filter for Vietnam from 2010 to 2016 and select relevant gender representation indicators.
- Group into two categories: **high-level** (managers, professionals, technicians) and **low-level** (clerks, elementary workers).
- Calculate average female representation per group and compute the **gap** (high - low).
- Compare public vs. private sectors using **grouped line plots** or **slope charts**.
- Highlight trends in **career mobility** and potential **gender barriers**.

---

### 🔄 External Data
- No additional datasets are required at this stage. If necessary, we may incorporate:
  - Country-level policy events or economic indicators 
  - Regional aggregates or population statistics for normalization (e.g., labor force size)

---

## 📅 Timeline
| Week | Task |
|------|------|
| 1    | Dataset exploration and cleaning |
| 2    | Initial visual drafts for both questions |
| 3    | Refine plots and interpret results |
| 4    | Final presentation and narrative design |

---

## 👨‍👨‍👦 Team Members:
- Phan Thi Hien Chi  
- Nguyen Mau Hoang Hiep
- Pham Minh Hieu

## Reference
FAISAL A. BAIG et al. (2021, October 5). *Introducing the Worldwide Bureaucracy Indicators*. World Bank Blogs. (https://blogs.worldbank.org/en/developmenttalk/introducing-worldwide-bureaucracy-indicators)

Harmon, J. (2024, April 30). *Worldwide Bureaucracy Indicators*. GitHub. (https://github.com/rfordatascience/tidytuesday/tree/main/data/2024/2024-04-30)