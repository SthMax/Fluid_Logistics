# Readme
Fluid Logitics Project Codes\

## Project Structure
### Generators

1. **Map Generator**:\
    Generating X \* Y MAP with randomly numbered X \* Y \* P ( P < 1 ) Blocks scattered into MAP

    Input:\
    &emsp; Dimension: X,Y as INT\
    &emsp; &emsp; &emsp; &emsp; X & Y is the size of horizontal and vertical size of tileMap, the total size of map will be (X+2), (Y+2)                
    &emsp; Block Density: P as FLOAT

    *Tentative Input:*\
    &emsp; Scatter Function (Not Implemented)

    Output:\
    &emsp; X*Y Array with numbered blocks from 1 to X*Y*P, 0 is empty block

2. **Channel Generator**\
    Generating N Channels around a X*Y Array, can be specified locations.

    Input:\
    &emsp; MAP: X \* Y Array\
    &emsp; Channel Numbers: N as INT, N < 2 \* (X+Y)\
    &emsp; Specified Locations: \
    &emsp; &emsp;   {"N/A","TLT","TTT","TRT","N/A"};\
    &emsp; &emsp;   {"TLL","N/A","N/A","N/A","TRR"};\
    &emsp; &emsp;   {"MLL","N/A","N/A","N/A","MRR"};\
    &emsp; &emsp;   {"DLL","N/A","N/A","N/A","DRR"};\
    &emsp; &emsp;   {"N/A","DLD","DDD","DRD","N/A"};\
    &emsp; &emsp;   as string array

    *Tentative Input:*\
    &emsp; Outbound Channel / Inbound Channel

    Output:\
    &emsp; (X+2) \* (Y+2) Array with numbered blocks from 1 to X \* Y \* P:
    &emsp; 0 is empty block, -1 is Inbound Channel, -2 is Outbound Channel, -3 is Wall



### Algorithms

1. **Runner**\
    Generating a Channeled MAP and then Running Mapping Algorithm in a single thread

    Input:\
    &emsp; X,Y,P,N and Specified Locations\
    &emsp; Algorithm: Specified Algorithm\
    &emsp; Target MAP: (X) \* (Y) Array

    Output:\
    &emsp; Total Steps and Running Time if runnable, -1 if not runnable

2. **Algorithms**\
    Will be plugged into runner to run, maintaining in a single file

### Management

1. **Manager**\
    Generating Muliple Runners in multiple threads and collecting datas, then Plot the data.

    Input:\
    &emsp; X,Y,P,N and Specified Locations\
    &emsp; Algorithm: Specified Algorithm\
    &emsp; Target MAP: (X) \* (Y) Array




        
    
