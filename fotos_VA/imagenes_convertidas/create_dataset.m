ruta = "peatones";

rel_path = strcat(".\",ruta)
% Declare how many images the dataset will have

% Use the dir function to get information about files in the folder
filesInfo = dir(fullfile(rel_path, '*.png')); % Change the file extension accordingly

% Count the number of files
n_images = length(filesInfo);

% n_images = 4;

% Declare a cell in which the paths will be stored
paths = {}; 

% Declare a matrix in which ROIs will be stored
rois = []; 

% Declare a cell in which to store previws
final_images = {}; 

for i = 1:n_images
    % Read each image
    path = strcat(".\",ruta,"\",num2str(i), '.png'); 
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
    roi = {[x(1) y(1) width height]};
    rois = [rois; roi]; 

    % Add preview
    final_images = vertcat(final_images, insertObjectAnnotation(current_image, 'rectangle', roi{1}, 'ROI')); 

end

% Preview the dataset
figure; 
title('Preview of the dataset'); 
montage(final_images); 

% Save the dataset
dataset = table(paths, rois); 
save(strcat(".\",ruta,"\",'dataset_',ruta,'.mat'), 'dataset'); 