from datetime import datetime

from django.db.models import Count, F, Q
from django.test import TestCase
from django.utils import timezone

from activity.models import Activity
from club.models import Club, ClubMember, ClubPostReply
from member.models import Member
from pay.models import Pay
from teenplay_server.category import Category


class ClubTestCase(TestCase):
    # club_id = 4
    # columns = [
    #     'id',
    #     'club_name',
    #     'club_intro',
    #     'club_info',
    #     'owner_id',
    #     'owner_name',
    #     'owner_email',
    #     'owner_phone',
    #     'club_profile_path',
    #     'club_banner_path',
    #     'club_member_count',
    #     'club_activity_count'
    # ]

    # club = Club.objects.filter(id=club_id) \
    #     .annotate(
    #     owner_id=F('member__id'),
    #     owner_name=F('member__member_nickname'),
    #     owner_email=F('member__member_email'),
    #     owner_phone=F('member__member_phone'),
    #     club_member_count=Count('clubmember', filter=Q(clubmember__status=1)),
    #     club_activity_count=Count('activity')).values(*columns)

    # print(club)

    member = Member.objects.get(id=8)
    print(member)
    # club_member = ClubMember.objects.filter(member=member)
    #
    # if club_member.exists():
    #     if club_member.first().status:
    #         print(club_member.first().status)
    # club = Club.objects.get(id=8)
    # pay = Pay.objects.get(id=17)
    # category = Category.objects.get(id=1)
    # columns = {
    #     'activity_title': '헬스클럽 23년 17회차 정기 활동',
    #     'activity_content': '<p>테스트입니다.</p><p><br></p><p><img style=\"width: 821.394px;\" src="activity/2024/03/05/healthclub_activity_img_fuVgL8H.jpg" data-filename=\"healthclub_activity_img.jpg\"></p><p><br></p><p><font color=\"#000000\" style=\"background-color: rgb(255, 255, 0);\">테스트입니다.</font></p><p>테스트입니다.</p><p><br></p>',
    #     'recruit_start': datetime(2023, 1, 10, 6, 0, 0),
    #     'recruit_end': datetime(2023, 1, 19, 20, 0, 0),
    #     'activity_intro': '안녕하세요. 그럼 운동하러 갑시다.',
    #     'activity_address_detail': '주차 공간 없습니다.',
    #     'thumbnail_path': 'activity/2024/03/05/healthclub_activity_img.jpg',
    #     'banner_path': 'activity/2024/03/05/healthclub_activity_banner_img.jpg',
    #     'activity_start': datetime(2023, 1, 20, 6, 0, 0),
    #     'activity_end': datetime(2023, 1, 20, 20, 0, 0),
    #     'category': category,
    #     'club': club,
    #     'pay': pay
    # }
    #
    # Activity.objects.create(**columns)

    # club = Club.objects.get(id=8)
    # columns = [
    #     'id', 'activity_title', 'thumbnail_path', 'activity_start',
    # ]

    # ongoing_activities = club.activity_set.filter(activity_end__gt=timezone.now(), status=1).values(*columns)\
    #     .annotate(participant_count=Count('activitymember', filter=Q(activitymember__status=1)))

    # ongoing_activities = Activity.objects.filter(club=club, activity_end__gt=timezone.now(), status=1)\
    #     .values('id', 'activity_title', 'thumbnail_path', 'activity_start')\
    #     .annotate(participant_count=Count('activitymember', filter=Q(activitymember__status=1)))
    #
    # finished_activities = Activity.objects.filter(club=club, activity_end__lte=timezone.now(), status=1) \
    #     .annotate(participant_count=Count('activitymember', filter=Q(activitymember__status=1))) \
    #     .values('id', 'activity_title', 'thumbnail_path', 'activity_start', 'participant_count') \
    #     .order_by('-id')

    # print(ongoing_activities)
    # print('=' * 20)
    # print(finished_activities)

    # ClubPostReply.objects.create(reply_content='모임 홍보글 댓글 테스트 내용8', club_post_id=1, member_id=2)
    club_id = 2
    view = 'activity'
    # 화면에서 필요한 컬럼들을 가독성을 높이기 위해 list형식으로 담아 사용
    columns = [
        'id',
        'club_name',
        'club_intro',
        'club_info',
        'club_profile_path',
        'club_banner_path',
        'owner_id',
        'owner_name',
        'owner_email',
        'owner_phone',
    ]

    # club_id를 통해 모임을 select 한 후 .annotate().values()를 사용해서 모임장의 정보를 각 쿼리셋 객체의 필드에 추가하고
    # 모임장의 정보는 정참조를 통해, 모임 구성원의 수는 역참조를 통해 club_member의 status가 1인 것만 카운트하여 필드에 추가
    club_list = Club.objects.filter(id=club_id) \
        .annotate(
        owner_id=F('member__id'),
        owner_name=F('member__member_nickname'),
        owner_email=F('member__member_email'),
        owner_phone=F('member__member_phone')
    ).values(*columns).annotate(
        club_member_count=Count('clubmember', filter=Q(clubmember__status=1)))
    # 위 코드에 이어서 사용할 경우 중복이 발생하여 집계가 제대로 되지 않기 때문에 모임의 활동수는 따로 집계하도록 구성
    # .distinct()를 사용하지 않은 이유는 group_by가 된 경우 중복 제거가 제대로 되지 않기 때문
    club_activity_count = Club.objects.filter(id=club_id).values('id') \
        .annotate(club_activity_count=Count('activity')).first()

    for club in club_list:
        club['club_activity_count'] = club_activity_count.get('club_activity_count')
        print(club)
