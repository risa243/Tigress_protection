; ModuleID = ""
target triple = "x86_64-pc-linux-gnu"
target datalayout = ""

define i64 @"SECRET"(i64 %"SymVar_0") nounwind
{
.3:
  %".4" = sub i64 %"SymVar_0", 902749805
  %".5" = zext i64 %"SymVar_0" to i128
  %".6" = zext i64 0 to i128
  %".7" = shl i128 %".6", 64
  %".8" = or i128 %".5", %".7"
  %".9" = zext i64 7 to i128
  %".10" = udiv i128 %".8", %".9"
  %".11" = trunc i128 %".10" to i64
  %".12" = zext i8 3 to i64
  %".13" = and i64 %".12", 63
  %".14" = lshr i64 %".11", %".13"
  %".15" = and i64 15, %".14"
  %".16" = or i64 1, %".15"
  %".17" = sub i64 64, %".16"
  %".18" = trunc i64 %".17" to i8
  %".19" = zext i8 %".18" to i64
  %".20" = and i64 %".19", 63
  %".21" = lshr i64 127996265, %".20"
  %".22" = zext i8 3 to i64
  %".23" = and i64 %".22", 63
  %".24" = lshr i64 %".11", %".23"
  %".25" = and i64 15, %".24"
  %".26" = or i64 1, %".25"
  %".27" = trunc i64 %".26" to i8
  %".28" = zext i8 %".27" to i64
  %".29" = and i64 %".28", 63
  %".30" = shl i64 127996265, %".29"
  %".31" = or i64 %".21", %".30"
  %".32" = zext i8 4 to i64
  %".33" = and i64 %".32", 63
  %".34" = lshr i64 %".31", %".33"
  %".35" = and i64 15, %".34"
  %".36" = or i64 1, %".35"
  %".37" = sub i64 64, %".36"
  %".38" = trunc i64 %".37" to i8
  %".39" = zext i8 %".38" to i64
  %".40" = and i64 %".39", 63
  %".41" = lshr i64 %"SymVar_0", %".40"
  %".42" = zext i8 3 to i64
  %".43" = and i64 %".42", 63
  %".44" = lshr i64 %".11", %".43"
  %".45" = and i64 15, %".44"
  %".46" = or i64 1, %".45"
  %".47" = sub i64 64, %".46"
  %".48" = trunc i64 %".47" to i8
  %".49" = zext i8 %".48" to i64
  %".50" = and i64 %".49", 63
  %".51" = lshr i64 127996265, %".50"
  %".52" = zext i8 3 to i64
  %".53" = and i64 %".52", 63
  %".54" = lshr i64 %".11", %".53"
  %".55" = and i64 15, %".54"
  %".56" = or i64 1, %".55"
  %".57" = trunc i64 %".56" to i8
  %".58" = zext i8 %".57" to i64
  %".59" = and i64 %".58", 63
  %".60" = shl i64 127996265, %".59"
  %".61" = or i64 %".51", %".60"
  %".62" = zext i8 4 to i64
  %".63" = and i64 %".62", 63
  %".64" = lshr i64 %".61", %".63"
  %".65" = and i64 15, %".64"
  %".66" = or i64 1, %".65"
  %".67" = trunc i64 %".66" to i8
  %".68" = zext i8 %".67" to i64
  %".69" = and i64 %".68", 63
  %".70" = shl i64 %"SymVar_0", %".69"
  %".71" = or i64 %".41", %".70"
  %".72" = and i64 31, %".71"
  %".73" = zext i8 4 to i64
  %".74" = and i64 %".73", 63
  %".75" = shl i64 %".72", %".74"
  %".76" = or i64 %".75", %".11"
  %".77" = and i64 15, %".76"
  %".78" = zext i8 2 to i64
  %".79" = and i64 %".78", 63
  %".80" = shl i64 %".77", %".79"
  %".81" = or i64 %".80", %".76"
  %".82" = and i64 15, %".81"
  %".83" = or i64 1, %".82"
  %".84" = sub i64 64, %".83"
  %".85" = trunc i64 %".84" to i8
  %".86" = zext i8 %".85" to i64
  %".87" = and i64 %".86", 63
  %".88" = lshr i64 %".4", %".87"
  %".89" = and i64 15, %".81"
  %".90" = or i64 1, %".89"
  %".91" = trunc i64 %".90" to i8
  %".92" = zext i8 %".91" to i64
  %".93" = and i64 %".92", 63
  %".94" = shl i64 %".4", %".93"
  %".95" = or i64 %".88", %".94"
  %".96" = sext i64 343000538 to i128
  %".97" = sub i64 %"SymVar_0", 696182945
  %".98" = sext i64 %".97" to i128
  %".99" = mul i128 %".96", %".98"
  %".100" = trunc i128 %".99" to i64
  %".101" = lshr i64 %".100", 16
  %".102" = trunc i64 %".101" to i8
  %".103" = zext i8 %".102" to i16
  %".104" = lshr i64 %".100", 24
  %".105" = trunc i64 %".104" to i8
  %".106" = zext i8 %".105" to i16
  %".107" = shl i16 %".106", 8
  %".108" = or i16 %".103", %".107"
  %".109" = zext i16 %".108" to i32
  %".110" = zext i32 %".109" to i64
  %".111" = trunc i64 %".110" to i16
  %".112" = zext i16 %".111" to i32
  %".113" = zext i32 %".112" to i64
  %".114" = trunc i64 %".113" to i16
  %".115" = zext i16 %".114" to i32
  %".116" = zext i32 %".115" to i64
  %".117" = trunc i64 %".116" to i16
  %".118" = zext i16 %".117" to i32
  %".119" = zext i32 %".118" to i64
  %".120" = trunc i64 %".119" to i16
  %".121" = trunc i16 %".120" to i8
  %".122" = zext i8 %".121" to i64
  %".123" = trunc i64 %".119" to i16
  %".124" = lshr i16 %".123", 8
  %".125" = trunc i16 %".124" to i8
  %".126" = zext i8 %".125" to i64
  %".127" = shl i64 %".126", 8
  %".128" = or i64 %".122", %".127"
  %".129" = lshr i64 %".100", 32
  %".130" = trunc i64 %".129" to i8
  %".131" = zext i8 %".130" to i16
  %".132" = lshr i64 %".100", 40
  %".133" = trunc i64 %".132" to i8
  %".134" = zext i8 %".133" to i16
  %".135" = shl i16 %".134", 8
  %".136" = or i16 %".131", %".135"
  %".137" = zext i16 %".136" to i32
  %".138" = zext i32 %".137" to i64
  %".139" = trunc i64 %".138" to i16
  %".140" = zext i16 %".139" to i32
  %".141" = zext i32 %".140" to i64
  %".142" = trunc i64 %".141" to i16
  %".143" = zext i16 %".142" to i32
  %".144" = zext i32 %".143" to i64
  %".145" = trunc i64 %".144" to i16
  %".146" = zext i16 %".145" to i32
  %".147" = zext i32 %".146" to i64
  %".148" = trunc i64 %".147" to i16
  %".149" = trunc i16 %".148" to i8
  %".150" = zext i8 %".149" to i64
  %".151" = shl i64 %".150", 16
  %".152" = or i64 %".128", %".151"
  %".153" = trunc i64 %".147" to i16
  %".154" = lshr i16 %".153", 8
  %".155" = trunc i16 %".154" to i8
  %".156" = zext i8 %".155" to i64
  %".157" = shl i64 %".156", 24
  %".158" = or i64 %".152", %".157"
  %".159" = lshr i64 %".100", 48
  %".160" = trunc i64 %".159" to i8
  %".161" = zext i8 %".160" to i16
  %".162" = lshr i64 %".100", 56
  %".163" = trunc i64 %".162" to i8
  %".164" = zext i8 %".163" to i16
  %".165" = shl i16 %".164", 8
  %".166" = or i16 %".161", %".165"
  %".167" = zext i16 %".166" to i32
  %".168" = zext i32 %".167" to i64
  %".169" = trunc i64 %".168" to i16
  %".170" = zext i16 %".169" to i32
  %".171" = zext i32 %".170" to i64
  %".172" = trunc i64 %".171" to i16
  %".173" = zext i16 %".172" to i32
  %".174" = zext i32 %".173" to i64
  %".175" = trunc i64 %".174" to i16
  %".176" = zext i16 %".175" to i32
  %".177" = zext i32 %".176" to i64
  %".178" = trunc i64 %".177" to i16
  %".179" = zext i16 %".178" to i32
  %".180" = zext i32 %".179" to i64
  %".181" = trunc i64 %".180" to i16
  %".182" = zext i16 %".181" to i32
  %".183" = zext i32 %".182" to i64
  %".184" = trunc i64 %".183" to i16
  %".185" = zext i16 %".184" to i32
  %".186" = zext i32 %".185" to i64
  %".187" = trunc i64 %".186" to i16
  %".188" = zext i16 %".187" to i32
  %".189" = zext i32 %".188" to i64
  %".190" = trunc i64 %".189" to i16
  %".191" = trunc i16 %".190" to i8
  %".192" = zext i8 %".191" to i64
  %".193" = shl i64 %".192", 32
  %".194" = or i64 %".158", %".193"
  %".195" = trunc i64 %".189" to i16
  %".196" = lshr i16 %".195", 8
  %".197" = trunc i16 %".196" to i8
  %".198" = zext i8 %".197" to i64
  %".199" = shl i64 %".198", 40
  %".200" = or i64 %".194", %".199"
  %".201" = trunc i64 %".100" to i8
  %".202" = zext i8 %".201" to i16
  %".203" = lshr i64 %".100", 8
  %".204" = trunc i64 %".203" to i8
  %".205" = zext i8 %".204" to i16
  %".206" = shl i16 %".205", 8
  %".207" = or i16 %".202", %".206"
  %".208" = zext i16 %".207" to i32
  %".209" = zext i32 %".208" to i64
  %".210" = trunc i64 %".209" to i16
  %".211" = zext i16 %".210" to i32
  %".212" = zext i32 %".211" to i64
  %".213" = trunc i64 %".212" to i16
  %".214" = trunc i16 %".213" to i8
  %".215" = zext i8 %".214" to i64
  %".216" = shl i64 %".215", 48
  %".217" = or i64 %".200", %".216"
  %".218" = trunc i64 %".212" to i16
  %".219" = lshr i16 %".218", 8
  %".220" = trunc i16 %".219" to i8
  %".221" = zext i8 %".220" to i64
  %".222" = shl i64 %".221", 56
  %".223" = or i64 %".217", %".222"
  %".224" = zext i8 2 to i64
  %".225" = and i64 %".224", 63
  %".226" = lshr i64 %".223", %".225"
  %".227" = and i64 15, %".226"
  %".228" = or i64 1, %".227"
  %".229" = sub i64 64, %".228"
  %".230" = trunc i64 %".229" to i8
  %".231" = zext i8 %".230" to i64
  %".232" = and i64 %".231", 63
  %".233" = lshr i64 %".71", %".232"
  %".234" = zext i8 %".121" to i64
  %".235" = zext i8 %".125" to i64
  %".236" = shl i64 %".235", 8
  %".237" = or i64 %".234", %".236"
  %".238" = zext i8 %".149" to i64
  %".239" = shl i64 %".238", 16
  %".240" = or i64 %".237", %".239"
  %".241" = zext i8 %".155" to i64
  %".242" = shl i64 %".241", 24
  %".243" = or i64 %".240", %".242"
  %".244" = zext i8 %".191" to i64
  %".245" = shl i64 %".244", 32
  %".246" = or i64 %".243", %".245"
  %".247" = zext i8 %".197" to i64
  %".248" = shl i64 %".247", 40
  %".249" = or i64 %".246", %".248"
  %".250" = zext i8 %".214" to i64
  %".251" = shl i64 %".250", 48
  %".252" = or i64 %".249", %".251"
  %".253" = zext i8 %".220" to i64
  %".254" = shl i64 %".253", 56
  %".255" = or i64 %".252", %".254"
  %".256" = zext i8 2 to i64
  %".257" = and i64 %".256", 63
  %".258" = lshr i64 %".255", %".257"
  %".259" = and i64 15, %".258"
  %".260" = or i64 1, %".259"
  %".261" = trunc i64 %".260" to i8
  %".262" = zext i8 %".261" to i64
  %".263" = and i64 %".262", 63
  %".264" = shl i64 %".71", %".263"
  %".265" = or i64 %".233", %".264"
  %".266" = zext i8 4 to i64
  %".267" = and i64 %".266", 63
  %".268" = lshr i64 %".265", %".267"
  %".269" = and i64 15, %".268"
  %".270" = or i64 1, %".269"
  %".271" = sub i64 64, %".270"
  %".272" = trunc i64 %".271" to i8
  %".273" = zext i8 %".272" to i64
  %".274" = and i64 %".273", 63
  %".275" = shl i64 %".95", %".274"
  %".276" = and i64 15, %".81"
  %".277" = or i64 1, %".276"
  %".278" = sub i64 64, %".277"
  %".279" = trunc i64 %".278" to i8
  %".280" = zext i8 %".279" to i64
  %".281" = and i64 %".280", 63
  %".282" = lshr i64 %".4", %".281"
  %".283" = and i64 15, %".81"
  %".284" = or i64 1, %".283"
  %".285" = trunc i64 %".284" to i8
  %".286" = zext i8 %".285" to i64
  %".287" = and i64 %".286", 63
  %".288" = shl i64 %".4", %".287"
  %".289" = or i64 %".282", %".288"
  %".290" = zext i8 %".121" to i64
  %".291" = zext i8 %".125" to i64
  %".292" = shl i64 %".291", 8
  %".293" = or i64 %".290", %".292"
  %".294" = zext i8 %".149" to i64
  %".295" = shl i64 %".294", 16
  %".296" = or i64 %".293", %".295"
  %".297" = zext i8 %".155" to i64
  %".298" = shl i64 %".297", 24
  %".299" = or i64 %".296", %".298"
  %".300" = zext i8 %".191" to i64
  %".301" = shl i64 %".300", 32
  %".302" = or i64 %".299", %".301"
  %".303" = zext i8 %".197" to i64
  %".304" = shl i64 %".303", 40
  %".305" = or i64 %".302", %".304"
  %".306" = zext i8 %".214" to i64
  %".307" = shl i64 %".306", 48
  %".308" = or i64 %".305", %".307"
  %".309" = zext i8 %".220" to i64
  %".310" = shl i64 %".309", 56
  %".311" = or i64 %".308", %".310"
  %".312" = zext i8 2 to i64
  %".313" = and i64 %".312", 63
  %".314" = lshr i64 %".311", %".313"
  %".315" = and i64 15, %".314"
  %".316" = or i64 1, %".315"
  %".317" = sub i64 64, %".316"
  %".318" = trunc i64 %".317" to i8
  %".319" = zext i8 %".318" to i64
  %".320" = and i64 %".319", 63
  %".321" = lshr i64 %".71", %".320"
  %".322" = zext i8 %".121" to i64
  %".323" = zext i8 %".125" to i64
  %".324" = shl i64 %".323", 8
  %".325" = or i64 %".322", %".324"
  %".326" = zext i8 %".149" to i64
  %".327" = shl i64 %".326", 16
  %".328" = or i64 %".325", %".327"
  %".329" = zext i8 %".155" to i64
  %".330" = shl i64 %".329", 24
  %".331" = or i64 %".328", %".330"
  %".332" = zext i8 %".191" to i64
  %".333" = shl i64 %".332", 32
  %".334" = or i64 %".331", %".333"
  %".335" = zext i8 %".197" to i64
  %".336" = shl i64 %".335", 40
  %".337" = or i64 %".334", %".336"
  %".338" = zext i8 %".214" to i64
  %".339" = shl i64 %".338", 48
  %".340" = or i64 %".337", %".339"
  %".341" = zext i8 %".220" to i64
  %".342" = shl i64 %".341", 56
  %".343" = or i64 %".340", %".342"
  %".344" = zext i8 2 to i64
  %".345" = and i64 %".344", 63
  %".346" = lshr i64 %".343", %".345"
  %".347" = and i64 15, %".346"
  %".348" = or i64 1, %".347"
  %".349" = trunc i64 %".348" to i8
  %".350" = zext i8 %".349" to i64
  %".351" = and i64 %".350", 63
  %".352" = shl i64 %".71", %".351"
  %".353" = or i64 %".321", %".352"
  %".354" = zext i8 4 to i64
  %".355" = and i64 %".354", 63
  %".356" = lshr i64 %".353", %".355"
  %".357" = and i64 15, %".356"
  %".358" = or i64 1, %".357"
  %".359" = trunc i64 %".358" to i8
  %".360" = zext i8 %".359" to i64
  %".361" = and i64 %".360", 63
  %".362" = lshr i64 %".289", %".361"
  %".363" = or i64 %".275", %".362"
  ret i64 %".363"
}