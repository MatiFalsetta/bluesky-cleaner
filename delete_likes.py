#!/usr/bin/env python3
"""
delete_likes.py - Remove all likes from your Bluesky account

This script uses the official Bluesky API (ATProto) to:
1. Get all posts that you have liked
2. Delete each like individually
3. Show real-time progress

Requires: pip install atproto
"""

import time
import sys
from typing import List, Dict, Any
from atproto import Client, models

def setup_client() -> Client:
    """
    Configure and authenticate the Bluesky client
    """
    print("🔐 Setting up Bluesky connection...")
    
    # Request credentials
    handle = input("Enter your Bluesky handle (e.g., user.bsky.social): ").strip()
    password = input("Enter your password: ").strip()
    
    try:
        client = Client()
        client.login(handle, password)
        print(f"✅ Successfully authenticated as @{handle}")
        return client
    except Exception as e:
        print(f"❌ Authentication error: {e}")
        print("Please verify your handle and password.")
        sys.exit(1)

def get_all_likes(client: Client) -> List[Dict[str, Any]]:
    """
    Get all like records from the user (not the posts, but the like records)
    """
    print("\n📋 Getting like records...")
    
    all_likes = []
    cursor = None
    
    try:
        while True:
            # Use listRecords to get like records directly
            params = {
                'repo': client.me.did,
                'collection': 'app.bsky.feed.like',  # Like collection
                'limit': 100  # Maximum allowed by the API
            }
            
            if cursor:
                params['cursor'] = cursor
            
            response = client.com.atproto.repo.list_records(params=params)
            
            if not response.records:
                break
                
            all_likes.extend(response.records)
            print(f"📦 Retrieved {len(all_likes)} like records so far...")
            
            # Check if there are more pages
            if hasattr(response, 'cursor') and response.cursor:
                cursor = response.cursor
            else:
                break
                
            # Small pause to avoid overloading the API
            time.sleep(0.1)
            
    except Exception as e:
        print(f"❌ Error getting like records: {e}")
        return all_likes
    
    print(f"✅ Total like records found: {len(all_likes)}")
    return all_likes

def delete_likes(client: Client, likes: List[Dict[str, Any]]) -> None:
    """
    Delete all like records from the list
    """
    if not likes:
        print("ℹ️  No likes to delete.")
        return
    
    print(f"\n🗑️  Starting deletion of {len(likes)} like records...")
    
    # Confirm action
    confirmation = input(f"⚠️  Are you sure you want to delete {len(likes)} likes? (y/N): ").strip().lower()
    if confirmation not in ['y', 'yes', 'si', 's', 'sí']:
        print("❌ Cancelled by user.")
        return
    
    deleted = 0
    errors = 0
    
    for i, like_record in enumerate(likes, 1):
        try:
            # Extract rkey from the like record URI
            rkey = like_record.uri.split('/')[-1]
            
            # Use correct syntax for delete_record
            from atproto import models
            
            delete_data = models.ComAtprotoRepoDeleteRecord.Data(
                repo=client.me.did,
                collection='app.bsky.feed.like',
                rkey=rkey
            )
            
            client.com.atproto.repo.delete_record(data=delete_data)
            deleted += 1
            
            # Show progress
            if i % 10 == 0 or i == len(likes):
                percentage = (i / len(likes)) * 100
                print(f"🔄 Progress: {deleted} deleted, {errors} errors ({percentage:.1f}%)")
            
            # Pause to avoid rate limiting
            time.sleep(0.2)
            
        except Exception as e:
            errors += 1
            print(f"⚠️  Error deleting like #{i}: {e}")
            
            # If there are many consecutive errors, ask whether to continue
            if errors > 5 and (errors / i) > 0.1:  # More than 10% errors
                continue_prompt = input("❓ Many errors occurred. Continue? (y/N): ").strip().lower()
                if continue_prompt not in ['y', 'yes', 'si', 's', 'sí']:
                    break
    
    print(f"\n✅ Process completed:")
    print(f"   ✓ Likes deleted: {deleted}")
    print(f"   ⚠ Errors: {errors}")

def show_preview_statistics(likes: List[Dict[str, Any]]) -> None:
    """
    Show statistics of like records before deletion
    """
    if not likes:
        return
    
    print(f"\n📊 Statistics of your likes:")
    print(f"   • Total like records: {len(likes)}")
    
    # Count likes by approximate date (using record information)
    recent_dates = 0
    for like in likes:
        try:
            # More recent records usually have higher rkeys
            rkey = like.uri.split('/')[-1]
            if rkey and len(rkey) > 10:  # Typical rkey format
                recent_dates += 1
        except:
            pass
    
    print(f"   • Valid records found: {recent_dates}")
    print(f"   • Note: Like records will be deleted, not the original posts")

def main():
    """
    Main program function
    """
    print("🦋 BLUESKY LIKE REMOVER")
    print("=" * 40)
    print("This script will remove ALL your likes from Bluesky.")
    print("⚠️  This action is NOT reversible.")
    print("=" * 40)
    
    try:
        # Setup client
        client = setup_client()
        
        # Get all likes
        likes = get_all_likes(client)
        
        if not likes:
            print("\n🎉 You have no likes to delete. Your account is already clean!")
            return
        
        # Show statistics
        show_preview_statistics(likes)
        
        # Delete likes
        delete_likes(client, likes)
        
        print("\n🎉 Process completed! All your likes have been processed.")
        
    except KeyboardInterrupt:
        print("\n\n⏹️  Process interrupted by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()