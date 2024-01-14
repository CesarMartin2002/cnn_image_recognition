% Set the path of the images and count them
clase = "peatones";
ruta = strcat('imagenes_jpg\',clase);
rel_path = strcat('.\', ruta); 
filesInfo = dir(fullfile(rel_path, '*.jpg')); 
n_images = length(filesInfo);

% Declare a cell in which the paths will be stored
paths = {}; 

% Declare a matrix in which ROIs will be stored
rois = []; 

% Declare a cell in which to store previws
final_images = {}; 

for i = 1:n_images
    % Read each image
    path = strcat('.\', ruta, '\', num2str(i), '.jpg'); 
    paths = vertcat(paths, path); 
    current_image = imread(path); 

    % Show a window in which the corners of the ROI can be chosen
    figure; 
    imshow(current_image); 
    title(strcat('Click on the first corner of ROI and then on the oppsite one. Image:  ',num2str(i),' out of ',num2str(n_images))); 
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
dataset = table(paths, rois, 'VariableNames', ["paths",clase]); 
save(strcat('.\', ruta, '\', strcat('dataset_',clase), '.mat'), 'dataset'); 