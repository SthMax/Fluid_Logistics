# Readme
Fluid Logitics Project Codes

## Project Structure
### Generators

1. Map Generator 
    Generating X*Y MAP with randomly numbered X*Y*P (P<1>) Blocks scattered into MAP
    Input:
        Dimension: X,Y as INT   
        Block Density: P as FLOAT
    *Tentative Input:*
        Scatter Function (Not Implemented)
    Output:
        X*Y Array with numbered blocks from 1 to X*Y*P, 0 is empty block

2. Channel Generator
    Generating N Channels around a X*Y Array, can be specified locations.
    Input:
        MAP: X*Y Array
        Channel Numbers: N as INT, N < 2*(X+Y)
        Specified Locations: {"N/A","TLT","TTT","TRT","N/A"};
                             {"TLL","N/A","N/A","N/A","TRR"};
                             {"MLL","N/A","N/A","N/A","MRR"};
                             {"DLL","N/A","N/A","N/A","DRR"};
                             {"N/A","DLD","DDD","DRD","N/A"};
                             as string array
    *Tentative Input:*
        Outbound Channel / Inbound Channel
    Output:
        (X+2)*(Y+2) Array with numbered blocks from 1 to X*Y*P, 0 is empty block, -1 is Inbound Channel, -2 is Outbound Channel, -3 is Wall

### Algorithms

1. Runner
    Generating a Channeled MAP and then Running Mapping Algorithm in a single thread
    Input:
        X,Y,P,N and Specified Locations
        Algorithm: Specified Algorithm
        Target MAP: (X+2)*(Y+2) Array
    Output:
        Total Steps and Running Time if runnable, -1 if not runnable

2. Algorithms
    Will be plugged into runner to run,
    Maintaining in a single file

### Management

1. Manager
    Generating Muliple Runners in multiple threads and collecting datas
    Then Plot the data.
    Input:
        X,Y,P,N and Specified Locations
        Algorithm: Specified Algorithm
        Target MAP: (X+2)*(Y+2) Array




        
    
