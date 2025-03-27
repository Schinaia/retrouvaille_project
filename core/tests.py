from django.test import TestCase

# Create your tests here.
class HomePageTests(TestCase):
    def home_page_status_code(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        
    def home_page_uses_correct_template(self):
         response = self.client.get("/")
         self.assertTemplateUsed(response, "/core/home.html")
         
from django.core import mail
from django.test import TestCase

class EmailTest(TestCase):
    def test_send_email(self):
        mail.send_mail('Subject here', 'Here is the message.',
            'from@example.com', ['retrouvaille@outlook.com'],
            fail_silently=False)
        print("Mailbox\n", mail.outbox[0].message(), "\n", "_" * 80)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Subject here')
        