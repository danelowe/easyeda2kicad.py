from easyeda2kicad.easyeda.parameters_easyeda import EeSymbolInfo


class MetadataProvider:
    def info(self, ee_data: dict, ee_data_info: dict) -> EeSymbolInfo:
        name_alias = ee_data_info.get("nameAlias", None)
        mpn = ee_data_info.get("BOM_Manufacturer Part", ee_data_info.get("name", ee_data.get("title", None)))
        value = None
        if name_alias:
            value = ee_data_info.get(name_alias, None)
        name = f'{ee_data_info["pre"].replace("?", "")}_{value}_{mpn}' if value else ee_data_info["name"]
        return EeSymbolInfo(
            name=name,
            prefix=ee_data_info["pre"],
            package=ee_data_info.get("package", None),
            manufacturer=ee_data_info.get("BOM_Manufacturer", None),
            datasheet=ee_data["lcsc"].get("url", None),
            lcsc_id=ee_data["lcsc"].get("number", None),
            jlc_id=ee_data_info.get("BOM_JLCPCB Part Class", None),
            mpn=mpn,
            description=ee_data.get("description", None),
            value=value
        )