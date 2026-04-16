import http.server
import socketserver
import json
import os

PORT = 3000
LEADS_FILE = 'leads.json'

REVIEWS_FILE = 'reviews.json'

DEFAULT_REVIEWS = [
    {
        "name": "Rahul S.",
        "program": "Weight Training",
        "rating": 5,
        "text": "Unique Fitness has completely transformed my lifestyle. The trainers are incredibly knowledgeable and the equipment is top-notch. Highly recommended!",
        "initial": "R"
    },
    {
        "name": "Priya M.",
        "program": "Zumba Enthusiast",
        "rating": 5,
        "text": "The Zumba classes here are so energetic and fun! It never feels like a workout. The gym is very clean and the staff is extremely friendly.",
        "initial": "P"
    },
    {
        "name": "Amit K.",
        "program": "Personal Training",
        "rating": 4,
        "text": "I joined for personal training and the results are amazing. My trainer crafted a perfect diet and workout plan. Great atmosphere overall.",
        "initial": "A"
    },
    {
        "name": "Sneha R.",
        "program": "Yoga & Core",
        "rating": 5,
        "text": "The ambiance is fantastic and the yoga instructors really pay attention to form. Definitely the best gym in Bhubaneswar!",
        "initial": "S"
    }
]

if not os.path.exists(REVIEWS_FILE):
    with open(REVIEWS_FILE, 'w') as f:
        json.dump(DEFAULT_REVIEWS, f, indent=4)

class FitnessHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/api/reviews':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            with open(REVIEWS_FILE, 'r') as f:
                self.wfile.write(f.read().encode('utf-8'))
        else:
            super().do_GET()

    def do_POST(self):
        if self.path == '/api/leads' or self.path == '/api/reviews':
            content_length = int(self.headers.get('Content-Length', 0))
            if content_length == 0:
                self.send_response(400)
                self.end_headers()
                return

            post_data = self.rfile.read(content_length)
            
            try:
                data = json.loads(post_data.decode('utf-8'))
            except Exception:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b'{"error": "Invalid JSON"}')
                return

            if self.path == '/api/leads':
                file_path = LEADS_FILE
                target_list = []
                if os.path.exists(file_path):
                    with open(file_path, 'r') as f:
                        try:
                            target_list = json.load(f)
                        except json.JSONDecodeError:
                            pass

                # Check for duplicates
                new_phone = data.get('phone')
                for lead in target_list:
                    if lead.get('phone') == new_phone:
                        self.send_response(400)
                        self.send_header('Content-type', 'application/json')
                        self.end_headers()
                        self.wfile.write(b'{"status": "error", "message": "You have already claimed your free pass!"}')
                        return

                target_list.append(data)
                
            elif self.path == '/api/reviews':
                file_path = REVIEWS_FILE
                target_list = []
                if os.path.exists(file_path):
                    with open(file_path, 'r') as f:
                        try:
                            target_list = json.load(f)
                        except json.JSONDecodeError:
                            pass
                target_list.insert(0, data)

            with open(file_path, 'w') as f:
                json.dump(target_list, f, indent=4)
                
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(b'{"status": "success"}')
        else:
            self.send_response(404)
            self.end_headers()

print(f"Starting Python HTTP Backend on port {PORT}...")
with socketserver.TCPServer(("", PORT), FitnessHandler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
