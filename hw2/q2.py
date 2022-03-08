from q2_atm import ATM, ServerResponse


def extract_PIN(encrypted_PIN) -> int:
    """Extracts the original PIN string from an encrypted PIN."""
    instance = ATM()
    pin = 0
    for i in range(10000):
        if instance.encrypt_PIN(i) == encrypted_PIN:
            return i
    return 0


def extract_credit_card(encrypted_credit_card) -> int:
    """Extracts a credit card number string from its ciphertext."""
    instance = ATM()
    exp = instance.rsa_card.e
    return round(encrypted_credit_card**(1/exp))


def forge_signature():
    """Forge a server response that passes verification."""
    # Return a ServerResponse instance.
    return ServerResponse(1, 1)
