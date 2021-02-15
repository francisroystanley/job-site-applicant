from mongoengine import *
import datetime


class UserSessionSchema(Document):
    meta = {
        'collection': 'sessions',
        'indexes': [
            {
                'fields': ['expiry'],
                'expireAfterSeconds': 3600
            }
        ]
    }
    acct_code = StringField()
    login_name = StringField()
    group_code = StringField()
    company_code = StringField()
    uuid = StringField()
    last_login = DateTimeField()
    password_reset_count = IntField()
    account_activated = BooleanField()

    login_params = DynamicField()
    policy = DynamicField()
    policy_params = DynamicField()
    person = DynamicField()
    businessunit = DynamicField()
    user_agent = StringField()
    client_ipaddress = StringField()
    device = StringField()
    status = StringField()
    user_type = StringField()
    auth_token = StringField()
    auth_provider = StringField()

    createdate = DateTimeField(default=datetime.datetime.utcnow)
    expiry = DateTimeField()


class BusinessUnitSchema(Document):
    meta = {
        'collection': 'businessunit',
        'indexes': [
            {
                'fields': ['expiry'],
                'expireAfterSeconds': 0
            }
        ]
    }
    bu_id = DynamicField()
    organization_id = DynamicField()
    businessunit_code = StringField()
    businessunit_name = StringField()
    logo_image = DynamicField()
    banner_image = DynamicField()
    contact_email = StringField()
    contact_number = StringField()
    address = StringField()
    description = DynamicField()
    created_by = StringField()
    date_created = DynamicField()
    date_updated = DynamicField()

    createdate = DateTimeField(default=datetime.datetime.utcnow)
    expiry = DateTimeField()


class CitizenshipSchema(Document):
    meta = {
        'collection': 'citizenship'
    }
    code = StringField()
    name = StringField()


class CitySchema(Document):
    meta = {
        'collection': 'city'
    }
    city_code = StringField()
    city_name = StringField()
    province_code = StringField()
    province_name = StringField()
    country_code = StringField()


class CountrySchema(Document):
    meta = {
        'collection': 'country'
    }
    country_code = StringField()
    country_name = StringField()


class JobClassCategorySchema(EmbeddedDocument):
    category_code = StringField()
    category_name = StringField()


class JobClassSchema(Document):
    meta = {
        'collection': 'job_class'
    }
    job_class_code = StringField()
    job_class_name = StringField()
    job_class_category = EmbeddedDocumentListField(JobClassCategorySchema)


class ProvinceSchema(Document):
    meta = {
        'collection': 'province'
    }
    province_code = StringField()
    province_name = StringField()
    country_code = StringField()


class ReligionSchema(Document):
    meta = {
        'collection': 'religion'
    }
    code = StringField()
    name = StringField()
