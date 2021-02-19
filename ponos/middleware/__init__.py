from flask_restful import Api

# Security Handlers
from .forgot_password import ForgotPasswordHandler
from .linkedin import LinkedInAuthRequestHandler, LinkedInAuthCallbackHandler
from .recaptcha import RecaptchaHandler
from .user import LoginHandler, User
from .user import AuthenticateHandler, MeHandler, UserMeHandler, UserGroupHandler
from .user import UserParamsHandler, UserPasswordHandler, UserPolicyHandler
from .user import UserPhotoHandler, UserResumeHandler

# System Handlers
from .activate import ActivateHandler
from .branch import BranchHandler
from .businessunit import BusinessUnitHandler, BusinessUnitPhotoHandler
from .consent import ConsentHandler
from .email import EmailVerifyHandler
from .env import EnvHandler
from .file_download import AttachmentHandler, ImageHandler, PhotoHandler, ResumeHandler
from .job_ad import JobAdHandler, JobAdApplicationHandler
from .job_ad import JobAdApplicationQuickHandler, JobAdSearchTagHandler, JobAdTagHandler
from .job_class import JobClassHandler
from .license import LicenseHandler
from .organization import OrganizationJobtitleHandler
from .person import PersonHandler, PersonProfileAffiliationHandler, PersonProfileAttachmentHandler
from .person import PersonProfileCertificateHandler, PersonProfileConsentHandler, PersonProfileDetailHandler
from .person import PersonProfileEducationHandler, PersonProfileIdentificationHandler, PersonProfileLicenseHandler
from .person import PersonProfilePortfolioHandler, PersonProfilePreferenceHandler, PersonProfileSkillHandler
from .person import PersonProfileSocialLinksHandler, PersonProfileTrainingHandler, PersonProfileWorkHistoryHandler
from .person import PersonRegisterHandler
from .place import CityHandler, ProvinceHandler
from .profile import CitizenshipHandler, ReligionHandler
from .request import RequestHandler
from .skill import SkillHandler
from .status import AllStatusActionHandler, StatusHandler, StatusActionHandler


