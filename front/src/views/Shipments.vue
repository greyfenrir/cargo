<template>
  <div class="home">
    <EditForm 
        v-if="editMode"
        v-bind:shipment="shipment"
        v-on:edit-save="editSave"
        v-on:edit-cancel="editCancel"
    />
    <ShipmentList
        v-if="!editMode"
        v-bind:shipments="shipments"
        @edit-shipment="editShipment"
    />
  </div>
</template>

<script>
import ShipmentList from '@/components/ShipmentList';
import EditForm from '@/components/EditForm.vue';
export default {
    data() {
        return {
            shipments: [],
            editMode: false
        }
    },
    components: {
    ShipmentList,
    EditForm
},
    mounted() {
        fetch ('http://127.0.0.1:8000/shipments/')
            .then(response => response.json())
            .then(json => {this.shipments = json})
    },
    methods: {
        editShipment(id) {
            this.shipment = this.shipments.filter(t => t.id === id)[0]
            this.switchEditMode()
        },
        editSave(id) {
            console.log("save: " + id)
            this.switchEditMode()
        },
        editCancel() {
            console.log("cancel")
            this.switchEditMode()
        },
        switchEditMode() {
            this.editMode = !this.editMode
        }
    }
}
</script>