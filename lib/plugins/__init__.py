from base import *
from folder import *
from fspot import *
from flickr import *
#from picasa import *

token_base = (
    ['Folder', MakeDirPhoto,    PhotoTargetDir    ],
    ['F-Spot', MakeFSpotPhoto,  PhotoTargetFspot  ],
    ['Flickr', MakeFlickrPhoto, PhotoTargetFlickr ],
#    ['Picasa', MakePicasaPhoto, PhotoTargetPicasa ],
    )

source_list=[]
make_photo_token ={}
photo_target_token={}

for k in token_base:
    source_list.append(k[0])
    make_photo_token[k[0]] = k[1]
    photo_target_token[k[0]] = k[2]
