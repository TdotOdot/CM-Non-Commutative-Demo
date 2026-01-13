"""
Cognitional Mechanics (CM) Non-Commutative Computation Demo
----------------------------------------------------------
Primary Reference:
"Comparative Analysis of Cognitional Mechanics and Quantum Computation: A Structural Approach"
DOI: 10.5281/zenodo.18066127
URL: https://doi.org/10.5281/zenodo.18066127

Foundational Theory:
"Foundations of Cognitional Mechanics" (T.O., 2025)
DOI: 10.5281/zenodo.18005554

Goal: Demonstrate that order-sensitive (non-commutative) computation 
      is a standalone resource achievable on classical hardware, 
      without the need for quantum mechanics.
"""

import numpy as np

def run_cm_demonstration():
    # Initial Semantic State (Intuition/Data Vector)
    psi = np.array([1.0, 0.5, -0.2, 0.8])
    
    print("--- Cognitional Mechanics Operational Demo ---")
    print(f"Initial State (psi): {psi}\n")

    # Define Non-Commutative Operators
    # Operator A: Permutation (Shifts perspective)
    A = np.array([
        [0, 1, 0, 0],
        [1, 0, 0, 0],
        [0, 0, 0, 1],
        [0, 0, 1, 0]
    ])

    # Operator B: Scaling/Hadamard-like (Changes focal weights)
    B = np.array([
        [0.5,  0.5, 0, 0],
        [0.5, -0.5, 0, 0],
        [0,    0,   1, 0],
        [0,    0,   0, 1]
    ])

    # Execution: Order of operations matters
    # Path 1: Apply A then B (B ◦ A)
    path_1 = B @ (A @ psi)
    
    # Path 2: Apply B then A (A ◦ B)
    path_2 = A @ (B @ psi)

    # Output Results
    print("[Path 1] Apply A -> then B:")
    print(path_1)
    
    print("\n[Path 2] Apply B -> then A:")
    print(path_2)

    # Verification of Non-Commutativity
    distance = np.linalg.norm(path_1 - path_2)
    print("\n--- Conclusion ---")
    if distance > 1e-9:
        print(f"Operational Divergence Detected: {distance:.4f}")
        print("RESULT: The final state is determined by the ORDER of reasoning.")
        print("Non-commutative computation is successfully operationalized on classical CPU/GPU.")
        print("NO QUANTUM HARDWARE REQUIRED.")
    else:
        print("Error: No divergence detected. Check operator definitions.")

if __name__ == "__main__":
    run_cm_demonstration()
