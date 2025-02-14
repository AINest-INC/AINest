# opensea_api.py
import requests

def get_opensea_asset(asset_contract_address, token_id, api_key):
    """Gets information about an asset on OpenSea.

    Args:
        asset_contract_address (str): The contract address of the asset.
        token_id (str): The token ID of the asset.
        api_key (str): Your OpenSea API key.

    Returns:
        dict: The asset information, or None if an error occurred.
    """
    url = f"https://api.opensea.io/api/v1/asset/{asset_contract_address}/{token_id}"
    headers = {
        "X-API-KEY": api_key
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error getting OpenSea asset: {response.status_code} - {response.text}")
        return None

if __name__ == '__main__':
    # Replace with your actual OpenSea API key, contract address, and token ID
    OPENSEA_API_KEY = "YOUR_OPENSEA_API_KEY"
    ASSET_CONTRACT_ADDRESS = "0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d"  # Bored Ape Yacht Club
    TOKEN_ID = "1"

    asset_info = get_opensea_asset(ASSET_CONTRACT_ADDRESS, TOKEN_ID, OPENSEA_API_KEY)

    if asset_info:
        print("OpenSea asset information:")
        import json
        print(json.dumps(asset_info, indent=4))
    else:
        print("Failed to get OpenSea asset information.")
