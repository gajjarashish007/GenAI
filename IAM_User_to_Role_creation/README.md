# IAM User to Role Converter

A web-based tool for converting AWS IAM Users to IAM Roles with their associated policies and trust relationships.

## 🎯 Purpose

This tool helps you migrate from IAM Users to IAM Roles by:
- Analyzing existing IAM users and their policies
- Creating equivalent IAM roles with appropriate trust policies
- Transferring all attached and inline policies
- Providing a clean, web-based interface for the conversion process

## 🌟 Features

- **🔍 User Discovery**: Browse and search all IAM users in your account
- **📋 Policy Analysis**: View attached managed policies and inline policies
- **🔧 Role Configuration**: Configure role names, descriptions, and trust policies
- **🎨 Trust Policy Templates**: Pre-built templates for common services (EC2, Lambda, ECS)
- **👁️ Conversion Preview**: Preview the conversion before executing
- **🚀 Automated Conversion**: One-click conversion process with progress tracking
- **📥 Export Configuration**: Download conversion configuration as JSON
- **🔄 Real-time Status**: Live connection status and operation logging

## 📁 Files

- `iam_user_to_role.html` - Main web interface
- `iam_conversion_backend.py` - Python backend server
- `launch_iam_converter.sh` - Launcher script with prerequisite checks
- `README.md` - This documentation

## 🔧 Prerequisites

### Required Software
- **Python 3.6+** ✅ (Already installed)
- **boto3** ✅ (Already installed)
- **AWS CLI** (Recommended for credential management)

### AWS Requirements
- **AWS Credentials** configured
- **IAM Permissions** for user and role management

## 🚀 Quick Start

### 1. Launch the Application
```bash
cd /home/ubuntu/iam_create_role
./launch_iam_converter.sh
```

### 2. Open Your Browser
Navigate to: **http://localhost:8081**

### 3. Login to the Application
Use the following credentials to access the tool:
- **Username:** `admin`
- **Password:** `123@admin`

### 4. Convert Users to Roles
1. Select an IAM user from the left panel
2. Configure the target role settings
3. Choose a trust policy template
4. Preview the conversion
5. Execute the conversion

## 🔐 Authentication

The application includes a login system to secure access to IAM operations.

### Default Credentials
- **Username:** `admin`
- **Password:** `123@admin`

### Security Features
- **Session Management**: Login state is maintained during browser session
- **Automatic Logout**: Session expires when browser is closed
- **Manual Logout**: Logout button available in the header
- **Authentication Checks**: All critical operations require authentication

### Customizing Credentials
To change the default credentials, edit the `VALID_CREDENTIALS` dictionary in `iam_conversion_backend.py`:

```python
VALID_CREDENTIALS = {
    'admin': '123@admin',
    'your_username': 'your_password'
}
```

**⚠️ Security Note:** In production environments, implement proper authentication with:
- Encrypted password storage
- Multi-factor authentication
- Session tokens with expiration
- Integration with enterprise identity providers

## ⚙️ Setup Details

### AWS Credentials Configuration

Choose one of these methods to configure AWS credentials:

#### Option A: AWS CLI (Recommended)
```bash
aws configure
```

#### Option B: Environment Variables
```bash
export AWS_ACCESS_KEY_ID=your_access_key_here
export AWS_SECRET_ACCESS_KEY=your_secret_key_here
export AWS_DEFAULT_REGION=us-east-1
```

#### Option C: IAM Roles (EC2 Instance)
If running on EC2, attach an IAM role with appropriate permissions.

### Required IAM Permissions

Your AWS credentials need these permissions:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "iam:ListUsers",
                "iam:GetUser",
                "iam:ListAttachedUserPolicies",
                "iam:ListUserPolicies",
                "iam:GetUserPolicy",
                "iam:GetPolicy",
                "iam:GetPolicyVersion",
                "iam:CreateRole",
                "iam:AttachRolePolicy",
                "iam:PutRolePolicy",
                "sts:GetCallerIdentity"
            ],
            "Resource": "*"
        }
    ]
}
```

## 🖥️ Interface Guide

### Left Panel - IAM Users
- **User List**: Shows all IAM users in your account
- **Search**: Filter users by name
- **User Details**: Click to view policies and configuration
- **Selection**: Selected user is highlighted in blue

### Right Panel - Role Configuration
- **Role Name**: Target role name (auto-populated)
- **Description**: Optional role description
- **Trust Policy Templates**: 
  - **EC2**: For EC2 instances
  - **Lambda**: For Lambda functions
  - **ECS**: For ECS tasks
  - **Custom**: Custom trust policy
- **Policy Preview**: Shows policies that will be copied

### Bottom Panel - Conversion Process
- **Preview**: Shows conversion summary
- **Progress Bar**: Real-time conversion progress
- **Logs**: Detailed operation logs
- **Export**: Download conversion configuration

## 🔄 Conversion Process

### Step 1: User Selection
1. Browse the user list on the left
2. Use the search box to filter users
3. Click on a user to select and load details

### Step 2: Role Configuration
1. **Role Name**: Modify if needed (defaults to `{username}-Role`)
2. **Description**: Add optional description
3. **Trust Policy**: Select template or create custom policy
4. **Policy Review**: Verify policies to be copied

### Step 3: Preview and Convert
1. Click **"👁️ Preview Conversion"** to see summary
2. Review the conversion plan
3. Click **"🔄 Convert to Role"** to execute
4. Monitor progress in real-time
5. Download configuration when complete

## 🎨 Trust Policy Templates

### EC2 Service
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "ec2.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

### Lambda Service
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

### ECS Tasks
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "ecs-tasks.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

### Custom Template
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::ACCOUNT-ID:root"
      },
      "Action": "sts:AssumeRole",
      "Condition": {}
    }
  ]
}
```

