<?xml version='1.0' encoding='UTF-8'?>
<Project Type="Project" LVVersion="18008000">
	<Item Name="我的电脑" Type="My Computer">
		<Property Name="NI.SortType" Type="Int">3</Property>
		<Property Name="server.app.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.control.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.tcp.enabled" Type="Bool">false</Property>
		<Property Name="server.tcp.port" Type="Int">0</Property>
		<Property Name="server.tcp.serviceName" Type="Str">????/VI???</Property>
		<Property Name="server.tcp.serviceName.default" Type="Str">????/VI???</Property>
		<Property Name="server.vi.callsEnabled" Type="Bool">true</Property>
		<Property Name="server.vi.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="specify.custom.address" Type="Bool">false</Property>
		<Item Name="M9700 Modbus Demo.vi" Type="VI" URL="../M9700 Modbus Demo.vi"/>
		<Item Name="依赖关系" Type="Dependencies">
			<Item Name="vi.lib" Type="Folder">
				<Item Name="VISA Configure Serial Port (Instr).vi" Type="VI" URL="/&lt;vilib&gt;/Instr/_visa.llb/VISA Configure Serial Port (Instr).vi"/>
				<Item Name="VISA Configure Serial Port" Type="VI" URL="/&lt;vilib&gt;/Instr/_visa.llb/VISA Configure Serial Port"/>
				<Item Name="VISA Configure Serial Port (Serial Instr).vi" Type="VI" URL="/&lt;vilib&gt;/Instr/_visa.llb/VISA Configure Serial Port (Serial Instr).vi"/>
			</Item>
			<Item Name="CTL Register Address.ctl" Type="VI" URL="../../../M9700 Driver/86/vi.lib/M9700 Modbus.llb/CTL Register Address.ctl"/>
			<Item Name="CTL CMD Register.ctl" Type="VI" URL="../../../M9700 Driver/86/vi.lib/M9700 Modbus.llb/CTL CMD Register.ctl"/>
			<Item Name="Read Input UIRP.vi" Type="VI" URL="../../../M9700 Driver/86/vi.lib/M9700 Modbus.llb/Read Input UIRP.vi"/>
			<Item Name="Read Input State.vi" Type="VI" URL="../../../M9700 Driver/86/vi.lib/M9700 Modbus.llb/Read Input State.vi"/>
			<Item Name="Write CMD Register.vi" Type="VI" URL="../../../M9700 Driver/86/vi.lib/M9700 Modbus.llb/Write CMD Register.vi"/>
			<Item Name="Write Single Value Register.vi" Type="VI" URL="../../../M9700 Driver/86/vi.lib/M9700 Modbus.llb/Write Single Value Register.vi"/>
			<Item Name="MB Modbus Command.ctl" Type="VI" URL="../../../M9700 Driver/86/vi.lib/M9700 Modbus.llb/MB Modbus Command.ctl"/>
			<Item Name="MB Modbus Data Unit.ctl" Type="VI" URL="../../../M9700 Driver/86/vi.lib/M9700 Modbus.llb/MB Modbus Data Unit.ctl"/>
			<Item Name="MB Decode Data.vi" Type="VI" URL="../../../M9700 Driver/86/vi.lib/M9700 Modbus.llb/MB Decode Data.vi"/>
			<Item Name="MB Modbus Command to Data Unit.vi" Type="VI" URL="../../../M9700 Driver/86/vi.lib/M9700 Modbus.llb/MB Modbus Command to Data Unit.vi"/>
			<Item Name="MB Serial String to Modbus Data Unit.vi" Type="VI" URL="../../../M9700 Driver/86/vi.lib/M9700 Modbus.llb/MB Serial String to Modbus Data Unit.vi"/>
			<Item Name="MB CRC-16.vi" Type="VI" URL="../../../M9700 Driver/86/vi.lib/M9700 Modbus.llb/MB CRC-16.vi"/>
			<Item Name="MB Serial Receive.vi" Type="VI" URL="../../../M9700 Driver/86/vi.lib/M9700 Modbus.llb/MB Serial Receive.vi"/>
			<Item Name="MB Serial Modbus Data Unit to String.vi" Type="VI" URL="../../../M9700 Driver/86/vi.lib/M9700 Modbus.llb/MB Serial Modbus Data Unit to String.vi"/>
			<Item Name="MB Serial Transmit.vi" Type="VI" URL="../../../M9700 Driver/86/vi.lib/M9700 Modbus.llb/MB Serial Transmit.vi"/>
			<Item Name="MB Serial Master Query.vi" Type="VI" URL="../../../M9700 Driver/86/vi.lib/M9700 Modbus.llb/MB Serial Master Query.vi"/>
			<Item Name="MB Serial Master Query Read Coils.vi" Type="VI" URL="../../../M9700 Driver/86/vi.lib/M9700 Modbus.llb/MB Serial Master Query Read Coils.vi"/>
			<Item Name="MB Serial Master Query Write Multiple Registers.vi" Type="VI" URL="../../../M9700 Driver/86/vi.lib/M9700 Modbus.llb/MB Serial Master Query Write Multiple Registers.vi"/>
			<Item Name="MB Serial Master Query Read Holding Registers.vi" Type="VI" URL="../../../M9700 Driver/86/vi.lib/M9700 Modbus.llb/MB Serial Master Query Read Holding Registers.vi"/>
		</Item>
		<Item Name="程序生成规范" Type="Build">
			<Item Name="M9700 Demo" Type="EXE">
				<Property Name="App_INI_aliasGUID" Type="Str">{FB02CEAF-B5A1-4293-928E-3529ED75289D}</Property>
				<Property Name="App_INI_GUID" Type="Str">{9DBCE783-2A33-4AB6-9661-2530AAEFBE49}</Property>
				<Property Name="App_serverConfig.httpPort" Type="Int">8002</Property>
				<Property Name="Bld_buildCacheID" Type="Str">{C8F8BB8C-9103-4E4A-AFA0-659D5397661C}</Property>
				<Property Name="Bld_buildSpecName" Type="Str">M9700 Demo</Property>
				<Property Name="Bld_defaultLanguage" Type="Str">ChineseS</Property>
				<Property Name="Bld_excludeLibraryItems" Type="Bool">true</Property>
				<Property Name="Bld_excludePolymorphicVIs" Type="Bool">true</Property>
				<Property Name="Bld_localDestDir" Type="Path">/F/LabView/NI_AB_PROJECTNAME/M9700 Demo</Property>
				<Property Name="Bld_modifyLibraryFile" Type="Bool">true</Property>
				<Property Name="Bld_previewCacheID" Type="Str">{86E9B2E5-2EF0-4883-9436-111D3423194E}</Property>
				<Property Name="Bld_targetDestDir" Type="Path"></Property>
				<Property Name="Bld_version.major" Type="Int">1</Property>
				<Property Name="Destination[0].destName" Type="Str">M9700 Demo.exe</Property>
				<Property Name="Destination[0].path" Type="Path">/F/LabView/NI_AB_PROJECTNAME/M9700 Demo/M9700 Demo.exe</Property>
				<Property Name="Destination[0].path.type" Type="Str">&lt;none&gt;</Property>
				<Property Name="Destination[0].type" Type="Str">App</Property>
				<Property Name="Destination[1].destName" Type="Str">????</Property>
				<Property Name="Destination[1].path" Type="Path">/F/LabView/NI_AB_PROJECTNAME/M9700 Demo/data</Property>
				<Property Name="Destination[1].path.type" Type="Str">&lt;none&gt;</Property>
				<Property Name="DestinationCount" Type="Int">2</Property>
				<Property Name="Exe_actXinfo_enumCLSID[0]" Type="Str">{2F4C2B07-941B-4EA6-A9DA-EABDC12994D7}</Property>
				<Property Name="Exe_actXinfo_enumCLSID[1]" Type="Str">{3C0FE734-0DB3-4A0C-8FB2-2D059F6DBBD6}</Property>
				<Property Name="Exe_actXinfo_enumCLSID[10]" Type="Str">{B38EC032-0175-4BFB-8253-9EEEE9976BC4}</Property>
				<Property Name="Exe_actXinfo_enumCLSID[11]" Type="Str">{BD31FCFC-B104-4C8D-84C8-BFF32751768F}</Property>
				<Property Name="Exe_actXinfo_enumCLSID[12]" Type="Str">{1F70B51D-23E1-45B8-A56B-FE03E33BE57D}</Property>
				<Property Name="Exe_actXinfo_enumCLSID[13]" Type="Str">{4BB2B949-EE48-460C-99BF-6F9CDAEAC710}</Property>
				<Property Name="Exe_actXinfo_enumCLSID[14]" Type="Str">{0E2BD99D-9F9D-4C59-B41F-C86641D5D97D}</Property>
				<Property Name="Exe_actXinfo_enumCLSID[15]" Type="Str">{40A777C6-C9CC-46C1-AF3E-B3030A61D6FB}</Property>
				<Property Name="Exe_actXinfo_enumCLSID[16]" Type="Str">{B1430310-A786-45EC-9D6F-9C3926153FD9}</Property>
				<Property Name="Exe_actXinfo_enumCLSID[2]" Type="Str">{CFBE1D37-798A-4C05-8794-C4DB570D4822}</Property>
				<Property Name="Exe_actXinfo_enumCLSID[3]" Type="Str">{FAD44029-2F81-4765-BDE8-B49125BBAACE}</Property>
				<Property Name="Exe_actXinfo_enumCLSID[4]" Type="Str">{A91FDB7D-888C-48FB-BD4B-D5634CCE782A}</Property>
				<Property Name="Exe_actXinfo_enumCLSID[5]" Type="Str">{69C023CA-8998-46E2-8442-3BB5C5342662}</Property>
				<Property Name="Exe_actXinfo_enumCLSID[6]" Type="Str">{0B4B8C27-135E-43AB-AF60-D45151B7CA48}</Property>
				<Property Name="Exe_actXinfo_enumCLSID[7]" Type="Str">{F6B3089F-D2D6-42D2-9BC4-D9CB295C5D23}</Property>
				<Property Name="Exe_actXinfo_enumCLSID[8]" Type="Str">{623FC285-5179-4C7B-AD84-DD5CCF39CAF2}</Property>
				<Property Name="Exe_actXinfo_enumCLSID[9]" Type="Str">{76C436A2-6AA1-435A-9539-1A65992629B7}</Property>
				<Property Name="Exe_actXinfo_enumCLSIDsCount" Type="Int">17</Property>
				<Property Name="Exe_actXinfo_majorVersion" Type="Int">5</Property>
				<Property Name="Exe_actXinfo_minorVersion" Type="Int">5</Property>
				<Property Name="Exe_actXinfo_objCLSID[0]" Type="Str">{BBB18AEF-140B-42CD-9D72-91C6578247C0}</Property>
				<Property Name="Exe_actXinfo_objCLSID[1]" Type="Str">{169BFC5F-926B-4C62-B04F-B138F74917E0}</Property>
				<Property Name="Exe_actXinfo_objCLSID[2]" Type="Str">{106389D2-B99A-4389-9016-AA0B3CC8D439}</Property>
				<Property Name="Exe_actXinfo_objCLSID[3]" Type="Str">{E0093534-C83E-4AE1-BD03-17832363BC35}</Property>
				<Property Name="Exe_actXinfo_objCLSID[4]" Type="Str">{885247BA-FDE3-4DD6-B3F4-EFB895D755E7}</Property>
				<Property Name="Exe_actXinfo_objCLSID[5]" Type="Str">{DB073904-60AA-4646-A01B-50CF8DE8676C}</Property>
				<Property Name="Exe_actXinfo_objCLSIDsCount" Type="Int">6</Property>
				<Property Name="Exe_actXinfo_progIDPrefix" Type="Str">M9700Demo</Property>
				<Property Name="Exe_actXServerName" Type="Str">M9700Demo</Property>
				<Property Name="Exe_actXServerNameGUID" Type="Str">{D5C57C25-07C2-40F8-B165-0C41F4379E56}</Property>
				<Property Name="Source[0].itemID" Type="Str">{3D549145-127C-4D42-92E1-6112CEA0492E}</Property>
				<Property Name="Source[0].type" Type="Str">Container</Property>
				<Property Name="Source[1].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[1].itemID" Type="Ref">/????/M9700 Modbus Demo.vi</Property>
				<Property Name="Source[1].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[1].type" Type="Str">VI</Property>
				<Property Name="SourceCount" Type="Int">2</Property>
				<Property Name="TgtF_companyName" Type="Str">Maynuo Electronic Co.,Ltd.</Property>
				<Property Name="TgtF_fileDescription" Type="Str">M9700 Demo</Property>
				<Property Name="TgtF_internalName" Type="Str">M9700 Demo</Property>
				<Property Name="TgtF_legalCopyright" Type="Str">Copyright 2010</Property>
				<Property Name="TgtF_productName" Type="Str">M9700 Demo</Property>
				<Property Name="TgtF_targetfileGUID" Type="Str">{31AB1B48-57AB-4E5E-87A6-06380AECE10E}</Property>
				<Property Name="TgtF_targetfileName" Type="Str">M9700 Demo.exe</Property>
			</Item>
		</Item>
	</Item>
</Project>
