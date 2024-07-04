import qrcode
import urllib.parse

def generate_wifi_qr(ssid: str, password: str) -> None:
    """
    Generates a QR code for a WiFi connection.

    Args:
        ssid (str): The SSID of the WiFi network.
        password (str): The password of the WiFi network.

    Returns:
        None
    """
    # Escape the SSID and password to handle special characters
    ssid_escaped = urllib.parse.quote(ssid, safe='')
    password_escaped = urllib.parse.quote(password, safe='')

    wifi_config = f"WIFI:S:{ssid_escaped};T:WPA;P:{password_escaped};;"
    print(f"QR Code content: {wifi_config}")  # Print the content for verification
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(wifi_config)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    img.save(f"{ssid}_wifi_qr.png")
    print(f"QR code for WiFi '{ssid}' generated and saved as {ssid}_wifi_qr.png")

def main():
    ssid = input("Enter WiFi SSID: ")
    password = input("Enter WiFi password: ")

    generate_wifi_qr(ssid, password)

if __name__ == "__main__":
    main()
