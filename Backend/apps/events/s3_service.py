import mimetypes
import uuid

import boto3
from django.conf import settings


def _get_s3_client():
    """
    Локально: берёт ключи из env (через settings).
    В ECS: можно будет убрать ключи из env и использовать IAM Role — boto3 подхватит сам.
    """
    kwargs = {"region_name": settings.AWS_S3_REGION_NAME}

    access_key = getattr(settings, "AWS_ACCESS_KEY_ID", None)
    secret_key = getattr(settings, "AWS_SECRET_ACCESS_KEY", None)

    if access_key and secret_key:
        kwargs.update(
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
        )

    return boto3.client("s3", **kwargs)


def upload_card_photo_to_s3(file_obj, *, key_prefix: str = "cards") -> str:
    """
    Загружает файл в S3 и возвращает URL, который можно сохранять в URLField.
    """
    s3 = _get_s3_client()

    original_name = getattr(file_obj, "name", "")
    ext = (original_name.rsplit(".", 1)[-1] if "." in original_name else "jpg").lower()

    key = f"{key_prefix}/{uuid.uuid4().hex}.{ext}"

    content_type, _ = mimetypes.guess_type(original_name)
    extra_args = {"ContentType": content_type or "application/octet-stream"}


    s3.upload_fileobj(
        Fileobj=file_obj,
        Bucket=settings.AWS_STORAGE_BUCKET_NAME,
        Key=key,
        ExtraArgs=extra_args,
    )

    # Формируем URL
    return f"https://{settings.AWS_S3_CUSTOM_DOMAIN}/{key}"