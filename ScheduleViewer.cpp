#include<windows.h>
#include<iostream>
int main(){
    std::cout << "Starting up the GTBTools" <<std::endl;
    bool returnValue=system("start pythonw.exe Scripts/main.py");
    if(returnValue){
        std::cerr << "Something went wrong,failed to start up.\n";
        return 1;
    }
    std::cout << "Shedule viewer started up";
}