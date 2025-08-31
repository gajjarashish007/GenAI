# Blog Post Image Specifications

This document provides detailed specifications for all images and diagrams needed for the dev.to blog post "Converting IAM Users to Roles: A Complete Web-Based Solution".

## Cover Image (IMAGE_PLACEHOLDER_COVER)
**Dimensions:** 1000x420px
**Description:**
- Modern, professional design with AWS branding colors (orange/blue)
- Title text: "Converting IAM Users to Roles"
- Subtitle: "Complete Web-Based Solution"
- Visual elements: AWS IAM icons, user-to-role transformation arrows
- Background: Gradient from AWS orange to blue
- Include AWS logo and IAM service icon

## Hero Image (IMAGE_PLACEHOLDER_HERO)
**Dimensions:** 800x400px
**Description:**
- Screenshot of the main web interface showing:
  - Left panel: List of IAM users with search functionality
  - Right panel: Role configuration form with trust policy templates
  - Bottom panel: Conversion preview and progress area
- Clean, modern UI with AWS-inspired styling
- Show sample data (anonymized user names like "user-1", "user-2")
- Highlight key features with subtle annotations

## Architecture Diagram (IMAGE_PLACEHOLDER_ARCHITECTURE)
**Dimensions:** 800x500px
**Description:**
- System architecture showing three main layers:
  1. **Frontend Layer**: Web browser with modern UI components
  2. **Backend Layer**: Python Flask server with authentication
  3. **AWS Layer**: IAM services and APIs
- Connection arrows showing data flow between layers
- Include icons for:
  - Web browser (Chrome/Firefox icon)
  - Python logo
  - AWS services (IAM, STS, CloudTrail)
- Color coding: Frontend (blue), Backend (green), AWS (orange)
- Add security indicators (locks, shields) for secure connections

## User Discovery Interface (IMAGE_PLACEHOLDER_USER_DISCOVERY)
**Dimensions:** 700x450px
**Description:**
- Screenshot of the user discovery panel showing:
  - Searchable list of IAM users
  - User details including creation date, last activity
  - Policy attachments (managed and inline)
  - Security indicators (MFA status, access key age)
- Sample users with realistic but anonymized data
- Highlight search functionality and filtering options
- Show user selection state with visual feedback

## Role Configuration Interface (IMAGE_PLACEHOLDER_ROLE_CONFIG)
**Dimensions:** 700x500px
**Description:**
- Role configuration form showing:
  - Role name input field (auto-populated)
  - Description text area
  - Trust policy template selector with options:
    * EC2 Service Role
    * Lambda Execution Role
    * ECS Task Role
    * Cross-Account Role
    * Custom Template
  - Trust policy JSON editor with syntax highlighting
- Show validation indicators (green checkmarks, red error icons)
- Include tooltips and help text

## Role Management Tabs (IMAGE_PLACEHOLDER_ROLE_TABS)
**Dimensions:** 800x600px
**Description:**
- Tabbed interface showing all management tabs:
  - Role Management (active tab)
  - Managed Policies
  - Inline Policies
  - Trust Policy
  - Policy Simulator
  - Analytics
  - Bulk Operations
  - Audit & Compliance
- Show content of the active tab with role selection dropdown
- Visual indicators for tab states (active, inactive, modified)
- Modern tab design with icons and labels

## Policy Simulator Interface (IMAGE_PLACEHOLDER_SIMULATOR)
**Dimensions:** 700x500px
**Description:**
- Policy simulator showing:
  - Action input field (e.g., "s3:GetObject")
  - Resource ARN input (e.g., "arn:aws:s3:::bucket/*")
  - Context keys section
  - Simulation results with Allow/Deny decisions
  - Detailed reasoning panel
- Color-coded results (green for Allow, red for Deny)
- Show sample simulation with realistic AWS actions

## Analytics Dashboard (IMAGE_PLACEHOLDER_ANALYTICS)
**Dimensions:** 800x500px
**Description:**
- Analytics dashboard with multiple widgets:
  - Role usage frequency chart (bar chart)
  - Permission utilization pie chart
  - Security risk indicators (gauges)
  - Recent activity timeline
  - Recommendations panel
- Use professional dashboard styling with cards/widgets
- Include sample data showing realistic usage patterns
- Color scheme: blues and greens for positive metrics, orange/red for warnings

## IAM Permissions Diagram (IMAGE_PLACEHOLDER_PERMISSIONS)
**Dimensions:** 600x400px
**Description:**
- Visual representation of required IAM permissions:
  - Central IAM user/role icon
  - Radiating arrows to different AWS services
  - Permission categories grouped by color:
    * User Management (blue)
    * Role Management (green)
    * Policy Management (orange)
    * Monitoring (purple)
- Include permission names as labels
- Use AWS service icons where applicable

## AWS Authentication Options (IMAGE_PLACEHOLDER_AUTH)
**Dimensions:** 700x300px
**Description:**
- Three authentication methods side by side:
  1. **AWS CLI**: Terminal window showing "aws configure"
  2. **Environment Variables**: Code snippet with export commands
  3. **IAM Roles**: EC2 instance with attached role icon
- Each method with pros/cons or use case descriptions
- Visual flow arrows showing credential flow
- Include security best practice indicators

