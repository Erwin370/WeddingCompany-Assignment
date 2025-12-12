from fastapi import APIRouter, HTTPException, Depends
from ..models.organization import OrganizationCreate, OrganizationResponse
from ..utils.database import db
from ..utils.auth import hash_password

router = APIRouter()

@router.post("/org/create", response_model=OrganizationResponse)
async def create_organization(org: OrganizationCreate):
    existing_org = await db.master.find_one({"organization_name": org.organization_name})
    if existing_org:
        raise HTTPException(status_code=400, detail="Organization already exists")

    collection_name = f"org_{org.organization_name}"
    hashed_password = hash_password(org.password)

    # Insert into master database
    new_org = {
        "organization_name": org.organization_name,
        "collection_name": collection_name,
        "admin_email": org.email,
        "admin_password": hashed_password
    }
    await db.master.insert_one(new_org)

    # Create dynamic collection
    await db.create_collection(collection_name)

    return OrganizationResponse(
        organization_name=org.organization_name,
        collection_name=collection_name,
        admin_email=org.email
    )