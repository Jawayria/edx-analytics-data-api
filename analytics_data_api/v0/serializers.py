from rest_framework import serializers
from analytics_data_api.v0.models import CourseActivityByWeek, ProblemResponseAnswerDistribution


class CourseActivityByWeekSerializer(serializers.ModelSerializer):
    """
    Representation of CourseActivityByWeek that excludes the id field.

    This table is managed by the data pipeline, and records can be removed and added at any time. The id for a
    particular record is likely to change unexpectedly so we avoid exposing it.
    """
    course_id = serializers.SerializerMethodField('get_course_id')

    def get_course_id(self, obj):
        return obj.course.course_id

    class Meta(object):
        model = CourseActivityByWeek
        fields = ('interval_start', 'interval_end', 'activity_type', 'count', 'course_id')


class ProblemResponseAnswerDistributionSerializer(serializers.ModelSerializer):
    """
    Representation of the Answer Distribution table, without id.

    This table is managed by the data pipeline, and records can be removed and added at any time. The id for a
    particular record is likely to change unexpectedly so we avoid exposing it.
    """

    class Meta(object):
        model = ProblemResponseAnswerDistribution
        fields = (
            'course_id',
            'module_id',
            'part_id',
            'correct',
            'count',
            'value_id',
            'answer_value_text',
            'answer_value_numeric',
            'variant',
            'created'
        )