# Conway-k-regular
## What is this? 
An implementation of Conway's Game of Life on a k-uniform tiling of convex polygons! This is one of the very first programming projects I ever worked on (outside of CS 5, Harvey Mudd's introductory computer science course), and as such, it's not exactly beautiful. Also, at the time, the only "graphics" library I'd ever had any exposure to was Python Turtle, which is why the simulation runs so slowly. 

## How does it work?
The primary difficulty was trying to figure out how we could store the data for the program, and access adjacent cells easily. Me and my friend Owen realized that we could achieve this by first finding a "unit cell" with which to tile the board, and then store each of these unit cells in a standard list-of-lists. Our current implementation is hard-coded for one specific tiling, but when we get more free time, we'd like to look into generating unit cells and adjacency rules automatically. 

## Where can I see it working? 
My YouTube channel! Here's a [link](https://youtu.be/011JXpdWA-8?t=7m42s)
