from django.db import models
from member.models import Member
from search.models import Like
from teenplay_server.models import Period, Category


class Wishlist(Period):
    member = models.ForeignKey(Member, null=False, blank=False, on_delete=models.PROTECT)
    # 0: 비공개, 1: 공개
    is_private = models.BooleanField(default=1, null=False, blank=False)
    wishlist_content = models.TextField(null=False, blank=False)
    category = models.ForeignKey(Category, null=False, blank=False, on_delete=models.PROTECT)
    # 0: 삭제, 1: 게시중
    status = models.BooleanField(default=1, null=False, blank=False)

    class Meta:
        db_table = 'tbl_wishlist'


class WishListLike(Like):
    wishlist = models.ForeignKey(Wishlist, null=False, blank=False, on_delete=models.PROTECT)
    member = models.ForeignKey(Member, null=False, blank=False, on_delete=models.PROTECT)
    # 0: 삭제, 1: 좋아요
    status = models.BooleanField(default=1, null=False, blank=False)

    class Meta:
        db_table = 'tbl_wishlist_like'


class WishlistReply(Period):
    wishlist = models.ForeignKey(Wishlist, null=False, blank=False, on_delete=models.PROTECT)
    member = models.ForeignKey(Member, null=False, blank=False, on_delete=models.PROTECT)
    reply_content = models.TextField(null=False, blank=False)
    # 0: 삭제, 1: 게시중
    status = models.BooleanField(default=1, null=False, blank=False)

    class Meta:
        db_table = 'tbl_wishlist_reply'


class WishlistTag(Period):
    tag_name = models.TextField(null=False, blank=False)
    wishlist = models.ForeignKey(Wishlist, null=False, blank=False, on_delete=models.PROTECT)
    # 0: 삭제
    status = models.BooleanField(default=1, null=False, blank=False)

    class Meta:
        db_table = 'tbl_wishlist_tag'