class MiddleWare(object):
    def __init__(self, app):
        self.__api = Api(app)

        # Security Endpoints
        self.__api.add_resource(AuthenticateHandler, '/api/authenticate')
        self.__api.add_resource(ForgotPasswordHandler, '/api/forgotpassword')
        self.__api.add_resource(RecaptchaHandler, '/api/recaptcha')
        self.__api.add_resource(LinkedInAuthRequestHandler, '/auth/linkedin/request')
        self.__api.add_resource(LinkedInAuthCallbackHandler, '/auth/linkedin/callback')
        self.__api.add_resource(LoginHandler, '/api/login')
        self.__api.add_resource(MeHandler, '/api/user/me')
        self.__api.add_resource(UserGroupHandler, '/api/user/<login_uuid>/group')
        self.__api.add_resource(UserMeHandler, '/api/me')
        self.__api.add_resource(UserParamsHandler, '/api/user/<login_uuid>/parameters')
        self.__api.add_resource(UserPasswordHandler, '/api/user/change_password')
        self.__api.add_resource(UserPhotoHandler, '/api/user/<person_id>/photo')
        self.__api.add_resource(UserPolicyHandler, '/api/user/<login_uuid>/policy')
        self.__api.add_resource(UserPolicyHandler, '/api/user/<login_uuid>/policy/<id>', endpoint='userpolicyinfo')
        self.__api.add_resource(UserResumeHandler, '/api/user/<person_id>/resume')

        # System Endpoints
        self.__api.add_resource(ActivateHandler, '/api/activate')
        self.__api.add_resource(AllStatusActionHandler, '/api/status_action')
        self.__api.add_resource(AttachmentHandler, '/attachment/<file_type>/<file_name>')
        self.__api.add_resource(BranchHandler, '/api/branch')
        self.__api.add_resource(BusinessUnitHandler, '/api/businessunit')
        self.__api.add_resource(BusinessUnitPhotoHandler, '/api/businessunit/<businessunit_id>/photo')
        self.__api.add_resource(CitizenshipHandler, '/api/citizenship')
        self.__api.add_resource(CityHandler, '/api/city')
        self.__api.add_resource(ConsentHandler, '/api/consent')
        self.__api.add_resource(EmailVerifyHandler, '/api/verify')
        self.__api.add_resource(EnvHandler, '/api/env')
        self.__api.add_resource(ImageHandler, '/<image>/<file_name>', endpoint='image')
        self.__api.add_resource(JobAdHandler, '/api/job_ad')
        self.__api.add_resource(JobAdHandler, '/api/job_ad/<id>', endpoint="job_ad_per_id")
        self.__api.add_resource(JobAdTagHandler, '/api/job_ad/<id>/search_tag', endpoint="job_ad_self_tag")
        self.__api.add_resource(JobAdApplicationHandler, '/api/job_ad_application')
        self.__api.add_resource(JobAdApplicationHandler, '/api/job_ad_application/<id>', endpoint="job_ad_application_per_id")
        self.__api.add_resource(JobAdApplicationQuickHandler, '/api/job_ad_application_quick')
        self.__api.add_resource(JobAdSearchTagHandler, '/api/job_ad_search_tag')
        self.__api.add_resource(JobClassHandler, '/api/job_class')
        self.__api.add_resource(LicenseHandler, '/api/license')
        self.__api.add_resource(LicenseHandler, '/api/license/<id>', endpoint="license_per_id")
        self.__api.add_resource(OrganizationJobtitleHandler, '/api/organization/jobtitle/<id>')
        self.__api.add_resource(PersonHandler, '/api/person')
        self.__api.add_resource(PersonProfileAffiliationHandler, '/api/person_affiliation')
        self.__api.add_resource(PersonProfileAffiliationHandler, '/api/person_affiliation/<id>', endpoint="person_affiliation_per_id")
        self.__api.add_resource(PersonProfileAttachmentHandler, '/api/person_attachment')
        self.__api.add_resource(PersonProfileAttachmentHandler, '/api/person_attachment/<id>', endpoint="person_attachment_per_id")
        self.__api.add_resource(PersonProfileCertificateHandler, '/api/person_certificate')
        self.__api.add_resource(PersonProfileCertificateHandler, '/api/person_certificate/<id>', endpoint="person_certificate_per_id")
        self.__api.add_resource(PersonProfileConsentHandler, '/api/person_consent')
        self.__api.add_resource(PersonProfileConsentHandler, '/api/person_consent/<id>', endpoint="person_consent_per_id")
        self.__api.add_resource(PersonProfileDetailHandler, '/api/person_detail')
        self.__api.add_resource(PersonProfileDetailHandler, '/api/person_detail/<id>', endpoint="person_detail_per_id")
        self.__api.add_resource(PersonProfileEducationHandler, '/api/person_education')
        self.__api.add_resource(PersonProfileEducationHandler, '/api/person_education/<id>', endpoint="person_education_id")
        self.__api.add_resource(PersonProfileIdentificationHandler, '/api/person_identification')
        self.__api.add_resource(PersonProfileIdentificationHandler, '/api/person_identification/<id>', endpoint="person_identification_per_id")
        self.__api.add_resource(PersonProfileLicenseHandler, '/api/person_license')
        self.__api.add_resource(PersonProfileLicenseHandler, '/api/person_license/<id>', endpoint="person_license_per_id")
        self.__api.add_resource(PersonProfilePortfolioHandler, '/api/person_portfolio')
        self.__api.add_resource(PersonProfilePortfolioHandler, '/api/person_portfolio/<id>', endpoint="person_portfolio_per_id")
        self.__api.add_resource(PersonProfilePreferenceHandler, '/api/person_preference')
        self.__api.add_resource(PersonProfilePreferenceHandler, '/api/person_preference/<id>', endpoint="person_preference_per_id")
        self.__api.add_resource(PersonProfileSkillHandler, '/api/person_skill')
        self.__api.add_resource(PersonProfileSkillHandler, '/api/person_skill/<id>', endpoint="person_skill_per_id")
        self.__api.add_resource(PersonProfileSocialLinksHandler, '/api/person_social_link')
        self.__api.add_resource(PersonProfileSocialLinksHandler, '/api/person_social_link/<id>', endpoint="person_social_link_per_id")
        self.__api.add_resource(PersonProfileTrainingHandler, '/api/person_training')
        self.__api.add_resource(PersonProfileTrainingHandler, '/api/person_training/<id>', endpoint="person_training_per_id")
        self.__api.add_resource(PersonProfileWorkHistoryHandler, '/api/person_work_history')
        self.__api.add_resource(PersonProfileWorkHistoryHandler, '/api/person_work_history/<id>', endpoint="person_work_history_per_id")
        self.__api.add_resource(PersonRegisterHandler, '/api/register')
        self.__api.add_resource(PhotoHandler, '/photo/<file_name>')
        self.__api.add_resource(ProvinceHandler, '/api/province')
        self.__api.add_resource(ReligionHandler, '/api/religion')
        self.__api.add_resource(RequestHandler, '/api/request/purge_person')
        self.__api.add_resource(ResumeHandler, '/resume/<file_name>')
        self.__api.add_resource(SkillHandler, '/api/skill')
        self.__api.add_resource(StatusHandler, '/api/status')
        self.__api.add_resource(StatusHandler, '/api/status/<id>', endpoint='status_self')
        self.__api.add_resource(StatusActionHandler, '/api/status/<status_id>/action', endpoint='status_action')
        self.__api.add_resource(StatusActionHandler, '/api/status/<status_id>/action/<id>', endpoint='status_action_self')
