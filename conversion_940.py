import os
import xml.etree.ElementTree as et
from datetime import date, datetime
import sys
import psycopg2
import logging


class Convert_940:

    def __init__(self, formatted_segments):
        self.formatted_segments = formatted_segments

    def parse_edi(self, formatted_segments):

        # variables specific to the translation
        orderlinenumber = ''
        depositor_order_number = ''
        customer_name = ''
        identifier = 0

        for seg in formatted_segments:
            if seg[0] == "ISA":
                identifier = 0
                nte_line = []
                global isa
                isa = seg[13].lstrip('0')
                n3_present = False
            if seg[0] == "W05":
                # Generating static XML elements.
                root = et.Element('Order')
                order_header_tag = et.SubElement(root, 'OrderHeader')
                facility_tag = et.SubElement(order_header_tag, 'Facility')
                facility_tag.text = 'SA1'
                client_tag = et.SubElement(order_header_tag, 'Client')
                client_tag.text = '21'
                depositor_order_number_tag = et.SubElement(order_header_tag, 'DepositorOrderNumber')
                order_status_tag = et.SubElement(order_header_tag, 'OrderStatus')
                order_status_tag.text = 'New'
                purchase_order_number_tag = et.SubElement(order_header_tag, 'PurchaseOrderNumber')
                master_reference_number_tag = et.SubElement(order_header_tag, 'MasterReferenceNumber')
                bill_to_tag = et.SubElement(order_header_tag, 'BillTo')
                bill_to_code_tag = et.SubElement(bill_to_tag, 'Code')
                ship_to_tag = et.SubElement(order_header_tag, 'ShipTo')
                ship_to_name_tag = et.SubElement(ship_to_tag, 'Name')
                ship_to_code_tag = et.SubElement(ship_to_tag, 'Code')
                ship_to_address1_tag = et.SubElement(ship_to_tag, 'Address1')
                ship_to_address2_tag = et.SubElement(ship_to_tag, 'Address2')
                ship_to_city_tag = et.SubElement(ship_to_tag, 'City')
                ship_to_state_tag = et.SubElement(ship_to_tag, 'State')
                ship_to_zip_code_tag = et.SubElement(ship_to_tag, 'ZipCode')
                ship_to_country_tag = et.SubElement(ship_to_tag, 'Country')
                ship_to_contact_phone_tag = et.SubElement(ship_to_tag, 'ContactPhone')
                dates_tag = et.SubElement(order_header_tag, 'Dates')
                purchase_order_date_tag = et.SubElement(dates_tag, 'PurchaseOrderDate')
                requested_ship_date_tag = et.SubElement(dates_tag, 'RequestedShipDate')
                cancel_date_tag = et.SubElement(dates_tag, 'CancelDate')
                ship_not_before_date_tag = et.SubElement(dates_tag, 'ShipNotBeforeDate')
                reference_information_tag = et.SubElement(order_header_tag, 'ReferenceInformation')
                customer_name_tag = et.SubElement(reference_information_tag, 'CustomerName')
                warehouse_code_tag = et.SubElement(reference_information_tag, 'WarehouseCode')
                account_number_tag = et.SubElement(reference_information_tag, 'AccountNumber')
                messages_tag = et.SubElement(order_header_tag, 'Messages')
                warehouse_instructions_tag = et.SubElement(messages_tag, 'WarehouseInstructions')
                shipping_instructions_tag = et.SubElement(order_header_tag, 'ShippingInstructions')
                shipment_method_of_payment_tag = et.SubElement(shipping_instructions_tag, 'ShipmentMethodOfPayment')
                transportation_method_tag = et.SubElement(shipping_instructions_tag, 'TransportationMethod')
                carrier_code_tag = et.SubElement(shipping_instructions_tag, 'CarrierCode')
                routing_tag = et.SubElement(shipping_instructions_tag, 'Routing')
                order_detail_tag = et.SubElement(root, 'OrderDetail')
                depositor_order_number_tag.text = seg[2]
                depositor_order_number = seg[2]
                purchase_order_number_tag.text = seg[3]
                master_reference_number_tag.text = seg[2]
            if seg[0] == "N1" and seg[1] == "BY":
                bill_to_code_tag.text = seg[4]
                customer_name_tag.text = seg[4]
                customer_name = seg[4]
            if seg[0] == "N1" and seg[1] == "ST":
                identifier = 1
                ship_to_name_tag.text = seg[2].replace("'", '')
                ship_to_code_tag.text = seg[4]
            if seg[0] == "N2" and identifier == 1:
                ship_to_address2_tag.text = seg[1]
                ship_to_address2 = seg[1]
            if seg[0] == "N3" and seg[1] != "" and identifier == 1:
                n3_present = True
                ship_to_address1_tag.text = seg[1].replace("'", '')
                ship_to_address1 = seg[1]
                try:
                    if "PHN" in seg[2]:
                        ship_to_contact_phone = str(seg[2]).split(":")
                        ship_to_contact_phone_tag.text = ship_to_contact_phone[1]
                    else:
                        ship_to_address1 = seg[1] + " " + seg[2]
                        ship_to_address1_tag.text = ship_to_address1
                except IndexError:
                    pass
            if seg[0] == "N4" and identifier == 1:
                ship_to_city_tag.text = seg[1].replace("'", '')
                ship_to_state_tag.text = seg[2]
                ship_to_zip_code_tag.text = seg[3]
                ship_to_country_tag.text = 'US'
            if seg[0] == "N1" and seg[1] == "BT":
                identifier = 2
            if seg[0] == "N9" and seg[1] == "WS":
                warehouse_code_tag.text = seg[2]
            if seg[0] == "G62" and seg[1] == "04":
                purchase_order_date = seg[2]
                purchase_order_date = '-'.join(
                    [purchase_order_date[:4], purchase_order_date[4:6], purchase_order_date[6:]])
                purchase_order_date_tag.text = purchase_order_date
            if seg[0] == "G62" and seg[1] == "10":
                requested_ship_date = seg[2]
                requested_ship_date = '-'.join(
                    [requested_ship_date[:4], requested_ship_date[4:6], requested_ship_date[6:]])
                requested_ship_date_tag.text = requested_ship_date
            if seg[0] == "G62" and seg[1] == "01":
                ship_not_before_date = seg[2]
                ship_not_before_date = '-'.join(
                    [ship_not_before_date[:4], ship_not_before_date[4:6], ship_not_before_date[6:]])
                ship_not_before_date_tag.text = ship_not_before_date
                cancel_date = seg[2]
                cancel_date = '-'.join([cancel_date[:4], cancel_date[4:6], cancel_date[6:]])
                cancel_date_tag.text = cancel_date
            if seg[0] == "NTE":
                nte_line.append(str(seg[2]).replace("'", ""))
            if seg[0] == "W66":

                # joining all NTE segments and applying it to the warhouse_instructions tag with a limit of 410 characters

                nte_full_line = ' '.join(nte_line)

                warehouse_instructions_tag.text = nte_full_line[:410]

                # Clearing nte_line for next iteration
                nte_line = []

                shipment_method_of_payment_tag.text = seg[1]
                transportation_method_tag.text = seg[2]
                routing_tag.text = seg[5]
                account_number_tag.text = seg[7]
                carrier_code_tag.text = seg[10]
            if seg[0] == "LX":
                orderlinenumber = seg[1]
            if seg[0] == "W01":
                order_line_tag = et.SubElement(order_detail_tag, 'OrderLine')
                order_line_number_tag = et.SubElement(order_line_tag, 'OrderLineNumber')
                order_line_number_tag.text = orderlinenumber
                item_number_tag = et.SubElement(order_line_tag, 'ItemNumber')
                item_upc_tag = et.SubElement(order_line_tag, 'ItemUPC')
                ordered_quantity_tag = et.SubElement(order_line_tag, 'OrderedQuantity')
                quantity_unit_of_measure_tag = et.SubElement(order_line_tag, 'QuantityUnitOfMeasure')
                item_description_tag = et.SubElement(order_line_tag, 'ItemDescription')
                pack_quantity_tag = et.SubElement(order_line_tag, 'PackQuantity')
                buyer_item_number_tag = et.SubElement(order_line_tag, 'BuyerItemNumber')
                ordered_quantity_tag.text = seg[1]
                quantity_unit_of_measure_tag.text = seg[2]
                item_number_tag.text = seg[7]
                item_upc_tag.text = seg[5]
            if seg[0] == "G69":
                item_description_tag.text = seg[1]
            if seg[0] == "N9" and seg[1] == "ZZ":
                pack_quantity_tag.text = seg[2]
            if seg[0] == "W20":
                pack_quantity_tag.text = seg[1]
            if seg[0] == "SE":
                identifier = 0
                if n3_present is False:
                    ship_to_address1_tag.text = ship_to_address2
                    ship_to_address2_tag.text = ""
                tree = et.ElementTree(root)
                et.indent(tree, space="\t", level=0)
                tree.write("C:\\FTP\\GPAEDIProduction\\Integral\\In\\940_21_" + str(depositor_order_number) + "_" + str(isa) + "_" + str(customer_name) + "_" + datetime.now().strftime("%Y%m%d%H%M%S") + ".xml", encoding="UTF-8", xml_declaration=True)
                tree.write("C:\\FTP\\GPAEDIProduction\\SA1-Equity Brands\\Out\\Archive\\940\\940_21_" + str(depositor_order_number) + "_" + str(isa) + "_" + str(customer_name) + "_" + datetime.now().strftime("%Y%m%d%H%M%S") + ".xml", encoding="UTF-8", xml_declaration=True)