<template>
  <form>
    <p>
      <label>From: </label><input type="text" v-model="shipment.from_addr"/>
      <label>To: </label><input type="text" v-model="shipment.to_addr"/>
    </p>
    <p>
      <label>State: </label>
      <select v-model="shipment.state">
        <option>Receiving</option>
        <option>Processing</option>
        <option>Fulfilling</option>
        <option>Done</option>
      </select>
    </p>
    <p>
      <button class="save" v-on:click="$emit('edit-save', shipment)">Save</button>
      <button class="cancel" v-on:click="$emit('edit-cancel', shipment)">Cancel</button>
    </p>
  </form>
</template>

<script>
export default {
    props:
        ["shipment"]
}
</script>