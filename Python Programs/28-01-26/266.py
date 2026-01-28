def lateral_surface_area_cube(side_length):
    if side_length < 0:
        raise ValueError("Side length must be non-negative")
    
    lateral_surface_area = 4 * (side_length ** 2)
    return lateral_surface_area


print(lateral_surface_area_cube(3))