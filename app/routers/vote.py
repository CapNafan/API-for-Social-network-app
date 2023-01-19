from fastapi import status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session

from app.models import Like, Dislike
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

    if found_like:
        like_query.delete(synchronize_session=False)
        db.commit()

        return {"message": "Like deleted"}

    else:
        new_like = Like(post_id=vote.post_id, user_id=current_user.id)
        db.add(new_like)
        db.commit()

        return {"message": "Added like"}


@router.post("/dislike", status_code=status.HTTP_201_CREATED)
def dislike(vote: DislikeSchema, db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):

    dislike_query = db.query(Dislike).filter(Dislike.post_id == vote.post_id, Dislike.user_id == current_user.id)
    found_dislike = dislike_query.first()

    if found_dislike:
        dislike_query.delete(synchronize_session=False)
        db.commit()

        return {"message": "Dislike deleted"}

    else:
        new_dislike = Dislike(post_id=vote.post_id, user_id=current_user.id)
        db.add(new_dislike)
        db.commit()

        return {"message": "Added dislike"}
