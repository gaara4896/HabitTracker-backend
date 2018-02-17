# HabitTracker-backend

## Http response code

### Success

	status code 200

### Failure

1. Failure

		status code 400

1. Token failure

		status code 401

1. Not found

		status code 404

1. Server error

		status code 500

## Endpoint

Path to the endpoint should be as below

```
protocol://domain:port/apis
```

Example

```
https://habitbackend-heroku.herokuapp.com/apis
```

### Authentication

Prefix

```
/auth
```

#### Register

```
POST /register
```

Parameter

location: Form

```
username = <username>
password = <password>
email = <email>
nickname = <nickname>
```

Response

1. Success

	status code: 200

	```
	{
		"success": {
			"message": "<Success Message>"
		}
	}
	```

1. Failure

	- Cause: Username used

		status code: 400

		```
		{
			"error": {
				"message": "<Error Message>"
			}
		}
		```

#### Login

```
POST /login
```

Parameter

location: Form

```
username = <username>
password = <password>
```

Response

1. Success

	status code: 200

	```
	{
		"success": {
			"access_token": <access_token>,
			"refresh_token": <refresh_token>
		}
	}
	```

1. Failure

	- Cause: Wrong password

		status code: 400

		```
		{
			"error": {
				"message": "<Error Message>"
			}
		}
		```
	- Cause: User not exist

		status code: 404

		```
		{
			"error": {
				"message": "<Error Message>"
			}
		}
		```

#### Fresh Login

```
POST /login
```

Parameter

location: Form

```
username = <username>
password = <password>
```

Response

1. Success

	status code: 200

	```
	{
		"success": {
			"access_token": <access_token>
		}
	}
	```

1. Failure

	- Cause: Wrong password

		status code: 400

		```
		{
			"error": {
				"message": "<Error Message>"
			}
		}
		```
	- Cause: User not exist

		status code: 404

		```
		{
			"error": {
				"message": "<Error Message>"
			}
		}
		```

#### Refresh

```
POST /refresh
```

Header

```
Authorization: Bearer <refresh_token>
```

Response

1. Success

	status code: 200

	```
	{
		"success": {
			"access_token": <access_token>
		}
	}
	```

1. Failure

	- Cause: No token presented, Invalid refresh token or expired refresh token

		status code: 401

		```
		{
			"error": {
				"message": "<Error Message>"
			}
		}
		```

#### Change Password

```
POST /change-password
```

Header

```
Authorization: Bearer <fresh_access_token>
```

Parameter

```
password_new = <password_new>
```

Response

1. Success

	status code: 200

	```
	{
		"success": {
			"message": <Success Message>
		}
	}
	```

1. Failure

	- Cause: No token presented, Invalid access token, expired access token and non fresh access token

		status code: 401

		```
		{
			"error": {
				"message": "<Error Message>"
			}
		}
		```

	- Cause: No user found

		status code: 404

		```
		{
			"error": {
				"message": "<Error Message>"
			}
		}
		```

#### Reset Password

```
POST /reset-password
```

Parameter

```
username = <username>
```

Response

1. Success

	status code: 200

	```
	{
		"success": {
			"message": <Success Message>
		}
	}
	```

1. Failure

	- Cause: No user found

		status code: 404

		```
		{
			"error": {
				"message": "<Error Message>"
			}
		}
		```
