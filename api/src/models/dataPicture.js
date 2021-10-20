import mongoose from "mongoose";

const Schema = mongoose.Schema;

const pictureSchema = new Schema({
    title: {
        type: String

    },
    file: {
        type: String
    },
    type: {
        type: String
    }
}, {
    timestamps: {
        createdAt: 'createdAt',
    }
});
const Picture = mongoose.model('Picture', pictureSchema);
export {Picture}




