from django.test import TestCase


class DailyReportViewTest(TestCase):
    def test_render_creation_form(self):
        # GET リクエストを送信
        response = self.client.get('/daily_report/')

        # ステータスコードが 200 であることを確認
        self.assertEqual(response.status_code, 200)

        # フォーム内に「日付」というテキストが含まれていることを確認
        self.assertContains(response, "日付")
        self.assertContains(response, "タイトル")
        self.assertContains(response, "daily report")