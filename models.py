from pydantic import BaseModel

class User(BaseModel):
    id: int
    username: str
    email: str

class Artist(BaseModel):
    id: int
    name: str

class Album(BaseModel):
    id: int
    title: str
    artist_id: int

class Track(BaseModel):
    id: int
    title: str
    album_id: int

class Playlist(BaseModel):
    id: int
    name: str
    user_id: int