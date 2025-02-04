import math

class Vector:
    def __init__(self, *components):
        # Flatten the components if any are lists
        flattened_components = []
        for component in components:
            if isinstance(component, list):
                flattened_components.extend(component)  # Flatten the list
            else:
                flattened_components.append(component)  # Just add the individual number
       
        # Ensure that all components are numeric
        if not all(isinstance(c, (int, float)) for c in flattened_components):
            raise ValueError("All vector components must be numeric.")
        
        self.vec_obj = [float(c) for c in flattened_components]
        
        # Dynamically create attributes like p1, p2, p3, ...
        for i, val in enumerate(self.vec_obj):
            setattr(self, f'p{i+1}', val)  # Create attributes p1, p2, p3, ...

    def __add__(self, other):
        if len(self.vec_obj) != len(other.vec_obj):
            raise ValueError("Vectors must have the same dimensionality to be added.")
        added_vec = [self.vec_obj[i] + other.vec_obj[i] for i in range(len(self.vec_obj))]
        return Vector(*added_vec)

    def __sub__(self, other):
        if len(self.vec_obj) != len(other.vec_obj):
            raise ValueError("Vectors must have the same dimensionality to be subtracted.")
        subtracted_vec = [self.vec_obj[i] - other.vec_obj[i] for i in range(len(self.vec_obj))]
        return Vector(*subtracted_vec)

    def __mul__(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise ValueError("Scalar multiplication requires a number.")
        scaled_vec = [round(c * scalar, 3) for c in self.vec_obj]
        return Vector(*scaled_vec)

    def dot(self, other):
        if len(self.vec_obj) != len(other.vec_obj):
            raise ValueError("Vectors must have the same dimensionality to compute the dot product.")
        return sum(self.vec_obj[i] * other.vec_obj[i] for i in range(len(self.vec_obj)))

    def magnitude(self):
        return round(math.sqrt(sum(c**2 for c in self.vec_obj)), 3)

    def __repr__(self):
        return f"Vector({', '.join(map(str, self.vec_obj))})"

def vec(*components):
    return Vector(*components)

