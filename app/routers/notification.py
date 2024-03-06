from fastapi import APIRouter, HTTPException, status, Depends
from pydantic import BaseModel
from models.notification import Notification
from internal.database import query, execute
from internal.auth import get_decoded_token

router = APIRouter()

# Affiche toutes les notifications
@router.get("/notifications")
async def get_notifications(connected_user_email: str = Depends(get_decoded_token)):
    notifications = query("SELECT * FROM notification")
    return {"notifications": notifications}

# Crée une notification
@router.post("/notification/", response_model=Notification, status_code=status.HTTP_201_CREATED)
async def create_notification(notification: Notification, connected_user_email: str = Depends(get_decoded_token)):
    req = f'INSERT INTO notification (planning_id, user_id, detail, title) VALUES ("{notification.planning_id}", "{notification.user_id}", "{notification.detail}", "{notification.title}")'
    execute(req)
    return {"message": "Notification created"}

# Affiche une notification
@router.get("/notification/{notification_id}")
async def get_notification(notification_id: int, connected_user_email: str = Depends(get_decoded_token)):
    notification = query(f"SELECT * FROM notification WHERE id={notification_id}")
    if len(notification) == 0:
        raise HTTPException(status_code=404, detail="Notification not found")
    return {"notification": notification}

# Met à jour une notification
@router.put("/notification/{notification_id}")
async def update_notification(notification_id: int, notification: Notification, connected_user_email: str = Depends(get_decoded_token)):
    check_notification = query(f"SELECT * FROM notification WHERE id={notification_id}")
    if len(check_notification) == 0:
        raise HTTPException(status_code=404, detail="Notification not found")
    req = f'UPDATE notification SET planning_id="{notification.planning_id}", user_id="{notification.user_id}", detail="{notification.detail}", title="{notification.title}" WHERE id={notification_id}'
    execute(req)
    return {"message": "Notification updated"}

# Supprime une notification
@router.delete("/notification/{notification_id}")
async def delete_notification(notification_id: int, connected_user_email: str = Depends(get_decoded_token)):
    check_notification = query(f"SELECT * FROM notification WHERE id={notification_id}")
    if len(check_notification) == 0:
        raise HTTPException(status_code=404, detail="Notification not found")
    req = f'DELETE FROM notification WHERE id={notification_id}'
    execute(req)
    return {"message": "Notification deleted"}
