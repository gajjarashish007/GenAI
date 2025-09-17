#!/usr/bin/env python3
"""
IAM User to Role Conversion Backend Server
Provides API endpoints for converting IAM users to IAM roles
"""

import json
import boto3
import logging
import base64
from datetime import datetime
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import threading
import time

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Authentication credentials
VALID_CREDENTIALS = {
    'admin': '123@admin'
}

class IAMConversionHandler(BaseHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        self.iam_client = None
        self.sts_client = None
        self.account_id = None
        super().__init__(*args, **kwargs)

    def authenticate_request(self):
        """Check if request is authenticated (for demo purposes, we'll skip complex auth)"""
        # In a production environment, you would implement proper session management
        # For this demo, we'll allow all requests after initial login validation
        return True

    def validate_credentials(self, username, password):
        """Validate login credentials"""
        return username in VALID_CREDENTIALS and VALID_CREDENTIALS[username] == password

    def do_GET(self):
        """Handle GET requests"""
        parsed_path = urlparse(self.path)
        path = parsed_path.path
        
        try:
            if path == '/':
                self.serve_html()
            elif path == '/api/status':
                self.handle_status()
            elif path == '/api/users':
                self.handle_get_users()
            elif path.startswith('/api/users/') and path.endswith('/details'):
                username = path.split('/')[-2]
                self.handle_get_user_details(username)
            else:
                self.send_error(404, "Not Found")
        except Exception as e:
            logger.error(f"Error handling GET request: {str(e)}")
            self.send_json_response({'error': str(e)}, 500)

    def do_POST(self):
        """Handle POST requests"""
        parsed_path = urlparse(self.path)
        path = parsed_path.path
        
        try:
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))
            
            if path == '/api/login':
                self.handle_login(data)
            elif path == '/api/create-role':
                self.handle_create_role(data)
            elif path == '/api/attach-policies':
                self.handle_attach_policies(data)
            else:
                self.send_error(404, "Not Found")
        except Exception as e:
            logger.error(f"Error handling POST request: {str(e)}")
            self.send_json_response({'error': str(e)}, 500)

    def handle_login(self, data):
        """Handle login authentication"""
        try:
            username = data.get('username', '').strip()
            password = data.get('password', '')
            
            if self.validate_credentials(username, password):
                logger.info(f"Successful login for user: {username}")
                self.send_json_response({
                    'success': True,
                    'message': 'Authentication successful',
                    'user': username
                })
            else:
                logger.warning(f"Failed login attempt for user: {username}")
                self.send_json_response({
                    'success': False,
                    'message': 'Invalid credentials'
                }, 401)
                
        except Exception as e:
            logger.error(f"Login error: {str(e)}")
            self.send_json_response({'error': str(e)}, 500)

    def serve_html(self):
        """Serve the main HTML file"""
        try:
            with open('/home/ubuntu/iam_create_role/iam_user_to_role.html', 'r') as f:
                content = f.read()
            
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(content.encode())
        except FileNotFoundError:
            self.send_error(404, "HTML file not found")

    def handle_status(self):
        """Check AWS connection status"""
        try:
            if not self.sts_client:
                self.sts_client = boto3.client('sts')
            
            response = self.sts_client.get_caller_identity()
            self.account_id = response['Account']
            
            self.send_json_response({
                'status': 'connected',
                'account_id': self.account_id,
                'user_arn': response.get('Arn', 'Unknown')
            })
        except Exception as e:
            logger.error(f"AWS connection failed: {str(e)}")
            self.send_json_response({
                'status': 'disconnected',
                'error': str(e)
            })

    def handle_get_users(self):
        """Get all IAM users"""
        try:
            if not self.iam_client:
                self.iam_client = boto3.client('iam')
            
            users = []
            paginator = self.iam_client.get_paginator('list_users')
            
            for page in paginator.paginate():
                for user in page['Users']:
                    # Get basic user info
                    user_info = {
                        'UserName': user['UserName'],
                        'UserId': user['UserId'],
                        'Arn': user['Arn'],
                        'CreateDate': user['CreateDate'].isoformat(),
                        'Path': user['Path']
                    }
                    
                    # Get attached policies count
                    try:
                        attached_policies = self.iam_client.list_attached_user_policies(
                            UserName=user['UserName']
                        )
                        user_info['AttachedPolicies'] = attached_policies['AttachedPolicies']
                    except Exception as e:
                        logger.warning(f"Failed to get attached policies for {user['UserName']}: {str(e)}")
                        user_info['AttachedPolicies'] = []
                    
                    # Get inline policies count
                    try:
                        inline_policies = self.iam_client.list_user_policies(
                            UserName=user['UserName']
                        )
                        user_info['InlinePolicies'] = inline_policies['PolicyNames']
                    except Exception as e:
                        logger.warning(f"Failed to get inline policies for {user['UserName']}: {str(e)}")
                        user_info['InlinePolicies'] = []
                    
                    users.append(user_info)
            
            self.send_json_response({'users': users})
            logger.info(f"Retrieved {len(users)} IAM users")
            
        except Exception as e:
            logger.error(f"Failed to get users: {str(e)}")
            self.send_json_response({'error': str(e)}, 500)

    def handle_get_user_details(self, username):
        """Get detailed information about a specific user"""
        try:
            if not self.iam_client:
                self.iam_client = boto3.client('iam')
            
            user_details = {'policies': []}
            
            # Get attached managed policies
            try:
                attached_policies = self.iam_client.list_attached_user_policies(
                    UserName=username
                )
                
                for policy in attached_policies['AttachedPolicies']:
                    # Get policy version details
                    try:
                        policy_details = self.iam_client.get_policy(
                            PolicyArn=policy['PolicyArn']
                        )
                        
                        policy_version = self.iam_client.get_policy_version(
                            PolicyArn=policy['PolicyArn'],
                            VersionId=policy_details['Policy']['DefaultVersionId']
                        )
                        
                        user_details['policies'].append({
                            'PolicyName': policy['PolicyName'],
                            'PolicyArn': policy['PolicyArn'],
                            'Type': 'Managed',
                            'Document': policy_version['PolicyVersion']['Document']
                        })
                    except Exception as e:
                        logger.warning(f"Failed to get policy details for {policy['PolicyName']}: {str(e)}")
                        user_details['policies'].append({
                            'PolicyName': policy['PolicyName'],
                            'PolicyArn': policy['PolicyArn'],
                            'Type': 'Managed',
                            'Document': None,
                            'Error': str(e)
                        })
                        
            except Exception as e:
                logger.warning(f"Failed to get attached policies for {username}: {str(e)}")
            
            # Get inline policies
            try:
                inline_policies = self.iam_client.list_user_policies(
                    UserName=username
                )
                
                for policy_name in inline_policies['PolicyNames']:
                    try:
                        policy_document = self.iam_client.get_user_policy(
                            UserName=username,
                            PolicyName=policy_name
                        )
                        
                        user_details['policies'].append({
                            'PolicyName': policy_name,
                            'Type': 'Inline',
                            'Document': policy_document['PolicyDocument']
                        })
                    except Exception as e:
                        logger.warning(f"Failed to get inline policy {policy_name}: {str(e)}")
                        user_details['policies'].append({
                            'PolicyName': policy_name,
                            'Type': 'Inline',
                            'Document': None,
                            'Error': str(e)
                        })
                        
            except Exception as e:
                logger.warning(f"Failed to get inline policies for {username}: {str(e)}")
            
            # Get user groups
            try:
                groups = self.iam_client.get_groups_for_user(UserName=username)
                user_details['groups'] = [group['GroupName'] for group in groups['Groups']]
            except Exception as e:
                logger.warning(f"Failed to get groups for {username}: {str(e)}")
                user_details['groups'] = []
            
            self.send_json_response(user_details)
            logger.info(f"Retrieved details for user {username}")
            
        except Exception as e:
            logger.error(f"Failed to get user details for {username}: {str(e)}")
            self.send_json_response({'error': str(e)}, 500)

    def handle_create_role(self, data):
        """Create IAM role with trust policy"""
        try:
            if not self.iam_client:
                self.iam_client = boto3.client('iam')
            
            role_name = data['roleName']
            trust_policy = data['trustPolicy']
            description = data.get('roleDescription', '')
            
            # Create the role
            create_role_params = {
                'RoleName': role_name,
                'AssumeRolePolicyDocument': json.dumps(trust_policy),
                'Path': '/',
            }
            
            if description:
                create_role_params['Description'] = description
            
            response = self.iam_client.create_role(**create_role_params)
            
            logger.info(f"Created IAM role: {role_name}")
            self.send_json_response({
                'success': True,
                'role_arn': response['Role']['Arn'],
                'role_name': role_name
            })
            
        except self.iam_client.exceptions.EntityAlreadyExistsException:
            error_msg = f"Role {data['roleName']} already exists"
            logger.error(error_msg)
            self.send_json_response({'error': error_msg}, 409)
        except Exception as e:
            logger.error(f"Failed to create role: {str(e)}")
            self.send_json_response({'error': str(e)}, 500)

    def handle_attach_policies(self, data):
        """Attach policies to the created role"""
        try:
            if not self.iam_client:
                self.iam_client = boto3.client('iam')
            
            role_name = data['roleName']
            policies = data['policies']
            
            attached_policies = []
            failed_policies = []
            
            for policy in policies:
                try:
                    if policy['Type'] == 'Managed':
                        # Attach managed policy
                        self.iam_client.attach_role_policy(
                            RoleName=role_name,
                            PolicyArn=policy['PolicyArn']
                        )
                        attached_policies.append({
                            'name': policy['PolicyName'],
                            'type': 'Managed',
                            'arn': policy['PolicyArn']
                        })
                        
                    elif policy['Type'] == 'Inline':
                        # Create inline policy for role
                        if policy.get('Document'):
                            self.iam_client.put_role_policy(
                                RoleName=role_name,
                                PolicyName=policy['PolicyName'],
                                PolicyDocument=json.dumps(policy['Document'])
                            )
                            attached_policies.append({
                                'name': policy['PolicyName'],
                                'type': 'Inline'
                            })
                        else:
                            failed_policies.append({
                                'name': policy['PolicyName'],
                                'error': 'No policy document available'
                            })
                            
                except Exception as e:
                    logger.warning(f"Failed to attach policy {policy['PolicyName']}: {str(e)}")
                    failed_policies.append({
                        'name': policy['PolicyName'],
                        'error': str(e)
                    })
            
            logger.info(f"Attached {len(attached_policies)} policies to role {role_name}")
            
            self.send_json_response({
                'success': True,
                'attached_policies': attached_policies,
                'failed_policies': failed_policies,
                'summary': f"Successfully attached {len(attached_policies)} policies"
            })
            
        except Exception as e:
            logger.error(f"Failed to attach policies: {str(e)}")
            self.send_json_response({'error': str(e)}, 500)

    def send_json_response(self, data, status_code=200):
        """Send JSON response"""
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
        
        response_json = json.dumps(data, indent=2, default=str)
        self.wfile.write(response_json.encode())

    def do_OPTIONS(self):
        """Handle CORS preflight requests"""
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def log_message(self, format, *args):
        """Override to use our logger"""
        logger.info(f"{self.address_string()} - {format % args}")

def start_server(port=8081):
    """Start the HTTP server"""
    server_address = ('', port)
    httpd = HTTPServer(server_address, IAMConversionHandler)
    
    logger.info(f"Starting IAM Conversion Server on port {port}")
    logger.info(f"Open your browser to: http://localhost:{port}")
    logger.info("Press Ctrl+C to stop the server")
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        logger.info("Server stopped by user")
        httpd.server_close()

if __name__ == '__main__':
    # Check AWS credentials
    try:
        sts = boto3.client('sts')
        identity = sts.get_caller_identity()
        logger.info(f"AWS credentials configured for account: {identity['Account']}")
        logger.info(f"User/Role ARN: {identity['Arn']}")
    except Exception as e:
        logger.error(f"AWS credentials not configured properly: {str(e)}")
        logger.error("Please run 'aws configure' or set environment variables")
        exit(1)
    
    # Start server
    start_server()
