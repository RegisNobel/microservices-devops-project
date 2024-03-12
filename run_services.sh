#!/bin/bash

# Variables
PYTHON="python3"
FRONTEND_SERVICE="frontend_service/app.py"
AUTO_MAIL_SERVICE="auto_mail_service/app.py"
STORAGE_SERVICE="storage_service/app.py"
PID_FILE="service_pids.txt"


# Function to run services
run_services() {
    # Run frontend service
    $PYTHON $FRONTEND_SERVICE &
    FRONTEND_PID=$!
    echo $FRONTEND_PID > $PID_FILE
    echo "Frontend service started (PID: $FRONTEND_PID)"

    # Run database service
    $PYTHON $DATABASE_SERVICE &
    DATABASE_PID=$!
    echo $DATABASE_PID >> $PID_FILE
    echo "Database service started (PID: $DATABASE_PID)"

    # Run auto mail service
    $PYTHON $AUTO_MAIL_SERVICE &
    AUTO_MAIL_PID=$!
    echo $AUTO_MAIL_PID >> $PID_FILE
    echo "Auto mail service started (PID: $AUTO_MAIL_PID)"
}

# Function to stop services
stop_services() {
    if [ -f "$PID_FILE" ]; then
        while read PID; do
            # Check if the process is running
            if kill -0 $PID 2>/dev/null; then
                kill $PID
                echo "Service stopped (PID: $PID)"
            else
                echo "No such process (PID: $PID), might have already been stopped."
            fi
        done < $PID_FILE
        rm $PID_FILE
    else
        echo "No PID file found. Are the services running?"
    fi
}

# Main script
case "$1" in
    start)
        run_services
        ;;
    stop)
        stop_services
        ;;
    *)
        echo "Usage: $0 {start|stop}"
        exit 1
esac