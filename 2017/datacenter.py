# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 17:57:35 2017

@author: Thomas
"""

import video
import endPoint
import cache

class datacenter:
    
    def __init__(self,path):
        f = open(path)
        self.V, self.E, self.R, self.C, self.X = f.readline().split(' ')
        self.V, self.E, self.R, self.C, self.X = int(self.V), int(self.E), int(self.R), int(self.C), int(self.X)
        vi = f.readline().split(' ')
        self.caches = []
        for i in range(self.C):
            self.caches.append(cache.cache(self.X))
        self.videos = []
        self.endPoints = []
        for i in range(len(vi)):
            self.vids.append(video.video(int(vi[i]), i, 0))
        for i in range(self.E):
            Ld,K = f.readline().split(' ')
            Ld,K = int(Ld),int(K)
            e = endPoint.endPoint(Ld)
            for j in range(K):
                c,Lc = f.readline().split(' ')
                e.addCacheLat(self.caches[int(c)],int(Lc))