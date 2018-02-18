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

location: Form

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

location: Form

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

### Habit

Prefix

```
/habits
```

#### Get All Habit

```
GET /
```

Header

```
Authorization: Bearer <access_token>
```

Response

1. Success

	status code: 200

	```
	{
		"success": {
			"result": [
				{
					"active": "<active>",
					"id": "<id>",
					"name": "<name>",
					"period": "<period>",
					"target_seconds": "<target_seconds>"
				},
				...
			]
		}
	}
	```

1. Failure

	- Cause: No access token presented, invalid access token, expired access token

		status code: 401

		```
		{
			"error": {
				"message": "<Error Message>"
			}
		}
		```

#### Get Habit

```
GET /<int:id>
```

Header

```
Authorization: Bearer <access_token>
```

Response

1. Success

	status code: 200

	```
	{
		"success": {
			"result": {
				"active": "<active>",
				"id": "<id>",
				"name": "<name>",
				"period": "<period>",
				"target_seconds": "<target_seconds>"
			}
		}
	}
	```

1. Failure

	- Cause: No access token presented, invalid access token, expired access token

		status code: 401

		```
		{
			"error": {
				"message": "<Error Message>"
			}
		}
		```

	- Cause: No habit found

		status cod: 404

		```
		{
			"error": {
				"message": "<Error Message>"
			}
		}
		```

#### Add Habit

```
POST /add
```

Header

```
Authorization: Bearer <access_token>
```

Parameter

location: Form

```
name = <name>
period = <(daily, weekly, monthly, yearly)>
target_seconds = <target_seconds>
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

	- Cause: No access token presented, invalid access token, expired access token

		status code: 401

		```
		{
			"error": {
				"message": "<Error Message>"
			}
		}
		```

#### Update Habit

```
PUT /<int:id>
```

Header

```
Authorization: Bearer <access_token>
```

Parameter

location: Form

```
habit_id = <habit_id>
name = <name> *OPTIONAL*
period = <(daily, weekly, monthly, yearly)> *OPTIONAL*
target_seconds = <target_seconds> *OPTIONAL*
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

	- Cause: No access token presented, invalid access token, expired access token

		status code: 401

		```
		{
			"error": {
				"message": "<Error Message>"
			}
		}
		```

	- Cause: No habit found

		status cod: 404

		```
		{
			"error": {
				"message": "<Error Message>"
			}
		}
		```

#### Activate Habit

```
POST /<int:id>
```

Header

```
Authorization: Bearer <access_token>
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

	- Cause: No access token presented, invalid access token, expired access token

		status code: 401

		```
		{
			"error": {
				"message": "<Error Message>"
			}
		}
		```

	- Cause: No habit found

		status cod: 404

		```
		{
			"error": {
				"message": "<Error Message>"
			}
		}
		```

#### Deactivate Habit

```
DELETE /<int:id>
```

Header

```
Authorization: Bearer <access_token>
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

	- Cause: No access token presented, invalid access token, expired access token

		status code: 401

		```
		{
			"error": {
				"message": "<Error Message>"
			}
		}
		```

	- Cause: No habit found

		status cod: 404

		```
		{
			"error": {
				"message": "<Error Message>"
			}
		}
		```

### Progress

Prefix

```
/progress
```

#### Get All Progress

```
GET /
```

Header

```
Authorization: Bearer <access_token>
```

Response

1. Success

	status code: 200

	```
	{
		"success": {
			"result": [
				{
					"end_time": "<end_time>", # ISO 8601 format
					"habit_id": "<habit_id">,
					"id": "<id>",
					"length_seconds": "<length_seconds>,
					"removed": "<removed>",
					"start_time": "<start_time>" # ISO 8601 format
				},
				...
			]
		}
	}
	```

1. Failure

	- Cause: No access token presented, invalid access token, expired access token

		status code: 401

		```
		{
			"error": {
				"message": "<Error Message>"
			}
		}
		```

#### Get Progress

```
GET /<int:id>
```

Header

```
Authorization: Bearer <access_token>
```

Response

1. Success

	status code: 200

	```
	{
		"success": {
			"result": {
				"end_time": "<end_time>", # ISO 8601 format
				"habit_id": "<habit_id">,
				"id": "<id>",
				"length_seconds": "<length_seconds>,
				"removed": "<removed>",
				"start_time": "<start_time>" # ISO 8601 format
			}
		}
	}
	```

1. Failure

	- Cause: No access token presented, invalid access token, expired access token

		status code: 401

		```
		{
			"error": {
				"message": "<Error Message>"
			}
		}
		```

	- Cause: No habit found

		status cod: 404

		```
		{
			"error": {
				"message": "<Error Message>"
			}
		}
		```

#### Start Habit

```
POST /start
```

Header

```
Authorization: Bearer <access_token>
```

Parameter

location: Form

```
habit_id = <habit_id>
time = <time> *OPTIONAL* # ISO 8601 Format
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

	- Cause: Habit started and not ended, time not formatted in ISO 8601 format

		status code: 400

		```
		{
			"error": {
				"message": "<Error Message>"
			}
		}
		```

	- Cause: No access token presented, invalid access token, expired access token

		status code: 401

		```
		{
			"error": {
				"message": "<Error Message>"
			}
		}
		```

	- Cause: Habit not found

		status code: 404

		```
		{
			"error": {
				"message": "<Error Message>"
			}
		}
		```

#### End Habit

```
POST /end
```

Header

```
Authorization: Bearer <access_token>
```

Parameter

location: Form

```
habit_id = <habit_id>
time = <time> *OPTIONAL* # ISO 8601 Format
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

	- Cause: Habit not started, time not formatted in ISO 8601 format

		status code: 400

		```
		{
			"error": {
				"message": "<Error Message>"
			}
		}
		```

	- Cause: No access token presented, invalid access token, expired access token

		status code: 401

		```
		{
			"error": {
				"message": "<Error Message>"
			}
		}
		```

	- Cause: Habit not found

		status code: 404

		```
		{
			"error": {
				"message": "<Error Message>"
			}
		}
		```

#### Update Progress

```
PUT /<int:id>
```

Header

```
Authorization: Bearer <access_token>
```

Parameter

location: Form

```
start_time = <start_time> *OPTIONAL* # ISO 8601 Format
end_time = <end_time> *OPTIONAL* # ISO 8601 Format
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

	- Cause: No access token presented, invalid access token, expired access token

		status code: 401

		```
		{
			"error": {
				"message": "<Error Message>"
			}
		}
		```

	- Cause: No progress found

		status cod: 404

		```
		{
			"error": {
				"message": "<Error Message>"
			}
		}
		```

#### Activate Progress

```
POST /<int:id>
```

Header

```
Authorization: Bearer <access_token>
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

	- Cause: No access token presented, invalid access token, expired access token

		status code: 401

		```
		{
			"error": {
				"message": "<Error Message>"
			}
		}
		```

	- Cause: No progress found

		status cod: 404

		```
		{
			"error": {
				"message": "<Error Message>"
			}
		}
		```

#### Deactivate Progress

```
DELETE /<int:id>
```

Header

```
Authorization: Bearer <access_token>
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

	- Cause: No access token presented, invalid access token, expired access token

		status code: 401

		```
		{
			"error": {
				"message": "<Error Message>"
			}
		}
		```

	- Cause: No progress found

		status cod: 404

		```
		{
			"error": {
				"message": "<Error Message>"
			}
		}
		```
