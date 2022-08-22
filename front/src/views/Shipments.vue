<template>
  <div class="home">
    <EditForm 
        v-if="editMode"
        v-bind:shipment="shipment"
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
import $ from 'jquery'
export default {
    data() {
        return {
            shipments: [],
            shipment: {},
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
            $.ajax({
                url: this.drfURI + 'auth/logout',
                type: 'DELETE',
                headers: {
                    'Authorization': 'Token ' + sessionStorage.getItem('token')
                },
            })
            sessionStorage.setItem('token', '')
            this.$router.push({name: 'home'})

        },
        addShipment(){
            const shipment = {
                id: '',
                created: '',
                from_addr: '',
                to_addr: '',
                state: 'Receiving',
                owner: ''
            }
            this.newShipment = true            
            this.editShipment(shipment)
        },
        editShipment(shipment) {
            this.shipment = shipment
            this.switchEditMode()
        },
        deleteShipment(shipment) {
            this.shipments = this.shipments.filter(s => s.id != shipment.id)
            if (!this.newShipment) {
                $.ajax({
                    url: this.drfURI + 'shipments/' + shipment.id  + '/',
                    type: 'DELETE',
                    headers: {
                        'Authorization': 'Token ' + sessionStorage.getItem('token')
                    }
                })
            }
        },
        editSave(shipment) {
            // some validation here...            
            if (this.newShipment) {
                $.ajax({
                    url: this.drfURI + 'shipments/',
                    type: 'POST',
                    headers: {
                        'Authorization': 'Token ' + sessionStorage.getItem('token')
                    },
                    data: {
                        'from_addr': shipment.from_addr,
                        'to_addr': shipment.to_addr,
                        'state': shipment.state
                    },
                    success: (response) => {                    
                        this.shipments.push(response)
                    }                    
                })                
            } else {
                $.ajax({
                    url: this.drfURI + 'shipments/' + shipment.id  + '/',
                    type: 'PUT',
                    headers: {
                        'Authorization': 'Token ' + sessionStorage.getItem('token')
                    },
                    data: {
                        'from_addr': shipment.from_addr,
                        'to_addr': shipment.to_addr,
                        'state': shipment.state
                    },
                    success: (response) => {                    
                        console.log('success: ' + response)
                    },
                    error: (response) => {
                        console.log('error: ' + response)
                    }
                })
            }
            this.newShipment = false
            this.switchEditMode()
        },
        editCancel(id) {            
            this.newShipment = false
            this.switchEditMode()
        },
        switchEditMode() {
            this.editMode = !this.editMode
        }
    }
}
</script>