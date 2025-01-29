from aiogram_dialog import DialogManager


async def get_photo_conversion_formats(dialog_manager: DialogManager, **kwargs):
    formats = [
        ("JPEG",),
        ("PNG",),
    ]

    current_format = dialog_manager.dialog_data.get("filename").split(".")[-1].upper()
    
    if (current_format,) in formats:
        formats.remove((current_format,))

    return {"formats": formats}


async def get_photo_url(dialog_manager: DialogManager, **kwargs):
    image_path = dialog_manager.dialog_data.get("image_path")

    return {"path": image_path}
