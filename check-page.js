const http = require('http');

const options = {
  hostname: 'localhost',
  port: 4321,
  path: '/index3',
  method: 'GET'
};

const req = http.request(options, (res) => {
  let data = '';
  
  res.on('data', (chunk) => {
    data += chunk;
  });
  
  res.on('end', () => {
    // Check for testimonials content
    const hasTestimonials = data.includes('Kyle M.');
    const hasInstructors = data.includes('George Digweed MBE');
    const hasFeatures = data.includes('Patented Laser Technology');
    
    console.log('Page length:', data.length);
    console.log('Has testimonials content:', hasTestimonials);
    console.log('Has instructor content:', hasInstructors);
    console.log('Has features content:', hasFeatures);
    
    // Look for the testimonial section
    const testimonialMatch = data.match(/testimonials-section[\s\S]{0,500}/);
    if (testimonialMatch) {
      console.log('\nTestimonial section preview:');
      console.log(testimonialMatch[0].substring(0, 200) + '...');
    }
    
    // Check for errors
    if (data.includes('Error') || data.includes('error')) {
      console.log('\nFound error in page!');
      const errorMatch = data.match(/[Ee]rror[\s\S]{0,200}/);
      if (errorMatch) {
        console.log(errorMatch[0]);
      }
    }
  });
});

req.on('error', (e) => {
  console.error(`Problem with request: ${e.message}`);
});

req.end();