from py_tresos.models.plugin_folder_mgr import eb_plugin_create
import pytest
import os.path
import shutil

class TestPluginFolderMgr:

    def setup_class(self):
        print("Initialize TestPluginFolderMgr Class")

    def teardown_class(self):
        print("Cleanup TestPluginFolderMgr Class")
        #shutil.rmtree("Plugin_Demo_TS_TxDxM1I0R0")

    def testPluginCreate(self):
        eb_plugin_create("toml/plugin_demo.toml")

        assert(os.path.isdir("Plugin_Demo_TS_TxDxM1I0R0") == True)
        assert(os.path.isdir("Plugin_Demo_TS_TxDxM1I0R0/config") == True)
        assert(os.path.isfile("Plugin_Demo_TS_TxDxM1I0R0/config/Plugin_Demo.xdm") == True)
        assert(os.path.isfile("Plugin_Demo_TS_TxDxM1I0R0/doc/Plugin_Demo_um.md") == True)
        
        assert(os.path.isdir("Plugin_Demo_TS_TxDxM1I0R0/generate/include") == True)
        assert(os.path.isdir("Plugin_Demo_TS_TxDxM1I0R0/generate/src") == True)
        assert(os.path.isdir("Plugin_Demo_TS_TxDxM1I0R0/generate_swcd/swcd") == True)

        assert(os.path.isfile("Plugin_Demo_TS_TxDxM1I0R0/include/Plugin_Demo.h") == True)
        assert(os.path.isfile("Plugin_Demo_TS_TxDxM1I0R0/make/Plugin_Demo_defs.mak") == True)
        assert(os.path.isfile("Plugin_Demo_TS_TxDxM1I0R0/make/Plugin_Demo_rules.mak") == True)
        assert(os.path.isfile("Plugin_Demo_TS_TxDxM1I0R0/META-INF/MANIFEST.MF") == True)

        assert(os.path.isfile("Plugin_Demo_TS_TxDxM1I0R0/src/Plugin_Demo.c") == True)
        assert(os.path.isfile("Plugin_Demo_TS_TxDxM1I0R0/build.properties") == True)
        assert(os.path.isfile("Plugin_Demo_TS_TxDxM1I0R0/Plugin_Demo.ant") == True)
        assert(os.path.isfile("Plugin_Demo_TS_TxDxM1I0R0/plugin.xml") == True)