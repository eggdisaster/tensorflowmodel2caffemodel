cmake_minimum_required (VERSION 2.8)

project (write_model)

add_executable(write_model write_model.cpp)

include_directories ( /home/dell/C3D/C3D-v1.0/include
    /usr/local/include
    /usr/local/cuda/include
    /usr/include
    /usr/include/hdf5/serial/
    )

target_link_libraries(write_model
    /home/dell/C3D/C3D-v1.0/build/lib/libcaffe.so
    /usr/lib/x86_64-linux-gnu/libglog.so
    /usr/lib/x86_64-linux-gnu/libboost_system.so
    )

