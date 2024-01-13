% Declare how many images the dataset will have
n_images = 4;

% Declare a cell in which the paths will be stored
paths = {}; 

% Declare a matrix in which ROIs will be stored
rois = []; 

% Declare a cell in which to store previws
final_images = {}; 

for i = 1:n_images
    % Read each image
    path = strcat(num2str(i), '.jpg'); 
    paths = vertcat(paths, path); 
    current_image = imread(path); 

    % Show a window in which the corners of the ROI can be chosen
    figure; 
    imshow(current_image); 
    title('Click on the first corner of ROI and then on the oppsite one'); 
    [x, y] = ginput(2); 
    close;

    % Calculate the ROI
    width = abs(x(2) - x(1)); 
    height = abs(y(2) - y(1)); 
    roi = [x(1) y(1) width height];
    rois = [rois; roi]; 

    % Add preview
    final_images = vertcat(final_images, insertObjectAnnotation(current_image, 'rectangle', roi, 'ROI')); 

end

% Preview the dataset
figure; 
title('Preview of the dataset'); 
montage(final_images); 

% Save the dataset
dataset = table(paths, rois); 
save('dataset.mat', 'dataset'); 