# AI Image Generation Platform

A full-stack web application that simulates an AI image generation service with user authentication, credit-based pricing, and Firebase backend.

## 🚀 Features

- **User Registration System**: Secure user signup with Firebase Auth
- **Credit-Based Pricing**: Dynamic pricing based on image generation styles
- **Real-time Validation**: Backend validation prevents credit exploitation
- **Responsive UI**: Clean, modern interface with modal-based signup
- **Firebase Integration**: Serverless backend with Firestore database

## 💰 Pricing Model

| Style | Credits Required |
|-------|------------------|
| Realistic | 1 credit |
| Cartoon | 1 credit |
| Abstract | 1 credit |
| Sketch | 1 credit |
| Digital Art | 2 credits |
| Watercolor | 2 credits |
| Anime | 2 credits |
| Oil Painting | 3 credits |

## 🛠️ Tech Stack

### Frontend
- **HTML5** - Semantic markup structure
- **CSS3** - Modern styling with modals and responsive design
- **Vanilla JavaScript** - Dynamic user interactions and API calls

### Backend
- **Firebase Functions** - Serverless Python functions
- **Firestore** - NoSQL database for user data and credits
- **Firebase Auth** - User authentication and management

### Development
- **Firebase Emulators** - Local development environment
- **Git** - Version control

## 📁 Project Structure

```
Feraset_First_Task/
├── public/                    # Frontend assets
│   ├── index.html            # Main application page
│   ├── script.js             # Client-side JavaScript
│   └── styles.css            # Application styling
├── mertferasetfirst/         # Firebase Functions
│   ├── main.py              # Core business logic
│   └── requirements.txt     # Python dependencies
├── firebase.json            # Firebase configuration
├── .firebaserc             # Firebase project settings
└── README.md               # Project documentation
```

## 🔧 Setup & Installation

### Prerequisites
- Node.js and npm
- Python 3.13+
- Firebase CLI
- Git

### Local Development

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Feraset_First_Task
   ```

2. **Install Firebase CLI**
   ```bash
   npm install -g firebase-tools
   ```

3. **Login to Firebase**
   ```bash
   firebase login
   ```

4. **Set up Python environment**
   ```bash
   cd mertferasetfirst
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

5. **Start Firebase Emulators**
   ```bash
   firebase emulators:start
   ```

6. **Access the application**
   - Frontend: http://localhost:5000
   - Firebase UI: http://localhost:4000

## 🏗️ Architecture

### Backend Functions

#### `register_this_user`
- **Purpose**: Creates new user accounts
- **Input**: Username and password
- **Output**: User ID and success status
- **Features**: 
  - Input validation
  - Automatic credit allocation (50 credits)
  - Timestamp tracking

#### `create_fake_image_url`
- **Purpose**: Generates fake image URLs with credit validation
- **Input**: User ID, image prompt, style choice
- **Output**: Fake image URL and remaining credits
- **Features**:
  - Credit balance verification
  - Style-based pricing enforcement
  - Atomic credit deduction
  - Prevention of negative credit exploitation

### Frontend Features

#### User Authentication
- Modal-based signup form
- Form validation and error handling
- Automatic session management

#### Image Generation Interface
- Text input for image prompts
- Style selection dropdown
- Real-time feedback and error messages
- Generated URL display

## 🔒 Security Features

### Credit System Protection
- **Balance Validation**: Ensures users have sufficient credits before processing
- **Atomic Transactions**: Prevents race conditions in credit deduction
- **Input Sanitization**: Validates all user inputs on the backend
- **Error Handling**: Comprehensive error messages for better UX

### Authentication
- Firebase Auth integration for secure user management
- UID-based user identification
- Session management and validation

## 🚀 Deployment

### Firebase Hosting Deployment

1. **Build and deploy**
   ```bash
   firebase deploy
   ```

2. **Deploy specific services**
   ```bash
   firebase deploy --only hosting,functions
   ```

## 🎯 Key Business Logic

### Credit Validation Algorithm
```python
# Prevent infinite generation exploit
if current_credits < credits_to_deduct:
    raise https_fn.HttpsError(
        code=https_fn.FunctionsErrorCode.FAILED_PRECONDITION,
        message=f"Insufficient credits. You have {current_credits} credits but need {credits_to_deduct} for {style} style."
    )
```

### Dynamic Pricing Implementation
The system uses a style-to-credit mapping that can be easily modified for business requirements:
- Simple styles (realistic, cartoon): 1 credit
- Medium complexity (digital art, anime): 2 credits  
- Complex styles (oil painting): 3 credits

## 🧪 Testing

### Local Testing with Emulators
- Functions run locally with hot reload
- Firestore emulator for database operations
- Complete development environment without production impact

### Manual Testing Scenarios
1. User registration flow
2. Credit balance validation
3. Image generation with various styles
4. Error handling for insufficient credits

## 📝 Technical Decisions

### Why Firebase?
- **Serverless Architecture**: No infrastructure management
- **Scalability**: Automatic scaling based on demand
- **Real-time Database**: Instant updates for credit balances
- **Authentication**: Built-in user management

### Why Python for Backend?
- **Readability**: Clear business logic implementation
- **Firebase SDK**: Native Python support for Firebase Functions
- **Error Handling**: Comprehensive exception management

### Why Vanilla JavaScript?
- **Performance**: No framework overhead
- **Simplicity**: Direct DOM manipulation for targeted features
- **Learning**: Demonstrates core JavaScript skills

## 🔮 Future Enhancements

- **Payment Integration**: Stripe/PayPal for credit purchases
- **Image Storage**: Actual image generation and storage
- **User Dashboard**: Credit history and usage analytics
- **Admin Panel**: User management and system monitoring
- **Rate Limiting**: API call throttling for abuse prevention

## 📞 Contact

**Mert Demir**  
Software Developer  
[Your contact information]

---

*This project was developed as a technical demonstration of full-stack development skills, focusing on secure backend architecture, user experience design, and scalable cloud deployment.*
