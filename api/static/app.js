  const { createApp } = Vue
 
  createApp({

    data() {
      return {
        fileName: null,
        file: null,
        video: null,
        url: null,
        scenes: null,
        loading: false,
        errors: false,
        hashFile: false,
        videoExt: 'mp4'
      }
    },

    methods: {
        reset(){
          this.fileName = null
          this.file = null 
          this.video = null
          this.scenes = null
          this.loading = false
          this.$refs.inputFile.value=null
          this.errors = false,
          this.hashFile = false,
          this.url = null

        },

        handleFile(e) {
          const files = Array.from(e.target.files) || null
          this.setFile(files)
        },

        dropFile(e){
          const files = e.dataTransfer.files
          this.setFile(files)
        },


        setFile(files){
          if(files && files.length > 0){
            this.fileName = files[0].name
            this.file = files[0]
          }
        },

        async handleUpload(){

          this.video = null
          this.scenes = null
          this.url = null
          let data = new FormData()
          data.append('file', this.file)
          this.loading = true
          const response = await fetch('/predict', {
            method: 'POST',
            body: data
          })

          const jsonData = await response.json()

          this.processData(jsonData)
              
          this.loading = false
   
        },

        async handleUrlYoutube(){
          this.video = null
          this.scenes = null
          let data = new FormData()
          data.append('url', this.url) 
          this.loading = true
          const response = await fetch('/predict_youtube', {
            method: 'POST',
            body: data
          })

          const jsonData = await response.json()

          this.processData(jsonData)

          this.loading = false
        },

        processData(jsonData){

          if(jsonData['success']){
            this.hashFile = jsonData['file_name']
            this.video = '/static/uploads/' + jsonData['dir'] + '/' + this.hashFile
            this.videoExt = this.hashFile.split('.').pop();
            this.scenes = jsonData['scenes']
            this.errors = false
            this.url = null
            this.fileName = null
            return true

          } else {
            this.errors = jsonData['error']
            return false
          }
          
        },

    },
    delimiters: ['[[',']]']
  }).mount('#app')
