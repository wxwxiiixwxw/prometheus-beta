import requests
from typing import Dict, Any, Optional

def send_http_get_request(url: str, 
                           headers: Optional[Dict[str, str]] = None, 
                           params: Optional[Dict[str, Any]] = None, 
                           timeout: int = 10) -> Dict[str, Any]:
    """
    Send an HTTP GET request to the specified URL.
    
    Args:
        url (str): The URL to send the GET request to
        headers (dict, optional): Optional headers to include in the request
        params (dict, optional): Optional query parameters to include
        timeout (int, optional): Request timeout in seconds. Defaults to 10.
    
    Returns:
        dict: A dictionary containing response details
    
    Raises:
        ValueError: If URL is empty or invalid
        requests.RequestException: For network-related errors
    """
    # Validate URL
    if not url or not isinstance(url, str):
        raise ValueError("A valid URL must be provided")
    
    try:
        # Send GET request
        response = requests.get(
            url, 
            headers=headers, 
            params=params, 
            timeout=timeout
        )
        
        # Raise an exception for HTTP errors
        response.raise_for_status()
        
        return {
            "status_code": response.status_code,
            "headers": dict(response.headers),
            "content": response.text,
            "json": response.json() if response.headers.get('content-type', '').startswith('application/json') else None
        }
    
    except requests.exceptions.HTTPError as he:
        raise
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"HTTP GET request failed: {str(e)}")