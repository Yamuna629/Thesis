% Define the dimensions of the structure
width = 100; % Width of structure in voxels
height = 100; % Height of structure in voxels
depth = 100; % Depth of structure in voxels

% Define the number of Monte Carlo samples
numSamples = 100000; % Increase this number for more accurate results

% Generate a random 3D structure with specified porosity
porosity = 0.5; % Porosity of structure
structure = rand(height, width, depth) > porosity; % Generate binary matrix

% Initialize variables for counting hits and misses
numHits = 0;
numMisses = 0;

% Loop through each Monte Carlo sample
for i = 1:numSamples
    % Generate a random point within the structure boundaries
    x = randi([1, width]);
    y = randi([1, height]);
    z = randi([1, depth]);
    
    % Check if the point falls within a pore (miss) or solid (hit)
    if structure(y, x, z) == 0 % Miss
        numMisses = numMisses + 1;
    else % Hit
        numHits = numHits + 1;
    end
end

% Calculate the porosity estimate
porosityEstimate = numMisses / (numHits + numMisses);

% Display the results
disp(['Actual porosity: ', num2str(porosity)]);
disp(['Estimated porosity: ', num2str(porosityEstimate)]);
