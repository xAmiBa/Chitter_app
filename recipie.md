## STRAIGHT UP

```
As a Maker
So that I can let people know what I am doing
I want to post a message (peep) to chitter
```
```As a maker
So that I can see what others are saying
I want to see all peeps in reverse chronological order
```
```As a Maker
So that I can better appreciate the context of a peep
I want to see the time at which it was made
```
```As a Maker
So that I can post messages on Chitter as me
I want to sign up for Chitter
```
* chitter database:
    * peeps
    * users
* classes:
    * PeepRepository
    * Peep
        * content
        * `date`
        * time
    * User
        * self.email (unique)
        * self.password
        * self.name (can be full name)
        * self.username (unique)
    * UserRepository (User objects)
        * sign up (password and email validation)
        * `log in (password validation)`
        * `log out`

Features:
* sign up to chitter -> User
* post a peep (content, username, date?, time) -> Peep
* see all peeps in reverse chronological order -> Peep

## HARDER

```As a Maker
So that only I can post messages on Chitter as me
I want to log in to Chitter
```
```As a Maker
So that I can avoid others posting messages on Chitter as me
I want to log out of Chitter
```
## ADVANCED

```As a Maker
So that I can stay constantly tapped in to the shouty box of Chitter
I want to receive an email if I am tagged in a Peep
```