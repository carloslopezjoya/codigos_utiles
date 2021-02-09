

for i=1:15
    
    a=['Foto_1125_001_' num2str(i) '.mat']
    load(a,'color_raw');
    c=squeeze(color_raw(1,:,:,:));
    hg=['Foto_1125_001_' num2str(i) '.jpg']
    imwrite(c,hg,'jpg')
    
   
end