import open3d as o3d
from pyntcloud import PyntCloud



from pyntcloud import PyntCloud
from pyntcloud.geometry.models.sphere import create_sphere
for i in [18, 19, 20, 21, 22, 23, 24, 25, 26]:
    file = "pt_0" + str(i) + ".ply"
    cloud = PyntCloud.from_file(file)
    convex_hull_id = cloud.add_structure("convex_hull")
    convex_hull = cloud.structures[convex_hull_id]
    print(convex_hull.volume)

