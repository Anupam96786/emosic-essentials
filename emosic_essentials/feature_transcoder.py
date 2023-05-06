class FeatureTranscoder:
    def __init__(self, features) -> None:
        self.__features = sorted(features)

    def encode(self, feature):
        if feature in self.__features:
            return [int(i == feature) for i in self.__features]
        else:
            raise "Unknown feature detected"
    
    def decode(self, encoded_array):
        if 1 in encoded_array:
            return self.__features[encoded_array.index(1)]
        else:
            raise "Unable to detect feature"
