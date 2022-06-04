from py_tresos.models.plugin_info import PluginInfo
import pytest

class TestPluginInfo:
    def test_constructor(self):
        plugin_info = PluginInfo()

        assert(plugin_info.name == "")
        assert(plugin_info.tresos_root == "")
        assert(plugin_info.header_files == [])
        assert(plugin_info.source_files == [])
        assert(plugin_info.gen_header_files == [])
        assert(plugin_info.gen_source_files == [])
        assert(plugin_info.header_file_tpl == "")
        assert(plugin_info.source_file_tpl == "")
        assert(plugin_info.ar_package == "")
        with pytest.raises(Exception) as err:
            value = plugin_info.eb_version
        assert(str(err.value) == "Invalid EB version (0.0.0)")
        with pytest.raises(Exception) as err:
            value = plugin_info.ar_version
        assert(str(err.value) == "Invalid AR version (0.0.0)")
        with pytest.raises(Exception) as err:
            value = plugin_info.root_path
        assert(str(err.value) == "Invalid Plugin Name ()")
        assert(plugin_info.uppercase_name == "")
        assert(plugin_info.gen_files_text == "")
        assert(plugin_info.src_files_text == "")
        assert(plugin_info.vendor_id == "0x0000")


    def test_parse(self):
        plugin_info = PluginInfo()
        plugin_info.parse('toml/plugin_demo.toml')

        assert(plugin_info.name == "Plugin_Demo")
        assert(plugin_info.tresos_root == "X:/tresos")
        assert(plugin_info.header_files == ["Plugin_Demo.h"])
        assert(plugin_info.source_files == ["Plugin_Demo.c"])
        assert(plugin_info.gen_header_files == ["Plugin_Demo_Cfg.h"])
        assert(plugin_info.gen_source_files == ["Plugin_Demo_Cfg.c"])
        assert(plugin_info.header_file_tpl == "")
        assert(plugin_info.source_file_tpl == "")
        assert(plugin_info.ar_package == "ARRoot")
        assert(plugin_info.eb_version == "TxDxM1I0R0")
        assert(plugin_info.ar_version == "4.0.3")
        assert(plugin_info.root_path == "Plugin_Demo_TS_TxDxM1I0R0")
        assert(plugin_info.uppercase_name == "PLUGIN_DEMO")
        assert(plugin_info.gen_files_text == 
                ("\t$(Plugin_Demo_OUTPUT_PATH)/include/Plugin_Demo_Cfg.h \\\n"
                 "\t$(Plugin_Demo_OUTPUT_PATH)/src/Plugin_Demo_Cfg.c"))
        assert(plugin_info.src_files_text == 
                ("\t$(Plugin_Demo_CORE_PATH)/src/Plugin_Demo.c"))
        assert(plugin_info.vendor_id == "0x0008")