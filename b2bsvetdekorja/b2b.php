<?php
use Magento\Framework\App\Bootstrap;
use Magento\CatalogInventory\Api\StockRegistryInterface;
use Magento\Catalog\Helper\Image as ImageHelper;
use PhpOffice\PhpSpreadsheet\Spreadsheet;
use PhpOffice\PhpSpreadsheet\Writer\Xlsx;

require __DIR__ . '/app/bootstrap.php';

$bootstrap = Bootstrap::create(BP, $_SERVER);
$objectManager = $bootstrap->getObjectManager();

$categoryId = 5; // Replace with the desired category ID
$websiteId = 1; // Replace with the desired website ID
$brand = 'Nike'; // Replace with the desired brand/manufacturer name

$stockRegistry = $objectManager->get(StockRegistryInterface::class);
$categoryFactory = $objectManager->create(\Magento\Catalog\Model\CategoryFactory::class);
$imageHelper = $objectManager->create(ImageHelper::class);

$category = $categoryFactory->create()->load($categoryId);
$categoryProductIds = $category->getProductCollection()->getAllIds();

$products = $objectManager->create(\Magento\Catalog\Model\ProductFactory::class)->create()->getCollection();
$products->addAttributeToSelect(['sku', 'name', 'price', 'special_price', 'dimension', 'image'])
    ->addIdFilter($categoryProductIds)
    ->addWebsiteFilter($websiteId)
    ->addAttributeToFilter('manufacturer', $brand);

$productData = [];

foreach ($products as $product) {
    $stockItem = $stockRegistry->getStockItem($product->getId());
    $stockQty = $stockItem->getQty();

    if ($stockQty >= 0) {
        $image = $imageHelper->init($product, 'product_page_image_small')->getUrl();

        $productData[] = [
            'SKU' => $product->getSku(),
            'Name' => $product->getName(),
            'Price' => $product->getPrice(),
            'Special Price' => $product->getSpecialPrice(),
            'Dimension' => $product->getAttributeText('dimension'),
            'Main Image' => $image,
            'Product URL' => $product->getProductUrl()
        ];
    }
}

$spreadsheet = new Spreadsheet();
$sheet = $spreadsheet->getActiveSheet();
$sheet->fromArray($productData, null, 'A1');

$writer = new Xlsx($spreadsheet);
$filename = 'product_data.xlsx';
$writer->save($filename);

echo 'Product data exported to ' . $filename;
