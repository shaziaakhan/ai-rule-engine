# AI Rule Agent

**AI-enhanced Business Rule Engine** for intelligent validation and decision automation. Combines traditional operator-based rule evaluation with Azure OpenAI-powered semantic understanding.

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

##  Key Features

 **Dual Evaluation Modes**
- **Traditional**: Fast operator-based validation (`eq`, `gt`, `lt`, `contains`, `in`, etc.)
- **AI-Enhanced**: Semantic understanding using Azure OpenAI for intelligent rule interpretation

 **Flexible Rule Definition**
- YAML/JSON-based rules for easy business user editing
- Natural language descriptions for AI-powered evaluation
- No hard-coding required

 **Production-Ready**
- Automatic fallback to traditional evaluation if AI fails
- Batch processing with detailed reporting
- Multiple output formats (JSON, text, table)

 **Easy Integration**
- Plug-and-play design for ETL pipelines, ML workflows, and applications
- Minimal dependencies
- Async support for high-performance scenarios

---

## Installation

```bash
pip install -i https://test.pypi.org/simple/ ai-rule-agent==0.1.1
```

### Requirements
- Python 3.8+
- PyYAML
- semantic-kernel (for AI-enhanced mode)

---

##  Quick Start

### Basic Usage (AI-Enhanced Mode)

```python
from ai_rule_agent import RuleEngine, load_rules

# Load rules from YAML file
rules_data = load_rules("customer_rules.yaml")
ruleset = rules_data.get("ruleset", {}).get("rules", [])

# Sample payload
payload = {
    "Age": 25,
    "CreditScore": 700,
    "AnnualIncome": 500000,
    "Country": "India",
    "KYCStatus": "Verified"
}

# Create AI-enhanced engine
engine = RuleEngine(
    ruleset=ruleset,
    model="gpt-4",
    api_key="your-azure-openai-api-key",
    endpoint="https://your-resource.openai.azure.com/",
    enable_semantic=True
)

# Evaluate rules
results = engine.evaluate(payload)

# Print formatted output
print(engine.format_output(results, format_type="text"))
```

### Traditional Mode (No AI)

```python
from ai_rule_agent import RuleEngine, load_rules

rules_data = load_rules("rules.yaml")
ruleset = rules_data.get("ruleset", {}).get("rules", [])

# Create traditional engine (no AI dependencies)
engine = RuleEngine(
    ruleset=ruleset,
    api_key="",
    model="",
    endpoint="",
    enable_semantic=False
)

results = engine.evaluate(payload)
print(engine.format_output(results, format_type="json"))
```

---

##  Rule Definition

Create a YAML file with your business rules:

```yaml
ruleset:
  name: "Customer Validation Rules"
  rules:
    - field: "Age"
      operator: "gte"
      value: 18
      description: "Customer must be at least 18 years old"

    - field: "CreditScore"
      operator: "gte"
      value: 650
      description: "Credit score should be 650 or higher for approval"

    - field: "Country"
      operator: "in"
      value: ["India", "USA", "UK"]
      description: "Service available only in India, USA, and UK"

    - field: "KYCStatus"
      operator: "eq"
      value: "Verified"
      description: "KYC must be completed and verified"
```

### Supported Operators

| Operator | Description | Example |
|----------|-------------|---------|
| `eq` | Equal to | `"Active"` |
| `not-eq` | Not equal to | `"Inactive"` |
| `gt` | Greater than | `100` |
| `gte` | Greater than or equal | `18` |
| `lt` | Less than | `1000` |
| `lte` | Less than or equal | `500` |
| `contains` | String contains | `"@example.com"` |
| `in` | Value in list | `["A", "B", "C"]` |

---

##  Output Formats

### Text Format (Human-Readable)
```python
print(engine.format_output(results, format_type="text"))
```
```
================================================================================
RULE EVALUATION REPORT
================================================================================

 SUMMARY
--------------------------------------------------------------------------------
  Evaluation Type:  semantic_enhanced
  Total Rules:      4
  Passed:           3 ✓
  Failed:           1 ✗
  Pass Rate:        75.0%

 DETAILED RESULTS
--------------------------------------------------------------------------------

  Rule #1 ✓
    Status:   Pass
    Message:  AI validation: Customer age meets minimum requirement
    Field:    Age
    Expected: 18
    Actual:   25
...
```

### Table Format
```python
print(engine.format_output(results, format_type="table"))
```

### JSON Format
```python
print(engine.format_output(results, format_type="json"))
```



## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Author

**Shazia Khan**
Email: shazia.khan@nihilent.com

---

