<template>
  <div>
    <ul>
        <li>
            From: {{ shipment.from_addr }}, 
            To: {{ shipment.to_addr }}, 
            State: {{ shipment.state }} 
            <button class="edit" v-on:click="$emit('edit-shipment', shipment.id)"> 
                Edit
            </button>
        </li>
    </ul>
  </div>
</template>

<script>
export default {
    computed: {
    },
    props: {
        shipment: {
            type: Object,
            required: true
        }
    }
}
</script>