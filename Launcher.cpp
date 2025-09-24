#include<windows.h>
#include<iostream>
#include<thread>
void upDate(){
    //I don't know how to do it,fuuuuuuuuuuuuuuuuuuuu*k.
}
int main(){
    std::thread UPDATE(upDate);
    std::cout << "Starting up the GTBTools" <<std::endl;
    bool returnValue=system("start pythonw.exe Scripts/main.py");
    if(returnValue){
        std::cerr << "Something went wrong,failed to start up.\n";
        return 1;
    }
    std::cout << "GTBTools started up";
    UPDATE.join();
}