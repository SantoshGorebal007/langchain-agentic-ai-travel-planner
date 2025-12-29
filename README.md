
# Travel AI Agent

![Travel AI Agent Banner](https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1200&q=80)

> **A smart, modular travel assistant powered by AI.**

---

## ✈️ Project Overview
Travel AI Agent is a Python-based assistant that helps users plan trips, discover places, estimate budgets, and get real-time information about flights, hotels, weather, and more. It is designed with modularity, extensibility, and data privacy in mind.

---

## 📁 Project Structure

```
travel ai agent/
├── .env                  # Environment variables (not tracked)
├── .gitignore            # Git ignore rules
├── README.md             # Project documentation
├── requirements.txt      # Python dependencies
├── conftest.py           # Pytest configuration
├── test_groq.py          # LLM test
├── test_llm.py           # LLM test
├── data/                 # Sample data (flights, hotels, places)
├── docs/                 # Project requirements and docs
├── src/                  # Source code
│   ├── config.py         # Configuration
│   ├── data_loader.py    # Data loading utilities
│   ├── agent/            # Agent logic and tools registry
│   ├── llm/              # LLM client (Groq)
│   ├── tools/            # Core tools (budget, flight, hotel, etc.)
│   └── utils/            # Utility functions
├── tests/                # Unit tests
└── ...
```

---

## 🧩 Key Features
- **Flight Search**: Find and recommend flights.
- **Hotel Recommender**: Suggest hotels based on preferences.
- **Places Discovery**: Explore attractions and points of interest.
- **Weather Lookup**: Get real-time weather info.
- **Budget Estimator**: Estimate trip costs.
- **Modular Tools**: Easily extend with new tools.
- **LLM Integration**: Uses Groq for natural language understanding.

---

## 🚀 Getting Started

1. **Clone the repository**
	```bash
	git clone <your-repo-url>
	cd travel ai agent
	```
2. **Create a virtual environment**
	```bash
	python -m venv .venv
	.venv\Scripts\activate  # On Windows
	# or
	source .venv/bin/activate  # On macOS/Linux
	```
3. **Install dependencies**
	```bash
	pip install -r requirements.txt
	```
4. **Set up your .env file**
	- Copy `.env.example` to `.env` and fill in your API keys/configs.

5. **Run tests**
	```bash
	pytest
	```

---

## 🗂️ Main Modules

| Module                | Description                        |
|-----------------------|------------------------------------|
| `src/agent/`          | Agent logic, tool registry         |
| `src/agent/tools/`    | Individual tool implementations    |
| `src/llm/`            | LLM client (Groq)                  |
| `src/tools/`          | Core business logic tools          |
| `src/utils/`          | Utility functions                  |
| `data/`               | Sample data (JSON)                 |
| `tests/`              | Unit tests                         |

---

## 🖼️ Visual Overview

<p align="center">
  <img src="https://cdn.dribbble.com/users/63407/screenshots/15472597/media/2e2e2e2e2e2e2e2e2e2e2e2e2e2e2e2e.png" width="600" alt="Travel AI Agent UI Mockup" style="border-radius: 12px; box-shadow: 0 4px 24px rgba(0,0,0,0.12);">
</p>

---

## 🧑‍💻 Contributing

1. Fork the repo
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 🙏 Acknowledgements
- [Unsplash](https://unsplash.com/) for banner images
- [Dribbble](https://dribbble.com/) for UI inspiration
- OpenAI, Groq, and the Python community
