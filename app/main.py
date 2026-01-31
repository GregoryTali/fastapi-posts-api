import httpx
from fastapi import FastAPI, HTTPException, Query
from typing import Optional

app = FastAPI()

BASE_URL = "https://jsonplaceholder.typicode.com"

@app.get("/posts")
async def list_posts(user_id: Optional[int] = Query(None)):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/posts")
        response.raise_for_status()
        posts = response.json()

    if user_id is not None:
        posts = [post for post in posts if post["userId"] == user_id]
    return posts


@app.get("/post/search")
async def search_posts(q: str = Query(..., min_length=1)):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/posts")
        response.raise_for_status()
        posts = response.json()

    q_lower = q.lower()

    filtered_posts = [
        post for post in posts if q_lower in post["title"].lower() or q_lower in post["body"].lower()
    ]

    return filtered_posts

@app.get("/post/{post_id}")
async def get_post_with_author(post_id: int, user_id):
    async with httpx.AsyncClient() as client:
        post_response = await client.get(f"{BASE_URL}/posts/{post_id}")
        if post_response.status_code == 404:
            raise HTTPException(status_code=404, detail="Post not found")
        post = post_response.json()

        user_response = await client.get(f"{BASE_URL}/users/{user_id}")
        user_response.raise_for_status()
        author = user_response.json()

    return {
        "post": post,
        "author": author
    }