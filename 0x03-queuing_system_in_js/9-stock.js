import express from 'express';
import { createClient } from 'redis';
import { promisify } from 'util';

const app = express();
const port = 1245;

// List of products
const listProducts = [
  { itemId: 1, itemName: 'Suitcase 250', price: 50, initialAvailableQuantity: 4 },
  { itemId: 2, itemName: 'Suitcase 450', price: 100, initialAvailableQuantity: 10 },
  { itemId: 3, itemName: 'Suitcase 650', price: 350, initialAvailableQuantity: 2 },
  { itemId: 4, itemName: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5 }
];

// Redis client
const client = createClient();
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

// Function to reserve stock by itemId
const reserveStockById = async (itemId, stock) => {
  await setAsync(`item.${itemId}`, stock);
};

// Function to get current reserved stock by itemId
const getCurrentReservedStockById = async (itemId) => {
  const stock = await getAsync(`item.${itemId}`);
  return stock ? parseInt(stock) : 0;
};

// Function to get item by id
const getItemById = (id) => {
  return listProducts.find(item => item.itemId === id);
};

// Route to list all products
app.get('/list_products', (req, res) => {
  res.json(listProducts.map(item => ({
    itemId: item.itemId,
    itemName: item.itemName,
    price: item.price,
    initialAvailableQuantity: item.initialAvailableQuantity
  })));
});

// Route to get product details by itemId
app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const item = getItemById(itemId);
  if (!item) {
    res.status(404).json({ status: "Product not found" });
  } else {
    const currentQuantity = await getCurrentReservedStockById(itemId);
    res.json({ ...item, currentQuantity });
  }
});

// Route to reserve product by itemId
app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const item = getItemById(itemId);
  if (!item) {
    res.json({ status: "Product not found" });
  } else {
    const currentQuantity = await getCurrentReservedStockById(itemId);
    if (currentQuantity === 0) {
      res.json({ status: "Not enough stock available", itemId });
    } else {
      await reserveStockById(itemId, currentQuantity - 1);
      res.json({ status: "Reservation confirmed", itemId });
    }
  }
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
