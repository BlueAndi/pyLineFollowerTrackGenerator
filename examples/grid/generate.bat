@echo off

cd ../../
pyLineFollowerTrackGenerator grid -a "Andreas Merkle" -d "Line follower grid track." -e web@blue-andi.de -mg cardboard -mr rubber -mp dry -s 3 examples/grid/grid.wbt examples/grid/grid_points.json
cd examples/grid
