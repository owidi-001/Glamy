import coreschema
from rest_framework.schemas import AutoSchema
import coreapi


class ProductSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_fields = []
        if method.lower() == ["post", "put"]:
            extra_fields = [
                coreapi.Field(
                    "category",
                    required=True,
                    example="",
                    location="form",
                    schema=coreschema.Object(
                        description="""
                                    properties - name,
                                    """,
                    ),
                ),
                coreapi.Field(
                    "name",
                    required=True,
                    location="form",
                    schema=coreschema.Integer(
                        description="Product name",
                    ),
                ),
                coreapi.Field(
                    "manufacturer",
                    required=True,
                    location="form",
                    schema=coreschema.Integer(
                        description="Product manufacturer",
                    ),
                ),
                coreapi.Field(
                    "description",
                    required=False,
                    location="form",
                    schema=coreschema.Integer(
                        description="More info on the product",
                    ),
                ),
                coreapi.Field(
                    "slug",
                    required=False,
                    location="form",
                    schema=coreschema.Integer(
                        description="slug",
                    ),
                ),
                coreapi.Field(
                    "image",
                    required=False,
                    location="form",
                    schema=coreschema.Integer(
                        description="image_url",
                    ),
                ),
                coreapi.Field(
                    "price",
                    required=False,
                    location="form",
                    schema=coreschema.Integer(
                        description="Product price",
                    ),
                ),
                coreapi.Field(
                    "created_by",
                    required=False,
                    location="form",
                    schema=coreschema.Integer(
                        description="Product vendor",
                    ),
                ),
            ]
        if method.lower() == "patch":
            extra_fields = [
                coreapi.Field(
                    "price",
                    required=True,
                    location="form",
                    schema=coreschema.Integer(
                        description="Adjust price",
                    ),
                ),
            ]
        manual_fields = super().get_manual_fields(path, method)
        return manual_fields + extra_fields


class CategorySchema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_fields = []
        if method.lower() == "post":
            extra_fields = [
                coreapi.Field("name", required=True, location="form"),
            ]
        manual_fields = super().get_manual_fields(path, method)
        return manual_fields + extra_fields
