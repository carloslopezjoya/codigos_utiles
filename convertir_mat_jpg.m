

for i=73:101
    
    a=['Foto_1117_001_' num2str(i) '.mat']
    load(a,'color_raw');
    c=squeeze(color_raw(1,:,:,:));
    hg=['Foto_1117_001_' num2str(i) '.jpg']
    imwrite(c,hg,'jpg')
    
   
end