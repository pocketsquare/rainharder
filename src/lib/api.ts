// API helper functions using environment variables

// Access public environment variables
const apiUrl = import.meta.env.PUBLIC_API_URL;

/**
 * Fetch data from the API
 * @param endpoint The API endpoint to fetch from
 * @returns The fetched data
 */
export async function fetchData(endpoint: string) {
  try {
    const response = await fetch(`${apiUrl}/${endpoint}`);
    
    if (!response.ok) {
      throw new Error(`API error: ${response.status}`);
    }
    
    return await response.json();
  } catch (error) {
    console.error('API fetch error:', error);
    throw error;
  }
}