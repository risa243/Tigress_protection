#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_263 = SymVar_0
ref_278 = ref_263 # MOV operation
ref_6669 = ref_278 # MOV operation
ref_6881 = ref_6669 # MOV operation
ref_6887 = ((0x3F22161B + ref_6881) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_7030 = ref_6887 # MOV operation
ref_9496 = ref_7030 # MOV operation
ref_9599 = ref_9496 # MOV operation
ref_9601 = (((sx(0x40, ref_9599) * sx(0x40, 0x378AED0A)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_9726 = ref_9601 # MOV operation
ref_9728 = (((sx(0x40, ref_9726) * sx(0x40, 0xDF2B78B)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_9980 = ref_9728 # MOV operation
ref_9988 = (ref_9980 >> (0x1 & 0x3F)) # SHR operation
ref_9995 = ref_9988 # MOV operation
ref_10133 = ref_9995 # MOV operation
ref_10147 = (0xF & ref_10133) # AND operation
ref_10429 = ref_10147 # MOV operation
ref_10435 = (0x1 | ref_10429) # OR operation
ref_11623 = ref_278 # MOV operation
ref_11741 = ref_11623 # MOV operation
ref_11755 = ((ref_11741 << (0x7 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_12812 = ref_278 # MOV operation
ref_13042 = ref_12812 # MOV operation
ref_13050 = (ref_13042 >> (0x39 & 0x3F)) # SHR operation
ref_13057 = ref_13050 # MOV operation
ref_13203 = ref_11755 # MOV operation
ref_13207 = ref_13057 # MOV operation
ref_13209 = (ref_13207 | ref_13203) # OR operation
ref_13352 = ref_13209 # MOV operation
ref_13364 = ref_10435 # MOV operation
ref_13366 = ((ref_13352 << ((ref_13364 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_14554 = ref_278 # MOV operation
ref_14672 = ref_14554 # MOV operation
ref_14686 = ((ref_14672 << (0x7 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_15743 = ref_278 # MOV operation
ref_15973 = ref_15743 # MOV operation
ref_15981 = (ref_15973 >> (0x39 & 0x3F)) # SHR operation
ref_15988 = ref_15981 # MOV operation
ref_16134 = ref_14686 # MOV operation
ref_16138 = ref_15988 # MOV operation
ref_16140 = (ref_16138 | ref_16134) # OR operation
ref_17639 = ref_7030 # MOV operation
ref_17742 = ref_17639 # MOV operation
ref_17744 = (((sx(0x40, ref_17742) * sx(0x40, 0x378AED0A)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_17869 = ref_17744 # MOV operation
ref_17871 = (((sx(0x40, ref_17869) * sx(0x40, 0xDF2B78B)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_18123 = ref_17871 # MOV operation
ref_18131 = (ref_18123 >> (0x1 & 0x3F)) # SHR operation
ref_18138 = ref_18131 # MOV operation
ref_18276 = ref_18138 # MOV operation
ref_18290 = (0xF & ref_18276) # AND operation
ref_18572 = ref_18290 # MOV operation
ref_18578 = (0x1 | ref_18572) # OR operation
ref_18855 = ref_18578 # MOV operation
ref_18857 = ((0x40 - ref_18855) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_18865 = ref_18857 # MOV operation
ref_18984 = ref_16140 # MOV operation
ref_18988 = ref_18865 # MOV operation
ref_18990 = (ref_18988 & 0xFFFFFFFF) # MOV operation
ref_18992 = (ref_18984 >> ((ref_18990 & 0xFF) & 0x3F)) # SHR operation
ref_18999 = ref_18992 # MOV operation
ref_19145 = ref_13366 # MOV operation
ref_19149 = ref_18999 # MOV operation
ref_19151 = (ref_19149 | ref_19145) # OR operation
ref_19293 = ref_19151 # MOV operation
ref_21317 = ref_278 # MOV operation
ref_22398 = ref_19293 # MOV operation
ref_22610 = ref_22398 # MOV operation
ref_22616 = ((0xAD6EED + ref_22610) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_22723 = ref_21317 # MOV operation
ref_22727 = ref_22616 # MOV operation
ref_22729 = ((ref_22727 + ref_22723) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_22872 = ref_22729 # MOV operation
ref_24896 = ref_278 # MOV operation
ref_25977 = ref_7030 # MOV operation
ref_26103 = ref_24896 # MOV operation
ref_26107 = ref_25977 # MOV operation
ref_26109 = (ref_26107 | ref_26103) # OR operation
ref_27215 = ref_19293 # MOV operation
ref_27427 = ref_27215 # MOV operation
ref_27433 = ((0x2B6B05ED + ref_27427) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_28540 = ref_22872 # MOV operation
ref_28658 = ref_28540 # MOV operation
ref_28670 = ref_27433 # MOV operation
ref_28672 = (ref_28670 & ref_28658) # AND operation
ref_28778 = ref_26109 # MOV operation
ref_28782 = ref_28672 # MOV operation
ref_28784 = ((ref_28782 + ref_28778) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_28927 = ref_28784 # MOV operation
ref_31000 = ref_28927 # MOV operation
ref_32343 = ref_22872 # MOV operation
ref_32461 = ref_32343 # MOV operation
ref_32475 = (0x3F & ref_32461) # AND operation
ref_32618 = ref_32475 # MOV operation
ref_32632 = ((ref_32618 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_32783 = ref_31000 # MOV operation
ref_32787 = ref_32632 # MOV operation
ref_32789 = (ref_32787 | ref_32783) # OR operation
ref_32931 = ref_32789 # MOV operation
ref_35095 = ref_19293 # MOV operation
ref_35325 = ref_35095 # MOV operation
ref_35333 = (ref_35325 >> (0x4 & 0x3F)) # SHR operation
ref_35340 = ref_35333 # MOV operation
ref_35478 = ref_35340 # MOV operation
ref_35492 = (0xF & ref_35478) # AND operation
ref_35774 = ref_35492 # MOV operation
ref_35780 = (0x1 | ref_35774) # OR operation
ref_36886 = ref_7030 # MOV operation
ref_37004 = ref_36886 # MOV operation
ref_37016 = ref_35780 # MOV operation
ref_37018 = ((ref_37004 << ((ref_37016 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_38124 = ref_7030 # MOV operation
ref_39336 = ref_19293 # MOV operation
ref_39566 = ref_39336 # MOV operation
ref_39574 = (ref_39566 >> (0x4 & 0x3F)) # SHR operation
ref_39581 = ref_39574 # MOV operation
ref_39719 = ref_39581 # MOV operation
ref_39733 = (0xF & ref_39719) # AND operation
ref_40015 = ref_39733 # MOV operation
ref_40021 = (0x1 | ref_40015) # OR operation
ref_40298 = ref_40021 # MOV operation
ref_40300 = ((0x40 - ref_40298) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_40308 = ref_40300 # MOV operation
ref_40427 = ref_38124 # MOV operation
ref_40431 = ref_40308 # MOV operation
ref_40433 = (ref_40431 & 0xFFFFFFFF) # MOV operation
ref_40435 = (ref_40427 >> ((ref_40433 & 0xFF) & 0x3F)) # SHR operation
ref_40442 = ref_40435 # MOV operation
ref_40588 = ref_37018 # MOV operation
ref_40592 = ref_40442 # MOV operation
ref_40594 = (ref_40592 | ref_40588) # OR operation
ref_41700 = ref_22872 # MOV operation
ref_42781 = ref_32931 # MOV operation
ref_42862 = ref_41700 # MOV operation
ref_42866 = ref_42781 # MOV operation
ref_42868 = ((ref_42866 + ref_42862) & 0xFFFFFFFFFFFFFFFF) # ADD operation
ref_42993 = ref_40594 # MOV operation
ref_42997 = ref_42868 # MOV operation
ref_42999 = (((sx(0x40, ref_42997) * sx(0x40, ref_42993)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_43138 = ref_42999 # MOV operation
ref_43343 = ref_43138 # MOV operation
ref_43345 = ref_43343 # MOV operation

print ref_43345 & 0xffffffffffffffff