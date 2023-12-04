from datetime import date, datetime
import smtplib, ssl
import os
import xml.etree.ElementTree as et


class create_notification_940:

    def __init__(self, formatted_segments, file):
        self.formatted_segments = formatted_segments
        self.file = file

    def parse_edi_email(self, formatted_segments, file):

        # SMTP Server Settings
        smtp_server = "smtp.office365.com"
        port = 587
        sender = "noreply@gpalogisticsgroup.com"
        recipients = ["Equitybrands@gpalogisticsgroup.com", "avelazquez@gpalogisticsgroup.com", "gpaops20@gpalogisticsgroup.com"]
        password = "Turn*17300"

        # variables specific to the translation
        count = 0
        body_text = ""
        for seg in formatted_segments:
            if seg[0] == "W05":
                depositor_order_number = seg[2]
                purchase_order_number = seg[3]
            if seg[0] == "N1" and seg[1] == "Z7":
                mark_for_name = seg[2]
            if seg[0] == "N1" and seg[1] == "BY":
                customer_name = seg[4]
            if seg[0] == "G62" and seg[1] == "10":
                ship_date = seg[2]
                ship_date = '/'.join([ship_date[4:6], ship_date[6:], ship_date[:4]])
            if seg[0] == "W76":
                quantity = seg[1]
            if seg[0] == "SE":
                count = count + 1
                body_text = body_text + str(customer_name) + "          " + str(purchase_order_number) + "             " + str(ship_date) + "            " + str(depositor_order_number) + "            " + str(quantity) + "\n"
        # Creating a secure SSL socket
        context = ssl.create_default_context()

        # Email Content
        Subject = "GPA Logistics Equity Brands Pickticket Upload: " + datetime.now().strftime(
            "%m/%d/%Y %H:%M:%S")
        Text = "Uploaded " + str(count) + " Picktickets for Equity Brands" + "\n" + "\n" + "From File: " + str(
            file) + "\n" + "\n" + "CONSIGNEE           PO NUM          REQUESTED SHIPDATE          PICKTICKET          QTY" + "\n" + "\n" + body_text

        Body = "\r\n".join((
            "From: %s" % sender,
            "To: %s" % recipients,
            "Subject: %s" % Subject,
            "",
            Text
        ))

        try:
            server = smtplib.SMTP(smtp_server, port)
            server.ehlo()
            server.starttls(context=context)
            server.ehlo()
            server.login(sender, password)
            server.sendmail(sender, recipients, Body)
        except Exception as e:
            print(e)
        finally:
            server.quit()
