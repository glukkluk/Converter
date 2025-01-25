async def get_photo_conversion_formats(**kwargs):
    formats = [
        ("JPEG", ),
        ("PNG", ),
    ]

    return {
        "formats": formats
    }