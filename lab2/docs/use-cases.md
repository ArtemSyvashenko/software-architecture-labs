# Use Cases — Streaming Service

## 1. Register user
Actor: Guest user  
Preconditions: User does not have an existing account with the same email.  
Main scenario:
1. User sends email and password.
2. System validates email and password.
3. System creates user account.
4. System returns created user data.
Alternative scenarios:
- Invalid email: system returns 400.
- Email already exists: system returns 409.

## 2. Login user
Actor: Registered user  
Preconditions: User account exists.  
Main scenario:
1. User sends email and password.
2. System verifies credentials.
3. System returns JWT token.
Alternative scenarios:
- Invalid credentials: system returns 401.

## 3. Create movie
Actor: Administrator  
Preconditions: User is authenticated.  
Main scenario:
1. User sends movie title, genre and release year.
2. System validates movie data.
3. System creates movie.
Alternative scenarios:
- Empty title: system returns 400.
- Duplicate title: system returns 409.

## 4. Browse movies
Actor: Authenticated user  
Preconditions: User is authenticated.  
Main scenario:
1. User requests movie list.
2. System returns available movies.
Alternative scenarios:
- Unauthorized request: system returns 401.

## 5. Create subscription
Actor: Authenticated user  
Preconditions: User is authenticated.  
Main scenario:
1. User selects subscription plan.
2. System validates plan and period.
3. System creates active subscription.
Alternative scenarios:
- Invalid plan: system returns 400.
- User already has active subscription: system returns 409.

## 6. Create payment
Actor: Authenticated user  
Preconditions: User is authenticated and has a valid subscription.  
Main scenario:
1. User sends payment amount.
2. System validates amount.
3. System creates payment record.
Alternative scenarios:
- Negative amount: system returns 400.
