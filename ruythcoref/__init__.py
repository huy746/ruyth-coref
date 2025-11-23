from .advanced_file_converter import AdvancedFileConverter

def convert(src_path, dest_path):
    """Hàm tiện lợi để chuyển đổi file"""
    return AdvancedFileConverter.convert(src_path, dest_path)

__all__ = ["convert", "AdvancedFileConverter"]
