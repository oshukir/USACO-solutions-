# import sys
# sys.stdin = open(r"billboard.in", "r")
# sys.stdout = open(r"billboard.out", "w")

# ax1, ay1, ax2, ay2 = map(int, input().split())
# bx1, by1, bx2, by2 = map(int, input().split())
# cx1, cy1, cx2, cy2 = map(int, input().split())

# total_area = (ax2-ax1) * (ay2-ay1) + (bx2-bx1) * (by2-by1)
# intersection_ax = max(min(ax2, cx2) - max(ax1, cx1), 0)
# intersection_ay = max(min(ay2, cy2) - max(ay1, cy1), 0)
# intersection_bx = max(min(bx2, cx2) - max(bx1, cx1), 0)
# intersection_by = max(min(by2, cy2) - max(by1, cy1), 0)

# union = total_area - (intersection_ax * intersection_ay) - (intersection_bx*intersection_by)
# print(union)



#USACO SOLUTION
import sys
sys.stdin = open(r"billboard.in", "r")
sys.stdout = open(r"billboard.out", "w")

class Rect:
    def __init__(self):
        self.x1, self.y1, self.x2, self.y2 = map(int, input().split())

    def area(self):
        return (self.y2 - self.y1) * (self.x2-self.x1)
    
def intersect(p, q):
    x_overlap = max(min(p.x2, q.x2) - max(p.x1, q.x1), 0)
    y_overlap = max(min(p.y2, q.y2) - max(p.y1, q.y1), 0)
    return x_overlap * y_overlap

rect = []
for _ in range(3):
    rect.append(Rect())

answer = rect[0].area() + rect[1].area() - intersect(rect[0], rect[2]) - intersect(rect[1], rect[2])
print(answer)