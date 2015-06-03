__author__ = 'RunzeZhao'
import pycrunchbase

cb = pycrunchbase.CrunchBase('your_crunchbase_api_access_code_here')

print cb.person('ben-horowitz')