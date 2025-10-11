import express from "express";
import mongoose from "mongoose";
import fetch from "node-fetch";
import cron from "node-cron";

const app = express();

// MongoDB connect
mongoose.connect("mongodb://127.0.0.1:27017/productsDB", {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

// Schema
const productSchema = new mongoose.Schema({
  title: String,
  price: Number,
  description: String,
  image: String,
  updatedAt: Date
});

const Product = mongoose.model("Product", productSchema);

// API se latest data fetch karke DB update
async function updateProductData() {
  try {
    console.log("🔄 Fetching latest product data...");
    const res = await fetch("https://fakestoreapi.com/products/1");
    const data = await res.json();

    await Product.findOneAndUpdate(
      { title: data.title },
      {
        title: data.title,
        price: data.price,
        description: data.description,
        image: data.image,
        updatedAt: new Date()
      },
      { upsert: true }
    );

    console.log("✅ Product data updated");
  } catch (err) {
    console.error("❌ Error updating product:", err);
  }
}

// Cron job: daily update at 12:00 AM
cron.schedule("0 0 * * *", updateProductData);

// API route for frontend
app.get("/product", async (req, res) => {
  const product = await Product.findOne();
  res.json(product);
});

// Start server
app.listen(5000, () => {
  console.log("🚀 Server running on http://localhost:5000");
  updateProductData();
});
