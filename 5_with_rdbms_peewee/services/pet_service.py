from models.pet import Pet
from dto.pet_dto import PetDTO
from orm import postgresql
from orm.pet_orm import PetORM


class PetService:
    @staticmethod
    @postgresql().atomic()
    async def addPetData(pet_request: PetDTO):
        pet = Pet(
            pet_id=pet_request.petId,
            group_id=pet_request.groupId,
            some_fields=pet_request.someFields,
        )
        await PetORM.save(pet)
        return pet

    @staticmethod
    @postgresql().atomic()
    async def addPetList(pet_request: PetDTO):
        pet_list = list(
            map(
                lambda x: Pet(
                    pet_id=pet_request.petId + str(x),
                    group_id=pet_request.groupId,
                    some_fields=pet_request.someFields,
                ),
                [1, 2, 3],
            )
        )
        print(pet_list[0].pet_id, pet_list[1].pet_id, pet_list[2].dict())
        await PetORM.save_all(pet_list)

    @staticmethod
    async def getPetData(pet_id: str):
        return await PetORM.find_by_pet_id(pet_id=pet_id)

    @staticmethod
    async def getPetDataByGroupId(group_id: str):
        return await PetORM.find_by_group_id(group_id=group_id)

    @staticmethod
    @postgresql().atomic()
    async def modifyPetData(pet_id: str, pet_request: PetDTO):
        pet = await PetORM.find_by_pet_id(pet_id=pet_id)

        pet.pet_id = pet_request.petId
        pet.group_id = pet_request.groupId
        pet.some_fields = pet_request.someFields
        await PetORM.save(pet)

        return pet

    @staticmethod
    @postgresql().atomic()
    async def deletePetData(pet_id: str):
        await PetORM.delete_by_id(pet_id=pet_id)
