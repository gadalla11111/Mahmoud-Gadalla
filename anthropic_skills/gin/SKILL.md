# Skill: gin

**Trigger:** build a Go HTTP API, Go web server, Go REST API, Go microservice, "use Gin framework", Go backend, Go router, Go middleware.

---

## What this skill does

Guides Go HTTP API development using Gin — the fastest Go web framework (40x faster than
alternatives via zero-allocation router). REST APIs, middleware chains, validation, and
microservices patterns.

**Source:** `gin-gonic/gin`

---

## Quick start

```go
package main

import "github.com/gin-gonic/gin"

func main() {
    r := gin.Default()  // includes Logger + Recovery middleware

    r.GET("/ping", func(c *gin.Context) {
        c.JSON(200, gin.H{"message": "pong"})
    })

    r.Run(":8080")
}
```

```bash
go get -u github.com/gin-gonic/gin
```

---

## Key patterns

```go
// Route groups + middleware
api := r.Group("/api/v1", AuthMiddleware())
{
    api.GET("/users", getUsers)
    api.POST("/users", createUser)
    api.DELETE("/users/:id", deleteUser)
}

// Request binding + validation
type CreateUserInput struct {
    Name  string `json:"name"  binding:"required"`
    Email string `json:"email" binding:"required,email"`
}

func createUser(c *gin.Context) {
    var input CreateUserInput
    if err := c.ShouldBindJSON(&input); err != nil {
        c.JSON(400, gin.H{"error": err.Error()})
        return
    }
    // ...
}

// Custom middleware
func AuthMiddleware() gin.HandlerFunc {
    return func(c *gin.Context) {
        token := c.GetHeader("Authorization")
        if !validateToken(token) {
            c.AbortWithStatusJSON(401, gin.H{"error": "unauthorized"})
            return
        }
        c.Next()
    }
}
```

---

## Performance defaults

- Use `gin.New()` + explicit middleware for production (no debug logs)
- `gin.SetMode(gin.ReleaseMode)` before `gin.New()`
- Zero-copy param binding via `c.Param()` / `c.Query()`

---

## Health

```yaml
pass_rate: null
trigger_accuracy: null
cross_references: []
archetype: web-framework
```
