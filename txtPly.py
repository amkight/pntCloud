import open3d as o3d
from pyntcloud import PyntCloud


pcd = o3d.io.read_point_cloud("pt_018.txt", format="xyz")
o3d.io.write_point_cloud("pt_018.ply", pcd, write_ascii=True)

pcd = o3d.io.read_point_cloud("pt_019.txt", format="xyz")
o3d.io.write_point_cloud("pt_019.ply", pcd, write_ascii=True)

pcd = o3d.io.read_point_cloud("pt_020.txt", format="xyz")
o3d.io.write_point_cloud("pt_020.ply", pcd, write_ascii=True)

pcd = o3d.io.read_point_cloud("pt_021.txt", format="xyz")
o3d.io.write_point_cloud("pt_021.ply", pcd, write_ascii=True)

pcd = o3d.io.read_point_cloud("pt_022.txt", format="xyz")
o3d.io.write_point_cloud("pt_022.ply", pcd, write_ascii=True)

pcd = o3d.io.read_point_cloud("pt_023.txt", format="xyz")
o3d.io.write_point_cloud("pt_023.ply", pcd, write_ascii=True)

pcd = o3d.io.read_point_cloud("pt_024.txt", format="xyz")
o3d.io.write_point_cloud("pt_024.ply", pcd, write_ascii=True)

pcd = o3d.io.read_point_cloud("pt_025.txt", format="xyz")
o3d.io.write_point_cloud("pt_025.ply", pcd, write_ascii=True)

pcd = o3d.io.read_point_cloud("pt_026.txt", format="xyz")
o3d.io.write_point_cloud("pt_026.ply", pcd, write_ascii=True)

# pcd = o3d.io.read_point_cloud("pt_027.txt", format="xyz")
# o3d.io.write_point_cloud("pt_027.ply", pcd, write_ascii=True)
#

