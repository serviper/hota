# List of custom derivatives

```xml
<hotair-core></hotair-core>
<hotair-payload>
  <hotair-ack>{{ acknowledgement key }}</hotair-ack>
  <!-- used to verify the placement of the other elements -->
  <hotair-frame id="{{ uuid }}"></hotair-frame>
</hotair-payload>
<!-- payload sent over WS -->
<hotair-redirect>{{ href }}</hotair-redirect>
<!-- equivalent to window.location.href = href; -->
<hotair-ephemeral-alert>{{ message }}</hotair-ephemeral-alert>
<!-- equivalent to alert(message); -->
<hotair-http verb="get | post | put | patch" href="..." headers="{}">{{ body }}</hotair-http>
<!-- strict form of client side requests, which would be sent back to server -->
```

# Typical Payload Pt. 1

```json
{
  "type": ActionType,
  "for": "id", // element id
  "nack": "..." // acknowledgement key
}
```

# ActionType

1. Insert at `payload.for`
2. Update frame `payload.for`
3. Insert at designated `hotair-core` element (inside head)
4. Handle Event

# Event Handlers

```py
{
  "4bcb11b4-765f-4fd0-a819-a4fc20ac9037": <function handler at 0x00000274647B8160>
}
```
