<template>
    <v-card class="mx-auto" max-width="344">
        <v-card-text>
            <div>Test Card</div>
            <p class="display-1 text--primary">test card title</p>
            <p>adjective</p>
            <div class="text--primary">
                {{curQuestion}} <br />
                <input type="text" @keyup.enter="onSubmit" />
            </div>
        </v-card-text>
        <v-card-actions>
            <v-btn text class="large primary" @click="onNext">Next</v-btn>
        </v-card-actions>
    </v-card>
</template>

<script>
export default {
    data: () => ({
        questionID: Number,
        questions: Array,
    }),
    props: {

    },
    computed: {
        curQuestion: function () {
            return this.questions[this.questionID];
        }
    },
    methods: {
        onNext: function () {
            this.questionID++;
        },
        onSubmit: function () {
            alert('submit');
        }
    },
    mounted () {
        this.questionID = 0;
        this.questions = ["one", "two", "three"];
    }
};
</script>
