<template>
  <div class="home">
    <EditForm 
        v-if="editMode"
        v-bind:id="shipment.id"
        v-bind:from="shipment.from_addr"
        v-bind:to="shipment.to_addr"
        v-bind:state="shipment.state"
        v-on:edit-save="editSave"
        v-on:edit-cancel="editCancel"
    />
    <ShipmentList
        v-if="!editMode"
        v-bind:shipments="shipments"
        @edit-shipment="editShipment"
        @delete-shipment="deleteShipment"
        @add-shipment="addShipment"
    />
    <button @click="logout">Logout</button>
  </div>
</template>

<script>
import ShipmentList from '@/components/ShipmentList';
import EditForm from '@/components/EditForm.vue';
export default {
    data() {
        return {
            shipments: [],
            editMode: false,
            newShipment: false
        }
    },

    components: {
        ShipmentList,
        EditForm
    },

    mounted() {
        fetch (this.drfURI + 'shipments/')
            .then(response => response.json())
            .then(json => {this.shipments = json})
    },
    
    methods: {
        logout() {
            sessionStorage.setItem('token', '')
            this.$router.push({name: 'home'})

        },
        addShipment(){
            const shipment = {
                id: Date.now(),
                created: Date.now(),
                from_addr: "",
                to_addr: "",
                owner: "admin"
            }
            this.shipments.push(shipment)
            this.editShipment(shipment.id)
            this.newShipment = true
        },
        editShipment(id) {
            this.shipment = this.shipments.filter(s => s.id === id)[0]
            this.switchEditMode()
        },
        deleteShipment(id) {
            this.shipments = this.shipments.filter(s => s.id != id)            
            if (!this.newShipment) {
                token = sessionStorage.getItem('token')
                // DELETE
            }
        },
        editSave(id, from, to, state) {
            // some validation here...
            this.shipment.from_addr = from
            this.shipment.to_addr = to
            this.shipment.state = state
            this.newShipment = false        
            token = sessionStorage.getItem('token')
            if (this.newShipment) {
                // POST                
            } else {
                // PUT
            }
            this.newShipment = false
            this.switchEditMode()
        },
        editCancel(id) {            
            if (this.newShipment) {
                this.deleteShipment(id)
            }
            this.newShipment = false
            this.switchEditMode()
        },
        switchEditMode() {
            this.editMode = !this.editMode
        }
    }
}
</script>