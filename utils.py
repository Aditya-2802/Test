from datetime import datetime
from dateutil import parser

def parse_event(event_type, payload):
    if event_type == 'push':
        head_commit = payload.get("head_commit", {})
        ref = payload.get("ref", "")
        to_branch = ref.split("/")[-1] if ref else None
        commit_timestamp = head_commit.get("timestamp")

        return {
            "request_id": head_commit.get("id"),
            "author": head_commit.get("author", {}).get("name"),
            "action": event_type,  # ✅ Now dynamic, based on the actual event
            "from_branch": None,
            "to_branch": to_branch,
            "timestamp": (
                parser.parse(commit_timestamp)
                if commit_timestamp else datetime.utcnow()
            )
        }

    # Handle other types later like 'pull_request', etc.
    return None


# def parse_event(payload):
    head_commit = payload.get("head_commit", {})
    ref = payload.get("ref", "")
    to_branch = ref.split("/")[-1] if ref else None
    commit_timestamp = head_commit.get("timestamp")

    return {
        "request_id": head_commit.get("id"),
        "author": head_commit.get("author", {}).get("name"),
        "action": "push",
        "from_branch": None,
        "to_branch": to_branch,
        "timestamp": (
            parser.parse(commit_timestamp)
            if commit_timestamp else datetime.utcnow()
        )
    }
