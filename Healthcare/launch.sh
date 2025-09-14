#!/bin/bash

echo "🏥 Starting Healthcare Platform..."

# Start server if not running
if ! pgrep -f "python3.*server.py" > /dev/null; then
    python3 server.py &
    echo "🚀 Server started on port 8080"
    sleep 2
fi

# Launch browser
if command -v google-chrome &> /dev/null; then
    google-chrome http://localhost:8080 &
elif command -v firefox &> /dev/null; then
    firefox http://localhost:8080 &
elif command -v chromium-browser &> /dev/null; then
    chromium-browser http://localhost:8080 &
elif command -v xdg-open &> /dev/null; then
    xdg-open http://localhost:8080 &
else
    echo "✅ Platform running at: http://localhost:8080"
    echo "📱 Open this URL in your browser"
fi

echo "🎯 Healthcare AI Platform launched successfully!"
