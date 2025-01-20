from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
from PyQt5.QtCore import Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # إعداد نافذة التطبيق
        self.setWindowTitle("Recycling App")
        self.setWindowIcon(QIcon("recyclingproduct.ico"))  # أيقونة مخصصة

        # إنشاء عنصر لعرض الويب
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://mohamedboukerche22.github.io/keep_it_clean2/"))  # تحويل الرابط إلى QUrl

        # إعداد تخطيط النافذة
        layout = QVBoxLayout()
        layout.addWidget(self.browser)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # السماح بتغيير الحجم:
        self.setMinimumSize(800, 600)  # تعيين الحد الأدنى للحجم (اختياري)
        self.setWindowState(self.windowState() | Qt.WindowMaximized)  # فتح النافذة في وضع ملء الشاشة عند البداية (اختياري)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
