from fastapi import status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session

from app.models import Like, Dislike, Post
from app.schema import LikeSchema, DislikeSchema
from app.database import get_db
from app.oauth2 import get_current_user


router = APIRouter(
    prefix="/vote",
    tags=["Vote"]
)


@router.post("/like", status_code=status.HTTP_201_CREATED)
def like(vote: LikeSchema, db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):

    like_query = db.query(Like).filter(Like.post_id == vote.post_id, Like.user_id == current_user.id)
    found_like = like_query.first()

    # Delete like if post was already liked
    if found_like:
        like_query.delete(synchronize_session=False)
        db.commit()

        return {"message": "Like deleted"}

    else:
        new_like = Like(post_id=vote.post_id, user_id=current_user.id)
        like_self = db.query(Post).filter(Post.id == new_like.post_id, Post.owner_id == new_like.user_id).first()

        # Forbid users to like their own posts
        if like_self:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden to vote for one's post")

        db.add(new_like)
        db.commit()

        return {"message": "Added like"}


@router.post("/dislike", status_code=status.HTTP_201_CREATED)
def dislike(vote: DislikeSchema, db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):

    dislike_query = db.query(Dislike).filter(Dislike.post_id == vote.post_id, Dislike.user_id == current_user.id)
    found_dislike = dislike_query.first()

    # Delete dislike if post was already liked
    if found_dislike:
        dislike_query.delete(synchronize_session=False)
        db.commit()

        return {"message": "Dislike deleted"}

    else:
        new_dislike = Dislike(post_id=vote.post_id, user_id=current_user.id)

        dislike_self = db.query(Post).filter(Post.id == new_dislike.post_id, Post.owner_id == new_dislike.user_id).first()

        # Forbid users to dislike their own posts
        if dislike_self:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden to vote for one's post")

        db.add(new_dislike)
        db.commit()

        return {"message": "Added dislike"}
