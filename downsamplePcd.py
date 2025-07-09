#!/usr/bin/env python3

import open3d as o3d
import sys
import os
import shutil

def downsample_and_replace(pcd_file, voxel_size):
    # Check input file exists
    if not os.path.isfile(pcd_file):
        print(f"Error: File '{pcd_file}' does not exist.")
        sys.exit(1)

    # Load point cloud
    print(f"Loading point cloud from: {pcd_file}")
    pcd = o3d.io.read_point_cloud(pcd_file)
    if not pcd.has_points():
        print("Error: Point cloud is empty or invalid.")
        sys.exit(1)

    # Downsample
    print(f"Downsampling with voxel size: {voxel_size}")
    down_pcd = pcd.voxel_down_sample(voxel_size=float(voxel_size))

    # Backup old file
    backup_file = pcd_file + ".bak.pcd"
    print(f"Backing up original file to: {backup_file}")
    shutil.move(pcd_file, backup_file)

    # Save downsampled point cloud under original filename
    print(f"Saving downsampled point cloud to: {pcd_file}")
    o3d.io.write_point_cloud(pcd_file, down_pcd)
    print("Done.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: python {sys.argv[0]} <input_pcd_file> <voxel_size>")
        sys.exit(1)

    input_pcd_file = sys.argv[1]
    voxel_size = sys.argv[2]
    downsample_and_replace(input_pcd_file, voxel_size)

