# AWS account management

**pre-step:** write down the account number in a place where you will not forget it!

##  Setting Up AWS Multi-Factor Authentication (MFA) and AWS CLI

## 1. Enable Multi-Factor Authentication (MFA) for AWS Console Login

### Step 1: Log in to AWS Management Console
- Open your web browser and go to [AWS Management Console](https://aws.amazon.com/console/).
- Log in using your AWS account credentials.

### Step 2: Navigate to IAM (Identity and Access Management)
- In the AWS Management Console, type "IAM" in the search bar and select **IAM**.
- On the left-hand side, click on **Users**.

### Step 3: Select Your User
- Find your username in the list of IAM users and click on it.
- This will take you to the **User Details** page.

### Step 4: Set Up MFA
- Under the **Security Credentials** tab, locate the **Multi-Factor Authentication (MFA)** section.
- Click on the **Manage** button.

### Step 5: Choose MFA Device
- Select the type of MFA device you want to use. The most common option is **Virtual MFA device**.
- Click **Next**.

### Step 6: Configure MFA Device
- Follow the instructions to configure your MFA device. If you chose **Virtual MFA device**, you would need to:
  1. Install a compatible app like Google Authenticator or Authy on your smartphone.
  2. Scan the QR code shown on the screen with your app.
  3. Enter the two consecutive MFA codes displayed by your app to complete the setup.

### Step 7: Finish MFA Setup
- After successfully entering the MFA codes, click **Assign MFA**.
- Your MFA setup is now complete.

### Step 8: Test MFA
- Log out of the AWS Management Console and log back in.
- You should be prompted to enter an MFA code from your device.

## 2. Install the AWS Command Line Interface (CLI)

### Step 1: Install AWS CLI via Homebrew (for macOS)
- If you're using macOS, the easiest way to install the AWS CLI is via Homebrew.
- Open your Terminal application.
- Run the following command to install Homebrew if you don't have it installed:
  ```bash
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
  ```
- Once Homebrew is installed, run the following command to install the AWS CLI:
  ```bash
  brew install awscli
  ```

### Step 2: Verify AWS CLI Installation
- After installation, you can verify the installation by running:
  ```bash
  aws --version
  ```
- This command should output the version number of the AWS CLI that you have installed.

### Step 3: Configure the AWS CLI
- To configure the AWS CLI with your credentials, run:
  ```bash
  aws configure
  ```
- You will be prompted to enter:
  - **AWS Access Key ID**
  - **AWS Secret Access Key**
  - **Default region name** (e.g., `us-west-2`)
  - **Default output format** (optional, e.g., `json`)

### Step 4: Test Your Configuration
- Test that your AWS CLI is configured correctly by running:
  ```bash
  aws sts get-caller-identity
  ```
- This command should return your AWS account details.

---


## AWS Profiles


Certainly! Here's an educational explanation and step-by-step guide on what an AWS profile is, the difference between using an AWS Secret Access Key directly versus using a profile, and how to set up and use an AWS profile for authentication in tools like AWS Amplify.

---

# Understanding AWS Profiles

## What is an AWS Profile?

An **AWS Profile** is a named set of configuration settings and credentials that you can store locally on your computer to interact with AWS services. Profiles allow you to manage multiple sets of credentials for different AWS accounts or roles and switch between them easily.

### Why Use an AWS Profile?

1. **Security**: Instead of embedding your AWS Access Key ID and Secret Access Key directly into your scripts or tools, you can reference a profile by name, which securely stores these credentials in a configuration file.

2. **Convenience**: If you work with multiple AWS accounts or roles, profiles let you quickly switch between them without manually entering credentials each time.

3. **Environment Separation**: Profiles can be used to separate credentials for different environments, such as development, staging, and production.

## Authenticating with AWS Access Keys vs. AWS Profiles

### Authenticating Directly with AWS Access Keys

When you authenticate directly using an **AWS Access Key ID** and **Secret Access Key**, you pass these credentials directly to the AWS CLI, SDKs, or other tools. This can be done through environment variables or directly within your code.

**Example using environment variables:**
```bash
export AWS_ACCESS_KEY_ID=your_access_key_id
export AWS_SECRET_ACCESS_KEY=your_secret_access_key
```

**Drawbacks:**
- **Security Risk**: Your credentials might be exposed in your environment or code.
- **Inconvenience**: Managing multiple sets of credentials becomes cumbersome.
- **Harder to Rotate**: It's more challenging to rotate keys securely and ensure all systems are updated.

### Authenticating with an AWS Profile

With a **profile**, you store your Access Key ID and Secret Access Key in a file on your computer. You can then reference this profile by name in your tools and scripts, making it easier and safer to manage your credentials.

**Example using a profile:**
```bash
aws configure --profile your-profile-name
```

**Benefits:**
- **Security**: Credentials are stored securely in a file, and you only reference the profile name.
- **Ease of Use**: Switch between different accounts and roles by changing the profile name.
- **Separation of Concerns**: Different profiles can be used for different environments (e.g., dev, prod).

## How to Set Up an AWS Profile

### Step 1: Configure Your Profile

You can create and configure a profile using the AWS CLI with the following command:

```bash
aws configure --profile your-profile-name
```

You’ll be prompted to enter the following information:

1. **AWS Access Key ID**: Enter your access key ID.
2. **AWS Secret Access Key**: Enter your secret access key.
3. **Default region name**: Enter the region you want to default to (e.g., `us-west-2`).
4. **Default output format**: Choose the output format (optional, e.g., `json`).

### Step 2: Verify Your Profile

To verify that your profile is set up correctly, you can list all your configured profiles:

```bash
aws configure list-profiles
```

You can also test the profile by running a command that requires authentication:

```bash
aws sts get-caller-identity --profile your-profile-name
```

This command will return the account details associated with that profile.

### Step 3: Use Your Profile in AWS Amplify or Other Tools

When initializing a system like AWS Amplify, you can specify the profile you want to use:

```bash
amplify configure --profile your-profile-name
```

Or when running any AWS CLI command, specify the profile like this:

```bash
aws s3 ls --profile your-profile-name
```

### Step 4: Reference the Profile in Your Scripts

In your scripts or applications, you can reference the profile rather than hard-coding your credentials:

- For AWS CLI: `--profile your-profile-name`
- For AWS SDKs: Most AWS SDKs (like the ones for Python, JavaScript, etc.) automatically use profiles stored in your configuration file.

### Where Are Profiles Stored?

AWS profiles are stored in two files on your local machine:

1. **Credentials File** (`~/.aws/credentials`): Stores the Access Key ID and Secret Access Key.
2. **Config File** (`~/.aws/config`): Stores region and output format settings.

You can manually edit these files to add or update profiles if needed.

---

By using an AWS profile, your protégé can manage her credentials more securely and conveniently, which is especially useful when working with multiple AWS accounts or environments. This approach will also help her to avoid directly exposing her AWS Access Key ID and Secret Access Key in her scripts or tools like AWS Amplify. 

Let me know if there's anything more you'd like to include or clarify!


##  Additional Amplify setup 

Installing the AWS CLI does not automatically set up the user to use AWS Amplify. AWS Amplify requires additional setup beyond just having the AWS CLI installed. Here's what your protégé will need to do to set up AWS Amplify:

### 1. Install the Amplify CLI
The AWS Amplify CLI is a separate command-line tool that you need to install to work with AWS Amplify.

- Install Node.js: Amplify CLI requires Node.js. If you don't have it installed, you can install it via Homebrew on macOS:
  ```bash
  brew install node
  ```

- Install the Amplify CLI globally using npm (which comes with Node.js):
  ```bash
  npm install -g @aws-amplify/cli
  ```

### 2. Configure the Amplify CLI
After installing the Amplify CLI, you need to configure it with your AWS credentials.

- Run the following command to configure Amplify:
  ```bash
  amplify configure
  ```

- Follow the prompts to sign in to your AWS account and set up the CLI:
  1. It will prompt you to specify a region.
  2. Then, it will ask for an IAM user to use with Amplify. You can either use an existing user or create a new one with the required permissions.
  3. The CLI will then save the configuration and link it to your AWS account.

### 3. Initialize a New Amplify Project (Optional)
If your protégé is starting a new project, they can initialize an Amplify project in their directory:

- Navigate to the root of the project directory in the terminal:
  ```bash
  cd path/to/your/project
  ```

- Run the following command to initialize Amplify in the project:
  ```bash
  amplify init
  ```

- Follow the prompts to configure your project. This will set up the necessary AWS resources and link them to your project.

### 4. Add Amplify Features (Optional)
After initializing the project, you can add specific Amplify categories like authentication, API, storage, etc., using the Amplify CLI commands, such as:

- To add authentication:
  ```bash
  amplify add auth
  ```

- To add an API:
  ```bash
  amplify add api
  ```

### 5. Deploy the Amplify Project
Once you’ve configured your Amplify project, you can deploy it to AWS:

- Run the following command to push your changes to the cloud:
  ```bash
  amplify push
  ```

This command provisions all the necessary AWS resources and deploys your application.

### Summary
While the AWS CLI is necessary for interacting with AWS services, the Amplify CLI is specifically designed for AWS Amplify projects and requires its installation and setup. The above steps outline how to get started with Amplify after the AWS CLI is installed.

Let me know if you'd like any further details or modifications!Rob