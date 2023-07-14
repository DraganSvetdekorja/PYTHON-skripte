

<?php

include_once('../importer/lib/global.php');
require_once(DIR_MAGENTO . 'app/Mage.php');
Mage::app();
// Connect to Magento 1 API

// Retrieve product collection
$collection = Mage::getModel('catalog/product')->getCollection();

// Apply filters, sorting, and specify attributes
$collection->addAttributeToSelect('name')
    ->addAttributeToSelect('price')
    ->addAttributeToSelect('thumbnail')
    ->addAttributeToSelect('category_id')
    ->addAttributeToFilter('status', 1)
    ->addAttributeToFilter('visibility', 4)
    ->addAttributeToSort('name', 'ASC');
	->setPageSize(20); // Set the desired page size
// Fetch the collection data
$products = $collection->getData();

// Close the Magento 1 API connection

// Display the product data as an HTML table
echo '<table class="table" id="productTable">';
echo '<thead><tr><th>Name</th><th>Price</th><th>Thumbnail</th><th>Category</th></tr></thead>';
echo '<tbody>';

foreach ($products as $product) {
    $name = $product['name'];
    $price = $product['price'];
    $thumbnailUrl = Mage::getModel('catalog/product')->load($product['entity_id'])->getThumbnailUrl();
    $categoryIds = $product['category_id'];

    // Retrieve category names
    $categoryNames = [];
    foreach ($categoryIds as $categoryId) {
        $category = Mage::getModel('catalog/category')->load($categoryId);
        $categoryNames[] = $category->getName();
    }
    $categoryNames = implode(', ', $categoryNames);

    echo "<tr><td>$name</td><td>$price</td><td><img src='$thumbnailUrl'></td><td>$categoryNames</td></tr>";
}

echo '</tbody></table>';
?>
