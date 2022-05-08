class MainPageManager:
    def ChechPosition(self, Data):
        Index = Data.PositionIndex 
        match(Index):
            case -1:
                print("Error")
                return
            case 0:
                print("Ksiegowy")
                return

            case 1:
                print("Magazynier")
                return