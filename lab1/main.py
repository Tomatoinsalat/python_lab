import sys     

def main() -> None:
    stations={}
    file_path = sys.argv[1]
    with open(file_path, 'rb') as file:
        for line in file:
            name, degrees = line.split(b';')
            degrees=float(degrees)
            if stations.get(name)==None:
                stations[name]=[degrees,degrees,degrees,1]
            else:
                data=stations[name]
                if degrees<data[0]:
                    data[0]=degrees
                elif degrees>data[2]:
                    data[2]=degrees
                data[1]+=degrees
                data[3]+=1
        stations=dict(sorted(stations.items()))
        for key in stations:
            data=stations[key]
            print (f"{key.decode('utf-8')};{data[0]};{round(data[1]/data[3],1):.1f};{data[2]}")

if __name__=="__main__":
    main()
