import utilities
from facebook import minifb

_FbApiKey = "3d391aa9632c0f79d83a6b97adbae34f"
_FbSecret = minifb.FacebookSecret("197f1a47faaf41323784c7c8500c09ce")

class Facebook(utilities.Parser):

    def __init__(self, uid):
        self.uid = uid
        
    def parse(self):
        response = minifb.call("facebook.profile.getFBML", _FbApiKey, _FbSecret, format='XML', uid=self.uid) 
        print response
        