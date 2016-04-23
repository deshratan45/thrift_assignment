namespace py MultiServer

service MultiServer{

	string ServerA()
	string ServerB(1:string s) 

}