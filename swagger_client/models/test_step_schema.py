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


class TestStepSchema(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, description=None, expected_result=None, attachment_ids=None):
        """
        TestStepSchema - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'description': 'str',
            'expected_result': 'str',
            'attachment_ids': 'list[str]'
        }

        self.attribute_map = {
            'id': '_id',
            'description': 'description',
            'expected_result': 'expectedResult',
            'attachment_ids': 'attachmentIds'
        }

        self._id = id
        self._description = description
        self._expected_result = expected_result
        self._attachment_ids = attachment_ids

    @property
    def id(self):
        """
        Gets the id of this TestStepSchema.
        _id of the TestStepSchema.

        :return: The id of this TestStepSchema.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this TestStepSchema.
        _id of the TestStepSchema.

        :param id: The id of this TestStepSchema.
        :type: str
        """

        self._id = id

    @property
    def description(self):
        """
        Gets the description of this TestStepSchema.
        description of the TestStepSchema.

        :return: The description of this TestStepSchema.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this TestStepSchema.
        description of the TestStepSchema.

        :param description: The description of this TestStepSchema.
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")

        self._description = description

    @property
    def expected_result(self):
        """
        Gets the expected_result of this TestStepSchema.
        expectedResult of the TestStepSchema.

        :return: The expected_result of this TestStepSchema.
        :rtype: str
        """
        return self._expected_result

    @expected_result.setter
    def expected_result(self, expected_result):
        """
        Sets the expected_result of this TestStepSchema.
        expectedResult of the TestStepSchema.

        :param expected_result: The expected_result of this TestStepSchema.
        :type: str
        """

        self._expected_result = expected_result

    @property
    def attachment_ids(self):
        """
        Gets the attachment_ids of this TestStepSchema.
        attachmentIds of the TestStepSchema.

        :return: The attachment_ids of this TestStepSchema.
        :rtype: list[str]
        """
        return self._attachment_ids

    @attachment_ids.setter
    def attachment_ids(self, attachment_ids):
        """
        Sets the attachment_ids of this TestStepSchema.
        attachmentIds of the TestStepSchema.

        :param attachment_ids: The attachment_ids of this TestStepSchema.
        :type: list[str]
        """

        self._attachment_ids = attachment_ids

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