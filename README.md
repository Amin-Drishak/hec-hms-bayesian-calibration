# HEC-HMS Bayesian Calibration (Toy Basin)

**Author:** Muhammad Amin Khan  
**Purpose:** Demonstration of **Bayesian/MCMC calibration** for a simplified HEC-HMS rainfall-runoff model.

---

## Workflow

This project demonstrates Bayesian calibration of a hydrological model using a toy basin setup:

1. Sets up a **toy basin** with synthetic rainfall and flow data.  
2. Uses a **Bayesian sampler** to estimate model parameters.  
3. Produces **uncertainty bounds** on simulated hydrographs.  

> ⚠️ Note: This example uses **synthetic data** for clarity and is intended as a scaffold for real calibration workflows.

---

## Tools & Libraries

- Python 3.x  
- NumPy, Pandas, Matplotlib  
- PyMC3 (for Bayesian inference)  
- HEC-HMS CLI (conceptual use)  

---

## How to Run

1. Clone the repository:
   ```bash
   git clone <your-repo-link>
   cd hec-hms-bayesian-calibration
2. Create and activate a Python virtual environment:
   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate  # Windows
   source .venv/bin/activate # Linux/macOS
### **3. Install dependencies**
   ```bash
   pip install -r requirements.txt
### **4. Run the simulation**
   ```bash
   python main.py
### **5. Check the output hydrograph**
   - The hydrograph image will be saved as `hydrograph.png` in the project folder.

  
