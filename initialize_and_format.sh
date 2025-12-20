#!/bin/bash

if [ ! -d "img" ]; then
    mkdir -p "img"
    touch "img/.gitkeep"
fi


for i in {1..16}; do
    folder=$(printf "%02d" $i)
    

    if [ ! -d "$folder" ]; then
        mkdir -p "$folder"
    fi
    
    if [ -d "$folder" ]; then
        pushd "$folder" > /dev/null
        
        files_exist=false
        for item in * .*; do
            # Skip . and ..
            [[ "$item" == "." || "$item" == ".." ]] && continue
            # Skip img directory and .gitkeep
            [[ "$item" == "img" || "$item" == ".gitkeep" ]] && continue
            files_exist=true
            break
        done
        
        if ! $files_exist; then
            touch .gitkeep
        else
            [ -f ".gitkeep" ] && rm .gitkeep
        fi
        
        if [ ! -e "img" ]; then
            ln -sf "../img" "img"
        fi
        
        popd > /dev/null
    fi
done

echo "Folder structure created"

if [ -f ".venv/bin/activate" ]; then
    source ".venv/bin/activate"
    if [ $? -ne 0 ]; then
        echo "Failed to activate virtual environment"
        read -p "Press enter to continue..."
        exit 1
    fi
else
    echo "Virtual environment not found at .venv/"
    read -p "Press enter to continue..."
    exit 1
fi

if ! python -c "import autopep8" > /dev/null 2>&1; then
    pip install autopep8 > /dev/null 2>&1
    if [ $? -ne 0 ]; then
        echo "Failed to install autopep8"
        read -p "Press enter to continue..."
        exit 1
    fi
fi

find . -name "*.py" -not -path "./.venv/*" -not -path "./.venv" | while read -r file; do
    echo "Formatting: $file"
    python -m autopep8 --in-place --aggressive --aggressive "$file"
done

echo "All Python files formatted"

read -p "Press enter to continue..."