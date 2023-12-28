<template>
    <div class="modal" v-show="isModalVisible">
        <div class="execute_btn">
            <button type="button" class="cancel"  @click="handleCancel" >X</button>
            <button type="submit" class="add" @click="addList">Add</button>
        </div>
        <form @submit.prevent="addList">
            <input type="text" id="listTitle" v-model="listTitle" placeholder="Title" required />
        </form>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        listTitle: "",
      };
    },
    methods: {
        handleCancel(){
            this.$emit("cancel");
        },
        addList() {
            // Émet un événement pour indiquer qu'une nouvelle liste doit être ajoutée
            this.$emit("add-list", this.listTitle);
            // Réinitialise le champ de texte
            this.listTitle = "";
        },
    },
    props: {
      isModalVisible: Boolean,
    },
  };
  </script>
  
  <style scoped>
   @import "@/components/style/variables.css";
  .modal {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    background-color: var(--bg-color-half);
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
    z-index: 1000;
    width: 90%;
    height: 50%;
  }

  button{
    width:10%;
    font-size: 20px;
    background-color: rgba(0, 0, 0, 0);
    border: none;
    box-shadow: 0 0 0px;
    color:white;
    box-shadow: 0 0 0px rgba(0, 0, 0, 0);
    font-family: 'Rubik', sans-serif;
  }

  input{
    display: flex;
    width: auto;
    height: 100%;
    font-size: 20px;
    padding: 10px;
    margin: 10px;
    background-color: var(--primary-color);
    border: none;
    border-radius: 20px;
    color :var(--bg-color);
    justify-content: center;
  }

  .execute_btn{
    display: flex;
    justify-content: space-between;
  }
  </style>
  