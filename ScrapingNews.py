import Express as Tribune
import BBC
import download_image as d_img
import Jazeera
import GetName as Previous
import Dawn
import Dataset
import ARY
Data_List = []
i = 1
while i != 0:
    #Tribune.ScrapExpressTribune()
    #BBC.BBCNews()
    Jazeera.AlJazeeraNews()

    #Dawn.DawnNews()
    #ARY.AryNews()
    d_img.image_download(Previous.Previous_Urls)
    i = 0
Data__set = Dataset.Get_data_list()
print(Data__set)