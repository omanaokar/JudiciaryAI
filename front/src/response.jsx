function Response({ responseQuery} ) {
    if (!responseQuery || responseQuery.length === 0) {
      // If responseQuery is null or empty, don't render anything
      return <></>;
    }
  
    return (
      <>
        {responseQuery.map((individualResponse) => (
          // Check if the query exists before rendering the response
          individualResponse.query ? (
            <div key={individualResponse.id} className="response-container">
              {/* Query aligned to the right */}
              <div className="queryText">
                {individualResponse.query}
              </div>
              
              {/* Response aligned to the left */}
              <div className="optionsButBig">
                <div className="descriptionText">
                <div dangerouslySetInnerHTML={{ __html: individualResponse.response }} />
                </div>
              </div>
            </div>
          ) : null // Render nothing if query is not present
        ))}
      </>
    );
  }
  
  export default Response;
  