## 🔧 Advanced Configuration

### Changing the Port
Edit `iam_conversion_backend.py` and modify the port number:
```python
start_server(8081)  # Change to your desired port
```

### Custom Trust Policies
1. Select "Custom" template
2. Modify the JSON in the trust policy textarea
3. Ensure valid JSON format
4. Include appropriate principals and conditions

### Batch Operations
Currently, the tool processes one user at a time. For batch operations:
1. Use the export feature to save configurations
2. Modify the backend to support batch processing
3. Or run multiple conversions sequentially

## 🛠️ Troubleshooting

### Connection Issues

**❌ Disconnected Status**
- Check AWS credentials: `aws sts get-caller-identity`
- Verify IAM permissions
- Check network connectivity to AWS APIs

### Common Errors

#### "Unable to locate credentials"
```bash
# Solution 1: Configure AWS CLI
aws configure

# Solution 2: Set environment variables
export AWS_ACCESS_KEY_ID=your_key
export AWS_SECRET_ACCESS_KEY=your_secret
export AWS_DEFAULT_REGION=us-east-1
```

#### "Access Denied" errors
- Your AWS user/role needs IAM permissions
- Contact AWS administrator for required permissions
- Check the IAM permissions section above

#### "Port 8081 already in use"
```bash
# Find and kill the process
sudo lsof -ti:8081 | xargs kill -9

# Or change the port in the backend script
```

#### "Role already exists"
- Choose a different role name
- Or delete the existing role if safe to do so
- The tool will not overwrite existing roles

### Validation Errors

#### "Invalid trust policy JSON"
- Check JSON syntax using a JSON validator
- Ensure proper quotes and brackets
- Use the provided templates as reference

#### "No policies found"
- User may not have any attached policies
- Check if user has group memberships
- Verify IAM permissions to read policies

## 📊 Monitoring and Logging

### Real-time Logs
- All operations are logged in the bottom panel
- Color-coded messages:
  - 🟢 **Green**: Success messages
  - 🟡 **Yellow**: Warnings
  - 🔴 **Red**: Errors
  - 🔵 **Blue**: Information

### Progress Tracking
- Visual progress bar shows conversion status
- Step-by-step progress updates
- Completion percentage

### Export Logs
- Download conversion configuration as JSON
- Includes timestamps and operation details
- Useful for audit trails and documentation

## 🔒 Security Considerations

### Credential Security
- Tool runs locally and connects directly to AWS APIs
- No data sent to external servers
- AWS credentials used only for API calls to your account
- Consider using IAM roles instead of access keys

### Permission Principle
- Use least-privilege IAM permissions
- Create dedicated IAM user/role for conversions
- Regularly rotate access keys
- Monitor CloudTrail for API calls

### Role Security
- Review trust policies carefully
- Use specific principals when possible
- Add conditions to trust policies for enhanced security
- Test role assumptions after creation

## 🚀 Best Practices

### Before Conversion
1. **Audit Current Users**: Review user permissions and usage
2. **Plan Role Strategy**: Design role naming and trust policy standards
3. **Test in Non-Production**: Validate the process in a test environment
4. **Backup Configurations**: Export current IAM configurations

### During Conversion
1. **One at a Time**: Convert users individually for better control
2. **Verify Policies**: Review all policies before conversion
3. **Test Role Assumption**: Verify roles work as expected
4. **Document Changes**: Keep records of conversions

### After Conversion
1. **Update Applications**: Modify applications to use roles
2. **Remove Old Users**: Safely remove converted users
3. **Monitor Usage**: Check CloudTrail for role usage
4. **Regular Reviews**: Periodically audit role permissions

## 🔄 Migration Strategy

### Phase 1: Preparation
- Inventory all IAM users
- Document current permissions
- Plan role architecture
- Set up conversion tool

### Phase 2: Conversion
- Convert non-critical users first
- Test role functionality
- Update application configurations
- Monitor for issues

### Phase 3: Cleanup
- Remove converted users
- Update documentation
- Train team on role usage
- Implement ongoing governance

## 📚 Additional Resources

### AWS Documentation
- [IAM Roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html)
- [Trust Policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html)
- [IAM Best Practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)

### Related Tools
- [AWS IAM Browser](../README.md) - For browsing existing IAM resources
- [AWS CLI](https://aws.amazon.com/cli/) - Command-line interface
- [AWS Console](https://console.aws.amazon.com/iam/) - Web-based management

## 🆘 Support

### Getting Help
1. Check this documentation
2. Review troubleshooting section
3. Check browser console for JavaScript errors
4. Check terminal output for Python backend errors
5. Verify AWS credentials and permissions

### Reporting Issues
- Include error messages
- Provide steps to reproduce
- Share relevant log entries
- Specify AWS region and account type

---

**⚠️ Important Notes:**
- This tool is for educational and administrative purposes
- Always test in non-production environments first
- Follow your organization's security policies
- Keep AWS credentials secure and rotate regularly
- Monitor AWS costs and usage during conversions

**🎯 Goal:** Simplify the migration from IAM Users to IAM Roles while maintaining security and functionality.
