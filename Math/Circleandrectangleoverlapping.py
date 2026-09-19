class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        # Find the closest point on the rectangle to the circle's center
        closest_x = max(x1, min(xCenter, x2))
        closest_y = max(y1, min(yCenter, y2))

        # Calculate the distance between the closest point and circle center
        dx = xCenter - closest_x
        dy = yCenter - closest_y

        # Check if the distance is within the circle's radius
        return dx * dx + dy * dy <= radius * radius
        