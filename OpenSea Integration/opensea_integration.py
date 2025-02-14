# opensea_integration.py
from opensea_api import get_opensea_asset

def integrate_opensea_with_ainest(asset_contract_address, token_id, api_key):
    """Integrates OpenSea asset information retrieval with AiNest.

    Args:
        asset_contract_address (str): The contract address of the asset.
        token_id (str): The token ID of the asset.
        api_key (str): Your OpenSea API key.

    Returns:
        dict: The asset information, or None if an error occurred.
    """
    asset_info = get_opensea_asset(asset_contract_address, token_id, api_key)
    if asset_info:
        print("OpenSea asset information retrieved successfully via AiNest integration.")
        return asset_info
    else:
        print("Failed to retrieve OpenSea asset information via AiNest integration.")
        return None

if __name__ == '__main__':
    # Replace with your actual OpenSea API key, contract address, and token ID
    OPENSEA_API_KEY = "YOUR_OPENSEA_API_KEY"
    ASSET_CONTRACT_ADDRESS = "0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d"  # Bored Ape Yacht Club
    TOKEN_ID = "1"

    asset_data = integrate_opensea_with_ainest(ASSET_CONTRACT_ADDRESS, TOKEN_ID, OPENSEA_API_KEY)

    if asset_data:
        print(asset_data)
