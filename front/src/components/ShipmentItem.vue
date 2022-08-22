<template>
  <div>
    From: {{ shipment.from_addr }}, 
    To: {{ shipment.to_addr }}, 
    State: {{ shipment.state }} 
    <button class="edit" v-on:click="$emit('edit-shipment', shipment)">
        Edit
    </button>
    <button class="delete" v-on:click="$emit('delete-shipment', shipment)">
        Delete
    </button>
  </div>
</template>

<script>
export default {
    computed: {
    },
    props: ["shipment"]
}
</script>