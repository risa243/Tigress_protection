set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} --VirtualizeDispatch=switch --VirtualizeSuperOpsRatio=0.0")

message("-- Virtualization super operators ratio: 0.0")
foreach(TIGRESS_SAMPLE ${TIGRESS_SAMPLES})
    list(GET ${TIGRESS_SAMPLE} 0 TNAME)
    list(GET ${TIGRESS_SAMPLE} 1 TFILE)
    add_executable(${TNAME}-virt-super-operators-ratio-0.0 ${TFILE})
endforeach(TIGRESS_SAMPLE)
