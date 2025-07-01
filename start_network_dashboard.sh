#!/bin/bash
echo ""
echo "Transforming data to long format..."
python excel_to_csv.py
echo "=================================="

# Quick Network Dashboard Launcher
echo "🌐 Starting Network-Accessible MQL Dashboard..."
echo "=================================="

# Get IP address
IP=$(python3 -c "
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('8.8.8.8', 80))
print(s.getsockname()[0])
s.close()
")

echo "🖥️  Your IP Address: $IP"
echo "📡 Access URLs:"
echo "   🏠 Local:   http://localhost:8501"
echo "   🌐 Network: http://$IP:8501"
echo ""
echo "🔗 Share this URL with others on your network:"
echo "   http://$IP:8501"
echo ""
echo "⏹️  Press Ctrl+C to stop the dashboard"
echo "=================================="

# Launch streamlit with network access
streamlit run streamlit_dashboard.py --server.address 0.0.0.0 --server.port 8501
