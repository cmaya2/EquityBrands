import xml.etree.ElementTree as et
from datetime import datetime


class Convert_945:

    def __init__(self, XML, path, mantis_import_path, transaction_number, client_id, connection):
        self.XML = XML
        self.path = path
        self.mantis_import_path = mantis_import_path
        self.transaction_number = transaction_number
        self.client_id = client_id
        self.connection = connection

    def parse_xml(self):

        # Load in the XML based on function that checks directory of file out of Class structure

        oak = et.parse(self.XML)
        rooted = oak.getroot()
        counter = 0
        header_string = ''
        body_string = ''
        body_header_string = ''
        segment_count = 0
        depositor_order_number = ''

        for element in rooted.iter():
            if element.tag == 'ShipmentHeader':
                for ReceiptHeader_child_element in element:
                    if ReceiptHeader_child_element.tag == 'Client':
                        client_id = ReceiptHeader_child_element.text
                    elif ReceiptHeader_child_element.tag == 'ShipmentID':
                        shipment_id = ReceiptHeader_child_element.text
                    elif ReceiptHeader_child_element.tag == 'DepositorOrderNumber':
                        depositor_order_number = ReceiptHeader_child_element.text
                    elif ReceiptHeader_child_element.tag == 'PurchaseOrderNumber':
                        purchase_order_number = ReceiptHeader_child_element.text
                    elif ReceiptHeader_child_element.tag == 'MasterReferenceNumber':
                        master_reference_number = ReceiptHeader_child_element.text
                    elif ReceiptHeader_child_element.tag == 'TotalQuantityShipped':
                        total_quantity_shipped = ReceiptHeader_child_element.text
                    elif ReceiptHeader_child_element.tag == 'TotalShipmentWeight':
                        total_shipment_weight = ReceiptHeader_child_element.text
                    elif ReceiptHeader_child_element.tag == 'PackWeightUnitOfMeasure':
                        header_pack_weight_unit_of_measure = ReceiptHeader_child_element.text
                    elif ReceiptHeader_child_element.tag == 'TotalShipmentVolume':
                        total_shipment_volume = ReceiptHeader_child_element.text
                    elif ReceiptHeader_child_element.tag == 'VolumeUnitOfMeasure':
                        volume_unit_of_measure = ReceiptHeader_child_element.text
                    elif ReceiptHeader_child_element.tag == 'TotalCartonCount':
                        total_carton_count = ReceiptHeader_child_element.text
                    elif ReceiptHeader_child_element.tag == 'TotalPalletCount':
                        total_pallet_count = ReceiptHeader_child_element.text
                    elif ReceiptHeader_child_element.tag == 'FreightCharge':
                        if ReceiptHeader_child_element.text is None:
                            freight_charge = '0'
                        else:
                            freight_charge = ReceiptHeader_child_element.text
            if element.tag == 'ShipTo':
                for ShipTo_child_element in element:
                    if ShipTo_child_element.tag == 'Name':
                        ship_to_name = ShipTo_child_element.text
                    elif ShipTo_child_element.tag == 'Code':
                        ship_to_code = ShipTo_child_element.text
                    elif ShipTo_child_element.tag == 'Address1':
                        ship_to_address1 = ShipTo_child_element.text
                    elif ShipTo_child_element.tag == 'Address2':
                        ship_to_address2 = ShipTo_child_element.text
                    elif ShipTo_child_element.tag == 'City':
                        ship_to_city = ShipTo_child_element.text
                    elif ShipTo_child_element.tag == 'State':
                        ship_to_state = ShipTo_child_element.text
                    elif ShipTo_child_element.tag == 'ZipCode':
                        ship_to_zipcode = ShipTo_child_element.text
                    elif ShipTo_child_element.tag == 'Country':
                        ship_to_country = ShipTo_child_element.text
                    elif ShipTo_child_element.tag == 'ContactName':
                        ship_to_contact_name = ShipTo_child_element.text
                    elif ShipTo_child_element.tag == 'ContactPhone':
                        ship_to_contact_phone = ShipTo_child_element.text
                    elif ShipTo_child_element.tag == 'ContactEmail':
                        ship_to_contact_email = ShipTo_child_element.text
            if element.tag == 'MarkFor':
                for MarkFor_child_element in element:
                    if MarkFor_child_element.tag == 'Name':
                        mark_for_name = MarkFor_child_element.text
                    elif MarkFor_child_element.tag == 'Code':
                        mark_for_code = MarkFor_child_element.text
                    elif MarkFor_child_element.tag == 'Address1':
                        mark_for_address1 = MarkFor_child_element.text
                    elif MarkFor_child_element.tag == 'Address2':
                        mark_for_address2 = MarkFor_child_element.text
                    elif MarkFor_child_element.tag == 'City':
                        mark_for_city = MarkFor_child_element.text
                    elif MarkFor_child_element.tag == 'State':
                        mark_for_state = MarkFor_child_element.text
                    elif MarkFor_child_element.tag == 'ZipCode':
                        mark_for_zipcode = MarkFor_child_element.text
                    elif MarkFor_child_element.tag == 'Country':
                        mark_for_country = MarkFor_child_element.text
                    elif MarkFor_child_element.tag == 'ContactName':
                        mark_for_contact_name = MarkFor_child_element.text
                    elif MarkFor_child_element.tag == 'ContactPhone':
                        mark_for_contact_phone = MarkFor_child_element.text
                    elif MarkFor_child_element.tag == 'ContactEmail':
                        mark_for_contact_email = MarkFor_child_element.text
            if element.tag == 'ShipFrom':
                for ShipFrom_child_element in element:
                    if ShipFrom_child_element.tag == 'Name':
                        ship_from_name = ShipFrom_child_element.text
                    elif ShipFrom_child_element.tag == 'Code':
                        ship_from_code = ShipFrom_child_element.text
                    elif ShipFrom_child_element.tag == 'Address1':
                        ship_from_address1 = ShipFrom_child_element.text
                    elif ShipFrom_child_element.tag == 'Address2':
                        ship_from_address2 = ShipFrom_child_element.text
                    elif ShipFrom_child_element.tag == 'City':
                        ship_from_city = ShipFrom_child_element.text
                    elif ShipFrom_child_element.tag == 'State':
                        ship_from_state = ShipFrom_child_element.text
                    elif ShipFrom_child_element.tag == 'ZipCode':
                        ship_from_zipcode = ShipFrom_child_element.text
                    elif ShipFrom_child_element.tag == 'Country':
                        ship_from_country = ShipFrom_child_element.text
                    elif ShipFrom_child_element.tag == 'ContactName':
                        ship_from_contact_name = ShipFrom_child_element.text
                    elif ShipFrom_child_element.tag == 'ContactPhone':
                        ship_from_contact_phone = ShipFrom_child_element.text
                    elif ShipFrom_child_element.tag == 'ContactEmail':
                        ship_from_contact_email = ShipFrom_child_element.text
            if element.tag == 'Dates':
                for Dates_child_element in element:
                    if Dates_child_element.tag == 'PurchaseOrderDate':
                        purchase_order_date = Dates_child_element.text
                    elif Dates_child_element.tag == 'ShipDate':
                        ship_date = Dates_child_element.text.replace('-', '')
                    elif Dates_child_element.tag == 'EstimatedDeliveryDate':
                        estimated_delivery_date = Dates_child_element.text
                    elif Dates_child_element.tag == 'ScheduledDeliveryDate':
                        scheduled_delivery_date = Dates_child_element.text
                    elif Dates_child_element.tag == 'PickupDate':
                        pick_up_date = Dates_child_element.text
            if element.tag == 'ReferenceInformation':
                for ReferenceInformation_child_element in element:
                    if ReferenceInformation_child_element.tag == 'BillOfLadingNumber':
                        bill_of_lading_number = ReferenceInformation_child_element.text
                    elif ReferenceInformation_child_element.tag == 'ProbillNumber':
                        probill_number = ReferenceInformation_child_element.text
                    elif ReferenceInformation_child_element.tag == 'CustomerName':
                        customer_name = ReferenceInformation_child_element.text
                    elif ReferenceInformation_child_element.tag == 'ContainerNumber':
                        waybill_holding = ReferenceInformation_child_element.text
                    elif ReferenceInformation_child_element.tag == 'SealNumber':
                        seal_number = ReferenceInformation_child_element.text
                    elif ReferenceInformation_child_element.tag == 'LoadNumber':
                        load_number = ReferenceInformation_child_element.text
                    elif ReferenceInformation_child_element.tag == 'E51':
                        label_code = ReferenceInformation_child_element.text
            if element.tag == 'TransportationInformation':
                for TransporationInformation_child_element in element:
                    if TransporationInformation_child_element.tag == 'ShipmentMethodOfPayment':
                        shipment_method_of_payment = TransporationInformation_child_element.text
                    if TransporationInformation_child_element.tag == 'TransportationMethod':
                        transportation_method = TransporationInformation_child_element.text
                    if TransporationInformation_child_element.tag == 'CarrierCode':
                        carrier_code = TransporationInformation_child_element.text
                    if TransporationInformation_child_element.tag == 'Routing':
                        routing = TransporationInformation_child_element.text
                    if TransporationInformation_child_element.tag == 'SpecialHandlingCode':
                        special_handling_code = TransporationInformation_child_element.text

        cursor = self.connection.cursor()
        cursor.execute("SELECT sequence_number FROM public.sequence where client='general'")
        data = cursor.fetchone()
        sequence_number = int(data[0]) + 1
        cursor.execute("update sequence set sequence_number =" + str(sequence_number) + " where client='general'")
        self.connection.commit()
        header_string = 'ISA*00*          *00*          *ZZ*GPALOGISTICS   *ZZ*WAPPLIANCE     *' + datetime.now().strftime("%y%m%d") + '*' + datetime.now().strftime("%H%M") + '*X*00401*' + str(sequence_number) + '*0*P*>~' \
                        'GS*SW*GPALOGISTICS*WAPPLIANCE*' + datetime.now().strftime("%Y%m%d") + '*' + datetime.now().strftime("%H%M") + '*' + str(sequence_number)[-4:] + '*X*004010~' \
                        'ST*945*1001~' \
                        'W06*N*' + depositor_order_number + '*' + datetime.now().strftime("%Y%m%d") + '*' + str(shipment_id) + '**' + str(purchase_order_number) + '~' \
                        'N1*ST*' + ship_to_name + '*92*' + ship_to_code + '~' \
                        'N3*' + ship_to_address1 + '~' \
                        'N4*' + ship_to_city + '*' + ship_to_state + '*' + ship_to_zipcode + '*' + ship_to_country + '~' \
                        'N1*SF*GPA*92*SA~' \
                        'N3*' + ship_from_address1 + '~' \
                        'N4*' + ship_from_city + '*' + ship_from_state + '*' + ship_from_zipcode + '*' + ship_from_country + '~' \
                        'N9*23*' + customer_name + '~' \
                        'G62*11*' + ship_date + '~' \
                        'W27*' + transportation_method + '*' + carrier_code + '*' + routing + '~'
        for element in rooted.iter():
            if element.tag == 'ShipmentDetail':
                for ShipmentDetail_child_element in element:
                    if ShipmentDetail_child_element.tag == 'Container':
                        counter = counter + 1
                        style = ''
                        color = ''
                        size = ''
                        for Container_sub_element in ShipmentDetail_child_element:
                            tracking_number = ''
                            tracking_qualifier = ''
                            if Container_sub_element.tag == 'SSCC':
                                sscc = Container_sub_element.text
                                if len(sscc) != 20:
                                    raise Exception("This UCC is invalid as it does not meet the 20 character requirement.")
                            if Container_sub_element.tag == 'TrackingNumber':
                                tracking_number = Container_sub_element.text
                                if tracking_number is not None:
                                    tracking_qualifier = 'CP'
                            if Container_sub_element.tag == 'CaseWeight':
                                case_weight = Container_sub_element.text
                            if Container_sub_element.tag == 'Item':
                                ordered_quantity = ''
                                shipped_quantity = ''
                                case_upc = ''
                                item_number = ''
                                for Item_sub_element in Container_sub_element:
                                    if Item_sub_element.tag == 'OrderLineNumber':
                                        order_line_number = Item_sub_element.text
                                    elif Item_sub_element.tag == 'OrderedQuantity':
                                        ordered_quantity = Item_sub_element.text
                                    elif Item_sub_element.tag == 'ItemNumber':
                                        item_number = Item_sub_element.text
                                        split = item_number.split("-")
                                    elif Item_sub_element.tag == 'ItemUPC':
                                        item_upc = Item_sub_element.text
                                    elif Item_sub_element.tag == 'CaseUPC':
                                        case_upc = Item_sub_element.text
                                    elif Item_sub_element.tag == 'BuyerItemNumber':
                                        BuyerItemNumber = Item_sub_element.text
                                    elif Item_sub_element.tag == 'GTIN':
                                        gtin = Item_sub_element.text
                                    elif Item_sub_element.tag == 'ReceivedQuantity':
                                        received_quantity = Item_sub_element.text
                                    elif Item_sub_element.tag == 'ShippedQuantity':
                                        shipped_quantity = Item_sub_element.text
                                        quantity_difference = int(ordered_quantity) - int(shipped_quantity)
                                    elif Item_sub_element.tag == 'QuantityUnitOfMeasure':
                                        quantity_unit_of_measure = Item_sub_element.text
                                    elif Item_sub_element.tag == 'ItemDescription':
                                        item_description = Item_sub_element.text
                                    elif Item_sub_element.tag == 'ProductGroup':
                                        product_group = Item_sub_element.text
                                    elif Item_sub_element.tag == 'AlternateItemNumber':
                                        alternate_item_number = Item_sub_element.text
                                    elif Item_sub_element.tag == 'LotNumber':
                                        lot_number = Item_sub_element.text
                                    elif Item_sub_element.tag == 'SKU':
                                        sku = Item_sub_element.text
                                    elif Item_sub_element.tag == 'Color':
                                        color = Item_sub_element.text
                                    elif Item_sub_element.tag == 'Style':
                                        style = Item_sub_element.text
                                    elif Item_sub_element.tag == 'Size':
                                        size = Item_sub_element.text
                                    elif Item_sub_element.tag == 'E57':
                                        if Item_sub_element.text == None:
                                            label_code = ''
                                        else:
                                            label_code = Item_sub_element.text
                                    elif Item_sub_element.tag == 'ProductType':
                                        product_type = Item_sub_element.text
                                    elif Item_sub_element.tag == 'ItemLength':
                                        item_length = Item_sub_element.text
                                    elif Item_sub_element.tag == 'ItemWidth':
                                        item_width = Item_sub_element.text
                                    elif Item_sub_element.tag == 'ItemHeight':
                                        item_height = Item_sub_element.text
                                    elif Item_sub_element.tag == 'PackQuantity':
                                        pack_quantity = Item_sub_element.text
                                    elif Item_sub_element.tag == 'InnerPackQuantity':
                                        inner_pack_quantity = Item_sub_element.text
                                    elif Item_sub_element.tag == 'PackSize':
                                        pack_size = Item_sub_element.text
                                    elif Item_sub_element.tag == 'PackSizeUnitOfMeasure':
                                        pack_size_unit_of_measure = Item_sub_element.text
                                    elif Item_sub_element.tag == 'PackWeight':
                                        pack_weight = Item_sub_element.text
                                    elif Item_sub_element.tag == 'PackWeightUnitOfMeasure':
                                        detail_pack_weight_unit_of_measure = Item_sub_element.text
                                    elif Item_sub_element.tag == 'PurchaseOrderNumber':
                                        detail_purchase_order_number = Item_sub_element.text
                                    elif Item_sub_element.tag == 'PackVolume':
                                        pack_volume = Item_sub_element.text
                                    elif Item_sub_element.tag == 'PackVolumeUnitOfMeasure':
                                        pack_volume_unit_of_measure = Item_sub_element.text
                                # Generating dynamic values with if statement for tracking number conditional.
                                if label_code == '':
                                    body_string = 'LX*' + str(order_line_number) + '~' \
                                                  'MAN*CP*' + str(sscc) + '~' \
                                                  'W12*CL*' + str(ordered_quantity) + '*' + str(shipped_quantity) + '*VN*' + str(item_number) + '~' \
                                                  'G69*' + str(item_description) + '~'
                                    segment_count = counter * 4
                                header_string = header_string + body_string
        segment_count = segment_count + 13
        footer_string = 'W03*' + str(total_quantity_shipped) + '*' + str(total_shipment_weight) + '*LB~' \
                        'SE*' + str(segment_count) + '*1001~' \
                        'GE*1*' + str(sequence_number)[-4:] + '~' \
                        'IEA*1*' + str(sequence_number) + '~'
        completed_string = header_string + footer_string
        with open(self.path + "Out\\" + self.transaction_number + "_" + self.client_id + "_" + str(depositor_order_number)
                  + "_" + datetime.now().strftime("%Y%m%d%H%M%S" + ".txt"), "w") as acknowledgement_file:
            acknowledgement_file.write(completed_string)
        with open(self.path + "Out\\Archive\\" + self.transaction_number + "\\" + self.transaction_number + "_" +
                  self.client_id + "_" + str(depositor_order_number) + "_" + datetime.now().strftime("%Y%m%d%H%M%S" + ".txt"),
                  "w") as acknowledgement_file:
            acknowledgement_file.write(completed_string)
