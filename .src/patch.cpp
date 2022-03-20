/*
    This is a patching script made for automatically installing the dot files to your system.
    You can either run the executable "patch" without giving arguments, to replace/move all files to your
    ~/.config folder or specify a specific part like './patch qtile' which will only patch the qtile
    configurations. See all available options inside the '.include' file.
*/

#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <filesystem>
#include <vector>
#include <fstream>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <boost/algorithm/string.hpp>

using namespace std;
namespace fs = filesystem;

vector<string> get_includes();

int main(int argc, char *argv[]) {
    vector<string> entries;
    string user_home = getenv("HOME");
    string nitrogen_cmd = "curl https://i.imgur.com/22G2GPV.jpg -o " + user_home + "/.wall.jpg && nitrogen --set-zoom-fill " + user_home + "/.wall.jpg";
    system(nitrogen_cmd.c_str());

    user_home.append("/.config/");

    //Parse arguments, if set, match to .include
    if (argc > 1) {
        vector<string> includes = get_includes();
        for (int i = 1; i < argc; ++i){

            if (find(includes.begin(), includes.end(), argv[i]) != includes.end()) 
                entries.push_back(argv[i]);

            else cerr << "[ERR] Invalid argument, '" 
                        << argv[i] 
                        << "' not found in .includes" 
                        << endl;

        }
    } 
    //If no args, parse .include
    else entries = get_includes();

    cout << "Checking '" << user_home << "'..." << endl;
    //Prepare user .config directory. Specifically, renaming specified configurations to 'filename.old',
    //appending '.old' as an extension to the file and not deleting it like a scumbag.
    bool directory_match = false;
    for (const auto & dir : fs::directory_iterator(user_home)) {
        for (const auto & entry : entries) {
            if (dir.is_directory() && boost::iequals(dir.path().filename().string(), entry)){
                directory_match = true;
                for (const auto & file : fs::directory_iterator(dir.path())) {
                    fs::path f = file.path();
                    if (std::rename(f.string().c_str(), f.string().append(".old").c_str()) < 0) {
                        perror("Error moving file");
                        return 0;
                    } else {
                        cout << "Successfully renamed file '" 
                                << f.filename().string()
                                << "' to '" 
                                << f.filename().string() 
                                << ".old'" 
                                << endl;
                    }
                }
            }
        }
    }

    if (directory_match) {
        cout << "Preserved files in '" << user_home << "' for later use" << endl;
    }

    //Loop through all entries and respective directories and move them
    for (const auto & entry : entries) {
        cout << "Applying " << entry << " configurations..." << endl;
        for (const auto & file : fs::directory_iterator("./"+entry)){
            try { //Copy the file to respective location.
                string fake_dir = user_home + entry;
                string fake_file = fake_dir + "/" + file.path().filename().string();
                fs::create_directories(fake_dir); // Recursively create target directory if not existing.
                fs::copy_file(file, fake_file, fs::copy_options::overwrite_existing);
            }
            catch (std::exception& e) { // Not using fs::filesystem_error since std::bad_alloc can throw too.  
                std::cout << e.what();
            }
        }
    }

    cout << endl 
            << "## DONE, Enjoy my dot files :)" 
            << endl 
            << "PS: You might need to restart X11 for changes to take effect." 
            << endl
            << "Please do star my repository: https://github.com/dehys/.files"
            << endl 
            << endl;

}

//Parsing of the .include file
vector<string> get_includes() {

    ifstream file ("./.include");
    string tmp_cont;
    std::vector<string> tokens;

    if (file.is_open()) {
        while ( file >> tmp_cont ) {
            tokens.push_back( tmp_cont );
        }
    }
    return tokens;
}