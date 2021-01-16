# List of custom derivatives

```xml
<hota-core></hota-core>
<hota-payload>
  <hota-ack>{{ acknowledgement key }}</hota-ack>
  <!-- used to verify the placement of the other elements -->
  <hota-frame id="{{ uuid }}"></hota-frame>
</hota-payload>
<!-- payload sent over WS -->
<hota-redirect>{{ href }}</hota-redirect>
<!-- equivalent to window.location.href = href; -->
<hota-ephemeral-alert>{{ message }}</hota-ephemeral-alert>
<!-- equivalent to alert(message); -->
<hota-http verb="get | post | put | patch" href="..." headers="{}">{{ body }}</hota-http>
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
3. Insert at designated `hota-core` element (inside head)
4. Handle Event

# Event Handlers

```py
{
  "4bcb11b4-765f-4fd0-a819-a4fc20ac9037": <function handler at 0x00000274647B8160>
}
```
