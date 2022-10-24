import numpy as np
import matplotlib.pyplot as plt
#
# N = 10
# data = np.random.random((N, 4))
# labels = ['point{0}'.format(i) for i in range(N)]
#
# plt.subplots_adjust(bottom = 0.1)
# plt.scatter(
#     data[:, 0], data[:, 1], marker='o', c=data[:, 2], s=data[:, 3] * 1500,
#     cmap=plt.get_cmap('Spectral'))
#
# for label, x, y in zip(labels, data[:, 0], data[:, 1]):
#     plt.annotate(
#         label,
#         xy=(x, y), xytext=(-20, 20),
#         textcoords='offset points', ha='right', va='bottom',
#         bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.5),
#         arrowprops=dict(arrowstyle = '->', connectionstyle='arc3,rad=0'))
#
# plt.show()

pr_num = 4
pk_num = 10
pr_shift = 50
pk_shift = 30
first_pr_n = 3
first_pk_n = 4

points = []
for pr_n in range(pr_num):
    for pk_n in range(pk_num):
        point_number = ((pr_n * pk_num + pk_n) + 1) * ((pr_n+1)%2) + (pr_n % 2) * ((pr_n + 1) * pk_num - pk_n)
        # point_number = ((pr_n * pk_num + pk_n)+1) * (pr_n+1)%2 + (pr_n%2)*((pr_n+1)*pk_num - pk_n)
        label = '({},{}) : {}, {}'.format(pk_n + first_pk_n, pr_n + first_pr_n, point_number, pk_n)
        points.append([pr_n * pr_shift, pk_n * pk_shift, label])


# plt.ylim(-50, 320)
# plt.xlim(-50, 150)
fig = plt.figure(figsize=(10, 8))
plt.scatter([point[0] for point in points], [point[1] for point in points])
for point in points:
    plt.annotate(point[2], xy=(point[0], point[1]))
plt.gca().set_aspect('equal')
plt.show()