resource_list_schema = {
    "page": int,
    "per_page": int,
    "total": int,
    "total_pages": int,
    "data": [
        {
            "id": int,
            "name": str,
            "year": int,
            "color": str,
            "pantone_value": str,
        }
    ],
}


register_success_schema = {
    "id": str,
    "token": str,
}

create_user_schema = {
    "name": str,
    "job": str,
    "id": int,
    "createdAt": str,
}

update_schema = {
    "updatedAt": str,
}
