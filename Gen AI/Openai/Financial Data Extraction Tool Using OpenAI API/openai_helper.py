import openai
from secret_key import openai_key
import json
import pandas as pd
import openai.error  # To handle OpenAI API errors

# Set the OpenAI API key
openai.api_key = openai_key

def extract_financial_data(text):
    # Prompt to extract financial data
    prompt = get_prompt_financial() + text
    
    try:
        # Call to the OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        
        # Extract the content from the response
        content = response['choices'][0]['message']['content']
       
        # Try to parse the response into JSON
        try:
            data = json.loads(content)
            return pd.DataFrame(data.items(), columns=["Measure", "Value"])

        except json.JSONDecodeError:
            print("Error in parsing the response. The response was not in valid JSON format.")
    
    # Handle OpenAI API errors
    except openai.error.RateLimitError:
        print("Rate limit exceeded. Please check your API usage or upgrade your plan.")
    except openai.error.InvalidRequestError as e:
        print(f"Invalid request: {e}")
    except openai.error.APIConnectionError:
        print("Network error. Please check your internet connection and try again.")
    except openai.error.OpenAIError as e:
        print(f"An error occurred: {e}")

    # Return an empty DataFrame with appropriate columns if an error occurs
    return pd.DataFrame({
        "Measure": ["Company Name", "Stock Symbol", "Revenue", "Net Income", "EPS"],
        "Value": ["", "", "", "", ""]
    })

def get_prompt_financial():
    # Financial data prompt template
    return '''Please retrieve company name, revenue, net income and earnings per share (a.k.a. EPS)
    from the following news article. If you can't find the information from this article 
    then return "". Do not make things up.    
    Then retrieve a stock symbol corresponding to that company. For this you can use
    your general knowledge (it doesn't have to be from this article). Always return your
    response as a valid JSON string. The format of that string should be this, 
    {
        "Company Name": "Walmart",
        "Stock Symbol": "WMT",
        "Revenue": "12.34 million",
        "Net Income": "34.78 million",
        "EPS": "2.1 $"
    }
    News Article:
    ============

    '''

if __name__ == '__main__':
    # Test with a sample news article
    text = '''
    Tesla's Earning news in text format: Tesla's earning this quarter blew all the estimates. They reported 4.5 billion $ profit against a revenue of 30 billion $. Their earnings per share was 2.3 $
    '''
    
    # Call the function to extract financial data
    df = extract_financial_data(text)

    # Print the result in DataFrame format
    print(df.to_string())