## Login Interface (IMAGE_PLACEHOLDER_LOGIN)
**Dimensions:** 500x400px
**Description:**
- Clean login form showing:
  - Username field (filled with "admin")
  - Password field (masked)
  - Login button
  - Security features list on the side
- Modern form design with AWS branding
- Include security icons (shield, lock)
- Show session management features

## Discovery Phase Interface (IMAGE_PLACEHOLDER_DISCOVERY)
**Dimensions:** 800x500px
**Description:**
- Multi-panel view showing discovery process:
  - User inventory panel with statistics
  - Risk assessment panel with color-coded users
  - Dependency mapping showing user-to-service connections
  - Planning checklist with progress indicators
- Use dashboard-style layout with cards
- Include progress bars and completion indicators

## Conversion Process Interface (IMAGE_PLACEHOLDER_CONVERSION)
**Dimensions:** 800x600px
**Description:**
- Step-by-step conversion interface showing:
  - Progress stepper (5 steps) with current step highlighted
  - Main content area showing current step details
  - Preview panel with conversion summary
  - Action buttons (Previous, Next, Convert)
  - Real-time progress bar during conversion
- Show step 4 (Preview) as active step
- Include validation checkmarks and warnings

## Post-Conversion Management (IMAGE_PLACEHOLDER_POST_CONVERSION)
**Dimensions:** 700x500px
**Description:**
- Post-conversion dashboard showing:
  - Conversion summary statistics
  - Role validation checklist
  - Application testing status
  - Monitoring setup progress
- Success indicators and next steps
- Include links to role management features
- Show completion percentages and status icons

## Bulk Operations Interface (IMAGE_PLACEHOLDER_BULK)
**Dimensions:** 800x500px
**Description:**
- Bulk operations panel showing:
  - Multi-select role list with checkboxes
  - Bulk action dropdown (Attach Policy, Update Trust Policy, etc.)
  - Progress tracking for bulk operations
  - Results summary with success/failure counts
- Show operation in progress with progress bars
- Include batch size and estimated completion time

## Audit Interface (IMAGE_PLACEHOLDER_AUDIT)
**Dimensions:** 700x500px
**Description:**
- Audit and compliance dashboard showing:
  - Change history timeline
  - Compliance status indicators
  - Audit report generation options
  - Export functionality
- Professional audit trail styling
- Include timestamps, user attribution, and change details
- Show compliance score or status indicators

## Security Best Practices Diagram (IMAGE_PLACEHOLDER_SECURITY)
**Dimensions:** 800x400px
**Description:**
- Security principles visualization:
  - Central security shield icon
  - Four quadrants showing:
    * Least Privilege (minimal permissions icon)
    * Separation of Duties (role segregation)
    * Regular Reviews (calendar/audit icon)
    * Monitoring (dashboard/alert icons)
- Professional security-focused design
- Use security-related icons and colors (blues, greens)

## Troubleshooting Interface (IMAGE_PLACEHOLDER_TROUBLESHOOTING)
**Dimensions:** 700x400px
**Description:**
- Troubleshooting panel showing:
  - Common issues list with expandable solutions
  - System status indicators (green/red lights)
  - Diagnostic tools section
  - Log viewer with error highlighting
- Problem-solution format with clear visual hierarchy
- Include status indicators and resolution steps

## Performance Metrics (IMAGE_PLACEHOLDER_PERFORMANCE)
**Dimensions:** 600x400px
**Description:**
- Performance dashboard showing:
  - Response time charts
  - Throughput metrics
  - Resource utilization graphs
  - Optimization recommendations
- Technical dashboard styling with charts and graphs
- Use performance-focused color scheme (greens for good, yellows/reds for issues)

## Call to Action (IMAGE_PLACEHOLDER_CTA)
**Dimensions:** 600x200px
**Description:**
- Compelling call-to-action banner:
  - "Get Started Today" prominent text
  - Download/GitHub buttons
  - Key benefits bullet points
  - Contact information or links
- Action-oriented design with contrasting colors
- Include relevant icons (download, GitHub, contact)

## General Design Guidelines

### Color Palette
- **Primary**: AWS Orange (#FF9900)
- **Secondary**: AWS Blue (#232F3E)
- **Success**: Green (#28a745)
- **Warning**: Yellow (#ffc107)
- **Danger**: Red (#dc3545)
- **Info**: Light Blue (#17a2b8)

### Typography
- **Headers**: Clean, modern sans-serif (Arial, Helvetica)
- **Body**: Readable sans-serif
- **Code**: Monospace font (Courier, Monaco)

### Icons
- Use consistent icon style (outline or filled)
- AWS service icons where applicable
- Security icons (shields, locks, keys)
- UI icons (arrows, checkmarks, warnings)

### Layout Principles
- Clean, uncluttered design
- Consistent spacing and alignment
- Clear visual hierarchy
- Responsive design considerations
- Accessibility compliance (color contrast, alt text)

### Image Quality
- High resolution (at least 2x for retina displays)
- Optimized file sizes for web
- Consistent styling across all images
- Professional appearance suitable for technical blog

### Annotations and Labels
- Clear, readable text overlays
- Consistent annotation style
- Minimal but informative labels
- Non-intrusive highlighting and callouts
