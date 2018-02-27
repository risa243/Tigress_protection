#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_263 = SymVar_0
ref_278 = ref_263 # MOV operation
ref_8493 = ref_278 # MOV operation
ref_9521 = ref_8493 # MOV operation
ref_9529 = ((ref_9521 - 0x35CEDE6D) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_9537 = ref_9529 # MOV operation
ref_13893 = ref_9537 # MOV operation
ref_17786 = ref_278 # MOV operation
ref_18831 = ref_17786 # MOV operation
ref_18841 = ((((0x0) << 64 | ref_18831) / 0x7) & 0xFFFFFFFFFFFFFFFF) # DIV operation
ref_22959 = ref_18841 # MOV operation
ref_27074 = ref_278 # MOV operation
ref_34696 = ref_22959 # MOV operation
ref_35726 = ref_34696 # MOV operation
ref_35736 = (ref_35726 >> (0x3 & 0x3F)) # SHR operation
ref_35743 = ref_35736 # MOV operation
ref_36235 = ref_35743 # MOV operation
ref_36251 = (0xF & ref_36235) # AND operation
ref_36783 = ref_36251 # MOV operation
ref_36799 = (0x1 | ref_36783) # OR operation
ref_37369 = ref_36799 # MOV operation
ref_37371 = ((0x40 - ref_37369) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_37379 = ref_37371 # MOV operation
ref_37784 = ref_37379 # MOV operation
ref_37786 = (ref_37784 & 0xFFFFFFFF) # MOV operation
ref_37788 = (0x7A11169 >> ((ref_37786 & 0xFF) & 0x3F)) # SHR operation
ref_37795 = ref_37788 # MOV operation
ref_43451 = ref_22959 # MOV operation
ref_44428 = ref_43451 # MOV operation
ref_44438 = (ref_44428 >> (0x3 & 0x3F)) # SHR operation
ref_44445 = ref_44438 # MOV operation
ref_44960 = ref_44445 # MOV operation
ref_44976 = (0xF & ref_44960) # AND operation
ref_45498 = ref_44976 # MOV operation
ref_45514 = (0x1 | ref_45498) # OR operation
ref_46008 = ref_45514 # MOV operation
ref_46010 = (ref_46008 & 0xFFFFFFFF) # MOV operation
ref_46012 = ((0x7A11169 << ((ref_46010 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_46019 = ref_46012 # MOV operation
ref_46512 = ref_46019 # MOV operation
ref_46526 = ref_37795 # MOV operation
ref_46528 = (ref_46526 | ref_46512) # OR operation
ref_47529 = ref_46528 # MOV operation
ref_47539 = (ref_47529 >> (0x4 & 0x3F)) # SHR operation
ref_47546 = ref_47539 # MOV operation
ref_48029 = ref_47546 # MOV operation
ref_48045 = (0xF & ref_48029) # AND operation
ref_48584 = ref_48045 # MOV operation
ref_48600 = (0x1 | ref_48584) # OR operation
ref_49170 = ref_48600 # MOV operation
ref_49172 = ((0x40 - ref_49170) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_49180 = ref_49172 # MOV operation
ref_49639 = ref_27074 # MOV operation
ref_49645 = ref_49180 # MOV operation
ref_49647 = (ref_49645 & 0xFFFFFFFF) # MOV operation
ref_49649 = (ref_49639 >> ((ref_49647 & 0xFF) & 0x3F)) # SHR operation
ref_49656 = ref_49649 # MOV operation
ref_53774 = ref_278 # MOV operation
ref_60882 = ref_22959 # MOV operation
ref_61909 = ref_60882 # MOV operation
ref_61919 = (ref_61909 >> (0x3 & 0x3F)) # SHR operation
ref_61926 = ref_61919 # MOV operation
ref_62453 = ref_61926 # MOV operation
ref_62469 = (0xF & ref_62453) # AND operation
ref_62981 = ref_62469 # MOV operation
ref_62997 = (0x1 | ref_62981) # OR operation
ref_63511 = ref_62997 # MOV operation
ref_63513 = ((0x40 - ref_63511) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_63521 = ref_63513 # MOV operation
ref_64071 = ref_63521 # MOV operation
ref_64073 = (ref_64071 & 0xFFFFFFFF) # MOV operation
ref_64075 = (0x7A11169 >> ((ref_64073 & 0xFF) & 0x3F)) # SHR operation
ref_64082 = ref_64075 # MOV operation
ref_69688 = ref_22959 # MOV operation
ref_70727 = ref_69688 # MOV operation
ref_70737 = (ref_70727 >> (0x3 & 0x3F)) # SHR operation
ref_70744 = ref_70737 # MOV operation
ref_71167 = ref_70744 # MOV operation
ref_71183 = (0xF & ref_71167) # AND operation
ref_71723 = ref_71183 # MOV operation
ref_71739 = (0x1 | ref_71723) # OR operation
ref_72243 = ref_71739 # MOV operation
ref_72245 = (ref_72243 & 0xFFFFFFFF) # MOV operation
ref_72247 = ((0x7A11169 << ((ref_72245 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_72254 = ref_72247 # MOV operation
ref_72714 = ref_72254 # MOV operation
ref_72728 = ref_64082 # MOV operation
ref_72730 = (ref_72728 | ref_72714) # OR operation
ref_73731 = ref_72730 # MOV operation
ref_73741 = (ref_73731 >> (0x4 & 0x3F)) # SHR operation
ref_73748 = ref_73741 # MOV operation
ref_74275 = ref_73748 # MOV operation
ref_74291 = (0xF & ref_74275) # AND operation
ref_74803 = ref_74291 # MOV operation
ref_74819 = (0x1 | ref_74803) # OR operation
ref_75327 = ref_53774 # MOV operation
ref_75333 = ref_74819 # MOV operation
ref_75335 = (ref_75333 & 0xFFFFFFFF) # MOV operation
ref_75337 = ((ref_75327 << ((ref_75335 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_75344 = ref_75337 # MOV operation
ref_75883 = ref_75344 # MOV operation
ref_75897 = ref_49656 # MOV operation
ref_75899 = (ref_75897 | ref_75883) # OR operation
ref_80084 = ref_75899 # MOV operation
ref_84533 = ref_278 # MOV operation
ref_85583 = ref_84533 # MOV operation
ref_85591 = ((ref_85583 - 0x297EE8A1) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_85599 = ref_85591 # MOV operation
ref_86060 = ref_85599 # MOV operation
ref_86076 = (((sx(0x40, 0x1471C5DA) * sx(0x40, ref_86060)) & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) & 0xFFFFFFFFFFFFFFFF) # IMUL operation
ref_90261 = ref_86076 # MOV operation
ref_90263 = ((ref_90261 >> 56) & 0xFF) # Byte reference - MOV operation
ref_90264 = ((ref_90261 >> 48) & 0xFF) # Byte reference - MOV operation
ref_90265 = ((ref_90261 >> 40) & 0xFF) # Byte reference - MOV operation
ref_90266 = ((ref_90261 >> 32) & 0xFF) # Byte reference - MOV operation
ref_90267 = ((ref_90261 >> 24) & 0xFF) # Byte reference - MOV operation
ref_90268 = ((ref_90261 >> 16) & 0xFF) # Byte reference - MOV operation
ref_90269 = ((ref_90261 >> 8) & 0xFF) # Byte reference - MOV operation
ref_90270 = (ref_90261 & 0xFF) # Byte reference - MOV operation
ref_97397 = ((ref_90265) << 8 | ref_90266) # MOVZX operation
ref_98369 = (ref_97397 & 0xFFFF) # MOVZX operation
ref_105565 = ((ref_90267) << 8 | ref_90268) # MOVZX operation
ref_112631 = (ref_105565 & 0xFFFF) # MOVZX operation
ref_113579 = (ref_98369 & 0xFFFF) # MOVZX operation
ref_120928 = (ref_113579 & 0xFFFF) # MOVZX operation
ref_120930 = (((ref_120928 & 0xFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_120931 = ((ref_120928 & 0xFFFF) & 0xFF) # Byte reference - MOV operation
ref_158688 = ref_80084 # MOV operation
ref_159145 = ref_158688 # MOV operation
ref_159161 = (0x1F & ref_159145) # AND operation
ref_160191 = ref_159161 # MOV operation
ref_160201 = ((ref_160191 << (0x4 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_160208 = ref_160201 # MOV operation
ref_164198 = ref_22959 # MOV operation
ref_164698 = ref_164198 # MOV operation
ref_164712 = ref_160208 # MOV operation
ref_164714 = (ref_164712 | ref_164698) # OR operation
ref_168861 = ref_164714 # MOV operation
ref_173610 = ref_168861 # MOV operation
ref_174126 = ref_173610 # MOV operation
ref_174142 = (0xF & ref_174126) # AND operation
ref_175114 = ref_174142 # MOV operation
ref_175124 = ((ref_175114 << (0x2 & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_175131 = ref_175124 # MOV operation
ref_179169 = ref_168861 # MOV operation
ref_179644 = ref_179169 # MOV operation
ref_179658 = ref_175131 # MOV operation
ref_179660 = (ref_179658 | ref_179644) # OR operation
ref_183911 = ref_179660 # MOV operation
ref_191412 = ((ref_90263) << 8 | ref_90264) # MOVZX operation
ref_192406 = (ref_191412 & 0xFFFF) # MOVZX operation
ref_199654 = ((ref_90269) << 8 | ref_90270) # MOVZX operation
ref_206621 = (ref_199654 & 0xFFFF) # MOVZX operation
ref_206623 = (((ref_206621 & 0xFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_206624 = ((ref_206621 & 0xFFFF) & 0xFF) # Byte reference - MOV operation
ref_207676 = (ref_192406 & 0xFFFF) # MOVZX operation
ref_214874 = (ref_207676 & 0xFFFF) # MOVZX operation
ref_221952 = (ref_214874 & 0xFFFF) # MOVZX operation
ref_222990 = (ref_221952 & 0xFFFF) # MOVZX operation
ref_230149 = (ref_112631 & 0xFFFF) # MOVZX operation
ref_237261 = (ref_230149 & 0xFFFF) # MOVZX operation
ref_237263 = (((ref_237261 & 0xFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_237264 = ((ref_237261 & 0xFFFF) & 0xFF) # Byte reference - MOV operation
ref_238359 = (ref_222990 & 0xFFFF) # MOVZX operation
ref_245204 = (ref_238359 & 0xFFFF) # MOVZX operation
ref_245206 = (((ref_245204 & 0xFFFF) >> 8) & 0xFF) # Byte reference - MOV operation
ref_245207 = ((ref_245204 & 0xFFFF) & 0xFF) # Byte reference - MOV operation
ref_249336 = ref_13893 # MOV operation
ref_254967 = ref_183911 # MOV operation
ref_255412 = ref_254967 # MOV operation
ref_255428 = (0xF & ref_255412) # AND operation
ref_255928 = ref_255428 # MOV operation
ref_255944 = (0x1 | ref_255928) # OR operation
ref_256490 = ref_255944 # MOV operation
ref_256492 = ((0x40 - ref_256490) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_256500 = ref_256492 # MOV operation
ref_256938 = ref_249336 # MOV operation
ref_256944 = ref_256500 # MOV operation
ref_256946 = (ref_256944 & 0xFFFFFFFF) # MOV operation
ref_256948 = (ref_256938 >> ((ref_256946 & 0xFF) & 0x3F)) # SHR operation
ref_256955 = ref_256948 # MOV operation
ref_261073 = ref_13893 # MOV operation
ref_266353 = ref_183911 # MOV operation
ref_266886 = ref_266353 # MOV operation
ref_266902 = (0xF & ref_266886) # AND operation
ref_267298 = ref_266902 # MOV operation
ref_267314 = (0x1 | ref_267298) # OR operation
ref_267830 = ref_261073 # MOV operation
ref_267836 = ref_267314 # MOV operation
ref_267838 = (ref_267836 & 0xFFFFFFFF) # MOV operation
ref_267840 = ((ref_267830 << ((ref_267838 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_267847 = ref_267840 # MOV operation
ref_268331 = ref_267847 # MOV operation
ref_268345 = ref_256955 # MOV operation
ref_268347 = (ref_268345 | ref_268331) # OR operation
ref_273922 = ref_80084 # MOV operation
ref_279692 = ((((((((ref_206623) << 8 | ref_206624) << 8 | ref_245206) << 8 | ref_245207) << 8 | ref_120930) << 8 | ref_120931) << 8 | ref_237263) << 8 | ref_237264) # MOV operation
ref_280657 = ref_279692 # MOV operation
ref_280667 = (ref_280657 >> (0x2 & 0x3F)) # SHR operation
ref_280674 = ref_280667 # MOV operation
ref_281201 = ref_280674 # MOV operation
ref_281217 = (0xF & ref_281201) # AND operation
ref_281665 = ref_281217 # MOV operation
ref_281681 = (0x1 | ref_281665) # OR operation
ref_282158 = ref_281681 # MOV operation
ref_282160 = ((0x40 - ref_282158) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_282168 = ref_282160 # MOV operation
ref_282671 = ref_273922 # MOV operation
ref_282677 = ref_282168 # MOV operation
ref_282679 = (ref_282677 & 0xFFFFFFFF) # MOV operation
ref_282681 = (ref_282671 >> ((ref_282679 & 0xFF) & 0x3F)) # SHR operation
ref_282688 = ref_282681 # MOV operation
ref_286776 = ref_80084 # MOV operation
ref_292048 = ((((((((ref_206623) << 8 | ref_206624) << 8 | ref_245206) << 8 | ref_245207) << 8 | ref_120930) << 8 | ref_120931) << 8 | ref_237263) << 8 | ref_237264) # MOV operation
ref_293070 = ref_292048 # MOV operation
ref_293080 = (ref_293070 >> (0x2 & 0x3F)) # SHR operation
ref_293087 = ref_293080 # MOV operation
ref_293614 = ref_293087 # MOV operation
ref_293630 = (0xF & ref_293614) # AND operation
ref_294067 = ref_293630 # MOV operation
ref_294083 = (0x1 | ref_294067) # OR operation
ref_294599 = ref_286776 # MOV operation
ref_294605 = ref_294083 # MOV operation
ref_294607 = (ref_294605 & 0xFFFFFFFF) # MOV operation
ref_294609 = ((ref_294599 << ((ref_294607 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_294616 = ref_294609 # MOV operation
ref_295115 = ref_294616 # MOV operation
ref_295129 = ref_282688 # MOV operation
ref_295131 = (ref_295129 | ref_295115) # OR operation
ref_296085 = ref_295131 # MOV operation
ref_296095 = (ref_296085 >> (0x4 & 0x3F)) # SHR operation
ref_296102 = ref_296095 # MOV operation
ref_296639 = ref_296102 # MOV operation
ref_296655 = (0xF & ref_296639) # AND operation
ref_297091 = ref_296655 # MOV operation
ref_297107 = (0x1 | ref_297091) # OR operation
ref_297645 = ref_297107 # MOV operation
ref_297647 = ((0x40 - ref_297645) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_297655 = ref_297647 # MOV operation
ref_298180 = ref_268347 # MOV operation
ref_298186 = ref_297655 # MOV operation
ref_298188 = (ref_298186 & 0xFFFFFFFF) # MOV operation
ref_298190 = ((ref_298180 << ((ref_298188 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_298197 = ref_298190 # MOV operation
ref_302322 = ref_13893 # MOV operation
ref_308017 = ref_183911 # MOV operation
ref_308474 = ref_308017 # MOV operation
ref_308490 = (0xF & ref_308474) # AND operation
ref_308946 = ref_308490 # MOV operation
ref_308962 = (0x1 | ref_308946) # OR operation
ref_309483 = ref_308962 # MOV operation
ref_309485 = ((0x40 - ref_309483) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_309493 = ref_309485 # MOV operation
ref_310052 = ref_302322 # MOV operation
ref_310058 = ref_309493 # MOV operation
ref_310060 = (ref_310058 & 0xFFFFFFFF) # MOV operation
ref_310062 = (ref_310052 >> ((ref_310060 & 0xFF) & 0x3F)) # SHR operation
ref_310069 = ref_310062 # MOV operation
ref_314066 = ref_13893 # MOV operation
ref_319395 = ref_183911 # MOV operation
ref_319840 = ref_319395 # MOV operation
ref_319856 = (0xF & ref_319840) # AND operation
ref_320388 = ref_319856 # MOV operation
ref_320404 = (0x1 | ref_320388) # OR operation
ref_320849 = ref_314066 # MOV operation
ref_320855 = ref_320404 # MOV operation
ref_320857 = (ref_320855 & 0xFFFFFFFF) # MOV operation
ref_320859 = ((ref_320849 << ((ref_320857 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_320866 = ref_320859 # MOV operation
ref_321369 = ref_320866 # MOV operation
ref_321383 = ref_310069 # MOV operation
ref_321385 = (ref_321383 | ref_321369) # OR operation
ref_326407 = ref_80084 # MOV operation
ref_332165 = ((((((((ref_206623) << 8 | ref_206624) << 8 | ref_245206) << 8 | ref_245207) << 8 | ref_120930) << 8 | ref_120931) << 8 | ref_237263) << 8 | ref_237264) # MOV operation
ref_333202 = ref_332165 # MOV operation
ref_333212 = (ref_333202 >> (0x2 & 0x3F)) # SHR operation
ref_333219 = ref_333212 # MOV operation
ref_333770 = ref_333219 # MOV operation
ref_333786 = (0xF & ref_333770) # AND operation
ref_334182 = ref_333786 # MOV operation
ref_334198 = (0x1 | ref_334182) # OR operation
ref_334727 = ref_334198 # MOV operation
ref_334729 = ((0x40 - ref_334727) & 0xFFFFFFFFFFFFFFFF) # SUB operation
ref_334737 = ref_334729 # MOV operation
ref_335220 = ref_326407 # MOV operation
ref_335226 = ref_334737 # MOV operation
ref_335228 = (ref_335226 & 0xFFFFFFFF) # MOV operation
ref_335230 = (ref_335220 >> ((ref_335228 & 0xFF) & 0x3F)) # SHR operation
ref_335237 = ref_335230 # MOV operation
ref_339313 = ref_80084 # MOV operation
ref_344487 = ((((((((ref_206623) << 8 | ref_206624) << 8 | ref_245206) << 8 | ref_245207) << 8 | ref_120930) << 8 | ref_120931) << 8 | ref_237263) << 8 | ref_237264) # MOV operation
ref_345543 = ref_344487 # MOV operation
ref_345553 = (ref_345543 >> (0x2 & 0x3F)) # SHR operation
ref_345560 = ref_345553 # MOV operation
ref_346087 = ref_345560 # MOV operation
ref_346103 = (0xF & ref_346087) # AND operation
ref_346612 = ref_346103 # MOV operation
ref_346628 = (0x1 | ref_346612) # OR operation
ref_347168 = ref_339313 # MOV operation
ref_347174 = ref_346628 # MOV operation
ref_347176 = (ref_347174 & 0xFFFFFFFF) # MOV operation
ref_347178 = ((ref_347168 << ((ref_347176 & 0xFF) & 0x3F)) & 0xFFFFFFFFFFFFFFFF) # SHL operation
ref_347185 = ref_347178 # MOV operation
ref_347632 = ref_347185 # MOV operation
ref_347646 = ref_335237 # MOV operation
ref_347648 = (ref_347646 | ref_347632) # OR operation
ref_348634 = ref_347648 # MOV operation
ref_348644 = (ref_348634 >> (0x4 & 0x3F)) # SHR operation
ref_348651 = ref_348644 # MOV operation
ref_349112 = ref_348651 # MOV operation
ref_349128 = (0xF & ref_349112) # AND operation
ref_349636 = ref_349128 # MOV operation
ref_349652 = (0x1 | ref_349636) # OR operation
ref_350200 = ref_321385 # MOV operation
ref_350206 = ref_349652 # MOV operation
ref_350208 = (ref_350206 & 0xFFFFFFFF) # MOV operation
ref_350210 = (ref_350200 >> ((ref_350208 & 0xFF) & 0x3F)) # SHR operation
ref_350217 = ref_350210 # MOV operation
ref_350640 = ref_350217 # MOV operation
ref_350654 = ref_298197 # MOV operation
ref_350656 = (ref_350654 | ref_350640) # OR operation
ref_354748 = ref_350656 # MOV operation
ref_355758 = ref_354748 # MOV operation
ref_355760 = ref_355758 # MOV operation

print ref_355760 & 0xffffffffffffffff