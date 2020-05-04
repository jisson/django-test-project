import logging

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.db import IntegrityError

from django_test_project.apps.listings import constants as listings_constants
from django_test_project.apps.listings import factories as listings_factories
from django_test_project.apps.users import factories as users_factories
from django_test_project.apps.users.models import ListingOwner

logger = logging.getLogger("django_test_project.listings")


def create_listings_for_owner(owner: ListingOwner):
    # First clean any already existing listings before to create new listings.
    logger.info(f"Cleaning already existing listings for owner: {owner} ...")
    owner.listings.all().delete()

    # Create 5 active listings ...
    logger.info(f"Creating 5 active listings for owner: {owner}")
    listings_factories.ActiveListingFactory.create_batch(5, owner=owner)

    # ... and 3 drafts.
    logger.info(f"Creating 3 drafts listings for owner: {owner}")
    listings_factories.ListingFactory.create_batch(
        3, owner=owner, status=listings_constants.LISTING_STATUS_DRAFT,
    )


def _create_listings_owner(username: str):
    try:
        logger.info(f"Creating user {username} ...")
        return users_factories.ActiveListingOwnerFactory(username=username)
    except IntegrityError:
        logger.info(f"User {username} already exists.")
        return get_user_model().objects.get(username=username)


def create_listings_owners() -> list:
    owner_joe = _create_listings_owner("Joe")
    owner_averell = _create_listings_owner("Averell")
    owner_william = _create_listings_owner("William")
    owner_jack = _create_listings_owner("Jack")

    return [
        owner_joe,
        owner_averell,
        owner_william,
        owner_jack,
    ]


def create_demo_user():
    logger.info("Creating demo user ...")
    try:
        get_user_model().objects.create_superuser(
            username="demo", email="demo@gmail.com", password="password",
        )
    except IntegrityError:
        logger.info("Demo user already exists.")

    logger.info(
        "You should now be able to login as the demo user with the following credentials:\n"
        " - username: demo\n"
        " - password: password\n"
    )


class Command(BaseCommand):

    help = "Populate the database with test data."

    def handle(self, *args, **options):
        owners = create_listings_owners()
        for owner in owners:
            logger.info(f"Processing listings for owner: {owner}")
            create_listings_for_owner(owner)

        create_demo_user()

        logger.info("All done !")
