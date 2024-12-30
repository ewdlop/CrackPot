#Biil Gates

import numpy as np

def cnot(control, target, threshold=0.5):
    """
    Controlled-NOT gate for real-valued bits.
    
    Parameters:
    - control (float): Control bit value between 0 and 1.
    - target (float): Target bit value between 0 and 1.
    - threshold (float): Threshold to decide if control is "active".
    
    Returns:
    - new_target (float): Updated target bit value.
    """
    if control >= threshold:
        # Flip target: If target >= threshold, set to 0; else set to 1
        new_target = 1.0 - target
    else:
        new_target = target
    return new_target

def toffoli(control1, control2, target, threshold=0.5):
    """
    Toffoli (Controlled-Controlled-NOT) gate for real-valued bits.
    
    Parameters:
    - control1 (float): First control bit value between 0 and 1.
    - control2 (float): Second control bit value between 0 and 1.
    - target (float): Target bit value between 0 and 1.
    - threshold (float): Threshold to decide if controls are "active".
    
    Returns:
    - new_target (float): Updated target bit value.
    """
    if (control1 >= threshold) and (control2 >= threshold):
        # Flip target
        new_target = 1.0 - target
    else:
        new_target = target
    return new_target

def controlled_gate(control, target, gate_function, threshold=0.5):
    """
    General controlled gate for real-valued bits.
    
    Parameters:
    - control (float): Control bit value between 0 and 1.
    - target (float): Target bit value between 0 and 1.
    - gate_function (callable): Function to apply to the target when control is active.
    - threshold (float): Threshold to decide if control is "active".
    
    Returns:
    - new_target (float): Updated target bit value.
    """
    if control >= threshold:
        return gate_function(target)
    else:
        return target

# Example gate functions
def not_gate(target):
    """Logical NOT gate."""
    return 1.0 - target

def identity_gate(target):
    """Identity gate (no change)."""
    return target

# Example usage
if __name__ == "__main__":
    # Initialize bits
    control = 0.7
    target = 0.3

    print("Original Target:", target)
    
    # Apply CNOT
    new_target_cnot = cnot(control, target)
    print("After CNOT:", new_target_cnot)
    
    # Apply Toffoli
    control2 = 0.8
    target_toffoli = 0.4
    new_target_toffoli = toffoli(control, control2, target_toffoli)
    print("After Toffoli:", new_target_toffoli)
    
    # Apply a general controlled NOT gate using controlled_gate
    new_target_general = controlled_gate(control, target, not_gate)
    print("After General Controlled NOT:", new_target_general)
