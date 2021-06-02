import secrets

class BaseHashGenerator(object):
    """
    All generators should extend this class overriding `.hash()` method.
    """

    def hash(self):
        raise NotImplementedError()


class ClientSecretGenerator(BaseHashGenerator):
    """ Generate a client_id for Basic Authentication scheme without colon char
        as in http://tools.ietf.org/html/rfc2617#section-2"""

    def hash(self):
        length = 40
        # chars = UNICODE_ASCII_CHARACTER_SET
        return secrets.token_urlsafe(length)


def generate_client_secret():
    """
    Generate a suitable client secret
    """
    client_secret_generator = ClientSecretGenerator()
    return client_secret_generator.hash()

# print(generate_client_secret())