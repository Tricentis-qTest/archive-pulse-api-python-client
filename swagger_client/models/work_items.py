# coding: utf-8

"""
    Pulse API

    Integrate all of your testing apps with Pulse API

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class WorkItems(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, issue_link=None, summary=None, description=None, project_id=None, sprint_id=None, release_id=None, test_cases=None, status=None, user_ids=None, start=None, end=None, component_ids=None, attachment_ids=None, created=None, updated=None, archived=None, order=None, custom=None):
        """
        WorkItems - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'issue_link': 'str',
            'summary': 'str',
            'description': 'str',
            'project_id': 'str',
            'sprint_id': 'str',
            'release_id': 'str',
            'test_cases': 'list[LinkedTestCaseSchema]',
            'status': 'float',
            'user_ids': 'list[str]',
            'start': 'datetime',
            'end': 'datetime',
            'component_ids': 'list[str]',
            'attachment_ids': 'list[str]',
            'created': 'UserDateSchema',
            'updated': 'UserDateSchema',
            'archived': 'bool',
            'order': 'float',
            'custom': 'object'
        }

        self.attribute_map = {
            'id': '_id',
            'issue_link': 'issueLink',
            'summary': 'summary',
            'description': 'description',
            'project_id': 'projectId',
            'sprint_id': 'sprintId',
            'release_id': 'releaseId',
            'test_cases': 'testCases',
            'status': 'status',
            'user_ids': 'userIds',
            'start': 'start',
            'end': 'end',
            'component_ids': 'componentIds',
            'attachment_ids': 'attachmentIds',
            'created': 'created',
            'updated': 'updated',
            'archived': 'archived',
            'order': 'order',
            'custom': 'custom'
        }

        self._id = id
        self._issue_link = issue_link
        self._summary = summary
        self._description = description
        self._project_id = project_id
        self._sprint_id = sprint_id
        self._release_id = release_id
        self._test_cases = test_cases
        self._status = status
        self._user_ids = user_ids
        self._start = start
        self._end = end
        self._component_ids = component_ids
        self._attachment_ids = attachment_ids
        self._created = created
        self._updated = updated
        self._archived = archived
        self._order = order
        self._custom = custom

    @property
    def id(self):
        """
        Gets the id of this WorkItems.
        _id of the WorkItems.

        :return: The id of this WorkItems.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this WorkItems.
        _id of the WorkItems.

        :param id: The id of this WorkItems.
        :type: str
        """

        self._id = id

    @property
    def issue_link(self):
        """
        Gets the issue_link of this WorkItems.
        issueLink of the WorkItems.

        :return: The issue_link of this WorkItems.
        :rtype: str
        """
        return self._issue_link

    @issue_link.setter
    def issue_link(self, issue_link):
        """
        Sets the issue_link of this WorkItems.
        issueLink of the WorkItems.

        :param issue_link: The issue_link of this WorkItems.
        :type: str
        """

        self._issue_link = issue_link

    @property
    def summary(self):
        """
        Gets the summary of this WorkItems.
        summary of the WorkItems.

        :return: The summary of this WorkItems.
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """
        Sets the summary of this WorkItems.
        summary of the WorkItems.

        :param summary: The summary of this WorkItems.
        :type: str
        """
        if summary is None:
            raise ValueError("Invalid value for `summary`, must not be `None`")

        self._summary = summary

    @property
    def description(self):
        """
        Gets the description of this WorkItems.
        description of the WorkItems.

        :return: The description of this WorkItems.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this WorkItems.
        description of the WorkItems.

        :param description: The description of this WorkItems.
        :type: str
        """

        self._description = description

    @property
    def project_id(self):
        """
        Gets the project_id of this WorkItems.
        projectId of the WorkItems.

        :return: The project_id of this WorkItems.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """
        Sets the project_id of this WorkItems.
        projectId of the WorkItems.

        :param project_id: The project_id of this WorkItems.
        :type: str
        """
        if project_id is None:
            raise ValueError("Invalid value for `project_id`, must not be `None`")

        self._project_id = project_id

    @property
    def sprint_id(self):
        """
        Gets the sprint_id of this WorkItems.
        sprintId of the WorkItems.

        :return: The sprint_id of this WorkItems.
        :rtype: str
        """
        return self._sprint_id

    @sprint_id.setter
    def sprint_id(self, sprint_id):
        """
        Sets the sprint_id of this WorkItems.
        sprintId of the WorkItems.

        :param sprint_id: The sprint_id of this WorkItems.
        :type: str
        """

        self._sprint_id = sprint_id

    @property
    def release_id(self):
        """
        Gets the release_id of this WorkItems.
        releaseId of the WorkItems.

        :return: The release_id of this WorkItems.
        :rtype: str
        """
        return self._release_id

    @release_id.setter
    def release_id(self, release_id):
        """
        Sets the release_id of this WorkItems.
        releaseId of the WorkItems.

        :param release_id: The release_id of this WorkItems.
        :type: str
        """

        self._release_id = release_id

    @property
    def test_cases(self):
        """
        Gets the test_cases of this WorkItems.
        testCases of the WorkItems.

        :return: The test_cases of this WorkItems.
        :rtype: list[LinkedTestCaseSchema]
        """
        return self._test_cases

    @test_cases.setter
    def test_cases(self, test_cases):
        """
        Sets the test_cases of this WorkItems.
        testCases of the WorkItems.

        :param test_cases: The test_cases of this WorkItems.
        :type: list[LinkedTestCaseSchema]
        """

        self._test_cases = test_cases

    @property
    def status(self):
        """
        Gets the status of this WorkItems.
        status of the WorkItems.

        :return: The status of this WorkItems.
        :rtype: float
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this WorkItems.
        status of the WorkItems.

        :param status: The status of this WorkItems.
        :type: float
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")

        self._status = status

    @property
    def user_ids(self):
        """
        Gets the user_ids of this WorkItems.
        userIds of the WorkItems.

        :return: The user_ids of this WorkItems.
        :rtype: list[str]
        """
        return self._user_ids

    @user_ids.setter
    def user_ids(self, user_ids):
        """
        Sets the user_ids of this WorkItems.
        userIds of the WorkItems.

        :param user_ids: The user_ids of this WorkItems.
        :type: list[str]
        """
        if user_ids is None:
            raise ValueError("Invalid value for `user_ids`, must not be `None`")

        self._user_ids = user_ids

    @property
    def start(self):
        """
        Gets the start of this WorkItems.
        start of the WorkItems.

        :return: The start of this WorkItems.
        :rtype: datetime
        """
        return self._start

    @start.setter
    def start(self, start):
        """
        Sets the start of this WorkItems.
        start of the WorkItems.

        :param start: The start of this WorkItems.
        :type: datetime
        """

        self._start = start

    @property
    def end(self):
        """
        Gets the end of this WorkItems.
        end of the WorkItems.

        :return: The end of this WorkItems.
        :rtype: datetime
        """
        return self._end

    @end.setter
    def end(self, end):
        """
        Sets the end of this WorkItems.
        end of the WorkItems.

        :param end: The end of this WorkItems.
        :type: datetime
        """

        self._end = end

    @property
    def component_ids(self):
        """
        Gets the component_ids of this WorkItems.
        componentIds of the WorkItems.

        :return: The component_ids of this WorkItems.
        :rtype: list[str]
        """
        return self._component_ids

    @component_ids.setter
    def component_ids(self, component_ids):
        """
        Sets the component_ids of this WorkItems.
        componentIds of the WorkItems.

        :param component_ids: The component_ids of this WorkItems.
        :type: list[str]
        """
        if component_ids is None:
            raise ValueError("Invalid value for `component_ids`, must not be `None`")

        self._component_ids = component_ids

    @property
    def attachment_ids(self):
        """
        Gets the attachment_ids of this WorkItems.
        attachmentIds of the WorkItems.

        :return: The attachment_ids of this WorkItems.
        :rtype: list[str]
        """
        return self._attachment_ids

    @attachment_ids.setter
    def attachment_ids(self, attachment_ids):
        """
        Sets the attachment_ids of this WorkItems.
        attachmentIds of the WorkItems.

        :param attachment_ids: The attachment_ids of this WorkItems.
        :type: list[str]
        """
        if attachment_ids is None:
            raise ValueError("Invalid value for `attachment_ids`, must not be `None`")

        self._attachment_ids = attachment_ids

    @property
    def created(self):
        """
        Gets the created of this WorkItems.

        :return: The created of this WorkItems.
        :rtype: UserDateSchema
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this WorkItems.

        :param created: The created of this WorkItems.
        :type: UserDateSchema
        """

        self._created = created

    @property
    def updated(self):
        """
        Gets the updated of this WorkItems.

        :return: The updated of this WorkItems.
        :rtype: UserDateSchema
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """
        Sets the updated of this WorkItems.

        :param updated: The updated of this WorkItems.
        :type: UserDateSchema
        """

        self._updated = updated

    @property
    def archived(self):
        """
        Gets the archived of this WorkItems.
        archived of the WorkItems.

        :return: The archived of this WorkItems.
        :rtype: bool
        """
        return self._archived

    @archived.setter
    def archived(self, archived):
        """
        Sets the archived of this WorkItems.
        archived of the WorkItems.

        :param archived: The archived of this WorkItems.
        :type: bool
        """

        self._archived = archived

    @property
    def order(self):
        """
        Gets the order of this WorkItems.
        order of the WorkItems.

        :return: The order of this WorkItems.
        :rtype: float
        """
        return self._order

    @order.setter
    def order(self, order):
        """
        Sets the order of this WorkItems.
        order of the WorkItems.

        :param order: The order of this WorkItems.
        :type: float
        """

        self._order = order

    @property
    def custom(self):
        """
        Gets the custom of this WorkItems.
        custom of the WorkItems.

        :return: The custom of this WorkItems.
        :rtype: object
        """
        return self._custom

    @custom.setter
    def custom(self, custom):
        """
        Sets the custom of this WorkItems.
        custom of the WorkItems.

        :param custom: The custom of this WorkItems.
        :type: object
        """

        self._custom = custom

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other