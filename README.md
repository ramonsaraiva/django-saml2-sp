# django-saml2-sp

A Django SAML2 SSO Service Provider PoC.  
Integrates with this [Django SAML2 Identity Provider PoC](https://github.com/ramonsaraiva/django-saml2-idp) _(IDP metadata XML file built-in)_.  
Uses [djangosaml2](https://github.com/knaperek/djangosaml2) as its skeleton.

## Running

To run the SP side of the SAML2 SSO, clone it and run `docker-compose up`.  
Make sure your host `9000` port is available.

Access http://localhost:9000/ to see the index page, it will show which user you are authenticated with (`AnonymousUser` if unauthenticated) and the possible actions you can take, either `login` or `logout`.

## Authentication flows

### IdP initiated flow
1. Clone the [Django SAML2 Identity Provider PoC](https://github.com/ramonsaraiva/django-saml2-idp)
2. Spin it up with `docker-compose up`
3. Go to IdP url http://localhost:8000/
4. Click on the `login` button
5. Login on the IdP
6. You're logged in in the IdP.
7. Go to the SP url http://localhost:9000/
8. Click on the `login` button
9. You'll be redirected to the IdP and redirected back to the SP, authenticated.

### SP initiated flow
3. Go to the SP url http://localhost:9000/
4. Click on the `login` button
5. You'll be redirected to the IdP login flow
6. Login on the IdP
7. You'll be redirected to the SP, authenticated.
