ax1, ay1, ax2, ay2 = map(int, input().split())
bx1, by1, bx2, by2 = map(int, input().split())
cx1, cy1, cx2, cy2 = map(int, input().split())

total_area = (ax2-ax1) * (ay2-ay1)
inter_wb1 = max(0, min(bx2, ax2) - max(ax1, bx1)) * max(0, min(by2, ay2) - max(ay1, by1))
inter_wb2 = max(0, min(cx2, ax2) - max(ax1, cx1)) * max(0, min(cy2, ay2) - max(ay1, cy1))

inter_bbw = max(0, min(ax2,min(bx2, cx2)) - max(ax1,max(bx1,cx1))) * max(0, min(ay2,min(by2, cy2)) - max(ay1,max(by1,cy1)))

total_area -= inter_wb1 + inter_wb2 - inter_bbw
print("YES" if total_area else "NO")
