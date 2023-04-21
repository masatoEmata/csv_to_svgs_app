import csv
import io

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_upload_csv_file():
    csv_rows = [["test1", "test2", "test3"]]
    csv_content = io.StringIO()
    csv_writer = csv.writer(csv_content)
    csv_writer.writerows(csv_rows)
    csv_content.seek(0)

    response = client.post(
        "/upload",
        files={"csv_file": ("test.csv", csv_content.getvalue(), "text/csv")},
    )

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/zip"
