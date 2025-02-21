from Package import Package
from Truck import Truck
from HubClass import Hub
from HashTableImp import HashTable
from utils.CsvDataLoader import read_packages_from_csv


hash_table = HashTable()


for package in read_packages_from_csv('csv/Package_File.csv'):
    hash_table.insert(package.id, package)

print("Hash Table after insertion:")
hash_table.display()

package_ids = hash_table.get_all_package_ids()
print("All package IDs:", package_ids)

